import utils
import random


def main():
    questions = utils.load_questions()

    random.shuffle(questions)

    print("Игра начинается!")

    for question in questions:

        print(question.build_question())

        user_answer = input()
        question.user_answer = user_answer
        question.asked = True

        if question.is_correct():
            question.points = question.get_points()

        print(question.build_feedback())

    utils.print_stats(questions)


if __name__ == '__main__':
    main()
