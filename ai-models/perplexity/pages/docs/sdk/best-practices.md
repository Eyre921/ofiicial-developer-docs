---
title: "Best Practices"
source: https://docs.perplexity.ai/docs/sdk/best-practices
path: docs/sdk/best-practices
---

Learn best practices for using the Perplexity SDKs in production, including environment variables, rate limiting, security, and efficient request patterns.

## Overview

This guide covers essential best practices for using the Perplexity SDKs in production environments. Following these practices will help you build robust, secure, and efficient applications.

## Security Best Practices

### Environment Variables

Always store API keys securely using environment variables:

<Steps>
  <Step title="Use environment variables">
    Store API keys in environment variables, never in source code.

    <CodeGroup>
      ```python Python theme={null}
      import os
      from perplexity import Perplexity

      # Good: Use environment variables
      client = Perplexity(
          api_key=os.environ.get("PERPLEXITY_API_KEY")
      )

      # Bad: Never hardcode API keys
      # client = Perplexity(api_key="pplx-abc123...")  # DON'T DO THIS
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Good: Use environment variables
      const client = new Perplexity({
          apiKey: process.env.PERPLEXITY_API_KEY
      });

      // Bad: Never hardcode API keys
      // const client = new Perplexity({
      //     apiKey: "pplx-abc123..."  // DON'T DO THIS
      // });
      ```
    </CodeGroup>

    <Warning>
      Never commit API keys to version control. Use .env files locally and secure environment variable management in production.
    </Warning>
  </Step>

  <Step title="Use .env files for local development">
    Create a `.env` file for local development (add it to .gitignore):

    ```bash theme={null}
    cat > .env << 'EOF'
    PERPLEXITY_API_KEY=your_api_key_here
    PERPLEXITY_MAX_RETRIES=3
    PERPLEXITY_TIMEOUT=30000
    EOF
    ```

    <CodeGroup>
      ```python Python theme={null}
      from dotenv import load_dotenv
      import os
      from perplexity import Perplexity

      # Load environment variables from .env file
      load_dotenv()

      client = Perplexity(
          api_key=os.getenv("PERPLEXITY_API_KEY"),
          max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3"))
      )
      ```

      ```typescript TypeScript theme={null}
      import dotenv from 'dotenv';
      import Perplexity from '@perplexity-ai/perplexity_ai';

      // Load environment variables from .env file
      dotenv.config();

      const client = new Perplexity({
          apiKey: process.env.PERPLEXITY_API_KEY,
          maxRetries: parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3')
      });
      ```
    </CodeGroup>
  </Step>

  <Step title="Validate environment variables">
    Check for required environment variables at startup.

    <CodeGroup>
      ```python Python theme={null}
      import os
      import sys
      from perplexity import Perplexity

      def create_client():
          api_key = os.getenv("PERPLEXITY_API_KEY")
          if not api_key:
              print("Error: PERPLEXITY_API_KEY environment variable is required")
              sys.exit(1)
          
          return Perplexity(api_key=api_key)

      client = create_client()
      ```

      ```typescript TypeScript theme={null}
      import Perplexity from '@perplexity-ai/perplexity_ai';

      function createClient(): Perplexity {
          const apiKey = process.env.PERPLEXITY_API_KEY;
          if (!apiKey) {
              console.error("Error: PERPLEXITY_API_KEY environment variable is required");
              process.exit(1);
          }
          
          return new Perplexity({ apiKey });
      }

      const client = createClient();
      ```
    </CodeGroup>
  </Step>
</Steps>

### API Key Rotation

Implement secure API key rotation:

<CodeGroup>
  ```python Python theme={null}
  import os
  import logging
  from perplexity import Perplexity
  from typing import Optional

  class SecurePerplexityClient:
      def __init__(self, primary_key: Optional[str] = None, fallback_key: Optional[str] = None):
          self.primary_key = primary_key or os.getenv("PERPLEXITY_API_KEY")
          self.fallback_key = fallback_key or os.getenv("PERPLEXITY_API_KEY_FALLBACK")
          self.current_client = Perplexity(api_key=self.primary_key)
          self.logger = logging.getLogger(__name__)
      
      def _switch_to_fallback(self):
          """Switch to fallback API key if available"""
          if self.fallback_key:
              self.logger.warning("Switching to fallback API key")
              self.current_client = Perplexity(api_key=self.fallback_key)
              return True
          return False
      
      def search(self, query: str, **kwargs):
          try:
              return self.current_client.search.create(query=query, **kwargs)
          except Exception as e:
              if "authentication" in str(e).lower() and self._switch_to_fallback():
                  return self.current_client.search.create(query=query, **kwargs)
              raise e

  # Usage
  client = SecurePerplexityClient()
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class SecurePerplexityClient {
      private primaryKey: string;
      private fallbackKey?: string;
      private currentClient: Perplexity;
      
      constructor(primaryKey?: string, fallbackKey?: string) {
          this.primaryKey = primaryKey || process.env.PERPLEXITY_API_KEY!;
          this.fallbackKey = fallbackKey || process.env.PERPLEXITY_API_KEY_FALLBACK;
          this.currentClient = new Perplexity({ apiKey: this.primaryKey });
      }
      
      private switchToFallback(): boolean {
          if (this.fallbackKey) {
              console.warn("Switching to fallback API key");
              this.currentClient = new Perplexity({ apiKey: this.fallbackKey });
              return true;
          }
          return false;
      }
      
      async search(query: string, options?: any) {
          try {
              return await this.currentClient.search.create({ query, ...options });
          } catch (error: any) {
              if (error.message.toLowerCase().includes('authentication') && this.switchToFallback()) {
                  return await this.currentClient.search.create({ query, ...options });
              }
              throw error;
          }
      }
  }

  // Usage
  const client = new SecurePerplexityClient();
  ```
</CodeGroup>

## Rate Limiting and Efficiency

### Intelligent Rate Limiting

Implement exponential backoff with jitter:

<CodeGroup>
  ```python Python theme={null}
  import time
  import random
  import asyncio
  from typing import TypeVar, Callable, Any
  import perplexity
  from perplexity import Perplexity

  T = TypeVar('T')

  class RateLimitedClient:
      def __init__(self, client: Perplexity, max_retries: int = 5):
          self.client = client
          self.max_retries = max_retries
      
      def _calculate_delay(self, attempt: int) -> float:
          """Calculate delay with exponential backoff and jitter"""
          base_delay = 2 ** attempt
          jitter = random.uniform(0.1, 0.5)
          return min(base_delay + jitter, 60.0)  # Cap at 60 seconds
      
      def with_retry(self, func: Callable[[], T]) -> T:
          """Execute function with intelligent retry logic"""
          last_exception = None
          
          for attempt in range(self.max_retries):
              try:
                  return func()
              except perplexity.RateLimitError as e:
                  last_exception = e
                  if attempt < self.max_retries - 1:
                      delay = self._calculate_delay(attempt)
                      print(f"Rate limited. Retrying in {delay:.2f}s (attempt {attempt + 1})")
                      time.sleep(delay)
                      continue
                  raise e
              except perplexity.APIConnectionError as e:
                  last_exception = e
                  if attempt < self.max_retries - 1:
                      delay = min(2 ** attempt, 10.0)  # Shorter delay for connection errors
                      print(f"Connection error. Retrying in {delay:.2f}s")
                      time.sleep(delay)
                      continue
                  raise e
          
          raise last_exception
      
      def search(self, query: str, **kwargs):
          return self.with_retry(
              lambda: self.client.search.create(query=query, **kwargs)
          )

  # Usage
  client = RateLimitedClient(Perplexity())
  result = client.search("artificial intelligence")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class RateLimitedClient {
      private client: Perplexity;
      private maxRetries: number;
      
      constructor(client: Perplexity, maxRetries: number = 5) {
          this.client = client;
          this.maxRetries = maxRetries;
      }
      
      private calculateDelay(attempt: number): number {
          const baseDelay = 2 ** attempt * 1000; // Convert to milliseconds
          const jitter = Math.random() * 500; // 0-500ms jitter
          return Math.min(baseDelay + jitter, 60000); // Cap at 60 seconds
      }
      
      async withRetry<T>(func: () => Promise<T>): Promise<T> {
          let lastError: any;
          
          for (let attempt = 0; attempt < this.maxRetries; attempt++) {
              try {
                  return await func();
              } catch (error: any) {
                  lastError = error;
                  
                  if (error.constructor.name === 'RateLimitError') {
                      if (attempt < this.maxRetries - 1) {
                          const delay = this.calculateDelay(attempt);
                          console.log(`Rate limited. Retrying in ${delay}ms (attempt ${attempt + 1})`);
                          await new Promise(resolve => setTimeout(resolve, delay));
                          continue;
                      }
                  } else if (error.constructor.name === 'APIConnectionError') {
                      if (attempt < this.maxRetries - 1) {
                          const delay = Math.min(2 ** attempt * 1000, 10000);
                          console.log(`Connection error. Retrying in ${delay}ms`);
                          await new Promise(resolve => setTimeout(resolve, delay));
                          continue;
                      }
                  }
                  
                  throw error;
              }
          }
          
          throw lastError;
      }
      
      async search(query: string, options?: any) {
          return this.withRetry(() => 
              this.client.search.create({ query, ...options })
          );
      }
  }

  // Usage
  const client = new RateLimitedClient(new Perplexity());
  const result = await client.search("artificial intelligence");
  ```
