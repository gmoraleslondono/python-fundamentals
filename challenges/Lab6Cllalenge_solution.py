# Game Tournament Analytics System.

# Part 1 - Tournament data
players = [
    {"name": "  Carlos Martin ", "team": "Falcons", "country": "Spain", "score": 850, "matches": 12, "wins": 8, "active": True},
    {"name": "anna andersson", "team": "Tigers", "country": "sweden", "score": 720, "matches": 10, "wins": 6, "active": True},
    {"name": "JOHN SMITH", "team": "Eagles", "country": "USA", "score": 640, "matches": 11, "wins": 5, "active": True},
    {"name": "  Maria Rossi", "team": "Falcons", "country": "Italy", "score": 580, "matches": 9, "wins": 4, "active": False},
    {"name": "Peter Johnson ", "team": "tigers", "country": "United Kingdom", "score": 490, "matches": 8, "wins": 3, "active": True},
    {"name": "sofia garcia", "team": "EAGLES", "country": "spain", "score": 450, "matches": 7, "wins": 2, "active": True},
    {"name": "Lars  Nilsson", "team": "Falcons", "country": "SWEDEN", "score": 390, "matches": 10, "wins": 2, "active": False},
    {"name": "Emily Brown", "team": "Tigers", "country": "USA", "score": 310, "matches": 6, "wins": 1, "active": True},
    {"name": "  David Wilson  ", "team": "Eagles", "country": "usa", "score": 275, "matches": 5, "wins": 0, "active": True},
    {"name": "Laura Martinez", "team": "falcons", "country": "SPAIN", "score": 520, "matches": 8, "wins": 4, "active": True},
    {"name": "ERIK LARSSON", "team": "Tigers", "country": "Sweden", "score": 680, "matches": 13, "wins": 7, "active": False},
    {"name": "Nina Petrova ", "team": "eagles", "country": "Russia", "score": 360, "matches": 7, "wins": 2, "active": True},
    {"name": "Tom Wilson", "team": "Falcons", "country": "usa", "score": 230, "matches": 6, "wins": 0, "active": True},
    {"name": "  Julia Klein", "team": "TIGERS", "country": "Germany", "score": 760, "matches": 11, "wins": 7, "active": True},
    {"name": "michael lee", "team": "Eagles", "country": "South Korea", "score": 410, "matches": 9, "wins": 3, "active": False}
]

# Part 2 - Clean the player data
normalized_players = [{"name" : player["name"].strip().title(),
                      "team" : player["team"].strip().title(),
                      "country" : player["country"].strip().title(),
                      "score" : player["score"],
                      "matches" : player["matches"],
                     "wins" : player["wins"],
                      "active" : player["active"]}
                    for player in players]

# Part 3 - Filter the tournament

active_players = [player for player in normalized_players if player["active"]== True]

players_three_wins = [player for player in normalized_players if player["wins"] >= 3]

players_highest_score = [player for player in normalized_players if player["score"] >= 500]

players_from_sweden = [player for player in normalized_players if player["country"] == "Sweden"]

players_active_usa = [player for player in normalized_players if player["active"] == True and player["country"] == "Usa"]

# Part 4 - Tournament statistics

unique_countries = {players["country"] for players in normalized_players}

unique_teams = {player["team"] for player in normalized_players}

player_score = {player["name"]: player["score"] for player in normalized_players}

player_wins = {player["name"] : player["wins"] for player in normalized_players}

awesome_players = [player for player in normalized_players if player["score"] > 700]


# Part 5 - Combine tournament data

names = ['Carlos Martin', 'Anna Andersson', 'John Smith', 'Maria Rossi', 'Peter Johnson', 'Sofia Garcia', 'Lars Nilsson', 'Emily Brown', 'David Wilson', 'Laura Martinez', 'Erik Larsson', 'Nina Petrova', 'Tom Wilson', 'Julia Klein', 'Michael Lee']

ages = [30, 25, 26, 43, 22, 60, 45, 31, 25, 30, 23, 36, 48, 19, 55]

tshirt_sizes = ["M", "L", "S", "XL", "M", "L", "S", "M", "XXL", "L", "XL", "S", "M", "XXL", "L"]

players_extra_info = [{"name": name, "age": age, "size": size} for name, age, size in zip(names, ages, tshirt_sizes)]

players_tshirt = dict(zip(names, tshirt_sizes))

players_age = dict(zip(names, ages))

