"""

Домашнее задание №2

Работа с файлами


* Скачайте файл по ссылке https://www.dropbox.com/s/sipsmqpw1gwzd37/referat.txt?dl=0
* Прочитайте содержимое файла в перменную, подсчитайте длинну получившейся строки
* Подсчитайте количество слов в тексте
* Замените точки в тексте на восклицательные знаки
* Сохраните результат в файл referat2.txt
"""

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    with open('referat.txt', 'r', encoding="utf-8")as myfile:
        content = myfile.read()
     #   print(content)
        dlina_stroki = len(content)
        print(dlina_stroki)
        kol_vo_slov = len(content.split())
        print(kol_vo_slov)

        content2 = content.replace('.', '!')
        print(content2)

    with open('referat2.txt', 'w', encoding="utf-8")as newfile:
        newfile.write(content2)


if __name__ == "__main__":
    main()
