---
pubDatetime: 2026-03-09T18:18:01Z
title: "YouTube: A Conversation With Adam Pointon"
postSlug: "youtube-a-conversation-with-adam-pointon-2026-03-09"
description: "YouTube: A Conversation With Adam Pointon"
tags:
  - conversation
  - video-summary
  - youtube
  - adam
  - pointon
  - with
---

> **Video**: [A Conversation With Adam Pointon](https://youtu.be/RcLfffQdmh8?si=iyfCMzNxHh5eldGS) by **Unsupervised Learning**
> **Transcript**: 6,468 words

This summary details "A Conversation With Adam Pointon" by Unsupervised Learning, where Adam Pointon, from Knockknock, discusses his company's solution to modern network security challenges. The core of the discussion revolves around Knockknock's innovative approach to reducing attack surface by making network services invisible until just-in-time, authenticated access is explicitly granted. This matters significantly because in an era of rapidly escalating vulnerabilities and sophisticated exploitation, traditional "detect and respond" security models are struggling, making preventative "default deny" strategies like Knockknock's crucial for protecting critical infrastructure.

## The Problem: Exploding Attack Surface & Vulnerability Pace

Adam Pointon highlights the critical problem of exposing services on the internet, especially before authentication, which creates an unmanageable attack surface. This issue is exacerbated by the accelerating pace of vulnerability discovery (CVEs). Pointon notes that in February, CVEs were already on track to break annual records, indicating that the speed of defensive response can no longer keep up with the speed of attack and exploitation.

Knockknock was founded about five to six years ago to solve this "just in time network access" challenge. The initial focus was on situations where traditional VPNs or cloud routing solutions were impractical. The fundamental concept is to add and remove IP addresses to firewalls and other control layers dynamically.

Pointon explains that the name "Knockknock" is inspired by the older "port knocking" technique, where a specific sequence of port hits would open a firewall rule. However, Knockknock evolved past the vulnerabilities of that method. The key difference is that with Knockknock, the targeted service isn't even *listening* on the network until authorized access is granted.
> "The actual problem that we're solving was exposure of services where customer couldn't use a VPN, they couldn't use a cloud routing thing. So we built v1 of knockknock to add IP addresses to firewalls and control layers... just attack surface having something visible pre-authentication on the network on the internet especially these days just seems crazy and knockknock helps people not do that."
He stresses, "if you can't see it, then the history and the future history is less important, right? cuz you can't attack it."

## Beyond Obscurity: A Preventative Stance

The conversation touches upon the "security through obscurity" debate. Pointon clarifies that obscurity can be effective if it involves sufficient randomness and if knowing the *mechanism* doesn't instantly reveal the *key*. He uses an analogy of a "drop zone" in Central Park: knowing that a park is used for drops doesn't mean knowing the exact location (the key).

Knockknock fundamentally moves beyond mere obscurity by taking services entirely off the public internet. This means an attacker cannot even map out an organization's infrastructure if a service isn't visible. For instance, if Citrix isn't visible, an attacker won't even know it's being used, let alone exploit a zero-day vulnerability.
> "If Citrix's not visible on the internet, then you don't you can't even map it out as an attacker. You don't know that that organization's using Citrix."

Given the overwhelming rate of vulnerability discovery and exploitation, Pointon argues that the "detect and respond" model is no longer sustainable. The solution, he states, is prevention:
> "Our view is you just have to prevent, you know, you just have to block everything, not have SSH on the internet at all because ultimately one day there will be an SSH thing and you just don't want to be in the firing line and that when it inevitably happens."

## How Knockknock Operates & Control Layer Integration

Knockknock is designed to hide anything that doesn't *need* to be publicly accessible, such as SSH, SFTP, RDP, internal applications, and especially development and test environments.

*   **Client-less Web Application:** Users interact with Knockknock via a web application, eliminating the need for client-side software installations (unlike traditional VPNs requiring keys and certificates). It integrates with existing identity platforms for single sign-on (SSO).
*   **Orchestration Agents:** Knockknock employs "orchestration agents" that subscribe to login events. Once a user (human or machine, like an SFTP automated file transfer) authenticates via the web app, these agents pull the necessary information and apply specific IP access rules to the appropriate control layers for a predefined, limited time.
*   **Diverse Control Mechanisms:** Knockknock started with edge firewalls (Palo Alto, Fortinet, Checkpoint) but has expanded significantly:
    *   **Host-based firewalls:** Linux (`iptables`) and Windows (for just-in-time RDP access).
    *   **Legacy systems:** Upcoming support for HPUX on RISC and Solaris Spark architectures, demonstrating the ability to integrate into challenging, older environments.
    Pointon emphasizes that the "receiving endpoint should be self-defending and it's it's reading in the rules and become, you know, being self-defending and exposing access only after it's had that identity process."

## The Vision: Policy-Driven, Universal Security

Pointon articulates a compelling future vision for security: a "universal security policy" defined in plain English. This policy would dictate "what should be able to talk to what." An intelligent layer would then translate this high-level policy into the specific syntax and protocols required by various control mechanisms, whether they are network firewalls, host firewalls, or other gating technologies.

The fundamental principle behind this approach is **default deny**.
> "There is no access until that policy is applied at those control layers and only then is it is the network visible... default deny but allow web and SSH and IKE through and let's just hope that they're fine. It's just can't do that anymore."

The conversation explores extending this policy-driven model beyond just network access. This could include policies for AI application usage, data governance (e.g., restricting data movement to certain geographic regions), and managing access for automated agents within a network. The underlying mechanism remains the same: "This data can't move in or out uh unless these things are in order. Um, so it's really the same model applied down at the data layer and particularly outbound."

Crucially, while automation is central, Pointon stresses the importance of a "human in the loop" for critical control changes. To prevent security misconfigurations (like accidentally wide-open "allow any any" rules), changes must be "mechanical and boring and very, you know, human-ledd," often involving approval workflows. The goal is always to be "as small and as precise as possible and predictable."

## Customer Impact & Future Outlook

Customers experience an "aha moment" when they realize how Knockknock can secure their exposed services. A powerful validation comes "3 or 6 months later a customer will come to us and say oh you know that vulnerability in XYZ product that went around. Thank you because we weren't affected."

Common use cases include:
*   Securing remote access and file transfers.
*   Critically, hiding **development and test environments**. These are often less secured, frequently run in debug mode, and can spew valuable error messages to attackers. Knockknock allows organizations to "hide whole subnets" for these environments, making them accessible only to authorized staff or testing teams, even when hosted in the cloud.

A major feature of Knockknock is not just granting access but also its **automatic removal**. This ensures that access windows are always transient and aligned with the "default deny" principle.

Looking ahead, while AI isn't yet fully automating rule changes, there's interest in using it to analyze existing rules, identify exposure levels (red, amber, green), and prioritize remediation. The future with "agentic" networks, where "hundreds of thousands of these things crawling across an internal network all of the time," further reinforces the need for a preventative approach to access control and data movement. Trying to respond reactively to such a complex environment would be impossible.

Knockknock offers a free DIY home user license at knc.io for individuals to experiment with the product. The team will also be present at major security conferences like RSA and Black Hat.

## Key Takeaways

*   Knockknock reduces network attack surface by making services invisible until explicit, just-in-time authenticated access is granted.
*   It builds upon "port knocking" principles but ensures services are completely off the network until a temporary, precise access window is opened.
*   The system champions a "default deny" preventative security model, which is increasingly vital against the accelerating pace of vulnerability discovery and exploitation.
*   Knockknock's orchestration agents dynamically apply and remove access rules across diverse control layers, including modern edge firewalls and host-based firewalls, even supporting legacy systems.
*   The long-term vision is to manage security via a universal, plain-English policy that translates into precise, auditable rules across network, application, and data layers.
*   Beyond traditional remote access, key use cases include securing automated file transfers and hiding vulnerable development/test environments from public internet exposure.
*   Crucially, Knockknock not only grants least-privilege access but also automatically removes it, ensuring access is always transient and precisely controlled.

---

*Summary generated from YouTube transcript (6,468 words) using Gemini 2.5 Flash on 2026-03-09.*