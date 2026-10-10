# Finding Salesforce exam material

## Exam guide
- Search (standard mode): `<certification name> exam guide` and `Salesforce Certified <name> exam outline`. If that misses or looks outdated, repeat in extended mode.
- Official sources, in order of preference: the Trailhead exam guide (trailhead.salesforce.com/help?article=...), the certification page on trailhead.salesforce.com/credentials, then Trailhead Academy. Prefer these over third-party study sites for the format, weightings and pass mark.
- If two sources disagree, use the one tied to the most recent release and tell the user.

## Preparation trail / trailmix
- If the Trailhead MCP connector is available, use `content_search` with the certification name (e.g. "Prepare for your Platform App Builder") to get the trail or trailmix and its module/unit list, then `fetch_content` for structure. Module body text may not come through; use the connector for the list of modules and units, then move on.
- Trailhead pages usually can't be fetched directly (robots-blocked). Don't spend calls on web_fetch for trailhead.salesforce.com/content/learn/...

## Unit and article text
- Unit text via web_search works best: `trailhead <module-slug> <unit-slug>` in standard mode. Fallback: the unit title in quotes, then extended mode.
- Salesforce Help: search the article title or the feature name plus "Salesforce Help". Keep the URL exactly as returned in results for review links.
- Developer exams: also search developer.salesforce.com docs (Apex Developer Guide, LWC, limits) by topic.
- Search snippets drop tables. When a fact depends on a table (editions, limits, permissions), confirm it with the matching Help article before using it.

## Link formats for review references
- Trailhead module: https://trailhead.salesforce.com/content/learn/modules/<module-slug>
- Trailhead unit: https://trailhead.salesforce.com/content/learn/modules/<module-slug>/<unit-slug>
- Salesforce Help / developer docs: the URL exactly as it appeared in search results. Never build one from memory.
