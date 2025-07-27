def supper_reduce_string(s):
    """
    Reduce the string s with no limit of the time.
    """
    prev_s = None
    while s != prev_s:
        prev_s = s
        s = __one_time_reduce(s)
    return s if s else "Empty String"


def __one_time_reduce(s):
    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)
    s = "".join(stack)
    return s
