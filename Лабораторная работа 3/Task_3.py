# TODO  Напишите функцию count_letters
#зададим функцию принимающую на вход отрывок стихотворения
def count_letters(passage):
    #приведем буквы к одному нижнему регистру по условию
    lowercase_text = passage.lower()

    letter_count = {}
    for character in lowercase_text:
        #проверка соответствия символа букве
        if character.isalpha():
            if character in letter_count:
                letter_count[character] = letter_count[character] + 1
            else:
                letter_count[character] = 1
    return letter_count



# TODO Напишите функцию calculate_frequency
#зададим функцию вычисления частоты
def calculate_frequency(letter_count):
    sum_of_letters = sum(letter_count.values())

    letter_frequency = {}
    for current_letter, count in letter_count.items():
        #отношение кол-ва повторений одной буквы на сумму всех букв
        letter_frequency[current_letter] = count / sum_of_letters

    return letter_frequency

main_str = """
У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо — песнь заводит,
Налево — сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух… там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил.
"""
count_data = count_letters(main_str)
frequency_data = calculate_frequency(count_data)


# TODO Распечатайте в столбик букву и её частоту в тексте
for letter, frequency in frequency_data.items():
    # вывод буквы с ее частотой, округленной до 2х знаков после запятой
    print(letter, round(frequency, 2))

