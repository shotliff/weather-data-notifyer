def makeFile():
    """
    Prompt users for the user variables
    :return:
    """
    # open/create config
    with open("settings/config.ini", "w") as file:
        # should probably figure out a way to verify the location is good
        loc = input("Location\n>")
        units = input("Unit: F/C\n>")
        while units.lower() not in ["f", "c"]:
            units = input("Unit: F/C\n>")
        interval = input("Notification Interval in Seconds\n>")
        while not interval.isdigit():
            interval = input("Notification Interval in Seconds\n>")


        if units.lower() == "f":
            units = "fahrenheit"
        else:
            units = "celcius"
        # We'll use split later, using hashes because am lazy
        file.write(f"{loc}#{units}#{interval}")
