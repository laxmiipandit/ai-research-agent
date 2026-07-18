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

I tested the agent on 15 questions — a mix of straightforward facts, harder multi-source comparisons, and a few genuinely tricky ones (disputed facts, unanswerable questions, and recent events).

**Result: 13/15 correct (87%)**

A few things stood out:

- On questions where sources actually disagree (like whether the Nile or Amazon is longer), the agent didn't just pick one — it explained the disagreement instead of papering over it.
- When asked something it genuinely couldn't know — like who'll win the next election — it said so, instead of guessing. Same with a question about very recent AI releases, where it was upfront that its sources didn't fully cover the timeframe asked.
- The one real weakness I found: a question about recent space mission updates returned slightly outdated info, since the search wasn't strongly weighted toward recency. Good thing to know and fix later.

Overall, the agent was more likely to admit uncertainty than to confidently make something up — which was honestly the main thing I was testing for.
## Running locally

\`\`\`bash
pip install -r requirements.txt
# Add your GROQ_API_KEY and TAVILY_API_KEY to a .env file
streamlit run app.py
\`\`\`

## Author

Built by Laxmi Pandit.