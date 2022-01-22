# 1. 숫자의 의미
def get_secret_word(numbers):
    for i in range(len(numbers)):
        numbers[i] = chr(numbers[i])
    return ''.join(numbers)


print(get_secret_word([83, 115, 65, 102, 89]))

# 2. 내 이름은 몇 일까
def get_secret_number(word):
    total = 0
    word_list = list(word)
    for one in word_list:
        total += ord(one)
    return total


print(get_secret_number('tom'))
# => 336

# 3. 강한 이름
