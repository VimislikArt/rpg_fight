##  This code is just for reference!
##
##  If you place this code in ren'py, you will get errors, because it doesn't include any of the images,
##  but feel free to copy + paste any elements you'd like to use for your own turn-based combat engine!
##

init python:
    class fighter:
        def __init__(self, name, level = 1, max_hp = 10, hp = 10, max_mp = 4, mp = 4, initiative = 0, element = "None", element_attack = "Sword", attack = 0):
            self.name = name
            self.level = 1
            self.max_hp = max_hp
            self.hp = hp
            self.max_mp = max_mp
            self.mp = mp
            self.initiative = initiative
            self.element = element
            self.element_attack = element_attack
            self.attack = attack

label class_sample:
    $ p1 = fighter("Player 1")
    $ p2 = fighter("Player 2", 2, 12, 12, 8, 8)
    $ skeleton = fighter("Halberd Skeleton", 1, 12, 12, 0, 0)
    $ skeleton_fire = fighter("Fire Skeleton", 1, 12, 12, 0, 0, 0, "Fire", "Fire")
    $ skeleton_water = fighter("Water Skeleton", 1, 12, 12, 0, 0, 0, "Water", "Water")
    $ skeleton_grass = fighter("Grass Skeleton", 1, 12, 12, 0, 0, 0, "Grass", "Grass")

label sample:
    $ player_max_hp = 10
    $ player_hp = player_max_hp
    $ player_max_mp = 4
    $ player_mp = player_max_mp
    $ player_level = 1

    $ player2_max_hp = 12
    $ player2_hp = player2_max_hp
    $ player2_max_mp = 8
    $ player2_mp = player2_max_mp
    $ player2_level = 2

    $ player_current = 1
    $ player_element = "Sword"
    $ player_attack_value = 0

    $ enemy_max_hp = 12
    $ enemy_hp = enemy_max_hp
    $ enemy_fire_hp = enemy_max_hp
    $ enemy_water_hp = enemy_max_hp
    $ enemy_grass_hp = enemy_max_hp
    $ enemy_attack_value = 0
    $ enemy_element = "Halberd"
    $ enemies_turn = 0

label sample2:

    $ p1.hp -= 2


label camera_playerattack:
    camera:
        ease 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-657.0, -549.0, -9.0)*RotateMatrix(-9.0, 0.0, -9.0) 
        easeout 10.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-405.0, -684.0, 342.0)*RotateMatrix(0.0, -9.0, -9.0)
    return

label camera_knight_attack:
    show knight attack:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1539.0, 1017.0, 288.0)*RotateMatrix(0.0, 18.0, 0.0) 
        easeout 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(729.0, 1017.0, 288.0)*RotateMatrix(0.0, 18.0, 0.0) 

    show skeleton hit

    camera:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-405.0, -684.0, 99.0)*RotateMatrix(0.0, 9.0, 0.0) 
        easein 0.2 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1368.0, -684.0, -279.0)*RotateMatrix(-9.0, -9.0, 0.0) 
        easein 10.0 subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1395.0, -702.0, -252.0)*RotateMatrix(0.0, -9.0, 0.0) 
    return

label camera_knight_win:
    camera:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-504.0, -702.0, -189.0)*RotateMatrix(9.0, 0.0, 0.0) 
        easein 10.0 subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-504.0, -702.0, 72.0)*RotateMatrix(9.0, 0.0, 0.0) 
    return

label camera_skeleton_attack:
    show skeleton attack:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(981.0, 774.0, 351.0)*RotateMatrix(0.0, -18.0, 0.0)
        easeout 1.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2016.0, 774.0, 351.0)*RotateMatrix(0.0, -18.0, 0.0) 
    show knight hit
    $ player_hp -= 2
    camera:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1395.0, -702.0, -252.0)*RotateMatrix(0.0, -9.0, 0.0) 
        easein 0.2  matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-504.0, -702.0, 45.0)*RotateMatrix(-9.0, 0.0, 0.0) 
        easein 10.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-504.0, -702.0, 189.0)*RotateMatrix(-9.0, 0.0, 0.0) 
    return

