class User:
    def __init___(self):
        self.name=None
        self.email=None
        self.phone=None

class UserBuilder(User):
    def __init__(self):
        self.user = User()
    def set_name(self,name):
        self.user.name=name
    def set_email(self,email):
        self.user.email=email
    def set_phone(self,phone):
        
        self.user.phone=phone
    def build(self):
        return self.user

user=(
    UserBuilder()
    .set_name("Anurag"),
    .set_email("dwivedi.anurag2017@gmail.com")
    .set_phone("8871826751")
    .build()
)

print(user.name)
           