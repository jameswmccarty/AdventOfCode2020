#!/usr/bin/python

"""
--- Day 20: Jurassic Jigsaw ---

The high-speed train leaves the forest and quickly carries you south. You can even see a desert in the distance! Since you have some spare time, you might as well see if there was anything interesting in the image the Mythical Information Bureau satellite captured.

After decoding the satellite messages, you discover that the data actually contains many small images created by the satellite's camera array. The camera array consists of many cameras; rather than produce a single square image, they produce many smaller square image tiles that need to be reassembled back into a single image.

Each camera in the camera array returns a single monochrome image tile with a random unique ID number. The tiles (your puzzle input) arrived in a random order.

Worse yet, the camera array appears to be malfunctioning: each image tile has been rotated and flipped to a random orientation. Your first task is to reassemble the original image by orienting the tiles so they fit together.

To show how the tiles should be reassembled, each tile's image data includes a border that should line up exactly with its adjacent tiles. All tiles have this border, and the border lines up exactly when the tiles are both oriented correctly. Tiles at the edge of the image also have this border, but the outermost edges won't line up with any other tiles.

For example, suppose you have the following nine tiles:

Tile 2311:
..##.#..#.
##..#.....
#...##..#.
####.#...#
##.##.###.
##...#.###
.#.#.#..##
..#....#..
###...#.#.
..###..###

Tile 1951:
#.##...##.
#.####...#
.....#..##
#...######
.##.#....#
.###.#####
###.##.##.
.###....#.
..#.#..#.#
#...##.#..

Tile 1171:
####...##.
#..##.#..#
##.#..#.#.
.###.####.
..###.####
.##....##.
.#...####.
#.##.####.
####..#...
.....##...

Tile 1427:
###.##.#..
.#..#.##..
.#.##.#..#
#.#.#.##.#
....#...##
...##..##.
...#.#####
.#.####.#.
..#..###.#
..##.#..#.

Tile 1489:
##.#.#....
..##...#..
.##..##...
..#...#...
#####...#.
#..#.#.#.#
...#.#.#..
##.#...##.
..##.##.##
###.##.#..

Tile 2473:
#....####.
#..#.##...
#.##..#...
######.#.#
.#...#.#.#
.#########
.###.#..#.
########.#
##...##.#.
..###.#.#.

Tile 2971:
..#.#....#
#...###...
#.#.###...
##.##..#..
.#####..##
.#..####.#
#..#.#..#.
..####.###
..#.#.###.
...#.#.#.#

Tile 2729:
...#.#.#.#
####.#....
..#.#.....
....#..#.#
.##..##.#.
.#.####...
####.#.#..
##.####...
##..#.##..
#.##...##.

Tile 3079:
#.#.#####.
.#..######
..#.......
######....
####.#..#.
.#...#.##.
#.#####.##
..#.###...
..#.......
..#.###...

By rotating, flipping, and rearranging them, you can find a square arrangement that causes all adjacent borders to line up:

#...##.#.. ..###..### #.#.#####.
..#.#..#.# ###...#.#. .#..######
.###....#. ..#....#.. ..#.......
###.##.##. .#.#.#..## ######....
.###.##### ##...#.### ####.#..#.
.##.#....# ##.##.###. .#...#.##.
#...###### ####.#...# #.#####.##
.....#..## #...##..#. ..#.###...
#.####...# ##..#..... ..#.......
#.##...##. ..##.#..#. ..#.###...

#.##...##. ..##.#..#. ..#.###...
##..#.##.. ..#..###.# ##.##....#
##.####... .#.####.#. ..#.###..#
####.#.#.. ...#.##### ###.#..###
.#.####... ...##..##. .######.##
.##..##.#. ....#...## #.#.#.#...
....#..#.# #.#.#.##.# #.###.###.
..#.#..... .#.##.#..# #.###.##..
####.#.... .#..#.##.. .######...
...#.#.#.# ###.##.#.. .##...####

...#.#.#.# ###.##.#.. .##...####
..#.#.###. ..##.##.## #..#.##..#
..####.### ##.#...##. .#.#..#.##
#..#.#..#. ...#.#.#.. .####.###.
.#..####.# #..#.#.#.# ####.###..
.#####..## #####...#. .##....##.
##.##..#.. ..#...#... .####...#.
#.#.###... .##..##... .####.##.#
#...###... ..##...#.. ...#..####
..#.#....# ##.#.#.... ...##.....

For reference, the IDs of the above tiles are:

1951    2311    3079
2729    1427    2473
2971    1489    1171

To check that you've assembled the image correctly, multiply the IDs of the four corner tiles together. If you do this with the assembled tiles from the example above, you get 1951 * 3079 * 2971 * 1171 = 20899048083289.

Assemble the tiles into an image. What do you get if you multiply together the IDs of the four corner tiles?

Your puzzle answer was 7492183537913.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Now, you're ready to check the image for sea monsters.

The borders of each tile are not part of the actual image; start by removing them.

In the example above, the tiles become:

.#.#..#. ##...#.# #..#####
###....# .#....#. .#......
##.##.## #.#.#..# #####...
###.#### #...#.## ###.#..#
##.#.... #.##.### #...#.##
...##### ###.#... .#####.#
....#..# ...##..# .#.###..
.####... #..#.... .#......

#..#.##. .#..###. #.##....
#.####.. #.####.# .#.###..
###.#.#. ..#.#### ##.#..##
#.####.. ..##..## ######.#
##..##.# ...#...# .#.#.#..
...#..#. .#.#.##. .###.###
.#.#.... #.##.#.. .###.##.
###.#... #..#.##. ######..

.#.#.### .##.##.# ..#.##..
.####.## #.#...## #.#..#.#
..#.#..# ..#.#.#. ####.###
#..####. ..#.#.#. ###.###.
#####..# ####...# ##....##
#.##..#. .#...#.. ####...#
.#.###.. ##..##.. ####.##.
...###.. .##...#. ..#..###

Remove the gaps to form the actual image:

.#.#..#.##...#.##..#####
###....#.#....#..#......
##.##.###.#.#..######...
###.#####...#.#####.#..#
##.#....#.##.####...#.##
...########.#....#####.#
....#..#...##..#.#.###..
.####...#..#.....#......
#..#.##..#..###.#.##....
#.####..#.####.#.#.###..
###.#.#...#.######.#..##
#.####....##..########.#
##..##.#...#...#.#.#.#..
...#..#..#.#.##..###.###
.#.#....#.##.#...###.##.
###.#...#..#.##.######..
.#.#.###.##.##.#..#.##..
.####.###.#...###.#..#.#
..#.#..#..#.#.#.####.###
#..####...#.#.#.###.###.
#####..#####...###....##
#.##..#..#...#..####...#
.#.###..##..##..####.##.
...###...##...#...#..###

Now, you're ready to search for sea monsters! Because your image is monochrome, a sea monster will look like this:

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   

When looking for this pattern in the image, the spaces can be anything; only the # need to match. Also, you might need to rotate or flip your image before it's oriented correctly to find sea monsters. In the above image, after flipping and rotating it to the appropriate orientation, there are two sea monsters (marked with O):

.####...#####..#...###..
#####..#..#.#.####..#.#.
.#.#...#.###...#.##.O#..
#.O.##.OO#.#.OO.##.OOO##
..#O.#O#.O##O..O.#O##.##
...#.#..##.##...#..#..##
#.##.#..#.#..#..##.#.#..
.###.##.....#...###.#...
#.####.#.#....##.#..#.#.
##...#..#....#..#...####
..#.##...###..#.#####..#
....#.##.#.#####....#...
..##.##.###.....#.##..#.
#...#...###..####....##.
.#.##...#.##.#.#.###...#
#.###.#..####...##..#...
#.###...#.##...#.##O###.
.O##.#OO.###OO##..OOO##.
..O#.O..O..O.#O##O##.###
#.#..##.########..#..##.
#.#####..#.#...##..#....
#....##..#.#########..##
#...#.....#..##...###.##
#..###....##.#...##.##.#

Determine how rough the waters are in the sea monsters' habitat by counting the number of # that are not part of a sea monster. In the above example, the habitat's water roughness is 273.

How many # are not part of a sea monster?

"""

