import json
import random
from pathlib import Path
from quiz import Quiz

class SafeExitRequested(Exception):
    pass

class QuizGame:
    def __init__(self, state_path="state.json"):
        self.state_path = Path(state_path)
        self.quizzes = []
        self.best_score = {"correct": 0, "total": 0, "percent": 0}
        self.load_state()

    def run(self):
        try:
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
                    self.save_state()
                    print("\n프로그램을 종료합니다. 저장이 완료되었습니다.")
                    break
        except SafeExitRequested:
            print("\n입력이 중단되었습니다. 가능한 범위까지 저장한 뒤 안전하게 종료합니다.")
            self.save_state()

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
            self.best_score = {"correct": correct_count, "total": total_count, "percent": percent}
            self.save_state()
            print("🎉 새로운 최고 점수입니다!")
        else:
            print("🙂 최고 점수는 그대로 유지됩니다.")
        print("=" * 48)

    def add_quiz(self):
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = self.get_nonempty_input("문제를 입력하세요: ")
        choices = [self.get_nonempty_input(f"선택지 {i}: ") for i in range(1, 5)]
        answer = self.get_int_input("정답 번호 (1-4): ", 1, 4)
        self.quizzes.append(Quiz(question, choices, answer))
        self.save_state()
        print("\n✅ 퀴즈가 추가되었습니다!")

    def show_quiz_list(self):
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다.")
            return
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)\n" + "-" * 48)
        for index, quiz in enumerate(self.quizzes, start=1):
            print(f"[{index}] {quiz.question}")
        print("-" * 48)

    def show_best_score(self):
        if self.best_score["total"] == 0:
            print("\n아직 퀴즈를 풀지 않았습니다.")
            return
        print(f"\n🏆 최고 점수: {self.best_score['percent']}점 ({self.best_score['total']}문제 중 {self.best_score['correct']}문제 정답)")

    def load_state(self):
        if not self.state_path.exists():
            self.quizzes = self.default_quizzes()
            self.best_score = {"correct": 0, "total": 0, "percent": 0}
            self.save_state()
            print("📂 state.json 파일이 없어 기본 퀴즈 데이터로 시작합니다.")
            return
        try:
            with self.state_path.open("r", encoding="utf-8") as file:
                data = json.load(file)
            self.quizzes = [Quiz.from_dict(item) for item in data.get("quizzes", [])]
            self.best_score = self.normalize_best_score(data.get("best_score"))
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score['percent']}점)")
        except:
            print("⚠️ 데이터 복구 중. 기본 데이터로 덮어씁니다.")
            self.quizzes = self.default_quizzes()
            self.best_score = {"correct": 0, "total": 0, "percent": 0}
            self.save_state()

    def save_state(self):
        data = {"quizzes": [q.to_dict() for q in self.quizzes], "best_score": self.best_score}
        try:
            with self.state_path.open("w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except OSError:
            pass

    def safe_input(self, prompt):
        try:
            return input(prompt)
        except (KeyboardInterrupt, EOFError):
            raise SafeExitRequested

    def get_nonempty_input(self, prompt):
        while True:
            value = self.safe_input(prompt).strip()
            if value: return value
            print("⚠️ 빈 입력은 허용되지 않습니다.")

    def get_int_input(self, prompt, minimum, maximum):
        while True:
            raw_value = self.safe_input(prompt).strip()
            if not raw_value: continue
            try:
                number = int(raw_value)
                if minimum <= number <= maximum: return number
            except ValueError: pass
            print(f"⚠️ {minimum}-{maximum} 사이의 숫자를 입력하세요.")

    def is_new_best_score(self, correct, total, percent):
        current_percent = self.best_score.get("percent", 0)
        current_correct = self.best_score.get("correct", 0)
        return percent > current_percent or (percent == current_percent and correct > current_correct)

    def normalize_best_score(self, best_score):
        if not isinstance(best_score, dict): return {"correct": 0, "total": 0, "percent": 0}
        c, t, p = int(best_score.get("correct", 0)), int(best_score.get("total", 0)), int(best_score.get("percent", 0))
        return {"correct": c, "total": t, "percent": p} if c >= 0 and t >= 0 and p >= 0 else {"correct": 0, "total": 0, "percent": 0}

    def default_quizzes(self):
        return [
            Quiz("Python에서 리스트를 만들 때 사용하는 기호는?", ["{}", "[]", "()", "<>"], 2),
            Quiz("Python에서 문자열 자료형의 이름은 무엇인가요?", ["int", "bool", "str", "list"], 3),
            Quiz("조건에 따라 다른 코드를 실행할 때 사용하는 키워드는?", ["for", "if", "import", "return"], 2),
            Quiz("반복문으로 리스트의 요소를 하나씩 꺼낼 때 사용하는 문장은?", ["while item in list", "for item in list", "if item in list", "def item in list"], 2),
            Quiz("함수를 정의할 때 사용하는 키워드는 무엇인가요?", ["class", "lambda", "def", "try"], 3),
            Quiz("예외 처리를 할 때 함께 사용하는 구문 조합으로 알맞은 것은?", ["if / else", "for / while", "try / except", "class / self"], 3),
            Quiz("데이터를 키(Key)와 값(Value)의 쌍으로 저장하는 자료형은?", ["tuple", "list", "set", "dict"], 4),
            Quiz("화면에 결과값을 출력할 때 사용하는 내장 함수는?", ["input()", "print()", "show()", "display()"], 2),
            Quiz("리스트나 문자열의 길이를 구할 때 사용하는 함수는?", ["len()", "size()", "count()", "length()"], 1),
            Quiz("파이썬의 창시자 이름은 무엇인가요?", ["Linus Torvalds", "James Gosling", "Guido van Rossum", "Brendan Eich"], 3),
        ]