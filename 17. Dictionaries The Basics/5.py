sport_team_rosters = {
    "New England Patriots": ["Tom Brady", "Rob Gronkowski", "Julian Edelman"],
    "New York Giants": ["Eli Manning", "Odell Beckham"]
}

sport_team_rosters["Pittsburgh Steelers"] = ["Ben Roethlisberger", "Antonio Brown"]
# print(sport_team_rosters)

sport_team_rosters["New York Giants"] = ["Eli Manning"]
# print(sport_team_rosters)


video_games_options = {}
# video_games_options = dict()

video_games_options["subtitle"] = True
video_games_options["difficulty"] = "Medium"
video_games_options["volume"] = 7
# print(video_games_options)

video_games_options["difficulty"] = "Hard"
video_games_options["subtitle"] = False
video_games_options["volume"] = 10


print(video_games_options)

words = ["danger", "beware", "danger"]

def count_words(words):
    counts = {}
    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts

print(count_words(words))
{"danger": 2, "beware": 1}