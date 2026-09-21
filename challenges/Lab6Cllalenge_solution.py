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
