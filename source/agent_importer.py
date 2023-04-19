import importlib
import re

from core.agent import Agent


def __to_snake_case(pascal_case: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_case).lower()


def import_agent(class_name: str) -> type:
    base_path = "agents"
    file_name = __to_snake_case(class_name)
    module_path = f"{base_path}.{file_name}"

    print(f"Loading agent {class_name} from file {module_path}")

    try:
        module = importlib.import_module(module_path)
    except:
        print("Couldn't import agent file")
        raise

    try:
        agent = getattr(module, class_name)
    except:
        print("File doesn't have importable class: " + class_name)
        raise

    try:
        assert issubclass(agent, Agent)
    except:
        print(f"Agent {class_name} doesn't inherit from base Agent class")
        raise

    return agent
