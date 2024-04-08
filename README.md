# Mindful Money Technical Challenge

This is my submission for the Mindful Money technical challenge as part of their interview process. You'll find my solutions to the tasks in `notebooks/match_companies.ipynb`. This notebook imports the `fffunds` package which contains some useful functions for matching company names and a very barebones framework for future work (the `Company` and `Fund` classes).

You can find my notes for future work at `docs/future-work.md`, and the test details can be found at `docs/challenge.md`.

## How to install

You'll need [Poetry](https://python-poetry.org/) to install the dependencies for this project. If you're running this in VS Code, I also recommend running `poetry config virtualenvs.in-project true` to make it easier for VS Code to detect the virtual environment Poetry creates.

After cloning this repository, make sure you're in the root folder and run `poetry install` to install the dependencies to a new Python virtual environment.

If using VS Code, you can then select both the Python interpreter and the Jupyter kernel to the virtual environment Poetry created (`./.venv` if you changed your config as above).
