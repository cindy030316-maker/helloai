print("안녕하세요, 파이썬의 세계에 오신 것을 환영합니다!")
import random  # 랜덤 숫자를 뽑기 위한 도구를 가져옵니다.

print("🎮 숫자 맞추기 게임에 오신 것을 환영합니다!")
print("컴퓨터가 1부터 50 사이의 숫자를 하나 생각했습니다. 맞춰보세요!")

# 1. 변수: 데이터를 담는 상자
# 컴퓨터가 1부터 50 사이의 임의의 숫자를 골라서 'secret_number'라는 상자에 담습니다.
secret_number = random.randint(1, 50)

# 2. 반복문: 특정 조건이 될 때까지 계속 반복
# 무한히 반복하라는 뜻입니다. (정답을 맞출 때까지 계속 물어봐야 하니까요!)
while True:
    
    # 3. 입력: 사용자에게 대답 듣기
    # input()은 사용자가 키보드로 치는 것을 가져옵니다. 
    # int()는 입력받은 '글자'를 계산할 수 있는 '숫자'로 바꿔줍니다.
    user_guess = input("숫자를 입력하세요: ")
    user_guess = int(user_guess)
    
    # 4. 조건문: 상황에 따라 다른 행동 하기
    if user_guess == secret_number:
        # 입력한 숫자와 컴퓨터의 숫자가 같을 때 (==는 같다는 뜻)
        print("🎉 정답입니다! 축하합니다!")
        break  # 정답을 맞췄으니 while 반복문을 부수고(break) 끝냅니다!
        
    elif user_guess < secret_number:
        # 입력한 숫자가 정답보다 작을 때
        print("UP! 더 큰 숫자입니다. ⬆️")
        
    else:
        # 입력한 숫자가 정답보다 클 때 (위의 조건이 둘 다 아닐 때)
        print("DOWN! 더 작은 숫자입니다. ⬇️")
        