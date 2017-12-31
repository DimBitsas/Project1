import csv


def skill_groups():
    # Read csv file and create a list of experience and inexperience players
    with open('soccer_players.csv', newline='') as csvfile:
        players = csv.DictReader(csvfile, delimiter=',')

        for row in players:
            temp_list = []
            # We do not need height in our output file
            del row['Height (inches)']
            if row['Soccer Experience'] == 'YES':
                for value in row.values():
                    temp_list.append(value)
                exp.append(temp_list)
            else:
                for value in row.values():
                    temp_list.append(value)
                ine.append(temp_list)


def split_players():
    # Split exp and ine groups to the three teams

    while exp:
        # Avoid pop from empty list
        if exp:
            dragons.append(exp.pop())
        if exp:
            sharks.append(exp.pop())
        if exp:
            raptors.append(exp.pop())

    while ine:
        # Avoid pop from empty list
        if ine:
            dragons.append(ine.pop())
        if ine:
            sharks.append(ine.pop())
        if ine:
            raptors.append(ine.pop())


def output_file():
    # Create the output file
    with open("teams.txt", "w") as file:
        file.write("DRAGONS\n")
        for player in dragons:
            file.write(", ".join(player))
            file.write("\n")
        file.write("\n")

        file.write("SHARKS\n")
        for player in sharks:
            file.write(", ".join(player))
            file.write("\n")
        file.write("\n")

        file.write("RAPTORS\n")
        for player in raptors:
            file.write(", ".join(player))
            file.write("\n")


if __name__ == '__main__':
    # Lists of experience and inexperience players
    exp = []
    ine = []
    # Lists of the three teams
    dragons = []
    sharks = []
    raptors = []

    skill_groups()
    split_players()
    output_file()
