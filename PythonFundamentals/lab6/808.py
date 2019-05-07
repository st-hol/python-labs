"""
***********************************************************
***             Лабораторна робота №6                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
Text = str(input("Введіть текст для обробки:"))
words = Text.split()
L = len(words)

q = [ words.count(item) for item in words]
[print('а) Слово ',words[i],' зустрічається ',q[i],'раз') for i in range(L)]
print("\n")

def calc_quantity(words, searched_letters):
    """
        Calculates quantity of defined letters in word.
               :param words:list of words, searched_letters:list of defined letters
               :return: countable_list: list of entires searched letters in every word
               :Tests:
               >>> calc_quantity(['aeiouAEIOU'],vowels)[0]==10
               True
    """
    countable_list=[]
    for word in words:
        countable_list.append(sum(x in searched_letters for x in word))
    return countable_list

vowels = list("aeiouAEIOU")
number_of_vowels=calc_quantity(words,vowels)
[print('б) В слові ', words[i],' голосних букв налічується ', number_of_vowels[i]) for i in range(L)]
print("\n")
a_b = list("abAB")
number_of_ab = calc_quantity(words,a_b)
[print('в) В слові ', words[i],' букв a,b налічується ', number_of_ab[i]) for i in range(L)]
print("\n")

import re
print('г) Текст, в словах якого закінчення слів на -ing замінено на -ed: ',re.sub(r'ing\b', 'ed', Text))

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=False)









#\b
#Matches the empty string, but only at the beginning or end of a word. A word is defined as a sequence of alphanumeric or underscore characters, so the end of a word is indicated by whitespace or a non-alphanumeric, non-underscore character. Note that formally, \b is defined as the boundary between a \w and a \W character (or vice versa), or between \w and the beginning/end of the string, so the precise set of characters deemed to be alphanumeric depends on the values of the UNICODE and LOCALE flags. For example, r'\bfoo\b' matches 'foo', 'foo.', '(foo)', 'bar foo baz' but not 'foobar' or 'foo3'. Inside a character range, \b represents the backspace character, for compatibility with Python’s string literals.