"""
minimal_agent.py — simplest working AgentBeats agent
Tested with the PyPI release of agentbeats (>=0.1.x)

Usage:
    uv run python minimal_agent.py
Required:
    - OPENAI_API_KEY in the .env file or environment variable
"""

from agents import Agent, Runner

if __name__ == "__main__":
    # Optional: check for API key before running
    from dotenv import load_dotenv
    load_dotenv()


    # Instantiate the agent with the TOML card (optional but recommended)
    # This will read configuration like ports, model type, etc.
    agent = Agent(name="test", handoff_description="A minimal agent that responds to messages.")

    # Start the agent event loop / server
    print("🚀 Starting MyAgent...")
    print({agent.handoff_description})
    
    # replace the text below for chat
    result = Runner.run_sync(agent, "Hello, what's your tool?")
    # print(dir(result))
    print(result.final_output)