import math

tiles = dict()
tile_mapping = dict()

class Tile:

	def __init__(self, num):
		self.num = num
		self.matched = set()
		self.on = set()
		self.edge_sets = set()
	
	def match_count(self):
		return len(self.matched)
	
	def build_edge_sets(self):
		top      = { (0,i) for i in range(10) if (0,i) in self.on    }
		top_r    = { (0,9-i) for i in range(10) if (0,i) in self.on }
		left     = { (i,0) for i in range(10) if (i,0) in self.on    }
		left_r   = { (9-i,0) for i in range(10) if (i,0) in self.on }
		bottom   = { (i,9) for i in range(10) if (i,9) in self.on    }
		bottom_r = { (9-i,9) for i in range(10) if (i,9) in self.on }
		right    = { (9,i) for i in range(10) if (9,i) in self.on    }
		right_r  = { (9,9-i) for i in range(10) if (9,i) in self.on }
		self.edge_sets = [ top, top_r, left, left_r, bottom, bottom_r, right, right_r ]
		rot_sets = []
		for item in self.edge_sets:
			new_set = { (y,x) for (x,y) in item }
			rot_sets.append(new_set)
		self.edge_sets += rot_sets
		rot_sets = []
		for item in self.edge_sets:
			new_set = { (9-x,9-y) for (x,y) in item }
			rot_sets.append(new_set)
		self.edge_sets += rot_sets
	
	# return True if the right edge of this block aligns with
	# the left-most edge of provided block number
	def right_edge_match(self, block):
		own_edge = { i for i in range(10) if (9,i) in self.on }
		left_edge= { i for i in range(10) if (0,i) in tiles[block].on }
		if own_edge == left_edge:
			return True
		return False

	# return True if the bottom edge of this block aligns with
	# the top-most edge of provided block number
	def bottom_edge_match(self, block):
		own_edge = { i for i in range(10) if (i,9) in self.on }
		top_edge=  { i for i in range(10) if (i,0) in tiles[block].on }
		if own_edge == top_edge:
			return True
		return False

