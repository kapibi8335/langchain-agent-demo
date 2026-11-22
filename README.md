# LangChain Agent Demo

Toy agent wiring a chat model and a local tool through LangChain.

## Setup

```sh
python3 -m venv .venv && . .venv/bin/activate
pip install -r requirements.txt
set -a; . ./.env; set +a
python3 agent.py
```

Configuration is read from the environment; see `.env.example`.
