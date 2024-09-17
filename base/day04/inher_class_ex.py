class PersonInfo:
    def __init__(self):
        self.name = ""
        self.age = 0        
    
    def intro(self):
        print('사람입니다.')
        
class ManInfo:
    def gender(self):
        print('남성입니다.')
        
class StudentInfo(PersonInfo, ManInfo):
    def __init__(self):
        self.school = ""
        
    def working(self):
        print('공부합니다.')
        
    def intro(self):
        super().intro()
        print('학생입니다.')
        
std1 = StudentInfo()
std1.intro()
std1.working()
std1.gender()

std1.name = "홍길동"
std1.age = 22
std1.school = "OO학교"

