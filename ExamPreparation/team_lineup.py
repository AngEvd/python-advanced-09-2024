def team_lineup(*args):
    result = ""
    players = {}
    for arg in args:
        if arg[1] not in players:
            players[arg[1]] = []
        players[arg[1]].append(arg[0])

    sorted_players = dict(sorted(players.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for key, value in sorted_players.items():
        result += f"{key}:\n"
        for val in value:
            result += f"  -{val}\n"

    return result


print(team_lineup(
   ("Harry Kane", "England"),
   ("Manuel Neuer", "Germany"),
   ("Raheem Sterling", "England"),
   ("Toni Kroos", "Germany"),
   ("Cristiano Ronaldo", "Portugal"),
   ("Thomas Muller", "Germany"),
   ("Bruno Fernandes", "Portugal"),
   ("Bernardo Silva", "Portugal"),
   ("Harry Maguire", "England")))


