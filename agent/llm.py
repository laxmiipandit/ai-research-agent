from groq import Groq
from dotenv import load_dotenv
import os
from agent.search import search_web

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def ask_llm(prompt, model="llama-3.3-70b-versatile"):
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


def research_answer(question, max_rounds=1):
    all_sources = []
    query = question

    for round_num in range(1, max_rounds + 1):
        results = search_web(query, max_results=5)
        all_sources.extend(results)

        context = ""
        for i, r in enumerate(all_sources, 1):
            context += f"[Source {i}] {r['title']}\n{r['url']}\n{r['content']}\n\n"

        answer_prompt = f"""Answer the following question using ONLY the sources below.
Cite sources using [Source X] notation.

Question: {question}

Sources:
{context}

Answer:"""

        answer = ask_llm(answer_prompt)

        check_prompt = f"""Question: {question}
Answer: {answer}

Is this answer complete and confident? Reply with ONLY:
- "SUFFICIENT" if yes
- Or a refined search query if more searching would help

Reply:"""

        check = ask_llm(check_prompt).strip()
        print(f"--- Round {round_num} self-check: {check} ---")

        if check.upper().startswith("SUFFICIENT") or round_num == max_rounds:
            return answer
        else:
            query = check

    return answer