def sum_numbers(text: str) -> int:
     arr = ""
     res = 0
     count = 0
     arr_list = []
     text = text.replace("'", "")
     if any(text) != 0:
        arr_list = text.split(' ')
        while count < len(arr_list):
            try:
                arr_list[count] = int(arr_list[count])
                count+=1
            except ValueError:
                arr_list.remove(arr_list[count])
     if any(arr_list) != 0:
          i = 0
          while i < len(arr_list):
             res+= int(arr_list[i])
             i+=1
     return res

if __name__ == '__main__':
    print("Example:")
    print(sum_numbers('hi'))

   #  These "asserts" are used for self-checking and not for an auto-testing
    assert sum_numbers('hi') == 0
    assert sum_numbers('who is 1st here') == 0
    assert sum_numbers('my numbers is 2') == 2
    assert sum_numbers('This picture is an oil on canvas '
 'painting by Danish artist Anna '
 'Petersen between 1845 and 1910 year') == 3755
    assert sum_numbers('5 plus 6 is') == 11
    assert sum_numbers('') == 0
    print("Coding complete? Click 'Check' to earn cool rewards!")w your tests and earn cool rewards!")Check' to earn cool rewards!")