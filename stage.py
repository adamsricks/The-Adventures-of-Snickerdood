from floor import Floor
from newEnemy import Enemy

class Stage():
    def __init__(self):
        self.platforms = []
        self.enemy = Enemy(100, 100, 400)
        self.startDoor = None
        self.endDoor = None
        
        self.name = ""
        self.nextStageName = ""


    def draw(self, screen):
        # for enemy in enemies:
        self.enemy.draw(screen)
        for platform in self.platforms:
            platform.draw(screen)
        if self.startDoor != None:
            self.startDoor.draw(screen)
        if self.endDoor != None:   
            self.endDoor.draw(screen)
    def run(self):
        x = 200
        y = 0
        self.enemy.append(self.enemy)
        for enemyies in enemy[:]:
            enemy.move(x, y)
        