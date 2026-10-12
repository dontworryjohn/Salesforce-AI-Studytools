# Finding Salesforce exam material

## Exam guide
- Search (standard mode): `<certification name> exam guide` and `Salesforce Certified <name> exam outline`. If that misses or looks outdated, repeat in extended mode.
- Official sources, in order of preference: the Trailhead exam guide (trailhead.salesforce.com/help?article=...), the certification page on trailhead.salesforce.com/credentials, then Trailhead Academy. Prefer these over third-party study sites for the format, weightings and pass mark.
- If two sources disagree, use the one tied to the most recent release and tell the user.

## Preparation trail / trailmix
- Trailhead MCP is strongly recommended for this step. If the connector is available, use `content_search` with the certification name (e.g. "Prepare for your Platform App Builder") to get the trail or trailmix and its module/unit list.
- `fetch_content` on a TRAIL returns a manifest of its children (module `apiName`, title, URL). Skip children whose `contentType` is `link` (surveys, Slack invites, news articles). Then `fetch_content` on a MODULE returns the full unit markdown; raise `maxUnits` if `truncated` is set. This is the best source for question facts, so prefer it to web search for unit text. Don't use `expand: true` on a large trail; fetch only the modules the scope needs.
- TRAILMIX results can't be fetched, and most trailmixes in search results are community-made. Prefer the official TRAIL (shown as type `LEARNINGPATH` in search, with `creatorName` null).
- Agentblazer: search `agentblazer` and choose the current-year trail, e.g. `become-an-agentblazer-champion-2026`, `-innovator-2026` or `-legend-2026`. Slugs without a year are older versions. The landing page is trailhead.salesforce.com/agentblazer, and the status FAQ is https://trailhead.salesforce.com/help?article=Agentblazer-Status-FAQ.
- Agentforce Specialist exam:
  - Credential page: https://trailhead.salesforce.com/en/credentials/agentforcespecialist. Its "Study & Prepare" section points only to trailhead.salesforce.com/agentblazer, so use all three Agentblazer status trails (Champion, Innovator, Legend) as the prep trail. `references/agentblazer-map.md` maps their modules to exam topics. Searching for its prep material returns only community trailmixes; ignore them.
  - Exam details (question count, time, pass mark, outline) are on the Trailhead Academy exam page linked from the credential page: https://trailheadacademy.salesforce.com/certificate/exam-agentforce-specialist---AI-201. The credential page draws its content in with JavaScript, so fetching it returns only navigation. If the Academy page fetches no better, search "Agentforce Specialist exam guide" and use the Trailhead help article it returns.

## Credential pages
- Every certification has a page at `https://trailhead.salesforce.com/en/credentials/<name>` (e.g. `agentforcespecialist`, `platformappbuilder`, `platformadministrator`). Its "Study & Prepare" section names the official prep trail, and its exam link goes to Trailhead Academy. When the prep trail isn't obvious, check this page first. A WebFetch summary is often empty here, so download the HTML with curl and pull out the links in the "Study & Prepare" section.
- If the connector is not available, tell the user once that the Trailhead MCP connector is missing and that questions will be less closely matched to the official prep trail. Give the server URL `https://mcp.trailhead.salesforce.com/mcp` and the setup hint (Claude.ai: Customize → Connectors → Add custom connector, no sign-in; Claude Code: `claude mcp add trailhead --transport http https://mcp.trailhead.salesforce.com/mcp --scope user`). Ask whether to continue without it; if yes, use the web search routes below.
- Trailhead pages usually can't be fetched directly (robots-blocked). Don't spend calls on web_fetch for trailhead.salesforce.com/content/learn/...

## Unit and article text
- With the Trailhead MCP, use `fetch_content` on the module (above). Without it, unit text via web_search works best: `trailhead <module-slug> <unit-slug>` in standard mode. Fallback: the unit title in quotes, then extended mode.
- Salesforce Help: search the article title or the feature name plus "Salesforce Help". Keep the URL exactly as returned in results for review links.
- Developer exams: also search developer.salesforce.com docs (Apex Developer Guide, LWC, limits) by topic.
- Search snippets drop tables. When a fact depends on a table (editions, limits, permissions), confirm it with the matching Help article before using it.

## Link formats for review references
- Trailhead module: https://trailhead.salesforce.com/content/learn/modules/<module-slug>
- Trailhead unit: https://trailhead.salesforce.com/content/learn/modules/<module-slug>/<unit-slug>
- Salesforce Help / developer docs: the URL exactly as it appeared in search results. Never build one from memory.
