# Visual Eye — ChatGPT App Directory Listing Metadata

**Document status:** Submission draft; not an approval or publication confirmation.  
**Developer:** Mohammad Hossein Azad  
**Publication type:** Individual developer  
**Intended availability:** Worldwide, subject to OpenAI eligibility, applicable law, and country availability controls.  
**Public contact:** mohammadhosseinazad3@gmail.com

## Listing fields

- **App name:** Visual Eye
- **Developer display name:** Mohammad Hossein Azad
- **Short description:** A guided visual-inspection workflow and touch-friendly interface for ChatGPT.
- **Category suggestion:** Productivity (or the closest available category in the submission portal).
- **Website:** https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/tree/main/chatgpt-app
- **Support:** https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/issues
- **Privacy policy:** https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/blob/main/chatgpt-app/PRIVACY.md
- **Terms of service:** https://github.com/mohammadhosseinazad/visual-eye-offline-agent-Description/blob/main/chatgpt-app/TERMS.md
- **MCP server:** https://visual-eye-v.onrender.com/mcp
- **Health check:** https://visual-eye-v.onrender.com/healthz

## Long description

Visual Eye adds a guided, touch-friendly workflow for reviewing images in ChatGPT. Users attach an image in the ChatGPT conversation and use Visual Eye's interface to choose a focused or more detailed review. The workflow helps organize visual feedback around composition, hierarchy, and design observations.

The Visual Eye MCP service supplies the interface and workflow state. It does not independently receive image-file bytes, run computer-vision inference, generate or edit image pixels, or perform measured eye tracking. Image interpretation and any image-generation capabilities depend on ChatGPT and the capabilities enabled in the user's experience. Any attention-path or heatmap-style explanation is an educational estimate, not a measured eye-tracking result.

## Suggested first-run prompt

"Use Visual Eye to guide a structured review of the image I attached. Start with a concise overview, then identify the most important visual strengths and possible improvements."

## Listing assets and declarations still required

- Demo recording URL: **Pending** — must be a publicly accessible recording of the real app workflow.
- Domain challenge token: **Pending** — obtain the exact token from the OpenAI submission portal and set it as the Render environment variable `OPENAI_APPS_CHALLENGE_TOKEN`.
- Developer identity verification: **Pending** — complete directly in the official OpenAI developer portal.
- Tool scan: **Pending final scan after the current code is deployed**.
- App policy and capability attestations: **Pending developer review and confirmation in the portal**.

Do not submit placeholder values for pending items. Select only countries in which the developer and app are eligible under current OpenAI requirements and applicable law; "worldwide" is an intended audience, not an exemption from country restrictions.
