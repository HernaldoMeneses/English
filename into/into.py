

text_all = []

def groop_to (read_Eng, read_Port):
    read_Eng = read_Eng
    read_Port = read_Port
    read_Key = {read_Eng:read_Port}
    text_all.append(read_Key)

read_Eng = "DearESL/EFL Collegues, I once met a teacher who had recently used one of my texts in her class."
read_Port = ""
groop_to (read_Eng, read_Port)


read_Eng = "At the end of the rem, one of her students said to her."
read_Port = ""
groop_to (read_Eng, read_Port)

read_Eng = "'Thank you for teaching me the secrets of English.'"
read_Port = ""
groop_to (read_Eng, read_Port)

read_Eng = "I still smile when I think of that comment."
read_Port = ""
groop_to (read_Eng, read_Port)

read_Eng = ""
read_Port = ""
groop_to (read_Eng, read_Port)



for item in text_all:
    for eng, port in item.items():
        print(f'English: {eng}')
        print(f'Portuguese: {port}\n')