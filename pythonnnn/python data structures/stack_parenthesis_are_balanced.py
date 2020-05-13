from stack import Stack


def is_match(p1,p2):
	if p1 == "(" and p2 ==")":
		return True
	elif p1 == "[" and p2 =="]":
		return True
	elif p1 == "{" and p2 =="}":
		return True
	else:
		return False


def is_paren_balanced(paren_string):
	s = Stack()
	is_balanced = True
	index = 0

	while index < len(paren_string)and is_balanced:
		paren = paren_string[index]
		#print('paren',paren)

		if paren in "([{":
			s.push(paren)
			#print('yes')
		else:
			if s.is_empty():
				is_balanced = False
				#print('yes')
			else:
				top = s.pop()
				#print(top)
				if not is_match(top,paren):
					is_balanced = False


		index +=1

	if s.is_empty() and is_balanced:
		
		return True
	else:
		#print(is_balanced)
		#print(s.is_empty())
		return False



print(is_paren_balanced("(())[]"))