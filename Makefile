PYTHON = python3

setup:
	@echo "Install pynput..."
	@pip install pynput -q
	@pip install py2app -q
test:
	${PYTHON} -m pytest

run:
	${PYTHON} setup.py py2app
	${PYTHON} keylogger.py /Users/adelgadri/Desktop/keylog

fclean:
	@-pip uninstall pynput -yq
	@-pip uninstall py2app -yq
	@rm *.txt
	@rm -rf build .eqqs

.PHONY:            test run fclean%%