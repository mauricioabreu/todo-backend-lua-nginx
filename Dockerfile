FROM openresty/openresty:alpine-fat

RUN apk add --no-cache git  

RUN luarocks install uuid
RUN luarocks install rxi-json-lua
RUN luarocks install lua-resty-cors