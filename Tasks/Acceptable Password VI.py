# Taken from mission Acceptable Password

def is_acceptable_password(password):

    test_list = [x for x in list(password)] # через временный список удяляем повторояющиеся элементы
    temp = []
    for i in test_list:
        if i not in temp:
            temp.append(i)
    if len(temp) <= 2:
        return False 
#___________________________________________
    check_word = 'password' # какое слово нельзя использовать
    if check_word in password.lower():
        return False

    elif password.isdigit() == True and len(password) <= 9: #can't be just digits but if more 9 char -> True
        return False
    
    elif len(password) > 9:
        return True

    elif len(password) > 6: #can be >6 char
        for x in password:
            if x.isdigit() == True: #min 1 char is digit
                return True
        else:
            return False
    else:
        return False


passw = 'aacaaaabbaaa'

print(is_acceptable_password(passw))

    
        
