def min_op(s, start, end):
    
    # if the string is empty
    if start > end:
        return 0

    # if the string has only one character
    if start == end:
        return 1

    # if string has only two characters and both are same
    if start + 1 == end and s[start] == s[end]:
        return 1

    # remove the first character and operate on the rest
    res = 1 + min_op(s, start + 1, end)

    # if the first two characters are same
    if s[start] == s[start + 1]:
        res = min(res, 1 + min_op(s, start + 2, end))

    # find the index of the next character same as the first
    for i in range(start + 2, end + 1):
        if s[start] == s[i]:
            res = min(res, min_op(s, start + 1, i - 1) + min_op(s, i + 1, end))
    return res

str = "2553432"
print(min_op(str, 0, len(str) - 1))
