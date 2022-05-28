FROM openresty/openresty:alpine-fat

RUN apk add --no-cache git  

RUN luarocks install uuid
RUN luarocks install rxi-json-lua
RUN luarocks install lua-resty-cors

COPY api /todoapp/api

COPY nginx.conf /usr/local/openresty/nginx/conf/nginx.conf

CMD sed -i -e 's/$LISTEN_PORT/'"$PORT"'/g' /usr/local/openresty/nginx/conf/nginx.conf && nginx -g 'daemon off;'