def flip_horiz(mapping):
	new = set()
	for item in list(mapping):
		x, y = item
		new.add((9-x,y))
	return new

def flip_vert(mapping):
	new = set()
	for item in list(mapping):
		x, y = item
		new.add((x,9-y))
	return new

def rotate(mapping):
	new = set()
	for item in list(mapping):
		x, y = item
		new.add((9-y,x))
	return new

def print_map(mapping):
	for i in range(10):
		out = ''
		for j in range(10):
			if (j,i) in mapping:
				out += "#"
			else:
				out += "."
		print(out)
	print()

def parse(block):
	idx = 0
	on  = set()
	for line in block.split('\n'):
		#print(idx, line)
		if "Tile" in line:
			num = int(line.strip().replace("Tile ",'').replace(":",''))
		else:
			for i, char in enumerate(line.strip()):
				if char == "#":
					on.add((i,idx))
			idx += 1
	tile = Tile(num)
	tile.on = on
	tile.build_edge_sets()
	tiles[num] = tile

def build_tile_layout():
	corners = []
	sides   = []
	fill    = []
	for tile in tiles.keys():
		if tiles[tile].match_count() == 2:
			corners.append(tile)
		elif tiles[tile].match_count() == 3:
			sides.append(tile)
		else:
			fill.append(tile)

	side_len = int(math.sqrt(len(tiles.keys())))
	tile_mapping[(0,0)] = corners.pop()
	last = tile_mapping[(0,0)]

	# top row from left-most corner
	for i in range(1,side_len-1):
		poss = tiles[last].matched
		for value in list(poss):
			if value in sides:
				tile_mapping[(i,0)] = value
				sides.remove(value)
				last = value
				break
	
	# right-most corner
	for value in corners:
		if value in tiles[last].matched:
			tile_mapping[(side_len-1,0)] = value
			corners.remove(value)
			last = value
			break

	# right side
	for i in range(1,side_len-1):
		poss = tiles[last].matched
		for value in list(poss):
			if value in sides:
				tile_mapping[(side_len-1,i)] = value
				sides.remove(value)
				last = value
				break

	# bottom-right corner
	for value in corners:
		if value in tiles[last].matched:
			tile_mapping[(side_len-1,side_len-1)] = value
			corners.remove(value)
			last = value
			break

	# bottom-left corner
	tile_mapping[(0,side_len-1)] = corners.pop()

	last = tile_mapping[(0,0)]
	# left side
	for i in range(1,side_len-1):
		poss = tiles[last].matched
		for value in list(poss):
			if value in sides:
				tile_mapping[(0,i)] = value
				sides.remove(value)
				last = value
				break

	# bottom row
	last = tile_mapping[(0,side_len-1)]
	for i in range(1,side_len-1):
		poss = tiles[last].matched
		for value in list(poss):
			if value in sides:
				tile_mapping[(i, side_len-1)] = value
				sides.remove(value)
				last = value
				break
	
	for i in range(1,side_len-1):
		last = tile_mapping[(0,i)]
		for j in range(1,side_len-1):
			poss = tiles[last].matched
			for value in list(poss):
				if value in fill and value in list(tiles[tile_mapping[(j,i-1)]].matched):
					tile_mapping[(j,i)] = value
					fill.remove(value)
					last = value
					break

