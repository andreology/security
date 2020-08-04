class User:
    """sytem user"""
    def __init__(self, trusted=False):
        self.trusted = trusted

    def can_login(self):
        """Only trusted users read data"""
        return self.trusted

def login(user):
    """give access to users with privileges"""
    if user.can_login is True:
        print("All data available")
    else:
        print("No data available")
hacker = User(trusted=False)

employee = User(trusted=True)

login(hacker)
login(employee)
