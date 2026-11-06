from quiz import Quiz

# 퀴즈 데이터
quiz_list = [
    Quiz("파이썬의 창시자는?", ["귀도 반 로섬", "린우스 토르발즈", "비야네 스트롭스트룹", "제임스 고슬링"], 1),
    Quiz("1 + 1 = ?", ["1", "2", "3", "4"], 2),
    Quiz("파이썬에서 출력하는 함수는?", ["input", "print", "open", "len"], 2),
]

def display_menu():
    """메뉴 화면 출력"""
    print("\n" + "="*50)
    print("        🎯 나만의 퀴즈 게임 🎯")
    print("="*50)
    print("1. 퀴즈 풀기")
    print("2. 퀴즈 추가")
    print("3. 퀴즈 목록")
    print("4. 점수 확인")
    print("5. 종료")
    print("="*50)

def get_menu_choice():
    """메뉴 선택 입력 (예외 처리 포함)"""
    while True:
        try:
            choice = input("선택: ").strip()
            
            # 빈 입력 처리
            if not choice:
                print("⚠️ 입력이 비어있습니다.")
                continue
            
            # 숫자 변환
            choice = int(choice)
            
            # 범위 확인
            if 1 <= choice <= 5:
                return choice
            else:
                print("⚠️ 1-5 사이의 숫자를 입력하세요.")
        
        except ValueError:
            print("⚠️ 숫자를 입력하세요.")
        except (KeyboardInterrupt, EOFError):
            print("\n프로그램을 종료합니다.")
            return 5  # 종료로 처리

def play_quiz():
    """퀴즈 풀기 - 준비 중"""
    print("\n📝 퀴즈를 시작합니다! (총 {}문제)".format(len(quiz_list)))
    score = 0
    
    for number, quiz in enumerate(quiz_list, 1):
        print("\n" + "-"*50)
        quiz.display(number)
        
        while True:
            try:
                user_answer = int(input("정답 입력: "))
                if 1 <= user_answer <= len(quiz.choices):
                    break
                else:
                    print(f"⚠️ 1-{len(quiz.choices)} 사이의 숫자를 입력하세요.")
            except ValueError:
                print("⚠️ 숫자를 입력하세요.")
        
        if quiz.check(user_answer):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸습니다! 정답은 {quiz.answer}번입니다.")
    
    print("\n" + "="*50)
    print(f"🏆 결과: {len(quiz_list)}문제 중 {score}문제 정답! ({score*100//len(quiz_list)}점)")
    print("="*50)

def add_quiz():
    """퀴즈 추가 - 준비 중"""
    print("\n📌 새로운 퀴즈를 추가합니다.")
    print("(준비 중입니다)")

def show_quiz_list():
    """퀴즈 목록 - 준비 중"""
    print("\n📋 등록된 퀴즈 목록 (총 {}개)".format(len(quiz_list)))
    print("-"*50)
    for i, quiz in enumerate(quiz_list, 1):
        print(f"[{i}] {quiz.question}")
    print("-"*50)

def show_score():
    """점수 확인 - 준비 중"""
    print("\n🏆 점수 확인")
    print("(준비 중입니다)")

def main():
    """메인 루프"""
    print("\n✅ 저장된 데이터를 불러왔습니다. (퀴즈 {}개)".format(len(quiz_list)))
    
    while True:
        try:
            display_menu()
            choice = get_menu_choice()
            
            if choice == 1:
                play_quiz()
            elif choice == 2:
                add_quiz()
            elif choice == 3:
                show_quiz_list()
            elif choice == 4:
                show_score()
            elif choice == 5:
                print("\n👋 프로그램을 종료합니다.")
                break
        
        except (KeyboardInterrupt, EOFError):
            print("\n👋 프로그램을 종료합니다.")
            break

if __name__ == "__main__":
    main()
