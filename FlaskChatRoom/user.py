

class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password =password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return self.name
