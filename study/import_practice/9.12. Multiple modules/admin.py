from user import User
from priveleges import Priviliges

class Admin(User):
    """Represent a Admin user"""
    def __init__(self, first_name, last_name, password, email, username, hobby, location):
        super().__init__(first_name, last_name, password, email, username, hobby, location)
        self.privileges = Priviliges()