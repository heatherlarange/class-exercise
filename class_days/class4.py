import json
import logging
from pathlib import Path

import pandas as pd
import yaml
import os
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)-8s %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


def inspect_csv(filepath):
    """Read a CSV file and display basic information."""
    # 1. Open the file and read it using pd.read_csv.
    # 2. Log the filepath at INFO.
    # 3. Print the first 3 rows.
    df = pd.read_csv("sample.csv")
    logger.info(f"Inspecting CSV: {filepath}")
    print(df.head(3))
    pass


def inspect_json(filepath):
    """Read a JSON file and display basic information."""
    # 1. Open the file and read it using json.load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    df = json.load(filepath)
    logger.info(f"Inspecting JSON: {filepath}")
    print(df)
    pass


def inspect_yaml(filepath):
    """Read a YAML file and display basic information."""
    # 1. Open the file and read it using yaml.safe_load().
    # 2. Log the filepath at INFO.
    # 3. Print the contents.
    df = yaml.safe_load(filepath)
    logger.info(f"Inspecting YAML: {filepath}")
    print(df)
    pass


def inspect_env():
    """Read a .env file and display basic information."""
    # 1. Log at INFO that .env was loaded.
    # 2. Print keys.
    # Do not print passwords, API keys, or other secret values.

    load_dotenv()

    keys = [
        key for key in ["USERNAME", "PASSWORD"]
        if os.getenv(key) is not None
    ]
    logger.info(".env loaded")
    print(keys)


def main():
    # 1. Create a Path object for the data directory.
    # 2. Use the / operator to build the CSV, JSON, and YAML paths.
    # 3. Call each inspection function using the matching path.
    # 4. Call inspect_env() without an argument.
    data_dir = Path("data")

    csv_path = data_dir / "data.csv"
    json_path = data_dir / "data.json"
    yaml_path = data_dir / "data.yaml"

    inspect_csv("csv_path")
    inspect_json("json_path")
    inspect_yaml("yaml_path")
    inspect_env()
    pass


if __name__ == "__main__":
    main()