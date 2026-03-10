# Agentic AI Learning Hub

A practical AI learning platform for querying course information and exploring agentic AI capabilities using LangChain, Groq, and Tavily.

## Code Overview

### Core Components

#### 1. Course Database
The application maintains an internal `COURSE_DB` with three featured courses:

```python
COURSE_DB = {
    "agentic ai": {
        "course_name": "Agentic AI",
        "duration": "12 weeks",
        "level": "Intermediate to Advanced",
        "tools": ["LangChain", "LangGraph", "CrewAI", ...],
        "modules": ["Agent fundamentals", "Tool calling", ...],
        "outcome": "Build production-style agents..."
    },
    "mlops": { ... },
    "llmops": { ... }
}
```

#### 2. Course Lookup Tool
A Pydantic-based tool for querying course information:

```python
@tool(args_schema=CcourseLookupInput)
def get_internal_course_info(course_name: str, include_modules: bool = True) -> str:
    """Look up information about a course from the internal COURSE_DB."""
    # Handle aliases and lookups
    key = aliases.get(key, key)
    data = COURSE_DB.get(key)
    # Return formatted course details
```

**Usage:**
```python
get_internal_course_info("Agentic AI", include_modules=True)
```

**Output:**
```
Course Name: Agentic AI
Duration: 12 weeks
Level: Intermediate to Advanced
Tools: LangChain, LangGraph, CrewAI, AutoGen, FastAPI, Vector Databases
Modules: Agent fundamentals, Tool calling, Planning and routing, ...
Outcome: Build production-style agents with tools, memory, routing, and control flows.
```

#### 3. AI Agent Configuration
The application uses Groq's LLM with integrated tools:

```python
# Initialize LLM
model = ChatGroq(model=MODEL_NAME, temperature=0, max_retries=2)

# Initialize web search
web_search = TavilySearch(max_results=5, topic="general", search_depth="advanced")

# Tools available: get_internal_course_info, web_search
```

## Setup

### Prerequisites
- Python 3.8+
- API Keys:
  - `GROQ_API_KEY` - Get from https://console.groq.com
  - `TAVILY_API_KEY` - Get from https://tavily.com

### Installation

```bash
# Clone and setup
git clone https://github.com/scai-learning-hub/agentic_ai_learning.git
cd agentic_ai_learning

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Configure environment
cp .env.example .env
# Edit .env with your API keys
```

### Environment Variables (`.env`)
```
GROQ_API_KEY=your_groq_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
MODEL_NAME=mixtral-8x7b-32768
```

## Running the Application

```bash
python main.py
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

Built with ❤️ by scaLearningHub
