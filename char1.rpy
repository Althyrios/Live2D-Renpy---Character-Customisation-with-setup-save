init python:

    # Sets
    Char_1Set1 = ["hair_base_on", "colar1_on", "colar2_on",
                "bottom_short_on", "panties_base_on", "legwear_police_on",
                "shoes_police_on", "top_casual_on"] # casual set

    Char_1Set2 = ["hair_base_on", "vest_on", "colar1_on", "colar2_on", "bottom_police_on",
                "panties_base_on", "legwear_police_on", "gloves_on",
                "shoes_police_on", "top_police_on"] # police set

    Char_1Set4 = ["hair_base_on", "panties_base_on",
                "top_casual_on"] # casual night set

    Char_1CustomSet1 = []
    Char_1CustomSet2 = []
    Char_1CustomSet3 = []

    Char_1Morph1 = ["blush_base_on",] # normal
    Char_1Morph2 = ["blush_heavy_on",] # heavy blush



    class Char_1Class(CharactersClass):
        def __init__(self,TAG,name,mood,affection):
            super(Char_1Class, self).__init__(TAG, name, mood, affection)

            self.parts = ["hair_base_on", "hair_bun_on",
                        "blush_base_on", "blush_heavy_on", "blush_tired_on",
                        "vest_on",
                        "colar1_on", "colar2_on",
                        "gloves_on",
                        "top_casual_on", "top_police_on",
                        "bottom_short_on", "bottom_police_on",
                        "panties_base_on",
                        "legwear_police_on",
                        "shoes_police_on"]


            self.initMorph = Char_1Morph1
            self.nakedBase = ["hair_base_on"]
            self.poseBase = "default_pose"
            #self.initSet = Char_1Set1
            
            self.pos = (0.77, 0.6)
            self.yanchor = 0.5
            self.Xat = Char_1_at
        

        # rule all combination
        def outfitChange(self,outfit):
            # if HAIR
            if outfit == "hair_base_on":
                self.unequip("hair_bun_on")
            elif outfit == "hair_bun_on":
                self.unequip("hair_base_on")

            # if TOP
            if outfit == "top_casual_on":
                self.unequip("top_police_on")
            elif outfit == "top_police_on":
                self.unequip("top_casual_on")
                
            # if BOTTOM
            if outfit == "bottom_short_on":
                self.unequip("bottom_police_on")
            elif outfit == "bottom_police_on":
                self.unequip("bottom_short_on")

            # if PANTIES
            # if outfit == "panties_base_on":

            # if LEGWEAR
            #if outfit == "legwear_police_on":

            #if SHOES
            #if outfit == "shoes_police_on":

        def morphChange(self, morph):
            
            # if BLUSH
            if morph == "blush_base_on":
                self.unmorph("blush_heavy_on")
            elif morph == "blush_heavy_on":
                self.unmorph("blush_base_on")