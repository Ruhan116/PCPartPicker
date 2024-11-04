from models.user_model import UserModel

class AuthController:
    def __init__(self):
        self.user_model = UserModel()

    def login(self, username, password):
        return self.user_model.verify_user(username, password)

    def sign_up(self, username, email, password, confirm_password):
        if password != confirm_password:
            print("Passwords do not match")
            return False
        return self.user_model.create_user(username, email, password)