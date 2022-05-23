class vehicle:
    def __init__(self):
        self.car1 = 'Tesla'
        self.car2 = 'Lamorghini'

    def main(self):
        print(f'I have {self.car1}')
        print(f'I have {self.car2}')

obj1 = vehicle()
print(f"1st car - {obj1.car1}")
obj1.main()