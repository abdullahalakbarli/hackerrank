#Problem link:https://www.hackerrank.com/challenges/string-validators/problem?isFullScreen=true
if __name__ == '__main__':
    s = input()
    alnum = any(c.isalnum() for c in s)
    print(alnum)
    alpha = any(c.isalpha() for c in s)
    print(alpha)
    digit = any(c.isdigit() for c in s)
    print(digit)
    lower = any(c.islower() for c in s)
    print(lower)
    upper = any(c.isupper() for c in s)
    print(upper)
