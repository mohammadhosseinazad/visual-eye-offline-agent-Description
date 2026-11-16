# Visual Eye — Offline Agent

**Visual Eye Offline Agent v1.3 Beautiful UI** is a local-first visual analysis workspace created by **Muhammad-Hossein Azad**.

It provides a locally hosted web interface for image upload, guided analysis, design recommendations, session memory, and local output generation.

## Release status

**Version:** 1.3 Beautiful UI  
**Status:** Pre-release candidate — not a stable production release  
**Creator:** Muhammad-Hossein Azad  
**Contact:** mohammadhosseinazad3@gmail.com

The v1.3 source archive has been recovered and its ZIP integrity verified. Core self-test, end-to-end workflow test, Python compilation, and the included loopback security regression test passed in the available Linux/Python 3.13 environment. These checks do not certify cross-platform compatibility, independent security, or production readiness.

The source package is not yet committed to this repository. The repository currently contains this project overview only.

## Main capabilities

- Local web interface, normally at `http://127.0.0.1:8765`
- Quick, Deep, and Custom analysis workflows
- Image validation and local session state
- Design recommendations and local output generation
- Optional local vision analysis through Ollama
- Optional image-generation/editing integration through ComfyUI
- Docker Compose files and Windows/Linux/macOS helper scripts

The built-in analysis and design outputs are not the same as generative pixel-level image editing. Generative editing requires a separately installed and configured ComfyUI service, a compatible workflow, and model assets.

## Offline operation

The application is local-first, but the recovered ZIP does **not** include the Python wheelhouse, container images, Ollama model blobs, ComfyUI installation, or model weights. A truly offline deployment requires preparing and verifying all platform-specific dependencies and model assets on a connected staging machine first.

## Important security limitation

The built-in HTTP server does not provide user authentication or TLS. It is intended to remain bound to loopback on the local computer. Do not expose it to a LAN or the public internet. Optional Ollama and ComfyUI endpoints must also be secured and reviewed separately.

## Privacy

Uploaded images, generated outputs, and session history are stored locally in the application's data directory. The application does not include a complete in-app retention manager. Review the privacy documentation before using it with sensitive images.

## Licensing

The recovered source package contains an Apache License 2.0 for original Visual Eye project materials. That license does not automatically cover third-party software, AI models, model assets, or custom nodes. The package's third-party license inventory is preliminary and redistribution review remains incomplete.

## Before a stable public release

- Complete dependency, container-image, model, and asset license review.
- Pin exact dependency versions and container image digests.
- Test clean installations on supported Windows, Linux, and macOS systems.
- Complete English localization and bilingual QA.
- Prepare a software bill of materials and final signed checksums.
- Obtain the missing Academy Masterclass application source, if that component is to be included.

## Project slogan

*See more. Smile more.*


## Separate ChatGPT interface

A separate hosted MCP touch interface for the Visual Eye workflow is documented in [chatgpt-app/](chatgpt-app/). This ChatGPT integration is distinct from the local-first Offline Agent described above; it provides workflow controls and does not itself run the local Ollama/ComfyUI stack.

- [ChatGPT app overview](chatgpt-app/README.md)
- [ChatGPT app privacy policy](chatgpt-app/PRIVACY.md)
- [ChatGPT app terms of use](chatgpt-app/TERMS.md)
- [Support and issue tracker](https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/issues)


## Engineering documentation and company handover

The following documents are maintained for developers, companies, and teams evaluating or adopting Visual Eye:

- [Project handover and adoption checklist](docs/PROJECT_HANDOVER.md)
- [Product scope and capability boundaries](docs/PRODUCT_SCOPE_AND_CAPABILITIES.md)
- [Architecture and data flow](docs/ARCHITECTURE.md)
- [Deployment and operations runbook](docs/DEPLOYMENT_AND_OPERATIONS.md)
- [Security and privacy guidance](docs/SECURITY_AND_PRIVACY.md)
- [QA matrix and release process](docs/QA_AND_RELEASE_PROCESS.md)
- [Product roadmap and open work](docs/ROADMAP.md)
- [Contributor and maintainer guidelines](CONTRIBUTING.md)
- [Known release blockers](RELEASE_BLOCKERS.md)
- [Preliminary third-party license review](THIRD_PARTY_LICENSE_REVIEW.md)

**Important handover note:** These documents intentionally distinguish verified facts from open work. The Offline Agent v1.3 source archive is not yet committed to this repository, and the hosted MCP interface is a separate deliverable. A company considering adoption should follow the handover checklist and confirm source, rights, dependencies, and test evidence with the original creator.
