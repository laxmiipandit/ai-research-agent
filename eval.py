from agent.llm import research_answer
import time

test_questions = [
    # Easy factual (kept from before, as a baseline)
    "Who is the current Prime Minister of India?",
    "What is the capital of Japan?",
    "What year did India gain independence?",
    "Who won the ICC Cricket World Cup 2023?",
    "What is the current version of Python as of 2026?",

    # Harder: multi-source reasoning
    "Compare the population of India and China as of the most recent estimates.",
    "What are the key differences between GPT-4 and Claude's approach to AI safety?",
    "What was the GDP growth rate of India in the most recent fiscal year, and how does it compare to the previous year?",

    # Harder: disagreement / nuance (like the mountain question)
    "Is Pluto a planet?",
    "What is the world's longest river — the Nile or the Amazon?",

    # Harder: recency (tests if search is actually being used, not old training data)
    "What major AI model releases happened in the last 3 months?",
    "What is the latest update on India's Chandrayaan space missions?",

    # Trick / should trigger honest uncertainty
    "Who will win the next Indian general election?",
    "What is the exact stock price of Tesla right now?",
    "What will the weather be like in Delhi next week?",
]
for i, question in enumerate(test_questions, 1):
    print(f"\n{'='*50}")
    print(f"Q{i}: {question}")
    print('='*50)
    answer = research_answer(question)
    print(f"ANSWER: {answer}")
    time.sleep(2)