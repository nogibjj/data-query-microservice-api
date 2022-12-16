install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

format:	
	black *.py

lint:
	pylint --disable=R,C --ignore-patterns=__*__.py --disable=W0511,E1101 *.py main/app/*.py main/data/*.py main/eda/*.py main/fastapi-apis/*.py main/helpers/*.py main/tests/*.py

test:
	# python -m pytest -vv --cov=Code_10 --cov=main test_*.py
	python -m pytest -vv --cov=main main/tests/test_*.py

build:
 	#build container
	docker build -t deploy-fastapi .

run:
	#run docker
	docker run -p 127.0.0.1:8080:8080 2d1505f9302f

deploy:
 	#deploy
	aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin 450825970415.dkr.ecr.us-east-1.amazonaws.com
	docker build -t globaltemperatures706 .
	docker tag globaltemperatures706:latest 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	docker push 450825970415.dkr.ecr.us-east-1.amazonaws.com/globaltemperatures706:latest
	
all: install format lint test deploy