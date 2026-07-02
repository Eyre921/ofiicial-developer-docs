---
title: "Fact Dynamics | Real-time Fact-Checking Flutter App"
source: https://docs.perplexity.ai/docs/cookbook/showcase/fact-dynamics
path: docs/cookbook/showcase/fact-dynamics
---

Cross-platform app for real-time fact-checking of debates, speeches, and images using Perplexity's Sonar API

# Fact Dynamics | Real-time Fact-Checking Flutter App

<p>
  <img alt="Fact Dynamics logo" />
</p>

**Hackathon Submission** - Built for Perplexity Hackathon in Information Tools & Deep Research categories.

Fact Dynamics is a cross-platform Flutter app that provides real-time fact-checking for spoken content and images. Perfect for live debates, presentations, and on-the-fly information verification.

## Features

* Real-time speech transcription and fact-checking during live conversations

* Image text extraction and claim verification with source citations

* Claim rating system (TRUE, FALSE, MISLEADING, UNVERIFIABLE) with explanations

* Source citations - Provides authoritative URLs backing each verdict

* Debate mode with continuous speech recognition and streaming feedback

* User authentication via Firebase (Google, Email) with persistent chat history

* Cross-platform support for iOS, Android, and Web

## Prerequisites

* Flutter SDK 3.0.0 or newer
* Dart SDK 2.17.0 or newer
* Firebase CLI for authentication and database setup
* Perplexity API key for Sonar integration
* Device with microphone access for speech recognition

## Installation (Follow Detailed guideline on the Repository)

```bash theme={null}
git clone https://github.com/vishnu32510/fact_pulse.git
cd fact_pulse
flutter pub get
```

## Usage

### Real-time Speech Fact-Checking

* Streams 5-second audio chunks through Flutter's `speech_to_text`
* Sends transcribed snippets to Sonar API with structured prompts
* Returns JSON with claims, ratings (TRUE/FALSE/MISLEADING/UNVERIFIABLE), explanations, and sources

### Image Analysis

* Uploads images/URLs to Sonar API for text extraction
* Verifies extracted claims against authoritative sources
* Provides comprehensive analysis with source attribution

## Screenshots

<table>
  <tr>
    <td>
      <img alt="Dashboard" />
    </td>

    <td>
      <img alt="Fact checking interface" />
    </td>
  </tr>
</table>

## Code Explanation

* Frontend: Flutter with BLoC pattern for state management targeting iOS, Android, and Web
* Backend: Firebase (Firestore, Authentication) for user data and chat history persistence
* Speech Processing: speech\_to\_text package for real-time audio transcription
* API Integration: Custom Dart client calling Perplexity Sonar API with structured prompts
* Image Processing: Built-in image picker with base64 encoding for multimodal analysis
* Data Architecture: Firestore collections per user with subcollections for debates, speeches, and images

## Open Source SDKs

Built two reusable packages for the Flutter community:

* **[perplexity\_dart](https://pub.dev/packages/perplexity_dart)** - Core Dart SDK for Perplexity API
* **[perplexity\_flutter](https://pub.dev/packages/perplexity_flutter)** - Flutter widgets and BLoC integration

## Demo Video

<iframe title="YouTube video player" />

## Links

* **[GitHub Repository](https://github.com/vishnu32510/fact_pulse)** - Full source code
* **[Live Demo](https://fact-pulse.web.app/)** - Try the web version
* **[Devpost Submission](https://devpost.com/software/fact-dynamics)** - Hackathon entry
