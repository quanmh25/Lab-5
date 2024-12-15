# Lab-5

Лабораторная работа №5

Работа с регулярными выражениями

**Задание 1.** Откройте файл ```task1_ru.txt``` или ```task1_en.txt```. Используя регулярные выражения, выполните задание для своего вариата из списка ниже:

Вариант 1. Все слова от 3 до 5 букв; все числа больше 3 знаков.  
Вариант 2. Все слова, начинающиеся с большой буквы; все слова, после которых стоит двоеточие.  
Вариант 3. Все слова, после которых стоит запятая; всю информацию в квадратных скобках.  
Вариант 4. Все слова, в которых есть дефис; всю информацию в круглых скобках.  
Вариант 5. Все числа, целые и дробные; все слова на 6 и на 8 букв.  
Вариант 6. Все целые числа меньше 10; все сочетания, в которых есть и буквы, и цифры.  
Вариант 7. Все слова, начинающиеся с буквы "с"; все слова, перед которыми стоит "и" или "the"  
Вариант 8. Все конструкции "рис. #" или "Fig. #"; все слова из 4 букв.  
Вариант 9. Все слова, заканчивающиеся на букву "e"; все числа в круглых скобках  
Вариант 10. Все слова, после которых стоит точка; все дробные числа.  

**Задание 2.** Откройте файл ```task2.html```. Используя регулярные выражения, выполните задание для своего вариата из списка ниже:

Вариант 1. Все открывающие теги без повторений.  
Вариант 2. Все закрывающие теги без повторений.  
Вариант 3. Все обозначения цветов.  
Вариант 4. Все ссылки в домене .com.  
Вариант 5. Все строки, находящиеся в атрибуте content любого тега.  
Вариант 6. Все ссылки на изображения.  
Вариант 7. Все названия используемых шрифтов.  
Вариант 8. Параметры используемых шрифтов: стиль, размер.  
Вариант 9. Все размеры изображений.  
Вариант 10. Все значения в пикселях.  

**Задание 3.** Откройте файл ```task3.txt```. Здесь содержится таблица, состоящая из 5 полей: ID, фамилия, электронная почта, дата регистрации и сайт. Вот только пользователи вносили эти данные в абсолютно своём порядке, вследствие чего все данные перепутаны. Приведите эту базу данных в нормальный вид, расположив данные в вышеуказанном порядке. Для этого при помощи регулярных выражений выделите из файла данные каждого вида, составьте из них таблицу и сохраните как файл формата ```csv```.

**Дополнительное задание**

Есть файл со случайными символами - ```task_add.txt```. Это бесполезные данные, белый шум, однако, в нём ещё можно найти что-то полезное. В этом файле скрыты 5 дат, 5 адресов электронной почты и 5 адресов сайтов. Каждый полезный элемент данных предваряется пробелом. Дата может быть в разных форматах и с разделителями вида ```- / .```. Найдите все 15 фрагментов данных в файле, используя регулярные выражения.

**Полезные ссылки**

Общая статья о регулярных выражениях: https://habr.com/ru/articles/349860/
Python docs: https://docs.python.org/3/library/re.html
