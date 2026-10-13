import os
from pathlib import Path

import pytest

import main


@pytest.fixture(autouse=True)
def set_src_working_directory():
    """Automatically changes working directory to the directory containing CSV files."""
    # Resolve repository root directory from tests/ test file location
    repo_root = Path(__file__).resolve().parent.parent
    src_dir = repo_root / "site" / "src"

    # Save original working directory
    original_cwd = Path.cwd()

    # Change to site/src
    os.chdir(src_dir)

    yield

    # Restore original working directory after test finishes
    os.chdir(original_cwd)


def test_csv_files_exist():
    # Check if the CSV files exist in the current working directory
    assert Path("BigListChoices.csv").exists(), "BigListChoices.csv does not exist."
    assert Path(
        "LittleListChoices.csv"
    ).exists(), "LittleListChoices.csv does not exist."


@pytest.mark.asyncio
async def test_matching_function():
    # Since pytest-asyncio is configured, await async functions directly instead of asyncio.run()
    await main.run_algo()
