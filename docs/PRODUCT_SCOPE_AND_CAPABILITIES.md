# Product Scope and Capability Boundaries

## Product family

Visual Eye currently has two separate implementations.

### A. Offline Agent v1.3 Beautiful UI

A local-first workspace with a web interface, normally configured for loopback access at `http://127.0.0.1:8765`. The documented workflows include Quick, Deep, and Custom analysis; image validation; local session state; design recommendations; and local output generation.

Optional integrations:
- **Ollama** for local vision-model inference.
- **ComfyUI** for separately configured image-generation or image-editing workflows.

These integrations require their own runtime, model files, workflows, configuration, and license review. They are not automatically bundled with the recovered source archive.

### B. ChatGPT MCP interface v1.1.2

A hosted MCP service exposing the `visual-eye.render` tool and a Persian right-to-left touch interface. It provides workflow controls and state. It does not itself process image pixels or run the Offline Agent's Ollama/ComfyUI stack.

Image understanding, if available in a ChatGPT session, is performed by the connected ChatGPT experience. Image generation or editing depends on separate ChatGPT capabilities or separately configured services.

## Capability truth table

| Capability | Offline Agent | ChatGPT MCP interface |
|---|---|---|
| Guided visual-analysis workflow | Yes, documented | Yes, via workflow UI |
| Local image upload/session handling | Yes | Not performed by MCP tool |
| Local vision inference | Optional Ollama integration | No |
| Image generation/editing | Optional ComfyUI integration | No, not by MCP service itself |
| Eye tracking | No | No |
| Measured gaze/attention heatmap | No | No |
| Educational attention estimate | May be presented as heuristic only | May be presented as heuristic only |
| Fully offline operation out of the box | No; dependencies/models are missing | No; hosted MCP service requires network |

## User-facing claims

Use accurate wording such as “guided visual analysis”, “design recommendations”, and “optional local model integration”.

Do not claim:
- real eye tracking, measured gaze, clinical diagnosis, or validated human-attention measurement;
- that the MCP server itself performs vision inference or image editing;
- that the recovered Offline Agent archive is fully offline-ready;
- production certification, security audit completion, or cross-platform compatibility without evidence.

## Intended future users

Designers, educators, creators, developers, and teams who want structured feedback about visual composition and image presentation. Any high-stakes or professional use should be independently validated for that domain.