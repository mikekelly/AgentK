# Agent K

[![Join the Discord](https://img.shields.io/badge/Discord-Join%20our%20server-5865F2?style=for-the-badge&logo=discord&logoColor=white)](https://discord.gg/TyW9gdA5) [![Follow on X.com](https://img.shields.io/badge/X.com-Follow-1DA1F2?style=for-the-badge&logo=x&logoColor=white)](https://x.com/NicerInPerson)

The autoagentic AGI.

AgentK is an AGI made of agents that collaborate, create new agents, and complete tasks.

It's a modular, self-evolving AGI system that gradually builds its own mind as you challenge it to complete tasks.

The "K" stands kernel, meaning small core. The aim is for AgentK to be the minimum set of agents and tools necessary for it to bootstrap itself and then grow its own mind.

AgentK's mind is made up of:

1. Agents who collaborate to solve problems, and;
2. Tools which those agents are able to use to interact with the outside world.

It develops both of these as regular python files (in the `agents` and `tools` directories) so it's very easy to track its progress, and even contribute yourself if you want.

AgentK is encouraged to write tests for itself. More can be done to aid with the detection and fixing of missbehaving agents and tools - this is work in progress.

AgentK is built on top of the excellent LangGraph and LangChain frameworks.

## How to run

AgentK runs isolated in a docker container, so you need the latest docker installed on your system.

1. Copy `.env.template` to `.env`
2. Set environment variables in `.env`
3. Run `./agentk`