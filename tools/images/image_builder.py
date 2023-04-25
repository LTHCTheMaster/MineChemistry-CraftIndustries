from .core import loadElements, saveElements, PeriodicTableBuilder, elements

class Run:
    def __init__(self):
        loadElements()
        self.period = PeriodicTableBuilder()

    def run(self, cmd: list[str]):
        if cmd[0] == "build":
            if cmd[1] == "elements":
                saveElements(cmd[2])
                return
            if cmd[1] == "periodic":
                self.period.save(cmd[2])
                return
            return
        if cmd[0] == "show":
            if cmd[1] == "periodic":
                self.period.show()
                return
            if cmd[1] == "element":
                for i in elements:
                    if cmd[2] == i.name.lower():
                        i.image.show()
                        return
            return
        if cmd[0] == "reload":
            self.reload()
            return
    
    def reload(self):
        loadElements()
        self.period = PeriodicTableBuilder()
