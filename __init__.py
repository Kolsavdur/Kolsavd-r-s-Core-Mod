from modloader import modast, modinfo
from modloader.modclass import Mod, loadable_mod
import renpy
from renpy.display import im

@loadable_mod
class AWSWMod(Mod):
    name = "Kolsavdur Core Mod"
    version = "v1.00"
    author = "Kolsavdur"
    dependencies = ["MagmaLink", "?Side Images"]

    def mod_load(self):
        ml = modinfo.get_mod("MagmaLink").import_ml() #Checks if MagmaLink is installed

        if modinfo.has_mod("Side Images"): #Side Images support (Thanks a ton with the help, 4onen! <3)
            #Remy Side Images
            renpy.exports.image("side remy sleep", im.Flip(im.Scale(im.Crop("cr/kolremy_sleeping.png",(5,30,500,600)),250,300),horizontal=True))
            renpy.exports.image("side remy angrycry", im.Flip(im.Scale(im.Crop("cr/kolremy_angrycry.png",(5,30,500,600)),250,300),horizontal=True))
            renpy.exports.image("side remy cry", im.Flip(im.Scale(im.Crop("cr/kolremy_cry.png",(5,30,500,600)),250,300),horizontal=True))
            renpy.exports.image("side remy lookcry", im.Flip(im.Scale(im.Crop("cr/kolremy_lookcry.png",(5,30,500,600)),250,300),horizontal=True))
            renpy.exports.image("side remy shycry", im.Flip(im.Scale(im.Crop("cr/kolremy_shycry.png",(5,30,500,600)),250,300),horizontal=True))
            renpy.exports.image("side remy startcry", im.Flip(im.Scale(im.Crop("cr/kolremy_startcry.png",(5,30,500,600)),250,300),horizontal=True))
            #Logan Side Images
            renpy.exports.image("side logan normal", im.Flip(im.Scale(im.Crop("cr/kollogan_normal.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan serious", im.Flip(im.Scale(im.Crop("cr/kollogan_serious.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan smiling", im.Flip(im.Scale(im.Crop("cr/kollogan_smiling.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan surprised", im.Flip(im.Scale(im.Crop("cr/kollogan_surprised.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan thinking", im.Flip(im.Scale(im.Crop("cr/kollogan_thinking.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan annoyed", im.Flip(im.Scale(im.Crop("cr/kollogan_annoyed.png",(100,0,250,300)),250,300),horizontal=True))
            #Tired Logan Side Images
            renpy.exports.image("side logan tnormal", im.Flip(im.Scale(im.Crop("cr/kollogan_tirednormal.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan tserious", im.Flip(im.Scale(im.Crop("cr/kollogan_tiredserious.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan tsmiling", im.Flip(im.Scale(im.Crop("cr/kollogan_tiredsmiling.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan tsurprised", im.Flip(im.Scale(im.Crop("cr/kollogan_tiredsurprised.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan tthinking", im.Flip(im.Scale(im.Crop("cr/kollogan_tiredthinking.png",(100,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side logan tannoyed", im.Flip(im.Scale(im.Crop("cr/kollogan_tiredannoyed.png",(100,0,250,300)),250,300),horizontal=True))
            #Martin Side Images
            renpy.exports.image("side martin normal", im.Flip(im.Scale(im.Crop("cr/kolmartin_normal.png",(140,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side martin happy", im.Flip(im.Scale(im.Crop("cr/kolmartin_happy.png",(140,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side martin serious", im.Flip(im.Scale(im.Crop("cr/kolmartin_serious.png",(140,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side martin shocked", im.Flip(im.Scale(im.Crop("cr/kolmartin_shocked.png",(140,0,250,300)),250,300),horizontal=True))
            renpy.exports.image("side martin confused", im.Flip(im.Scale(im.Crop("cr/kolmartin_confused.png",(140,0,250,300)),250,300),horizontal=True))
            #Edmund Side Images
            renpy.exports.image("side edmund", im.Flip(im.Scale(im.Crop("cr/koledmund.png",(10,0,250,300)),250,300),horizontal=True))
            #Maverick Side Images
            renpy.exports.image("side maverick annoyed", im.Flip(im.Scale(im.Crop("cr/kolmav_annoyed.png",(0,0,500,600)),250,300),horizontal=True))
            renpy.exports.image("side maverick irritated", im.Flip(im.Scale(im.Crop("cr/kolmav_irritated.png",(0,0,500,600)),250,300),horizontal=True))
            renpy.exports.image("side maverick sad", im.Flip(im.Scale(im.Crop("cr/kolmav_sad.png",(0,0,500,600)),250,300),horizontal=True))
            renpy.exports.image("side maverick shock", im.Flip(im.Scale(im.Crop("cr/kolmav_shock.png",(0,0,500,600)),250,300),horizontal=True))



        #Searches for where the player would start the game on a normal playthrough
        ml.find_label("seccont") \
            .search_say("I awoke from uneasy dreams looking at an unfamiliar ceiling. Just for a moment, I wondered where I was before the events of last night all came back to me.", depth=800)


    def mod_complete(self):
        pass
