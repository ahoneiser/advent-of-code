.PHONY: lint
lint:
	poetry run ./bin/lint.sh

.PHONY: tests
tests:
	poetry run pytest
