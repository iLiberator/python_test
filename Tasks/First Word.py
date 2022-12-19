def first_word(text):
    #function returns the first word in a given text.
    list_no = ['.', ' ', ',', '...']
    list = text.split()
    end = ''
    for x in list:
        if x in list_no or x.isdigit() == True:
            continue
        else:
            for i in x:
                if i == '.':
                    #index = x.find(',')
                    #end = end + x[0:index]
                    end = (end + x.replace('.', ' ')).split()[0]
                    return end
                elif i == ',':
                    end = (end + x.replace(',', ' ')).split()[0]
                    return end
            else:
                return x

test = 'greetings, friends'

print(first_word(test))


#assert first_word("Hello world") == "Hello"
#assert first_word(" a word ") == "a"
#assert first_word("don't touch it") == "don't"
#assert first_word("greetings, friends") == "greetings"
#assert first_word("... and so on ...") == "and"
#assert first_word("hi") == "hi"