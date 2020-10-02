def del_char(s, c):
    res = ''
    if len(c) == 1:
        for i in range(len(s)):
            if s[i] != c:
                res += s[i]
        return res
    else:
        return s


if __name__ == '__main__':
    s = input("\n Enter a string: ")
    c = input("\n Enter del char: ")
    print(del_char(s, c))