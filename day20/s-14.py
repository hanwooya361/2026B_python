# 텍스트 마이닝 실습에 필요한 데이터셋
import pandas as pd
url = "https://raw.githubusercontent.com/bab2min/corpus/master/sentiment/naver_shopping.txt"
df = pd.read_table(url, names=['rating', 'review']) # rating: 평점, review: 리뷰
df = df[df['rating'] != 3]  # 평점 3 제외
df['label'] = (df['rating'] >= 4).astype(int)   # 평점4 이상은 긍정, 평점2 이하 부정
df_sample = df.sample(n=5000, random_state=42).reset_index(drop=True)   # 전체 데이터셋에서 특정n개 샘플링
print(df_sample.shape)
# 1) 텍스트에서 전처리 = 정규표현식 자주 사용됨  vs 리액트/js 입력 유효성검사
import re # 정규표현식 함수
cleaned_list = []    # 정규 표현식 통과한 목록
for text in df_sample['review']:    # 리뷰들을 반복
    # re.sub(r'[표현식]', '치환문자')
    text = re.sub(r'[^가-힣a-zA-z0-9\s]', '', str(text))
    # .join(): 각 리스트 항목 사이에 특정 문자 연결
    #  vs 
    # .split(): 하나의 문자열내 특정문자로 분리해 리스트 반환
    cleaned_text = ''.join(text.split()) # 
    cleaned_list.append(cleaned_text)
df_sample['cleaned_review'] = cleaned_list  
print(df_sample.head(3))

# 2) 한국어 형태소 분석기, kiwi
from kiwipiepy import Kiwi
kiwi = Kiwi()   # 한국어 형태소 분석기 객체 생성
# 3) 사전 학습에 없는 단어 추가
for word in ['가성비', '레전드', '내돈내산']:
    # kiwi.add_user_word('새로운단어', '품사')
    kiwi.add_user_word( word, 'NNG')
# 4. 불용어: 핵심의미가 없는 형태소를 1차적으로 걸러내기 위해 
from kiwipiepy.utils import Stopwords
kiwi_stopwords = Stopwords()
custom_stopwords = {'새끼', '야르', '그냥', '모른다', '그저'}
# 5. 
def tokenize_kiwi(text):
    # kiwi.tokenize(분석할문장, stopwords=불용어객체)
    tokens = kiwi.tokenize(text, stopwords=kiwi_stopwords)   
    # 추출할 품사 키워드, NNG 일반명사, NNP 고유명사, VV 동사, VA 형용사, MAG 일반부사 허용 
    target_tags = {'NNG', 'NNP', 'VV', 'VA', 'MAG'}
    result = []
    for t in tokens:    # 토큰나이즈가 된 리스트에서 원하는것만 필터링/추출
        # t.tag: 품사, t.from: 형태소 문자열 반환
        if t.tag in target_tags and t.form not in custom_stopwords: # 내가 원하는 품사에 포함된 단어이면
            if len(t.form) > 1 or t.form in {'안', '못', '잘'}: # 일부 제외한 한단어 제외
                # 동사 형용사 어간 뒤에 다 붙인다. 좋고 좋아서 좋네요 -> 좋다
                word = t.form + '다' if t.tag in {'VV', 'VA'} else t.form
                result.append(word)
    return result
# 
test_word = df_sample['cleaned_review'].iloc[0]
print(test_word)
print(tokenize_kiwi(test_word))