def str_reverse(str_chaine):
    str_reverse = ""
    for i in range(len(str_chaine)):
        str_reverse += str_chaine[len(str_chaine)-1-i]
    return str_reverse
