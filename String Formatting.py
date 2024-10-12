def decimalToBinary(n): 
    return "{0:b}".format(int(n))

def decimaltohex(n): 
    return "{0:x}".format(int(n))

def print_formatted(number):
    width = len(decimalToBinary(number))
    for n in range(1, number + 1):
        n_decimal = str(n).rjust(width)
        n_octal = '{:o}'.format(n).rjust(width)
        n_hex = decimaltohex(n).upper().rjust(width) 
        n_binary = decimalToBinary(n).rjust(width)
        print(n_decimal, n_octal, n_hex, n_binary)
if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