</CodeGroup>

### Request Batching

Efficiently batch multiple requests:

<CodeGroup>
  ```python Python theme={null}
  import asyncio
  from typing import Callable, Awaitable, List, TypeVar, Generic
  from perplexity import AsyncPerplexity, DefaultAioHttpClient

  T = TypeVar('T')

  class BatchProcessor(Generic[T]):
      def __init__(self, batch_size: int = 5, delay_between_batches: float = 1.0):
          self.batch_size = batch_size
          self.delay_between_batches = delay_between_batches
      
      async def process_batch(
          self, 
          items: List[str], 
          process_func: Callable[[str], Awaitable[T]]
      ) -> List[T]:
          """Process items in batches with rate limiting"""
          results = []
          
          for i in range(0, len(items), self.batch_size):
              batch = items[i:i + self.batch_size]
              
              # Process batch concurrently
              tasks = [process_func(item) for item in batch]
              batch_results = await asyncio.gather(*tasks, return_exceptions=True)
              
              # Filter out exceptions and collect results
              for result in batch_results:
                  if not isinstance(result, Exception):
                      results.append(result)
              
              # Delay between batches
              if i + self.batch_size < len(items):
                  await asyncio.sleep(self.delay_between_batches)
          
          return results

  # Usage
  async def main():
      processor = BatchProcessor(batch_size=3, delay_between_batches=0.5)
      
      async with AsyncPerplexity(
          http_client=DefaultAioHttpClient()
      ) as client:
          
          async def search_query(query: str):
              return await client.search.create(query=query)
          
          queries = ["AI", "ML", "DL", "NLP", "CV"]
          results = await processor.process_batch(queries, search_query)
          
          print(f"Processed {len(results)} successful queries")

  asyncio.run(main())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  class BatchProcessor<T> {
      constructor(
          private batchSize: number = 5,
          private delayBetweenBatches: number = 1000
      ) {}
      
      async processBatch<R>(
          items: T[],
          processFunc: (item: T) => Promise<R>
      ): Promise<R[]> {
          const results: R[] = [];
          
          for (let i = 0; i < items.length; i += this.batchSize) {
              const batch = items.slice(i, i + this.batchSize);
              
              // Process batch concurrently
              const tasks = batch.map(item => 
                  processFunc(item).catch(error => error)
              );
              const batchResults = await Promise.all(tasks);
              
              // Filter out exceptions and collect results
              for (const result of batchResults) {
                  if (!(result instanceof Error)) {
                      results.push(result);
                  }
              }
              
              // Delay between batches
              if (i + this.batchSize < items.length) {
                  await new Promise(resolve => 
                      setTimeout(resolve, this.delayBetweenBatches)
                  );
              }
          }
          
          return results;
      }
  }

  // Usage
  async function main() {
      const processor = new BatchProcessor<string>(3, 500);
      const client = new Perplexity();
      
      const searchQuery = (query: string) => 
          client.search.create({ query });
      
      const queries = ["AI", "ML", "DL", "NLP", "CV"];
      const results = await processor.processBatch(queries, searchQuery);
      
      console.log(`Processed ${results.length} successful queries`);
  }

  main();
  ```
</CodeGroup>

## Production Configuration

### Configuration Management

Use environment-based configuration for different deployment stages:

<CodeGroup>
  ```python Python theme={null}
  import os
  from dataclasses import dataclass
  from typing import Optional
  import httpx
  from perplexity import Perplexity, DefaultHttpxClient

  @dataclass
  class PerplexityConfig:
      api_key: str
      max_retries: int = 3
      timeout_seconds: float = 30.0
      max_connections: int = 100
      max_keepalive: int = 20
      environment: str = "production"
      
      @classmethod
      def from_env(cls) -> "PerplexityConfig":
          """Load configuration from environment variables"""
          api_key = os.getenv("PERPLEXITY_API_KEY")
          if not api_key:
              raise ValueError("PERPLEXITY_API_KEY environment variable is required")
          
          return cls(
              api_key=api_key,
              max_retries=int(os.getenv("PERPLEXITY_MAX_RETRIES", "3")),
              timeout_seconds=float(os.getenv("PERPLEXITY_TIMEOUT", "30.0")),
              max_connections=int(os.getenv("PERPLEXITY_MAX_CONNECTIONS", "100")),
              max_keepalive=int(os.getenv("PERPLEXITY_MAX_KEEPALIVE", "20")),
              environment=os.getenv("ENVIRONMENT", "production")
          )
      
      def create_client(self) -> Perplexity:
          """Create optimized client based on configuration"""
          timeout = httpx.Timeout(
              connect=5.0,
              read=self.timeout_seconds,
              write=10.0,
              pool=10.0
          )
          
          limits = httpx.Limits(
              max_keepalive_connections=self.max_keepalive,
              max_connections=self.max_connections,
              keepalive_expiry=60.0 if self.environment == "production" else 30.0
          )
          
          return Perplexity(
              api_key=self.api_key,
              max_retries=self.max_retries,
              timeout=timeout,
              http_client=DefaultHttpxClient(limits=limits)
          )

  # Usage
  config = PerplexityConfig.from_env()
  client = config.create_client()
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';
  import https from 'https';

  interface PerplexityConfig {
      apiKey: string;
      maxRetries: number;
      timeoutMs: number;
      maxConnections: number;
      maxKeepalive: number;
      environment: string;
  }

  class ConfigManager {
      static fromEnv(): PerplexityConfig {
          const apiKey = process.env.PERPLEXITY_API_KEY;
          if (!apiKey) {
              throw new Error("PERPLEXITY_API_KEY environment variable is required");
          }
          
          return {
              apiKey,
              maxRetries: parseInt(process.env.PERPLEXITY_MAX_RETRIES || '3'),
              timeoutMs: parseInt(process.env.PERPLEXITY_TIMEOUT || '30000'),
              maxConnections: parseInt(process.env.PERPLEXITY_MAX_CONNECTIONS || '100'),
              maxKeepalive: parseInt(process.env.PERPLEXITY_MAX_KEEPALIVE || '20'),
              environment: process.env.NODE_ENV || 'production'
          };
      }
      
      static createClient(config: PerplexityConfig): Perplexity {
          const httpsAgent = new https.Agent({
              keepAlive: true,
              keepAliveMsecs: config.environment === 'production' ? 60000 : 30000,
              maxSockets: config.maxConnections,
              maxFreeSockets: config.maxKeepalive,
              timeout: config.timeoutMs
          });
          
          return new Perplexity({
              apiKey: config.apiKey,
              maxRetries: config.maxRetries,
              timeout: config.timeoutMs,
              httpAgent: httpsAgent
          } as any);
      }
  }

  // Usage
  const config = ConfigManager.fromEnv();
  const client = ConfigManager.createClient(config);
  ```
</CodeGroup>

### Monitoring and Logging

Implement comprehensive monitoring:

