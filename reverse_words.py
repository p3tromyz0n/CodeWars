def task():
    '''
    Complete the function that accepts a string parameter,
    and reverses each word in the string. All spaces in the string should be retained.

    "This is an example!" ==> "sihT si na !elpmaxe"
    "double  spaces"      ==> "elbuod  secaps"
    '''


def reverse_words(text):

    new_text = []
    f = text.split(" ")
    for i in f:
        new_text.append(i[::-1])
    s = " ".join(new_text)
    return s


def reverse_words_short(text):
    return " ".join(i[::-1] for i in text.split(" "))


