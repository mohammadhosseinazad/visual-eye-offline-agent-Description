# Visual Eye 1.3 — release blockers

**Status: Pre-release candidate. Not a stable production release.**

## Verified in the recovered package

- The original v1.3 ZIP archive was recovered from the user's existing Library files.
- ZIP integrity check passed: 131 archive entries; no corrupt member detected.
- Python compilation completed successfully in the available Linux environment.
- `SELF_TEST.py` passed.
- `E2E_TEST.py` passed.
- `SECURITY_TEST.py` passed its loopback Host/Origin and browser security-header checks.

These checks cover only the supplied test environment. They are not an independent security audit or cross-platform certification.

## Remaining work before a stable public release

1. Complete third-party dependency, Docker image, model, and asset license review.
2. Pin exact dependency versions and immutable container image digests.
3. Prepare platform-specific offline wheels and test clean installs on supported Windows, Linux, and macOS systems.
4. Pin model revisions, checksums, licenses, storage requirements, and hardware requirements. Model files are not included in the recovered ZIP.
5. Complete English localization and bilingual QA; some generated analysis and error messages may remain Persian.
6. Keep the built-in HTTP server on localhost. It has no user authentication or TLS; LAN/public exposure is unsupported.
7. Obtain the actual Academy Masterclass HTML/application if that component is intended for distribution.
8. Generate a final SBOM, checksums, and signed release artifacts after all release changes.
9. Upload the verified source package and supporting documents to the GitHub repository.

## Offline deployment limitation

The source archive does not include all platform-specific Python wheels, container images, Ollama model blobs, ComfyUI installation, or AI model weights. A truly offline installation requires preparing and verifying those assets on a connected staging machine before transfer.

## Recommendation

Publish only as a clearly labeled **v1.3 Pre-release** until the blockers above are addressed. Do not describe this package as a fully offline, production-certified release.
