def max_subsequence_12(s):
    k = 12
    stack = []
    to_remove = len(s) - k

    for ch in s:
        while stack and to_remove > 0 and stack[-1] < ch:
            stack.pop()
            to_remove -= 1
        stack.append(ch)

    return int("".join(stack[:k]))


total = 0
with open("input.txt") as f:
    for line in f:
        line = line.strip()
        if len(line) >= 12:
            total += max_subsequence_12(line)

print(total)
