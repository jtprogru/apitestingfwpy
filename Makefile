MOCK_URL := http://127.0.0.1:8000
MOCK_BASE_URL := http://127.0.0.1:8000/objects

.DEFAULT_GOAL := help

.PHONY: help install test test-local test-docker mock mock-docker-up mock-docker-down

help: ## Show this help
	@grep -E '^[a-zA-Z0-9_-]+:.*?## .*$$' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "  \033[36m%-18s\033[0m %s\n", $$1, $$2}'

install: ## Install all dependencies (default + dev groups)
	uv sync

test: ## Run tests against the public restful-api.dev service
	uv run pytest -vvv

test-local: ## Run tests against a locally running mock (start it via `make mock` first)
	BASE_URL=$(MOCK_BASE_URL) uv run pytest -vvv

test-docker: ## Build mock image, run tests against it, then tear it down
	docker compose up -d --build mock
	until curl -sf $(MOCK_URL)/health > /dev/null; do sleep 0.3; done; \
		BASE_URL=$(MOCK_BASE_URL) uv run pytest -vvv; status=$$?; \
		docker compose down; \
		exit $$status

mock: ## Run the FastAPI mock locally on :8000
	uv run --group mock uvicorn mock_service.main:app --host 0.0.0.0 --port 8000 --reload

mock-docker-up: ## Start the mock service in Docker
	docker compose up -d --build mock

mock-docker-down: ## Stop and remove the mock service container
	docker compose down
