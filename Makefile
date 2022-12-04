install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv test_*.py 00_Source_Data/*.py

format:	
	black *.py 00_Source_Data/*py 

lint:
	pylint --disable=R,C *.py 00_Source_Data/*.py

# build:
# 	docker build -t $(IMAGE_NAME) .

# deploy:
	

all: install lint test format #deploy