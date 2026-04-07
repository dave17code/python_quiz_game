from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []

    def run(self):
        while True:
            self.show_menu()
            menu_number = self.get_int_input("선택: ", 1, 5)

            if menu_number == 2:
                self.add_quiz()
            elif menu_number == 3:
                self.show_quiz_list()
            elif menu_number == 5:
                print("\n프로그램을 종료합니다.")
                break

    def show_menu(self):
        print("\n" + "=" * 48)
        print("        🎯 나만의 Python 퀴즈 게임 🎯")
        print("=" * 48)
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
        print("=" * 48)

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = self.get_nonempty_input("문제를 입력하세요: ")
        choices = []
        for number in range(1, 5):
            choice = self.get_nonempty_input(f"선택지 {number}: ")
            choices.append(choice)
        answer = self.get_int_input("정답 번호 (1-4): ", 1, 4)

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        print("\n✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 48)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("-" * 48)

    def safe_input(self, prompt):
        return input(prompt)

    def get_nonempty_input(self, prompt):
        while True:
            value = self.safe_input(prompt).strip()
            if not value:
                print("⚠️ 빈 입력은 허용되지 않습니다. 다시 입력해주세요.")
                continue
            return value

    def get_int_input(self, prompt, minimum, maximum):
        while True:
            raw_value = self.safe_input(prompt).strip()
            if raw_value == "":
                print("⚠️ 빈 입력은 허용되지 않습니다. 다시 입력해주세요.")
                continue
            try:
                number = int(raw_value)
            except ValueError:
                print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
                continue
            if number < minimum or number > maximum:
                print(f"⚠️ 잘못된 입력입니다. {minimum}-{maximum} 사이의 숫자를 입력하세요.")
                continue
            return number