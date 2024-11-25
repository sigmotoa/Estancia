from fastapi import APIRouter

from data.WebUAA import COURSE_DATA

estancia = APIRouter()


@estancia.get("/lists")
def show_content_list():
    titles = [{"id": item.id, "title":item.title} for item in COURSE_DATA]
    return titles