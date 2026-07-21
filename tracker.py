# ----------------------------------------------------
# Varsity Sports Performance Tracker
# Built by: [Your Name]
# ----------------------------------------------------

# 1. Define the player data (Variables and Lists)
player_name = "Captain"
points_scored = [18, 22, 14, 25, 16]  # Points from the last 5 basketball games

# 2. Create a function to calculate the scoring average
def calculate_scoring_average(game_scores):
    # 'sum' adds all the numbers together; 'len' counts how many games were played
    total_points = sum(game_scores)
    number_of_games = len(game_scores)
    
    # Calculate the statistical average
    average = total_points / number_of_games
    return average

# 3. Create a function to find the player's peak performance game
def find_highest_score(game_scores):
    # 'max' automatically hunts for the biggest number in our list
    highest = max(game_scores)
    return highest

# 4. Run the code and print the results to the screen
player_average = calculate_scoring_average(points_scored)
peak_game = find_highest_score(points_scored)

print("=== VARSITY SPORTS PERFORMANCE REPORT ===")
print("Player Name:", player_name)
print("Points Scored in Last 5 Games:", points_scored)
print("-----------------------------------------")
print("Season Scoring Average:", player_average, "points per game")
print("Peak Single-Game Performance:", peak_game, "points")
print("=========================================")

Initial copy of tracker script
