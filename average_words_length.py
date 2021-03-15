def average_words_length(text_value):
    ponctue_list = ['.',';','!','?',':',',',"'"]
    list_words = text_value.split(' ')
    count = len(list_words)
    sum_length = 0
    for loop_word in list_words:
        ponctue=True
        word_length = 0
        for c in loop_word:
            if c not in ponctue_list:
                word_length += 1
            ponctue = ponctue and (c in ponctue_list)
        if ponctue:
            count -= 1
        else:
            sum_length += word_length
    average = float(sum_length / count)
    return average
