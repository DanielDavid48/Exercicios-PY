
print('\033[32mBem vindo!\033[m')

s = 0

for x in range(1, 500, 2):
    if x % 3 == 0:
        s += x
print(f'{s}')
print('FIM')