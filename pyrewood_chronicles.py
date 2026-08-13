# Nathan Bragg
# Project 2 - IT-140
# 9/10/21

# Import the randint and choice methods from the random module, and sleep from the time module
from random import randint, choice
from time import sleep

# Initialize some global variables to be used in functions later.
blood = False
item_list = ['sword', 'shield', 'armor', 'knives', 'oil', 'torch']
room_count = 0


def instructions():
    """
    This function will print the following paragraph which will lay out the objective of this adventure, along with
    the means by which to win.  It also details the actions the player can take during their adventure in terms of
    interacting with items and companions in the game, as well as how to see this info, and how to exit the game
    """
    print('The Pyrewood Chronicles - A Text Adventure')
    print('Find and defeat the bandits to avenge the fallen Marquess.')
    print('Do this by collecting the 6 necessary items, or recruiting 3 companions, or defeat them in combat.')
    print('Move commands: north, east, south, west, up, down')
    print('Add to Inventory: get \'item name\'')
    print('Add companion to your party: join \'companion name\'')
    print('Rest to regain hp: rest')
    print('To see these instructions again: help')
    print('Quit the game: \'q\' or \'quit\'')
    print('')
    print('HAVE FUN!')
    sleep(1)


def attributes():
    """
    A function to randomly roll the stats for the player, between 3 and 18.  Depending on the value, they may receive a
    bonus added to the stat.  These stats will be used for skill checks.
    """
    # Generate a random number between 3 and 18
    stat = randint(3, 18)

    # If-else statements to determine if there is a bonus number based on the value of the random stat value
    if stat > 16:
        bonus = 3
    elif stat > 13:
        bonus = 2
    elif stat > 10:
        bonus = 1
    else:
        bonus = 0

    # Return the stat and bonus
    return stat, bonus


class Player:
    """
    The Player class.  This will assign the value to the stats by calling the attributes function.  Along with
    assigning the inventory, satchel, and companion lists.  The various methods revolve around actions that the
    player class can perform or uses during gameplay as well as displaying info about the player.
    """
    # Method to initialize the variables pertaining to the Player class, each stat will call the attributes function.
    # The rest of the variable will be set to various empty lists, integers, strings, etc.
    def __init__(self):
        # VIG = vigor, to be used as the Strength stat since str is a built-in.
        self.vig, self.vig_bonus = attributes()
        # DEX = dexterity at this time this stat is not used in any skill checks.
        self.dex, self.dex_bonus = attributes()
        # CON = constitution, this stat will apply a bonus to their health.
        self.con, self.con_bonus = attributes()
        # PER = perception, to be used as the Intelligence stat since int is a built-in.
        self.per, self.per_bonus = attributes()
        # WIS = wisdom, at this time this stat is not used in any skill checks.
        self.wis, self.wis_bonus = attributes()
        # CHA = charisma, this stat is used in skill checks to see if companions will join the player.
        self.cha, self.cha_bonus = attributes()
        # Max_hp will call the attributes function and then add 10 to the value that gets returned.
        self.max_hp = randint(10, 28) + self.con_bonus
        # Current_hp will be initialized to equal max_hp.
        self.current_hp = self.max_hp
        # Set inventory to an empty list
        self.inventory = []
        # Set satchel to an empty list
        self.satchel = []
        # Set companions to an empty list
        self.companion = []
        # Set the damage variable to an empty string
        self.damage = ''
        # Set the deflection variable to be 0 plus any bonus from the DEX attribute.
        self.deflection = 0 + self.dex_bonus

    # Stats method, to display all the Players stats, items, companions, health, etc...
    def stats(self):
        # If-else statements to check Players inventory in order to display the proper damage they will do.
        if 'sword' in self.inventory and 'torch' in self.inventory:
            self.damage = '3-12'
        elif 'sword' in self.inventory:
            self.damage = '2-8'
        elif 'torch' in self.inventory:
            self.damage = '1-6'
        else:
            self.damage = '1-4'

        # Print the details of the character.
        print('____________________________________________________')
        print(f'CHARACTER DETAILS                                   ')
        # Sets the printed values of the stats to be 2 digits (i.e. 08, 18, 03...)
        print(f'STR:{self.vig:02d} | DEX:{self.dex:02d} | CON:{self.con:02d} | INT:{self.per:02d} | WIS:{self.wis:02d} '
              f'| CHA:{self.cha:02d} ')
        # Displays current_hp next to max_hp for quick reference
        print(f'HP: {self.current_hp} / {self.max_hp}')
        # Display the character damage and deflection value for quick reference
        print(f'Damage: {self.damage} + {self.vig_bonus} | Defense: {self.deflection}')
        # Format the printing of the objects in inventory to be separated by a comma rather than displayed as a list
        print('Inventory: {}'.format(', '.join(self.inventory)))
        # Format the printing of the objects in satchel to be separated by a comma rather than displayed as a list
        print('Satchel: {}'.format(', '.join(self.satchel)))
        # Format the printing of the objects in companion to be separated by a comma rather than displayed as a list
        print('Companions: {}'.format(', '.join(self.companion)))
        print('____________________________________________________\n')

    # Attack method, determines how much damage the Player can deal to an enemy.
    def attack(self):
        # Player damage will be determined by what items are in the players inventory if any.  Damage will be a
        # random integer plus any bonus damage for VIG stat.
        if 'sword' in self.inventory and 'torch' in self.inventory:
            char_attack = randint(3, 12) + self.vig_bonus
        elif 'sword' in self.inventory:
            char_attack = randint(2, 8) + self.vig_bonus
        elif 'torch' in self.inventory:
            char_attack = randint(1, 6) + self.vig_bonus
        else:
            char_attack = randint(1, 4) + self.vig_bonus

        # Return the players total attack as an integer.
        return int(char_attack)

    # Companion attack method to determine any additional damage dealt during a battle.
    def companion_attack(self):
        # Initialize the 3 companions attack to 0
        cook_attack = 0
        squire_attack = 0
        ranger_attack = 0

        # For loop to check the companion list, for each friend in the list, generate a random integer for each other
        # their attacks
        for friend in self.companion:
            if friend == 'cook':
                cook_attack = randint(1, 4)
            elif friend == 'squire':
                squire_attack = randint(1, 6)
            elif friend == 'ranger':
                ranger_attack = randint(2, 8)

        # Return the combined amount of each friends attack to be returned as an integer.
        return int(cook_attack + squire_attack + ranger_attack)

    # Rest method for a player to regain their health.
    def rest(self):
        # Check if the current hp is less than max.  If it is, then set current hp equal to a random integer between
        # 1 and the value of the max hp minus the current hp. (i.e. 24 / 36(max), range of health to gain is between 1
        # and 12)
        if self.current_hp < self.max_hp:
            self.current_hp += randint(1, (self.max_hp - self.current_hp))
        # If current health is equal to or greater than max hp, the print the message.
        elif self.current_hp >= self.max_hp:
            print('I don\'t need to rest right now.')
            sleep(0.5)

    # Defense method, to determine how much damage reduction the player receives from any items in their inventory.
    def defense(self, e_name, e_atk):
        # Checks to see if armor and shield are in the inventory, if so, deduct the deflection value plus 2 from
        # the enemies attack
        if 'armor' in self.inventory and 'shield' in self.inventory:
            e_atk -= self.deflection + 2
        # Checks to see if armor or shield are in the inventory, if so, deduct the deflection value plus 1 from
        # the enemies attack
        elif 'armor' in self.inventory or 'shield' in self.inventory:
            e_atk -= self.deflection + 1
        # If neither in the inventory, deduct the deflection value from the enemies attack
        else:
            e_atk -= self.deflection

        # If the enemies attack is equal to 0 or less, then print the message that they player dodged the attack.
        if e_atk <= 0:
            print(f'You dodge the {e_name}\'s attack.')
        # Else, print the message that the enemy damaged them and deduct that value from the players current hp.
        else:
            self.current_hp -= e_atk
            print(f'The {e_name} attacks you for {e_atk} damage.')


