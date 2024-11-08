from GameFrame import RoomObject, Globals
from Objects.Punch import Punch2
import pygame


class Character2(RoomObject):
    """
    A class for the player's avitar (the character2)
    """
    
    def __init__(self, room, x, y):
        """
        Initialise the character2 object
        """
        RoomObject.__init__(self, room, x, y)
        
        # set image
        self.moving = self.load_image("Character_stants_left.png")
        self.Punch = self.load_image("Character_punch_left.png")
        self.set_image(self.moving,100,100)

        # register events
        self.handle_key_events = True

        self.can_shoot = True

        
    def key_pressed(self, key):
        """
        Respond to keypress up and down
        """
        
        if key[pygame.K_LEFT]:
            self.x -= 10
        elif key[pygame.K_RIGHT]:
            self.x += 10
        
        if key[pygame.K_SPACE]:
            self.set_image(self.Punch,100,100)
        else:
            self.set_image(self.moving,100,100)
        if key[pygame.K_SPACE]:
            self.shoot_Punch2()

        
    def keep_in_room(self):
        """
        Keeps the ship inside the room
        """
        if self.x < 0:
            self.x = 0
        elif self.x + self.height> Globals.SCREEN_HEIGHT:
            self.x = Globals.SCREEN_HEIGHT - self.height

    def step(Character1):
        """
        Determine what happens to the Ship on each click of the game clock
        """

    def handle_collision(self, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Character1":
            self.room.running = False

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

    def shoot_Punch2(self):
        """
        Shoots a laser from the Character
        """
        if self.can_shoot:
            new_Punch2 = Punch2(self.room, 
                            self.x - self.width, 
                            self.y + self.height/4 - 8)
            self.room.add_room_object(new_Punch2)
            self.can_shoot = False
            self.set_timer(10,self.reset_shot)
            
    def reset_shot(self):
        """
        Allows ship to shoot again
        """
        self.can_shoot = True