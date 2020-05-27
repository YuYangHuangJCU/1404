"""
CP1404/CP5632 Practical
Demos of various os module examples
"""
import os


def main():
    """Demo os module functions."""
    print("Start Dir is: {}".format(os.getcwd()))

    # Change to desired Dir
    os.chdir('Lyrics/Christmas')

    # Print a list of all files in current Dir
    print("Files are in {}:\n{}\n".format(os.getcwd(), os.listdir('.')))

    # Make a new Dir
    # The next time you run this, it will crash if the Dir exists
    # TODO: Use exception handling to avoid the crash (just pass)
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    # Loop through each file in the (current) Dir
    for filename in os.listdir('.'):
        # Ignore directories, just process files
        if os.path.isdir(filename):
            continue

        new_name = get_fixed_filename(filename)
        print("Renaming {} to {}".format(filename, new_name))

        # TODO: Try these options one at a time
        # Option 1: rename file to new name - in place
        # os.rename(filename, new_name)

        # Option 2: move file to new place, with new name
        # shutil.move(filename, 'temp/' + new_name)


def get_fixed_filename(filename):
    """Return a 'fixed' version of filename."""
    new_name = filename.replace(" ", "_").replace(".TXT", ".txt")
    return new_name


def demo_walk():
    """Process all sub_dir using os.walk()."""
    os.chdir('Lyrics')
    for Dir_name, sub_dir, f_names in os.walk('.'):
        print("Dir:", Dir_name)
        print("\tcontains sub_dir:", sub_dir)
        print("\tand files:", f_names)
        print("(Current working Dir is: {})".format(os.getcwd()))

        # TODO: add a loop to rename the files
        for filename in f_names:
            full_name = os.path.join(Dir_name, filename)
            new_name = os.path.join(Dir_name, get_fixed_filename(filename))
            os.rename(full_name, new_name)


main()
# demo_walk()
