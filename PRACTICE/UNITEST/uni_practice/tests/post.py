class Post:
    def __init__(self, title: str, content: str):
        self.title = title
        self.content = content

    def json(self):
        return {"title": self.title,
                "content": self.content
                }

    def __repr__(self):
        return f"{self.title}, {self.content}"
