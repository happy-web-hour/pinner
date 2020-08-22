db.createCollection("pinner");
db.pinner.insertMany([
	{
		"pin": "123e4567-e89b-12d3-a456-426614174000",
		"users":[
			{
				"userId": "us1e4567-e89b-12d3-a456-426614174000",
				"name": "Joao zinho da silva"
			},
			{
				"userId": "us2e4567-e89b-12d3-a456-426614174000",
				"name": "Gabibol faz mais um"
			}
		]
	}
]);