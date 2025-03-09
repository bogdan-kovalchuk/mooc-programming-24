# Hello Visual Studio Code
while True:
    editor = input("Editor:").lower()
    if editor in ["word", "notepad"]:
        print("awful")
    elif editor == "visual studio code":
        print("an excellent choice!")
        break
    else:
        print("not good")
