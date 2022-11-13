class Question:

    def __init__(self, text, level, correct_answer):
        self.text = text
        self.level = level
        self.correct_answer = correct_answer

        self.asked = False
        self.user_answer = None
        self.points = 0
        self.max_level = 5

    def __repr__(self):
        return f"Вопрос: {self.text} сложность: {self.level} ответ: {self.correct_answer}"

    def get_points(self):
        """Возвращает int, количество баллов.
        Баллы зависят от сложности: за 1 дается 10 баллов, за 5 дается 50 баллов.
        """

        return int(self.level) * 10

    def is_correct(self):
        """Возвращает True, если ответ пользователя совпадает
        с верным ответом иначе False.
        """

        return self.user_answer == self.correct_answer

    def build_question(self):
        """Возвращает вопрос в понятном пользователю виде, например:
        Вопрос: What do people often call American flag?
        Сложность 4/5
        """

        return f"Вопрос: {self.text}\nСложность {self.level}/{self.max_level}"

    def build_feedback(self):

        """Возвращает :
        Ответ верный, получено __ баллов
        или
        Ответ неверный, верный ответ __
        """

        if self.is_correct():
            return f"Ответ верный, получено {self.points} баллов\n"
        return f"Ответ неверный, верный ответ {self.correct_answer}\n"
