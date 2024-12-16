# Prac 14.12.24
# Regular Expression 


import re
import timeit

# res = re.search("meow", "eemeowmeowfrfrfrmeow")
# print(res)
# print(dir(res))
# print(res.end())
# print(res.group())
# print(res.string)

# res = re.search("Meow", "eemeowmeowfrfrfrmeow")
# print(res)

# res = re.findall("meow", "eemeowmeowfrfrfrmeow")
# print(res)


# res = re.match("meow", "ewewemeowmeowfrfrfrmeow") # только в начале строки
# print(res)

# res = re.fullmatch("meow","meow")
# print(res)

# res = re.finditer("meow", "eemeowmeowfrfrfrmeow")
# print(next(res), next(res), next(res))


# res = re.escape("https://www.python.org")
# print(res)

# res = re.escape("meow\\n")
# print(res)

# res = re.search("meow\\n", "meow\\nlalal")
# print(res)

# res = re.search("meow\n", "meow\\nlalal")
# print(res)

# res = re.search("meow\\\n", "meow\\nlalal")
# print(res)

# res = re.search(r"meow\\n", "meow\\nlalal")
# print(res)

# res = re.search(re.escape("meow\\n"), "meow\\nlalal")
# print(res)

# res = re.split("meow", "eemeowqqqmeowfrfrfrmeowqqq")
# print(res)

# res = re.sub("meow", "bark", "eemeowqqqmeowfrfrfrmeowqqq")
# print(res)

# res = re.subn("meow", "bark", "eemeowqqqmeowfrfrfrmeowqqq")
# print(res)

# mask = re.compile("[eq]{2}m")

# res = timeit.timeit(
#     "re.findall('([eq]{2})m', 'eemeowqqqmeowfrfrfrmeowqqq')",
#     globals=globals(),
#     number=1000000
# )
# print(res)

# res = timeit.timeit(
#     "mask.findall('eemeowqqqmeowfrfrfrmeowqqq')",
#     globals=globals(),
#     number=1000000
# )
# print(res)


# метасимволы диапазона

# res = re.findall(r"M.ow", "eeMeowqqqMeowfrfrfrMeowqqqMiow")
# print(res)

# res = re.findall(r"M[a-c]ow", "eeMeowqqqMeowfrfrfrMeowqqqMiow")
# print(res)

# res = re.findall(r"M[aA-zZ1-3]ow[qfr]", "eeM2owqqqMeowfrfrfrMeowqqqMiow")
# print(res)

# [a-zA-Z0-9_] == \w
# res = re.findall(r"2\w", "d2sf2dfs2 fgfdg5")
# print(res)

# [^a-zA-Z0-9_] == \W
# res = re.findall(r"\W", "dsfdfs2 fgfdg5 ")
# print(res)

# res = re.findall(r"g\d", "meow5g5meow ")
# print(res)

# инверсия
# res = re.findall(r"g\D", "meow5g5gmeow ")
# print(res)

# [ \t\n\r\f\v] == \s
# res = re.findall(r"o\s[^wg]", "meo 5 g5gmeow ")
# print(res)

# граница слова
# res = re.findall(r"\b\w+", "meo 5 g5gmeow ")
# print(res)

# Повторители

# res = re.findall(r"m*eo", "meommeoweowow")
# print(res)

# res = re.findall(r"m+eow", "meow mmeow eow bow")
# print(res)

# res = re.findall(r"m?eo", "meow mmeow eow bow")
# print(res)

# res = re.findall(r"m{2,5}eo", "meow mmeow eow bow")
# print(res)

# res = re.findall(r"[eb]{1,5}ow", "meow mmeow eow bow")
# print(res)

# чередование

# res = re.findall(r"eow|Meow|Deow", "Meow Weow Deow")
# print(res)

# группы -- круглые скобки

# Non-Captured group Они создают подшаблон, который
#  функционирует как единое целое, но не сохраняет 
# совпадающую последовательность символов
# res = re.findall(r"(?:la)+", "lalalalllla")
# print(res)

# res = re.findall(r"((M|D|W)eow)", "Meow Weow Deow")
# print(res)

