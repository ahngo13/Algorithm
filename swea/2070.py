import sys

sys.stdin = open('2070_input.txt')

TC = int(input())

for tc in range(1, TC+1):
    a,b = list(map(int, input().split()))
    sign = ''
    if a>b:
        sign = '>'
    elif a<b:
        sign = '<'
    else:
        sign = '='
    print(f'#{tc} {sign}')

# 1. 합체, concatenation (+) 'hello ' + 'world' =>
#   -> + 
# 2. 수술, interpolation `hello ${name}`
#   -> f'{name}'