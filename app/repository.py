from datetime import datetime

class CommentsRepository:
    def __init__(self):
        self.comments = [
            {"id": 1, "name": "Ali", "comment_date": datetime(2022, 2, 15, 12, 30, 0), "context": "This is a comment", "category": "Positive"},
            {"id": 2, "name": "Ahmed", "comment_date": datetime(2023, 1, 12, 5, 18, 45), "context": "I hate the World", "category": "Negative"},
            {"id": 3, "name": "Mohamed", "comment_date": datetime(2021, 12, 31, 23, 59, 59), "context": "Happy New Year everyone", "category": "Positive"},
            {"id": 4, "name": "Sayed", "comment_date": datetime(2022, 9, 27, 14, 34, 56), "context": "I love the World", "category": "Positive"},
            {"id": 5, "name": "Mahmoud", "comment_date": datetime(2002, 3, 4, 13, 56, 23), "context": "I want to kill everyone", "category": "Negative"},
            {"id": 6, "name": "Mahmoud", "comment_date": datetime(2015, 5, 19, 7, 0, 0), "context": "Hope the world be better and better", "category": "Positive"},
        ]

    def get_all(self):
        # return by the desc order of dates
        return sorted(self.comments, key=lambda comment: comment["comment_date"], reverse=True)

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
