from pathlib import Path

from pydantic import BaseModel

from setup import init_notebooks


class Config(BaseModel):
    project_root: Path = Path(__file__).resolve().parent


# Singleton-style access
CONFIG = Config()
# init setup
init_notebooks()
