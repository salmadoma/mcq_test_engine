.PHONY: help

help: ## This help.
	@awk 'BEGIN {FS = ":.*?## "} /^[a-zA-Z_-]+:.*?## / {printf "\033[36m%-30s\033[0m %s\n", $$1, $$2}' $(MAKEFILE_LIST)

.DEFAULT_GOAL := help

SERVICES := mcq_test_engine postgres_db
DOCKER_COMPOSE_PROJECT := development
DOCKER_COMPOSE := docker-compose -f docker-compose-$(DOCKER_COMPOSE_PROJECT).yaml

# DOCKER TASKS
# Runs all services
run: ## Runs all services
	$(DOCKER_COMPOSE) down
	$(DOCKER_COMPOSE) build
	$(DOCKER_COMPOSE) up

# Down all services
down: ## Down all services
	$(DOCKER_COMPOSE) down

# make generate_env
generate_env: ## Generate .env file, ex: `make generate_env development`
	- cp ./packaging/env/env.$(DOCKER_COMPOSE_PROJECT).example .env