<CodeGroup>
  ```python Python theme={null}
  import logging
  import time
  import functools
  from typing import Any, Callable
  from perplexity import Perplexity
  import perplexity

  # Configure logging
  logging.basicConfig(
      level=logging.INFO,
      format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
  )
  logger = logging.getLogger(__name__)

  class MonitoredPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
          self.request_count = 0
          self.error_count = 0
          self.total_response_time = 0.0
      
      def _log_request(self, method: str, **kwargs):
          """Log request details"""
          self.request_count += 1
          logger.info(f"Making {method} request #{self.request_count}")
          logger.debug(f"Request parameters: {kwargs}")
      
      def _log_response(self, method: str, duration: float, success: bool = True):
          """Log response details"""
          self.total_response_time += duration
          avg_response_time = self.total_response_time / self.request_count
          
          if success:
              logger.info(f"{method} completed in {duration:.2f}s (avg: {avg_response_time:.2f}s)")
          else:
              self.error_count += 1
              logger.error(f"{method} failed after {duration:.2f}s (errors: {self.error_count})")
      
      def search(self, query: str, **kwargs):
          self._log_request("search", query=query, **kwargs)
          start_time = time.time()
          
          try:
              result = self.client.search.create(query=query, **kwargs)
              duration = time.time() - start_time
              self._log_response("search", duration, success=True)
              return result
          except Exception as e:
              duration = time.time() - start_time
              self._log_response("search", duration, success=False)
              logger.error(f"Search error: {type(e).__name__}: {e}")
              raise
      
      def get_stats(self):
          """Get client statistics"""
          return {
              "total_requests": self.request_count,
              "error_count": self.error_count,
              "success_rate": (self.request_count - self.error_count) / max(self.request_count, 1),
              "avg_response_time": self.total_response_time / max(self.request_count, 1)
          }

  # Usage
  client = MonitoredPerplexityClient(Perplexity())
  result = client.search("machine learning")
  print(client.get_stats())
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface ClientStats {
      totalRequests: number;
      errorCount: number;
      successRate: number;
      avgResponseTime: number;
  }

  class MonitoredPerplexityClient {
      private client: Perplexity;
      private requestCount: number = 0;
      private errorCount: number = 0;
      private totalResponseTime: number = 0;
      
      constructor(client: Perplexity) {
          this.client = client;
      }
      
      private logRequest(method: string, params: any): void {
          this.requestCount++;
          console.log(`Making ${method} request #${this.requestCount}`);
          console.debug(`Request parameters:`, params);
      }
      
      private logResponse(method: string, duration: number, success: boolean = true): void {
          this.totalResponseTime += duration;
          const avgResponseTime = this.totalResponseTime / this.requestCount;
          
          if (success) {
              console.log(`${method} completed in ${duration.toFixed(2)}ms (avg: ${avgResponseTime.toFixed(2)}ms)`);
          } else {
              this.errorCount++;
              console.error(`${method} failed after ${duration.toFixed(2)}ms (errors: ${this.errorCount})`);
          }
      }
      
      async search(query: string, options?: any) {
          this.logRequest("search", { query, ...options });
          const startTime = performance.now();
          
          try {
              const result = await this.client.search.create({ query, ...options });
              const duration = performance.now() - startTime;
              this.logResponse("search", duration, true);
              return result;
          } catch (error) {
              const duration = performance.now() - startTime;
              this.logResponse("search", duration, false);
              console.error(`Search error: ${error}`);
              throw error;
          }
      }
      
      getStats(): ClientStats {
          return {
              totalRequests: this.requestCount,
              errorCount: this.errorCount,
              successRate: (this.requestCount - this.errorCount) / Math.max(this.requestCount, 1),
              avgResponseTime: this.totalResponseTime / Math.max(this.requestCount, 1)
          };
      }
  }

  // Usage
  const client = new MonitoredPerplexityClient(new Perplexity());
  const result = await client.search("machine learning");
  console.log(client.getStats());
  ```
</CodeGroup>

## Error Handling Best Practices

### Graceful Degradation

Implement fallback strategies for different error types:

<CodeGroup>
  ```python Python theme={null}
  from typing import Optional, Dict, Any
  import perplexity
  from perplexity import Perplexity

  class ResilientPerplexityClient:
      def __init__(self, client: Perplexity):
          self.client = client
          self.circuit_breaker_threshold = 5
          self.circuit_breaker_count = 0
          self.circuit_breaker_open = False
      
      def _should_circuit_break(self) -> bool:
          """Check if circuit breaker should be triggered"""
          return self.circuit_breaker_count >= self.circuit_breaker_threshold
      
      def _record_failure(self):
          """Record a failure for circuit breaker"""
          self.circuit_breaker_count += 1
          if self._should_circuit_break():
              self.circuit_breaker_open = True
              print("Circuit breaker activated - temporarily disabling API calls")
      
      def _record_success(self):
          """Record a success - reset circuit breaker"""
          self.circuit_breaker_count = 0
          self.circuit_breaker_open = False
      
      def search_with_fallback(
          self, 
          query: str, 
          fallback_response: Optional[Dict[str, Any]] = None
      ):
          """Search with graceful degradation"""
          if self.circuit_breaker_open:
              print("Circuit breaker open - returning fallback response")
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "service_unavailable"
              }
          
          try:
              result = self.client.search.create(query=query)
              self._record_success()
              return result
              
          except perplexity.RateLimitError:
              print("Rate limited - implementing backoff strategy")
              # Could implement intelligent backoff here
              raise
              
          except perplexity.APIConnectionError as e:
              print(f"Connection error: {e}")
              self._record_failure()
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "connection_error"
              }
              
          except Exception as e:
              print(f"Unexpected error: {e}")
              self._record_failure()
              return fallback_response or {
                  "query": query,
                  "results": [],
                  "status": "error"
              }

  # Usage
  client = ResilientPerplexityClient(Perplexity())
  result = client.search_with_fallback("machine learning")
  ```

  ```typescript TypeScript theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  interface FallbackResponse {
      query: string;
      results: any[];
      status: string;
  }

  class ResilientPerplexityClient {
      private client: Perplexity;
      private circuitBreakerThreshold: number = 5;
      private circuitBreakerCount: number = 0;
      private circuitBreakerOpen: boolean = false;
      
      constructor(client: Perplexity) {
          this.client = client;
      }
      
      private shouldCircuitBreak(): boolean {
          return this.circuitBreakerCount >= this.circuitBreakerThreshold;
      }
      
      private recordFailure(): void {
          this.circuitBreakerCount++;
          if (this.shouldCircuitBreak()) {
              this.circuitBreakerOpen = true;
              console.log("Circuit breaker activated - temporarily disabling API calls");
          }
      }
      
      private recordSuccess(): void {
          this.circuitBreakerCount = 0;
          this.circuitBreakerOpen = false;
      }
      
      async searchWithFallback(
          query: string,
          fallbackResponse?: FallbackResponse
      ): Promise<any> {
          if (this.circuitBreakerOpen) {
              console.log("Circuit breaker open - returning fallback response");
              return fallbackResponse || {
                  query,
                  results: [],
                  status: "service_unavailable"
              };
          }
          
          try {
              const result = await this.client.search.create({ query });
              this.recordSuccess();
              return result;
              
          } catch (error: any) {
              if (error.constructor.name === 'RateLimitError') {
                  console.log("Rate limited - implementing backoff strategy");
                  throw error;
              } else if (error.constructor.name === 'APIConnectionError') {
                  console.log(`Connection error: ${error.message}`);
                  this.recordFailure();
                  return fallbackResponse || {
                      query,
                      results: [],
                      status: "connection_error"
                  };
              } else {
                  console.log(`Unexpected error: ${error.message}`);
                  this.recordFailure();
                  return fallbackResponse || {
                      query,
                      results: [],
                      status: "error"
                  };
              }
          }
      }
  }

  // Usage
  const client = new ResilientPerplexityClient(new Perplexity());
  const result = await client.searchWithFallback("machine learning");
  ```
</CodeGroup>

## Testing Best Practices

### Unit Testing with Mocking

Create testable code with proper mocking:

<CodeGroup>
  ```python Python theme={null}
  import unittest
  from unittest.mock import Mock, patch
  from perplexity import Perplexity, RateLimitError
  from perplexity.types.search_create_response import SearchCreateResponse, Result

  class TestPerplexityIntegration(unittest.TestCase):
      def setUp(self):
          self.mock_client = Mock(spec=Perplexity)

      def test_search_success(self):
          # Mock successful response
          mock_result = Result(
              title="Test Result",
              url="https://example.com",
              snippet="Test snippet"
          )

          mock_response = SearchCreateResponse(
              id="search_123",
              results=[mock_result]
          )

          self.mock_client.search.create.return_value = mock_response

          # Test your application logic
          result = self.mock_client.search.create(query="Perplexity Search API rate limit and retry handling example")

          self.assertEqual(result.id, "search_123")
          self.assertEqual(len(result.results), 1)
          self.assertEqual(result.results[0].title, "Test Result")

      @patch('perplexity.Perplexity')
      def test_rate_limit_handling(self, mock_perplexity_class):
          # Mock rate limit error
          mock_client = Mock()
          mock_perplexity_class.return_value = mock_client
          mock_client.search.create.side_effect = RateLimitError(
              "Rate limited",
              response=Mock(status_code=429),
              body={}
          )

          # Test your error handling logic here
          with self.assertRaises(RateLimitError):
              mock_client.search.create(query="Perplexity Search API Python SDK quickstart example")

  if __name__ == '__main__':
      unittest.main()
  ```

  ```typescript TypeScript theme={null}
  import { jest, describe, beforeEach, test, expect } from '@jest/globals';
  import Perplexity from '@perplexity-ai/perplexity_ai';

  // Mock the Perplexity client
  jest.mock('@perplexity-ai/perplexity_ai');

  describe('Perplexity Integration', () => {
      let mockClient: any;

      beforeEach(() => {
          mockClient = new Perplexity();
      });

      test('should handle successful search', async () => {
          const mockResponse = {
              id: "search_123",
              results: [{ title: "Test Result", url: "https://example.com", snippet: "Test snippet" }]
          };

          jest.spyOn(mockClient.search, 'create').mockResolvedValue(mockResponse as any);

          const result = await mockClient.search.create({ query: "Perplexity Search API rate limit and retry handling example" });

          expect(result.id).toBe("search_123");
          expect(result.results).toHaveLength(1);
          expect(result.results[0].title).toBe("Test Result");
      });

      test('should handle rate limit errors', async () => {
          const rateLimitError = new Error('Rate limited');

          jest.spyOn(mockClient.search, 'create').mockRejectedValue(rateLimitError);

          await expect(mockClient.search.create({ query: "Perplexity Search API Python SDK quickstart example" })).rejects.toThrow('Rate limited');
      });
  });
  ```
</CodeGroup>

<AccordionGroup>
  <Accordion title="Response — Perplexity Search API rate limit and retry handling example">
    ````json theme={null}
    {
      "id": "fc4a9702-2f8c-454c-bff5-04f63041aaa7",
      "results": [
        {
          "snippet": "The SDKs provide specific exception types for different error scenarios:\n* **APIConnectionError** - Network connection issues\n* **RateLimitError** - API rate limit exceeded\n* **APIStatusError** - HTTP status errors (4xx, 5xx)\n* **AuthenticationError** - Invalid API key or authentication issues\n* **ValidationError** - Invalid request parameters\n...\nHandle common API errors with try-catch blocks:\n<CodeGroup>\n```python Python theme={null}\nimport perplexity\nfrom perplexity import Perplexity\nclient = Perplexity()\ntry:\nsearch = client.search.create(query=\"machine learning\")\nprint(search.results)\nexcept perplexity.APIConnectionError as e:\nprint(\"Network connection failed\")\nprint(e.__cause__)\nexcept perplexity.RateLimitError as e:\nprint(\"Rate limit exceeded, please retry later\")\nexcept perplexity.APIStatusError as e:\nprint(f\"API error: {e.status_code}\")\nprint(e.response)\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity();\ntry {\nconst search = await client.search.create({ query: \"machine learning\" });\nconsole.log(search.results);\n} catch (error: any) {\nif (error.constructor.name === 'APIConnectionError') {\nconsole.log(\"Network connection failed\");\nconsole.log(error.cause);\n} else if (error.constructor.name === 'RateLimitError') {\nconsole.log(\"Rate limit exceeded, please retry later\");\n} else if (error.constructor.name === 'APIStatusError') {\nconsole.log(`API error: ${error.status}`);\nconsole.log(error.response);\n}\n}\n```\n</CodeGroup>\n...\n### Exponential Backoff for Rate Limits\nImplement intelligent retry logic for rate limit errors:\n<CodeGroup>\n```python Python theme={null}\nimport time\nimport random\nimport perplexity\nfrom perplexity import Perplexity\ndef search_with_retry(client, query, max_retries=3):\nfor attempt in range(max_retries):\ntry:\nreturn client.search.create(query=query)\nexcept perplexity.RateLimitError:\nif attempt == max_retries - 1:\nraise  # Re-raise on final attempt\n# Exponential backoff with jitter\ndelay = (2 ** attempt) + random.uniform(0, 1)\nprint(f\"Rate limited. Retrying in {delay:.2f} seconds...\")\n              time.sleep(delay)\nexcept perplexity.APIConnectionError:\nif attempt == max_retries - 1:\nraise\n# Shorter delay for connection errors\ndelay = 1 + random.uniform(0, 1)\nprint(f\"Connection error. Retrying in {delay:.2f} seconds...\")\n              time.sleep(delay)\n# Usage\nclient = Perplexity()\nresult = search_with_retry(client, \"artificial intelligence\")\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nasync function searchWithRetry(\nclient: Perplexity, \n      query: string, \n      maxRetries: number = 3\n) {\nfor (let attempt = 0; attempt < maxRetries; attempt++) {\ntry {\nreturn await client.search.create({ query });\n} catch (error: any) {\nif (attempt === maxRetries - 1) {\nthrow error; // Re-throw on final attempt\n}\nif (error.constructor.name === 'RateLimitError') {\n// Exponential backoff with jitter\nconst delay = (2 ** attempt + Math.random()) * 1000;\nconsole.log(`Rate limited. Retrying in ${delay}ms...`);\nawait new Promise(resolve => setTimeout(resolve, delay));\n} else if (error.constructor.name === 'APIConnectionError') {\n// Shorter delay for connection errors\nconst delay = (1 + Math.random()) * 1000;\nconsole.log(`Connection error. Retrying in ${delay}ms...`);\nawait new Promise(resolve => setTimeout(resolve, delay));\n} else {\nthrow error; // Don't retry other errors\n}\n}\n}\n}\n// Usage\nconst client = new Perplexity();\nconst result = await searchWithRetry(client, \"artificial intelligence\");\n```\n</CodeGroup>\n...\n```python Python theme={null}\nimport perplexity\nfrom perplexity import Perplexity\nclient = Perplexity()\ntry:\nchat = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[{\"role\": \"user\", \"content\": \"What's the weather?\"}]\n)\nexcept perplexity.APIStatusError as e:\nprint(f\"Status Code: {e.status_code}\")\nprint(f\"Error Type: {e.type}\")\nprint(f\"Error Message: {e.message}\")\n# Access raw response for detailed debugging\nif hasattr(e, 'response'):\nprint(f\"Raw Response: {e.response.text}\")\nprint(f\"Request ID: {e.response.headers.get('X-Request-ID')}\")\nexcept perplexity.ValidationError as e:\nprint(f\"Validation Error: {e}\")\n# Handle parameter validation errors\nexcept Exception as e:\nprint(f\"Unexpected error: {type(e).__name__}: {e}\")\n```\n...\nImplement fallback mechanisms when API calls fail:\n<CodeGroup>\n```python Python theme={null}\nimport perplexity\nfrom perplexity import Perplexity\ndef get_ai_response(query, fallback_response=\"I'm sorry, I'm temporarily unavailable.\"):\nclient = Perplexity()\ntry:\n# Primary: Try online model\nresponse = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[{\"role\": \"user\", \"content\": query}]\n)\nreturn response.choices[0].message.content\nexcept perplexity.RateLimitError:\ntry:\n# Fallback: Try offline model if rate limited\nresponse = client.chat.completions.create(\nmodel=\"llama-3.1-8b-instruct\",\nmessages=[{\"role\": \"user\", \"content\": query}]\n)\nreturn response.choices[0].message.content\nexcept Exception:\nreturn fallback_response\nexcept perplexity.APIConnectionError:\n# Network issues - return cached response or fallback\nreturn fallback_response\nexcept Exception as e:\nprint(f\"Unexpected error: {e}\")\nreturn fallback_response\n# Usage\nresponse = get_ai_response(\"What is machine learning?\")\n...\n<Step title=\"Always handle rate limits\">\nRate limiting is common with API usage.\nAlways implement retry logic with exponential backoff.\n<Warning>\nDon't implement aggressive retry loops without delays - this can worsen rate limiting.\n...\nInclude proper logging to track error patterns and API health.\n...\nCheck for invalid API keys and provide helpful error messages.\n<CodeGroup>",
          "title": "Error Handling",
          "url": "https://docs.perplexity.ai/docs/sdk/error-handling",
          "date": null,
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "",
          "title": "Best Practices",
          "url": "https://docs.perplexity.ai/docs/search/best-practices",
          "date": null,
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "",
          "title": "Perplexity API: Setup, Models, Integration & Best Practices",
          "url": "https://zuplo.com/learning-center/perplexity-api",
          "date": "2025-03-28",
          "last_updated": "2026-05-24"
        },
        {
          "snippet": "I am getting a \" [429] Request rate limit exceeded, please try again later.\" error from make.com.\n...\nYou can try placing a sleep module before each ai module to wait 3-5 seconds.",
          "title": "How can i optimise the number of api calls, and cell ...",
          "url": "https://community.make.com/t/how-can-i-optimise-the-number-of-api-calls-and-cell-updates-in-this-scenario/49923",
          "date": "2024-08-07",
          "last_updated": "2026-05-16"
        },
        {
          "snippet": "## Search API Rate Limits\nThe Search API has separate rate limits that apply to all usage tiers:\n| Endpoint       | Rate Limit             | Burst Capacity |\n| -------------- | ---------------------- | -------------- |\n| POST `/search` | 50 requests per second | 50 requests    |\n**Search Rate Limiter Behavior:**\n* **Burst**: Can handle 50 requests instantly\n* **Sustained**: Exactly 50 QPS average over time\n<Note>\nSearch rate limits are independent of your usage tier and apply consistently across all accounts using the same leaky bucket algorithm.\n</Note>\n...\nWhen you exceed your rate limits:\n1. **429 Error** - Your request gets rejected with \"Too Many Requests\"\n2. **Continuous Refill** - Tokens refill continuously based on your rate limit\n3. **Immediate Recovery** - New requests become available as soon as tokens refill\n**Example Recovery Times:**\n* **50 QPS limit**: 1 token refills every 20ms\n* **500 QPS limit**: 1 token refills every 2ms\n* **1,000 QPS limit**: 1 token refills every 1ms\n...\nVisit the [API Platform console](https://console.perplexity.ai) to see your current tier and total spending.\n...\nAdd credits to your account through the billing section.\nYour tier will automatically upgrade once you reach the spending threshold.\n...\nYour new rate limits take effect immediately after the tier upgrade.\nCheck your settings page to confirm.\n...\nIf you require custom rate limits beyond Tier 5, [fill out our rate limit increase request form](https://perplexity.typeform.com/to/yctmfyVT) and we'll review your use case to accommodate your needs.",
          "title": "Rate Limits & Usage Tiers - Perplexity API",
          "url": "https://docs.perplexity.ai/docs/admin/rate-limits-usage-tiers",
          "date": null,
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "",
          "title": "Best Practices",
          "url": "https://docs.perplexity.ai/docs/sdk/best-practices",
          "date": null,
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "Use highly specific queries for more targeted results.\nFor example, instead of searching for “AI”, use a detailed query like “artificial intelligence machine learning healthcare applications 2024”.\n```\n# Better: Specific query\nsearch = client.search.create(\nquery=\"artificial intelligence medical diagnosis accuracy 2024\",\nmax_results=10\n)\n# Avoid: Vague query\nsearch = client.search.create(\nquery=\"AI medical\",\n...\n)\n```\n...\nBreak your main topic into related sub-queries to cover all aspects of your research.\nUse the multi-query search feature to run multiple related queries in a single request for more comprehensive and relevant information.\n```\n...\nclient = Perplexity()\n# Comprehensive research with related queries\nsearch = client.search.create(\n...\n)\n...\n```\nYou can include up to 5 queries in a single multi-query request for efficient batch processing.\n3\nHandle rate limits efficiently\nImplement exponential backoff for rate limit errors and use appropriate batching strategies.\n```\nimport time\nimport random\nfrom perplexity import RateLimitError\ndef search_with_retry(client, query, max_retries=3):\nfor attempt in range(max_retries):\ntry:\nreturn client.search.create(query=query)\nexcept RateLimitError:\nif attempt < max_retries - 1:\n# Exponential backoff with jitter\ndelay = (2 ** attempt) + random.uniform(0, 1)\ntime.sleep(delay)\nelse:\nraise\n# Usage\ntry:\nsearch = search_with_retry(client, \"AI developments\")\nfor result in search.results:\nprint(f\"{result.title}: {result.url}\")\nexcept RateLimitError:\nprint(\"Maximum retries exceeded for search\")\n```\n4\nProcess concurrent searches efficiently\nUse async for concurrent requests while respecting rate limits.\n```\nimport asyncio\nfrom perplexity import AsyncPerplexity\nasync def batch_search(queries, batch_size=3, delay_ms=1000):\nasync with AsyncPerplexity() as client:\nresults = []\nfor i in range(0, len(queries), batch_size):\nbatch = queries[i:i + batch_size]\nbatch_tasks = [\nclient.search.create(query=query, max_results=5)\nfor query in batch\n]\nbatch_results = await asyncio.gather(*batch_tasks)\nresults.extend(batch_results)\n# Add delay between batches\nif i + batch_size < len(queries):\nawait asyncio.sleep(delay_ms / 1000)\nreturn results\n# Usage\nqueries = [\"AI developments\", \"climate change\", \"space exploration\"]\nresults = asyncio.run(batch_search(queries))\nprint(f\"Processed {len(results)} searches\")\n```\n...\n#### Rate-Limited Concurrent Processing\nFor large-scale applications, implement controlled concurrency with rate limiting:\n```\nimport asyncio\nfrom perplexity import AsyncPerplexity\nclass SearchManager:\ndef __init__(self, max_concurrent=5, delay_between_batches=1.0):\nself.max_concurrent = max_concurrent\nself.delay_between_batches = delay_between_batches\nself.semaphore = asyncio.Semaphore(max_concurrent)\nasync def search_single(self, client, query):\nasync with self.semaphore:\nreturn await client.search.create(query=query, max_results=5)\nasync def search_many(self, queries):\nasync with AsyncPerplexity() as client:\ntasks = [\nself.search_single(client, query)\nfor query in queries\n]\nresults = await asyncio.gather(*tasks, return_exceptions=True)\n# Filter out exceptions and return successful results\nsuccessful_results = [\nresult for result in results\nif not isinstance(result, Exception)\n]\nreturn successful_results\n# Usage\nasync def main():\nmanager = SearchManager(max_concurrent=3)\nqueries = [\n\"AI research 2024\",\n\"quantum computing advances\",\n\"renewable energy innovations\",\n\"biotechnology breakthroughs\",\n\"space exploration updates\"\n]\nresults = await manager.search_many(queries)\nprint(f\"Successfully processed {len(results)} out of {len(queries)} searches\")\nasyncio.run(main())\n```\n#### Error Handling in Async Operations\nImplement robust error handling for async search operations:\n```\nimport asyncio\nimport logging\nfrom perplexity import AsyncPerplexity, APIStatusError, RateLimitError\nlogging.basicConfig(level=logging.INFO)\nlogger = logging.getLogger(__name__)\nasync def resilient_search(client, query, max_retries=3):\nfor attempt in range(max_retries):\ntry:\nresult = await client.search.create(query=query, max_results=5)\nlogger.info(f\"Search successful for: {query}\")\nreturn result\nexcept RateLimitError as e:\nif attempt < max_retries - 1:\ndelay = 2 ** attempt\nlogger.warning(f\"Rate limited for '{query}', retrying in {delay}s\")\nawait asyncio.sleep(delay)\nelse:\nlogger.error(f\"Max retries exceeded for: {query}\")\nreturn None\nexcept APIStatusError as e:\nlogger.error(f\"API error for '{query}': {e}\")\nreturn None\nexcept Exception as e:\nlogger.error(f\"Unexpected error for '{query}': {e}\")\nreturn None\nasync def main():\nasync with AsyncPerplexity() as client:\nqueries = [\"AI developments\", \"invalid query\", \"tech trends\"]\ntasks = [resilient_search(client, query) for query in queries]\nresults = await asyncio.gather(*tasks)\nsuccessful_results = [r for r in results if r is not None]\nprint(f\"Successful searches: {len(successful_results)}/{len(queries)}\")\nasyncio.run(main())\n```\n...\nRequest only the number of results you actually need.\nMore results = longer response times.\n...\nImplement caching for queries that don’t need real-time results.",
          "title": "Best Practices - Perplexity",
          "url": "https://docs.perplexity.ai/guides/search-best-practices",
          "date": "2025-10-09",
          "last_updated": "2026-05-10"
        },
        {
          "snippet": "The SDKs provide specific exception types for different error scenarios: - **APIConnectionError** - Network connection issues\n- **RateLimitError** - API rate limit exceeded\n- **APIStatusError** - HTTP status errors (4xx, 5xx)\n- **AuthenticationError** - Invalid API key or authentication issues\n- **ValidationError** - Invalid request parameters\n## ​ Basic Error Handling\nHandle common API errors with try-catch blocks:\n```\nimport perplexity\nfrom perplexity import Perplexity\nclient = Perplexity()\ntry:\nsearch = client.search.create(query=\"machine learning\")\nprint(search.results)\nexcept perplexity.APIConnectionError as e:\nprint(\"Network connection failed\")\nprint(e.__cause__)\nexcept perplexity.RateLimitError as e:\nprint(\"Rate limit exceeded, please retry later\")\nexcept perplexity.APIStatusError as e:\nprint(f\"API error: {e.status_code}\")\nprint(e.response)\n```\nCommon HTTP status codes: 400 (Bad Request), 401 (Authentication), 403 (Permission Denied), 404 (Not Found), 429 (Rate Limit), 500+ (Server Error).\n...\n### ​ Exponential Backoff for Rate Limits\nImplement intelligent retry logic for rate limit errors:\n```\nimport time\nimport random\nimport perplexity\nfrom perplexity import Perplexity\ndef search_with_retry(client, query, max_retries=3):\nfor attempt in range(max_retries):\ntry:\nreturn client.search.create(query=query)\nexcept perplexity.RateLimitError:\nif attempt == max_retries - 1:\nraise # Re-raise on final attempt\n# Exponential backoff with jitter\ndelay = (2 ** attempt) + random.uniform(0, 1)\nprint(f\"Rate limited. Retrying in {delay:.2f} seconds...\")\n time.sleep(delay)\nexcept perplexity.APIConnectionError:\nif attempt == max_retries - 1:\nraise\n# Shorter delay for connection errors\ndelay = 1 + random.uniform(0, 1)\nprint(f\"Connection error. Retrying in {delay:.2f} seconds...\")\n time.sleep(delay)\n# Usage\nclient = Perplexity()\nresult = search_with_retry(client, \"artificial intelligence\")\n```\n...\nImplement fallback mechanisms when API calls fail:\n```\nimport perplexity\nfrom perplexity import Perplexity\ndef get_ai_response(query, fallback_response=\"I'm sorry, I'm temporarily unavailable.\"):\nclient = Perplexity()\ntry:\n# Primary: Try online model\nresponse = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[{\"role\": \"user\", \"content\": query}]\n)\nreturn response.choices[0].message.content\nexcept perplexity.RateLimitError:\ntry:\n# Fallback: Try offline model if rate limited\nresponse = client.chat.completions.create(\nmodel=\"llama-3.1-8b-instruct\",\nmessages=[{\"role\": \"user\", \"content\": query}]\n)\nreturn response.choices[0].message.content\nexcept Exception:\nreturn fallback_response\nexcept perplexity.APIConnectionError:\n# Network issues - return cached response or fallback\nreturn fallback_response\nexcept Exception as e:\nprint(f\"Unexpected error: {e}\")\nreturn fallback_response\n# Usage\nresponse = get_ai_response(\"What is machine learning?\")\nprint(response)\n```\n...\n1\nAlways handle rate limits\nRate limiting is common with API usage.\nAlways implement retry logic with exponential backoff.\n2\nLog errors for monitoring\nInclude proper logging to track error patterns and API health.\n...\n3\nSet appropriate timeouts\nConfigure timeouts to prevent hanging requests.\n```\n...\nCheck for invalid API keys and provide helpful error messages.\n```\ntry:\nresult = client.search.create(query=\"test\")\n...\nprint(\"Invalid API key. Please check your PERPLEXITY_API_KEY environment variable.\")\n```",
          "title": "Error Handling - Perplexity",
          "url": "https://docs.perplexity.ai/guides/perplexity-sdk-error-handling",
          "date": "2025-12-05",
          "last_updated": "2026-01-27"
        },
        {
          "snippet": "",
          "title": "Fix Perplexity API Errors 429, 405, 500 | Complete Tutorial 2025",
          "url": "https://www.hostingseekers.com/blog/fix-perplexity-api-errors-tutorial/",
          "date": "2025-11-21",
          "last_updated": "2026-05-16"
        }
      ],
      "server_time": null
    }
    ````
  </Accordion>

  <Accordion title="Response — Perplexity Search API Python SDK quickstart example">
    ````json theme={null}
    {
      "id": "a3284d7c-f02c-45fc-82db-d368ad880edc",
      "results": [
        {
          "snippet": "",
          "title": "Quickstart - Perplexity API",
          "url": "https://docs.perplexity.ai/docs/getting-started/quickstart",
          "date": null,
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "",
          "title": "Perplexity Search API",
          "url": "https://docs.perplexity.ai/docs/search/quickstart",
          "date": null,
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "# Quickstart\n> Learn how to use the official Perplexity SDKs for Python and TypeScript to access the Perplexity APIs with type safety and async support.\n...\nThe official Perplexity SDKs provide convenient access to the Perplexity APIs from Python 3.8+ and Node.js applications.\nBoth SDKs include type definitions for all request parameters and response fields, with both synchronous and asynchronous clients.\nAccess four APIs: **Agent API** for third-party models with web search tools and presets, **Search** for ranked web search results, **Sonar** for web-grounded AI responses, and **Embeddings** for generating text embeddings.\n...\n<Card title=\"Search\" icon=\"search\" href=\"/docs/search/quickstart\">\nRanked web search results with filtering, multi-query support, and domain controls.\n...\n## Installation\nInstall the SDK for your preferred language:\n<CodeGroup>\n```bash Python theme={null}\npip install perplexityai\n```\n```bash TypeScript theme={null}\nnpm install @perplexity-ai/perplexity_ai\n```\n</CodeGroup>\n## Authentication\n<Card title=\"Get your Perplexity API Key\" icon=\"key\" arrow=\"True\" horizontal=\"True\" iconType=\"solid\" cta=\"Click here\" href=\"https://console.perplexity.ai\">\nNavigate to the **API Keys** tab in the API Portal and generate a new key.\n</Card>\nAfter generating the key, set it as an environment variable in your terminal:\n<Tabs>\n<Tab title=\"Windows\">\n```bash theme={null}\nsetx PERPLEXITY_API_KEY \"your_api_key_here\"\n```\n</Tab>\n<Tab title=\"MacOS/Linux\">\n```bash theme={null}\nexport PERPLEXITY_API_KEY=\"your_api_key_here\"\n```\n</Tab>\n</Tabs>\n### Using Environment Variables\nYou can use the environment variable directly:\n<CodeGroup>\n```python Python theme={null}\nimport os\nfrom perplexity import Perplexity\nclient = Perplexity() # Automatically uses PERPLEXITY_API_KEY\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity({\napiKey: process.env['PERPLEXITY_API_KEY'], // This is the default and can be omitted\n});\n```\n</CodeGroup>\nOr use [python-dotenv](https://pypi.org/project/python-dotenv/) (Python) or [dotenv](https://www.npmjs.com/package/dotenv) (Node.js) to load the environment variable from a `.env` file:\n<CodeGroup>\n```python Python theme={null}\nimport os\nfrom dotenv import load_dotenv\nfrom perplexity import Perplexity\nload_dotenv()\nclient = Perplexity() # Uses PERPLEXITY_API_KEY from .env file\n```\n```typescript TypeScript theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nimport dotenv from 'dotenv';\ndotenv.config();\nconst client = new Perplexity(); // Uses PERPLEXITY_API_KEY from .env file\n```\n</CodeGroup>\n<Tip>\nNow you're ready to start using the Perplexity APIs!\nChoose your API below for step-by-step usage guides.\n</Tip>\n<CardGroup cols={2}>\n<Card title=\"Agent API\" icon=\"code-circle\" href=\"/docs/agent-api/quickstart\">\nGet started with third-party models\n</Card>\n<Card title=\"Search\" icon=\"search\" href=\"/docs/search/quickstart\">\nGet started with web search\n</Card>\n...\nGet started with AI responses\n</Card>\n<Card title=\"Embeddings\" icon=\"cube\" href=\"/docs/embeddings/quickstart\">\nGet started with text embeddings\n...\nInstall from PyPI with pip\n</Card>\n<Card title=\"Node.js and TypeScript Package\" icon=\"brand-npm\" href=\"https://www.npmjs.com/package/@perplexity-ai/perplexity_ai\">\nInstall from npm registry\n</Card>\n</CardGroup>",
          "title": "Quickstart - Perplexity API",
          "url": "https://docs.perplexity.ai/docs/sdk/overview",
          "date": null,
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "",
          "title": "Perplexity API",
          "url": "https://docs.perplexity.ai/docs/getting-started/overview",
          "date": null,
          "last_updated": "2026-05-26"
        },
        {
          "snippet": "The Perplexity Python library provides convenient access to the Perplexity REST API from any Python 3.8+\napplication.\nThe library includes type definitions for all request params and response fields,\nand offers both synchronous and asynchronous clients powered by httpx.\nIt is generated with Stainless.\n...\nThe REST API documentation can be found on docs.perplexity.ai.\nThe full API of this library can be found in api.md.\n## Installation\n```\n# install from PyPI\npip install perplexityai\n```\n## Search API\nGet web search results:\n```\nimport os\nfrom perplexity import Perplexity\nclient = Perplexity(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"), # This is the default and can be omitted\n)\nsearch = client.search.create(\nquery=\"latest AI developments 2024\",\nmax_results=5\n)\nfor result in search.results:\nprint(f\"{result.title}: {result.url}\")\n```\n...\n```\n...\nfrom perplexity import Perplexity\nclient = Perplexity(\n...\n)\n...\nmessages=[\n{\n...\n\"content\": \"Tell me about the latest developments in AI\",\n}\n],\nmodel=\"sonar\",\n)\nprint(stream_chunk.id)\n```\n...\nSimply import `AsyncPerplexity` instead of `Perplexity` and use `await` with each API call:\n```\nimport os\nimport asyncio\nfrom perplexity import AsyncPerplexity\nclient = AsyncPerplexity(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"), # This is the default and can be omitted\n)\nasync def main() -> None:\nstream_chunk = await client.chat.completions.create(\nmessages=[\n{\n\"role\": \"user\",\n\"content\": \"Tell me about the latest developments in AI\",\n}\n],\nmodel=\"sonar\",\n)\nprint(stream_chunk.id)\nasyncio.run(main())\n```\n...\nYou can enable this by installing `aiohttp`:\n```\n# install from PyPI\npip install perplexityai[aiohttp]\n```\nThen you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:\n```\nimport asyncio\nfrom perplexity import DefaultAioHttpClient",
          "title": "perplexityai/perplexity-py - GitHub",
          "url": "https://github.com/perplexityai/perplexity-py",
          "date": "2025-09-25",
          "last_updated": "2025-10-19"
        },
        {
          "snippet": "## Get your Perplexity API Key\nNavigate to the **API Keys** tab in the API Portal and generate a new key.\nSee the API Groups page to set up an API group.\n**OpenAI SDK Compatible:** Perplexity’s API supports the OpenAI Chat Completions format.\nYou can use OpenAI client libraries by pointing to our endpoint.\n...\n## ​ Making Your First API Call\n- Python SDK\n- TypeScript SDK\n- cURL\n**Install the SDK first:** `pip install perplexityai`\n```\nfrom perplexity import Perplexity\n# Initialize the client (uses PERPLEXITY_API_KEY environment variable)\nclient = Perplexity()\n# Make the API call\ncompletion = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What were the results of the 2025 French Open Finals?\"}\n]\n)\n# Print the AI's response\nprint(completion.choices[0].message.content)\n```\nSet your API key as an environment variable: `export PERPLEXITY_API_KEY=\"your_api_key_here\"` (macOS/Linux) or `setx PERPLEXITY_API_KEY \"your_api_key_here\"` (Windows).",
          "title": "Quickstart",
          "url": "https://docs.perplexity.ai/getting-started/quickstart",
          "date": "2026-01-10",
          "last_updated": "2026-01-27"
        },
        {
          "snippet": "",
          "title": "Perplexity Search APIdocs.perplexity.ai › guides › search-quickstart",
          "url": "https://docs.perplexity.ai/docs/search/quickstart.md",
          "date": null,
          "last_updated": "2026-05-27"
        },
        {
          "snippet": "### 2.\nSearch API Quickstart (Python & TypeScript SDKs)\nThe docs recommend using official SDKs for safety and type-safety; you can also call the HTTP endpoint directly (POST https://api.perplexity.ai/search) with an Authorization header.\nBelow is a minimal Python example that mirrors the documented pattern.\n#### Basic Python example (client.search.create)\n# Example (conceptual) — mirrors docs pattern\nfrom perplexity import Client  # hypothetical SDK import style\nclient = Client(api_key=”YOUR_API_KEY”)\nresp = client.search.create(\nquery=”latest AI model research 2025″,\nmax_results=5\n)\n# Example response shape (simplified):\n# resp.results -> [ { “title”: “…”, “url”: “…”, “snippet”: “…”, “rank”: 1 }, … ]\nprint(resp.results[0][“title”], resp.results[0][“url”])\nThis call returns ranked results you can present to users or feed into an LLM for grounded synthesis.\nIf you prefer raw HTTP the docs provide a curl example for POST /search.\n...\nStart with the quickstart, use multi-query for depth, control content with max_tokens_per_page, and organize keys and billing via API Groups.",
          "title": "Mastering the Perplexity AI API Documentation",
          "url": "https://seabuckdigital.com/perplexity-ai-api-documentation/",
          "date": "2025-11-08",
          "last_updated": "2026-04-08"
        },
        {
          "snippet": "The Perplexity AI Toolkit makes it easy to use Perplexity Labs' `Sonar` language models (built on top of Meta's latest and most advanced model `LLama-3.1`) for creating chatbots, generating text, and searching the web (***in real-time** *).\nIt's designed for everyone, from beginners to experienced developers, allowing quick addition of AI features to projects with simple commands.\n...\n## Prerequisites\n- `Python 3.x`\n- An API key from Perplexity AI\n## Dependencies\nThe following Python packages are required:\n- `requests`: For making HTTP requests to the Perplexity API.\n...\n## Installation\nTo use the Perplexity AI Toolkit, clone the repository to your local machine and install the required Python packages.\nClone the repository:\n```\ngit clone https://github.com/RMNCLDYO/perplexity-ai-toolkit.git\n```\nNavigate to the repositories folder:\n```\ncd perplexity-ai-toolkit\n```\nInstall the required dependencies:\n```\npip install -r requirements.txt\n```\n## Configuration\n1. Obtain an API key from Perplexity.\n2. You have three options for managing your API key:\nClick here to view the API key configuration options - **Setting it as an environment variable on your device (recommended for everyday use)**\n- Navigate to your terminal.\n- Add your API key like so:\n```\nexport PERPLEXITY_API_KEY=your_api_key\n```\nThis method allows the API key to be loaded automatically when using the wrapper or CLI.\n- **Using an .env file (recommended for development):**\n- Install python-dotenv if you haven't already: `pip install python-dotenv`.\n- Create a .env file in the project's root directory.\n- Add your API key to the .env file like so:\n```\nPERPLEXITY_API_KEY=your_api_key\n```\nThis method allows the API key to be loaded automatically when using the wrapper or CLI, assuming you have python-dotenv installed and set up correctly.\n- **Direct Input:**\n- If you prefer not to use a `.env` file, you can directly pass your API key as an argument to the CLI or the wrapper functions.\n***CLI** *\n```\n--api_key \"your_api_key\"\n```\n***Wrapper** *\n```\napi_key=\"your_api_key\"\n```\n...\nThe Perplexity AI Toolkit can be used in two different modes: `Chat`, and `Search`.\n...\nChat mode is intended for chatting with an AI model (similar to a chatbot) or building conversational applications.\n#### Example Usage\n***CLI** *\n```\npython cli.py --chat\n```\n***Wrapper** *\n```\nfrom perplexity import Chat\nChat().run()\n```\n> An executable version of this example can be found here.\n(*You must move this file to the root folder before running the program.*)\n## Search Mode\nSearch mode is intended for searching online (in real-time) for a single query as perplexity does not support multi-turn conversations with their online models.\n#### Example Usage\n***CLI** *\n```\npython cli.py --search --query \"What is today's date?\"\n```\n***Wrapper** *\n```\nfrom perplexity import Search\nSearch().run(query=\"What is today's date?\")\n```\n> An executable version of this example can be found here.\n(*You must move this file to the root folder before running the program.*)\n*Search mode is limited to 'online' models, such as `llama-3.1-sonar-small-128k-online`, `llama-3.1-sonar-large-128k-online` and `llama-3.1-sonar-huge-128k-online`.*\n...\nA lightweight Python API wrapper and CLI for Perplexity’s Sonar language models.",
          "title": "RMNCLDYO/perplexity-ai-toolkit: A lightweight Python API ... - GitHub",
          "url": "https://github.com/RMNCLDYO/perplexity-ai-toolkit",
          "date": "2024-01-10",
          "last_updated": "2025-10-28"
        },
        {
          "snippet": "> Get started with Perplexity's Sonar API for web-grounded AI responses.\nMake your first API call in minutes.\n...\nPerplexity's Sonar API provides web-grounded AI responses with support for streaming, tools, search options, and more.\nYou can use it with OpenAI-compatible client libraries or our native SDKs for type safety and enhanced features.\nUse the Sonar API when you need web search capabilities built-in, streaming responses, or Perplexity's Sonar models.\n...\n## Installation\nInstall the SDK for your preferred language:\n<CodeGroup>\n```bash Python theme={null}\npip install perplexityai\n```\n```bash Typescript theme={null}\nnpm install @perplexity-ai/perplexity_ai\n```\n```bash OpenAI Python (Compatible) theme={null}\npip install openai\n```\n```bash OpenAI Typescript (Compatible) theme={null}\nnpm install openai\n```\n</CodeGroup>\n## Authentication\nSet your API key as an environment variable.\nThe SDK will automatically read it:\n<Tabs>\n<Tab title=\"macOS/Linux\">\n```bash theme={null}\nexport PERPLEXITY_API_KEY=\"your_api_key_here\"\n```\n</Tab>\n<Tab title=\"Windows\">\n```powershell theme={null}\nsetx PERPLEXITY_API_KEY \"your_api_key_here\"\n```\n</Tab>\n...\nAll SDK examples below automatically use the `PERPLEXITY_API_KEY` environment variable.\nYou can also pass the key explicitly if needed.\n...\n## Basic Usage\n### Non-Streaming Request\n<CodeGroup>\n```python Python SDK theme={null}\nfrom perplexity import Perplexity\nclient = Perplexity()\ncompletion = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the latest developments in quantum computing?\"}\n]\n)\nprint(completion.choices[0].message.content)\n```\n```typescript Typescript SDK theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity();\nconst completion = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the latest developments in quantum computing?\"\n}\n],\n});\nconsole.log(completion.choices[0].message.content);\n```\n```python OpenAI Python SDK theme={null}\nimport os\nfrom openai import OpenAI\nclient = OpenAI(\napi_key=os.environ.get(\"PERPLEXITY_API_KEY\"),\nbase_url=\"https://api.perplexity.ai\"\n)\nresp = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the latest developments in quantum computing?\"}\n]\n)\nprint(resp.choices[0].message.content)\n```\n```typescript OpenAI Typescript SDK theme={null}\nimport OpenAI from 'openai';\nconst client = new OpenAI({\napiKey: process.env.PERPLEXITY_API_KEY,\nbaseURL: \"https://api.perplexity.ai\"\n});\nconst resp = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the latest developments in quantum computing?\"\n}\n],\n});\nconsole.log(resp.choices[0].message.content);\n```\n```bash cURL theme={null}\ncurl https://api.perplexity.ai/v1/sonar \\\n-H \"Authorization: Bearer $PERPLEXITY_API_KEY\" \\\n-H \"Content-Type: application/json\" \\\n-d '{\n\"model\": \"sonar-pro\",\n\"messages\": [\n{\n\"role\": \"user\",\n\"content\": \"What are the latest developments in quantum computing?\"\n}\n]\n}' | jq\n```\n</CodeGroup>\n### Streaming Response\n<CodeGroup>\n```python Python SDK theme={null}\nfrom perplexity import Perplexity\nclient = Perplexity()\nstream = client.chat.completions.create(\nmodel=\"sonar-pro\",\nmessages=[\n{\"role\": \"user\", \"content\": \"What are the most popular open-source alternatives to OpenAI's GPT models?\"}\n],\nstream=True\n)\nfor chunk in stream:\nif chunk.choices[0].delta.content:\nprint(chunk.choices[0].delta.content, end=\"\")\n```\n```typescript Typescript SDK theme={null}\nimport Perplexity from '@perplexity-ai/perplexity_ai';\nconst client = new Perplexity();\nconst stream = await client.chat.completions.create({\nmodel: \"sonar-pro\",\nmessages: [\n{ role: \"user\", content: \"What are the most popular open-source alternatives to OpenAI's GPT models?\"\n}\n],\nstream: true,\n});\nfor await (const chunk of stream) {\nif (chunk.choices[0].delta.content) {\nprocess.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);\n}\n}\n```\n```bash cURL theme={null}\ncurl https://api.perplexity.ai/v1/sonar \\\n-H \"Authorization: Bearer $PERPLEXITY_API_KEY\" \\\n-H \"Content-Type: application/json\" \\\n-d '{\n\"model\": \"sonar-pro\",\n\"messages\": [\n{\n\"role\": \"user\",\n\"content\": \"What are the most popular open-source alternatives to OpenAI'\\''s GPT models?\"\n}\n],\n\"stream\": true\n}'\n```\n</CodeGroup>\n...\nGet raw search results with the Search API.",
          "title": "Sonar API - Perplexity",
          "url": "https://docs.perplexity.ai/docs/sonar/quickstart",
          "date": null,
          "last_updated": "2026-05-25"
        }
      ],
      "server_time": null
    }
    ````
  </Accordion>
