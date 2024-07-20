
init python:

# Class Characters
    class CharactersClass(object):
        def __init__(self,TAG,name,mood,affection):
            self.TAG = TAG              # object tag : NameX
            self.imgTAG = TAG           # tag for the image
            self.name = name            # name currently used
            self.names = [name]         # list of al names
            self.mood = mood            # current mood
            self.affection = affection  # current affection

            characters.append(self) # AJOUT A LA LISTE DES PERSO

            self.inventory = []

            self.history = []  #checkpoint with the character (exemple "met")

            # Default position of the image in the screen
            self.xpos = 0.8
            self.yanchor = 0.5
            self.xzoom = 1
            self.Xat = at_right

            self.parts = []         # list of all parts of the image
            self.initMorph = []     # list of all initial body parts
            self.currentMorph = []  # list of all body parts equiped
            self.currentSet = []    # list of all clothes parts equiped
            self.nakedBase = []     # list of all parts when naked
            self.poseBase = ""      # pose used by default (ex : idle / dancing / ...) different than expressions ( smiling ...)

        # Show function that display the player on the screen
        def show(self, position=None, xpos=None, xzoom=1, pose=None):
            # self.equipMorph(self.currentMorph)
            self.equipSet(self.currentSet)
            self.equipMorph(self.currentMorph)
            if pose is None:
                pose = self.poseBase
            if xpos is not None:
                self.xpos = xpos
            self.xzoom = xzoom
            if position is None:
                position = center
            #renpy.show("{} {}".format(self.imgTAG, pose), at_list=(position,)) #, tag=xzoom)
            renpy.show("{} {}".format(self.imgTAG, pose), at_list=(position,))

        # return the current set of body atributes used by the character
        def getMorph(self):
            return self.currentMorph
        
        # return the current set of clothes and accessories equiped on the character
        def getSet(self):
            return self.currentSet

        # Initialize function for all characters
        def introduction(self):
            self.changeSet(self.nakedBase)
            self.changeMorph(self.initMorph)
            self.changePose(self.poseBase)
            if self == Char_1:
                self.changeSet(Char_1Set1)
            elif self == Char_2:
                self.changeSet(Char_2Set1)


    #MANAGE CHARACTERS APPEARANCE
        
        #Equip and Unequip body parts
        def morph(self, part):
            if part not in self.currentMorph:
                self.currentMorph.append(part)
            renpy.show("{} {}".format(self.imgTAG, part))

            # manage which part need to be replaced when another is added
            self.morphChange(part) # this function depends on the children class
            
        def unmorph(self, part):
            if part in self.currentMorph:
                renpy.show("{} -{}".format(self.imgTAG, part))
                self.currentMorph.remove(part)

        def equipMorph(self, arguments):
            for part in arguments:
                self.morph(part)


        # unequip current set and equip "body sets"
        def eraseMorph(self):
            for part in self.currentMorph[:]:  # Using [:] to create a copy of the list
                self.unmorph(part)
 
        def changeMorph(self, outfit):
            self.eraseMorph()
            self.equipMorph(outfit)
        


        #Change character animation
        def changePose(self, pose):
            renpy.show("{} {}".format(self.imgTAG, pose))


        #Equip and Unequip clothes and clothes sets :
        def equip(self, part):
            if part not in self.currentSet:
                self.currentSet.append(part)
            renpy.show("{} {}".format(self.imgTAG, part))

            # manage which part need to be replaced when another is added
            self.outfitChange(part) # this function depends on the children class

        def unequip(self, part):
            if part in self.currentSet:
                renpy.show("{} -{}".format(self.imgTAG, part))
                self.currentSet.remove(part)

        def equipSet(self, arguments):
            for part in arguments:
                self.equip(part)

        # unequip current set and equip set
        def eraseClothes(self):
            for part in self.currentSet[:]:  # Using [:] to create a copy of the list
                self.unequip(part)
 
        def changeSet(self, outfit):
            self.eraseClothes()
            self.equipSet(outfit)



    # Manage inventory
        def addInventory(self,item):
            self.inventory.append(item)

        def getItem(self,item):
            if item in self.inventory:
                return item.name
            elif self.inventory == []:
                return "no object in inventory"
            else:
                return "object is not in inventory"

        def removeFromInventory(self,item):
            if item in self.inventory:
                self.inventory.remove(item)




init -1:

# Make sure that body parts, clothes and accessories are saved in the right folder as name.exp3,
# as well as poses (animations) posename.motion3.

    image Char_1 = Live2D("images/characters/char_1", default_fade=0.0, loop=True,
                        nonexclusive=["hair_base_on", "hair_bun_on",
                                    "blush_base_on", "blush_heavy_on", "blush_tired_on",
                                    "vest_on",
                                    "colar1_on", "colar2_on",
                                    "gloves_on",
                                    "top_casual_on", "top_police_on",
                                    "bottom_short_on", "bottom_police_on",
                                    "panties_base_on",
                                    "legwear_police_on",
                                    "shoes_police_on",], seamless=True)


define C1 = Character('[Char_1X.name]', color="#dd12bb", image="Char_1")


define characters = []
define locations = []

define right_pos = (0.8, 0.6)
define zoom_characters = 0.9

transform at_right:
    xpos 0.8
    ypos 0.6
    anchor (0.5, 0.5)
    zoom zoom_characters
    xzoom 1

transform Char_1_at:
    xpos Char_1X.xpos
    ypos 0.6
    xanchor 0.5, 
    yanchor Char_1X.yanchor
    zoom zoom_characters
    xzoom Char_1X.xzoom