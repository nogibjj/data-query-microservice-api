install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 10_Code/*py 

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib
	pylint --disable=R,C *.py 00_Source_Data/*.py 10_Code/*.py

test:
	# python -m pytest -vv --cov=10_Code --cov=main test_*.py

build:
 	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	# docker run -p 127.0.0.1:8080:8080 6b246acc760c

deploy:
 	#deploy
	# aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 667719398048.dkr.ecr.us-east-1.amazonaws.com
	# docker build -t name_of_app .
	# docker tag name_of_app:latest 667719398048.dkr.ecr.us-east-1.amazonaws.com/name_of_app:latest
	# docker push 667719398048.dkr.ecr.us-east-1.amazonaws.com/name_of_app:latest

all: install format lint #test deploy