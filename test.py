import re


# line = '''Renault Logan, 2015 г.в., в605ен178
#         Ford Fusion, 2017 г.в., а 301 рр 198
#         Volkswagen Polo, 2013 г.в., у617оо-147
#         Lada Granta, 2011 г.в., с313ур 98
#         Иж-21251, 1991 г.в., д 2139 ЛГ'''

# line2 = 'IP address to find: 127.0.0.1 or 192.168.0.1 or 10.77.70.11 but not 111.612.257.002'

# line3 = 'Римские числа: XVII, XLXI, XII, CXVI'

# line4 = 'RGB colors: #1AFFa1, #171c3a, #72CAD5, #ABC'

# result_lp = re.findall(r"\w ?\d{3,4} ?\w{2}[ -]?(?:\d{2,3})?", line)
# result_ip0 = re.findall(r"\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}", line2)
# result_ip = re.findall(r"(?:^|\b(?<!\.))(?:1?\d\d?|2[0-4]\d|25[0-5])(?:\.(?:1?\d\d?|2[0-4]\d|25[0-5])){3}(?=$|[^\w.])", line2)
# result_roman = re.findall(r"\b[IVXLCM]+", line3)
# result_rgb = re.findall(r"#(?:[0-9a-fA-F]{3}){1,2}", line4)
# print(result_rgb)


text = "Hello world, hello Python!"

# Cách dùng \b ở đầu cuối 
pattern = r"\bh" # Chỉ tìm các từ có chữ h ở đầu
        # r"o\b" # Chỉ tìm các từ có chữ o ở cuối
result = re.findall(pattern, text)
print(result)


text1 = "Hello,   world!\nThis is a test."

# Tìm tất cả các khoảng trắng trong văn bản

pattern = r"\s+"                        # r"\s+" là biểu thức chính quy sẽ khớp với một hoặc nhiều ký tự khoảng trắng liên tiếp.
result1 = re.findall(pattern, text1)
print("Kết quả với \\s+:", result1)

# \s
# Dấu cách
# Dấu tab (\t)
# Dấu xuống dòng (\n)
# Dấu trở về đầu dòng (\r)
# Các ký tự khoảng trắng khác