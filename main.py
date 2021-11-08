import json
import random

def shuffle(lst):
    new_lst = lst.copy()
    random.shuffle(new_lst)
    return new_lst

def game(MEMORY_DICT):
    score = 0
    cycles = 0
    while True:
        for random_value in shuffle(list(MEMORY_DICT)):
            real_answers = MEMORY_DICT[random_value]
            answer = input(f"what is the value associated with {random_value}: ")

            if type(real_answers) == list:
                check = answer.lower() in [real_answer.lower() for real_answer in real_answers]
            else:
                check = answer.lower() == real_answers.lower()

            if check:
                score += 1
                print(f"Correct! Score:{score}")
            else:
                score = 0
                print(f"False! The correct answer was any of: {real_answers}")
        cycles += 1
        print(f"cycle! total:{cycles}")


def main():
    MEMORY_DICT = json.loads(open(input("json memory dictionary file name: ")).read())
    game(MEMORY_DICT)


main()
