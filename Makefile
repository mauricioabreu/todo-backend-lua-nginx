build:
	@docker build -t todo-backend-nginx-lua .

run:
	@docker run --rm -v $(PWD)/nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf \
		-v $(PWD)/api:/todoapp/api \
		-p 8080:80 todo-backend-nginx-lua
