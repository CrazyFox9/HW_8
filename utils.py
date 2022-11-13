import json
from classes.question import Question


def load_questions():
    """ загружает вопросы из файла и создает экземпляры класса Question """

    questions = []

    with open("data/questions.json", "r", encoding="utf-8") as file:
        question_load = json.load(file)

    for question_load in question_load:
        q = question_load.get("q")
        d = int(question_load.get("d"))
        a = question_load.get("a")
        new_question = Question(q, d, a)

        questions.append(new_question)

    return questions


def print_stats(questions):
    """ подсчитывает результаты и выводит статистику """

    score = 0
    answered_question = 0

    for question in questions:
        if question.is_correct():
            answered_question += 1
        score += question.points

    print("Вот и всё!")
    print(f"Отвечено {answered_question} вопроса из {len(questions)}")
    print(f"Набрано баллов: {score}")