label camera_knight_died:
    camera:
        subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1503.0, -621.0, 117.0)*RotateMatrix(369.0, 9.0, 0.0) 
        easein 0.1 subpixel True matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-1503.0, -621.0, 558.0)*RotateMatrix(369.0, 9.0, 0.0)
    return

image knight2 idle:
    "images/knight idle1.png"
    pause 1.0
    "images/knight idle2.png"
    pause 1.0
    repeat

image knight idle:
    "images/knight idle1.png"
    pause 1.0
    "images/knight idle2.png"
    pause 1.0
    repeat

image knight attack:
    "images/knight attack1.png"
    pause 0.3
    "images/knight attack2.png"
    pause 2.0
    "knight idle"

image knight2 attack:
    "images/knight attack1.png"
    pause 0.3
    "images/knight attack2.png"
    pause 2.0
    "knight idle"

image knight hit:
    "images/knight_hit.png"
    pause 1.0
    "knight idle"
image knight2 hit:
    "images/knight_hit.png"
    pause 1.0
    "knight idle"

image skeleton idle:
    "images/skeleton idle1.png"
    pause 1.0
    "images/skeleton idle2.png"
    pause 1.0
    repeat

image skeleton_fire idle:
    "images/skeleton idle1.png"
    pause 1.0
    "images/skeleton idle2.png"
    pause 1.0
    repeat

image skeleton_water idle:
    "images/skeleton idle1.png"
    pause 1.0
    "images/skeleton idle2.png"
    pause 1.0
    repeat

image skeleton_grass idle:
    "images/skeleton idle1.png"
    pause 1.0
    "images/skeleton idle2.png" 
    pause 1.0
    repeat

image skeleton attack:
    "images/skeleton attack1.png"
    pause 0.3
    "images/skeleton attack2.png"
    pause 2.0
    "skeleton idle"
image skeleton_fire attack:
    "images/skeleton attack1.png"
    pause 0.3
    "images/skeleton attack2.png"
    pause 2.0
    "skeleton idle"
image skeleton_water attack:
    "images/skeleton attack1.png"
    pause 0.3
    "images/skeleton attack2.png"
    pause 2.0
    "skeleton idle"
image skeleton_grass attack:
    "images/skeleton attack1.png"
    pause 0.3
    "images/skeleton attack2.png"
    pause 2.0
    "skeleton idle"

image skeleton hit:
    "images/skeleton_hit.png"
    pause 1.0
    "skeleton idle"
image skeleton_grass hit:
    "images/skeleton_hit.png"
    pause 1.0
    "skeleton idle"
image skeleton_fire hit:
    "images/skeleton_hit.png"
    pause 1.0
    "skeleton idle"
image skeleton_water hit:
    "images/skeleton_hit.png"
    pause 1.0
    "skeleton idle"


# Random Number Generator
label dice_roll:
    $ d4 = renpy.random.randint(1, 4)
    $ d6 = renpy.random.randint(1, 6)
    $ d10 = renpy.random.randint(1, 10)
    $ d20 = renpy.random.randint(1, 20)
    return

label start:

    hide black

