
def quickfactorizer(z):		#like the original factorizer
	#n = [0, 1, 2, 3, 4, 5]	#except reduces redundancy
	#loop = 0				#by eliminating multiples of checked numbers
	factors = []
	tries = []
	i = 2 					#exclude all multiples of numbers that were checked
	if z<=1: 				# ^ HOW DO?
		return ["No Prime Factors"]
	while z>1:
		bull = True
#		for i in n:
#			i += loop*6
		for f in tries:
			if i%f == 0:
				bull = False
				break
		if bull:
			tries.append(i)
			if i>=int(math.sqrt(z)):
				factors.append(z)
				z = 1
			elif i>=2:
				while z%i==0:
					factors.append(i)
					z = int(z/i)
			if z == 1:
				break
		if i>2:
			i += 2
		else:
			i +=1
		
#		loop+=1
	return factors
