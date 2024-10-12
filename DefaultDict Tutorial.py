from collections import defaultdict
import sys
d = defaultdict(list)
n, m = map(int, input().split())
for i in range(n):
    word = sys.stdin.readline().strip()
    d[word].append(i + 1)  
for i in range(m):
    word = sys.stdin.readline().strip()
    if d[word]:
        print(*d[word])  
    else:
        print(-1)
