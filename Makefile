NAME=falcon1-ml
COMMIT_ID=$(shell git rev-parse HEAD)


build-ml-api-heroku:
	docker build --build-arg PIP_EXTRA_INDEX_URL=${PIP_EXTRA_INDEX_URL} -t registry.heroku.com/$(NAME)/web:$(COMMIT_ID) .

push-ml-api-heroku:
	docker tag 1a805e2176bb registry.heroku.com/$(NAME)/web:$(COMMIT_ID)
	docker push registry.heroku.com/$(NAME)/web:$(COMMIT_ID)
	




