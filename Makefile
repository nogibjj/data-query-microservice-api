install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py 10_Code/*py 

lint:
	# pylint --disable=R,C --ignore-patterns=test_.*?py *.py dblib
	pylint --disable=R,C *.py Source_Data_00/*.py Code_10/*.py

test:
	# python -m pytest -vv --cov=Code_10 --cov=main test_*.py

build:
 	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 9e4cf21dba97

deploy:
 	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 450825970415.dkr.ecr.us-east-1.amazonaws.com
	docker build -t globaltemperatures706 .
	docker tag globaltemperatures706:latest 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	docker push 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	
all: install format lint #deploy test