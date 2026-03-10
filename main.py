from __future__ import annotations

import os

import argparse
import argparse
from dotenv import load_dotenv
from pydantic import BaseModel, Field

from langchain.agents import create_agent

from langchain.tools import tool
from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch

load_dotenv(override=True)


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")
MODEL_NAME = os.getenv("MODEL_NAME")


COURSE_DB = {
    "agentic ai": {
        "course_name": "Agentic AI",
        "duration": "12 weeks",
        "level": "Intermediate to Advanced",
        "tools": [
            "LangChain",
            "LangGraph",
            "CrewAI",
            "AutoGen",
            "FastAPI",
            "Vector Databases",
        ],
        "modules": [
            "Agent fundamentals",
            "Tool calling",
            "Planning and routing",
            "Memory and state",
            "Multi-agent workflows",
            "Evaluation and guardrails",
            "Deployment patterns",
        ],
        "outcome": "Build production-style agents with tools, memory, routing, and control flows.",
    },
    "mlops": {
        "course_name": "MLOps",
        "duration": "14 weeks",
        "level": "Intermediate",
        "tools": [
            "MLflow",
            "DVC",
            "Docker",
            "Kubernetes",
            "Airflow",
            "Evidently",
        ],
        "modules": [
            "Experiment tracking",
            "Data and model versioning",
            "CI/CD for ML",
            "Model serving",
            "Monitoring",
            "Production pipelines",
        ],
        "outcome": "Build reliable ML pipelines and deploy models in production.",
    },
    "llmops": {
        "course_name": "LLMOps",
        "duration": "12 weeks",
        "level": "Intermediate to Advanced",
        "tools": [
            "vLLM",
            "LangServe",
            "LangSmith",
            "LangFuse",
            "Docker",
            "Kubernetes",
        ],
        "modules": [
            "PromptOps",
            "Serving and inference",
            "Observability",
            "Evaluation pipelines",
            "Security and guardrails",
            "Scaling LLM systems",
        ],
        "outcome": "Operate and monitor production LLM systems end to end.",
    },
}




class CcourseLookupInput(BaseModel):
    course_name:str=Field(description="The name of the course to look up, for example 'Agentic AI', 'MLOps', or 'LLMOps'. ")
    include_modules:bool=Field(default=True,description="Whether to include the course modules in the output.")


@tool(args_schema=CcourseLookupInput)
def get_internal_course_info(course_name: str, include_modules: bool = True) -> str:
    """
    Look up information about a course from the internal COURSE_DB.
    """
    key=course_name.strip().lower()
    aliases = {
        "agentic ai": "agentic ai", 
        "agentic ai course": "agentic ai",
        "ml ops": "mlops",

        "mlops": "mlops",
        "llm ops": "llmops",            
        "llmops": "llmops",
    }

    key = aliases.get(key, key)
    data=COURSE_DB.get(key)
    if not data:
        return f"Sorry, I couldn't find any information about the course '{course_name}'."      
    response = f"Course Name: {data['course_name']}\nDuration: {data['duration']}\nLevel: {data['level']}\nTools: {', '.join(data['tools'])}\nOutcome: {data['outcome']}"

    lines=[
        f"Course Name: {data['course_name']}",
        f"Duration: {data['duration']}",
        f"Level: {data['level']}",
        f"Tools: {', '.join(data['tools'])}",
        f"Outcome: {data['outcome']}",
    ]

    if include_modules:
        lines.append(f"Modules: {', '.join(data['modules'])}")

    return "\n".join(lines)

web_search = TavilySearch(max_results=5, topic="general",search_depth="advanced",include_raw_content=False)





model=ChatGroq(model=MODEL_NAME,temperature=0,max_retries=2)


sytem_prompt = """
You are a practical AI assistant.

Tool rules:
1. Use get_internal_course_info for internal course details.
2. Use TavilySearch for latest public information, trends, releases, and web facts.
3. You may use both tools if needed.
4. Do not invent internal data.
5. Keep answers concise but concrete.
"""
agent = create_agent(model=model, 
                     tools=[get_internal_course_info, web_search], 
                     system_prompt=sytem_prompt)

def extract_final_text(result: dict) -> str:
    messages = result.get("messages", [])
    if not messages:
        return "No messages returned."

    last_message = messages[-1]

    # Common case: AIMessage with string content
    if hasattr(last_message, "content"):
        content = last_message.content

        if isinstance(content, str) and content.strip():
            return content.strip()

        if isinstance(content, list):
            parts = []
            for item in content:
                if isinstance(item, dict):
                    text = item.get("text")
                    if isinstance(text, str) and text.strip():
                        parts.append(text.strip())
                elif isinstance(item, str) and item.strip():
                    parts.append(item.strip())

            if parts:
                return "\n".join(parts)

    return str(last_message)
def run_once(query: str) -> None:
    result = agent.invoke(
        {
            "messages": [
                {"role": "user", "content": query}
            ]
        }
    )

    # print("\nFull agent result:", result)

    final_text = extract_final_text(result)

    print("\n=== FINAL ANSWER ===\n")
    print(final_text if final_text else "Sorry, I couldn't generate a response.")
def intractive_chat():
    print("Welcome to the AI assistant. Type 'exit' to quit.")
    while True:
        query = input("You: ")
        if query.lower() == "exit":
            print("Goodbye!")
            break
        print("AI Assistant:",query)
        run_once(query)
        print()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Run the AI assistant in interactive mode or with a single query.")
    parser.add_argument("--query", type=str, help="A single query to run the assistant with.")
    args = parser.parse_args()

    if args.query:
        run_once(args.query)
    else:
        intractive_chat()