lines = open("in.txt").read().split("\n")

sum=0
for line in lines:
    max_cubes = {"red" : 0, "green" : 0, "blue" : 0}

    game_id, games = line.split(': ')
    game_id = game_id.split(' ')[1]
    games = games.split('; ')
    for i in range(len(games)):
        tuples = games[i].split(', ')
        for tuple in tuples:
            num,color = tuple.split(' ')
            if int(num) > max_cubes[color]:
                max_cubes[color] = int(num)
    power = 1
    for val in max_cubes.values():
        power = power * val
    sum = sum + power
    #print(max_cubes)
print(sum)