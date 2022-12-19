# Taken from mission Acceptable Password I

def is_acceptable_password(password):
    if password.isdigit() == True:
        return False

    elif len(password) > 6:
        for x in password:
            if x.isdigit() == True:
                return True
        else:
            return False
    else:
        return False


passw = '1234s567'

print(is_acceptable_password(passw))