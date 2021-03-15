#!/usr/bin/python
# -*- coding: latin-1 -*-
from str_reverse import str_reverse
from nbr_reverse import nbr_reverse
from digit_reverse import digit_reverse
from words_count import words_count
from average_words_length import average_words_length
from palindrome import palindrome
from check_duplicates import check_duplicates

if __name__=="__main__":
    while(True):
        choice = int(input("""Choisissez une fonctions a tester :
                1 - inverser une chaine.
                2 - inverser un nombre.
                3 - inverser un digit.
                4 - compter le nombre de mots dans une phrase et la moyenne de leurs tailles.
                5 - tester si un nombre est un palindrome.
                6 - afficher les elements duppliques.\n"""))
        if choice == 1:
            str_value=str(input("Entrez une chaine string : "))
            rev_string = str_reverse(str_value)
            print("Chaine inversee : ",rev_string)
        elif choice == 2:
            nbr_value=int(input("entrez un nombre entier : "))
            rev_int = nbr_reverse(nbr_value)
            print("Nombre inverse : ",rev_int)
        elif choice == 3:
            digit_value=str(input("entrez un nombre : "))
            rev_digit = digit_reverse(digit_value)
            print("Digits inversee : ",rev_digit)
        elif choice == 4:
            text_value=str(input("entrez un text : "))
            count=words_count(text_value)
            print("le nombre de mots est : ",count)
            average = average_words_length(text_value)
            print("average word length : ",average)
        elif choice == 5:
            word=str(input("entrez un mot : "))
            if palindrome(word):
                print(word," est un palindrome")
            else:
                print(word," n'est pas un palindrome")
        elif choice == 6:
            mylist=[]
            size=int(input("entrez le nombre d'éléments : "))
            for i in range(size):
                elem=input("entrez une valeur : ")
                mylist.append(elem)
            print(mylist)
            myduplicates = check_duplicates(mylist)
            print("my duplicates : ",myduplicates)
        else:
            break
