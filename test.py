with open('myfile.txt', 'r', encoding="utf-8")as myfile:
    for line in myfile:
        line = line.upper()
        line = line.replace("\n", "")
        print(line)