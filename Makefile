# Tests, linters & formatters
fmt:
  make -k ruff-fmt black

lint:
  make -k ruff black-check mypy

black:
  python -m black .

black-check:
  python -m black --check .

ruff:
  python -m ruff .

ruff-fmt:
  python -m ruff --fix-only .

test:
  python -m pytest

mypy:
  python -m mypy .