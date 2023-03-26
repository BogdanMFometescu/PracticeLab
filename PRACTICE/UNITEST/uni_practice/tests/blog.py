from tests.post import Post


class Blog:
    def __init__(self, title: str, author: str):
        self.title = title
        self.author = author
        self.posts = []

    def __repr__(self):
        return f"{self.title} by {self.author} ({len(self.posts)} posts)"

    def create_post(self, title: str, content: str):
        self.posts.append(Post(title, content))

    def json(self):
        return {
            "title": self.title,
            "author": self.author,
            "posts": [post.json() for post in self.posts]
        }
