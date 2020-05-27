import os


def main():
    exten__catgo = {}
    os.chdir("FilesToSort")
    for f_name in os.listdir('.'):
        if os.path.isdir(f_name):
            continue

        exten = f_name.split('.')[-1]
        if exten not in exten__catgo:
            categories_ = input("What categories_ would you like to sort {} files into? ".format(exten))
            exten__catgo[exten] = categories_
            try:
                os.mkdir(categories_)
            except FileExistsError:
                pass

        os.rename(f_name, "{}/{}".format(exten__catgo[exten], f_name))


main()
