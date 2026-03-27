import requests
from bs4 import BeautifulSoup

def get_all_world_rates():
    """네이버 금융에서 전 세계 모든 환율 데이터를 가져오는 함수"""
    url = "https://finance.naver.com/marketindex/exchangeList.naver"
    all_rates = {}
    
    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        res = requests.get(url, headers=headers)
        res.encoding = 'euc-kr'
        soup = BeautifulSoup(res.text, 'html.parser')
        
        rows = soup.select("table.tbl_exchange tbody tr")
        for row in rows:
            name_cell = row.select_one(".tit a").text.strip()
            value_cell = row.select_one(".sale").text.strip().replace(",", "")
            # "미국 USD" -> "미국"만 추출
            clean_name = name_cell.split()[0]
            all_rates[clean_name] = float(value_cell)
        return all_rates
    except:
        return {"미국": 1350.0, "유럽": 1450.0, "일본": 900.0}

def start_program():
    print("\n" + "🌐"*25)
    print("🛒 전 세계 모든 국가 자동 인식 쇼핑 가이드 v6.0")
    print("🌐"*25)

    rates = get_all_world_rates()
    print(f"✅ 현재 {len(rates)}개 화폐 정보를 실시간으로 연결 중입니다.")

    # 1. 국가 입력 및 자동 매핑
    country = input("\n📍 구매 국가를 입력하세요 (예: 미국, 프랑스, 일본, 남아공...): ").strip()

    # [핵심 로직] 유럽 국가들을 '유럽' 유로화로 자동 연결
    euro_zone = ["프랑스", "독일", "이탈리아", "스페인", "네덜란드", "벨기에", "오스트리아"]
    if country in euro_zone:
        print(f"🇪🇺 {country}은(는) 유럽 연합 국가이므로 '유럽 유로(EUR)' 환율을 적용합니다.")
        country = "유럽"

    # 2. 환율 사전에서 국가 찾기
    rate = None
    if country in rates:
        rate = rates[country]
    else:
        # "남아공"처럼 줄여 쓴 경우를 위해 키워드 검색
        for key in rates.keys():
            if country in key:
                rate = rates[key]
                country = key
                break
    
    if not rate:
        print(f"⚠️ '{country}' 정보를 찾지 못해 기본값(미국)을 적용합니다.")
        rate = rates.get("미국", 1350.0)
        country = "미국(기본)"

    print(f"💰 적용 환율: {country} = {rate:,.2f}원")

    try:
        # 3. 가격 및 배송비 입력
        price = float(input(f"\n💵 {country} 현지 가격을 입력하세요: "))
        ship_input = input("🚚 배송비를 입력하세요 (없으면 엔터, 있으면 3000, 4500 등): ")
        shipping = float(ship_input) if ship_input else 0

        # 4. 특수 통화 계산 (일본, 베트남 등 100단위 통화)
        # 보통 100단위 환율인 경우 나라 이름에 포함되거나 별도 처리가 필요함
        if country in ["일본", "베트남", "인도네시아"]:
            krw_price = (price / 100) * rate
        else:
            krw_price = price * rate
            
        total = krw_price + shipping

        print("-" * 50)
        print(f"📝 {country} 쇼핑 최종 견적")
        print(f"👉 원화 환산: {krw_price:,.0f}원")
        print(f"👉 설정 배송비: {shipping:,.0f}원")
        print(f"💰 최종 합계: {total:,.0f}원")
        
        # 5. 스마트 어드바이스
        if total >= 200000:
            advice = "🚨 20만원 초과! 관세 면제 한도 확인이 필요합니다."
        elif shipping >= 5000:
            advice = "📦 배송비가 높습니다. 합배송 상품을 찾아보세요!"
        else:
            advice = "✅ 합리적인 가격대입니다. 지금 구매하세요!"
            
        print(f"\n💡 가이드: {advice}")
        print("=" * 50 + "\n")

    except ValueError:
        print("⚠️ 에러: 숫자로만 정확히 입력해 주세요!")

if __name__ == "__main__":
    start_program()