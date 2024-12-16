import re
import csv
import json


BLUE = "\033[94m"
END = "\033[0m"


# Task 1
def taskFirst():
    with open("task1-en.txt", 'r', encoding ="utf-8" ) as file1:
        tmp1 = file1.read()
        res_1 = re.findall(r"\b[A-Z][a-z]*\b", tmp1)
        res_2 = re.findall(r"\b\w+(?=:)", tmp1)

        print(BLUE + "All words starting with capital letter: " + END + str(res_1))
        print(BLUE + "All words followed by a colon: " + END + str(res_2))


# Task 2
def taskSecond():
    with open("task2.html", 'r', encoding="utf-8") as file2:
        tmp2 = file2.read()
        # HTML opening tags have the format </tag>, for example </div>, </p>, etc.
        tag_open = re.findall(r"</\s*([a-zA-Z0-9]+)(\s*[^>]*)?>", tmp2)

        # HTML closing tags have the format </tag>, for example </div>, </p>, etc.
        tag_close = re.findall(r"</\s*([a-zA-Z0-9]+)\s*>", tmp2)
        res = set(tag_close)
        print(BLUE + "All unique closing tags: " + END + str(res))


# Task 3
def taskThird():
    with open("task3.txt", 'r', encoding="utf-8") as file3:
        tmp3 = file3.read()

        id = re.findall(r"\b\d+\b", tmp3)
        surname = re.findall(r"[a-zA-Z]+", tmp3)

        date = re.findall(r"\b\d{4}-\d{2}-\d{2}\b", tmp3)
        mail = re.findall(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}", tmp3)

        # [^\s] khớp với bất kỳ ký tự nào không phải khoảng trắng.
        website = re.findall(r"https?://[^\s]+", tmp3)
    
    n = min(len(id), len(surname), len(mail), len(date), len(website))
    id_lst = []
    for i in range(1,len(id) + 1):
        id_lst.append(i) 

    res_table = []
    for i in range(n):
        res_table.append((id_lst[i], surname[i], mail[i], date[i], website[i]))

    with open("result.csv", 'w', encoding="utf-8") as file_csv:
        file = csv.writer(file_csv)
        file.writerow(("ID", "Surname", "Mail", "Registration Date", "Website"))
        file.writerows(res_table)

    print(BLUE + "Saved data in result.csv" + END)

    # with open("new.json", 'w', encoding="utf-8") as file_json:
    #     json.dump(res_table, file_json, indent=4)


def taskExtra():
    print(BLUE + "Extra Task" + END)
    with open("task_add.txt", 'r', encoding="utf-8") as file4:
        tmp4 = file4.read()

        dates = re.findall(r"(\d{4}[-/.]\d{2}[-/.]\d{2})|(\d{2}[-/.]\d{2}[-/.]\d{4})", tmp4)
        # dates = re.findall (r"\b(\d{2,4}[./-]\d{2,4}[./-]\d{2,4})", tmp4)
        date = [x[0] if x[0] else x[1] for x in dates]
        print("Found 5 dates: ",date)

        mail = re.findall(r"\b[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}\b", tmp4)
        # mail = re.findall(r"\s([\w.%+-]+@[\w.-]+\.[a-zA-Z]{2,})", tmp4)
        print("Found 5 mails: ", mail)
        
        sites = re.findall(r"\bhttps?://[^\s]+\b", tmp4)
        print("Found 5 sites: ", sites)


if __name__ == '__main__':

    taskFirst()
    taskSecond()
    taskThird()
    taskExtra()