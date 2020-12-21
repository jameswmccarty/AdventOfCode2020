#!/usr/bin/python

"""

--- Day 21: Allergen Assessment ---

You reach the train's last stop and the closest you can get to your vacation island without getting wet. There aren't even any boats here, but nothing can stop you now: you build a raft. You just need a few days' worth of food for your journey.

You don't speak the local language, so you can't read any ingredients lists. However, sometimes, allergens are listed in a language you do understand. You should be able to use this information to determine which ingredient contains which allergen and work out which foods are safe to take with you on your trip.

You start by compiling a list of foods (your puzzle input), one food per line. Each line includes that food's ingredients list followed by some or all of the allergens the food contains.

Each allergen is found in exactly one ingredient. Each ingredient contains zero or one allergen. Allergens aren't always marked; when they're listed (as in (contains nuts, shellfish) after an ingredients list), the ingredient that contains each listed allergen will be somewhere in the corresponding ingredients list. However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present: maybe they forgot to label it, or maybe it was labeled in a language you don't know.

For example, consider the following list of foods:

mxmxvkd kfcds sqjhc nhms (contains dairy, fish)
trh fvjkl sbzzf mxmxvkd (contains dairy)
sqjhc fvjkl (contains soy)
sqjhc mxmxvkd sbzzf (contains fish)

The first food in the list has four ingredients (written in a language you don't understand): mxmxvkd, kfcds, sqjhc, and nhms. While the food might contain other allergens, a few allergens the food definitely contains are listed afterward: dairy and fish.

The first step is to determine which ingredients can't possibly contain any of the allergens in any food in your list. In the above example, none of the ingredients kfcds, nhms, sbzzf, or trh can contain an allergen. Counting the number of times any of these ingredients appear in any ingredients list produces 5: they all appear once each except sbzzf, which appears twice.

Determine which ingredients cannot possibly contain any of the allergens in your list. How many times do any of those ingredients appear?

Your puzzle answer was 2125.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

Now that you've isolated the inert ingredients, you should have enough information to figure out which ingredient contains which allergen.

In the above example:

    mxmxvkd contains dairy.
    sqjhc contains fish.
    fvjkl contains soy.

Arrange the ingredients alphabetically by their allergen and separate them by commas to produce your canonical dangerous ingredient list. (There should not be any spaces in your canonical dangerous ingredient list.) In the above example, this would be mxmxvkd,sqjhc,fvjkl.

Time to stock your raft with supplies. What is your canonical dangerous ingredient list?


"""

allergens = dict()
foods = dict()
foods_list = []

def parse(line):
	left, right = line.split("(contains ")
	right = right.strip(")").strip().split(", ")
	left  = left.strip().split(" ")
	
	for item in right:
		if item in allergens:
			allergens[item].append(set(left))
		else:
			allergens[item] = [ set(left) ]

	foods_list.append(set(left))
	
	for item in left:
		if item in foods:
			foods[item].update(set(right))
		else:
			foods[item] = set(right)


if __name__ == "__main__":

	# Part 1 Solution
	with open("day21_input", 'r') as infile:
		for line in infile.readlines():
			parse(line.strip())

	for item in allergens.keys():
		allergens[item] = set.intersection(*allergens[item])

	known_harmful = set()
	for item in allergens.keys():
		known_harmful.update(allergens[item])

	safe_foods = set(foods.keys())

	for bad in known_harmful:
		safe_foods.discard(bad)

	count = 0
	for item in foods_list:
		t = item.intersection(safe_foods)
		count += len(t)
	print(count)

	# Part 2 Solution
	for item in allergens.keys():
		for good in safe_foods:
			allergens[item].discard(good)

	done = False
	while not done:
		done = True
		for item in allergens.keys():
			if len(allergens[item]) == 1:
				for a in allergens.keys():
					if a != item:
						allergens[a].discard(list(allergens[item])[0])
		for item in allergens.keys():
			if len(allergens[item]) != 1:
				done = False
	
	alphabetical = [x for x in allergens.keys()]
	alphabetical.sort()
	out = ""
	for item in alphabetical:
		out += ''.join(allergens[item])+","
	print(out[:-1])
