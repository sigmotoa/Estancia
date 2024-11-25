from model.model import CourseItem, CourseContent

COURSE_DATA = [
    CourseItem(
        id=1,
        title="Using CLI",
        key_contents=[
            CourseContent(topic="Why use CLI?", description="The importance and powe of use the CLI", resources=["https://www.freecodecamp.org/news/command-line-for-beginners/"])

        ]
    )
]