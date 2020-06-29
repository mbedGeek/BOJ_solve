# BOJ - 17609 Palindrome

import sys
input = sys.stdin.readline

def similar(s):
    if pal(s[1:]):
        return True
    if pal(s[:-1]):
        return True
    return False

def pal(s):
    l = len(s)
    i = 0
    if l % 2:
        while i <= l // 2:
            if s[i] != s[l-1-i]:
                return False
            i += 1
    else:
        while i < l // 2:
            if s[i] != s[l-1-i]:
                return False
            i += 1
    return True

def is_palin(s):
    l = len(s)
    i = 0
    if l % 2:
        while i <= l // 2:
            if s[i] != s[l - 1 - i]:
                if similar(s[i:l-i]):
                    return 1
                return 2
            i += 1
    else:
        while i < l // 2:
            if s[i] != s[l - 1 - i]:
                if similar(s[i:l-i]):
                    return 1
                return 2
            i += 1
    return 0

for _ in range(int(input())):
    inString = input().strip()
    print(is_palin(list(inString)))