</AccordionGroup>

## Performance Best Practices Summary

<Steps>
  <Step title="Use environment variables for configuration">
    Never hardcode API keys or configuration values.
  </Step>

  <Step title="Implement intelligent rate limiting">
    Use exponential backoff with jitter for retry strategies.
  </Step>

  <Step title="Configure connection pooling">
    Optimize HTTP client settings for your use case.
  </Step>

  <Step title="Monitor and log appropriately">
    Track performance metrics and error rates.
  </Step>

  <Step title="Implement graceful degradation">
    Provide fallback responses when APIs are unavailable.
  </Step>

  <Step title="Write testable code">
    Use dependency injection and mocking for unit tests.
  </Step>
</Steps>

## Related Resources

<CardGroup>
  <Card title="Error Handling" icon="alert-triangle" href="/docs/sdk/error-handling">
    Comprehensive error handling strategies
  </Card>

  <Card title="Performance" icon="bolt" href="/docs/sdk/performance">
    Async operations and optimization techniques
  </Card>

  <Card title="Configuration" icon="settings" href="/docs/sdk/configuration">
    Production-ready configuration patterns
  </Card>

  <Card title="Type Safety" icon="shield-check" href="/docs/sdk/type-safety">
    Leveraging types for safer code
  </Card>
</CardGroup>
