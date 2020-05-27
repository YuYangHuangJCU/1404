import os


def main():
    os.chdir("FilesToSort")
    for f_name in os.listdir('.'):
        if os.path.isdir(f_name):
            continue
        exten_ = f_name.split('.')[-1]
        try:
            os.mkdir(exten_)
        except FileExistsError:
            pass
        print("{}/{}".format(exten_, f_name))
        os.rename(f_name, "{}/{}".format(exten_, f_name))


main()
