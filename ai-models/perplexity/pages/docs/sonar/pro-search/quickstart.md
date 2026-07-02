---
title: "Quickstart"
source: https://docs.perplexity.ai/docs/sonar/pro-search/quickstart
path: docs/sonar/pro-search/quickstart
---

Get started with Pro Search for Sonar Pro - enhanced search with automated tools, multi-step reasoning, and real-time thought streaming

## Overview

Pro Search enhances [Sonar Pro](/docs/sonar/models/sonar-pro) with automated tool usage, enabling multi-step reasoning through intelligent tool orchestration including web search and URL content fetching.

<Warning>
  Pro Search only works when streaming is enabled. Non-streaming requests will fall back to standard Sonar Pro behavior.
</Warning>

<div>
  <div>
    <h3>Standard Sonar Pro</h3>

    <ul>
      <li>Single web search execution</li>
      <li>Fast response synthesis</li>
      <li>Fixed search strategy</li>
      <li>Static result processing</li>
    </ul>
  </div>

  <div>
    <h3>Pro Search for Sonar Pro</h3>

    <ul>
      <li>Multi-step reasoning with automated tools</li>
      <li>Dynamic tool execution</li>
      <li>Real-time thought streaming</li>
      <li>Adaptive research strategies</li>
    </ul>
  </div>
</div>

## Basic Usage

Enabling Pro Search requires setting `stream` to `true` and specifying `"search_type": "pro"` in your API request. The default search type is `"fast"` for regular Sonar Pro.

