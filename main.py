from quiz import Quiz

quiz_list = [
    Quiz("대한민국의 수도는?", ["서울", "부산", "대구", "인천"], 1),
    Quiz("1 + 1 = ?", ["1", "2", "3", "4"], 2),
    Quiz("파이썬에서 출력하는 함수는?", ["input", "print", "open", "len"], 2),  # ← 새 문제!
]

def run_game():
    score = 0
    print("===== 퀴즈 게임 시작! =====")

    for number, quiz in enumerate(quiz_list, 1):
        quiz.display(number)
        user = int(input("정답 번호 입력: "))

        if quiz.check(user):
            print("✅ 정답입니다!")
            score += 1
        else:
            print(f"❌ 틀렸어요. 정답은 {quiz.answer}번!")

    print(f"\n🎉 게임 종료! 총 {len(quiz_list)}문제 중 {score}개 정답!")

if __name__ == "__main__":
    run_game()