label camera_action:

    camera:
        perspective True
        gl_depth True
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-162.0, -603.0, -162.0)*RotateMatrix(0.0, 0.0, 0.0) 
        easeout 0.5 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-972.0, -450.0, -909.0)*RotateMatrix(0.0, 0.0, 0.0) 

    scene bg:
        matrixtransform ScaleMatrix(1.7, 1.65, 1.0)*OffsetMatrix(0.0, -144.0, -1638.0)*RotateMatrix(0.0, 0.0, 0.0) 
    show tower:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(3330.0, 684.0, -423.0)*RotateMatrix(0.0, 0.0, 0.0) 
    show ceiling:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, -351.0, 270.0)*RotateMatrix(-72.0, 0.0, 0.0)
    show middle at reset 
    show floor:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 1296.0, 297.0)*RotateMatrix(72.0, 0.0, 0.0) 
    show knight idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(729.0, 1017.0, 288.0)*RotateMatrix(0.0, 18.0, 0.0) 
    show skeleton idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2016.0, 774.0, 351.0)*RotateMatrix(0.0, -18.0, 0.0) 
    
    $ renpy.pause(0.5, hard='True')
    
    camera:
        ease 5.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-972.0, -450.0, -909.0)*RotateMatrix(0.0, -9.0, 0.0) 
        ease 5.0 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(-972.0, -450.0, -909.0)*RotateMatrix(0.0, 0.0, 0.0)
        repeat

    # Player Stats
    $ player_max_hp = 10
    $ player_hp = player_max_hp

    # Enemy Stats
    $ enemy_max_hp = 6
    $ enemy_hp = enemy_max_hp

    menu:
        "Simplest Battle Engine":
            jump simple_battle
        "Simplest Battle Engine (With Graphics)":
            jump simple_battle_graphics
        "Slightly Harder Version of the Battle":
            jump harder_battle
        "WARNING!  REALLY COMPLICATED BATTLE!  WARNING!":
            jump complicated_battle
        "play that zoom in animation again!":
            camera:
                perspective True
                gl_depth True
            jump camera_action
    return

## SIMPLE BATTLE

label simple_battle:
    camera:
        perspective True
        gl_depth True
        matrixtransform ScaleMatrix(1.7, 1.65, 1.0)*OffsetMatrix(0.0, -90.0, -2205.0)*RotateMatrix(0.0, 0.0, 0.0) 

    scene bg:
        matrixtransform ScaleMatrix(1.7, 1.65, 1.0)*OffsetMatrix(0.0, -144.0, -1638.0)*RotateMatrix(0.0, 0.0, 0.0) 
    hide tower
    hide ceiling
    hide middle
    hide floor
    hide knight idle
    hide skeleton idle

    $ player_hp = 10
    $ enemy_hp = 6

    while player_hp > 0:

        # Player Turn

        menu:
            "Attack":
                $ enemy_hp -= 2
                "That's a strong hit!  Enemy has [enemy_hp] hp!"
                if enemy_hp <= 0:
                    "You win the combat encounter!"
                    jump simple_end
            "Don't Attack":
                "You don't attack..."

        # Enemy Turn
        $ player_hp -= 2
        "The Enemy makes an attack, reducing you to [player_hp] hp!"

    "You died..."

    menu simple_end:
        "Play this level again?":
            jump simple_battle
        "Back to Main Menu":
            jump start

## SIMPLE BATTLE WITH GRAPHICS

label simple_battle_graphics:

    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp

    show screen hp_bars_1v1

    while player_hp > 0:

        # Player Turn
        call camera_playerattack
        menu:
            "Attack":
                call camera_knight_attack
                $ enemy_hp -= 2
                "That's a strong hit!  Enemy has [enemy_hp] hp!"

                if enemy_hp <= 0:
                    call camera_knight_win
                    "You win the combat encounter!"
                    jump simple_graphic
            "Don't Attack":
                "You don't attack..."

        # Enemy Turn
        call camera_skeleton_attack
        "The Enemy makes an attack, reducing you to [player_hp] hp!"

    call camera_knight_died
    "You died..."

    hide screen hp_bars_1v1
    menu simple_graphic:
        "Play this level again?":
            jump simple_battle_graphics
        "Back to Main Menu":
            jump start
                
## HARDER BATTLE

