class Abhi():
    def __init__(self):
        print("hey i am parent")
    
class Super(Abhi):
    def __init__(self):
        print("the next line is from parent class")
        super().__init__()

test=Super()