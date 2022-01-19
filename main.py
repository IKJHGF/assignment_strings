# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line

# create a variable for every player that scored
scorer_goal_0 = 'Ruud Gullit'
scorer_goal_1 = 'Marco van Basten'

# create a variable of each minute of the match that a goal was scored in
goal_0 = 32
goal_1 = 54

# create a string that reports on who scored when using +
# format is <scorer_name> <when_they_scored>, <scorer_name> <when_they_scored>
f'{scorer_goal_0} {goal_0}, {scorer_goal_1} {goal_1}'

# store result in variable scorers
scorers = f'{scorer_goal_0} {goal_0}, {scorer_goal_1} {goal_1}'

# use + operator to create a single string with information about who scored when
# format is <scorer_name> scored in the <when_they_scored>nd minute
# format is <scorer_name> scored in the <when_they_scored>th minute
f"{scorer_goal_0} scored in the {goal_0}nd minute"
f"{scorer_goal_1} scored in the {goal_1}th minute"

# store result in variable report
# use '\n' to create a new line
report = f"{scorer_goal_0} scored in the {goal_0}nd minute" '\n' f"{scorer_goal_1} scored in the {goal_1}th minute"

# create a variable player (use the name of a player of the soccer match) and store his name as a string
player = 'Erwin Koeman'

# create first_name and use slicing to isolate the player's first name
player_first_name = player.split(" ", 1)
first_name = player_first_name[0]

# last_name_len > use find, slicing and len to find and store the last name of the player
last_name = player.split(" ", 1)
player_last_name = last_name[1]
last_name_len = len(player_last_name)

# name_short > isolate and store player's name in format E. Koeman
name_short = (player[0]) + '. ' + (player_last_name)

# chant > first_name! * x, x is number of characters in their first name (last character is not a space!)
number = len(first_name)
chant_plus_character = (first_name +'! ')*number
chant = chant_plus_character[:-1]
# good_chant
good_chant = True
x = 'good_chant' 
y = 'chant'
print(x != y)



