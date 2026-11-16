# Visual Eye for ChatGPT — Release Notes 1.1.2

**Release status:** Submission candidate; public approval and final deployment verification are pending.

## Included
- MCP endpoint for the Visual Eye guided workflow.
- `visual-eye.render` tool for returning structured workflow/interface state.
- Discoverable UI resource serving the touch-friendly interface.
- Persian right-to-left interface content.
- Health-check endpoint.
- Prepared route for the OpenAI app-domain challenge, gated by the `OPENAI_APPS_CHALLENGE_TOKEN` environment variable.
- Public privacy policy, terms of use, and support issue tracker.

## Clarifications
- The MCP service provides the interface and workflow state; it does not itself perform image inference, image generation, pixel-level editing, or measured eye tracking.
- Users attach images directly in ChatGPT. Image interpretation depends on ChatGPT's available capabilities.
- The domain-challenge route will not verify until the exact token from the OpenAI submission portal is configured in the hosting environment.

## Verification still required
- Deploy the current 1.1.2 source changes and confirm the live health response.
- Confirm the domain challenge returns the exact portal token as plain text.
- Run the final tool scan and all test cases in `QA_TEST_CASES.md`.
- Verify the UI renders correctly inside the supported ChatGPT app environment.
- Record and publish the demo video.
- Complete developer identity verification and submission attestations.
