def del_non_alpha(str_list):
    for item in str_list:
        if not item.isalpha():
            str_list.remove(item)

    return str_list


def is_anagram(first_str, second_str):
    str1_list = list(first_str.lower())
    str2_list = list(second_str.lower())
    print("str1 = {} and str2 = {}".format(str1_list, str2_list))

    str1_list = del_non_alpha(str1_list)
    str2_list = del_non_alpha(str2_list)
    print("str1 = {} and str2 = {}".format(str1_list, str2_list))

    for item in first_str:
        # print("item = ", item)
        if item.isalpha() and item in str2_list:
            str1_list.remove(item)
            str2_list.remove(item)
        print("str1 = {} and str2 = {}".format(str1_list, str2_list))

    if not str1_list and not str2_list:
        return True
    else:
        return False


if __name__ == '__main__':
    # print(is_anagram("spar", "rasp"))
    print(is_anagram("snooze alarms", "Alas No more Zs"))
