# Visual Eye — Downloads

Choose the experience that matches your device.

## Public product website

- [Open the Visual Eye multilingual website](https://mohammadhosseinazad.github.io/visual-eye-offline-agent-Description/)
- The landing page currently provides Persian, English, Arabic, Turkish, Russian, Spanish, French, German, and Simplified Chinese UI translations.
- The language selector is stored in the browser and supports right-to-left layout for Persian and Arabic.

## 1. Visual Eye Offline Agent

- [Open the official GitHub Releases page](https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/releases)
- [Browse source code and documentation](https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description)

The Offline Agent is a local-first source package with Windows and Linux setup guidance. The GitHub release page is the authoritative place to see which assets are currently published. Check the exact asset filename and release notes before downloading.

**Important distribution limits**
- The available package is source code, not a signed Windows installer or Linux package such as .deb/.rpm/AppImage.
- Platform-specific clean-install testing is still required.
- A complete offline bundle is not yet available: Python wheels, container images, Ollama model files, ComfyUI setup, and model weights are not all included.
- The built-in HTTP service is intended for localhost only. It has no built-in user authentication or TLS; do not expose it to a LAN or the internet.

## 2. Mobile / ChatGPT companion

- [Open the ChatGPT companion source repository](https://github.com/mohammadhosseinazad/visual-eye-touch-mcp-app)
- [Download the companion source ZIP](https://github.com/mohammadhosseinazad/visual-eye-touch-mcp-app/archive/refs/heads/main.zip)

This is a mobile-friendly ChatGPT/MCP source project, not a standalone Android APK or iOS app. It requires the supported ChatGPT/MCP hosting and setup path. App Directory listing or approval must not be claimed unless it is actually granted.

## Release readiness

The public website and its nine-language landing-page UI are available. The desktop package, standalone mobile installers, complete offline dependencies/models, security review, license review, and cross-platform certification remain separate release tasks. See [RELEASE_BLOCKERS.md](RELEASE_BLOCKERS.md) for the current checklist.

---
Created by **Muhammad-Hossein Azad**.
