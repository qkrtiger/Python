class MyCal:
    @staticmethod
    def add(a, b):
        print(f'{a} + {b} = {a + b}')
    
    @staticmethod
    def sub(a, b):
        print(f'{a} - {b} = {a - b}')
        
MyCal.add(5, 7)
MyCal.sub(6, 3)