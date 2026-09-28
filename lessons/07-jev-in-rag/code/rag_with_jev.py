"""Jev in a RAG pipeline: route the question, filter passages, check the answer.

python rag_with_jev.py
"""

from typesafe_sdk import Choice, Noul, Score, TypeSafeClient

client = TypeSafeClient()

question = "How many days do I have to return a phone bought on sale?"

# ── Step 1: route. Where should we look? ─────────────────────────────
route = client.system_one(
    state={"question": question},
    questions={
        "source": Choice(
            instructions="Where should we look to answer `question`",
            criteria={
                "company_docs": "Our own policies, products, pricing or account rules",
                "web_search": "Recent news or facts about the outside world",
                "no_lookup": "Small talk or general knowledge that needs no lookup",
            },
        )
    },
).answers["source"]
print(f"1. Route → {route.choice} (confidence {route.confidence:.2f})")

# ── Step 2: filter. Which retrieved passages actually help? ──────────
passages = [
    "Returns: most items can be returned within 30 days of delivery.",
    "Sale items: phones and laptops bought on sale can be returned within 10 days.",
    "Shipping: orders above ₹499 ship free across India.",
    "Warranty: phones come with a 1-year manufacturer warranty.",
]
relevance = client.system_one(
    state={"question": question, "passages": passages},
    questions={
        f"p{i}": Score(
            instructions=f"How useful is `passages[{i}]` for answering `question`",
            criteria=["Not related", "Somewhat related", "Answers it directly"],
        )
        for i in range(len(passages))
    },
)
keep = [p for i, p in enumerate(passages) if relevance.answers[f"p{i}"].score >= 1.0]
print("2. Keep these passages:")
for p in keep:
    print("   -", p)

# ── Step 3: check. Does the source support the LLM's answer? ─────────
llm_answer = "You can return a phone bought on sale within 10 days."
check = client.system_one(
    state={"answer": llm_answer, "sources": keep},
    questions={"supported": Noul(instructions="Every claim in `answer` is supported by `sources`")},
).answers["supported"]
print(f"3. Answer supported by sources? {check.noul:.2f}")
