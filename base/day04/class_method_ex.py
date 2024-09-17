# 인스턴스 생성 개수 파악
class Prod:
    count = 0 # 클래스 속성으로 모든 인스턴스 공통
    
    def __init__(self):
        Prod.count += 1
        
    @classmethod
    def get_count(cls):
        print(f'생산 제품 수 : {cls.count}')
        
p1 = Prod()
p2 = Prod()
p3 = Prod()
p4 = Prod()

Prod.get_count()