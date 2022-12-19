# Taken from mission Acceptable Password I

def is_acceptable_password(password):
    if len(password) > 6:
        for x in password:
            if x.isdigit() == True:
                return True
        else:
            return False
    else:
        return False


passw = 'sh17ort'

print(is_acceptable_password(passw))