Here is an example of how to enable Pro Search with streaming:

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  messages = [
      {
          "role": "user", 
          "content": "Summarize developments in post-quantum cryptography and how lattice-based and hash-based schemes are being standardized by NIST."
      }
  ]

  response = client.chat.completions.create(
      model="sonar-pro",
      messages=messages,
      stream=True,
      web_search_options={
          "search_type": "pro"
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript Typescript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Summarize developments in post-quantum cryptography and how lattice-based and hash-based schemes are being standardized by NIST.'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'pro'
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/v1/sonar \
    --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Summarize developments in post-quantum cryptography and how lattice-based and hash-based schemes are being standardized by NIST."
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "pro"
      }
    }' --no-buffer
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "8326e168-7408-4978-853c-468a2500f757",
    "results": [
      {
        "snippet": "NIST’s Post-Quantum Cryptography (PQC) project leads the national and global effort to secure electronic information against the future threat of quantum computers—machines that may be years or decades away but could eventually break many of today’s widely used cryptographic systems.\nThrough a multi-year international competition involving industry, academia, and governments, NIST released the principal three PQC standards in 2024 and is developing additional standards to serve as backups or alternatives.\nOrganizations should begin applying these standards now to migrate their systems to quantum-resistant cryptography.\n...\n#### PQC Standards SIn August 2024, NIST released its principal PQC standards (as Federal Information Processing Standards, or FIPS), specifying key establishment and digital signature schemes based on candidates evaluated and selected through this multi-year process.\n##### FIPS 203# Module-Lattice-Based\nKey-Encapsulation Mechanism Standard\n(ML-KEM)\n##### FIPS 204# Module-Lattice-Based\nDigital Signature Standard\n(ML-DSA)\n##### FIPS 205# Stateless Hash-Based\nDigital Signature Standard\n(SLH-DSA)\n#### Migration to PQCioWith the release of the first three final PQC standards, organizations should begin migrating their systems to quantum-resistant cryptography.\n...\nUnder the transition timeline in NIST IR 8547, NIST will deprecate and ultimately remove quantum-vulnerable algorithms from its standards by 2035, with high-risk systems transitioning much earlier.\n...\n#### Ongoing PQC Standardization ProcessonNIST expects that the two digital signature standards (ML-DSA and SLH-DSA) and key-encapsulation mechanism standard (ML-KEM) will provide the foundation for most deployments of post-quantum cryptography.\n***They can and should be put into use now.** *\nNIST continues to evaluate the security and performance of innovative algorithms in order to identify additional candidates for standardization.\nIn addition to the three algorithms specified in the initial FIPS standards, the Falcon digital signature algorithm and HQC key encapsulation mechanism were selected for ongoing standardization; that process is underway.\nThis process continues with a longer-term effort that solicited additional algorithms for digital signature schemes that could serve as a backup to ML-DSA or that could address unique use cases.",
        "title": "Post-Quantum Cryptography | CSRC",
        "url": "https://csrc.nist.gov/projects/post-quantum-cryptography",
        "date": "2017-01-03",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "**Post-Quantum Cryptography Standardization** is a program and competition by NIST to update their standards to include post-quantum cryptography.\nIt was announced at PQCrypto 2016.\nTwenty-three signature schemes and fifty-nine encryption/KEM schemes were submitted by the initial submission deadline at the end of 2017 of which sixty-nine total were deemed complete and proper and participated in the first round.\nSeven of these, of which three are signature schemes, advanced to the third round, which was announced in July 2020.\nOn August 13, 2024, NIST released final versions of the first three Post Quantum Crypto Standards: FIPS 203, FIPS 204, and FIPS 205.\n...\nAcademic research on the potential impact of quantum computing dates back to at least 2001.\nA NIST published report from April 2016 cites experts that acknowledge the possibility of quantum technology to render the commonly used RSA algorithm insecure by 2030.\nAs a result, a need to standardize quantum-secure cryptographic primitives was pursued.\nSince most symmetric primitives are relatively easy to modify in a way that makes them quantum resistant, efforts have focused on public-key cryptography, namely digital signatures and key encapsulation mechanisms.\nIn December 2016 NIST initiated a standardization process by announcing a call for proposals.\n...\n|Hash-based| |- Gravity-SPHINCS - SPHINCS+| |\n...\nOn July 22, 2020, NIST announced seven finalists (\"first track\"), as well as eight alternate algorithms (\"second track\").\nThe first track contains the algorithms which appear to have the most promise, and will be considered for standardization at the end of the third round.\n...\nOn August 13, 2024, NIST released final versions of its first three Post Quantum Crypto Standards.\nAccording to the release announcement:\n> While there have been no substantive changes made to the standards since the draft versions, NIST has changed the algorithms’ names to specify the versions that appear in the three finalized standards, which are:\n>\n- Federal Information Processing Standard (FIPS) 203, intended as the primary standard for general encryption.\nAmong its advantages are comparatively small encryption keys that two parties can exchange easily, as well as its speed of operation.\nThe standard is based on the CRYSTALS-Kyber algorithm, which has been renamed ML-KEM, short for Module-Lattice-Based Key-Encapsulation Mechanism.\n> - FIPS 204, intended as the primary standard for protecting digital signatures.\nThe standard uses the CRYSTALS-Dilithium algorithm, which has been renamed ML-DSA, short for Module-Lattice-Based Digital Signature Algorithm.\n> - FIPS 205, also designed for digital signatures.\nThe standard employs the SPHINCS+ algorithm, which has been renamed SLH-DSA, short for Stateless Hash-Based Digital Signature Algorithm.\nThe standard is based on a different math approach than ML-DSA, and it is intended as a backup method in case ML-DSA proves vulnerable.\n> - Similarly, when the draft FIPS 206 standard built around FALCON is released, the algorithm will be dubbed FN-DSA, short for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm.\nOn March 11, 2025 NIST released Hamming Quasi-Cyclic (HQC) as the fifth algorithm for post-quantum asymmetric encryption as used for key encapsulation / exchange.\nThe new algorithm is as a backup for ML-KEM, the main algorithm for general encryption.\nHQC is a code-based scheme using different math than ML-KEM, thus mitigating possible weaknesses should any be found in the lattice-based ML-KEM.\nThe draft standard incorporating the HQC algorithm is expected in early 2026 with the final in 2027.",
        "title": "NIST Post-Quantum Cryptography Standardization - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/NIST_Post-Quantum_Cryptography_Standardization",
        "date": "2017-12-29",
        "last_updated": "2026-03-31"
      },
      {
        "snippet": "- NIST has released a final set of encryption tools designed to withstand the attack of a quantum computer.\n- These post-quantum encryption standards secure a wide range of electronic information, from confidential email messages to e-commerce transactions that propel the modern economy.\n- NIST is encouraging computer system administrators to begin transitioning to the new standards as soon as possible.\nGAITHERSBURG, Md.\n— The U.S. Department of Commerce’s National Institute of Standards and Technology (NIST) has finalized its principal set of encryption algorithms designed to withstand cyberattacks from a quantum computer.\n...\nThe algorithms announced today are specified in the first completed standards from NIST’s post-quantum cryptography (PQC) standardization project, and are ready for immediate use.\n...\nThe standards — containing the encryption algorithms’ computer code, instructions for how to implement them, and their intended uses — are the result of an eight-year effort managed by NIST, which has a long history of developing encryption.\nThe agency has rallied the world’s cryptography experts to conceive, submit and then evaluate cryptographic algorithms that could resist the assault of quantum computers.\n...\nThe algorithms NIST has standardized are based on different math problems that would stymie both conventional and quantum computers.\n“These finalized standards include instructions for incorporating them into products and encryption systems,” said NIST mathematician Dustin Moody, who heads the PQC standardization project.\n...\nMoody said that these standards are the primary tools for general encryption and protecting digital signatures.\nNIST also continues to evaluate two other sets of algorithms that could one day serve as backup standards.\nOne of these sets consists of three algorithms designed for general encryption but based on a different type of math problem than the general-purpose algorithm in the finalized standards.\nNIST plans to announce its selection of one or two of these algorithms by the end of 2024.\nThe second set includes a larger group of algorithms designed for digital signatures.\nIn order to accommodate any ideas that cryptographers may have had since the initial 2016 call for submissions, NIST asked the public for additional algorithms in 2022 and has begun a process of evaluating them.\nIn the near future, NIST expects to announce about 15 algorithms from this group that will proceed to the next round of testing, evaluation and analysis.\nWhile analysis of these two additional sets of algorithms will continue, Moody said that any subsequent PQC standards will function as backups to the three that NIST announced today.\n...\nThe new standards are designed for two essential tasks for which encryption is typically used: general encryption, used to protect information exchanged across a public network; and digital signatures, used for identity authentication.\nNIST announced its selection of four algorithms — CRYSTALS-Kyber, CRYSTALS-Dilithium, Sphincs+ and FALCON — slated for standardization in 2022 and released draft versions of three of these standards in 2023.\nThe fourth draft standard based on FALCON is planned for late 2024.\nWhile there have been no substantive changes made to the standards since the draft versions, NIST has changed the algorithms’ names to specify the versions that appear in the three finalized standards, which are:\n- **Federal Information Processing Standard (FIPS) 203**, intended as the primary standard for general encryption.\nAmong its advantages are comparatively small encryption keys that two parties can exchange easily, as well as its speed of operation.\nThe standard is based on the CRYSTALS-Kyber algorithm, which has been renamed ML-KEM, short for Module-Lattice-Based Key-Encapsulation Mechanism.\n- **FIPS 204**, intended as the primary standard for protecting digital signatures.\nThe standard uses the CRYSTALS-Dilithium algorithm, which has been renamed ML-DSA, short for Module-Lattice-Based Digital Signature Algorithm.\n- **FIPS 205**, also designed for digital signatures.\nThe standard employs the Sphincs+ algorithm, which has been renamed SLH-DSA, short for Stateless Hash-Based Digital Signature Algorithm.\nThe standard is based on a different math approach than ML-DSA, and it is intended as a backup method in case ML-DSA proves vulnerable.\nSimilarly, when the draft FIPS 206 standard built around FALCON is released, the algorithm will be dubbed FN-DSA, short for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm.",
        "title": "NIST Releases First 3 Finalized Post-Quantum Encryption Standards",
        "url": "https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards",
        "date": "2024-08-13",
        "last_updated": "2026-05-14"
      },
      {
        "snippet": "**FIPS 203, FIPS 204,** and** FIPS 205**, which specify algorithms derived from **CRYSTALS-Dilithium, CRYSTALS-KYBER**, and **SPHINCS^+^,** were published August 13, 2024.\n**FALCON** was also selected and will be published in **FIPS 206 (in development)**.\nSee NIST IR 8413, Status Report of the Third Round of the NIST Post-Quantum Cryptography Standardization Process.\n**HQC** was selected for standardization on March 11, 2025.\nSee NIST IR 8545, Status Report on the Fourth Round of the NIST Post-Quantum Cryptography Standardization Process.",
        "title": "PQC Standardization Process - Post-Quantum Cryptography | CSRC",
        "url": "https://csrc.nist.gov/projects/post-quantum-cryptography/post-quantum-cryptography-standardization",
        "date": "2017-01-03",
        "last_updated": "2026-05-22"
      },
      {
        "snippet": "- Three NIST standards that were developed through a rigorous, international process are ready to be implemented now.\nAs researchers around the world race to build quantum computers that could break the current encryption providing security and privacy for our digital lives, NIST is helping to secure our future by developing algorithms to protect our data and systems.\nNIST has already released three post-quantum cryptography standards that can be implemented now to secure a wide range of electronic information, from confidential email messages to e-commerce transactions that propel the modern economy.\nNIST continues to evaluate additional algorithms that could one day serve as backup standards.\nThese Federal Information Processing Standards (FIPS), which are mandatory for federal systems and adopted by organizations around the world, provide detailed descriptions of post-quantum encryption and digital signature algorithms so they can be implemented consistently to facilitate secure and interoperable communication.\nThey were developed through an eight-year effort managed by NIST, which has a long history of developing cryptography standards.\n...\nThe new algorithm will serve as a backup for the general encryption needed to protect data from quantum computers developed in the future.\n...\nThree new algorithms are expected to be ready for use in 2024.\nOthers will follow.",
        "title": "Post-quantum cryptography | NIST",
        "url": "https://www.nist.gov/pqc",
        "date": "2025-12-03",
        "last_updated": "2026-05-20"
      },
      {
        "snippet": "",
        "title": "Post-Quantum Cryptography and Quantum-Safe Security - arXiv",
        "url": "https://arxiv.org/html/2510.10436v1",
        "date": "2025-10-11",
        "last_updated": "2026-03-24"
      },
      {
        "snippet": "**Post-Quantum Cryptography Standardization** is a program and competition by NIST to update their standards to include post-quantum cryptography.\nIt was announced at PQCrypto 2016.\n23 signature schemes and 59 encryption/KEM schemes were submitted by the initial submission deadline at the end of 2017 of which 69 total were deemed complete and proper and participated in the first round.\nSeven of these, of which 3 are signature schemes, have advanced to the third round, which was announced on July 22, 2020.\nOn August 13, 2024, NIST released final versions of the first three Post Quantum Crypto Standards: FIPS 203, FIPS 204, and FIPS 205.\n...\nAcademic research on the potential impact of quantum computing dates back to at least 2001.\nA NIST published report from April 2016 cites experts that acknowledge the possibility of quantum technology to render the commonly used RSA algorithm insecure by 2030.\nAs a result, a need to standardize quantum-secure cryptographic primitives was pursued.\nSince most symmetric primitives are relatively easy to modify in a way that makes them quantum resistant, efforts have focused on public-key cryptography, namely digital signatures and key encapsulation mechanisms.\nIn December 2016 NIST initiated a standardization process by announcing a call for proposals.\nThe competition is now in its third round out of expected four, where in each round some algorithms are discarded and others are studied more closely.\nNIST hopes to publish the standardization documents by 2024, but may speed up the process if major breakthroughs in quantum computing are made.\nIt is currently undecided whether the future standards will be published as FIPS or as NIST Special Publication (SP).\n...\nOn July 22, 2020, NIST announced seven finalists (\"first track\"), as well as eight alternate algorithms (\"second track\").\nThe first track contains the algorithms which appear to have the most promise, and will be considered for standardization at the end of the third round.\nAlgorithms in the second track could still become part of the standard, after the third round ends.\nNIST expects some of the alternate candidates to be considered in a fourth round.\nNIST also suggests it may re-open the signature category for new schemes proposals in the future.\n...\nOn July 5, 2022, NIST announced the first group of winners from its six-year competition.\n...\nOn August 13, 2024, NIST released final versions of its first three Post Quantum Crypto Standards.\nAccording to the release announcement:\nWhile there have been no substantive changes made to the standards since the draft versions, NIST has changed the algorithms’ names to specify the versions that appear in the three finalized standards, which are:\n- Federal Information Processing Standard (FIPS) 203, intended as the primary standard for general encryption.\nAmong its advantages are comparatively small encryption keys that two parties can exchange easily, as well as its speed of operation.\nThe standard is based on the CRYSTALS-Kyber algorithm, which has been renamed ML-KEM, short for Module-Lattice-Based Key-Encapsulation Mechanism.\n- FIPS 204, intended as the primary standard for protecting digital signatures.\nThe standard uses the CRYSTALS-Dilithium algorithm, which has been renamed ML-DSA, short for Module-Lattice-Based Digital Signature Algorithm.\n- FIPS 205, also designed for digital signatures.\nThe standard employs the Sphincs+ algorithm, which has been renamed SLH-DSA, short for Stateless Hash-Based Digital Signature Algorithm.\nThe standard is based on a different math approach than ML-DSA, and it is intended as a backup method in case ML-DSA proves vulnerable.\n- Similarly, when the draft FIPS 206 standard built around FALCON is released, the algorithm will be dubbed FN-DSA, short for FFT (fast-Fourier transform) over NTRU-Lattice-Based Digital Signature Algorithm.\nOn March 11, 2025 NIST released HQC as the fifth algorithm for post-quantum asymmetric encryption as used for key encapsulation / exchange.\nThe new algorithm is as a backup for ML-KEM, the main algorithm for general encryption.\nHQC is based on different math than ML-KEM, thus mitigating weakness if found.\nThe draft standard incorporating the HQC algorithm is expected in early 2026 with the final in 2027.",
        "title": "NIST Post-Quantum Cryptography Standardization - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Post-Quantum_Cryptography_Standardization",
        "date": "2025-03-19",
        "last_updated": "2025-03-26"
      },
      {
        "snippet": "NIST is leading a global effort to create electronic defenses against such attacks through its Post-Quantum Cryptography (PQC) project, which released * *the first three finalized PQC standards* * in 2024.\n...\nTo counter this looming threat, we need encryption methods that can stave off cyberattacks by both the conventional computers we know today and the quantum computers of tomorrow.\nThese new methods are called post-quantum encryption algorithms.\n...\nTo stave off attacks by a quantum computer — if and when a cryptographically relevant one is built — the worldwide community must retire current encryption algorithms.\nPost-quantum encryption algorithms must be based on math problems that would be difficult for both conventional and quantum computers to solve.\nThe algorithms are designed for two main tasks for which encryption is typically used: general encryption, used to protect information such as passwords exchanged across a public network, and digital signatures, used for identity authentication.\nOf the four algorithms NIST has selected as the initial ones to be standardized, three are based on a family of math problems called structured lattices, while the fourth uses mathematical relationships known as hash functions.\nInstead of requiring a computer to factor large numbers, lattice and hash problems use other types of math that experts believe will be hard to solve for quantum computers and conventional computers alike.\nAdditional algorithms still under consideration are designed for general encryption and do not use structured lattices or hash functions in their approaches.\nTo put these algorithms into practice, NIST has led efforts to develop technical standards for post-quantum encryption.\nThese standards aim to provide solutions for different situations, employ varied approaches for encryption, and offer more than one algorithm for each kind of application in the event one proves vulnerable.\n...\nNIST kicked off the Post-Quantum Cryptography project in 2016 and late that year formally asked the world’s cryptography experts to submit algorithms that would prove intractable to both classical and quantum computers.\n...\nWe now have post-quantum encryption algorithms that are ready for use.\nNIST released the first three finalized PQC standards that incorporate them in 2024.",
        "title": "What Is Post-Quantum Cryptography? | NIST",
        "url": "https://www.nist.gov/cybersecurity-and-privacy/what-post-quantum-cryptography",
        "date": "2024-08-13",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "",
        "title": "Post-Quantum Cryptography (PQC) Standardization - 2025 Update",
        "url": "https://postquantum.com/post-quantum/cryptography-pqc-nist/",
        "date": "2025-09-24",
        "last_updated": "2026-05-25"
      },
      {
        "snippet": "",
        "title": "Post-quantum cryptography - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Post-quantum_cryptography",
        "date": "2010-03-18",
        "last_updated": "2026-05-06"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

## Enabling Automatic Classification

Sonar Pro can be configured to automatically classify queries into Pro Search or Fast Search based on complexity. This is the recommended approach for most applications.

Set `search_type: "auto"` to let the system intelligently route queries based on complexity.

<CodeGroup>
  ```python Python SDK theme={null}
  from perplexity import Perplexity

  client = Perplexity()

  response = client.chat.completions.create(
      model="sonar-pro",
      messages=[
          {
              "role": "user",
              "content": "Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data."
          }
      ],
      stream=True,
      web_search_options={
          "search_type": "auto"  # Automatic classification
      }
  )

  for chunk in response:
      if chunk.choices[0].delta.content:
          print(chunk.choices[0].delta.content, end="")
  ```

  ```typescript Typescript SDK theme={null}
  import Perplexity from '@perplexity-ai/perplexity_ai';

  const client = new Perplexity();

  const response = await client.chat.completions.create({
    model: 'sonar-pro',
    messages: [
      {
        role: 'user',
        content: 'Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data.'
      }
    ],
    stream: true,
    web_search_options: {
      search_type: 'auto'  // Automatic classification
    }
  });

  for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write((chunk.choices[0]?.delta?.content ?? '') as string);
    }
  }
  ```

  ```bash cURL theme={null}
  curl --request POST \
    --url https://api.perplexity.ai/v1/sonar \
    --header "Authorization: Bearer $PERPLEXITY_API_KEY" \
    --header "Content-Type: application/json" \
    --data '{
      "model": "sonar-pro",
      "messages": [
        {
          "role": "user",
          "content": "Compare the energy efficiency (kWh/100mi and MPGe) of the Tesla Model 3, Chevrolet Bolt, and Nissan Leaf using EPA data."
        }
      ],
      "stream": true,
      "web_search_options": {
        "search_type": "auto"
      }
    }' --no-buffer
  ```
</CodeGroup>

<Accordion title="Response">
  ```json theme={null}
  {
    "id": "cab71ad3-867d-4139-997e-c36ce805351b",
    "results": [
      {
        "snippet": "The following table compares official EPA ratings for fuel economy (in miles per gallon gasoline equivalent, mpg-e or MPGe, for plug-in electric vehicles) for series production all-electric passenger vehicles rated by the EPA for model years 2015, 2016, 2017, and 2023 versus the model year\n2016 vehicles that were rated the most efficient by the EPA with plug-in hybrid drivetrains (Chevrolet Volt – second generation), gasoline-electric hybrid drivetrains (Toyota Prius Eco - fourth generation), and the average new vehicle for that model year, which has a fuel economy of 25 mpg~‑US~ (9.4 L/100 km; 30 mpg~‑imp~).\nEPA rating data are taken from manufacturer testing of their own vehicles using a series of tests specified by federal law.\n...\nReal-world EV efficiency can also be expressed in miles per kilowatt-hour (mi/kWh), which converts EPA MPGe values into direct electrical energy consumption, allowing cross-comparison between electric and gasoline vehicles.\n...\n|Vehicle|Model year|EPA rated fuel economy|EPA rated fuel economy|EPA rated fuel economy|Notes| | |\n...\n|Toyota Prius HEV|2023|57 mpg|57 mpg|56 mpg|(9)| | |\n|Hyundai Ioniq 6 Long Range RWD w/ 18-inch wheels|2023|140 mpg‑e 24.1 kWh/100 mi; 15.0 kWh/100 km|153 mpg‑e 22.0 kWh/100 mi; 13.7 kWh/100 km|127 mpg‑e 26.5 kWh/100 mi; 16.5 kWh/100 km|(1)| | |\n...\n|Tesla Model Y AWD|2023|123 mpg‑e 27.4 kWh/100 mi; 17.0 kWh/100 km|129 mpg‑e 26.1 kWh/100 mi; 16.2 kWh/100 km|116 mpg‑e 29.1 kWh/100 mi; 18.1 kWh/100 km|(1)| | |\n|Tesla Model 3 Standard Range|2020|141 mpg‑e 23.9 kWh/100 mi; 14.9 kWh/100 km|148 mpg‑e 22.8 kWh/100 mi; 14.2 kWh/100 km|132 mpg‑e 25.5 kWh/100 mi; 15.9 kWh/100 km|(1)| | |\n...\n|Tesla Model 3 Long Range AWD|2020|121 mpg‑e 27.9 kWh/100 mi; 17.3 kWh/100 km|124 mpg‑e 27.2 kWh/100 mi; 16.9 kWh/100 km|116 mpg‑e 29.1 kWh/100 mi; 18.1 kWh/100 km|(1)| | |\n|Chevrolet Bolt EV|2017|119 mpg‑e 28.3 kWh/100 mi; 17.6 kWh/100 km|121 mpg‑e 27.9 kWh/100 mi; 17.3 kWh/100 km|110 mpg‑e 30.6 kWh/100 mi; 19.0 kWh/100 km| | | |\n...\n|Nissan Leaf (24 kW-h)|2013/14/15/16|114 mpg‑e 29.6 kWh/100 mi; 18.4 kWh/100 km|126 mpg‑e 26.8 kWh/100 mi; 16.6 kWh/100 km|101 mpg‑e 33.4 kWh/100 mi; 20.7 kWh/100 km|(1) (6)| | |\n...\n|Nissan Leaf (30 kW-h)|2016|112 mpg‑e 30.1 kWh/100 mi; 18.7 kWh/100 km|124 mpg‑e 27.2 kWh/100 mi; 16.9 kWh/100 km|101 mpg‑e 33.4 kWh/100 mi; 20.7 kWh/100 km|(1)| | |",
        "title": "Electric car EPA fuel economy - Wikipedia",
        "url": "https://en.wikipedia.org/wiki/Electric_car_EPA_fuel_economy",
        "date": "2015-04-30",
        "last_updated": "2026-05-05"
      },
      {
        "snippet": "Instead of focusing on battery size or total range, we look at **energy consumption (kWh per 100 miles)** and **MPGe**, the EPA’s miles-per-gallon equivalent metric.\n...\n**Methodology**: Recurrent's Most Efficient EVs of 2026 were determined based on combined efficiency in kWh/100miles as reported to the EPA.\n...\n## 3.\nTesla Model 3\n**Efficiency:** 25 kWh/100 miles\n**MPGe:** 134.8\n**Body style:** Compact sedan\n...\n## 5.\nTesla Model Y\n**Efficiency:** 26 kWh/100 miles\n**MPGe:** 129.6\n**Body style:** Compact crossover SUV\n...\n## 6.\nNissan LEAF\n**Efficiency:** 28 kWh/100 miles\n**MPGe:** 120.4\n**Body style:** Compact crossover (redesigned)",
        "title": "2026 Most Efficient EV by Size According to Testing - Recurrent",
        "url": "https://www.recurrentauto.com/research/most-efficient-ev",
        "date": "2026-03-02",
        "last_updated": "2026-05-27"
      },
      {
        "snippet": "|EPA MPG MPGe:Miles per Gallon Equivalent 1 gallon of gasoline=33.7 kWh About All-Electric Cars|Electricity Combined MPG:111 MPGe City MPG:123 Highway MPG:99 30 kWh/100 miles|",
        "title": "Find and Compare Cars",
        "url": "https://www.fueleconomy.gov/feg/noframes/48400.shtml",
        "date": "2023-01-01",
        "last_updated": "2024-10-03"
      },
      {
        "snippet": "MPGe is a unit of measure used by the Environmental Protection Agency (EPA) to represent EV fuel economy in a common unit with gas-powered vehicles, where 33.7 kilowatt-hours of electricity are equal to the energy contained in one gallon of gasoline.\nAmong those 17 models, there were a total of 37 unique configurations that achieved 100 MPGe or higher.\nThe Tesla Model 3 in rear-wheel drive configuration achieved the highest rating for MY 2022 with 132 MPGe.\n||\n|--|\n|||\n|Tesla Model 3|132|\n|Lucid Air|131|\n|Tesla Model Y|129|\n|Chevrolet Bolt EV|120|\n|Hyundai Kona Electric|120|\n|Tesla Model S|120|\n|Kia EV6|117|\n|Chevrolet Bolt EUV|115|\n|Hyundai Ioniq 5|114|\n|Kia Niro Electric|112|\n|Nissan Leaf|111|\n|MINI Cooper SE|110|\n|BMW i4 Gran Coupe|109|\n|Polestar 2|107|\n|Volkswagen ID.4|107|\n|Ford Mustang Mach-E|103|\n|Tesla Model X|102|\n...\n**Source: **U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.",
        "title": "FOTW #1257, September 26, 2022: Seventeen EV Models Achieved ...",
        "url": "https://www.energy.gov/eere/vehicles/articles/fotw-1257-september-26-2022-seventeen-ev-models-achieved-epa-combined-rating",
        "date": "2022-09-26",
        "last_updated": "2025-10-09"
      },
      {
        "snippet": "Nevertheless, the efficiency and range varies a lot from EV to EV.\nTo help you choose which electric car is more suitable for you, I made the table below with EPA efficiency and range figures – for different driving scenarios (city, highway and mixed/combined).\nElectric car range and efficiency (EPA)\n|Electric car\n|City\nrange\n|Combined\nrange\n|Highway\nrange\n|City\nefficiency\n|Combined\nefficiency\n|Highway\nefficiency\n|2019 Tesla Model 3 Long Range (RWD)\n|340 miles\n547 km\n|325 miles\n523 km\n|307 miles\n494 km\n|24,8 kWh/100 miles\n15,4 kWh/100 km\n|25,9 kWh/100 miles\n16,1 kWh/100 km\n|27,4 kWh/100 miles\n17 kWh/100 km\n|2019 Tesla Model 3 Long Range (AWD)\n|320 miles\n515 km\n|310 miles\n499 km\n|297 miles\n478 km\n|28,1 kWh/100 miles\n17,5 kWh/100 km\n|29,1 kWh/100 miles\n18,1 kWh/100 km\n|30,1 kWh/100 miles\n18,7 kWh/100 km\n|2019 Tesla Model 3 Standard Range Plus\n|253 miles\n407 km\n|240 miles\n386 km\n|224 miles\n361 km\n|24,1 kWh/100 miles\n15 kWh/100 km\n|25,3 kWh/100 miles\n15,7 kWh/100 km\n|27,2 kWh/100 miles\n16,9 kWh/100 km\n|2019 Tesla Model S Long Range\n|382 miles\n614 km\n|370 miles\n595 km\n|356 miles\n573 km\n|29,3 kWh/100 miles\n18,2 kWh/100 km\n|30,4 kWh/100 miles\n18,9 kWh/100 km\n|31,5 kWh/100 miles\n19,6 kWh/100 km\n|2019 Tesla Model X Long Range\n...\n22,5 kWh/100 km\n...\n|2017-2019 Chevrolet Bolt EV\n|255 miles\n411 km\n|238 miles\n383 km\n|217 miles\n350 km\n|26,3 kWh/100 miles\n16,4 kWh/100 km\n|28,3 kWh/100 miles\n17,6 kWh/100 km\n|30,6 kWh/100 miles\n19 kWh/100 km\n|2020 Chevrolet Bolt EV\n|279 miles\n449 km\n|259 miles\n417 km\n|237 miles\n381 km\n|26,5 kWh/100 miles\n16,5 kWh/100 km\n|28,6 kWh/100 miles\n17,7 kWh/100 km\n|31,2 kWh/100 miles\n19,4 kWh/100 km",
        "title": "Electric car range and efficiency (EPA) - 🔋PushEVs",
        "url": "https://pushevs.com/electric-car-range-efficiency-epa/",
        "date": null,
        "last_updated": "2024-02-21"
      },
      {
        "snippet": "An efficient EV is simply a car that uses fewer kilowatt-hours of electricity to go the same distance.\n...\n53–140 MPGe\nEPA spread\nModel‑year 2024 EVs range from about 53 to 140 miles‑per‑gallon‑equivalent, nearly a 3x difference in efficiency.\n1.5–4.2 mi/kWh\nEnergy use\nOn the same test cycle, some EVs travel less than 1.5 miles per kWh while the best creep above 4 miles per kWh.\n...\nMPGe, or **miles per gallon equivalent**, is the EPA’s attempt to put EVs in gas‑car language.\nOne “gallon” of gasoline is treated as 33.7 kWh of energy.\nIf an EV uses 25 kWh to travel 100 miles, the math works out to roughly 135 MPGe.\n...\nElectricity is billed in **kilowatt‑hours** (kWh).\nSo the most honest unit is simply: how many kWh do you burn to go 100 miles?\n- **kWh/100 mi**: lower is better (like L/100 km)\n- **mi/kWh**: higher is better (like MPG)\nExample: a car that uses 25 kWh/100 mi delivers 4.0 mi/kWh.\nAt $0.15/kWh, those 100 miles cost about $3.75.\n...\nTake the EPA’s kWh/100‑mile number, divide by 100, and multiply by your home rate.\n...\nThat’s why EPA ratings show 2024 EVs spanning roughly 53–140 MPGe while gasoline cars live between 9–57 MPG for the same model year.\n...\nRecent EPA data and independent testing put a handful of EVs at the sharp end of the efficiency spear, especially in sedan form.\n### Sample of highly efficient EVs on sale (2024–2025)\nRepresentative trims; always confirm the exact configuration’s window sticker, as wheels, motors, and options change the numbers.\n|Model & year|Type|Energy use (kWh/100 mi)*|Approx. mi/kWh|EPA combined MPGe*|Notable trait|\n|--|--|--|--|--|--|\n|Lucid Air Pure (2025 RWD)|Sedan|≈23–24|≈4.2–4.3|High 130s–140s|Luxury sedan that somehow drinks like a subcompact.|\n|Hyundai Ioniq 6 SE (2024–2025 RWD)|Sedan|≈24–25|≈4.0–4.2|Around 140|Super‑slippery aero and efficient 800‑V platform.|\n|Tesla Model 3 Long Range RWD (2025)|Sedan|≈25|≈4.0|Low‑to‑mid 130s|The efficiency benchmark among mass‑market sedans.|\n|Tesla Model Y Long Range RWD (2025)|SUV|≈27–28|≈3.6–3.7|Mid‑120s|Roomier crossover form factor, small aero penalty.|\n|Lexus RZ 300e (2024–2025)|SUV|≈27|≈3.7|Mid‑120s|Luxury compact SUV that surprised everyone with its frugality.|\n|Kia EV6 / Hyundai Kona Electric / Kia Niro EV (2024–2025 RWD)|Crossovers|≈28–29|≈3.4–3.6|High teens/low 120s|The efficient heartland of the EV market.|\n|GMC Hummer EV Pickup/SUV|Truck/SUV|≈70+|≈1.4–1.5|Under 50|Off‑the‑charts consumption; think of it as a rolling coal plant with a conscience.|\n...\n### Sedans & hatchbacks\n- **Typical energy use:** ~24–30 kWh/100 mi\n- **Examples:** Hyundai Ioniq 6, Tesla Model 3, Lucid Air, Chevy Bolt (used)\n...\n#### 1.\nStart with kWh/100 mi, not just range\nRange is a product of pack size; kWh/100 mi is the diet.\n...\n#### 2.\nNormalize for body style and mission\nCompare sedans to sedans, crossovers to crossovers, trucks to trucks.\n...\nWhen you compare electric cars, focus less on the billboard range number and more on **kWh per 100 miles, body style, and real battery health**.\n- Use kWh/100 miles (or mi/kWh) as your primary yardstick; MPGe is just the translation into gas‑car language.",
        "title": "Electric Car Efficiency Comparison: 2025 Buyer's Guide - Recharged",
        "url": "https://recharged.com/articles/electric-car-efficiency-comparison-guide",
        "date": "2025-11-17",
        "last_updated": "2026-05-26"
      },
      {
        "snippet": "With an EPA-rated efficiency of 111 MPGe, it’s middle-of-the-road in efficiency, far below the Tesla but way above the 2021 Ford Mustang Mach-E GT’s 84 MPGe.\n...\nRecent figures from the U.S. Environmental Protection Agency (EPA) show that the 2021 Tesla Model 3 Standard Range Plus RWD stands at the top of the efficiency range, boasting a combined 142 MPGe—the electrical equivalent of a gallon of fuel.\n...\nEV testing and analysis firm Recurrent crunched the numbers on a set of 99 cars—half Tesla Model 3s and half Nissan Leafs—and their 500,000 data points of efficiency metrics were logged between November 2021 and March 2022.\nUsing an EPA figure-based mile per kWh (mi/kWh) measurement as opposed to MPGe, the Tesla range was calculated from 3.33 to 4.17 mi/kWh, and the Nissan Leaf was 2.94 to 3.45 mi/kWh.\nTherefore, even bargain standard Model 3s will achieve greater road efficiency than the best Leaf.\nHowever, the EPA ratings weren’t what was measured when real-world driving conditions were considered.\nOver the four-month timeframe, Recurrent revealed the median observed efficiency for each vehicle as the Tesla Model 3 having 3.39 mi/kWh and the Nissan Leaf having 3.71 mi/kWh.",
        "title": "Is the Nissan Leaf More Efficient Than the Tesla Model 3? Here's What 1 Study Found",
        "url": "https://www.motorbiscuit.com/nissan-leaf-more-efficient-tesla-model-3-what-study-found/",
        "date": "2022-08-11",
        "last_updated": "2025-06-25"
      },
      {
        "snippet": "Compare USA EV efficiency by kWh/100 mi and MPGe, with EPA and charging metrics across all models and trims.\nUpdated monthly (2026).",
        "title": "Most Efficient EVs in the USA (kWh/100 mi) - BEV Database",
        "url": "https://bev-database.com/cars-list-usa/most-efficient-electric-cars",
        "date": "2026-02-28",
        "last_updated": "2026-02-28"
      },
      {
        "snippet": ",\nModel Year 2022 EVs Achieving EPA Combined Rating of 100 MPGe or more,\nMake and Model,Highest MPGe For Base Model\nTesla Model 3,132\nLucid Air,131\nTesla Model Y,129\nChevrolet Bolt EV,120\nHyundai Kona Electric,120\nTesla Model S,120\nKia EV6,117\nChevrolet Bolt EUV,115\nHyundai Ioniq 5,114\nKia Niro Electric,112\nNissan Leaf,111\nMINI Cooper SE,110\nBMW i4 Gran Coupe,109\nPolestar 2,107\nVolkswagen ID.4,107\nFord Mustang Mach-E,103\nTesla Model X,102\n,\n...\nEVs include only all-electric vehicles.,\n...\nOnly the base model names are shown and only the highest MPGe values are shown for each model name.\nSome models listed have configurations that fall below 100 MPGe.,\n...\n,\n\"Source: U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.\",\n,\n,\nhttps://www.fueleconomy.gov/feg/evSelect.jsp,",
        "title": "FOTW_1257_web.xlsx",
        "url": "https://www.energy.gov/sites/default/files/2022-09/FOTW_1257_web.xlsx",
        "date": null,
        "last_updated": "2025-03-28"
      },
      {
        "snippet": ",\nModel Year 2022 EVs Achieving EPA Combined Rating of 100 MPGe or more,\nMake and Model,Highest MPGe For Base Model\nTesla Model 3,132\nLucid Air,131\nTesla Model Y,129\nChevrolet Bolt EV,120\nHyundai Kona Electric,120\nTesla Model S,120\nKia EV6,117\nChevrolet Bolt EUV,115\nHyundai Ioniq 5,114\nKia Niro Electric,112\nNissan Leaf,111\nMINI Cooper SE,110\nBMW i4 Gran Coupe,109\nPolestar 2,107\nVolkswagen ID.4,107\nFord Mustang Mach-E,103\nTesla Model X,102\n,\n...\nEVs include only all-electric vehicles.,\n...\nOnly the base model names are shown and only the highest MPGe values are shown for each model name.\nSome models listed have configurations that fall below 100 MPGe.,\n...\n,\n\"Source: U.S. Department of Energy and U.S. Environmental Protection Agency’s Fuel Economy Website, Compare Electric Vehicles Side-by-Side.\nData accessed August 24, 2022.\",\n,\n,\nhttps://www.fueleconomy.gov/feg/evSelect.jsp,",
        "title": "[XLS] FOTW #1257 - Energy.gov",
        "url": "https://www.energy.gov/documents/fotw1257webxlsx",
        "date": null,
        "last_updated": "2026-03-05"
      }
    ],
    "server_time": null
  }
  ```
</Accordion>

#### How Classification Works

The classifier analyzes your query and automatically routes it to:

* **Pro Search** for complex queries requiring:
  * Multi-step reasoning or analysis
  * Comparative analysis across multiple sources
  * Deep research workflows

* **Fast Search** for straightforward queries like:
  * Simple fact lookups
  * Direct information retrieval
  * Basic question answering

#### Billing with Auto Classification

**You are billed based on which search type your query triggers:**

* If classified as **Pro Search**: \$14–\$22 per 1,000 requests (based on context size)
* If classified as **Fast Search**: \$6–\$14 per 1,000 requests (based on context size - same as standard Sonar Pro)

To see the full pricing details, see the <a href="/docs/sonar/pro-search/quickstart#pricing">Pricing</a> section.

<Tip>
  Automatic classification is recommended for most applications as it balances cost optimization with query performance. You get Pro Search capabilities when needed without overpaying for simple queries.
</Tip>

### Manually Specifying the Search Type

If needed, you can manually specify the search type. This is useful for specific use cases where you know the query requires Pro Search capabilities.

* **`"search_type": "pro"`**: Manually specify Pro Search for complex queries when you know multi-step tool usage is needed
* **`"search_type": "fast"`**: Manually specify Fast Search for simple queries to optimize speed and cost (this is also the default when `search_type` is omitted)

## Built-in Tool Capabilities

Pro Search provides access to two powerful built-in tools that the model can use automatically:

<CardGroup>
  <Card title="web_search" icon="search" href="/docs/sonar/pro-search/tools#web_search">
    Conduct targeted web searches with custom queries, filters, and search strategies based on the evolving research context.
  </Card>

  <Card title="fetch_url_content" icon="globe" href="/docs/sonar/pro-search/tools#fetch_url_content">
    Retrieve and analyze content from specific URLs to gather detailed information beyond search result snippets.
  </Card>
</CardGroup>

<Info>
  The model automatically decides which tools to use and when, creating dynamic research workflows tailored to each specific query. These are built-in tools called by the system. Custom tools cannot be registered. Learn more in the [Built-in Tool Capabilities](/docs/sonar/pro-search/tools) guide.
</Info>

## Additional Capabilities

Pro Search also provides access to advanced Sonar Pro features that enhance your development experience:

* **[Stream Mode Guide](/docs/sonar/pro-search/stream-mode)**: Control streaming response formats with concise or full mode for optimized bandwidth usage and enhanced reasoning visibility.

## Pricing

Pro Search pricing consists of token usage plus request fees that vary by search type and context size.

<div>
  <div>
    <h3>Token Usage (Same for All Search Types)</h3>

    <div>
      <div>
        <span>Input Tokens</span>
        <span>\$3 per 1M</span>
      </div>

      <div>
        <span>Output Tokens</span>
        <span>\$15 per 1M</span>
      </div>
    </div>
  </div>

  <div>
    <h3>Request Fees (per 1,000 requests)</h3>

    <div>
      <h4>Pro Search (Complex Queries)</h4>

      <div>
        <div>
          <span>High Context</span>
          <span>\$22</span>
        </div>

        <div>
          <span>Medium Context</span>
          <span>\$18</span>
        </div>

        <div>
          <span>Low Context</span>
          <span>\$14</span>
        </div>
      </div>
    </div>

    <div>
      <h4>Fast Search (Simple Queries)</h4>

      <div>
        <div>
          <span>High Context</span>
          <span>\$14</span>
        </div>

        <div>
          <span>Medium Context</span>
          <span>\$10</span>
        </div>

        <div>
          <span>Low Context</span>
          <span>\$6</span>
        </div>
      </div>
    </div>
  </div>
</div>

<Info>
  When using `search_type: "auto"`, you're billed at the Pro Search rate if your query is classified as complex, or the Fast Search rate if classified as simple. See the full pricing details <a href="/docs/getting-started/pricing">here</a>.
</Info>

## Next Steps

<CardGroup>
  <Card title="Pro Search Tools" icon="brain" href="/docs/sonar/pro-search/tools">
    Learn about the tools available to the model for Pro Search.
  </Card>

  <Card title="Pro Search Classifier" icon="brain" href="/docs/sonar/pro-search/classifier">
    Learn about the classifier that automatically determines whether a query requires Pro Search or Fast Search.
  </Card>

  <Card title="Pro Search Stream Mode" icon="bolt" href="/docs/sonar/pro-search/stream-mode">
    Learn about the streaming mode for Pro Search.
  </Card>

  <Card title="Agent API Quickstart" icon="rocket" href="/docs/agent-api/quickstart">
    Get started with the Agent API.
  </Card>
</CardGroup>
