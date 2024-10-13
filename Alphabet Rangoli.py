def print_rangoli(size):
    alphabet = [chr(i) for i in range(97, 97 + size)]
    lines = []
    for i in range(size):
        s = '-'.join(alphabet[size-1:i:-1] + alphabet[i:size])
        lines.append(s.center(4*size-3, '-'))
    lines = lines[::-1]
    print('\n'.join(lines + lines[-2::-1]))
if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)
