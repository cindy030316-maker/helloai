def run_store():
    # 1. 재고 데이터 (변수와 딕셔너리)
    inventory = {"우유": 5, "삼각김밥": 3, "콜라": 10}
    
    print("="*40)
    print("🏪 미니 편의점 재고 관리 시스템")
    print("="*40)

    while True:
        print(f"\n현재 재고: {inventory}")
        item = input("판매할 물건 이름을 입력하세요 (종료는 'q'): ")

        if item.lower() == 'q':
            print("영업을 종료합니다. 수고하셨습니다!")
            break

        # 2. 조건문으로 재고 확인
        if item in inventory:
            count = int(input(f"{item}을 몇 개 판매하시겠습니까? "))
            
            if inventory[item] >= count:
                # 재고 감소 연산
                inventory[item] -= count
                print(f"✅ {item} {count}개 판매 완료!")
            else:
                print(f"❌ 잔여 재고가 부족합니다! (현재 {inventory[item]}개)")
        else:
            print("❓ 해당 상품은 우리 매장에 없습니다.")

        # 3. 재고 부족 알림 (숫자 게임의 정답 체크 느낌!)
        for name, stock in inventory.items():
            if stock == 0:
                print(f"⚠️ 경고: {name} 재고가 바닥났습니다! 발주가 필요합니다.")

if __name__ == "__main__":
    run_store()