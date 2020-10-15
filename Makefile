NAME=ml_api
COMMIT_ID=$(shell git rev-parse HEAD)


build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web:$(COMMIT_ID) .

push-ml-api-heroku:
	echo Baah@2019 | docker login --username baahdocker --password-stdin registry.heroku.com
	docker tag ml_api registry.heroku.com/falcon1-ml/web
	docker push registry.heroku.com/falcon1-ml/web
	




