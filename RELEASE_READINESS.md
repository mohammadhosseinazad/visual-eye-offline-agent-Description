# Visual Eye Offline Agent v1.3 — Release Readiness

**Status: pre-release candidate; not stable or production-certified.**

## Verified in the available Linux/Python 3.13 environment
- Python compilation (`compileall`)
- Core self-test
- End-to-end session, upload, analysis, analytical output, final output, and design-spec workflow
- Loopback Host/Origin and response-header regression checks
- Session-file path/schema validation added during final hardening

## Security hardening in this revision
- Session image paths are accepted only when they resolve to an existing file under `01_Offline_Agent/data/uploads`.
- Session records reject malformed or oversized user-flow arrays and ignore unknown serialized fields.
- User-flow input is validated before the session record is persisted.
- User brief text is limited to 4,000 characters.
- Memory event limits are type-checked and clamped to 1–500.

## Remaining release blockers
1. Full source tree and binary package must be committed/uploaded to GitHub; documentation-only commits do not constitute a source release.
2. Dependency versions and container base images need immutable pins and a clean dependency installation test.
3. Docker images/Compose flows need actual build and runtime testing.
4. Windows, Linux, and macOS clean-install tests remain outstanding; only Linux/Python 3.13 core tests have been run here.
5. Third-party library, container, model, model-asset, and custom-node license/redistribution review is preliminary.
6. Model files, offline wheelhouse, Docker images, Ollama, and ComfyUI are not bundled; full offline installation is not yet verified.
7. English localization and bilingual QA remain incomplete for generated content and some errors.
8. Academy Masterclass application source was not present in the recovered package.
9. Final SBOM, signed release artifacts, and independent security review remain outstanding.

## Network exposure warning
The built-in server has no authentication or TLS and must remain bound to loopback (`127.0.0.1` / `localhost`). Do not expose it to LAN or the public internet.

## Honest release decision
Do not label v1.3 as a stable public release until every blocker above is resolved and independently re-tested.