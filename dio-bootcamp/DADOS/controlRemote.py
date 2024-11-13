from abc import ABC, abstractmethod, abstractproperty


class ControlRemote(ABC):
    @abstractmethod
    def on(self):
        pass

    @abstractmethod
    def off(self):
        pass

    @property
    @abstractproperty
    def mark(self):
        pass

class ControlTV(ControlRemote):
    def off(self):
        print("off")
    def on(self):
        print("on")
    def mark(self):
        print("lg")

control = ControlTV()
control.on()
control.off()


class ControlAIR(ControlRemote):
    def off(self):
        print("off air")
    def on(self):
        print("on air")
    def mark(self):
        print("lg")

control = ControlAIR()
control.on()
control.off()

