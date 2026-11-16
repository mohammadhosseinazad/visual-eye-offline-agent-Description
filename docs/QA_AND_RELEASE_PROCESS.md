# QA Matrix and Release Process

## Test evidence currently recorded

### Offline Agent v1.3

The recovered source archive passed:
- ZIP integrity check;
- Python compilation in Linux/Python 3.13;
- `SELF_TEST.py`;
- `E2E_TEST.py`;
- `SECURITY_TEST.py` for the included loopback Host/Origin and browser security-header checks.

These results are limited to the available environment. They do not establish Windows/macOS compatibility, full offline operation, production readiness, or an independent security audit.

### Hosted MCP v1.1.2

Earlier direct tests passed for:
- MCP initialization;
- tool discovery;
- resource discovery and read;
- a direct `visual-eye.render` tool call;
- health endpoint availability at the time of testing.

Still unconfirmed:
- post-commit deployed revision and current health;
- actual UI rendering in ChatGPT clients;
- complete end-to-end user journey;
- public App Directory review/approval.

## Recommended QA matrix

| Area | Test | Evidence required |
|---|---|---|
| Installation | Clean install on each supported OS | OS version, commands, logs |
| Startup | Start/stop/restart | logs and exit codes |
| Image validation | valid, oversized, malformed, unsupported files | expected error/result |
| Workflows | Quick, Deep, Custom | screenshots and test records |
| Local inference | Ollama configured/unavailable | model ID, output, fallback behavior |
| Generative workflow | ComfyUI configured/unavailable | workflow ID, output, failure handling |
| Data handling | session persistence and deletion | file-system evidence |
| Network safety | loopback-only binding | listening sockets and regression tests |
| MCP protocol | initialize, tools/list, resources/read, tool call | request/response fixtures |
| ChatGPT UI | launch and render on supported clients | screen recording and client/version |
| Localization | Persian RTL and English | screenshots and language QA |
| Recovery | backup and restore | verified restore record |

## Release gates

A release may be called stable only after:
1. Source archive is committed and tagged.
2. Reproducible clean installation is documented.
3. Dependencies and container images are pinned.
4. Third-party and model license review is complete.
5. Supported OS/browser matrix passes.
6. Security and privacy blockers are resolved.
7. User documentation and support process are complete.
8. SBOM, checksums, and signed artifacts are published.
9. Release notes list known limitations and test evidence.

## Versioning

Use semantic versioning where practical. Do not reuse a version number for materially different builds. Tag the exact commit used for each release and attach checksums to binary/source archives.

## Test report template

- Product and version:
- Commit SHA:
- Test date/time and timezone:
- OS / runtime / browser:
- Test case:
- Steps:
- Expected result:
- Actual result:
- Pass / fail / blocked:
- Logs or screenshot reference:
- Tester:
