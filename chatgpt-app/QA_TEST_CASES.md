# Visual Eye — App Submission QA Test Cases

**Status:** Proposed test plan. These cases are not represented as executed or passed. Run them against the deployed endpoint and the actual ChatGPT app experience before submission.

## Positive test cases (5)

### P1 — MCP initialization
- **Setup:** Use a standards-compliant MCP client with network access.
- **Action:** Send an `initialize` request to `https://visual-eye-v.onrender.com/mcp`.
- **Expected:** A valid MCP initialization response is returned, including a supported protocol version and server capabilities.

### P2 — Tool discovery
- **Setup:** Complete initialization.
- **Action:** Call `tools/list`.
- **Expected:** The response lists `visual-eye.render` with a valid input schema and a clear description of its interface/workflow purpose.

### P3 — UI resource discovery and read
- **Setup:** Complete initialization.
- **Action:** Call `resources/list`, then read the advertised Visual Eye UI resource.
- **Expected:** The resource is discoverable and returns valid HTML for the Visual Eye interface. Check that Persian text displays correctly and that the page is usable at mobile and desktop widths.

### P4 — Render the initial workflow
- **Setup:** Complete initialization and discover the render tool.
- **Action:** Call `visual-eye.render` using a valid initial/target workflow input accepted by the current tool schema.
- **Expected:** The tool returns a successful structured response with the requested interface state and valid stage/title/options fields. No claim should be made that the MCP server itself analyzed an image.

### P5 — End-user guided image review
- **Setup:** Open the app in a ChatGPT experience that supports the integration and attach a non-sensitive sample image directly in the ChatGPT composer.
- **Action:** Start Visual Eye, choose Quick review, and ask ChatGPT for feedback; repeat with Deep review.
- **Expected:** The interface is visible and interactive, the selected workflow is clear, and ChatGPT provides image feedback based on the attached image and its available vision capability. Confirm the app does not ask users to upload image bytes to the MCP endpoint.

## Negative test cases (3)

### N1 — Invalid or missing required input
- **Action:** Send a render-tool request with a required field omitted or a value outside the declared schema.
- **Expected:** The server/client returns a controlled validation error or protocol-level invalid-parameters response. It must not crash or return a misleading successful render.

### N2 — Unsupported image payload assumption
- **Action:** Attempt to pass raw image-file bytes or an undeclared image-upload field to the MCP render tool.
- **Expected:** The request is rejected by schema validation or the unsupported field is not treated as an uploaded image. The app must not claim that the MCP service received or analyzed the image.

### N3 — Unavailable service
- **Action:** Simulate an unavailable endpoint or network timeout in the test client.
- **Expected:** The client displays a clear connection/unavailable state and does not fabricate analysis results or claim that the workflow completed.

## Evidence to capture

For each executed case, record:
- Date/time and environment
- Test case ID
- Pass/fail
- Sanitized request and response or screenshot
- App build/version and deployed commit
- Any defect and retest result

Do not include private user images, credentials, access tokens, or personal data in submission evidence.
