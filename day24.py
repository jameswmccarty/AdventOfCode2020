#!/usr/bin/python

"""

--- Day 24: Lobby Layout ---

Your raft makes it to the tropical island; it turns out that the small crab was an excellent navigator. You make your way to the resort.

As you enter the lobby, you discover a small problem: the floor is being renovated. You can't even reach the check-in desk until they've finished installing the new tile floor.

The tiles are all hexagonal; they need to be arranged in a hex grid with a very specific color pattern. Not in the mood to wait, you offer to help figure out the pattern.

The tiles are all white on one side and black on the other. They start with the white side facing up. The lobby is large enough to fit whatever pattern might need to appear there.

A member of the renovation crew gives you a list of the tiles that need to be flipped over (your puzzle input). Each line in the list identifies a single tile that needs to be flipped by giving a series of steps starting from a reference tile in the very center of the room. (Every line starts from the same reference tile.)

Because the tiles are hexagonal, every tile has six neighbors: east, southeast, southwest, west, northwest, and northeast. These directions are given in your list, respectively, as e, se, sw, w, nw, and ne. A tile is identified by a series of these directions with no delimiters; for example, esenee identifies the tile you land on if you start at the reference tile and then move one tile east, one tile southeast, one tile northeast, and one tile east.

Each time a tile is identified, it flips from white to black or from black to white. Tiles might be flipped more than once. For example, a line like esew flips a tile immediately adjacent to the reference tile, and a line like nwwswee flips the reference tile itself.

Here is a larger example:

sesenwnenenewseeswwswswwnenewsewsw
neeenesenwnwwswnenewnwwsewnenwseswesw
seswneswswsenwwnwse
nwnwneseeswswnenewneswwnewseswneseene
swweswneswnenwsewnwneneseenw
eesenwseswswnenwswnwnwsewwnwsene
sewnenenenesenwsewnenwwwse
wenwwweseeeweswwwnwwe
wsweesenenewnwwnwsenewsenwwsesesenwne
neeswseenwwswnwswswnw
nenwswwsewswnenenewsenwsenwnesesenew
enewnwewneswsewnwswenweswnenwsenwsw
sweneswneswneneenwnewenewwneswswnese
swwesenesewenwneswnwwneseswwne
enesenwswwswneneswsenwnewswseenwsese
wnwnesenesenenwwnenwsewesewsesesew
nenewswnwewswnenesenwnesewesw
eneswnwswnwsenenwnwnwwseeswneewsenese
neswnwewnwnwseenwseesewsenwsweewe
wseweeenwnesenwwwswnew

In the above example, 10 tiles are flipped once (to black), and 5 more are flipped twice (to black, then back to white). After all of these instructions have been followed, a total of 10 tiles are black.

Go through the renovation crew's list and determine which tiles they need to flip. After all of the instructions have been followed, how many tiles are left with the black side up?

Your puzzle answer was 330.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

The tile floor in the lobby is meant to be a living art exhibit. Every day, the tiles are all flipped according to the following rules:

    Any black tile with zero or more than 2 black tiles immediately adjacent to it is flipped to white.
    Any white tile with exactly 2 black tiles immediately adjacent to it is flipped to black.

Here, tiles immediately adjacent means the six tiles directly touching the tile in question.

The rules are applied simultaneously to every tile; put another way, it is first determined which tiles need to be flipped, then they are all flipped at the same time.

In the above example, the number of black tiles that are facing up after the given number of days has passed is as follows:

Day 1: 15
Day 2: 12
Day 3: 25
Day 4: 14
Day 5: 23
Day 6: 28
Day 7: 41
Day 8: 37
Day 9: 49
Day 10: 37

Day 20: 132
Day 30: 259
Day 40: 406
Day 50: 566
Day 60: 788
Day 70: 1106
Day 80: 1373
Day 90: 1844
Day 100: 2208

After executing this process a total of 100 times, there would be 2208 black tiles facing up.

How many tiles will be black after 100 days?


"""

valid_dirs = ('e', 'se', 'sw', 'w', 'nw', 'ne')

"""
  \ e  /
ne +--+ se
  /    \
-+      +-
  \    /
nw +--+ sw
  / w  \
"""

swaps = {"se, w" : "sw",
		 "w, se" : "sw",
		 "ne, se": "e",
		 "se, ne": "e",
		 "nw, sw": "w",
		 "sw, nw": "w",
		 "ne, w" : "nw",
		 "w, ne" : "nw",
		 "sw, e" : "se",
		 "e, sw" : "se",
		 "e, nw" : "ne",
		 "nw, e" : "ne"}

