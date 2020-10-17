NAME=falcon1-ml
COMMIT_ID=$(shell git rev-parse HEAD)


build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web:$(COMMIT_ID) .

push-ml-api-heroku:
	docker login --username=baahdocker --password=11850bef-71a1-464c-9274-b78095c4ed53 registry.heroku.com
	docker push registry.heroku.com/falcon1-ml/web:$(COMMIT_ID)
	