# res = re.findall(r"name:([aA-zZ]{3,})Age", "name:MashaAge:5")
# print(res)

# Позиционные (положение внутри строки)
# res = re.findall(r"^M\w*\s",  "Meow Weow Deow Mama ")
# print(res)

# res = re.findall(r"M\w*\s$",  "Meow Weow Deow Mama ")
# print(res)


# флаги
# mask = re.compile("cat", re.I)  # ignore case
# res = mask.findall("Cat")
# print(res)

# mask = re.compile(
#     r"""name:           # prefix
#         ([aA-zZ]{3,})   # main part
#         Age             # postfix""", 
#     re.X  # verbose
# )
# res = mask.findall("name:MashaAge:5")
# print(res)

# # Индексация группы
# res = re.sub(r"(\w+).(\w+)",   r"\2-\1 \1", "lala.haha")
# print(res)



# ^: Khi nằm trong [], sẽ mang nghĩa phủ định
# \s: Khớp với bất kỳ ký tự khoảng trắng nào.
# [^\s] sẽ khớp với bất kỳ ký tự nào không phải là khoảng trắng.





mail = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tmp)
    # . thì cần ký tự thoát còn @ thì không

# Các ký tự đặc biệt cần thoát:
    # . (dấu chấm) khớp với bất kỳ ký tự nào ngoại trừ dấu xuống dòng
    # ^ (dấu mũ) biểu thị bắt đầu của dòng
    # $ (dấu đô la) biểu thị kết thúc của dòng
    # * (dấu sao) khớp với 0 hoặc nhiều lần ký tự trước nó
    # + (dấu cộng) khớp với 1 hoặc nhiều lần ký tự trước nó
    # ? (dấu hỏi) khớp với 0 hoặc 1 lần ký tự trước nó
    # [] (ngoặc vuông) biểu thị một nhóm ký tự
    # {} (ngoặc nhọn) biểu thị số lượng chính xác
    # () (ngoặc tròn) tạo nhóm và bắt các nhóm con
    # \ (dấu gạch chéo ngược) được sử dụng để thoát các ký tự đặc biệt



# tôi chỉ ghi . chứ không \. thì có sai không
# Có, nếu bạn chỉ ghi dấu chấm . mà không thoát nó (\.) trong biểu thức chính quy, điều này sẽ tạo ra sự khác biệt lớn. 
# Trong biểu thức chính quy, dấu chấm . là một ký tự đặc biệt đại diện cho bất kỳ ký tự nào trừ dấu xuống dòng (\n). 
# Khi bạn muốn khớp với ký tự chấm thực sự, bạn cần sử dụng ký tự thoát \..


# Ghi dấu chấm không thoát
# Điều này sẽ khớp với bất kỳ chuỗi nào có dạng "example" theo sau là bất kỳ ký tự nào và sau đó là "com".
pattern_unescaped = r"example.com"
result_unescaped = re.findall(pattern_unescaped, tmp)
print("Kết quả với dấu chấm không thoát:", result_unescaped)

# Thoát dấu chấm
# Điều này sẽ chỉ khớp với chuỗi chính xác "example.com".
pattern_escaped = r"example\.com"
result_escaped = re.findall(pattern_escaped, tmp)
print("Kết quả với dấu chấm thoát:", result_escaped)

# Minh họa cụ thể
text = '''
Visit example.com for more info.
Check exampleXcom for alternatives.
'''

# Kết quả với dấu chấm không thoát
# Điều này xảy ra vì dấu chấm . trong biểu thức chính quy khớp với bất kỳ ký tự nào.
pattern_unescaped = r"example.com"
result_unescaped = re.findall(pattern_unescaped, text)
print("Kết quả với dấu chấm không thoát:", result_unescaped)  # ['example.com', 'exampleXcom']

# Kết quả với dấu chấm thoát
# Điều này xảy ra vì dấu chấm \. trong biểu thức chính quy chỉ khớp với ký tự chấm thực sự.
pattern_escaped = r"example\.com"
result_escaped = re.findall(pattern_escaped, text)
print("Kết quả với dấu chấm thoát:", result_escaped)  # ['example.com']






