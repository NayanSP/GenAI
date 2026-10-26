
import os
import requests

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, ToolMessage

load_dotenv()

if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("Please set OPENAI_API_KEY in your .env file")


# TOOL 1: Addition
@tool
def add_numbers(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b


# TOOL 2: Multiplication
@tool
def multiply_numbers(a: float, b: float) -> float:
    """Multiply two numbers."""
    return a * b


# TOOL 3: Wikipedia search
@tool
def wikipedia_search(query: str) -> str:
    """Search Wikipedia for information about a topic."""
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 3,
    }

    headers = {
        "User-Agent": "AIResearchAssistant/1.0 (educational project)"
    }

    try:
        response = requests.get(
            url,
            params=params,
            headers=headers,
            timeout=15,
        )
        response.raise_for_status()
        data = response.json()

        results = data["query"]["search"]

        if not results:
            return "No Wikipedia results found."

        return "\n\n".join(
            f"Title: {item['title']}\n"
            f"Snippet: {item['snippet']}"
            for item in results
        )

    except (requests.RequestException, ValueError, KeyError) as e:
        return f"Wikipedia search error: {e}"


# Register all tools
tools = [
    add_numbers,
    multiply_numbers,
    wikipedia_search,
]

tool_map = {t.name: t for t in tools}


# Initialize the OpenAI model
llm = ChatOpenAI(
    model="gpt-4o-mini",
    temperature=0,
)

llm_with_tools = llm.bind_tools(tools)


# Agent execution loop
def ask_assistant(question: str) -> str:
    messages = [HumanMessage(content=question)]

    for _ in range(5):
        response = llm_with_tools.invoke(messages)
        messages.append(response)

        # No tool call means the model has a final answer
        if not response.tool_calls:
            return response.content

        # Execute the tools requested by the model
        for call in response.tool_calls:
            name = call["name"]
            args = call["args"]

            print(f"\nCalling tool: {name}")
            print(f"Arguments: {args}")

            if name not in tool_map:
                result = "Unknown tool."
            else:
                try:
                    result = tool_map[name].invoke(args)
                except Exception as e:
                    result = f"Tool execution failed: {e}"

            print(f"Tool result: {result}")

            messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=call["id"],
                )
            )

    return "Stopped after reaching the tool-call limit."


# Interactive application
if __name__ == "__main__":
    print("AI Research Assistant")
    print("Type 'exit' to quit.")

    while True:
        question = input("\nYou: ").strip()

        if question.lower() in {"exit", "quit"}:
            print("Goodbye!")
            break

        if not question:
            continue

        try:
            answer = ask_assistant(question)
            print(f"\nAssistant: {answer}")

        except Exception as e:
            print(f"Error: {e}")
