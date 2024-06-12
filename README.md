# Project Title

Demo Project built using Python with pytest framework

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

```sh 
## Setup configuration for poetry
poetry config virtualenvs.in-project true
poetry lock --no-update
poetry install --no-ansi --no-root
source .venv/bin/activate
```

## Usage
To run the tests, run the following command
```sh
pytest
```

If one needs to run a specific test, then they can run

```sh
pytest -k test_commands
```
