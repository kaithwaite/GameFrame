from GameFrame import RoomObject, Globals
from Objects.Punch import Punch
import pygame 

class Character1(RoomObject):
    """
    A class for the player's avitar (the character)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the character object
        """
        self.state = "stants"
        self.state = "punch"
        
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.moving = self.load_image("Character_stants_right.png")
        self.punch = self.load_image("Character_punch_right.png")
        self.set_image(self.moving,100,100)


        # register events
        self.handle_key_events = True
        
        self.can_shoot = True
        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_a]:
            self.x -= 10
        elif key[pygame.K_d]:
            self.x += 10
        
        if key[pygame.K_f]:
            self.set_image(self.punch,100,100)
        else:
            self.set_image(self.moving,100,100)
        if key[pygame.K_f]:
            self.shoot_Punch()
    
        

            
        # register events
        self.register_collision_object("Character_2")
        
    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.x < 0:
            self.x = 0
        elif self.x + self.height> Globals.SCREEN_HEIGHT:
            self.x = Globals.SCREEN_HEIGHT - self.height

    def step(self):
        self.keep_in_room()
        """
        Determine what happens to the Ship on each click of the game clock
        """

    def shoot_Punch(self):
        """
        Shoots a laser from the Character
        """
        if self.can_shoot:
            new_Punch = Punch(self.room, 
                            self.x + self.width, 
                            self.y + self.height/4 - 8)
            self.room.add_room_object(new_Punch)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True