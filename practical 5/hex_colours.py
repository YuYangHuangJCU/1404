COLOUR_CODES = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7",
                "AntiqueWhite1": "#ffefdb", "AntiqueWhite2": "#eedfcc",
                "AntiqueWhite3": "#cdc0b0", "AntiqueWhite4": "#8b8378",
                "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6",
                "aquamarine4": "#458b74", "azure1": "#f0ffff"}
c_name = input("Please enter a colour name: ")
while c_name != "":
    print("The code for {} is {}".format(c_name,COLOUR_CODES.get(c_name)))
    c_name = input("Please enter a colour name: ")