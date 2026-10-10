# SF-AI-Tools

AI skills for Salesforce work, packaged for Claude.

## Skills

| Skill | What it does |
|---|---|
| [`salesforce-cert-mock-exam`](skills/salesforce-cert-mock-exam/SKILL.md) | Builds hard, scenario-based mock exams, quizzes, flashcards and timed exams for any Salesforce certification (Administrator, Platform App Builder, Platform Developer, Agentforce Specialist, Data Cloud, architect exams and more). Grounded in the official exam guide, Trailhead prep trails and Salesforce Help, with explanations for every option and review links. |

## Structure

```
skills/
└── salesforce-cert-mock-exam/
    ├── SKILL.md                 # Skill instructions
    ├── references/retrieval.md  # How to find exam guides, trails and Help articles
    ├── scripts/build_timed_exam.py  # Fills and validates the timed-exam template
    └── assets/timed-exam.html   # Timed exam / practice mode HTML template
```

## Using the skill

**Claude.ai:** zip the `skills/salesforce-cert-mock-exam` folder and upload it under Settings → Capabilities → Skills.

**Claude Code:** copy the folder into `~/.claude/skills/` (personal) or `.claude/skills/` in a project.

Then just ask, e.g. *"Quiz me on Platform App Builder"* or *"Give me a timed Administrator mock exam."*

## Recommended: Trailhead MCP connector

Set up Trailhead MCP in the same AI client where you use this skill. The skill uses the connector to find the official certification preparation trail and retrieve its structure. Without it, the skill tells you the connector is missing, shows how to add it, and offers to continue with web search instead, so questions may be less closely matched to the official prep trail. The server provides public Trailhead learning content, requires no authentication, and does not access private learner data. This connector setup is separate from installing the skill.

Server URL: `https://mcp.trailhead.salesforce.com/mcp`

### Claude.ai (browser)

1. Sign in to [Claude.ai](https://claude.ai) and open **Customize → Connectors**.
2. Select **Add → Add custom connector**.
3. Name it **Trailhead** and enter `https://mcp.trailhead.salesforce.com/mcp` as the server URL.
4. Continue through the setup, choose **No sign in** for authentication, then add the connector.
5. In a chat, select **+ → Connectors** and enable Trailhead for that conversation.

Custom connectors are available on Claude Free, Pro, Max, Team, and Enterprise plans; Free accounts are limited to one custom connector. For Team or Enterprise, an organization owner may need to add the connector first. See Anthropic's [remote MCP connector instructions](https://support.claude.com/en/articles/11175166-get-started-with-custom-connectors-using-remote-mcp).

### Claude Code

Run this in a terminal. The `user` scope makes the connector available in all your Claude Code projects:

```sh
claude mcp add trailhead --transport http https://mcp.trailhead.salesforce.com/mcp --scope user
```

### Claude Desktop

Open **Settings → Developer → Edit Config** and add the server under `mcpServers` in `claude_desktop_config.json`:

```json
{
    "mcpServers": {
        "trailhead": {
            "type": "http",
            "url": "https://mcp.trailhead.salesforce.com/mcp"
        }
    }
}
```

Save the file and restart Claude Desktop.

### VS Code

Create or edit `.vscode/mcp.json` in your workspace and add:

```json
{
    "servers": {
        "trailhead": {
            "type": "http",
            "url": "https://mcp.trailhead.salesforce.com/mcp"
        }
    }
}
```

Save the file and reload VS Code if the server does not appear in the MCP tools list.

### Verify the connection

Ask your assistant: *"Use Trailhead MCP to find beginner content on Salesforce Flow."* A working connector should return Trailhead content. For more clients, troubleshooting, and usage tips, see the [Trailhead MCP setup guide](https://trailhead.salesforce.com/support/mcp).

## Disclaimer

Not affiliated with or endorsed by Salesforce. Practice questions are generated from public Salesforce material and are not real exam questions.
