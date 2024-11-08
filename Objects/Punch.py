from GameFrame import RoomObject, Globals


class Punch(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Character_punch_right_hitbox.png")
        self.set_image(image, 50, 50)
        
        # register events
        self.register_collision_object("Character_2")

    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

         # register events
        self.register_collision_object("Character2")

    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        
        if other_type == "Character2":
            self.room.running = False

class Punch2(RoomObject):
    """
    Class for the lasers shot by the Ship
    """
    
    def __init__(self, room, x, y):
        """
        Inistialise the laser
        """
        # include attributes and methods from RoomObject
        RoomObject.__init__(self, room, x, y)
        
        # set image
        image = self.load_image("Character_punch_left_hitbox.png")
        self.set_image(image, 50, 50)

        # register events
        self.register_collision_object("Character_1")

        
    def step(self):
        """
        Determine what happens to the laser on each tick of the game clock
        """
        self.outside_of_room()
        
    def outside_of_room(self):
        """
        removes laser if it has exited the room
        """
        if self.x > Globals.SCREEN_WIDTH:
            self.room.delete_object(self)

         # register events
        self.register_collision_object("Character1")
    
    def handle_collision(self, other, other_type):
        """
        Handles the collision events for the Asteroid
        """
        if other_type == "Character1":
            self.room.running = False
       