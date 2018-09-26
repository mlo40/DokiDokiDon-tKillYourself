# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define -2 gui.hover_sound = "audio/hover.ogg"
define -2 gui.activate_sound = "audio/select.ogg"

define fade = Fade(0.5, 0.0, 0.5)
define fadehold = Fade(0.5, 1.0, 0.5)
define flash = Fade(0.1, 0.0, 0.5, color="#fff")

define y = Character("Yuri")
define m = Character("MUNIKA")
define s = Character("Sayori")
define se = Character("Sayori", kind=nvl)
define sp = Character("SPICYBOI")
define g = Character("[name]")
define e = Character("emils_gailis/the dev")
define TE = Character("TheErican")
define DB = Character("Dat Boi")


# The game starts here.

label start:
        
    python:
        
        name = renpy.input(_("What's your name?"))
        
        name = name.strip() or __("That BOI MC")

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
 

    scene bg room
    
    play music "audio/17654.ogg" fadein 10.0
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show monika:
        xalign 0.5
        yalign 0.0

    # These display lines of dialogue.

    m "[name] Hello faggot you sem to have woken up"
    
    g "what wrong with you i ant a faggot"
    
    m "nothing is wrong with me you're the one who downloaded this game if we can even call it that"

    m "any ways [name] i am her to show you how things work in this world cunt"
    
    show monika:
        xalign 0.-0.3
        yalign 0.0
    
    show yuri:
        xalign 0.5
        yalign 0.0
    
    y "munika somone killd sayori WITH MEMES"
    
    show saorry:
        xalign 1.5
        yalign 0.0
 
    
    s "what da fug you gays talking about"
    
    y "oh good your ok"
    
    s "you know i am barely hanging in by a thread"
    
    m "yuri i need to talk to you sayori tell him the shit he needs to know"
    
    s "for fucks sake"
    
    hide monika
    hide yuri
    
    show saorry:
        xalign 0.5
        yalign 0.0
        
    stop music   fadeout 3.0
    
    g "wtf yust hapend"
    
    s "doki doki yust hapend faggot any ways do you want to know sum \"information?\" of whats going on"
    
    nvl clear
    
label question:
    
    nvl clear
    
menu:
    
    s "wich do you choose"
    
    "yes":
        call yes from _call_yes
    
    "no":
        call no from _call_no
        
    "minigame":
        call minigame from _call_minigame
        
        nvl clear
        

label end_for_right_now:
    
    nvl clear
   
    show eyes
    
    e "hope you liked it my nibba [name] i will add more and
       ther might be a big update soon and it will change alot"
    
    # This ends the game.
    
    return