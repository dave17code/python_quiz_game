import random
from quiz import Quiz

class QuizGame:
    def __init__(self):
        self.quizzes = []
        self.best_score = {"correct": 0, "total": 0, "percent": 0}

    def run(self):
        while True:
            self.show_menu()
            menu_number = self.get_int_input("선택: ", 1, 5)

            if menu_number == 1:
                self.play_quiz()
            elif menu_number == 2:
                self.add_quiz()
            elif menu_number == 3:
                self.show_quiz_list()
            elif menu_number == 4:
                self.show_best_score()
            elif menu_number == 5:
                print("\n프로그램을 종료합니다.")
                break

    def show_menu(self):
        print("\n" + "=" * 48)
        print("        🎯 나만의 Python 퀴즈 게임 🎯")
        print("=" * 48)
        print("1. 퀴즈 풀기\n2. 퀴즈 추가\n3. 퀴즈 목록\n4. 점수 확인\n5. 종료")
        print("=" * 48)

    def play_quiz(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 먼저 퀴즈를 추가해주세요.")
            return

        questions = self.quizzes[:]
        random.shuffle(questions)

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(questions)}문제)")
        correct_count = 0

        for index, quiz in enumerate(questions, start=1):
            print("\n" + "-" * 40)
            quiz.display(index=index)
            user_answer = self.get_int_input("정답 입력 (1-4): ", 1, 4)

            if quiz.is_correct(user_answer):
                print("✅ 정답입니다!")
                correct_count += 1
            else:
                correct_text = quiz.choices[quiz.answer - 1]
                print(f"❌ 오답입니다. 정답은 {quiz.answer}번 ({correct_text}) 입니다.")

        total_count = len(questions)
        percent = int((correct_count / total_count) * 100) if total_count else 0

        print("\n" + "=" * 48)
        print(f"🏆 결과: {total_count}문제 중 {correct_count}문제 정답! ({percent}점)")

        if self.is_new_best_score(correct_count, total_count, percent):
            self.best_score = {
                "correct": correct_count,
                "total": total_count,
                "percent": percent,
            }
            print("🎉 새로운 최고 점수입니다!")
        else:
            print("🙂 최고 점수는 그대로 유지됩니다.")
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

    def show_best_score(self):
        if self.best_score["total"] == 0:
            print("\n아직 퀴즈를 풀지 않았습니다.")
            return
        print(
            "\n🏆 최고 점수: "
            f"{self.best_score['percent']}점 "
            f"({self.best_score['total']}문제 중 {self.best_score['correct']}문제 정답)"
        )

    def is_new_best_score(self, correct, total, percent):
        current_percent = self.best_score.get("percent", 0)
        current_correct = self.best_score.get("correct", 0)
        if percent > current_percent: return True
        if percent == current_percent and correct > current_correct: return True
        return False

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