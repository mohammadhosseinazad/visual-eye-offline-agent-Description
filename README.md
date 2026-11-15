# Visual Eye — Offline Agent

**Visual Eye Offline Agent v1.3 Beautiful UI** is a local-first visual analysis workspace created by **Mohammad Hossein Azad**.

The project is designed to help users load and analyze images through a local web interface. Its documented workflow includes **Quick**, **Deep**, and **Custom** analysis modes, image validation, session handling, and local result generation.

## Project status

- Repository: Public
- Current release target: v1.3
- Source package: pending final upload and verification
- License: not yet assigned; see [License and third-party notices](#license-and-third-party-notices)

> This repository is being prepared for the verified v1.3 source release. Until the source files and dependency notices are uploaded, this README is an overview and not a complete installation guide.

## Main capabilities

- Local web-based interface for image analysis
- Quick, Deep, and Custom analysis workflows
- Image input validation and session management
- Local result generation
- Optional integration with [Ollama](https://ollama.com/) for local vision-model inference
- Optional integration with [ComfyUI](https://www.comfy.org/) for compatible image-generation or editing workflows

## Offline operation

Visual Eye is intended for local-first use. Actual offline operation depends on the required application dependencies, model weights, and any optional services being installed and available locally before disconnecting from the internet. Optional ComfyUI workflows also require compatible workflows and models.

## Important scope note

Visual Eye's built-in analysis and design guidance should not be confused with direct generative pixel editing. Generative image workflows require a separately configured ComfyUI service, a compatible workflow, and the required models.

## Installation

A verified, version-specific installation guide will be added with the v1.3 source package. Please do not rely on commands or setup steps from older versions until that guide is published.

## Security and privacy

- Keep image files and generated results in locations you control.
- Review configuration before exposing the local service to a network.
- Do not expose development servers or model endpoints to the public internet without appropriate authentication and network controls.
- Report suspected security issues privately to the project maintainer rather than publishing sensitive exploit details in an issue.

## License and third-party notices

No open-source license has been assigned to this repository yet. Until a license file is added, all rights are reserved by the copyright holder to the extent permitted by applicable law. The presence of a public GitHub repository does not by itself grant permission to reuse, modify, or redistribute the code.

Before release, third-party libraries, models, model weights, workflows, and assets must be reviewed individually and their required notices included.

## Maintainer

**Mohammad Hossein Azad**  
Contact: mohammadhosseinazad3@gmail.com

---

*See more. Smile more.*
