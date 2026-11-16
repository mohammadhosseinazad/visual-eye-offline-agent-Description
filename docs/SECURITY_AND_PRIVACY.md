# Security and Privacy Guidance

## Security posture

This document describes known limitations, not a security certification.

### Offline Agent

- The built-in HTTP server does not provide user authentication or TLS.
- It is intended to remain bound to loopback on the local computer.
- Do not expose it to LAN or public internet.
- Optional Ollama and ComfyUI endpoints must be secured and reviewed separately.
- Uploaded images, generated outputs, and session history are stored in the local application data directory.
- The application does not currently include a complete in-app retention manager.

### Hosted MCP interface

The MCP service provides workflow controls/state. The documented design does not send image bytes to the MCP tool; image understanding is handled by the connected ChatGPT experience when available. Reconfirm this data flow against source code before changing the privacy statement or adding new tools.

## Minimum security requirements before production

- Bind local services to loopback unless authenticated network access is implemented.
- Add authentication, authorization, TLS, CSRF/origin protections, and rate limiting before any network exposure.
- Validate and constrain image file types, dimensions, file sizes, and parsing behavior.
- Keep temporary files and session data in a controlled directory with restrictive permissions.
- Define retention, deletion, backup, and recovery behavior.
- Avoid logging image contents, tokens, credentials, or personal data.
- Store secrets in deployment secret managers, not source code or repository files.
- Pin dependencies and container images; scan for vulnerabilities.
- Review model files, custom nodes, workflows, and third-party binaries before execution.
- Conduct an independent security review before production deployment.

## Privacy review questions for an adopting organization

1. What image data is stored, where, and for how long?
2. Who can access local session directories and generated outputs?
3. Are any optional model runtimes configured to call external services?
4. Are logs free of image payloads and credentials?
5. Can a user delete a session and all derived files?
6. Are backups encrypted and subject to a retention schedule?
7. Are notices and consent appropriate for images containing people or confidential material?

## Responsible-use limitations

Visual Eye is a visual-assistance and design-feedback tool, not a medical, forensic, biometric identification, or clinical attention-measurement system. An educational attention estimate is a heuristic visualization and must never be represented as measured eye tracking.

## Vulnerability reporting

Please report suspected security issues privately to the project maintainer before publishing exploit details. Do not include credentials, private images, or sensitive personal data in public issues. The public issue tracker is for general bugs and feature requests, not secret disclosure.