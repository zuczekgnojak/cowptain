LINT_DIRS := unit wsgi src
python_version?=3.10

.PHONY: build
build:
	docker build --build-arg="PYTHON_VERSION=$(python_version)" -t cowptain:$(python_version) .

.PHONY: run
run:
	docker run -it --rm cowptain:$(python_version) bash

.PHONY: build-dev
build-dev:
	docker build --build-arg="PIP_ARG=-e" -t cowptain-dev .

.PHONY: run-dev
run-dev:
	docker run -it --rm \
		--name cowptain-dev \
		-v ${PWD}/src:/cowptain/src \
		-v ${PWD}/unit:/cowptain/unit \
		-v ${PWD}/wsgi:/cowptain/wsgi \
		-v ${PWD}/Makefile:/cowptain/Makefile \
		cowptain-dev bash

.PHONY: unit
unit:
	python -m unittest discover unit

.PHONY: wsgiref
wsgiref:
	python -m unittest wsgi/test_wsgiref.py

.PHONY: gunicorn
gunicorn:
	python -m unittest wsgi/test_gunicorn.py

.PHONY: uwsgi
uwsgi:
	python -m unittest wsgi/test_uwsgi.py

.PHONY: black
black:
	python -m black --check --line-length=79 $(LINT_DIRS)

.PHONY: flake8
flake8:
	python -m flake8 $(LINT_DIRS)

.PHONY: isort
isort:
	python -m isort --check --profile black --line-length 79 $(LINT_DIRS)

.PHONY: pylint
pylint:
	python -m pylint --errors-only $(LINT_DIRS)

.PHONY: mypy
mypy:
	python -m mypy $(LINT_DIRS)
