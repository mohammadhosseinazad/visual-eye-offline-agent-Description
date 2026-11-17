# Visual Eye — Offline Agent

**Visual Eye Offline Agent v1.3 Beautiful UI** is a local-first visual analysis workspace created by **Muhammad-Hossein Azad**.

## Source package

The complete v1.3 source archive has been recovered from the project files, cleaned of test uploads, generated outputs, session records, local path pointers, and Python cache files, and validated. It contains the Offline Agent source, Persian interface, English UI preview, engine, setup scripts, Docker files, guides, tests, and the supplied Master Prompt Studio and Academy reference materials.

**The source tree has not yet been committed to this GitHub repository.** A clean archive is available in the current ChatGPT conversation as `Visual_Eye_v1.3_Source_Clean.zip`. Its SHA-256 is:

`24eb1237f29e10f4c4fa32de27d08ab1975be444cd53e452a96fea5a2820034b`

The ZIP passed its archive integrity check. In the available Linux/Python 3.13 environment, Python compilation, `SELF_TEST.py`, `E2E_TEST.py`, `SECURITY_TEST.py`, and `SESSION_SECURITY_TEST.py` passed. These checks do not certify cross-platform compatibility, independent security, or production readiness.

## Main capabilities

- Local web interface, normally at `http://127.0.0.1:8765`
- Quick, Deep, and Custom analysis workflows
- Image validation and local session state
- Design recommendations and local output generation
- Optional local vision analysis through Ollama
- Optional image-generation/editing integration through ComfyUI
- Docker Compose files and Windows/Linux/macOS helper scripts

The built-in analysis and design outputs are not equivalent to generative pixel-level image editing. Generative editing requires a separately installed and configured ComfyUI service, a compatible workflow, and model assets.

## Important security limitation

The built-in HTTP server does not provide user authentication or TLS. It is intended for localhost use only. Do not expose it to a LAN or the public internet. The server rejects non-loopback binding in its current configuration.

## Offline operation

The clean source archive does not include Python wheel bundles, container images, Ollama model blobs, ComfyUI installation, or model weights. A truly offline deployment requires preparing and verifying all platform-specific dependencies and model assets separately.

## Licensing

The source archive includes an Apache License 2.0 for original Visual Eye project materials. Third-party software, models, assets, and custom nodes retain their own licenses; redistribution review is still required.

## Separate ChatGPT interface

The hosted MCP touch interface is a separate deliverable from the Offline Agent. Its secure setup workflow is described in [docs/SERVER_SETUP_AND_AUTO_CONNECT.md](docs/SERVER_SETUP_AND_AUTO_CONNECT.md).

*See more. Smile more.*
