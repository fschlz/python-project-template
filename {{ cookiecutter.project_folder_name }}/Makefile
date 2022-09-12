.PHONY: \
	setup-env install install-dev tests \
	docker-build-run docker-build docker-run \
	docker-rm docker-rm-container dokcer-rm-image \
	pre-commit docs sphinx_html sphinx_apidoc
.DEFAULT_GOAL := run

export DOCKER=docker
export DOCKERFILE=Dockerfile
export IMAGE_NAME=templateproject-image
export CONTAINER_NAME=templateproject-container
export HOST_PORT=9999
export CONTAINER_PORT=9999

# all commands should be executed in the root dir or the project,
# specific environments should be deactivated

env-dev:
	poetry install --dev

install:
	poetry add $(pkg)

install-dev:
	poetry add --dev $(pkg)

requirements:
	poetry export -f requirements.txt --output ./src/requirements.txt

docker-build-run: docker-build docker-run

docker-build:
	$(DOCKER) build -t $(IMAGE_NAME) -f $(DOCKERFILE) .

docker-run:
	$(DOCKER) run -it --rm -p $(HOST_PORT):$(CONTAINER_PORT)/tcp --name $(CONTAINER_NAME) $(IMAGE_NAME) python app.py

docker-rm: docker-rm-container docker-rm-image

docker-rm-container:
	-$(DOCKER) rm $(CONTAINER_NAME)

docker-rm-image:
	-$(DOCKER) image rm $(IMAGE_NAME)

tests:
	poetry run pytest ./tests

pre-commit:
	pre-commit run --all-files

docs: sphinx_apidoc sphinx_html

sphinx_html:
	poetry run sphinx-build -b html docs/source/ docs/build/html -E -a

sphinx_apidoc:
	poetry run sphinx-apidoc -o ./docs/source/modules ./src/{{ cookiecutter.package_name }}
