class Programmer:
    def __init__(self, name, post):
        self.name = name
        self.work_time = 0
        self.posts = {"Junior": 10, "Middle": 15, "Senior": 20}
        self.post = [post, self.posts[post]]
        self.money = 0

    def work(self, time):
        self.work_time += time
        self.money += time * self.post[1]

    def rise(self):
        if self.post[0] == 'Junior':
            self.post = ["Middle", self.posts["Middle"]]
        elif self.post[0] == 'Middle':
            self.post = ["Senior", self.posts["Senior"]]
        elif self.post[0] == 'Senior':
            self.post = ["Senior", self.post[1] + 1]

    def info(self):
        return f"{self.name} {self.work_time}ч. {self.money}тгр."


programmer = Programmer('Васильев Иван', 'Junior')
programmer.work(750)
print(programmer.info())
programmer.rise()
programmer.work(500)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
programmer.rise()
programmer.work(250)
print(programmer.info())
