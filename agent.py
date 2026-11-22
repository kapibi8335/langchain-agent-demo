import os

from langchain_core.tools import tool
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(
    base_url=os.environ["OPENAI_BASE_URL"],
    api_key=os.environ["OPENAI_API_KEY"],
    model=os.environ.get("OPENAI_MODEL", "gpt-4o"),
)


@tool
def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in text."""
    return len(text.split())


if __name__ == "__main__":
    reply = llm.invoke("Summarise what a vector store is in one sentence.")
    print(reply.content)
