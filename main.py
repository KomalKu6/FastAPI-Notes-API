from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()
notes = []
class Note(BaseModel):
    title:str
    content: str


@app.post("/notes")
def create_note(note:Note):
    new_note = { 
     "id":len(notes) + 1,
        "title": note.title,
    "content": note.content

    }
    notes.append(new_note)
    return {
         "message": "note created successfully", "note": new_note}

@app.get("/")
def home():
    return {"message": "Welcome to the Notes API"}

@app.get("/notes")
def get_notes():
    return notes