label harder_battle:

    $ player_hp = player_max_hp
    $ enemy_hp = enemy_max_hp
    $ player_attack_value = 0

    show screen hp_bars_1v1

    while player_hp > 0 and enemy_hp > 0:

        # Player Turn - two choices!
        call dice_roll

        menu:
            "Light Attack":
                call camera_knight_attack
                if d10 >= 8:                                                # 30%
                    $ player_attack_value = d4 + d6
                    $ enemy_hp -= player_attack_value
                    "Critical Hit!  [player_attack_value] damage!"          # 70%
                else:
                    $ enemy_hp -= d4
                    "[d4] damage!"
            "Heavy Attack":
                call camera_knight_attack                       
                if d10 >= 9:                                                # 20%
                    $ player_attack_value = (d6 + d4)*2
                    $ enemy_hp -= player_attack_value
                    "Critical Hit!  You hit for [player_attack_value] damage!"
                elif d10 >= 5:                                              # 40%  
                    $ player_attack_value =  d6 + 2                                        
                    $ enemy_hp -= player_attack_value
                    "That's a strong hit!  Enemy takes [player_attack_value] hp!"
                else:                                                       # 40% 
                    "You miss!"                                      
        
        if enemy_hp <= 0:
            call camera_knight_win
            "You win the combat encounter!"
            jump harder_menu

        # Enemy Turn - Semi-randomized behavior!

        call dice_roll

        if d20 >= 19:                                            # 20%       
            call camera_skeleton_attack                                                                                
            $ player_hp -= d10
            "The Enemy makes a wild attack for [d10] damage!"
        elif d20 <=2:                                            # 20%
            $ enemy_hp += d4
            if enemy_hp < enemy_max_hp:
                "The Enemy heals itself, raising [d4] hp!"
            else:
                $ enemy_hp = enemy_max_hp
                "The Enemy fully heals itself back to full hp!"
        else:                                                    # 60%
            call camera_skeleton_attack                                                                                
            $ player_hp -= d4
            "The Enemy attacks for [d4] damage!"

    call camera_knight_died
    "You died..."
    hide screen hp_bars_1v1

    menu harder_menu:
        "Play this level again?":
            $ player_hp = player_max_hp
            $ enemy_hp = enemy_max_hp
            jump harder_battle
        "Back to Main Menu":
            jump start

## COMPLICATED BATTLE

label complicated_battle:
    # Player Stats
    $ player_max_hp = 10
    $ player_hp = player_max_hp
    $ player_max_mp = 4
    $ player_mp = player_max_mp
    $ player_level = 1

    $ player2_max_hp = 12
    $ player2_hp = player2_max_hp
    $ player2_max_mp = 8
    $ player2_mp = player2_max_mp
    $ player2_level = 2

    $ player_current = 1
    $ player_element = "Sword"
    $ player_attack_value = 0

    # Enemy Stats
    $ enemy_max_hp = 12
    $ enemy_hp = enemy_max_hp
    $ enemy_fire_hp = enemy_max_hp
    $ enemy_water_hp = enemy_max_hp
    $ enemy_grass_hp = enemy_max_hp
    $ enemy_attack_value = 0
    $ enemy_element = "Halberd"
    $ enemies_turn = 0

    show skeleton idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2016.0, 774.0, 351.0)*RotateMatrix(0.0, 0.0, 0.0) 
    show skeleton_fire idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(2223.0, 864.0, 423.0)*RotateMatrix(0.0, 0.0, 0.0) matrixcolor TintMatrix("#f00")
    show skeleton_grass idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1611.0, 750.0, 300.0)*RotateMatrix(0.0, 0.0, 0.0) matrixcolor TintMatrix("#00ff15")
    show skeleton_water idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(1818.0, 891.0, 459.0)*RotateMatrix(0.0, 0.0, 0.0) matrixcolor TintMatrix("#00eeff")
    show knight idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(729.0, 1017.0, 288.0)*RotateMatrix(0.0, 0.0, 0.0) 
    show knight2 idle:
        matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(576.0, 1044.0, 369.0)*RotateMatrix(0.0, 0.0, 0.0) matrixcolor TintMatrix("#8f7cd1")

    hide screen hp_bars_1v1
    show screen hp_bars_2v4


