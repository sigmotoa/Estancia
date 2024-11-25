from fastapi import APIRouter

from data.WebUAA import COURSE_DATA

estancia = APIRouter()


@estancia.get("/lists")
def show_content_list():
    return COURSE_DATA["title"]