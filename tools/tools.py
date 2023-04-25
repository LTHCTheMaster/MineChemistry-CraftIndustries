from images import Run as RunIMG
from images.core import elements

def work():
    img = RunIMG()
    while True:
        try:
            cmd = input(" :\t").split(" ")
            match cmd[0]:
                case "quit" | "exit" | "stop":
                    break
                case "image":
                    img.run(cmd[1:])
                case "export":
                    elements.exportList(cmd[1])
                case _:
                    pass
        except:
            pass
    return

if __name__ == '__main__':
    work()
