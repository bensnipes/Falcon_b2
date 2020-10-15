NAME=ml_api
COMMIT_ID=$(shell git rev-parse HEAD)


build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web:$(COMMIT_ID) .

push-ml-api-heroku:
	heroku container:login
	echo Baah@2019 | docker login --username baahdocker --password-stdin registry.heroku.com
	heroku container:push web --app falcon1-ml
	




