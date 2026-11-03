# httpx란? 외부 api 통신하는 라이브러리, api 연동 / spring api
# httpx 라이브러리에는 .json() 타입변환 하지만 xml 변환지원x

import httpx
import pandas as pd

# 0] 공공데이터포털 본인 인증키
service_key = "18af255dfe8f68f335c52040b89c218076ce97d04b6744a00c95b4d0e0eddcfb"
# 1] 공공데이터포털 json 형식의 자료 요청
def test1() :
    # https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553?page=1&perPage=10&serviceKey=18af255dfe8f68f335c52040b89c218076ce97d04b6744a00c95b4d0e0eddcfb
    # 2] 신청한 데이터 api의 주소 및 파라미터 분석, page 현재페이지, perPage 페이지당자료수, servicekey
    url = "https://api.odcloud.kr/api/15052602/v1/uddi:855807e2-fe8a-4e47-8a5a-ce1894e410d7_201909031553"
    url += "?page=1"
    url += "&perPage=10"
    url += f"&serviceKey={service_key}"
    # 3] httpx 이용해 통신하기
    response = httpx.get(url)
    print(response)
    # 4] 응답결과 JSON 변환, .json()
    response_json = response.json()
    # 5] 판다스에 저장하기, 
    df = pd.DataFrame(response_json['data'])
    df.info()
test1()

# 2] 공공데이터포털 xml 형식의 자료 요청, 
import xmltodict    # xml 변환 라이브러리
def test2() :
    # 1] 요청할 api주소
    url = "https://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyFullDown"
    url += f"?serviceKey={service_key}"
    url += "pageNo=1&numOfRows=100"
    # 2] httpx 이용한 api 요청
    response = httpx.get(url)
    # 3] 요청 응답 자료를 문자열로 변환해 파이썬 dict 형식으로 변환
    response_xml = xmltodict.parse(response.text)
    print(response_xml)
    # 4] 
    df = pd.DataFrame(response_xml["response"]["body"]["items"]["item"])
    df.info()
test2()