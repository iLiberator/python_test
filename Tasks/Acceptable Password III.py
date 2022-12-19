# Taken from mission Acceptable Password I

def is_acceptable_password(password):

    if password.isdigit() == True and len(password) <= 9: #can't be just digits
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


passw = '123sasdasd'

print(is_acceptable_password(passw))