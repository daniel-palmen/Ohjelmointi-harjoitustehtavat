class User:
    def __init__(self,firstName,lastName,userName,email,location):
        self.firstName = firstName
        self.lastName = lastName
        self.userName = userName
        self.email = email
        self.location = location
    def describe_user(self):
        print(f'Name: {self.firstName} {self.lastName}')
        print(f'Username: {self.userName}')
        print(f'Email: {self.email}')
        print(f'Location: {self.location}')
    def greet_user(self):
        print(f'Welcome back {self.userName}!')
    