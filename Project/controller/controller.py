# controller.py
from model import Issue
from view import View

class Controller:
    def __init__(self):
        self.issues = []

    def create_issue(self):
        title, description, severity = View.prompt_for_issue_details()
        issue = Issue(title, description, severity)
        self.issues.append(issue)
        print("Issue created successfully!\n")

    def add_comment_to_issue(self, issue_index):
        if 0 <= issue_index < len(self.issues):
            comment = View.prompt_for_comment()
            self.issues[issue_index].add_comment(comment)
            print("Comment added successfully!\n")
        else:
            print("Invalid issue index!\n")

    def close_issue(self, issue_index):
        if 0 <= issue_index < len(self.issues):
            self.issues[issue_index].close_issue()
            print("Issue closed successfully!\n")
        else:
            print("Invalid issue index!\n")

    def display_all_issues(self):
        View.display_issues(self.issues)
