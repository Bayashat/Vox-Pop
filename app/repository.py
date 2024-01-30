class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "name": "Ali", "comment_date": "2021-01-01", "context": "This is a comment", "category": "Positive"},
            {"id": 2, "name": "Ahmed", "comment_date": "2024-01-30", "context": "I hate the World", "category": "Negative"},
            {"id": 3, "name": "Mohamed", "comment_date": "2023-12-31", "context": "Happy New Year everyone", "category": "Positive"},
            {"id": 4, "name": "Sayed", "comment_date": "2022-01-01", "context": "I love the World", "category": "Positive"},
            {"id": 5, "name": "Mahmoud", "comment_date": "2021-01-01", "context": "This is a comment", "category": "Positive"},
            {"id": 6, "name": "Mahmoud", "comment_date": "2021-01-01", "context": "This is a comment", "category": "Positive"},
        ]

    def get_all(self):
        return self.comments

    def get_one(self, comment_id):
        for comment in self.comments:
            if comment["id"] == comment_id:
                return comment
        return None

    def save(self, comment):
        comment["id"] = self.get_next_id()
        self.comments.append(comment)
        return comment

    def get_next_id(self):
        return len(self.comments) + 1