#################
    while True:

        # Player 1 Turn
        "Player 1's Turn!"
        if player_hp > 0:
            $ player_current = 1
            $ player_current_level = player_level
            call player_attack

        "Player 2's Turn!"
        # Player 2 Turn
        if player2_hp > 0:
            $ player_current = 2
            $ player_current_level = player2_level
            call player_attack
        
        # Enemies Turn

        "It's the skeleton's turn to attack!"
        while enemies_turn < 4:

            # Determines Enemy Turn

            if enemies_turn == 0 and enemy_hp > 0:
                $ enemy_element = "Halberd"
                call enemy_attack
            elif enemies_turn == 1 and enemy_fire_hp > 0:
                $ enemy_element = "Fire"
                call enemy_attack
            elif enemies_turn == 2 and enemy_water_hp > 0:
                $ enemy_element = "Water"
                call enemy_attack
            elif enemies_turn == 3 and enemy_grass_hp > 0:
                call enemy_attack
                $ enemy_element = "Grass"
            else:
                $ enemies_turn += 1
##########


menu complicated_menu:
    "Play this level again?":
        $ player_hp = player_max_hp
        $ enemy_hp = enemy_max_hp
        jump harder_battle
    "Back to Main Menu":
        hide skeleton_grass
        hide skeleton_fire
        hide skeleton_water
        hide knight2
        jump start

label player_attack:
    call dice_roll

    menu player_attack_choice:
        "Attack Halberd Skeleton!" if enemy_hp > 0:
            $ enemy_element = "Halberd"
        "Attack Fire Skeleton!" if enemy_fire_hp > 0:
            $ enemy_element = "Fire"
        "Attack Water Skeleton!" if enemy_water_hp > 0:
            $ enemy_element = "Water"
        "Attack Grass Skeleton!" if enemy_grass_hp > 0:
            $ enemy_element = "Grass"

    menu:
        "Sword Slash" if player_current == 1 or player_current == 2:
            $ player_element = "Sword"
            if d10 >= 8:                                                # 30%
                $ player_attack_value = d4 + d6 + player_current_level
                "Critical Hit!"
            elif d10 == 1:                                              # 10%
                $ player_attack_value = 0
                "You missed!"
            else:                                                       # 60%
                $ player_attack_value = d4 + player_current_level
        "Fire Spin - 2 MP" if player_current == 1 and player_mp > 0:
            $ player_mp -= 2
            $ player_element = "Fire"
            if d10 == 10:
                $ player_attack_value = d4 * 2 + d6 + player_current_level
                "Burn, baby!"
            else:
                $ player_attack_value = d4 + player_current_level
        "HydroSword - 3 MP" if player_current == 2 and player2_mp > 0:
            $ player2_mp -= 3
            $ player_element = "Water"
            if d10 == 10:                            
                $ player_attack_value = d4 * 2 + d6 + player_current_level
                "Splash!"
            else:                                 
                $ player_attack_value = d4 + player_current_level
        "Grass Blade - 3 MP" if player_current == 2 and player2_mp > 0:
            $ player2_mp -= 3
            $ player_element = "Grass"
            if d10 == 10:                           
                $ player_attack_value = d4 * 2 + d6 + player_current_level
                "Vine Whip!"
            else:                                 
                $ player_attack_value = d4 + player_current_level

    # Weakness + Resist
    if enemy_element == player_element:
        $ player_attack_value == round(player_attack_value*0.5)
    elif enemy_element == "Water" and player_element ==  "Grass":
        $ player_attack_value *= 3
    elif enemy_element == "Fire" and player_element ==  "Water":
        $ player_attack_value *= 3
    elif enemy_element == "Grass" and player_element ==  "Fire":
        $ player_attack_value *= 3

    # Transfer Damage
    if enemy_element == "Halberd":
        show skeleton hit
        $ enemy_hp -= player_attack_value
    if enemy_element == "Fire":
        show skeleton_fire hit
        $ enemy_fire_hp -= player_attack_value
    if enemy_element == "Water":
        show skeleton_water hit
        $ enemy_water_hp -= player_attack_value
    if enemy_element == "Grass":
        show skeleton_grass hit
        $ enemy_grass_hp -= player_attack_value

    # Communicate Damage
    if player_current == 2:
        show knight2 attack
    else:
        show knight attack
    "You dealt [player_attack_value] damage to the [enemy_element] Skeleton!"

    # Evaluate for Death
    if enemy_hp <= 0 and enemy_fire_hp <= 0 and enemy_water_hp <= 0 and enemy_grass_hp <= 0:
        hide screen hp_bars_2v4
        hide skeleton idle with dissolve
        hide skeleton_fire idle with dissolve
        hide skeleton_water idle with dissolve
        hide skeleton_grass idle with dissolve
        "You win the combat encounter!"
        jump complicated_menu
    elif enemy_hp <= 0 and enemy_element == "Halberd":
        hide skeleton idle with dissolve
        "Halberd Skeleton is defeated!"
    elif enemy_fire_hp <= 0 and enemy_element == "Fire":
        hide skeleton_fire idle with dissolve
        "Fire Skeleton is defeated!"
    elif enemy_hp <= 0 and enemy_element == "Water":
        hide skeleton_water idle with dissolve
        "Water Skeleton is defeated!"
    elif enemy_hp <= 0 and enemy_element == "Grass":
        hide skeleton_grass idle with dissolve
        "Grass Skeleton is defeated!"

    return

