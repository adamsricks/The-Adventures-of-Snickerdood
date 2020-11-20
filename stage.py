from floor import Floor

class Stage():
    def __init__(self):
        self.platforms = []

        self.startDoor = None
        self.endDoor = None

        self.name = ""
        self.nextStageName = ""


    def draw(self, screen):
        for platform in self.platforms:
            platform.draw(screen)
        if self.startDoor != None:
            self.startDoor.draw(screen)
        if self.endDoor != None:   
            self.endDoor.draw(screen)