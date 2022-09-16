from random import choice

coin_list = ['O', 'P']
result = ''
attempt_count = 1
    while result.find('PPP') or result.find('OOO'):
        attempt = choice(coin_list)
        result += attempt
        attempt_count += 1
    else:
        print(result, '(попыток: ', attempt_count, ')')
print(result, attempt_count)