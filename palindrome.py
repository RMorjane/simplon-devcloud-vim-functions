from str_reverse import str_reverse
def palindrome(word):
    rev_word = str_reverse(word)
    return (rev_word == word)
