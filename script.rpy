# Study Buddy (draft name)
# Drafts and ideas for a studying helper game
# Initial ideas:
#       - Adding your module names and chapters to a database
#       - Being able to tick off when completed
#       - Each completed, increases the pet and/or plant's health (tamagochi style maybe)
#       - Ability to switch module and/or lessons at will, saving progress ongoing throughout
#       - Maybe opening quiz to what you prefer? Animal or plant growth on completion?

# VARIABLES
# Study Buddy is the name of our main character
define sb = Character("Study Buddy")

# Module name part of game (naming your current study module, eg "Maths 101")
default module_name = "Unnamed Module"
# Chapters of said module
default chapters = []
default completed_chapters = []
default max_chapters = 10

# Study Buddy / plant growth
default plant_growth = 0

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




label add_chapter:

    while len(chapters) < max_chapters:

        $ chapter = renpy.input(
            "Enter a chapter/topic, or leave blank when you're finished:"
        )
        $ chapter = chapter.strip()

        # If player leaves it blank, auto know they've added all chapters
        # and jump to studying menu
        if chapter == "":
            jump study_menu

        $ chapters.append(chapter)

        "Added [chapter]!"

        if len(chapters) >= max_chapters:
            "You've reached the maximum of [max_chapters] chapters."
            jump study_menu

    jump study_menu


label study_menu:

    if not chapters:
        "You haven't added any chapters yet!"
        return

    python:
        available_chapters = [
            chapter for chapter in chapters
            if chapter not in completed_chapters
        ]

    if not available_chapters:
        "You've completed everything for this module!"
        return

    $ choice = renpy.display_menu(
        [(chapter, chapter) for chapter in available_chapters]
    )

    $ current_chapter = choice
    jump study_session

label study_session:

    sb "Time to work on [current_chapter]!"

    menu:
        "Finish studying":

            $ completed_chapters.append(current_chapter)
            $ plant_growth += 10

            sb "Nice work!"
            sb "Your plant grew a little!"

            jump plant_screen



label plant_screen:
    "plant screen here"




    return
