#!/usr/bin/python

"""

--- Day 18: Operation Order ---

As you look out the window and notice a heavily-forested continent slowly appear over the horizon, you are interrupted by the child sitting next to you. They're curious if you could help them with their math homework.

Unfortunately, it seems like this "math" follows different rules than you remember.

The homework (your puzzle input) consists of a series of expressions that consist of addition (+), multiplication (*), and parentheses ((...)). Just like normal math, parentheses indicate that the expression inside must be evaluated before it can be used by the surrounding expression. Addition still finds the sum of the numbers on both sides of the operator, and multiplication still finds the product.

However, the rules of operator precedence have changed. Rather than evaluating multiplication before addition, the operators have the same precedence, and are evaluated left-to-right regardless of the order in which they appear.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
      9   + 4 * 5 + 6
         13   * 5 + 6
             65   + 6
                 71

Parentheses can override this order; for example, here is what happens if parentheses are added to form 1 + (2 * 3) + (4 * (5 + 6)):

1 + (2 * 3) + (4 * (5 + 6))
1 +    6    + (4 * (5 + 6))
     7      + (4 * (5 + 6))
     7      + (4 *   11   )
     7      +     44
            51

Here are a few more examples:

    2 * 3 + (4 * 5) becomes 26.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 437.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 12240.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 13632.

Before you can help with the homework, you need to understand it yourself. Evaluate the expression on each line of the homework; what is the sum of the resulting values?

Your puzzle answer was 3647606140187.

The first half of this puzzle is complete! It provides one gold star: *
--- Part Two ---

You manage to answer the child's questions and they finish part 1 of their homework, but get stuck when they reach the next section: advanced math.

Now, addition and multiplication have different precedence levels, but they're not the ones you're familiar with. Instead, addition is evaluated before multiplication.

For example, the steps to evaluate the expression 1 + 2 * 3 + 4 * 5 + 6 are now as follows:

1 + 2 * 3 + 4 * 5 + 6
  3   * 3 + 4 * 5 + 6
  3   *   7   * 5 + 6
  3   *   7   *  11
     21       *  11
         231

Here are the other examples from above:

    1 + (2 * 3) + (4 * (5 + 6)) still becomes 51.
    2 * 3 + (4 * 5) becomes 46.
    5 + (8 * 3 + 9 + 3 * 4 * 3) becomes 1445.
    5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4)) becomes 669060.
    ((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2 becomes 23340.

What do you get if you add up the results of evaluating the homework problems using these new rules?

"""

numbers = [ chr(i) for i in range(48,58) ]

token_stack = []
P = []

def eqn_parse(line, idx):
	total = 0
	last_op = None
	current_num = None
	while idx < len(line):
		char = line[idx]
		if char == "*" or char == "+":
			last_op = char
		elif char in numbers:
			current_num = int(char)
		elif char == "(":
			current_num, offset = eqn_parse(line[idx+1:], 0)
			idx += offset
		elif char == ")":
			return (total, idx+1)
		if current_num != None and last_op == None:
			total = current_num
			current_num = None
		elif current_num != None and last_op != None:
			if last_op == "*":
				total *= current_num
			elif last_op == "+":
				total += current_num
			current_num = None
			last_op = None
		idx += 1
	return (total, idx)

def tokenize(line):
	for char in line:
		if char == "(" or char == ")":
			token_stack.append(char)
		elif char in numbers:
			token_stack.append(char)
		elif char == "+":
			token_stack.append(char)
		elif char == "*":
			token_stack.append(char)

def make_postfix():
	stack = []
	while len(token_stack) > 0:
		current = token_stack.pop(0)
		if current in numbers:
			P.append(current)
		elif current == "(":
			stack.append(current)
		elif current == ")":
			while len(stack) > 0 and stack[-1] != "(":
				P.append(stack.pop())
			if stack[-1] == "(":
				stack.pop()
		elif current ==  "+" or current == "*":
			prec = 0
			if current == "+":
				prec = 1
			if len(stack) == 0 or stack[-1] == "(":
				stack.append(current)
			else:
				while len(stack) > 0 and stack[-1] != "(" and (stack[-1] != "*" and prec == 0):
					P.append(stack.pop())
				stack.append(current)
	while len(stack) > 0:
		P.append(stack.pop())

def postfix_eval():
	stack = []
	while len(P) > 0:
		current = P.pop(0)
		if current in numbers:
			stack.append(int(current))
		else:
			a = stack.pop()
			b = stack.pop()
			if current == "+":
				stack.append(a+b)
			elif current == "*":
				stack.append(a*b)
	return stack.pop()

if __name__ == "__main__":


	# Part 1 Solution
	total = 0

	with open("day18_input", 'r') as infile:
		for line in infile.readlines():
			t, idx = eqn_parse(line.strip(),0)
			total += t
	print(total)


	# Part 2 Solution
	total = 0
	
	with open("day18_input", 'r') as infile:
		idx = 0
		for line in infile.readlines():
			if line.strip() != '':
				token_stack = []
				P = []
				tokenize(line.strip())
				make_postfix()
				total += postfix_eval()
	print(total)
