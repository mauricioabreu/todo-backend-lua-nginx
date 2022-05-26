run:
	@docker-compose up api

test:
	@docker-compose up test

format-py:
	@black

reload-nginx:
	@docker kill --signal=SIGHUP nginx-lua-api