class Enemy:
    """
    The Enemy class.  This will assign the type of enemy the player can run into and their stats.
    """
    # Initialize the values for name, hp, and attack.  These will then be set based on the enemy_char method
    def __init__(self):
        self.name = ''
        self.hp = 1
        self.attack = 1

    # Enemy_char method.  This determines which enemy the player runs into based on the room they're in.  If the player
    # is in any of the outside environments then they'll run into a goblin, wolf, or troll.  Otherwise, they'll run
    # into a bandit.  This method takes the argument of loc (location).
    def enemy_char(self, loc):
        # Create a list equal to the names in the room dictionary for all rooms outside the castle
        wilderness = ['Woods', 'North Trail', 'West Trail', 'South Trail']
        # If the location argument is in the wilderness list, then it will randomly choose between one of the three
        # enemies associated with the wilderness (goblin, wolf, or troll).
        if loc in wilderness:
            name = choice(['goblin', 'wolf', 'troll'])
            # Sets the name, hp, and attack values if the chosen enemy is a goblin.
            if name == 'goblin':
                self.name = 'goblin'
                self.hp = randint(1, 12)
                self.attack = randint(1, 4)
            # Sets the name, hp, and attack values if the chosen enemy is a wolf.
            elif name == 'wolf':
                self.name = 'wolf'
                self.hp = randint(4, 20)
                self.attack = randint(2, 8)
            # Sets the name, hp, and attack values if the chosen enemy is a troll.
            elif name == 'troll':
                self.name = 'troll'
                self.hp = randint(6, 36)
                self.attack = randint(4, 12)
        # If the location isn't in the wilderness, then the enemy is a bandit, and sets the name, hp, and attack as
        # such.
        else:
            self.name = 'bandit'
            self.hp = randint(3, 18)
            self.attack = randint(1, 6)

        # Returns all values associated with self that are set for each call to this method.
        return self


