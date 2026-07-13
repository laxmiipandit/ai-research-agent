#  AI Research Agent

A generative AI research agent that searches the web, reasons across multiple sources, and answers questions with citations — with a self-checking loop that decides when to search again for a more complete answer.

**🔗 Live app:** [Try it here](https://laxmiipandit-ai-research-agent-app-vw6hsb.streamlit.app)

## What it does

Given any question, the agent:
1. Searches the live web for relevant sources
2. Reasons across multiple sources to generate an answer with citations
3. Self-checks its own answer for completeness/confidence
4. If uncertain, refines its search query and searches again (up to 2 rounds)
5. Returns a final, source-backed answer

## Why this is different from a basic chatbot

- **Not just LLM knowledge** — answers are grounded in live web search, not just training data
- **Self-correcting** — the agent evaluates its own answer quality before responding
- **Transparent** — every claim is cited back to its source

## Tech stack

- **LLM:** Groq API (Llama 3.3 70B)
- **Web search:** Tavily API
- **Frontend:** Streamlit
- **Language:** Python
- **Deployment:** Streamlit Community Cloud

## Evaluation

Tested on a set of 15 questions spanning factual lookup, multi-source reasoning, and ambiguous/disputed topics (e.g. "Is Pluto a planet?").
*(Results to be added once full evaluation run completes)*

## Running locally

\`\`\`bash
pip install -r requirements.txt
# Add your GROQ_API_KEY and TAVILY_API_KEY to a .env file
streamlit run app.py
\`\`\`

## Author

Built by Laxmi Pandit as part of a self-directed AI/GenAI engineering learning path.