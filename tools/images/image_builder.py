from .core import loadElements, saveElements, PeriodicTableBuilder

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
