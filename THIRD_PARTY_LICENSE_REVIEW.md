# Third-party license review — preliminary

This is a technical inventory, not legal advice or final redistribution clearance. The Apache-2.0 license in the source package applies only to original Visual Eye project materials; it does not relicense third-party software, models, model weights, workflows, or assets.

## Components identified

| Component | Project use | Review status |
|---|---|---|
| NumPy | Required Python dependency | BSD 3-Clause; exact wheel and bundled notices still need review |
| OpenCV / opencv-python-headless | Required image processing dependency | Upstream Apache-2.0; exact wheel and bundled native notices still need review |
| Ollama | Optional local model runtime | MIT upstream; pin exact image/version and preserve notices |
| ComfyUI | Optional external image-generation/editing backend | GPL-3.0 upstream; separately installed, not included in the archive |
| Qwen3-VL 8B | Recommended vision model through Ollama | Model card indicates Apache-2.0; verify exact model manifest and digest |
| Qwen Image Edit 2511 | Model downloaded by ComfyUI helper script | Model card indicates Apache-2.0; verify exact checkpoint and accompanying assets |
| Qwen VAE, text encoder, Lightning LoRA | Downloaded as separate model assets | Exact files and redistribution terms not fully verified; do not mirror or redistribute pending review |

## Required before stable release

1. Freeze exact Python dependency versions and inspect platform wheels and bundled native libraries.
2. Pin Ollama and Docker base images by immutable digest.
3. Verify model manifests, revisions, hashes, and license terms.
4. Review every ComfyUI custom node and workflow dependency individually.
5. Preserve required copyright, license, attribution, and NOTICE files.
6. Obtain qualified legal review of the final distribution model, particularly for GPL components and model assets.

**Conclusion:** Keep the release labeled pre-release. Do not claim that all third-party components or model assets are cleared for redistribution.
