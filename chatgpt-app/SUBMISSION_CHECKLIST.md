# Visual Eye — Submission Checklist

Use this checklist in the official OpenAI developer submission portal. A checked item should mean it has actually been completed and verified.

## Prepared materials
- [x] App name, developer display name, intended individual publication, and contact email supplied by developer.
- [x] Draft listing metadata: `SUBMISSION_METADATA.md`.
- [x] Privacy policy: `PRIVACY.md`.
- [x] Terms of use: `TERMS.md`.
- [x] Five positive and three negative proposed test cases: `QA_TEST_CASES.md`.
- [x] Demo recording script: `DEMO_RECORDING_SCRIPT.md`.
- [x] Release notes draft: `RELEASE_NOTES_1.1.2.md`.

## Must be completed by developer / in portal
- [ ] Verify developer identity using the official verification flow and eligible original government-issued ID.
- [ ] Review and accept the applicable developer terms and policy attestations truthfully.
- [ ] Create the app draft and enter listing metadata.
- [ ] Enter the exact demo recording URL after recording and uploading the real demo.
- [ ] Obtain the domain challenge token from the portal.
- [ ] Set Render environment variable `OPENAI_APPS_CHALLENGE_TOKEN` to that exact token.
- [ ] Confirm `https://visual-eye-v.onrender.com/.well-known/openai-apps-challenge` returns the exact token as plain text.
- [ ] Confirm the live deployment is the intended commit/version.
- [ ] Run the portal tool scan and resolve all reported issues.
- [ ] Execute and document all eight test cases against the final deployed build.
- [ ] Select only countries/territories where the developer and app are eligible under OpenAI rules and applicable law.
- [ ] Submit for review.

## Not yet claimed as complete
A prepared checklist, source commit, successful earlier MCP smoke tests, or a live health endpoint does not mean the app has passed the final portal scan, completed identity/domain verification, or been published.
