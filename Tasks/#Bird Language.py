#Bird Language

'''
У Стефана есть друг -- маленькая робо-птичка. Какое-то время он пытался научить её говорить по-английски. И вот сегодня она произнесла первое слово:
«hieeelalaooo». Звучит как «hello», но слишком уж много гласных. Стефан попросил Николу помочь с этим, и тот изучил, как птица меняет слова. 
Теперь нам осталось только написать модуль для перевода с птичьего.

Птичка меняет слова по следующим правилам:
- после каждой согласной буквы она добавляет случайную гласную букву (l ⇒ la or le);
- после каждой гласной буквы она добавляет две таких же буквы (a ⇒ aaa);
Гласные буквы == "aeiouy".

Вам дана птичья фраза как несколько слов, разделёных пробелами (каждая пара слов разделена одним пробелом). 
Птичка не знает ничего о знаках пунктуации и использует только буквы. Все слова даны в нижнем регистре. 
Необходимо перевести эту птичью песню в понятную простым роботам фразу.

Входные данные: Птичья фраза как строка (string).

Выходные данные: Перевод как строка (string).
'''
text = 'aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa'

def translate(text: str) -> str:
    #согласные
    CONSONANT = [
        'b', 'c', 'd', 'f', 'h', 
        'g', 'j', 'k', 'l', 'm', 
        'n', 'p', 'q', 'r', 's', 't', 
        'v', 'w', 'x', 'z'
        ]
    #гласные
    VOWEL = ['a', 'e', 'i', 'o', 'u', 'y']
    test1 = ''
    ind = 0
    while ind < len(text):
        if text[ind] == ' ':
            test1 += ' '
            ind += 1
        else:
            if text[ind] in CONSONANT:
                test1 += text[ind]
                ind += 2
            else:
                test1 += text[ind]
                ind += 3
    return test1


print(translate(text))

#assert translate("hieeelalaoo") == "hello"
#assert translate("hoooowe yyyooouuu duoooiiine") == "how you doin"
#assert translate("aaa bo cy da eee fe") == "a b c d e f"
#assert translate("sooooso aaaaaaaaa") == "sos aaa"

#'aaabucidyeeefigihoiiijukulemonoooopyqorysotauuuviwuxayyyzu ziyyyxuwivouuutesiriqopaooonimelykijaiiihigefaeeedacybuaaa'