# Visual Eye — Open Source Project

**Creator:** Muhammad-Hossein Azad  
**Contact:** mohammadhosseinazad3@gmail.com  
**Project:** Visual Eye Offline Agent v1.3 Beautiful UI  
**License:** Apache-2.0 for original project materials; third-party components retain their own licenses.

Visual Eye is a local-first visual analysis workspace. The application source, Persian interface, English UI preview, analysis engine, setup scripts, Docker files, documentation, and tests are now published in this repository.

## Get the source

- [Offline Agent source code](source/v1.3/01_Offline_Agent/)
- [English README and quick start](source/v1.3/01_Offline_Agent/README_EN.md)
- [Persian installation guide](source/v1.3/01_Offline_Agent/01_INSTALL_GUIDE.html)
- [Persian user guide](source/v1.3/01_Offline_Agent/02_USER_GUIDE.html)
- [Security notes](source/v1.3/01_Offline_Agent/11_SECURITY_NOTES.html)
- [Release blockers](source/v1.3/RELEASE_BLOCKERS.md)
- [Third-party license review](source/v1.3/THIRD_PARTY_LICENSE_REVIEW.md)

Use GitHub's **Code → Download ZIP** to download the repository source.

## Quick start

Read the installation guide first.

- Windows: run `source/v1.3/01_Offline_Agent/RUN_WINDOWS.bat`.
- Linux/macOS: run `chmod +x source/v1.3/01_Offline_Agent/RUN_LINUX_MAC.sh && ./source/v1.3/01_Offline_Agent/RUN_LINUX_MAC.sh`.
- Default local address: `http://127.0.0.1:8765`.
- Python 3.10+ is recommended. Install the dependencies listed in `requirements.txt`.

Optional AI integrations require separately installed Ollama and/or ComfyUI services and separately downloaded model assets. Those large model files and offline dependency bundles are not included.

## Important safety notice

**v1.3 is a pre-release candidate, not a production-hardened server.** The built-in HTTP service has no user authentication or TLS and is intended for local loopback use only. Do not expose it to a LAN, VPN, public IP, reverse proxy, or the Internet. Keep the bind address at `127.0.0.1`.

The included tests passed in the available Linux/Python 3.13 environment, but this does not certify cross-platform compatibility, production security, model quality, or a fully offline installation. Read the security, privacy, and release-blocker documents before use or redistribution.

## Included checks

From `source/v1.3/01_Offline_Agent/`:

```bash
python -m compileall -q .
python SELF_TEST.py
python E2E_TEST.py
python SECURITY_TEST.py
python SESSION_SECURITY_TEST.py
```

## Other project materials

- [Master Prompt Studio](source/v1.3/02_Master_Prompt_Studio/)
- [Academy Masterclass references and status](source/v1.3/03_Academy_Masterclass/)

*See more. Smile more.*
