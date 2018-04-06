#!/usr/bin/env python3

def decode(file_in, file_out):
    print("Input: '{}'; Output: '{}'".format(file_in, file_out))

    with open(file_in, "r", encoding='utf-8') as r, \
         open(file_out, "w") as w:
        for line in r: # it might be better to read by char
            for symbol in line:
                try:
                    new_symbol = symbol.encode('cp1252').decode('cp1251')

                    w.write(new_symbol)
                except UnicodeEncodeError:

                    pass # it's good
import pdfminer.high_level                       # Импортируем библиотеку распознавания PDF
text_from_pdf = open("C:\\lol.txt", "wb") # Создаём файл, в который запишем вытащенный из PDF текст.
with open('C:\\Belim1.pdf', 'rb') as file:# Открываем pdf файл для извлечения из него текста.
    pdfminer.high_level.extract_text_to_fp(file, text_from_pdf) # Применяем библиотеку для разбора pdf
print("Распознавание завершено")                 # Выводим в терминал сообщение, что процесс распознавания завершен.
text_from_pdf.close()                            # Закрываем файл, в который записали результат распознавания.

#with open("qwerty.txt", "r", encoding="utf8") as file:# Открываем файл, в который помещали распознанный текст.
  #  file = file.read()                           # Присваиваем переменной file весь текст открытого файла.
    #print(file)                                  # Выводим содержание переменной в терминал (в редакторе PyCham)
if __name__ == '__main__':
    decode('C:\\lol.txt','C:\\lol1.txt' )