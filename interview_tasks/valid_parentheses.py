"""
Given a string s containing just the characters '(', ')', '{', '}', '[', and ']', determine if the input string is valid.

A string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.


"""
# ------------------------ INPUT DATA ------------------------
# Example 1:
s1 = "()[]{}"
expected1 = True

# Example 2:
s2 = "(]"
expected2 = False

# Example 3:
s3 = "(({{["
expected3 = False
# ------------------------- SOLUTION -------------------------

def solution(string):
    closing = {")":"(", "]":"[", "}":"{"}
    openings = []
    for i in string:
        if i in closing:
            if len(openings) == 0 or openings.pop() != closing[i]:
                return False
        else:
            openings.append(i)
    return True if len(openings) == 0 else False

# -------------------------- TESTS ---------------------------
assert solution(s1) == expected1
assert solution(s2) == expected2
assert solution(s3) == expected3
