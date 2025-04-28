from typing import Literal, Any
from pathlib import Path
import json
import os

pymaker_config: dict[
      Literal["ollama_host_ip"] 
    | Literal["ollama_host_port"] 
    | Literal["ollama_model"]
    | Literal["prompt_prefix_file"]
    , Any
]

config_path: Path
if 'DOCKER_COMPOSE' in os.environ:
    config_path = Path("/config/")
elif 'K8S' in os.environ:
    config_path = Path("/config/")
else:
    config_path = Path("../config/")

pymaker_config = json.loads((config_path / "pymaker_config.json").read_text())

def get_prompt_prefix() -> str:
    prefix_path = config_path / pymaker_config["prompt_prefix_file"]
    prompt_prefix = prefix_path.read_text()
    return prompt_prefix

if __name__ == "__main__":
    print(pymaker_config["ollama_host_ip"])
