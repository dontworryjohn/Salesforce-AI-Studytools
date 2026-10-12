# Agentblazer trails → Agentforce Specialist topics

Snapshot of the 2026 Agentblazer status trails, grouped into exam-style topics. Trails change each year and sometimes mid-year, so on every run re-fetch the three trail manifests with `fetch_content` and:
- slot any module not listed here into the closest topic by its title and description;
- drop modules that are no longer in the trail.

Skip children whose `contentType` is `link` (videos, surveys, community invites, news articles).

Trails (fetch each with `fetch_content`, `expand: false`):
- Champion: `become-an-agentblazer-champion-2026`
- Innovator: `become-an-agentblazer-innovator-2026`
- Legend: `become-an-agentblazer-legend-2026`

Use the prefix in front of each module (C, I or L) to tell which trail it comes from. Superbadges (`superbadge-…`) return metadata only, so take facts from the modules they build on.

## 1. AI and agent fundamentals
- C: `artificial-intelligence-fundamentals`, `generative-ai-basics`, `natural-language-processing-basics`, `large-language-models`, `ai-fluency-fundamentals`, `reasoning-in-artificial-intelligence`, `autonomous-agents`
- C: `introduction-to-agentforce`, `einstein-copilot-basics` (Agentforce Basics), `new-agentforce-builder-quick-look`, `introduction-to-agent-builder`, `agentexchange-quick-look`

## 2. Prompt engineering and Prompt Builder
- C: `prompt-fundamentals`, `prompt-builder-basics`
- I: `quick-start-prompt-builder`, `quick-start-create-prompt-builder-flex-template`, `quick-start-create-a-sales-email-prompt-template`, `superbadge_prompt_builder_templates_sbu`
- L: `prompt-engineering-techniques`, `custom-service-agents-with-prompt-builder-and-agentforce`

## 3. Trust, security and AI governance
- C: `the-einstein-trust-layer`, `data-fundamentals-for-ai`, `secure-and-trusted-headless-foundation`
- I: `ai-strategy`, `trusted-agentic-ai`, `threat-modeling-for-ai-agents`
- L: `deploy-agent-authentication`

## 4. Planning, building and customising agents (subagents, instructions, actions)
- C: `quick-start-assemble-a-service-agent-with-agentforce-builder`, `programmatic-instructions-in-agentforce`, `use-employee-agents-to-get-work-done`
- I: `agentforce-agent-planning`, `agent-behavior-basics`, `quick-start-einstein-copilot` (Agent Actions), `customize-a-service-agent-with-prompts-flows-and-actions`, `agentforce-grid`
- L: `agent-customization-quick-look`, `agent-customization-with-flows`, `agent-customization-with-apex`, `superbadge-advanced-agentforce-flow-administration`, `superbadge-flow-for-agentforce`, `superbadge-apex-for-agentforce`

## 5. Data 360, grounding and RAG
- C: `ai-data-crm-quick-look`
- I: `ai-data-project-planning`, `data-foundation-for-headless-functionality`
- L: `grounding-an-agent-with-data`, `retrieval-augmented-generation-quick-look`, `agentforce-data-library-basics`, `data-cloud-powered-experiences`, `data-cloud-powered-agentforce`, `search-index-types-data-cloud-quick-look`, `unstructured-data-in-data-cloud`, `data-360-sandboxes`, `connect-data-cloud-to-copilot-and-prompt-builder`

## 6. Testing, deployment, monitoring and developer tools
- I: `agent-behavior-evaluation`, `agentforce-deployment-quick-look`, `agentforce-help-agent`, `agentforce-voice-quick-look`
- L: `agentforce-testing-tools-and-strategies`, `agentforce-agent-testing`, `agentforce-analytics-and-monitoring`, `agent-analytics-and-monitoring`, `agent-behavior-troubleshooting-in-agentforce`
- L (Slack): `quick-start-create-employee-agents-in-agentforce`, `connect-your-agentforce-org-with-slack`, `agentforce-configuration-for-slack-deployment`
- L (developer): `create-an-agent-using-pro-code-tools` (Agentforce DX), `agent-api-quick-look`, `get-started-with-einstein-models-api`
- I/C (headless): `salesforce-headless-360-quick-look`, `headless-tools-and-functionality`, `headless-360-use-a-conversation-to-build-an-agent`, `headless-360-use-cases-in-action`

## 7. Agentforce in Sales, Service and Industries
- C: `agentforce-service-agent-quick-look`, `agentforce-sales-agents-quick-look`, `agentforce-for-setup-quick-look`, `agentforce-on-the-salesforce-mobile-app-quick-look`, `salesforce-in-claude-quick-look`
- I: `agentforce-sdr-setup-and-customization`, `agentforce-for-sales-coaching-setup-and-customization`, `build-your-first-sales-coach`, `quick-start-build-an-agent-to-create-quotes-fast`, `agentic-sales-cycle-powered-by-headless-360`, `agentforce-service-planner-quick-look`, `agentforce-service-assistant`, `superbadge-agentforce-service-agents`, `quick-start-agentforce-coworker`
- I (industries): `agentforce-for-industries-quick-look`, `agentforce-for-financial-services-cloud`, `agentic-advisor-for-agentforce-financial-services`, `meeting-concierge`

## Weighting when the official outline can't be found
Use the exam guide's domains and weights when you can get them, and map these topics onto them. If you can't, use the seven topics above as the domains. Weight them by practice emphasis, not module count, because the exam centres on building agents:
- Topics 2, 4 and 5 (prompts, building agents, grounding): about 60% together
- Topics 3 and 6: about 30%
- Topics 1 and 7: about 10%

Say in the exam `subtitle` and in the reply that these weights are practice defaults, not official.
