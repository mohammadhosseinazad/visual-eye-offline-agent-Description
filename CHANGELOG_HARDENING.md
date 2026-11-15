# v1.3 pre-release hardening notes

- Validate persisted session image paths against the uploads directory and require the target file to exist.
- Validate session schema and user-flow array shape/size on load.
- Validate user-flow input before saving it to session state.
- Bound user brief length to 4,000 characters.
- Type-check and clamp memory event limits to 1–500.
- Re-run compile, self-test, end-to-end, and HTTP security regression suites after changes.

These changes improve input and local-state robustness; they are not a substitute for a full security audit or network authentication.