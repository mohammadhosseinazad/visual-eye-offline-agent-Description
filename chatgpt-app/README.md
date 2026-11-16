# Visual Eye for ChatGPT — MCP App

**Visual Eye** is a touch-first visual-analysis workflow for ChatGPT, created by **محمدحسین آزاد (Mohammad Hossein Azad)**.

- MCP service: https://visual-eye-v.onrender.com/mcp
- Health check: https://visual-eye-v.onrender.com/healthz
- Support: https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/issues
- Contact: mohammadhosseinazad3@gmail.com

## What this app does

The MCP service exposes the `visual-eye.render` tool and a Persian right-to-left touch interface. The accompanying Visual Eye skill guides ChatGPT through target-image selection, Quick, Deep, and Custom workflows, visual hierarchy and composition analysis, and image-specific recommendations.

The MCP service provides the interface and workflow state only. It does **not** itself perform computer-vision inference, image editing, image generation, or eye tracking. Image understanding and any image generation/editing are handled by the connected ChatGPT experience and its available capabilities. Any attention map is an educational estimate, not measured eye-tracking data.

## Privacy and terms

- [Privacy policy](PRIVACY.md)
- [Terms of use](TERMS.md)

## Current release status

**MCP service code:** 1.1.2 (domain-verification route prepared; current deployment still needs a post-commit check)

The hosted MCP endpoint has passed health, initialization, tool discovery, resource discovery/read, and a direct `visual-eye.render` tool-call test. Rendering the interface inside ChatGPT and public directory approval are separate steps and are not claimed as completed.

**طراح برنامه: محمدحسین آزاد**

## App Directory submission preparation

- [Submission listing metadata](SUBMISSION_METADATA.md)
- [Positive and negative QA test cases](QA_TEST_CASES.md)
- [Demo recording script](DEMO_RECORDING_SCRIPT.md)
- [Release notes 1.1.2](RELEASE_NOTES_1.1.2.md)
- [Submission checklist](SUBMISSION_CHECKLIST.md)

- [Platform distribution eligibility status](PLATFORM_DISTRIBUTION_STATUS.md)
