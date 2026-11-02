# 동적페이지 라이브러리 설치
# pip install playwright    # 셀레니움과 비슷한 동적 페이지 조작 라이브러리
# playwright install        # 크롬과 비슷한 백그라운드용 브라우저 설치(크로미움)

import asyncio              # 비동기 라이브러리
from playwright.async_api import async_playwright   # 비동기 동적 페이지 라이브러리


# 예제3] 동적 페이지 크롤링, 대기/이벤트 존재하는 상태
# 1) 크롤링할 페이지 주소 가져온다. 파라미터 분석, ssc=검색결과텝메뉴, query=검색어
url = "https://search.naver.com/search.naver?ssc=tab.image.all&query=카리나"
# 2) 비동기 함수 만들기
# async def 함수명() : # 함수 선언하고 동기화
async def run() :
    item_list = []
    # 2-1) async_playwright() 실행하고 종료되기 전까지 동기화 처리
    async with async_playwright() as p :    
        # 2-2) 크로미움(구글회사가 제공하는 백그라운드 브라우저)
        # await p.chromium.launch(headless = True백그라운드/False뷰모드)
        browser = await p.chromium.launch(headless = False)
        # 2-3) 현재 실행된 크로미움의 새로운 페이지(빈 페이지) 
        page = await browser.new_page()
        # 2-4) 빈 페이지에 특정한 URL 주소 대입
        await page.goto(url)
        # 3) 스크롤 내리기, 2번
        for i in range(2) :
            await page.wait_for_timeout(3000)   # page.wait_for_timeout(3000): 밀리초만큼 대기상태 함수 
            # await page.evaluate("JS코드삽입")
            # window.scrollTo(가로, 세로): 스크롤 이동함수
            # document.body.scrollHeight: 현재 페이지의 스크롤 세로 높이
            # window.scrollTo(0,document.body.scrollHeight): 현재 스크롤 페이지의 가장 하단으로 이동
            await page.evaluate("window.scrollTo(0,document.body.scrollHeight)")

            # 4) 특정 마크업 가져오기, .query_selector: 1개, .query_selector_all : 여러개 
            items =  await page.query_selector_all(".title_item")
            # 5) 반복문 이용한 사진/제목
            for item in items :
                title = await item.query_selector(".info_title")
                title = await title.inner_text() if title.inner_text() else "제목없음" # 특정한 마크업의 사이 텍스트 추출
                image = await item.query_selector("img._fe_image_tab_content_thumbnail_image")
                image = await image.get_attribute("src") if image else "이미지없음"   # 특정한 마크업의 속성값 추출
                item_list.append({"제목": title, "사진": image})
    return item_list


# *** asyncio.run(동기화함수())
item_list = asyncio.run(run())
print(item_list)