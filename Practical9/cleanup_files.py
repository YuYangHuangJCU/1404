import os


def main():
    os.chdir('Lyrics')
    for d_name, sb_dir, f_name in os.walk('.'):
        for filename in f_name:
            new_name = get_fixed_filename(filename)
            print("Renaming {} to {}".format(filename, new_name))

            full_name = os.path.join(d_name, filename)
            new_name = os.path.join(d_name, new_name)
            os.rename(full_name, new_name)


def get_fixed_filename(filename):
    name = filename.replace(" ", "_").replace(".TXT", ".txt")
    """Changing file extension"""
    return name


main()
