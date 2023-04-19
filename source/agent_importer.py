import importlib
import re


def to_snake_case(pascal_case: str) -> str:
    return re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_case).lower()


def import_agent(class_name: str) -> type:
    base_path = "agents"
    file_name = to_snake_case(class_name)
    module_path = f"{base_path}.{file_name}"

    print(f"Loading agent {class_name} from file {module_path}")

    module = importlib.import_module(module_path)
    agent = getattr(module, class_name)
    return agent
