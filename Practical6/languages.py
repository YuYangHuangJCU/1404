from CP1404.prac_06.programming_language import ProgrammingLanguage

# Main function


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [ python, visual_basic]  # Creating an array
    print("The dynamically typed languages are:")
    for language in languages:  # Selection combined with loop
        if language.is_dynamic():
            print(language.name)


# Selection
if __name__ == "__main__":
    main()
