test:
	# pytest --cov=./tests -v --cov-report=xml
	py.test -n 8 --boxed --junitxml=report.xml
coverage:
	coverage xml