black_tiles = set()

def tokenize(line):
	tokens = []
	while len(line) > 0:
		if line[:2] in valid_dirs:
			tokens.append(line[:2])
			line = line[2:]
		else:
			tokens.append(line[0])
			line = line[1:]
	return tokens

def compress(tokens):
	compressed = []
	while len(tokens) > 0:
		trial = ', '.join(tokens[:2])
		if trial in swaps.keys():
			if swaps[trial] != '':
				compressed.append(swaps[trial])
			tokens = tokens[2:]
		else:
			compressed.append(tokens[0])
			tokens = tokens[1:]
	return compressed

def path_compress(path):
	# X = NE | SW
	# Y =  E | W
	# Z = SE | NW
	last_sum = 0
	while last_sum != sum(path.values()):
		last_sum = sum(path.values())
		# Cancel E and W
		m = min(path['e'],path['w'])
		path['e'] -= m
		path['w'] -= m
		# Cancel NE and SW
		m = min(path['ne'],path['sw'])
		path['ne'] -= m
		path['sw'] -= m
		# Cancel NW and SE
		m = min(path['nw'],path['se'])
		path['nw'] -= m
		path['se'] -= m
		# Compress NE + SE = E
		m = min(path['ne'],path['se'])
		path['e'] += m
		path['ne'] -= m
		path['se'] -= m
		# Compress NW + SW = W
		m = min(path['nw'],path['sw'])
		path['w'] += m
		path['nw'] -= m
		path['sw'] -= m
		# Compress SE + W = SW
		m = min(path['se'],path['w'])
		path['sw'] += m
		path['se'] -= m
		path['w'] -= m
		# Compress NE + W = NW
		m = min(path['ne'],path['w'])
		path['nw'] += m
		path['ne'] -= m
		path['w'] -= m
		# Compress SW + E = SE
		m = min(path['sw'],path['e'])
		path['se'] += m
		path['sw'] -= m
		path['e'] -= m
		# Compress NW + E = NE
		m = min(path['nw'],path['e'])
		path['ne'] += m
		path['nw'] -= m
		path['e'] -= m
	
	return path
	
def parse(line):
	tokens = tokenize(line)
	#tokens = compress(tokens)
	#last = float('inf')
	#while last != len(tokens):
	#	last = len(tokens)
	#	tokens = compress(tokens)
	path = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
	for t in tokens:
		path[t] += 1
	path = path_compress(path)
	path = ','.join(str(x) for x in path.values())
	if path in black_tiles:
		black_tiles.remove(path)
	else:
		black_tiles.add(path)

def count_adjacent(path):
	count = 0
	start_loc = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
	path = [ int(x) for x in path.split(",") ]
	start_loc['e']  = path[0]
	start_loc['se'] = path[1]
	start_loc['ne'] = path[2]
	start_loc['w']  = path[3]
	start_loc['nw'] = path[4]
	start_loc['sw'] = path[5]

	for step in valid_dirs:
		trial = start_loc.copy()
		trial[step] += 1
		trial = path_compress(trial)
		trial = ','.join(str(x) for x in trial.values())
		if trial in black_tiles:
			count += 1

	return count

def new_day():
	global black_tiles
	next = set()
	evaluated = set()
	for tile in list(black_tiles):
		count = count_adjacent(tile)
		if not (count == 0 or count > 2):
			next.add(tile)
		for i in range(6):
			trial = [ int(x) for x in tile.split(",") ]
			trial[i] += 1
			start_loc = {"e" : 0, "se": 0, "ne": 0, "w": 0, "nw": 0, "sw": 0}
			start_loc['e']  = trial[0]
			start_loc['se'] = trial[1]
			start_loc['ne'] = trial[2]
			start_loc['w']  = trial[3]
			start_loc['nw'] = trial[4]
			start_loc['sw'] = trial[5]
			start_loc = path_compress(start_loc)
			trial = ','.join(str(x) for x in start_loc.values())
			if trial not in evaluated:
				evaluated.add(trial)
				if count_adjacent(trial) == 2:
					next.add(trial)
	black_tiles = next

if __name__ == "__main__":

	# Part 1 Solution
	with open("day24_input", 'r') as infile:
		for line in infile.readlines():
			parse(line.strip())
	print(len(black_tiles))

	# Part 2 Solution
	for _ in range(100):
		new_day()
	print(len(black_tiles))
