Char_1X
image blackscreen:
    Solid("#000000")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0

image whitescreen:
    Solid("#ffffff")
    on show:
        alpha 1.0
        linear 0.4 alpha 1.0
    on hide:
        alpha 1.0
        linear 0.4 alpha 0.0



init -1:
    
    default Cheat = 0

init:
    default Char_1X = Char_1Class("Char_1", "Char_1", 0,0)


# Le jeu commence ici
label start:
    
    camera :
        perspective True
    
    $ Char_1X.introduction()




label firstscene:

    # $ Char_1X = Char_1Class("Char_1", "Char_1", 0,0,0,0)
    
    $ Char_1X.xpos = 0.6
    $ Char_1X.show(at_right) # same as "show Char_1 at at_right"
    $ Char_1X.show(Char_1_at) # same as "show Char_1 at Char_1_at"


    "Test" "HelloWorld \"LoremIpsumDolor\""

    $ Char_1X.changeSet(Char_1Set2)

    $ Char_1X.morph("blush_heavy_on")

    C1 "test"

    hide Char_1
    
    return
