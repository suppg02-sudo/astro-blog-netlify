---
pubDatetime: 2026-02-15T17:09:27Z
title: "Exploring Nametag: A New Open-Source PRM in Early Development"
postSlug: "nametag-open-source-prm"
description: "Exploring Nametag: A New Open-Source PRM in Early Development"
tags:
  - ai-assisted-development
  - self-hosted
  - youtube
  - monica-alternative
  - personal-relationship-manager
  - docker
---

Exploring Nametag, a new open-source Personal Relationship Manager (PRM) in active development, created by Matto as an alternative to the less-maintained Monica PRM. This 94-minute live stream demonstrates deployment, features, and UI walkthrough with the developer present for real-time Q&A and bug fixes.

## What is Nametag?

Nametag is an open-source **Personal Relationship Manager** designed to help users track people in their lives and how they're connected. Think of it as "a CRM for your actual relationships instead of sales prospects."

**Core capabilities include:**

- Track people with flexible attributes (name, birthday, important dates, notes)
- Map relationships between people (family, friends, colleagues)
- Visualize your network as an interactive graph
- Organize contacts into custom groups
- Set reminders for important dates and staying in touch
- Full dark mode support
- Multi-language support (English, Spanish, Japanese, Norwegian, German)
- Multiplatform Docker support (ARM64 included)

## Developer Background & Transparency

**Matto** is the developer behind Nametag:

- Senior Software Engineer at Spotify (backend API, Python, Django)
- Based in Madrid, Spain
- Created Nametag because Monica PRM wasn't well-maintained
- Used Claude AI for code generation but validates all code manually
- Experience: Python, Django, DevOps with AWS, onboard SDK, Python C++

The stream had an important discussion about **AI in software development**:

- The stream discussed an email DB Tech received from Palup.ai offering to create an AI clone for chat support
- Concerns were raised about AI lacking actual human experience and building echo chambers
- Matto confirmed using Claude for code but emphasized his experience qualifies him to validate AI-generated code
- This was presented as **responsible AI usage** - experienced developer using it to accelerate work, not replace human judgment

This is a key distinction: AI used as a coding assistant vs AI "cloning" services that try to replace human connection entirely.

## Deployment & Architecture

**Docker Compose Setup:**

The demo showed a simplified deployment using Docker Compose with three containers:

- **PostgreSQL database**: Data persistence
- **Application container**: The main Nametag app (Node.js based)
- **Cron container**: Handles reminders and cleanup tasks

**Environment variables required:**

```bash
DATABASE_HOST=db              # Changed from localhost for Docker networks
DATABASE_PORT=5432
DATABASE_NAME, USER, PASSWORD
URL=your-domain-or-ip        # Application URL
SECRET_KEY=32-char-key          # Generate with: openssl rand -base64 32
CRON_SECRET=16-char-min        # For scheduled tasks
DISABLE_REGISTRATION=true     # Disable after first user (optional)
EMAIL_CONFIG=SMTP|Resend        # Optional for notifications
```

**Deployment steps demonstrated:**

1. Create directory and copy docker-compose.yaml
2. Create .env file with required variables
3. Run `docker compose up -d`
4. Access at port 3000

**Key architectural notes:**

- No default admin account - first user to register becomes admin
- Registration can be disabled after first user via environment variable
- JSON import/export for data backup and restore
- Roadmap includes 2FA and OIDC for enhanced security

## Features Demonstrated

### People Management

The walkthrough showed creating person entries with:

- First name, last name (or initial)
- Nickname
- "Known through" field (connection reference)
- Relationship type to you
- Last contact date
- Important dates (birthdays, anniversaries)
- Reminders with customizable frequency
- Notes section

**Built-in relationship types:** Acquaintance, Child, Colleague, Friend, Other, Parent, Relative, Sibling, Spouse - plus custom types can be created.

### Relationship Connections & Visualization

**Bug discovered and fixed in real-time:**

The stream revealed an interesting bug where relationship visualization arrows were pointing incorrectly, causing confusion about parent/child relationships. Matto fixed this in real-time during the stream.

**Network graph features:**

- Interactive graph showing relationship connections
- Click nodes to view person details
- Arrow direction indicates relationship type
- Visual representation of family/friend network
- Different animations on each page load

### Groups & Organization

Custom groups for categorizing contacts (examples: Work, Friends, Relatives, Church, Disc Golf) make it easier to organize your network for easier navigation.

### Settings & Configuration

**Appearance:** Light and dark themes with full dark mode support.

**Languages:** English, Spanish, Japanese, Norwegian, German.

**Date formats:** Multiple format choices (MDY, DMY, YMD, etc.) with the user noting preference for DMY but acknowledging American MDY convention.

**Account management:** Password change, export data (JSON), import data, delete account.

## Technical Stack & Roadmap

**Technology stack (inferred):**

- **Backend:** Python with Django
- **Database:** PostgreSQL
- **Frontend:** JavaScript framework
- **Deployment:** Docker with docker-compose
- **Architecture:** Microservices (app, db, cron containers)

**Confirmed roadmap items:**

- CardDAV support (highly requested feature)
- Profile pictures for people
- Pictures in network visualization
- Advanced notification customization (user-defined timing)
- 2FA implementation
- OIDC implementation
- Export as genealogy tree format

**Current version:** 0.18.0 (upgraded from 0.14 during demo) - status is early development with breaking changes possible.

## Community & Self-Hosting Benefits

The stream highlighted why self-hosted solutions like Nametag are valuable:

- Complete data ownership and privacy
- No account limits
- No email service required (optional)
- Free forever for self-hosted version
- Active development with responsive developer engagement

## Comparison: Monica vs Nametag

| Feature | Monica | Nametag |
|---------|--------|----------|
| Maintenance | Minimal recent activity | Active development |
| Network Visualization | Basic (per video) | Interactive graph |
| Docker Support | Available | Native, multi-container |
| Documentation | Mixed quality | Very good balance |
| Custom Relationship Types | Yes | Yes |
| Groups | Yes | Yes |
| CardDAV | Yes | In development |
| AI Transparency | Not specified | Uses Claude (transparent) |

## Limitations & Challenges

**Current limitations:**

- Manual person entry (no bulk import from contacts initially)
- Picture support not yet implemented (on roadmap)
- Notification customization uses fixed intervals only, not user-customizable
- Multi-user scenarios not well-defined (data sharing complexity)
- Early development status means breaking changes possible between versions

**Bugs fixed during stream:**

- Relationship visualization arrows (direction confusion)
- Relationship type button UI bug

## Conclusion

Nametag represents a fresh, actively-developed alternative in the Personal Relationship Manager space with strong documentation, Docker-native deployment, and responsive developer engagement. While still early in development (breaking changes possible), the project shows promise for users seeking a modern self-hosted relationship management solution.

The stream demonstrated the value of early-stage open-source projects with direct developer interaction, real-time bug fixes, and community-driven feature development. The developer's transparency about using AI to accelerate development while maintaining human oversight sets a positive example for responsible AI usage in software development.

---

### References

- Full transcript: `/media/docs/output/youtube_Explorning_Nametag_A_New_Open-Source_PRM_in_Early__WNYJuh67jY4_20260215_170114.txt`
- Short summary: `/media/docs/output/youtube_Explorning_Nametag_A_New_Open-Source_PRM_in_Early__WNYJuh67jY4_20260215_170114_summary_short.md`
- Video: [Exploring Nametag](https://www.youtube.com/watch?v=WNYJuh67jY4)