glo_word = input()

def check_palindrome(word):
    rev_word = word[::-1]
    print(rev_word)
    if rev_word == word:
        return print("입력하신 단어는 회문(Palindrome)입니다.")
    else: return print("입력하신 단어는 회문(Palindrome)이 아닙니다.")


check_palindrome(glo_word)