
class speedSwitcher():
    def __init__(self) -> None:
        self.curSpeed = 100
        self.speed_settings = (1,5,10,25,50,100,250,500)
    
    def increase(self):
        if self.curSpeed != self.speed_settings[0]:
            self.curSpeed = self.speed_settings[self.speed_settings.index(self.curSpeed) - 1]
            return True
        else:
            return False
    def decrease(self):
        if self.curSpeed != self.speed_settings[-1]:
            self.curSpeed = self.speed_settings[self.speed_settings.index(self.curSpeed) + 1]
            return True
        else:
            return False

class sizeSwitcher():
    def __init__(self) -> None:
        self.curSize = 50
        self.size_settings = (15,25,50,100,150)
    def increase(self):
        if self.curSize != self.size_settings[-1]:
            self.curSize = self.size_settings[self.size_settings.index(self.curSize) + 1]
            return True
        else:
            return False
    def decrease(self):
        if self.curSize != self.size_settings[0]:
            self.curSize = self.size_settings[self.size_settings.index(self.curSize) - 1]
            return True
        else:
            return False
