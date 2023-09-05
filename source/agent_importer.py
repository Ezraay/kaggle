import importlib
import re

from source.core.agent import Agent


def __to_snake_case(pascal_case: str) -> str:
    """
        Converts a PascalCase string to snake_case.
        Parameters:
        ---------
        pascal_case : str
            The input string in PascalCase format.

        Returns:
            The converted string in snake_case format.
    """
    return re.sub(r'(?<!^)(?=[A-Z])', '_', pascal_case).lower()


def import_agent(class_name: str) -> type:
    """
        Dynamically imports an agent's class based on its class name. Assumes
        agent files are in a folder named 'agents' and the file naming convention
        is snake_case corresponding to the PascalCase class name.

        Parameters:
        ----------
        class_name : str
        The name of the agent's class in PascalCase.

        Return:
        The imported class of the agent.

        Raises:
        ------
        Import Error:
            If the module cannot be imported.
        AttributeError:
            If the specified class cannot be found within the imported module.
        AssertionError:
            If the imported class is not a subclass of the Agent base class.
    """
    base_path = "source.agents"
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
