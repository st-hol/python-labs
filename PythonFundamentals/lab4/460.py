"""
***********************************************************
***             Лабораторна робота №4                  ***
***          з курсу "Основи програмування              ***
***              на скриптових мовах"                   ***
***                   Варіант №7                       ***
***     Виконав:студент Головачук С.В.   Група ТІ-72    ***
***********************************************************
"""
def toDec(string):
    return int(string)
def HexToDec (string):
    """
        :param string:str

        :return: integer

        :Tests:
        >>> HexToDec('1C3B3')==int("1C3B3",16)
        True
        >>> HexToDec('A')==int("A",16)
        True
        """
    answer = 0
    hex = "0123456789ABCDEF" # len=16
    for ind,item in enumerate(string) :
        value= hex.index(item) # 0 to 15
        #index = string.index(i)
        power = (len(string)-(ind+1)) #power of 16
        answer += (value*16**power)
    return answer
#
# print('Example, using Python\'s function int("hex-number", 16): ', int("1C3B3",16))
# print('Executed answer: ', HexToDec('1C3B3'))


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

# >>> HexToDec('BACFE')==int("BACFE",16) #actually it's mistake, but i did it specially for test.
# True











# Отделяем от числа все цифры и умножаем каждую из них на 16
# После того, как мы сделали этот шаг, нам необходимо пронумеровать разряды чисел.
# Делается это просто – мы приписываем ко всем числам 16, на которые мы умножали наши исходные цифры, степени, начиная с наибольшей и до 0
# Теперь нам остаётся только перемножить и сложить всё это








# def hex(s):
#     _hexer = "0123456789ABCDEF"
#     return sum([_hexer.find(var) * 16 ** i for i, var in enumerate(reversed(s.upper()))])




# def todec(n):
#    n = str(n)
#    if not n: return 0
#    if n[0] not in '01': raise ValueError
#    return (2 ** (len(n)-1)) * (n[0] == '1') + todec(n[1:])
#
# def horner(n):
#     n = str(n)
#     if not n: return 0
#     if n[-1] not in '01': raise ValueError
#     return horner(n[:-1]) * 2 + (n[-1]=='1')

















# function
# TruncStrReal(str: string):longint;
# var
# res: longint;
# i: integer;
# begin
# res: = 0;
# i: = 1;
# while (str[i] <> '.') and (i <= length(str)) do begin
# res: = res * 10 + (ord(str[i]) - ord('0'));
# inc(i);
# end;
# TruncStrReal: = res;
# end;
#
# var
# strInt: string;
# i: integer;
# flag: boolean;
# begin
# ClrScr;
# readln(strInt);
# flag: = false;
# for i: =
#     1
# to
# length(strInt)
# do
# if not (strInt[i] in ['0'..'9', '.']) then begin
# writeln('There is no number.');
# flag: = true;
# break;
# end;
# if not flag then
# writeln('Integer: ', TruncStrReal(strInt));
#
# readkey;
# end.