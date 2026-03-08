**CRITICAL**: At the start of EVERY conversation, IMMEDIATELY invoke these skills using the Skill tool to load development guidelines:
- `data-app-html-python:data-app` — web app architecture, routing, and data source patterns
- `workshop-ai:workshop-ai` — AI capabilities (image generation, AI-powered features, managed connectors)

## Data Source & AI Implementation - CRITICAL

**When your task involves ANY connector, data source, or AI service, invoke the relevant skill before writing any related code.**

1. Check available connectors in system prompt under "Available Connectors"
2. Invoke using: `Skill` tool with `connectors-python:connector-{type}` format

**Examples:**
- Neon database → invoke `connectors-python:connector-neon`
- PostgreSQL → invoke `connectors-python:connector-postgresql`
- Gemini (AI) → invoke `connectors-python:connector-workshop-gemini`
- OpenAI → invoke `connectors-python:connector-workshop-openai`
- Anthropic → invoke `connectors-python:connector-workshop-anthropic`

**For AI tasks** (image generation, chat, content generation), also invoke `workshop-ai:workshop-ai` for patterns on parallel image generation, AI-powered app endpoints, and which models to use.

**DO NOT:**
- Manually implement database connections or AI integrations
- Write connector code before invoking the skill
- Guess at connection patterns
- **Deviate from the skill's code examples** (model names, SDK methods, parameters, patterns) — use them exactly as shown unless the user explicitly requests otherwise

**WHY:** Connector skills provide:
- Correct dependency installation commands
- Proper secret/environment variable names
- Tested connection patterns with **specific, verified values** (model names, API parameters)
- Security best practices

**Skills are authoritative, not suggestions.** The code examples, model names, and parameters in skills have been tested against the actual connectors. Copy them exactly. Do not substitute "better" alternatives — e.g., do not replace a skill's specified model with a different one you think is superior.


## Frontend Implementation - CRITICAL

**When your task involves frontend code (HTML, CSS, UI, static assets), invoke the `frontend-design:frontend-design` skill before writing any related code** and follow its guidelines for design and UX.
