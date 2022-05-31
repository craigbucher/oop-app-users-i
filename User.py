# your User class goes here

class User:
    def __init__(self, name, email, license, age, gender):
        self.name = name
        self.email = email
        self.license = license
        self.age = age
        self.gender = gender
        
    def __str__(self):
        return f"My name is {self.name}. I am a {self.age} year old {self.gender} and my email address is {self.email}"

alice = User('Alice', 'alice@email.com', 'IL30357688', '22', 'female')
bob = User('Bob', 'bob@email.com', 'IL7358723478', '57', 'male')
charlie = User('Charlie', 'charlie@email.com', 'VA734874', '33', 'male')
print(charlie)
