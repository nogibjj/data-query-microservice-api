install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py mylib/*py 

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib
	pylint --disable=R,C *.py mylib/*.py

test:
	python -m pytest -vv --cov=mylib --cov=main test_*.py

build:
 	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 5ef41dd238a1

deploy:
 	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 667719398048.dkr.ecr.us-east-1.amazonaws.com
	docker build -t activity_to_cure_boredom .
	docker tag activity_to_cure_boredom:latest 667719398048.dkr.ecr.us-east-1.amazonaws.com/activity_to_cure_boredom:latest
	docker push 667719398048.dkr.ecr.us-east-1.amazonaws.com/activity_to_cure_boredom:latest
	# docker login -u AWS -p $(aws ecr get-login-password --region us-east-1) 667719398048.dkr.ecr.us-east-1.amazonaws.com
	# docker login -u AWS -p $(aws ecr get-login-password --region the-region-you-are-in) xxxxxxxxx.dkr.ecr.the-region-you-are-in.amazonaws.com

all: install format lint test deploy