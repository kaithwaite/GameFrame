from GameFrame import Globals, Level
from Objects.Character1 import Character1
from Objects.Character2 import Character2
from Objects.Score import Score


class GamePlay(Level):
    def __init__(self, screen, joysticks):
        Level.__init__(self, screen, joysticks)
        
        # set background image
        self.set_background_image("Fighting_background.png")

        # add objects
        self.add_room_object(Character1(self, 165, 600))
        self.add_room_object(Character2(self, 500, 600))
        
        # add HUD items
        self.score = Score(self, 
                           Globals.SCREEN_WIDTH/2 - 20, 20, 
                           str(Globals.SCORE))
        self.add_room_object(self.score)