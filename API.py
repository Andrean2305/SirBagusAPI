from fastapi import FastAPI, Path
from typing import Optional
from pydantic import BaseModel
import datetime
from dateutil.relativedelta import relativedelta
from datetime import datetime, timedelta

now = datetime.datetime.now()
date_formatted = now.strftime("%d/%m/%Y %H:%M:%S")

app = FastAPI()

todos = {
    1: {
        "title": "WADS",
        "description": "MAKING API",
        "time": date_formatted,
        "completed": True
    }
}

class Todo(BaseModel):
    title: str
    description: str
    time: str
    completed: bool


class Update(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    time: Optional[str] = None
    completed: Optional[bool] = None

# Endpoints

@app.get("/")
def read_root():
    return {"message": "Welcome to my Todo API!"}


@app.get("/todos/{id}")
def read_todo_by_id(id: int = Path(..., description="ID of the todo to retrieve")):
    if id not in todos:
        return {"error": "Todo not found"}
    return todos[id]


@app.get("/todos/by_title/{title}")
def read_todo_by_title(title: str):
    for id in todos:
        if todos[id]["title"] == title:
            return todos[id]
    return {"error": "Todo not found"}


@app.post("/todos/{id}")
def create_todo(id: int, todo: Todo):
    if id in todos:
        return {"error": "Todo ID already exists"}
    todos[id] = todo.dict()
    return {"message": "Todo created successfully", "todo": todos[id]}


@app.put("/todos/{id}")
def update_todo_by_id(id: int, todo: Update):
    if id not in todos:
        return {"error": "Todo not found"}

    todo_dict = todo.dict(exclude_unset=True)
    todos[id].update(todo_dict)
    return {"message": "Todo updated successfully", "todo": todos[id]}


@app.delete("/todos/{id}")
def delete_todo_by_id(id: int):
    if id not in todos:
        return {"error": "Todo not found"}
    del todos[id]
    return {"message": "Todo deleted successfully", "id": id}

#Assuming all of the assignments have 7 days deadline
@app.get("/todos/next_7_days")
def read_todos_next_7_days():
    todos_in_week = []
    for id in todos:
        todo_date = datetime.datetime.strptime(todos[id]["time"], "%d/%m/%Y %H:%M:%S")
        if todo_date.date() <= (datetime.datetime.now() + datetime.timedelta(days=7)).date():
            todos_in_week.append(todos[id])
    return todos_in_week

#Delete anything pass deadline
@app.delete("/todos/delete_old")
def delete_old_todos():
    deleted_ids = []
    current_time = datetime.now()
    for id, todo in todos.items():
        todo_time = datetime.strptime(todo["time"], "%d/%m/%Y %H:%M:%S")
        if current_time - todo_time > timedelta(days=7):
            deleted_ids.append(id)
    for id in deleted_ids:
        del todos[id]
    return {"message": f"{len(deleted_ids)} todos deleted successfully"}