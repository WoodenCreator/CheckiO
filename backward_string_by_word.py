def backward_string_by_word(text: str) -> str:
    str_new = ""
    i = 0
    g = 0
    tmp = 0
    while i < len(text):
        if text[i] == ' ' or i==len(text)-1:
           g = i
           if text[i] == ' ':
               g-=1
           while g >= tmp:
                str_new += text[g]
                g-=1
           if text[i]==' ':
                str_new+=' '
           tmp = i+1
        i+=1
    return str_new

if __name__ == '__main__':
    print("Example:")
    print(backward_string_by_word(''))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert backward_string_by_word('') == ''
    assert backward_string_by_word('world') == 'dlrow'
    assert backward_string_by_word('hello world') == 'olleh dlrow'
    assert backward_string_by_word('hello   world') == 'olleh   dlrow'
    assert backward_string_by_word('welcome to a game') == 'emoclew ot a emag'
    print("Coding complete? Click 'Check' to earn cool rewards!")
