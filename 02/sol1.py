lines = open("in.txt").read().split("\n")

max_cubes = {"red" : 12, "green" : 13, "blue" : 14}
sum=0
for line in lines:
    game_id, games = line.split(': ')
    game_id = game_id.split(' ')[1]
    flag_game_invalid = False
    games = games.split('; ')
    for i in range(len(games)):
        tuples = games[i].split(', ')
        for tuple in tuples:
            num,color = tuple.split(' ')
            if int(num) > max_cubes[color]:
                flag_game_invalid = True
    if(flag_game_invalid):
        print("game", game_id, "invalid")
            #sum = sum + int(game_id)
    else:
        sum = sum + int(game_id)
print(sum)