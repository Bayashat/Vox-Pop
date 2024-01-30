class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "name": "Ali", "comment_date": "15.02.2022", "context": "This is a comment", "category": "Positive"},
            {"id": 2, "name": "Ahmed", "comment_date": "30.01.2023", "context": "I hate the World", "category": "Negative"},
            {"id": 3, "name": "Mohamed", "comment_date": "31.12.2024", "context": "Happy New Year everyone", "category": "Positive"},
            {"id": 4, "name": "Sayed", "comment_date": "27.09.2020", "context": "I love the World", "category": "Positive"},
            {"id": 5, "name": "Mahmoud", "comment_date": "04.03.2002", "context": "I want to kill everyone", "category": "Negative"},
            {"id": 6, "name": "Mahmoud", "comment_date": "19.05.2015", "context": "Hope the world be better and better", "category": "Positive"},
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
