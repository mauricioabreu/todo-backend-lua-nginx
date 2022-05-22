FROM openresty/openresty:alpine-fat

RUN apk add --no-cache git  

RUN luarocks install json-lua