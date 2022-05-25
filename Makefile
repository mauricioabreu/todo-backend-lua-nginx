run:
	@docker-compose up api

test:
	@docker-compose up test

formatpy:
	@black