def skill(value, att, room=None):
    """
    A function to check if a skill was successfully used (in the background).  Depending on the skill that was
    checked the player may see an additional message, or find an item.  The function will take up to three variables,
    value of the skill, the name of the skill, and if required, the room that the check is being performed in.
    """
    # If-Else check to determine if there is any value to be subtracted or added to the randomly generated value
    # based on the value of the skill (or stat) to be checked.
    if value <= 6:
        result = randint(1, 20) - 2
    elif value <= 9:
        result = randint(1, 20) - 1
    elif value <= 12:
        result = randint(6, 20)
    elif value <= 15:
        result = randint(6, 20) + 1
    else:
        result = randint(10, 20) + 2

    # If-Else check if the skill to be checked was 'int'
    if att == 'int':
        # If the room parameter was set to 'hallway_3' and the blood value is False, process this if statement
        if room == 'hallway_3' and blood is False:
            # Call the global blood variable
            # If statement to determine the output based on the results of the randomly generated value
            if result < 12:
                # If the result is less than 12, then their skill check failed and print this message
                print('Looking out the window, you don\'t notice anything unusual on the ground below, and decide to '
                      'continue your search.')
                # Return False
                return False
            # Else they passed their skill check
            else:
                # Print this message
                print('You notice blood splatter on the window ledge, but no droplets in the hallway.  Maybe\n'
                      'whoever\'s blood this is left something behind outside.')
                # Return True
                return True

        # Else if the room parameter was set to 'pantry', process this elif statement
        elif room == 'pantry':
            # If their skill result is greater than 12
            if result > 12:
                # Print this message
                print('You notice a key ring with several keys, and recall at least one of them is to the door in '
                      'the cellar.')
                # Return True since the call to this function is simply checking if the skill check passed or not.
                return True
            # If the result was 12 or less, then return False
            else:
                return False

    # If the skill to check is 'cha', then return the result of the skill check
    elif att == 'cha':
        return result

    # If the skill to check is 'str', then return the result of the skill check
    elif att == 'str':
        return result

    # If the skill check is 'dex', then process this elif statement
    elif att == 'dex':
        # If the skill result is greater than 14
        if result > 14:
            # Print this statement
            print('You noticed the arrow flying towards you and with lightning reflexes you managed to dodge it.')
            # Return 0 which will be subtracted from the players current hp in the main loop
            return 0
        # Else if the result is 14 or less
        else:
            # Randomly generate a value between 1 and 4
            arrow_dmg = randint(1, 4)
            # Print this message
            print(f'You noticed the arrow, unfortunately it was only after it pierced your flesh '
                  f'causing {arrow_dmg} damage')
            # Return the random number to be subtracted from the players current hp.
            return arrow_dmg


def random_item():
    """
    Function to randomly place an item in room contents when main is run.
    """
    # Use the global variables item_list and room_count in order to modify them
    global item_list
    global room_count

    # If room count is less than or equal to 9 and the length of item_list is greater than 2, then if the randomly
    # generated number between 0 and 2 equals 1 (33% chance to place an item), place a randomly chosen item from
    # item_list, remove that item, add 1 to the room_count and return the item to be placed in the room dictionary in
    # main, for the current rooms contents.  If the random value was not 1, then return an empty string
    if room_count <= 5 and len(item_list) > 2:
        room_count += 1
        if randint(0, 2) == 1:
            item = choice(item_list)
            item_list.remove(item)
            return item
        else:
            return ' '
    # If the room count is greater than 5 or there are any items left in the list, then process this code.  This will
    # ensure that all items are placed in case the randomly generated if statement returns false too many times.
    elif room_count > 5 and len(item_list) > 0:
        item = choice(item_list)
        item_list.remove(item)
        room_count += 1
        return item
    # Else, if all items are placed, then return an empty string
    else:
        return ' '


def finish():
    """
    Function for when the player wins.
    """
    sleep(0.5)
    print('\nYou emerge from the cavern having to shield your eyes from the sun\'s glare.  Lady Sophia is '
          'safe,\nthe Marquees and Marchioness have been avenged, yet your heart is heavy.  If the '
          'words the bandit\nspoke are true, then the plot against his Grace runs deeper then you '
          'could\'ve imagined.\n'
          'To be continued...\n')
    print('CONGRATULATIONS!  You\'ve completed the first part of \"The Pyrewood Chronicles\"')
    exit()


