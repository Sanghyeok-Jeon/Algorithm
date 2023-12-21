S = input()
bomb_s = input()

stack = []
for s in S:
    stack.append(s)
    if bomb_s[-1] == s and ''.join(stack[-len(bomb_s):]) == bomb_s:
        del stack[-len(bomb_s):]

if stack:
    print(''.join(stack))
else:
    print('FRULA')