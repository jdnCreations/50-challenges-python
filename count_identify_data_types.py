def count_datatypes(*args):
    # [int, str, bool, list, tuple, dict]
    dt_list = [0, 0, 0, 0, 0, 0]
    for item in args:
        if type(item) == int:
            dt_list[0] += 1
        elif type(item) == str:
            dt_list[1] += 1
        elif type(item) == bool:
            dt_list[2] += 1
        elif type(item) == list:
            dt_list[3] += 1
        elif type(item) == tuple:
            dt_list[4] += 1
        elif type(item) == dict:
            dt_list[5] += 1
    return dt_list


count_datatypes(1, 45, "Hi", False), [2, 1, 1, 0, 0, 0]
count_datatypes([10, 20], ("t", "Ok"), 2, 3, 1), [3, 0, 0, 1, 1, 0]
count_datatypes("Hello", "Bye", True, True, False, {"1": "One", "2": "Two"}, [1, 3], {"Brayan": 18}, 25, 23), [2, 2, 3, 1, 0, 2]
count_datatypes(), [0, 0, 0, 0, 0, 0]
count_datatypes(4, 21, ("ES", "EN"), ("a", "b"), False, [1, 2, 3], [4, 5, 6]), [2, 0, 1, 2, 2, 0]
count_datatypes("Nice", "Bad", 1, 999, 0, False, {"Hi": "Bye"}), [3, 2, 1, 0, 0, 1]