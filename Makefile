build:
	@docker build -t todo-backend-nginx-lua .

run:
	@docker run --rm -v $(PWD)/nginx.conf:/usr/local/openresty/nginx/conf/nginx.conf -p 8080:80 todo-backend-nginx-lua