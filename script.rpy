# Study Buddy (draft name)
# Drafts and ideas for a studying helper game
# Initial ideas:
#       - Adding your module names and chapters to a database
#       - Being able to tick off when completed
#       - Each completed, increases the pet and/or plant's health (tamagochi style maybe)
#       - Ability to switch module and/or lessons at will, saving progress ongoing throughout
#       - Maybe opening quiz to what you prefer? Animal or plant growth on completion?
#       -

# VARIABLES
# Study Buddy is the name of our main character
define sb = Character("Study Buddy")

# Module name part of game (naming your current study module, eg "Maths 101")
default module_name = "Unnamed Module"

# The game starts here.
label start:
    scene studyhall
    sb "Welcome to Study Buddy!"
    # Naming our study module (eg "Maths 101")
    sb "What's the module you're studying called?"
    $ module_name = renpy.input("Enter the module name (for example: 'Maths 101'):")
    $ module_name = module_name.strip()

    if module_name == "":
        $ module_name = "module"

    "You named it [module_name]."

    sb "Sweet! This is your plant."
    show plant00 # Eventually a nice plant image
    sb "Whiles working on [module_name], your plant will grow and improve!"
    sb "Like all good plants, they take time to grow, so please don't rush through
    just to level it up quicker..."
    sb "A healthy plant takes time and effort, just like studying does."


    return
