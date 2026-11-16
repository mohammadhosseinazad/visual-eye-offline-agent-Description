# Visual Eye Roadmap

This roadmap separates confirmed work from proposed work. Items are not complete unless linked to a commit or test report.

## P0 — Preserve and make the project reproducible

- [ ] Commit the complete Offline Agent v1.3 source archive and its checksum after confirming the correct archive and redistribution rights.
- [ ] Preserve original creator attribution and license notices.
- [ ] Reconcile source files with the existing install guide and documentation.
- [ ] Publish exact dependency manifests and supported runtime versions.
- [ ] Tag the current MCP source revision and verify the deployed Render commit.
- [ ] Add automated CI for linting, tests, and packaging where the source permits.

## P1 — Complete release readiness

- [ ] Complete third-party dependency, model, workflow, and asset license review.
- [ ] Produce an SBOM and vulnerability scan.
- [ ] Build verified offline dependency bundles for each supported OS.
- [ ] Test clean installation on Windows, Linux, and macOS.
- [ ] Complete English localization and Persian/English QA.
- [ ] Define data retention and deletion behavior.
- [ ] Record end-to-end tests and a genuine demo recording.

## P2 — Improve security and usability

- [ ] Add authentication and TLS before any LAN/multi-user deployment.
- [ ] Add configurable upload limits and robust malformed-file handling.
- [ ] Add session management and user-controlled deletion.
- [ ] Improve accessibility, keyboard navigation, and RTL layout.
- [ ] Add diagnostics that redact secrets and private image content.
- [ ] Document hardware requirements and model selection.

## P3 — Ecosystem and adoption

- [ ] Prepare a company adoption pack and contributor onboarding guide.
- [ ] Define a transparent governance and maintainer process.
- [ ] Evaluate lawful distribution channels and platform eligibility before claiming availability.
- [ ] Consider integrations only after security, privacy, and license review.

## Explicitly not promised

- ChatGPT App Directory acceptance or availability.
- A fully offline package before all dependencies and model assets are bundled and tested.
- Real eye tracking or measured gaze analytics.
- Production certification or independent security audit until evidence exists.
