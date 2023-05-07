"# SirBagusAPI" 

Endpoint	Method	Description	Body Request	Body Response
/	GET	Welcome message	-	{"message": "Welcome to my Todo API!"}
/todos/{id}	GET	Get Todo from ID	-	{"title": "WADS", "description": "MAKING API", "time": "07/05/2023 20:34:52", "completed": true}
/todos/by_title/{title}	GET	Get Todo by using the Title	-	{"title": "WADS", "description": "MAKING API", "time": "07/05/2023 20:34:52", "completed": true}
/todos/{id}	POST	Create a new Todo	{"title": "string", "description": "string", "time": "string", "completed": true}	{"message": "Todo created successfully", "todo": {"title": "Chemistry", "description": "Exercise 6", "time": "07/05/2023 20:34:52", "completed": true}}
/todos/{id}	PUT	Update Todo	{"title": "string", "description": "string", "time": "string", "completed": true}	{"message": "Todo updated successfully", "todo": {"title": "Math", "description": "Exercise 7", "time": "07/05/2023 20:34:52", "completed": true}}
/todos/{id}	DELETE	Delete Todo	-	{"message": "Todo deleted successfully", "id": 1}
/todos/next_7_days	GET	Get Todos for the next 7 days	-	[{"title": "WADS", "description": "MAKING API", "time": "08/05/2023 10:00:00", "completed": false}, {"title": "Chemistry", "description": "Exercise 6", "time": "10/05/2023 09:00:00", "completed": false}]
/todos/delete_past	DELETE	Delete Todos that are more than 7 days old	-	{"message": "Todos deleted successfully", "count": 2}
