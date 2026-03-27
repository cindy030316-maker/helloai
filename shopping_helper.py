import requests
from bs4 import BeautifulSoup

def get_realtime_rate():
    """네이버 금융에서 실시간 달러 환율을 가져오는 함수"""
    url = "https://finance.naver.com/marketindex/"
    try:
        response = requests.get(url)
        response.encoding = 'euc-kr'
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # 실시간 환율 문자열 추출 (예: "1,350.00")
        rate_text = soup.select_one(".head_info .value").text
        # 계산을 위해 쉼표(,) 제거 후 실수(float)로 변환
        return float(rate_text.replace(",", ""))
    except Exception as e:
        print(f"환율 정보를 가져오지 못했습니다: {e}")
        return None

def start_shopping_helper():
    print("\n" + "="*50)
    print("🛒 글로벌 최저가 계산기: 스마트 직구 도우미")
    print("="*50)

    # 1. 실시간 환율 로드
    exchange_rate = get_realtime_rate()
    
    if exchange_rate:
        print(f"📊 현재 실시간 환율: 1달러 = {exchange_rate:,.2f}원")
        print("-" * 50)

        try:
            # 2. 사용자로부터 달러 가격 입력 받기 (input)
            usd_price = float(input("💵 상품의 달러($) 가격을 입력하세요: "))
            
            # 3. 배송비 설정 (고정 변수)
            shipping_fee = 3000 

            # 4. 산술 연산 (환율 적용 + 배송비 합산)
            krw_price = usd_price * exchange_rate
            total_cost = krw_price + shipping_fee

            # 5. 최종 결과 출력
            print("-" * 50)
            print(f"✅ 원화 환산 금액: {krw_price:,.0f}원")
            print(f"✅ 최종 결제 금액(배송비 {shipping_fee:,}원 포함): {total_cost:,.0f}원")
            print("="*50 + "\n")

        except ValueError:
            print("⚠️ 오류: 숫자 형식으로 금액을 입력해 주세요.")
    else:
        print("프로그램을 실행할 수 없습니다.")

if __name__ == "__main__":
    start_shopping_helper()
    