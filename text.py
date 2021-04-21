import datetime

# current date as filename.
filename = datetime.datetime.now()

# create empty file
def create_file():

    with open(filename.strftime("%d %B %Y")+".txt", "w") as file:
        file.write("")

create_file()