label enemy_attack:

    call dice_roll

    # Selects Player
    if player_hp > 0 and player2_hp > 0:
        if d20 > 10:
            $ player_current = 1
        else:
            $ player_current = 2
    elif player_hp > 0:
        $ player_current = 1
    else:
        $ player_current = 2

    # Attacks
    if d10 == 10:                                                                             
        $ enemy_attack_value = d6
        "The [enemy_element] Skeleton makes a wild attack at Player [player_current]!"
    elif d10 >= 1:
        $ enemy_attack_value = d4
        "The [enemy_element] Skeleton makes an attack at Player [player_current]!"
    else:
        "The [enemy_element] Skeleton attacks at Player [player_current]..."

    # Show Attacking Enemy
    if enemy_element == "Fire":
        show skeleton_fire attack
    elif enemy_element == "Halberd":
        show skeleton attack
    elif enemy_element == "Water":
        show skeleton_water attack
    elif enemy_element == "Grass":
        show skeleton_grass attack

    # Show hit Player
    if enemy_attack_value == 0:
        "...but misses!"
    elif player_current == 1:
        show knight hit
        $ player_hp -= enemy_attack_value
        "Player 1 takes [enemy_attack_value] damage!"
    elif player_current == 2:
        show knight2 hit
        $ player2_hp -= enemy_attack_value
        "Player 2 takes [enemy_attack_value] damage!"

    # Evaluates Death
    if player_current == 1 and player_hp <= 0:
        hide knight with dissolve
        "Player 1 defeated!"
    elif player_current == 2 and player2_hp <= 0:
        hide knight with dissolve
        "Player 2 defeated!"

    if player_hp <=0 and player2_hp <= 0:
        hide screen hp_bars_2v4
        "You lost..."
        jump complicated_menu

    $ enemies_turn += 1

    return

screen hp_bars_1v1:

    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "Player 1"
        bar value player_hp range player_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "Skeleton"
        bar value enemy_hp range enemy_max_hp

screen hp_bars_2v4:

    vbox:
        spacing 20
        xalign 0.1
        yalign 0.0
        xmaximum 600
        text "Player 1   -  Current MP: [player_mp]"
        bar value player_hp range player_max_hp
        text "Player 2   -  Current MP: [player2_mp]"
        bar value player2_hp range player2_max_hp
    vbox:
        spacing 20
        xalign 0.9
        yalign 0.0
        xmaximum 600
        text "Halberd Skeleton"
        bar value enemy_hp range enemy_max_hp

        text "Fire Skeleton"
        bar value enemy_fire_hp range enemy_max_hp

        text "Water Skeleton"
        bar value enemy_water_hp range enemy_max_hp

        text "Grass Skeleton"
        bar value enemy_grass_hp range enemy_max_hp