def __main__():
    # use the global variable blood
    global blood

    # A nested dictionary. Each key is the room name for the program to reference and the values are a dictionary of
    # room names for display, descriptions, directions mapped to other rooms, as well as any contents or companions
    # to interact with.  Contents will call the random_item function.
    rooms = {'start': {'name': 'Courtyard',
                       'text': 'You stand in the courtyard of the castle you once called home.  Twelve years you\nspent'
                               ' roaming these grounds as a squire to the Lord who lives here, or at least\n'
                               'use to live here.  Sir Myrim Blackwater, Marquess of Pyrewood is dead now.  As '
                               'you\ngaze upon the massive wooden doors before you, you wonder if you can uncover '
                               'what\ntranspired within these cold walls...\n',
                       'south': 'great hall', 'contents': [], 'companion': []},
             'great hall': {'name': 'Great Hall',
                            'text': 'You now stand in the Great Hall, where you were knighted\nonly a few years ago.  '
                                    'You recall the kitchen was to the\neast and the trophy room was through the west '
                                    'door.  The\nstone staircase to the south still holds an ominous\nfeeling as it\'s '
                                    'shrouded in darkness.\n',
                            'east': 'kitchen', 'west': 'trophy room', 'south': 'staircase',
                            'contents': [random_item()], 'companion': []},
             'kitchen': {'name': 'Kitchen', 'text': 'You\'ve walked into the smell of curing flesh, as you see\nsalted'
                                                    ' meat hanging from the ceiling, ready to be made into\njerky.  The'
                                                    ' door on the north wall leads to the larder room.\nThe east side'
                                                    ' of the room is the pantry.\n',
                         'north': 'larder', 'east': 'pantry', 'west': 'great hall', 'contents': [random_item()],
                         'companion': ['cook']},
             'larder': {'name': 'Larder', 'text': 'The air in this room is cool to help preserve the perishable\nfood.'
                                                  '  However the only thing keeping cold in here is a dead body, with\n'
                                                  'a cleaver embedded into his skull.  A bandit whom didn\'t make it\n'
                                                  'out alive presumably.\n',
                        'south': 'kitchen', 'contents': [random_item()], 'companion': []},
             'pantry': {'name': 'Pantry',
                        'text': 'The shelves are usually packed full of provisions, but now only hold a few items.  '
                                '\nYou recall sneaking in here at night to help yourself to bread and jerky as a\n'
                                'young squire, while trying to avoid the cook.\n',
                        'west': 'kitchen', 'contents': ['jerky', 'bread'], 'companion': []},
             'trophy room': {'name': 'Trophy Room',
                             'text': 'This room is filled with the trophies of several animal hunts.  You recall '
                                     'assisting in the hunt of the black bear\nthat still towers over you in the '
                                     'corner.  The archway on the west wall leads to the library.\n',
                             'west': 'library', 'east': 'great hall', 'contents': [random_item()], 'companion':
                                 ['squire']},
             'library': {'name': 'Library', 'text': 'You\'ve entered a massive library with books and scrolls from '
                                                    'floor to ceiling on three\nof the walls with a massive oak desk'
                                                    ' sitting in the middle of the room.\n',
                         'east': 'trophy room', 'contents': [random_item()], 'companion': []},
             'staircase': {'name': 'Staircase', 'text': 'The massive stone steps lead up to the living quarters, and '
                                                        'down to the cellar.\n',
                           'up': 'hallway1', 'down': 'cellar', 'north': 'great hall', 'contents': [],
                           'companion': []},
             'hallway1': {'name': 'Upstairs Hallway', 'text': 'The long hallway leads to the various rooms of the '
                                                              'Marquees and Marchioness.\n',
                          'east': 'bedroom1', 'west': 'bedroom2', 'south': 'hallway2', 'down': 'staircase',
                          'contents': [], 'companion': []},
             'bedroom1': {'name': 'Bedroom 1', 'text': 'This is their Grace\'s private chamber.  His Grace\'s '
                                                       'great sword still hangs on the wall\nabove the fireplace.  The '
                                                       'Marchionesses changing screen lays on the floor torn to pieces.'
                                                       'Clothing is scattered everywhere\nand the furniture has been '
                                                       'tossed around.  There is a large pool of blood near the '
                                                       'fireplace with drag marks leading towards a window.\n',
                          'west': 'hallway1', 'east': 'window', 'contents': [random_item()], 'companion': []},
             'window': {'name': 'Bedroom Window', 'text': 'You peer out the window to see the twisted body of Her Grace'
                                                          ' ,\nlaying lifeless on the cold ground below.  Her throat\n'
                                                          'has been sliced and the fall snapped some of the bones out\n'
                                                          'through her alabaster skin.\n',
                        'west': 'bedroom1', 'contents': [], 'companion': []},
             'bedroom2': {'name': 'Bedroom 2', 'text': 'These are the chambers of Lady Sophia, the heir of the castle.'
                                                       '  Her room lays in shambles\nas her clothing is scattered '
                                                       'on the floor, and most of the furniture\nis in broken pieces.  '
                                                       'You notice some blood splattered on the floor.\n',
                          'east': 'hallway1', 'contents': [random_item()], 'companion': []},
             'hallway2': {'name': 'Upstairs Hallway', 'text': 'More rooms of their Grace.\n', 'east': 'bedroom3',
                          'west': 'drawing room', 'south': 'hallway3', 'north': 'hallway1', 'contents': [],
                          'companion': []},
             'drawing room': {'name': 'Drawing Room', 'text': 'Given the layout of the room, with the plush '
                                                              'over-sized chairs around an ornate table, and '
                                                              'the large\nDavenport positioned in front of the '
                                                              'fireplace indicates that this must be the drawing room.',
                              'east': 'hallway2', 'contents': [random_item()], 'companion': []},
             'bedroom3': {'name': 'Bedroom', 'text': 'Just a spare bedroom with a simple bed, chest of drawers, '
                                                     'changing screen, and a small table with two chairs',
                          'west': 'hallway2', 'contents': [random_item()], 'companion': []},
             'hallway3': {'name': 'End of Hallway', 'text': 'You\'ve reached the end of the hallway.  The window '
                                                            'shutters lay on the floor smashed to pieces.\n',
                          'north': 'hallway2', 'contents': [], 'companion': []},
             'cellar': {'name': 'Cellar', 'text': 'The musty air fills your nostrils as soon as you step off the '
                                                  'stairs.\n',
                        'west': 'door', 'up': 'staircase', 'contents': [random_item()], 'companion': []},
             'door': {'name': 'Tunnel Door', 'text': 'You try to open the door but it\'s locked.\n',
                      'west': 'door', 'east': 'cellar', 'contents': [], 'companion': []},
             'tunnel': {'name': 'Tunnels', 'text': 'You\'re in the tunnels.\n', 'south': 'ice house', 'east': 'cellar',
                        'contents': [], 'companion': []},
             'ice house': {'name': 'Ice House', 'text': 'This room is colder than the larder.  There\'s snow from the '
                                                        'previous winter still packed in a corner.\n',
                           'south': 'woods', 'north': 'tunnel', 'contents': [random_item()], 'companion': []},
             'woods': {'name': 'Woods', 'text': 'You come out of the ice house into the thick of the woods.  You see '
                                                'a game trail to the south, and a foot trail to the west.\n',
                       'west': 'west trail', 'north': 'ice house', 'south': 'south trail', 'contents': [], 'companion':
                           []},
             'west trail': {'name': 'West Trail', 'text': 'The trail comes to a fork, north or south.  The north trail '
                                                          'doesn\'t show much use.  The south trail widens slight, but '
                                                          'shows\n as much use as the north trail.  None of this area '
                                                          'is familiar.\n',
                            'north': 'north trail', 'south': 'west trail', 'east': 'woods', 'contents': [],
                            'companion': []},
             'north trail': {'name': 'North Trail', 'text': 'Trees, all you see are trees all around you.\n',
                             'north': 'north trail', 'contents': [], 'companion': []},
             'south trail': {'name': 'South Trail', 'text': 'You see the body of a bandit, one of his legs is clearly '
                                                            'broken as the bone\nis protruding through his flesh.  Two '
                                                            'arrows are sticking out his back.\nThis was probably the '
                                                            'one who left the castle by way of the second floor '
                                                            'window.\n',
                             'east': 'cave', 'north': 'woods', 'contents': ['apple'], 'companion': ['ranger']},
             'cave': {'name': 'Bandit Hideout', 'text': 'You\'ve found the hideout of the bandits who killed your lord '
                                                        'and lady.  As you creep into\nthe cave you see the flickers '
                                                        'of fire light dancing on the cave walls.  You can hear\n'
                                                        'several voices talking.  As you peer around the last corner '
                                                        'you see Lady Sophia, she\'s wrapped\nin chains, her lip is'
                                                        ' cracked open with fresh blood trickling out,\nand you can '
                                                        'several burn marks upon her arms.\n',
                      'contents': [], 'companion': []}}

    # Create list with the various directions the player can travel
    directions = ['north', 'south', 'east', 'west', 'up', 'down']
    # Set the start room
    current_room = rooms['start']
    # Create an empty list to display the room directions a player can travel
    room_directions = []

    # call the instructions function.
    instructions()

    # Assign Player class to the variable p for less typing to call class methods later.
    p = Player()

    # While loop for the game to continue until conditions are met for exiting (win, lose, or quit).
    while True:
        # Call the character class to display player stats, companions and inventory while in the loop.
        p.stats()
        # Display the current room name in all uppercase letters
        print('[{}]'.format(current_room['name'].upper()))
        # Display the text associated with the current room.
        print(current_room['text'])

        # if the list room_direction is empty, then look at each direction in the directions list, if they're listed
        # in the current rooms dictionary, then append them to the room_direction list and then print.  Otherwise, if the
        # room_directions list is not empty, set it to empty and repeat.
        for direction in directions:
            if direction in current_room:
                room_directions.append(direction)
        # Display the directions that a player can take depending on the room they're in.
        print('Directions: {}'.format(', '.join(room_directions)))
        # Set the room_directions list back to empty
        room_directions = []

        # If the current room has contents, then process this statement.
        if current_room['contents']:
            # Display what items are in the room.
            print('In the room is: {}'.format(', '.join(current_room['contents'])))

        # If the current room has a companion, then process this statement.
        if current_room['companion']:
            # Display the companions that are in the room.
            print('In the room is a: {}'.format(', '.join(current_room['companion'])))

        # If keys are not currently in the players inventory, then process this statement
        if 'keys' not in p.inventory:
            # If the current room is pantry, then continue
            if current_room == rooms['pantry']:
                # If the skill check passed, then continue
                if skill(p.per, 'int', 'pantry'):
                    # Add 'keys' to the players inventory.
                    p.inventory.append('keys')

        # If the current room is 'hallway3', then process this statement.
        if current_room == rooms['hallway3']:
            # If the global blood variable is False, then continue
            if blood is False:
                # Skill check passed
                if skill(p.per, 'int', 'hallway_3'):
                    # Set the global blood variable to True
                    blood = True

        # IF the current room is 'door', then process this statement.
        if current_room == rooms['door']:
            # If 'keys' are in the players inventory, continue
            if 'keys' in p.inventory:
                # Print this message
                print('You use the cellar key to unlock the door.')
                # Set the current room equal to 'tunnel'
                current_room = rooms['tunnel']
                # Remove the 'keys' from the inventory (this way it doesn't throw of the inventory check at the final
                # room of the game).
                p.inventory.remove('keys')
                # Move back to the start of the while loop, this way the player knows they're in the Tunnel,
                # and not stuck somewhere in limbo.
                continue
            # If keys are not in the inventory, then process this statement.
            elif 'keys' not in p.inventory:
                # If the result of a 'str' skill check is greater than 12, then continue.
                if skill(p.vig, 'str') > 12:
                    # If the skill check passed, then print this message
                    print('You throw your shoulder against the door, smashing it open.')
                    # Player looses 4 health because they really threw their shoulder into it.
                    p.current_hp -= 4
                    # Set current room to Tunnel
                    current_room = rooms['tunnel']
                    # Move back to the start of the while loop, as mentioned earlier.
                    continue
                # Else they failed their skill check and don't know how to open the door now.
                else:
                    # Print this message.
                    print('You tried to bash the door but couldn\'t.  You see no way of opening this door without the '
                          'key.')

        # If the current room is 'tunnel', then process this statement.
        if current_room == rooms['tunnel']:
            # Set the 'west' key in the 'cellar' key of the rooms dictionary equal to tunnel, this will bypass the
            # 'door' key if the player goes back to the cellar later.
            rooms['cellar']['west'] = 'tunnel'
            # Set the players current hp to itself minus the results of the 'dex' skill check.
            p.current_hp -= skill(p.dex, 'dex')

        # If the current room is 'woods', then process this statement
        if current_room == rooms['woods']:
            # Check if the random integer is true or false, if true then continue
            if randint(0, 1):
                # Set the players current hp to itself minus the results of the 'dex' skill check.
                p.current_hp -= skill(p.dex, 'dex')
                # Print this message
                print('Bandits are hiding in the woods and using you for target practice.')
            # If the global blood variable is true, then continue and print the message.
            if blood is True:
                print('You notice drag marks and a blood trail towards the south.')

        # If current room is 'north trail', then process this statement
        if current_room == rooms['north trail']:
            # If the players current hp is greater or equal to 0, then continue.
            if p.current_hp <= 0:
                # The player lost and the game is over. :(
                print('You\'ve wandered through the woods until your body gives out and you collapse from starvation.')
                print('GAME OVER')
                exit()
            # Otherwise the player looses 5 hp for aimlessly wandering through the woods unprepared.
            p.current_hp -= 5

        # If the current room is cave, then process this statement, which is the final room of the game.
        if current_room == rooms['cave']:
            # Make three variables to call the Enemy class to get each bandit's hp and attack
            bandit1 = Enemy().enemy_char(current_room['name'])
            bandit2 = Enemy().enemy_char(current_room['name'])
            bandit3 = Enemy().enemy_char(current_room['name'])

            # Create a target dictionary that calls the Enemy class to get the bandits hp function for their
            # individual hp.
            targets = {'Bandit 1': bandit1.hp, 'Bandit 2': bandit2.hp, 'Bandit 3': bandit3.hp}

            # Print a blank line, then the message, followed by another blank line.
            print('')
            print('You see three bandits stand up and draw daggers as you enter the cavern.')
            print('')
            # pause for 1/2 a second.
            sleep(0.5)

            # if the player has all 6 items in their inventory then they automatically win the game.
            if len(p.inventory) == 6:
                print(f'As soon as you see them your reflexes take over.  You throw the oil at their feet,\nalong with '
                      f'the torch setting them ablaze.  With your next breath you throw the kitchen knives\nat '
                      f'the bandit farthest away, embedding them into his throat and chest.  Before he hits the '
                      f'ground\nyou\'ve exploded into a dash raising your shield to protect yourself from the\n'
                      f'flames and to knock the remaining bandits down.\nWhile they\'re prone you quickly thrust your '
                      f'sword into each of their chests ending\ntheir tortured screams.  Kicking dirt to put the '
                      f'flames out you search their bodies to find\nthe key to the Lady\'s chains.')
                # Call the finish function to display the message that they won.
                finish()

            # If they don't have all 6 items, process this statement
            else:
                # For loop to look through the companion list and for each 'friend' in the list, process the loop.
                for friend in p.companion:
                    # Select a random enemy from the targets' dictionary.
                    random_enemy = choice(list(targets.keys()))
                    # Remove the random enemy.
                    targets.pop(random_enemy)
                    # Print the message for which companion took out which enemy.
                    print('{} takes out {}'.format(friend.capitalize(), random_enemy))
                    # Print a blank line for easier reading.
                    print('')
                # Now if the length of the targets dictionary is 0, process this statement.
                if len(targets) == 0:
                    # Print the message that the companions dispatched all the enemies. Because friends are awesome!
                    print(
                        f'Your companions launch a surprise attack, taking out all of the bandits.  You find the keys\n'
                        f'to release Lady Sophia.  With his last breath the bandit proclaims more will come as his\n'
                        f'liege will not stop until these lands are his.')
                    # Pause the game for 1 second to allow the player to read all the walls of text this game produces.
                    sleep(1)
                    # Call the finish function to display the message that they won.
                    finish()

            # If the statement above did not generate the finish() function, then while the targets
            # dictionary isn't empty, execute the following code
            while targets != {}:
                # Create a list of the names of the bandits left in the targets dictionary, to be used in a for loop
                # later.
                target_list = list(targets.keys())
                # Print the targets' dictionary.
                print(targets)
                # Display the players current hp.
                print(f'Player: {p.current_hp}')
                # Print a blank line for clarity.
                print('')
                # Print a message that lets the player know the bandits are attacking.
                print(f'The bandit(s) launch an attack.')

                # For each bandit left in the target list, execute the Player class defense function passing in the
                # bandit name and a call to the Enemy class enemy_char function to get a random attack value each
                # time the defense function is called.
                for _ in target_list:
                    p.defense('bandit', Enemy().enemy_char(current_room['name']).attack)

                # If the players health is at or below 0, print the message that they lost and exit the program
                if p.current_hp <= 0:
                    print('The bandits were too much for your skill.  As you lay on the cavern floor, the damp earth\n'
                          'beneath your body begins to feel colder and colder as the life blood trickles out of your '
                          'wounds.\nGAME OVER')
                    exit()

                # Selects a random enemy from the target list that the player will attack.
                random_enemy = choice(list(targets.keys()))

                # Set the attack variable equal to the Player class attack method.
                attack = p.attack()
                # Set the comp_attack variable equal to the Player class companion attack method.
                comp_attack = p.companion_attack()
                # Subtract the players attack and the companion attack from the randomly selected target's hp.
                targets[random_enemy] -= attack + comp_attack
                # If there is a companion in the companion list, then process this statement
                if p.companion:
                    # Prints the message telling the player how much damage the player did and the companion.
                    print(f'You attacked {random_enemy} causing {attack} damage, and your companion did {comp_attack} '
                          f'damage.')
                else:
                    # Otherwise display the damage that the player did since there's no companions around,
                    # it's lonely fighting alone.
                    print(f'You attacked {random_enemy} causing {attack} damage.')
                # If the randomly selected targets hp is less than or equal to 0, then process this statement.
                if targets[random_enemy] <= 0:
                    # remove the random enemy from the target list.
                    targets.pop(random_enemy)
                    # Print the message letting the player know they killed the bandit.
                    print(f'You slayed the bandit.')
                # Print a blank line for clarity.
                print('')
                # Pause for a second and take a breath before continuing the fight.
                sleep(1)
            # If the target dictionary is empty, the print this message.
            print('With his last breath the bandit proclaims more will come as his liege will\nnot stop until these '
                  'lands are his.')
            # Call the finish function, because you won!!
            finish()

        # Get the players input, and strip it.
        command = input('\nWhat do you want to do? ').strip()

        # If the players input is in directions list, then process this statement.
        if command in directions:
            # If the command is in the current room, then continue.
            if command in current_room:
                # The current room will be set to the value of the key equal to command of the current room
                current_room = rooms[current_room[command]]

                # If the randomly generated number equal 1, then process this statement (random battle).
                if randint(1, 4) == 1:
                    # Assign the enemy associated with the current room, found in the enemy character method of the
                    # Enemy class to the variable 'e'.
                    e = Enemy().enemy_char(current_room['name'])

                    # Print the message that displays the name of the enemy they stumbled upon.
                    print(f'You come across a roaming {e.name}.')
                    # While loop to run until it isn't true, meaning the player died or the enemy died, there can be
                    # only one.
                    while True:
                        # Display the player and enemy hp so the player can make an informed decision of how to
                        # proceed (fight or flee).
                        print(f'Player: {p.current_hp}  |  Enemy: {e.hp}')
                        # Ask for the players input (fight of flee).
                        command = input('What do you do? (attack or flee) \n')
                        # If their choice is to fight, then process this statement.
                        if command.lower() == 'attack':
                            # Set player attack to the attack method of the player class.
                            player_attack = p.attack()
                            # Do the same for companion.
                            comp_attack = p.companion_attack()
                            # Subtract the player and companion damage from the enemy's hp.
                            e.hp -= player_attack + comp_attack
                            # Display what the damage done is.
                            print(f'You attack the {e.name} for {player_attack} damage.')
                            # If there is a companion in the companion list, then print this message.
                            if p.companion:
                                print(f'Your companion(s) attack the {e.name} for {comp_attack} damage')
                            # If the enemies hp is less than or equal to 0, then they died, and print this message to
                            # let the player know.
                            if e.hp <= 0:
                                print(f'You slayed the {e.name}')
                                # Take a 1-second breather as that was an intense battle.
                                sleep(1)
                                # Exit the while loop.
                                break

                            # If the enemy is still ticking after all of that, then call the defense method of the
                            # Player class, passing in the enemy name, and a call to their attack method.
                            p.defense(e.name, Enemy().enemy_char(current_room['name']).attack)

                            # If the players hp drops to 0 or less, then oops, they died.
                            if p.current_hp <= 0:
                                # Print the message reminding them of the enemy that was their downfall.
                                print(f'The {e.name} slayed you.')
                                # Exit the game
                                exit()

                        # If player flees, then process this cowardly statement.
                        elif command.lower() == 'flee':
                            # If the random integer is True, then process this.
                            if randint(0, 1):
                                # Print the fled.
                                print('You managed to run away.')
                                # Exit the while loop.
                                break
                            else:
                                # Otherwise they didn't get away and the enemy attacks them.
                                print(f'The {e.name} blocked your escape.')
                                # attack is set to a random number between 1 and 4.
                                e_attack = randint(1, 4)
                                # Subtract the attack value from the player's hp.
                                p.current_hp -= e_attack
                                # Display how much they're hurting now.
                                print(f'And attacked you for {e_attack} damage.')
                                # Continue back to the start of this while loop.
                                continue

                        else:
                            # If they try anything other than attack or flee, then they can't do that now.
                            print('You can\'t do that right now.')
            else:
                # If the direction isn't in the direction list, then the player can't go that way and let them know.
                print('I can\'t go that way.')
                # Now take a 1-second breather as that player entered a bizarre command.
                sleep(1)

        # If the lowercase command is equal to 'q' or 'quit', then say goodbye and exit the program.
        elif command.lower() in ('q', 'quit'):
            print('Good-bye.')
            exit()

        # If the lowercase command is equal to 'help', then call the instructions function so they know what they
        # can or should do.
        elif command.lower() == 'help':
            instructions()

        # Check is the split lowercase command is greater than 1
        elif len(command.lower().split()) > 1:
            # If the first element of the split command is 'get', then process this.
            if command.lower().split()[0] == 'get':
                # Set the item to the lowercase second index element in the split command.
                item = command.lower().split()[1]
                # If that item is in the contents of the current room, then continue.
                if item in current_room['contents']:
                    # If it's any of the items in this group which is food, then it'll go into the satchel list.
                    if item in ('jerky', 'bread', 'apple'):
                        # Remove the item from the room contents so the player can't exploit a loophole and keep
                        # grabbing items.
                        current_room['contents'].remove(item)
                        # add the item to the satchel list.
                        p.satchel.append(item)
                    else:
                        # Otherwise remove the item from the contents of the room, and add it to the inventory list.
                        current_room['contents'].remove(item)
                        p.inventory.append(item)
                else:
                    # Otherwise the player is being silly and that item isn't in this room.
                    print('I don\'t see that here.')

            # If the lowercase command is equal to 'rest', then call the rest method of the Player class.
            elif command.lower() == 'rest':
                p.rest()

            # Check if the first element of the lowercase split command is equal to join.
            elif command.lower().split()[0] == 'join':
                # If it is, then the second element will be set to the member variable.
                member = command.lower().split()[1]
                # If the member is in the current rooms companion key, then continue.
                if member in current_room['companion']:
                    # If the players intelligence skill is less than or equal to 12, then continue.
                    if int(skill(p.cha, 'cha')) <= 12:
                        # Print a blank line for clarity, then print the message about how much the companion in this
                        # room hates the player.
                        print('')
                        print(f'How dare you show your face here!  You turned your back on His Grace when he '
                              f'needed help and now he\'s dead.  Now YOU, will find no help here!')
                        # Generate a random number between 1 and 4 for the attack the companion will inflict on the
                        # player.
                        attack = randint(1, 4)
                        # Print the message that the companion hit the player.
                        print(f'The {member} spits at your feet before punching you in the gut for {attack} health as '
                              f'they leave.')
                        # Take a 1-second breather to understand what just happened.
                        sleep(1)
                        # Subtract the attack from the players' hp.
                        p.current_hp -= attack
                        # Remove that companion from the current room's dictionary.
                        current_room['companion'].remove(member)
                    # Otherwise the companion will join the player.
                    else:
                        # Print the message to let them know they're joining the fight.
                        print(f'Welcome home sir knight, you\'ll have my assistance in avenging His Grace.')
                        # Take a 1-second breather to celebrate your new friendship!
                        sleep(1)
                        # Remove the companion from the current room's dictionary.
                        current_room['companion'].remove(member)
                        # Add that companion to the Players companion list.
                        p.companion.append(member)
                # Else that companion isn't here, and let the player know that.
                else:
                    print('I can\'t ask them to join my crusade.')

            # Check if the first element of the split command is equal to 'eat'.
            elif command.lower().split()[0] == 'eat':
                # Set item to the second element of the split command.
                item = command.lower().split()[1]
                # If that item is in the satchel then process this statement.
                if item in p.satchel:
                    # Remove the item from teh satchel list.
                    p.satchel.remove(item)
                    # Add a randomly generated number between 1 and 6 to the player's hp.
                    p.current_hp += randint(1, 6)
                    # Remind the player that they ate the item, and regained some hp.
                    print(f'You eat the {item}, regaining health.')
                # Else that item isn't edible.
                else:
                    print('I can\'t eat that.')
            # If the command wasn't in any of those if-elif statements, then let the player know that we don't
            # understand what they're trying to do.
            else:
                print('I don\'t understand what you want to do.')

        # If the command wasn't any of those previous items, then let the player know we don't understand what they
        # want.
        else:
            print('I don\'t understand what you want to do.')

        # Finally, if the players hp gets to 0 or less, then print the message that they lost and exit the game.
        if p.current_hp <= 0:
            print(f'The toll of your quest has been too great of a burden for you to continue.')
            exit()


# Run the main function.
__main__()
