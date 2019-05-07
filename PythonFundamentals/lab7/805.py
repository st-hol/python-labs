

# string = "fdasaAAAdsfSffas"
# string1 = "fdasafffas"
# string2 = "Affsa"


def search_small_groups(string):
    """
          :Tests:
          >>> search_small_groups("fdasaAAAdsfSffas")=="fdasa..........."
          True
          >>> search_small_groups("fdasafffas")=="fdasafffas"
          True
          >>> search_small_groups("Affsa")=="....."
          True
       """
    i=0
    lowercase = string.islower()
    while i < len(string):
        if lowercase:
            return string
            # i += 1
            # continue

        elif string[i].isupper():
            app = ['.' for i in range(len(string)-i)]
            string = string[:i] + ''.join(app)
            break
        i += 1
    return string


#
# print(string)
# print(search_small_groups(string))
#
# print(string1)
# print(search_small_groups(string1))
#
# print(string2)
# print(search_small_groups(string2))
#


if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)














import re
# if (re.match("^[a-z-]*$", string)):
#     print(string)
# else:
#     pass


# string = string.replace(string[i], '.')
# string = string[:i] + '.' + string[i + 1:]