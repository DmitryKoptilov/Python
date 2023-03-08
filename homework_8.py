s = input("Enter str.:")
ch = input("Enter symb.:")
index = 0
while index < len(s):
    if s.find(ch, index) == -1:
        break
    print(s.find(ch, index))
    index = s.find(ch, index) + 1
