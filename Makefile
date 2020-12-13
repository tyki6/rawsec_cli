install:
	pip install -r requirements.txt
install-dev:
	pip install -r dev-requirements.txt
full-install: install install-dev
	cd docs && pip install -r requirements.txt && cd ..
lint:
	pre-commit run --all-files
docstr:
	docstr-coverage rawsec_cli tests --skipinit --badge=img --verbose 2
tox:
	pip install tox tox-gh-actions
	tox
test:
	coverage run --branch -p -m pytest
coverage:
	coverage combine | true && coverage report -m
html:
	cd docs && make html && cd ../
deploy:
	pip install setuptools wheel twine
	echo "[pypi]" >> ~/.pypirc
	echo "username = ${PYPI_USERNAME}" >> ~/.pypirc
	echo "password = ${PYPI_PASSWORD}" >> ~/.pypirc
	python setup.py sdist bdist_wheel
	twine upload dist/*
	rm -fr build dist
fake-deploy:
	pip install setuptools wheel twine
	echo "[pypi]" >> ~/.pypirc
	echo "username = ${PYPI_USERNAME}" >> ~/.pypirc
	echo "password = ${PYPI_PASSWORD}" >> ~/.pypirc
	python setup.py sdist
	twine upload --repository-url https://test.pypi.org/legacy/ dist/*
	rm -fr build dist
docker:
	docker build -t docker.pkg.github.com/$IMAGE_NAME:$DOCKER_TAG .
	docker push docker.pkg.github.com/$IMAGE_NAME:$DOCKER_TAG
freeze:
	pip freeze > freeze.txt
clean:
	rm -rf docs/build .tox .pytest_cache build  rawsec.egg-info dist coverage_html_report   dumpSyntax .coverage .coverage.* .rnd .mypy_cache
help:
	@echo "make install           Install requirements."
	@echo "make install-dev       Install dev requirements."
	@echo "make full-install      Install requirements + dev requirements + docs requirements."
	@echo "make lint              Run Lint."
	@echo "make docstr            Run docstr report."
	@echo "make tox               Run Unit test tox."
	@echo "make test              Run Unit test."
	@echo "make coverage          Show coverage report."
	@echo "make html              Generate docs."
	@echo "make deploy            Deploy package on pypi."
	@echo "make fake-deploy       Test Deploy."
	@echo "make docker            Build docker and pushblish on github registry."
	@echo "make freeze            Run pip freeze."
	@echo "make clean             Clean Your project.Delete useless file."
	@echo "make help              Show this help message."
