#: Print out this help message
help:
	@grep -B1 -E "^[a-zA-Z0-9_-]+\:([^\=]|$$)" Makefile \
		| grep -v -- -- \
		| sed 'N;s/\n/###/' \
		| sed -n 's/^#: \(.*\)###\(.*\):.*/\2###\1/p' \
		| column -t  -s '###'

#: Create a Python bundle from gallery with shiv
bundle:
	@mkdir -p	bin
	shiv -c gallery -o ./bin/gallery .

#: Create a Python bundle from viewer with shiv
viewer:
	@mkdir -p	bin
	shiv -c gallery-viewer -o ./bin/gallery-viewer .

#: Create a deb package
build:
	@mkdir -p	bin
	fpm -s python -t deb -p bin .

.PHONY: test
#: Run unit tests
test:
	.venv/bin/pytest test/unit

.PHONY: integration-test
#: Run integration tests
integration-test:
	.venv/bin/pytest test/integration

.PHONY: test-all
#: Run all tests
test-all:
	.venv/bin/pytest

#: Create venv for project
venv:
	python -m venv .venv

#: Install dev dependencies
dev-environment:
	pip install ".[test]"

#: Clean build artifacts
clean:
	rm -R build
