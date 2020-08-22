## pinner
### APIs
- POST /pin - cria um novo HH  

**Request**

**Response**
200
```json 
{
	"pin": "string"
}
```
	
- PATCH /pin/{pin} - adiciona o usuário ao pin  
**Request**
```json
{
	"name": "string"
}
```
**Response**
200 
```json
{
    "userId": "string",
    "name": "string"
}
```
404 - Pin not found

- DELETE /pin/{pin}/{userId} - remove usuário do hh

**Request**

**Response**
200 

- GET /pin/{pin}/users - retorna o nome dos usuarios

**Request**
```json 
[
	"string"
]
```

**Response**
200
```json 
[
	{
		"userId": "string",
		"name": "string"
	}
]
```

### Database
Schema:
```json
[
	{
		"pin":"string",
		"users":[
			{
				"userId": "string",
				"name": "string"
			}	
		]
	}
]
```