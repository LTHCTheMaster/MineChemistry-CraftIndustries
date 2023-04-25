from images import Run as RunIMG

def work():
    img = RunIMG()
    while True:
        try:
            cmd = input(" :\t").split(" ")
            if cmd[0] in ("quit", "exit", "stop"):
                break
            elif cmd[0] == "image":
                img.run(cmd[1:])
        except:
            pass
    return

if __name__ == '__main__':
    work()
