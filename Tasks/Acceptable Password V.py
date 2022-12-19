# Taken from mission Acceptable Password

def is_acceptable_password(password):

    check_word = 'password'

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


passw = '123pAswordasdasd'

print(is_acceptable_password(passw))

