from fastapi import FastAPI, HTTPException
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from typing import Annotated, Literal

app = FastAPI()

tasks = {
    'T001': {'title':'FastAPI', 'completion_status':'Pending'},
    'T002': {'title':'LangGraph', 'completion_status':'Ongoing'},
    'T003': {'title':'LangChain', 'completion_status':'Completed'}
}

class Task(BaseModel):
    id: Annotated[str, Field(..., description="Id of the task")]
    title: Annotated[str, Field(..., description="Title of the Task")]
    completion_status: Annotated[Literal['Pending', 'Ongoing', 'Completed'], Field(..., description="Status of the task")]

@app.get('/tasks')
def view_tasks():
    return tasks

@app.get('/tasks/{task_id}')
def view_single_task(task_id: str):
    if task_id in tasks:
        return tasks[task_id] # Fixed: changed 'id' to 'task_id'
    raise HTTPException(status_code=404, detail='Task not found')

@app.post('/create')
def create_data(task: Task):
    if task.id in tasks:
        raise HTTPException(status_code=409, detail="Task Already exists")
    tasks[task.id] = task.model_dump()

    return JSONResponse(status_code=201, content={'message': 'Patient created successfully'})
