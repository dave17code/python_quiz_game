class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question
        self.choices = choices
        self.answer = answer

    def display(self, index=None):
        if index is not None:
            print(f"[문제 {index}]")
        print(self.question)
        print()
        for number, choice in enumerate(self.choices, start=1):
            print(f"{number}. {choice}")
        print()

    def is_correct(self, user_answer):
        return user_answer == self.answer

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }

    @classmethod
    def from_dict(cls, data):
        question = str(data["question"])
        choices = data["choices"]
        answer = int(data["answer"])

        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 정확히 4개여야 합니다.")

        cleaned_choices = [str(choice) for choice in choices]

        if answer < 1 or answer > 4:
            raise ValueError("정답 번호는 1부터 4 사이여야 합니다.")

        return cls(question, cleaned_choices, answer)