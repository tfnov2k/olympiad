# The script of the game goes in this file.
# image bg room = "bg room.jpeg"
# Declare characters used by this game. The color argument colorizes the
# name of the character.

define y = Character("Yeetus")
define a = Character("Alexandre")
define l = Character("0-shim-shim")
define s = Character("Stellaris")
define e = Character("Edhruvi")
define p = Character("Wise Philosopher")
define q = Character("Greek Translator")

transform elevated_center:
    xalign 0.5
    yalign 0.533

transform left_side:
    xalign 0.25  
    yalign 0.53   

transform right_side:
    xalign 0.75  
    yalign 0.53   


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg yeet
    with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    
    show yeet at elevated_center
    with dissolve

    # These display lines of dialogue.

    y "Chaire! I'm Yeetus"

    y "Welcome to the Greek Mathematics Olympiad, a most prestigious event that occurs once every 40 years"

    y "This competition embodies the spirit of ancient Greek mathematical tradition, emphasizing geometry, numerology and logical reasoning"

    y "This year, we have the honor of hosting four brilliant geniuses who have been selected as our exceptional competitors"

    y "The prize for our champion is truly extraordinary - a scholarship to the esteemed Pythagoras School of Mathematics"

    y "At this renowned institution, the victor will have the opportunity to study philosophy, mathematics, science and mysticism under the guidance of the great Pythagoras himself"

    y "Remember, in the words of Pythagoras: Number is the ruler of forms and ideas, and the cause of gods and demons! May your minds be sharp and your calculations precise"

    show yeet happy at elevated_center
    with dissolve
    
    y "Kali tychi! Good luck to all our competitors. May the most worthy mathematician emerge victorious"
    
    hide yeet
    scene bg menu1
    with fade

    $ renpy.notify("It is Hour-H of Day-D")

    show yeet at elevated_center
    with dissolve

    y "Esteemed guests and fellow mathematicians, I shall now unveil to you our illustrious contenders"

    scene bg alex
    with fade
    show yeet at left_side
    with dissolve
    show alex at right_side
    with dissolve

    y "This is Alexandre, the warrior-scholar of the Strigerius Clan, from Gaul, France"

    hide yeet
    show alex at elevated_center
    with dissolve

    a "Bonjour"

    a "I understand the parabolic trajectory of arrows and javelins and I apply Greek geometry to battlefield strategy"

    a "My goal is to earn honor through both intelligence and combat skills"

    hide alex
    scene bg larme
    with fade
    show yeet at left_side
    with dissolve
    show larme at right_side 
    with dissolve

    y "This is O-shim-shim, a brilliant and respected war strategist from Seres, China"

    hide yeet
    show larme at elevated_center
    with dissolve

    l "Wang jun an"

    l "I am an advisor to the military general. I see war like a chessboard, planning multiple moves ahead"

    l "I learned Greek cipher techniques to encode messages for war councils"

    l "I wish to teach Greek generals the tactic of feigning weakness to lure overconfident troops of Romans into a trap"

    hide larme
    scene bg seira
    show yeet at left_side
    with dissolve
    show seira at right_side
    with dissolve

    y "This is Stellaris, a wise astronomer from Magna Graecia, Italia"

    hide yeet
    show seira at elevated_center
    with dissolve

    s "Ais"
    
    s "I love stargazing"

    s "My drudic knowledge has given me insights into lunar cycles and star navigation"

    s "My goal is to share my knowledge of Etruscan celestial observations, calendar systems and divination through the stars"

    s "I want to teach Greek sailors how to use the North Star (Polaris) for navigation"

    hide seira
    scene bg eviru
    with fade
    show yeet at left_side
    with dissolve
    show eviru at right_side 
    with dissolve

    y "This is Edhruvi, a poet-sage from Taprobane, Sri Lanka"

    hide yeet
    show eviru at elevated_center
    with dissolve

    e "Ayubovan"
    
    e "Maths is poetry"

    e "I express my ideas in a metaphorical language, replying in riddles because I believe that equations reveal the rhythm of existence"

    e "You may often see me scribbling equations in the sand, composing verses about nature and the heavens..."

    e "...and debating the Greek philosophers about the deeper meaning of mathematics"

    hide edhruvi
    scene bg hall1
    with fade
    show yeet at elevated_center
    with dissolve

    y "Choose your character"
    hide yeet

    menu:

        "Choose your character"

        "Alexandre, the brave warrior-scholar":

            jump alexandre

        "O-shim-shim, the genius war-strategist":

            jump oshimshim

        "Stellaris, the wise astronomer":

            jump stellaris

        "Edhruvi, the brilliant poet-sage":

            jump edhruvi


label alexandre:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    p "Πόσα τρίγωνα ἔχει τὸ ἑξάγωνον"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "How many triangles does a hexagon have?"

    hide philosopher1

    menu:

        "How many triangles does a hexagon have?"
        
        "4":

            jump bad_ending

        "6":

            jump good_ending

        "8":

            jump bad_ending

label stellaris:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    p "Πόσας γραμμὰς συμμετρίας ἔχει τὸ ἰσόπλευρον τρίγωνον"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "How many lines of symmetry does an equilateral triangle have?"

    hide philosopher1

    menu:

        "How many lines of symmetry does an equilateral triangle have?"
        
        "1":

            jump bad_ending

        "3":

            jump good_ending

        "infinite":

            jump bad_ending

label oshimshim:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    p "Τίς ἐστιν ὁ ἑπόμενος ἀριθμὸς ἐν τῇ ἀκολουθίᾳ: α΄, α΄, β΄, γ΄, ε΄, η΄, ..."

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "What is the next number in the sequence: 1, 1, 2, 3, 5, 8, ...?"

    hide philosopher1

    menu:

        "How many triangles does a hexagon have?"
        
        "9":

            jump bad_ending

        "13":

            jump good_ending

        "15":

            jump bad_ending

label edhruvi:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    p "Τί ἐστι τὸ ἐμβαδὸν ὀρθογωνίου μῆκος ἓξ καὶ πλάτος τέτταρα ἔχοντος"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "What is the area of a rectangle with length 6 and width 4?"

    hide philosopher1

    menu:

        "What is the area of a rectangle with length 6 and width 4?"
        
        "12":

            jump bad_ending

        "24":

            jump good_ending

        "32":

            jump bad_ending

label good_ending:

    # Add a line to indicate the end of the game
    "Good ending."

    # Use the return statement to end the game
    return

label bad_ending:

    # Add a line to indicate the end of the game
    "Bad ending."

    # Use the return statement to end the game
    return

