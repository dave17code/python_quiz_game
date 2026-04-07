from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []

    def run(self):
        while True:
            self.show_menu()
            menu_number = int(input("선택 (1-5): "))
            
            if menu_number == 5:
                print("\n프로그램을 종료합니다.")
                break

    def show_menu(self):
        print("\n" + "=" * 48)
        print("        🎯 나만의 Python 퀴즈 게임 🎯")
        print("=" * 48)
        print("1. 퀴즈 풀기")
        print("2. 퀴즈 추가")
        print("3. 퀴즈 목록")
        print("4. 점수 확인")
        print("5. 종료")
        print("=" * 48)