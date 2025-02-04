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
    yalign 0.533   

transform right_side:
    xalign 0.75  
    yalign 0.533   

# The game starts here.

label start:

    play music "greek_music.mp3"

    scene bg odeon
    with fade

    "Welcome to the Odeon of Herodes Atticus Amphitheatre, found in the Acropolis of Athens, Greece"

    scene bg yeet
    with fade
    
    show yeet at elevated_center
    with dissolve

    y "Chaire! I'm Yeetus"

    y "Welcome to the Greek Mathematics Olympiad, a most prestigious event that occurs once every 50 years"

    y "This competition embodies the spirit of ancient Greek mathematical tradition, emphasizing geometry, numerology and logical reasoning"

    y "This year, we have the honor of hosting four brilliant geniuses who have been selected as our exceptional competitors"

    y "The prize for our champion is truly extraordinary - a scholarship to the esteemed Pythagoras School of Mathematics"

    y "At this renowned institution, the victor will have the opportunity to study philosophy, mathematics, science and mysticism under the guidance of the great Pythagoras himself"

    y "Remember, in the words of Pythagoras: Number is the ruler of forms and ideas, and the cause of gods and demons! May your minds be sharp and your calculations precise"

    show yeet happy at elevated_center
    with dissolve
    
    y "Kali tychi! Good luck to all our competitors. May the most worthy mathematician emerge victorious"
    
    hide yeet
    scene bg menu2
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

    p "{font=DejaVuSans.ttf}Πόσα τρίγωνα ἔχει τὸ ἑξάγωνον{/font}"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "How many triangles does a hexagon have?"

    hide philosopher1

    menu:

        "How many triangles does a hexagon have?"
        
        "4":

            jump bad_ending_alexandre

        "6":

            jump good_ending_alexandre

        "8":

            jump bad_ending_alexandre

label stellaris:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    "{font=DejaVuSans.ttf}Πόσας γραμμὰς συμμετρίας ἔχει τὸ ἰσόπλευρον τρίγωνον{/font}"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "How many lines of symmetry does an equilateral triangle have?"

    hide philosopher1

    menu:

        "How many lines of symmetry does an equilateral triangle have?"
        
        "1":

            jump bad_ending_stellaris

        "3":

            jump good_ending_stellaris

        "infinite":

            jump bad_ending_stellaris

label oshimshim:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    "{font=DejaVuSans.ttf}Τίς ἐστιν ὁ ἑπόμενος ἀριθμὸς ἐν τῇ ἀκολουθίᾳ: α΄, α΄, β΄, γ΄, ε΄, η΄, ...{/font}"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "What is the next number in the sequence: 1, 1, 2, 3, 5, 8, ...?"

    hide philosopher1

    menu:

        "What is the next number in the sequence: 1, 1, 2, 3, 5, 8, ...?"
        
        "9":

            jump bad_ending_oshimshim

        "13":

            jump good_ending_oshimshim

        "15":

            jump bad_ending_oshimshim

label edhruvi:

    scene bg hall2
    with fade
    show philosopher2 at elevated_center
    with dissolve

    p "Here is your question -"

    "{font=DejaVuSans.ttf}Τί ἐστι τὸ ἐμβαδὸν ὀρθογωνίου μῆκος ἓξ καὶ πλάτος τέτταρα ἔχοντος{/font}"

    hide philosopher2
    show philosopher1 at elevated_center
    with dissolve

    q "Let me translate that for you"

    q "What is the area of a rectangle with length 6 and width 4?"

    hide philosopher1

    menu:

        "What is the area of a rectangle with length 6 and width 4?"
        
        "12":

            jump bad_ending_edhruvi

        "24":

            jump good_ending_edhruvi

        "32":

            jump bad_ending_edhruvi

label good_ending_alexandre:

    show alex at elevated_center
    with dissolve

    a "W-w-we made it?"

    hide alex 
    show alex happy at elevated_center
    with dissolve

    a "My clan back home is going to be so proud of me. I might even be made leader of the Strigerius clan now"

    a "I shall celebrate by treating everyone in the Ampitheatre with one bottle of red wine"

    hide eviru

    "Good ending."

    jump end_screen

    return

label bad_ending_alexandre:

    show alex at elevated_center
    with dissolve

    a "What just happened? That cannot be right"

    hide alex
    show alex angry at elevated_center
    with dissolve

    a "I am a disappointment to the Strigerius clan"

    a "Had father been here, he would have claimed that I am just another one of his adopted sons and not one of his own blood"

    hide alex

    "Bad ending."

    jump end_screen

    return

label good_ending_oshimshim:

    show larme at elevated_center
    with dissolve

    l "We did it?"

    hide larme 
    show larme happy at elevated_center
    with dissolve

    l "This is the beginning of something magnificent, I am calling it"

    l "In honor of my win, I shall gift you all some mind-challenging board games I brought from Seres, China"

    hide larme

    "Good ending."

    jump end_screen

    return

label bad_ending_oshimshim:

    show larme at elevated_center
    with dissolve

    l "Surely it cannot be"

    hide larme
    show larme angry at elevated_center
    with dissolve

    l "I might have been overconfident in my answer"

    l "I request you all to not make today change your mind about how wise Chinesemen can be. I am better than this"

    hide larme

    "Bad ending."

    jump end_screen

    return

label good_ending_stellaris:

    show seira at elevated_center
    with dissolve

    s "I got it"

    hide seira 
    show seira happy at elevated_center
    with dissolve

    s "Deep down, I always knew I had it in me"

    s "I shall ship some sweets and treats to my little sister Stella Luna who looks up to me"

    hide seira

    "Good ending."

    jump end_screen
    
    return

label bad_ending_stellaris:

    show seira at elevated_center
    with dissolve

    s "Oh no, I missed"

    hide seira
    show seira angry at elevated_center
    with dissolve

    s "I did not give it enough thought"

    s "I will only come back stronger. I must not show weakness in front of my sister, Stella Luna"

    hide seira

    "Bad ending."

    jump end_screen

    return

label good_ending_edhruvi:

    show eviru at elevated_center
    with dissolve

    e "No wonder I'm right"

    hide eviru 
    show eviru happy at elevated_center
    with dissolve

    e "There was no doubt about it"

    e "There shall be a grand march with men playing the Kymbala and the Syrinx, from the Amphitheatre to the city centre in honor of me winning"

    hide eviru

    "Good ending."

    jump end_screen

    return

label bad_ending_edhruvi:

    show eviru at elevated_center
    with dissolve

    e "No-no-no"

    hide eviru
    show eviru angry at elevated_center
    with dissolve

    e "I was wronged"

    e "I request you to give me another chance, or invite me again in 50 years, I beg"

    hide eviru

    "Bad ending."

    jump end_screen

    return

label end_screen:

    show bg end
    with fade

    "The end."

    "This is a work of fiction. Any resemblance to any character, living or dead, or to actual events is purely coincidental."

    "Made by Yeetus"


