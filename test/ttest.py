def abbrev_name(string):
    splited_string = string.split(" ")
    name = splited_string[0]
    surname = splited_string[1]
    return name[0].upper() + "." + surname[0].upper()






print (abbrev_name("akaki sixarulidze"))