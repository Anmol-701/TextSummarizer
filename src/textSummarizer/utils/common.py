import os
import yaml
from pathlib import Path
from typing import Any, List

from box import Box
from box.exceptions import BoxValueError
from ensure import ensure_annotations
from src.textSummarizer.logging import logger


@ensure_annotations
def read_yaml(path_to_yaml: Path) -> Box:
    """
    Reads a YAML file and returns a Box object (dot-accessible dictionary).

    Args:
        path_to_yaml (Path): Path object pointing to the YAML file.

    Raises:
        ValueError: If the YAML file is empty or invalid.
        Exception: For any other exception that occurs.

    Returns:
        Box: A dot-accessible dictionary containing the YAML content.
    """
    try:
        with open(path_to_yaml, "r") as yaml_file:
            content = yaml.safe_load(yaml_file)
            if content is None:
                raise ValueError("YAML file is empty")
            logger.info(f"YAML file loaded successfully: {path_to_yaml}")
            return Box(content)
    except BoxValueError:
        raise ValueError("YAML file is invalid or empty")
    except Exception as e:
        raise e


# @ensure_annotations
def create_directories(path_to_directories: List[Path], verbose: bool = True):
    """
    Creates directories from a list of Path objects.

    Args:
        path_to_directories (List[Path]): List of directory paths to create.
        verbose (bool, optional): Whether to log directory creation. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Created directory at: {path}")
