class Session:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            print("Session instance created")  # Only when first created
            cls._instance = super(Session, cls).__new__(cls)
            cls._instance.current_user = None
        return cls._instance

    def set_user(self, user_id):
        self.current_user = user_id
        print(f"Session set for user: {self.current_user}")

    def get_user(self):
        return self.current_user

    def clear_user(self):
        self.current_user = None
