import json
import random


def shuffle(lst):
    new_lst = lst.copy()
    random.shuffle(new_lst)
    return new_lst


def set_bounds(lst: list, search_str: str, first: bool) -> int:
    try:
        return lst.index(search_str)
    except ValueError:
        if search_str != "":
            print("string not found; using default")
        return 0 if first else len(lst) - 1


def game(MEMORY_DICT, first, last):
    score = 0
    cycles = 0
    keys = list(MEMORY_DICT.keys())

    keys = keys[set_bounds(keys, first, True):set_bounds(keys, last, False)]
    while True:
        for random_value in shuffle(keys):
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
                cycles = 0
                print(f"False! The correct answer was any of: {real_answers}")
                break
        cycles += 1
        print(f"Cycle! Total cycles: {cycles}")


def main():
    try:
        MEMORY_DICT = json.loads(open("dicts/" + input("json memory dictionary file name: ")).read())
        first = input("starting key? leave blank for first key:")
        last = input("ending key? leave blank for last key:")
        game(MEMORY_DICT, first, last)
    except FileNotFoundError:
        print("file not found")
        main()


main()
