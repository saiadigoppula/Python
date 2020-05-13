import math

T = 3
values = ["5 9 -1 8 1 2","3 9 1 4","10 1 22 3 17 -1 5 -1 8 -1 10"]



#print(str(values[0]))
updated_values = []
for x in range(T):
	y = 0
	every_str = ''
	first = str(values[x])
	#for y in range(len(first)):
	while(y<len(first)):
		if(first[y] !=' '):

			if(y+4 <= len(first)):
				if(first[y] !='-') and (first[y+3]=='-'):
					if(y !=0):
						if (first[y] != '1'):
							every_str = every_str + str(int(first[y]) - 1)
							print('1',every_str)
						else:
							every_str = every_str + str(int(1))
							print('2',every_str)


				else:
					if first[y]=='-':
						if((int(first[y-2]) % 2) == 0 and (int(first[y+3]) % 2) ==0) or((int(first[y-2]) % 2) != 0 and (int(first[y+3]) % 2) !=0) :
							blank = abs(int(first[y-2]) - int(first[y+3]))
							if (blank != '1'):
								every_str = every_str + str(blank - 1)
								print('3',every_str)
							else:
								every_str = every_str + str(int(1))
								print('4',every_str)

								
						else:
							new_value = math.floor((int(first[y-2]) + int(first[y+3]))/2)
							if (new_value != '1'):
								every_str = every_str + str(new_value- 1)
								print('5',every_str)
							else:
								every_str = every_str + str(int(1))
								print('6',every_str)
								
						y = y+1
					else:
						if(y !=0):
							if(y+1 == len(first)):
								every_str = every_str + first[y]
								print('6.5',every_str)
							else:	
								if (first[y] != '1'):
									every_str = every_str + str(int(first[y] )- 1)
									print('7',every_str)
								else:
									every_str = every_str + str(int(1))
									print('8',every_str)








			else:
				if first[y]=='-':
					if((int(first[y-2]) % 2) == 0 and (int(first[y+3]) % 2) ==0) or ((int(first[y-2]) % 2) != 0 and (int(first[y+3]) % 2) !=0) :
						blank = abs(first[y-2] - first[y+3])
						if (blank != '1'):
							every_str = every_str + str(blank - 1)
							print('9',every_str)
						else:
							every_str = every_str + str(int(1))
							print('10',every_str)

							
					else:
						new_value = math.floor((first[y-2] + first[y+3])/2)
						if (new_value != '1'):
							every_str = every_str + str(new_value- 1)
							print('11',every_str)
						else:
							every_str = every_str + str(int(1))
							print('12',every_str)
							
					y = y+1
				else:
					if(y !=0):
						if(y+1 == len(first)):
							every_str = every_str + first[y]
							print('13',every_str)
						else:	
							if (first[y] != '1'):
								every_str = every_str + str(int(first[y] )- 1)
								print('14',every_str)
							else:
								every_str = every_str + str(int(1))
								print('15',every_str)
							






		#	if(first[y] !='-') and (first[y+3]=='-') and (y-3<=len(first)):
		#		if(first[y]=='-'):
		#			if((first[y-2] % 2) == 0 and (first[y+3] % 2) ==0) or((first[y-2] % 2) != 0 and (first[y+3] % 2) !=0) :
		#				blank = abs(first[y-2] - first[y+3])
		#				if(blank == 1):
		#					print(blank-1)


			#else:
			#	print(int(first[y]) - 1 )

		y = y +1
	print(every_str)



