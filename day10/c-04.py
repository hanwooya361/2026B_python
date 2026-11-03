import asyncio
from playwright.async_api import async_playwright

# 예시4] 동적크롤링 
# 1) 중고나라 홈페이지 제품 크롤링  url = "https://web.joongna.com/search/"
async def run() :   
    ###########  사용자로부터 콘솔에 입력받기
    keyword = input("중고제품명: ")
    min_price = input("최소가격: ")
    max_price = input("최대가격: ")
    # 2) async_playwright() 실행하고 끝날때까지 대기상태
    async with async_playwright() as p :
         # 3) 크로니움 실행
        browser = await p.chromium.launch(headless=False)
        # 기존 브라우저 선언 아래에 추가
        browser = await browser.new_context(
        viewport={"width": 1920, "height": 1080},
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/156.0.0.0 Safari/537.36"
        )
        # 4) 빈 페이지 열기
        page = await browser.new_page()
        # 5) 특정 페이지 이동
        await page.goto(f"https://web.joongna.com/search/{keyword}")
        # 6) 3초 대기상태
        await page.wait_for_timeout(3000)
        # 7) 입력받은 값을 웹페이지에 채우기
        # page.get_by_속성명("속성값")
        # DOM.fill(값)
        await page.get_by_placeholder("최소 가격").fill(min_price)
        await page.wait_for_timeout(1000)   # 1초간 일시정지
        await page.get_by_placeholder("최대 가격").fill(max_price)
        await page.wait_for_timeout(1000)

        # 8) 특정한 마크업 클릭 이벤트 실행, Dom.click()
        await page.get_by_text("적용").click()  # 텍스트로 적용을 갖고있는 마크업 선택
        await page.wait_for_timeout(3000)

        # 9) 제품사진, 명, 가격 추출
        # href^:'/시작주소/' : 시작주소로 시작하는 모든 주소 식별
        items = await page.query_selector_all("div.group > div > a[href^='/product/']")
        for item in items :
            title = await item.query_selector(".typo-body-sm-medium-14")
            title = await title.inner_text() if title else "제품명없음"
            price = await item.query_selector(".typo-title-lg-semibold-18")
            price = await price.inner_text() if price else "제품가격없음"
            image = await item.query_selector(".img")
            image = await image.get_attribute("src") if image else "이미지없음"
            print(title, price, image)


        
asyncio.run(run())