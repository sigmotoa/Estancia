from fastapi import APIRouter, Path

from data.WebUAA import COURSE_DATA

estancia = APIRouter()


@estancia.get("/lists")
def show_content_list():
    titles = [{"id": item.id, "title":item.title} for item in COURSE_DATA]
    return titles


@estancia.get("/lists/{item_id}")
def show_one_content(item_id:int=Path(...)):
    for item in COURSE_DATA:
        if item.id==item_id:
            return item

    return {"message":"Item not found"}
