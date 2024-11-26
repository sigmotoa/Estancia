from model.model import CourseItem, CourseContent

COURSE_DATA = [
    CourseItem(
        id=1,
        title="Using CLI",
        key_contents=[
            CourseContent(topic="Why use CLI?", description="The importance and power of use the CLI", resources=["https://www.freecodecamp.org/news/command-line-for-beginners/"])
        ]
    ),
    CourseItem(
        id=2,
        title="What is GIT?",
        key_contents=[
            CourseContent(topic="What is git?", description="Git is the most used Version Control System used in the world. Allows to manage and share projects in all scales."),
            CourseContent(topic="Official WEB",description="This is the official web site about git.",resources=["https://git-scm.com/"]),
            CourseContent(topic="Git Pro. the book", description="A free book about git. In a lot of languages.", resources=["https://git-scm.com/book/en/v2"]),
            CourseContent(topic="Github is a Service", description="Git is a tool, and github is a service.", resources=["https://www.geeksforgeeks.org/difference-between-git-and-github/"])

        ]
    )
]