def solve_tile_orientation():

	side_len = int(math.sqrt(len(tiles.keys())))
	last = tile_mapping[(0,0)]

	solved = False
	rot_count = 0
	
	c = tile_mapping[(0,0)] # corner      c-r
	r = tile_mapping[(1,0)] # right side  |
	b = tile_mapping[(0,1)] # bottom      b
	
	# solve top left corner first
	# starting with the top left and right side
	rot_count_r = 0
	rot_count_c = 0
	cycle_count = 0
	while not solved:
		if tiles[c].right_edge_match(r):
			solved = True
			break
		tiles[r].on = rotate(tiles[r].on)
		rot_count_r += 1
		if rot_count_r == 3:
			tiles[r].on = rotate(tiles[r].on)
			tiles[r].on = flip_vert(tiles[r].on)
			rot_count_r = 0
		cycle_count += 1
		if cycle_count == 8:
			tiles[c].on = rotate(tiles[c].on)
			rot_count_c += 1
			cycle_count = 0
			if rot_count_c == 3:
				tiles[c].on = rotate(tiles[c].on)
				tiles[c].on = flip_vert(tiles[c].on)
				rot_count_c = 0

	# next solve the tile below the top left corner
	rot_count_b = 0
	rot_count_c = 0
	cycle_count = 0
	solved = False
	while not solved:
		if tiles[c].bottom_edge_match(b):
			solved = True
			break
		tiles[b].on = rotate(tiles[b].on)
		rot_count_b += 1
		if rot_count_b == 3:
			tiles[b].on = rotate(tiles[b].on)
			tiles[b].on = flip_vert(tiles[b].on)
			rot_count_b = 0
		cycle_count += 1
		if cycle_count == 8:
			tiles[c].on = flip_vert(tiles[c].on)
			tiles[r].on = flip_vert(tiles[r].on)
			cycle_count = 0

	# solve the top row
	last = r
	for i in range(2,side_len):
		rot_count = 0
		while not tiles[last].right_edge_match(tile_mapping[(i,0)]):
			tiles[tile_mapping[(i,0)]].on = rotate(tiles[tile_mapping[(i,0)]].on)
			rot_count += 1
			if rot_count == 4:
				tiles[tile_mapping[(i,0)]].on = rotate(tiles[tile_mapping[(i,0)]].on)
				tiles[tile_mapping[(i,0)]].on = flip_horiz(tiles[tile_mapping[(i,0)]].on)
				rot_count = 0
		last = tile_mapping[(i,0)]

	# solve follow-on rows
	for j in range(1,side_len):
		rot_count = 0
		while not tiles[tile_mapping[(0,j-1)]].bottom_edge_match(tile_mapping[(0,j)]):
			tiles[tile_mapping[(0,j)]].on = rotate(tiles[tile_mapping[(0,j)]].on)
			rot_count += 1
			if rot_count == 4:
				tiles[tile_mapping[(0,j)]].on = rotate(tiles[tile_mapping[(0,j)]].on)
				tiles[tile_mapping[(0,j)]].on = flip_horiz(tiles[tile_mapping[(0,j)]].on)
				rot_count = 0
		last = tile_mapping[(0,j)]
		for i in range(1,side_len):
			rot_count = 0
			while not tiles[last].right_edge_match(tile_mapping[(i,j)]) and not tiles[tile_mapping[(i,j-1)]].bottom_edge_match(tile_mapping[(i,j)]):
				tiles[tile_mapping[(i,j)]].on = rotate(tiles[tile_mapping[(i,j)]].on)
				rot_count += 1
				if rot_count == 4:
					tiles[tile_mapping[(i,j)]].on = rotate(tiles[tile_mapping[(i,j)]].on)
					tiles[tile_mapping[(i,j)]].on = flip_horiz(tiles[tile_mapping[(i,j)]].on)
					rot_count = 0
			last = tile_mapping[(i,j)]

