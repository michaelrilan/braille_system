from gingerit import GingerIt as gn

while True:
    text = input("Enter a sentence(press '0' to exit) >>: ")
    print("Inputted Text:" + text)
    if text == '0':
        print("goodbye")
        break
    else:
        corrected_text = gn().parse(text)
        print(corrected_text['result'])
    