class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_human_info(self):
        print(f'Name: {self.name}, {self.age} years old.')

    def introduce_myself(self):
        print(f'Hello, I am {self.name}. Nice to meet you.')

    def tell_us_whats_your_age(self):
        print(f'Glad you asked, buddy. I am {self.age} years old and still growing!')

    @staticmethod
    def feature1():
        print('TEST 1')
        print('TEST 2')


class Worker(Human):

    def print_worker_info(self):
        print(f'This worker is {self.name}, {self.age} years old. They\'re known by their worker ID')
        

    @staticmethod
    def feature1():
        print('WORKA AHHH')
        super(Worker, Worker).feature1()
        
        


marcin = Human('Marcin', 21)
piotr = Worker('Piotr', 19)

piotr.feature1()

