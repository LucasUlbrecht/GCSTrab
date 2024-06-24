# view.py
class View:
    @staticmethod
    def display_issue(issue):
        print(f"Title: {issue.title}")
        print(f"Description: {issue.description}")
        print(f"Severity: {issue.severity}")
        print(f"Status: {issue.status}")
        print("Comments:")
        for comment in issue.comments:
            print(f"  - {comment}")
        print("\n")

    @staticmethod
    def display_issues(issues):
        for issue in issues:
            View.display_issue(issue)

    @staticmethod
    def prompt_for_issue_details():
        title = input("Enter issue title: ")
        description = input("Enter issue description: ")
        severity = input("Enter issue severity: ")
        return title, description, severity

    @staticmethod
    def prompt_for_comment():
        return input("Enter your comment: ")
