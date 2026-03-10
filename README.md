# Agentic AI Learning

Welcome to the **Agentic AI Learning Hub** - a comprehensive educational platform for learning and mastering agentic AI systems.

## Overview

This repository contains learning materials, code examples, and projects for understanding:
- **Agentic AI Fundamentals**
- **Agent Development Frameworks** (LangChain, LangGraph, CrewAI, AutoGen)
- **MLOps & Production Deployment**
- **Advanced Agent Patterns**

## Course Offerings

### Agentic AI
- **Duration**: 12 weeks
- **Level**: Intermediate to Advanced
- **Focus**: Building production-style agents with tools, memory, routing, and control flows
- **Tools**: LangChain, LangGraph, CrewAI, AutoGen, FastAPI, Vector Databases

### MLOps
- **Duration**: 14 weeks
- **Level**: Advanced
- **Focus**: Production ML systems, deployment, monitoring, and scaling

## Getting Started

### Prerequisites
- Python 3.8+
- pip or conda
- API keys (GROQ, Tavily)

### Installation

```bash
# Clone this repository
git clone https://github.com/scaLearningHub/agentic_ai_learning.git
cd agentic_ai_learning

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Setup environment variables
cp .env.example .env
# Edit .env with your API keys
```

## Project Structure

```
agentic_ai_learning/
├── main.py              # Main learning hub entry point
├── requirements.txt     # Project dependencies
├── .env.example         # Example environment variables
├── README.md           # This file
└── [additional modules]
```

## Environment Variables

Create a `.env` file with the following:

```
GROQ_API_KEY=your_groq_key
TAVILY_API_KEY=your_tavily_key
MODEL_NAME=mixtral-8x7b-32768
```

## Contributing

We welcome contributions! Please:
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions and support, reach out to the scaLearningHub team.

---

**Happy Learning!** 🚀
