# Todo backend (NGINX+Lua)

Todo backend powered by NGINX and Lua

## Live

There is a public URL here: http://www.todobackend.com/specs/index.html?https://todo-backend-nginx-lua.herokuapp.com/todos

This URL tests all the use cases for an app to be compatible with www.todobackend.com

## Running

`make run` runs the API server.

You can start to use the API endpoints

| Endpoint     	| Action      	| Method 	|               Data                                      	| Response                                                                      	|
|--------------	|-------------	|--------	|-----------------------------------------------------	|-------------------------------------------------------------------------------	|
| /todos       	| Create todo 	| POST   	| JSON(title: string, completed: boolean, order: int) 	| JSON(title: string, completed: boolean, order: int, uid: string, url: string) 	|
| /todos/\<id> 	| Read todo   	| GET    	| N/A                                                 	| JSON(title: string, completed: boolean, order: int, uid: string, url: string) 	|
| /todos/\<id> 	| Delete todo 	| DELETE 	| N/A                                                 	| JSON(title: string, completed: boolean, order: int, uid: string, url: string) 	|
| /todos       	| List todos  	| GET    	| N/A                                                 	| JSON(title: string, completed: boolean, order: int, uid: string, url: string) 	|
| /todos/\<id> 	| Update todo 	| PATCH  	| JSON(title: string, completed: boolean, order: int) 	| JSON(title: string, completed: boolean, order: int, uid: string, url: string) 	|

## Tests

We only have integrations tests.

Before running the test suite, make sure you have the API server running by issuing the following command:

```console
make run
```

Then you can rust the tests:

```console
make test
```