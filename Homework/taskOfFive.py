

def user_greetings(name):
    print(f"Hello there, {name}")


def change_list_elements(array: list, first, second):
    array[first], array[second] = array[second], array[first]


def oh_no_my_essay(essay: str):
    essay = [word[::-1] for word in essay.split()]
    return ' '.join(essay)


def find_cubes(array):
    return [(num, num ** 3) for num in array]


def sort_dict(my_dict: dict, param):
    sorted_dict = my_dict.copy()

    if param == 0 or param == 1:
        sorted_dict = dict(sorted(sorted_dict.items(), key=lambda pair: pair[param]))

    return sorted_dict
