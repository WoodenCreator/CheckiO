def between_markers(text: str, begin: str, end: str) -> str:
    str_res = ""
    count=0
    temp = 0
    count_begin = 0
    ok = 0
    end_sim = 0
    ok_= -1
    while count < len(text):
        #check for the begin string
        if text[count] == begin[count_begin] and ok == 0:
            if ok_ == -2:
                str_res = ""
                ok_ = -3
                break
            temp = count
            while count_begin < len(begin):
                if text[temp] == begin[count_begin]:
                    count_begin+=1
                    temp+=1
                else:
                    count_begin = 0
                    temp = 0
                    break
            if count_begin == len(begin):
                count+=count_begin
                ok = 1
                ok_ = 0
                count_begin = 0
            #check for the end string(after begin symbols)
        if text[count] == end[count_begin]:
            temp = count
            while count_begin < len(end):
                if text[temp] == end[count_begin]:
                    count_begin+=1
                    temp+=1
                else:
                    count_begin = 0
                    temp = 0
                    break
                if count_begin == len(end):
                    if ok_ == -1:
                        ok_= -2
                    count_begin = 0
                    temp = 0
        if text[count] == end[count_begin] and ok == 1:
            temp = count
            while count_begin < len(end):
                if text[temp] == end[count_begin]:
                    count_begin+=1
                    temp+=1
                else:
                    count_begin = 0
                    temp = 0
                    break
            if count_begin == len(end):
                count+=count_begin
                ok_ = 1
                count_begin = 0
        #write res string
        if ok == 1 and ok_ == 0:
            str_res+=text[count]
        count+=1



    if (ok_ == -2):
        str_res = ""
        count=0
        temp = 0
        count_begin = 0
        while count < len(text):
            if text[count] == end[count_begin]:
                temp = count
                while count_begin < len(end):
                    if text[temp] == end[count_begin]:
                        count_begin+=1
                        temp+=1
                    else:
                        count_begin = 0
                        temp = 0
                        break
            if count_begin == len(end):
                str_res+=text[:count]
                break
            count+=1



    if (ok_ == -1 and str_res == ""):
        str_res +=text


    return str_res





if __name__ == '__main__':
    print('Example:')
    print(between_markers('What is >apple<', '>', '<'))

    # These "asserts" are used for self-checking and not for testing
    assert between_markers('What is >apple<', '>', '<') == "apple", "One sym"
    assert between_markers("<head><title>My new site</title></head>",
                           "<title>", "</title>") == "My new site", "HTML"
    assert between_markers('No[/b] hi', '[b]', '[/b]') == 'No', 'No opened'
    assert between_markers('No [b]hi', '[b]', '[/b]') == 'hi', 'No close'
    assert between_markers('No hi', '[b]', '[/b]') == 'No hi', 'No markers at all'
    assert between_markers('No <hi>', '>', '<') == '', 'Wrong direction'
    print('Wow, you are doing pretty good. Time to check it!')