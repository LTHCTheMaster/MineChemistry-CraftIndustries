from .core import PeriodicTableBuilder, elements

class Run:
    def __init__(self):
        self.period = PeriodicTableBuilder(elements)

    def run(self, cmd: list[str]):
        if cmd[0] == "build":
            if cmd[1] == "elements":
                elements.saveElements(cmd[2])
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
                for i in elements.elements:
                    if cmd[2] == i.name.lower():
                        i.image.show()
                        return
            return
        if cmd[0] == "reload":
            self.reload()
            return
    
    def reload(self):
        elements.reloadElements()
        self.period = PeriodicTableBuilder(elements)
