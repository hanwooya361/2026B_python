# 비지니스 로직 == AI 모델 예측
import pandas as pd
class ItemService :
    # 생성자 
    def __init__(self):
        # self.변수명 = 값:  멤버변수
        self.df = pd.DataFrame([
            {'id':1, 'name':'콜라', 'price':1000},
            {'id':2, 'name':'사이다', 'price':2000}
        ])
    # 함수 
    def items(self):
        # df.to_dict(orient="records") 
        # 행마다 딕셔너리 반환해 리스트 반환
        return self.df.to_dict(orient="records")
###############################################################
# 서비스 객체 생성 
item_service = ItemService() 