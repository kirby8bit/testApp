.PHONY = help setup run 

.DEFAULT_GOAL = help

help:
	@echo "---------------HELLO-----------------"
	@echo "---------------REKRUTO-----------------"
	@echo "To setup venv type make setup"
	@echo "To run the project type make run"
	@echo "enter in your browser: localhost:8000/?name=Rekruto&message=Давай дружить!"
	@echo "------------------------------------"

setup:
	python3.8 -m venv env

run:
	docker-compose up 