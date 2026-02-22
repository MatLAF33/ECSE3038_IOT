
from fastapi import FastAPI, HTTPException, Response
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from uuid import UUID, uuid4
from datetime import datetime

app = FastAPI()


class Book(BaseModel):
  id: UUID = Field(default_factory=uuid4)
  title: str
  author: str
  year: int
  genre: str
  created_at: datetime = Field(default_factory=datetime.now)
  updated_at: datetime = Field(default_factory=datetime.now)

class PartialBook(BaseModel):
  title: str | None = None
  author: str | None = None
  year: int | None  = None
  genre: str | None = None

books: dict[UUID, Book] = {}

@app.put("/books/{book_id}") #@ is a decorator, it modifies the behavior of the function that follows it
def full_update_book(book_id: UUID, book_data: Book):
  exists = book_id in books

  book_data.id = book_id
  book_data.updated_at = datetime.now()

  if not exists:
    book_data.created_at = datetime.now()
    books[book_id] = book_data

    return JSONResponse(book_data.model_dump(mode="json"), status_code=201)
  
  else:
    book_data.created_at = books[book_id].created_at
    books[book_id] = book_data
    return book_data
  

@app.patch("/books/{book_id}")
def partial_update_book(book_id: UUID, partial_book_data: PartialBook):

  exists = book_id in books

  if not exists:
    raise HTTPException(detail=f"Book with id: {str(book_id)} not found", status_code=404)
  
  existing_book = books[book_id]

  update_data = partial_book_data.model_dump(exclude_unset=True)

  for field, value in update_data.items():
    setattr(existing_book, field, value)

  existing_book.updated_at = datetime.now()

  books[book_id] = existing_book

  return existing_book

@app.delete("/books/{book_id}")
def delete_book(book_id: UUID):
	exists = book_id in books

	if not exists:
		raise HTTPException(detail=f"Book of id: {str(book_id)} not found", status_code=404)

	del books[book_id]
	return Response(status_code=204)