def build_bitmap():

	global_on = set()
	side_len = int(math.sqrt(len(tiles.keys())))
	
	for j in range(side_len):
		for i in range(side_len):
			current = tiles[tile_mapping[(i,j)]].on
			for coord in current:
				x, y = coord
				if x>0 and x<9 and y>0 and y<9:
					x -= 1
					y -= 1
					x += i*8
					y += j*8
					global_on.add((x,y))
	"""
	for i in range(8*side_len):
		out = ''
		for j in range(8*side_len):
			if (j,i) in global_on:
				out += "#"
			else:
				out += "."
		print(out)
	"""

	return global_on


def build_test_bitmap():

	offset_map = set()

	image = ["#.#..#.##...#.##..#####",
			"###....#.#....#..#......",
			"##.##.###.#.#..######...",
			"###.#####...#.#####.#..#",
			"##.#....#.##.####...#.##",
			"...########.#....#####.#",
			"....#..#...##..#.#.###..",
			".####...#..#.....#......",
			"#..#.##..#..###.#.##....",
			"#.####..#.####.#.#.###..",
			"###.#.#...#.######.#..##",
			"#.####....##..########.#",
			"##..##.#...#...#.#.#.#..",
			"...#..#..#.#.##..###.###",
			".#.#....#.##.#...###.##.",
			"###.#...#..#.##.######..",
			".#.#.###.##.##.#..#.##..",
			".####.###.#...###.#..#.#",
			"..#.#..#..#.#.#.####.###",
			"#..####...#.#.#.###.###.",
			"#####..#####...###....##",
			"#.##..#..#...#..####...#",
			".#.###..##..##..####.##.",
			"...###...##...#...#..###"]

	for j,line in enumerate(image):
		for i, char in enumerate(line):
			if char == "#":
				offset_map.add((j,i))
	
	return offset_map


def dragon_search(bitmap):
	monster =	["                  #","#    ##    ##    ###"," #  #  #  #  #  #   "]

	offset_map = set()
	bitmap_width  = 8*int(math.sqrt(len(tiles.keys())))
	bitmap_height = 8*int(math.sqrt(len(tiles.keys())))

	for j,line in enumerate(monster):
		for i, char in enumerate(line):
			if char == "#":
				offset_map.add((i,j))

	found = False
	rot_count = 0
	while not found:
		for j in range(bitmap_height):
			for i in range(bitmap_width):
				search_mask = { (x+j,y+i) for x,y in offset_map }
				if len(bitmap.intersection(search_mask)) == len(search_mask):
					found = True
					break
		if found:
			break
		bitmap = { (bitmap_height-y,x) for x,y in bitmap }
		if rot_count == 3:
			bitmap = { (bitmap_height-y,x) for x,y in bitmap }
			bitmap = { (bitmap_width-x,y) for x,y in bitmap }
			rot_count = 0
		rot_count += 1

	for j in range(bitmap_height):
		for i in range(bitmap_width):
			search_mask = { (x+j,y+i) for x,y in offset_map }
			if len(bitmap.intersection(search_mask)) == len(search_mask):
				for point in search_mask:
					bitmap.discard(point)

	return len(bitmap) 


if __name__ == "__main__":

	# Part 1 Solution

	with open("day20_input", 'r') as infile:
		for block in infile.read().split('\n\n'):
			parse(block)

	for tile in tiles.keys():
		for compare in tiles.keys():
			if compare != tile:
				for edge in tiles[tile].edge_sets:
					for comp in tiles[compare].edge_sets:
						if edge == comp:
							tiles[tile].matched.add(compare)
							tiles[compare].matched.add(tile)

	total = 1
	for tile in tiles.keys():
		if tiles[tile].match_count() == 2:
			total *= tile
	print(total)

	# Part 2 Solution
	build_tile_layout()
	#print(len(tile_mapping), tile_mapping)
	solve_tile_orientation()
	global_map = build_bitmap()
	#global_map = build_test_bitmap()
	print(dragon_search(global_map))
