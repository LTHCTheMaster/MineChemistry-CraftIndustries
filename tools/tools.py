from images import Run as RunIMG
from images.core import elements

def work():
    img = RunIMG()
    while True:
        try:
            cmd = input(" :\t").split(" ")
            if cmd[0] in ("quit", "exit", "stop"):
                break
            elif cmd[0] == "image":
                img.run(cmd[1:])
            elif cmd[0] == "export":
                elements.exportList(cmd[1])
        except:
            pass
    return

if __name__ == '__main__':
    work()
