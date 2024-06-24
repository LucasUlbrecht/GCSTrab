# model.py
class Issue:
    def __init__(self, title, description, severity, status='open'):
        self.title = title
        self.description = description
        self.severity = severity
        self.status = status
        self.comments = []

    def add_comment(self, comment):
        self.comments.append(comment)

    def close_issue(self):
        self.status = 'closed'

    def __str__(self):
        return f"Issue(title={self.title}, severity={self.severity}, status={self.status})"
