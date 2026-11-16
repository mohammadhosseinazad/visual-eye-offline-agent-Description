# Deployment and Operations Runbook

This runbook records safe operational boundaries and known endpoints. It is not a substitute for inspecting the exact source revision and deployment configuration.

## 1. Offline Agent v1.3

### Current state

- Release label: pre-release candidate.
- Normal local UI address documented by the project: `http://127.0.0.1:8765`.
- The recovered ZIP passed an archive integrity check and a limited test suite in Linux/Python 3.13.
- The source archive, complete offline dependency cache, container images, Ollama model blobs, ComfyUI installation, and model weights are not currently included in this public repository.

### Safe installation principle

Do not invent commands or install dependencies from an unverified source. Obtain the exact source archive and its original install guide, verify its checksum, inspect the included README and scripts, then reproduce installation in a disposable test environment first.

### Network boundary

The built-in HTTP server has no user authentication or TLS. Keep it bound to loopback. Do not expose port 8765 to a LAN, reverse proxy, or public internet until authentication, TLS, authorization, and security testing have been implemented.

### Truly offline setup

A truly offline installation requires a connected staging machine to prepare and verify:
- platform-specific Python wheels;
- pinned container images and digests, if Docker is used;
- Ollama runtime and exact model blobs;
- ComfyUI runtime, workflows, custom nodes, and model assets;
- checksums, licenses, and installation instructions.

Transfer and test these assets on each supported target OS. The current archive alone is not a complete offline bundle.

## 2. Hosted MCP service

### Known service URLs

- MCP: https://visual-eye-v.onrender.com/mcp
- Health: https://visual-eye-v.onrender.com/healthz

### Routine checks

1. Open the health endpoint and record the response and timestamp.
2. Inspect the Render deployment event and deployed commit.
3. Run MCP initialize and tools/list against the deployed endpoint.
4. Run the documented `visual-eye.render` test with valid and invalid inputs.
5. Verify resource discovery/read if those resources are part of the current implementation.
6. Test actual UI rendering in a supported ChatGPT client.
7. Record logs, test results, and any regressions without exposing secrets.

Earlier protocol checks passed, but repeat these checks after every deployment. A healthy endpoint alone does not prove ChatGPT UI compatibility.

### Render environment configuration

The MCP code includes a domain-verification route that is conditional on an environment variable named `OPENAI_APPS_CHALLENGE_TOKEN`. The value must be obtained through the legitimate OpenAI developer workflow and configured securely in Render only if required. Never commit the token to GitHub or include it in screenshots/logs. A missing token is expected to leave the route unavailable.

Do not assume that configuring this token completes developer verification, regional eligibility, app review, or public listing approval.

## 3. Backups and recovery

- Keep an immutable copy of each source archive and its SHA-256 checksum.
- Tag source revisions corresponding to deployed versions.
- Export deployment configuration without secret values.
- Keep a record of Render service identity, deployment commit, runtime logs, and rollback target.
- Back up user data only with the user's informed consent and a documented retention policy.
- Test restoration before calling a backup valid.

## 4. Incident response

For a suspected compromise: restrict public exposure, rotate affected secrets in their issuing systems, preserve relevant logs, identify the deployed commit, roll back to a known-good revision if needed, and document impact. Do not paste secrets into GitHub issues.