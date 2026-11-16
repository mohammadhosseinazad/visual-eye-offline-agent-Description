# Visual Eye — Project Handover

**Project:** Visual Eye  
**Creator and original author:** Muhammad-Hossein Azad (محمدحسین آزاد)  
**Contact:** mohammadhosseinazad3@gmail.com  
**Project slogan:** See more. Smile more.  
**Documentation status:** Handover baseline, 2026-11-16

## Purpose

Visual Eye is a family of related visual-analysis experiences. The repository currently documents two distinct deliverables. They must not be confused or represented as one runtime:

1. **Visual Eye Offline Agent v1.3 Beautiful UI** — a local-first web workspace for image upload, guided analysis, recommendations, session state, and optional local AI integrations.
2. **Visual Eye for ChatGPT / MCP v1.1.2** — a hosted MCP interface and workflow-state service. It exposes a touch-first workflow but does not itself perform computer-vision inference, image generation, pixel editing, or eye tracking.

## Ownership and attribution

Retain the original creator attribution in source headers, UI credits, documentation, release notes, and derivative-work notices. A company or contributor may maintain or extend the project, but must not remove or misrepresent the original authorship. Any future ownership, licensing, or commercial arrangement should be documented in a signed agreement with the creator.

## Repository map

- `README.md` — public project overview and release status.
- `docs/` — engineering, operations, security, QA, contribution, and handover documentation.
- `chatgpt-app/` — documentation for the separate hosted MCP interface, privacy, terms, and submission preparation.
- `RELEASE_BLOCKERS.md` — known pre-release blockers for Offline Agent v1.3.
- `THIRD_PARTY_LICENSE_REVIEW.md` — preliminary dependency/model license inventory.

## Current known endpoints

- MCP endpoint: https://visual-eye-v.onrender.com/mcp
- Health endpoint: https://visual-eye-v.onrender.com/healthz
- ChatGPT integration documentation: [chatgpt-app/README.md](../chatgpt-app/README.md)

The hosted service is deployed on Render. The health endpoint and MCP protocol have passed earlier direct checks, but the latest deployment and in-ChatGPT rendering must be rechecked before claiming current production readiness.

## Version and release truth

- Offline Agent: **v1.3 Beautiful UI — pre-release candidate**, not a stable production release. Its source archive was recovered and archive integrity and a limited set of Linux/Python 3.13 tests passed. The source archive itself is not yet committed in this public repository.
- Hosted MCP interface: **v1.1.2 code/documentation baseline**. Earlier direct MCP protocol tests passed. Post-commit deployment verification, actual ChatGPT UI rendering, and directory approval remain unconfirmed.
- No public App Directory approval is claimed.

## Handover checklist for an adopting company

- [ ] Obtain the complete original source archive and verify its checksum with the creator.
- [ ] Confirm repository access, ownership, licensing, and written permission for the intended commercial use.
- [ ] Review all source code and reproduce the build from a clean environment.
- [ ] Reconcile source version, release notes, dependencies, and deployed service version.
- [ ] Complete third-party software, model, workflow, and asset license review.
- [ ] Create a software bill of materials (SBOM) and vulnerability report.
- [ ] Review privacy, retention, security boundaries, and data flows.
- [ ] Run the full QA matrix on supported operating systems and browsers.
- [ ] Establish maintainers, issue triage, release signing, backup, and incident response.
- [ ] Publish only after all release blockers are closed and evidence is attached.

## What this handover does not imply

This document is not proof of a stable release, a security audit, legal clearance, ownership transfer, or App Directory approval. Unknowns are deliberately recorded as unknowns rather than guessed.