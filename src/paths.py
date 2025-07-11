import os

ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAG_ASSISTANT_DIR = os.path.join(ROOT_DIR, "src")

ENV_FPATH = os.path.join(ROOT_DIR, ".env")

PROMPT_CONFIG_FPATH = os.path.join(RAG_ASSISTANT_DIR, "config", "prompt.yaml")
MODELS_CONFIG_FPATH = os.path.join(RAG_ASSISTANT_DIR, "config", "models.yaml")
