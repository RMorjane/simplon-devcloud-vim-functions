def words_count(text_value):
    list_words = text_value.split(' ')
    count = len(list_words)
    for loop_word in list_words:
        ponctue=True
        for c in loop_word:
            ponctue = ponctue and (c in ['.',';','!','?',':',','])
        if ponctue:
            count -= 1
    return count
