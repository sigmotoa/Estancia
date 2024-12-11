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
    ),
    CourseItem(
        id=3,
        title="First steps in GIT",
        key_contents=[
            CourseContent(topic="Download", description="Go to the git website and download and install based in your OS.", resources=["https://git-scm.com/downloads/"]),
            CourseContent(topic="Install", description="Click next in the window until finish."),
            CourseContent(topic="Setting Up", description="In the Command Line add your name and email. Is mandatory to sign your commits.", resources=["https://git-scm.com/book/ms/v2/Getting-Started-First-Time-Git-Setup"])
        ]
    ),
    CourseItem(
        id=4,
        title="Your first local repo",
        key_contents=[
            CourseContent(topic="Choose or create an empty folder", description="In an empty folder viewed from CLI run: ´git init .´ ", resources=["https://git-scm.com/book/ms/v2/Git-Basics-Getting-a-Git-Repository"])
        ]
    )
]