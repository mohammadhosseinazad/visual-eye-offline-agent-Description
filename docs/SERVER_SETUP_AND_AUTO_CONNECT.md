# Server Setup & Auto Connect — shared product specification

Status: implementation specification; not yet an implemented installer.

This feature is shared by Visual Eye Offline Agent and the hosted Visual Eye ChatGPT app, but the two products have different trust boundaries.

## Product experience

The first-run wizard offers:
1. Set up a new server.
2. Connect to an existing server.
3. Run diagnostics / reconnect.

The wizard detects platform and capabilities, validates inputs, explains each change, and shows a final review before applying any server-side change. It must never silently open firewall ports, install untrusted packages, or expose a local-only service.

## Offline Agent — target implementation

### Supported deployment profiles
- Local-only: bind to 127.0.0.1; no LAN access.
- Private LAN: bind to a private interface only after enabling authentication, role-based authorization, TLS, origin/CSRF protections, rate limiting, and audit logging.
- Remote/VPS: HTTPS reverse proxy or managed TLS, firewall allow-listing, authentication, backups, and health monitoring.

### Setup workflow
1. Detect OS, architecture, runtime versions, free disk, memory, and available ports.
2. Show supported/unsupported checks and a preflight report.
3. Choose local, LAN, or remote profile.
4. Configure bind address, port, public base URL, TLS mode, admin account, and optional Ollama/ComfyUI endpoints.
5. Generate a one-time setup token and securely provision credentials. Never place secrets in command-line arguments, logs, browser local storage, or Git.
6. Install pinned dependencies and the service using a signed/reproducible package.
7. Configure service supervision (systemd on Linux; an appropriate Windows service wrapper on Windows).
8. Apply firewall changes only after explicit confirmation and only for the selected profile.
9. Run health, TLS, authentication, and dependency checks.
10. Save a redacted connection profile and show a QR code / copyable URL where appropriate.

### Auto Connect
- Store endpoint and non-secret metadata in the user's local profile.
- Store tokens in OS credential storage (Windows Credential Manager, macOS Keychain, Linux Secret Service); never plain text config.
- On launch, perform a bounded health check, authenticate, and reconnect with exponential backoff.
- Provide disconnect, forget endpoint, rotate credential, and revoke device controls.
- Clearly distinguish offline, unreachable, unauthorized, incompatible-version, and degraded states.

### Required endpoints / contract
- GET /healthz: version, readiness, and non-sensitive capability flags only.
- POST /api/setup/complete: one-time setup-token exchange; disable after success.
- POST /api/auth/session or standards-based OAuth/OIDC flow.
- GET /api/status: authenticated service status.
- GET /api/capabilities: versioned feature/capability document.
All mutating endpoints require authorization, CSRF/origin protection where cookie auth is used, input validation, and audit events. Do not expose an unauthenticated arbitrary shell/command endpoint.

### Security requirements
- The existing Offline Agent HTTP server is documented as loopback-only and without authentication/TLS. Do not expose it to LAN or Internet until the security controls above are implemented and independently tested.
- No arbitrary remote shell, no unrestricted file access, no user-supplied URL fetching from the server, no credentials in telemetry.
- Pin dependencies and container digests; verify package signatures and checksums.
- Use least privilege; service account must not run as root/Administrator.
- Back up configuration with secrets excluded or encrypted; document restore and credential rotation.

## ChatGPT / hosted MCP app — target implementation

The hosted MCP app is a workflow UI, not an installer running on a customer's server. It must not ask users to paste root passwords, SSH private keys, API tokens, or other server secrets into chat or widget state.

It can guide the user through deployment and collect a non-secret HTTPS endpoint. It may display the exact steps to add that endpoint as a remote MCP server in a supported host. A user must authorize that connection in the host's own connector settings. The widget cannot silently register itself as a connector or make a third-party ChatGPT account connect to an arbitrary endpoint.

For the user's self-hosted server, provide:
- deployment profile selection and generated non-secret configuration guidance;
- endpoint format validation in the UI (not a network fetch/proxy);
- a copyable endpoint and host-side connection instructions;
- clear states: setup not started, awaiting host authorization, connected (only when verified by host), failed;
- link to the server's own health page.

Do not add an unrestricted URL-fetch tool to the hosted MCP backend. That would create an SSRF and network-pivoting risk. If server-to-server verification is ever added, use a strict allow-list or a customer-controlled outbound agent and validate DNS/IP ranges on every redirect and connection.

## Shared compatibility model

Every server publishes a versioned capability document. Clients negotiate minimum supported API version and feature flags. A newer client must degrade gracefully when connected to an older server. Keep hosted MCP app and Offline Agent release/version numbers distinct.

## Acceptance criteria

- Clean install and upgrade tested on every declared OS.
- Setup can be cancelled and safely resumed.
- No secret appears in logs, URLs, browser storage, diagnostics, or Git.
- Local-only profile binds to loopback.
- LAN/remote profiles are blocked until authentication and TLS are enabled.
- Auto reconnect uses bounded exponential backoff and does not create request storms.
- Invalid certificates, expired/revoked credentials, incompatible versions, and unreachable servers have actionable messages.
- Uninstall and reset remove service artifacts while preserving user data only with explicit choice.
- Independent security review before production release.

## Current repository limitation

The public Offline Agent repository currently contains project documentation but not the complete v1.3 application source archive. Therefore this document defines the required implementation and must not be represented as a shipped installer or completed feature until the source is restored, code is added, and the acceptance tests pass.
