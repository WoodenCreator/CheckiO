def left_join(phrases: tuple) -> str:
    str_res = ""
    left = ""
    count = 0

    for g in phrases:
        left+=g
        count +=1
        if count < len(phrases):
            left+=","

    count = 0
    length = 0
    while length<len(left):
        if left[length] == 'r' and left[length+1] == 'i' and left[length+2] == 'g' and left[length+3] == 'h' and left[length+4] == 't':
            str_res+="left"
            length+=5
        else:
            str_res+=left[length]
            length+=1
    return str_res


if __name__ == '__main__':
    print('Example:')
    print(left_join(("left", "right", "left", "stop")))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert left_join(("left", "right", "left", "stop")) == "left,left,left,stop", "All to left"
    assert left_join(("bright aright", "ok")) == "bleft aleft,ok", "Bright Left"
    assert left_join(("brightness wright",)) == "bleftness wleft", "One phrase"
    assert left_join(("enough", "jokes")) == "enough,jokes", "Nothing to replace"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")Check' to earn cool rewards!")