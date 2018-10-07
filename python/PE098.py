# find anagram pairs

data = open("PE098.txt", "r")
words = [i.split('"')[1] for i in data.read().split(',')]

words_dict = {'init':['init']}
for word in words:
	s = ''.join(sorted(word))
	if(s in words_dict):
		words_dict[s].append(word)
	else:
		words_dict[s] = [word]

words_pair = sorted([words_dict[key] for key in list(words_dict.keys()) if len(words_dict[key])>1], key=lambda k: len(k[0]), reverse=True)

'''
words_pair

['INTRODUCE', 'REDUCTION']
['CREATION', 'REACTION']
['CENTRE', 'RECENT']
['COURSE', 'SOURCE']
['CREDIT', 'DIRECT']
['DANGER', 'GARDEN']
['EXCEPT', 'EXPECT']
['FORMER', 'REFORM']
['IGNORE', 'REGION']
['ARISE', 'RAISE']
['BOARD', 'BROAD']
['EARTH', 'HEART']
['LEAST', 'STEAL']
['NIGHT', 'THING']
['PHASE', 'SHAPE']
['QUIET', 'QUITE']
['SHEET', 'THESE']
['SHOUT', 'SOUTH']
['THROW', 'WORTH']
['CARE', 'RACE']
['DEAL', 'LEAD']
['EARN', 'NEAR']
['EAST', 'SEAT']
['FILE', 'LIFE']
['FORM', 'FROM']
['HATE', 'HEAT']
['ITEM', 'TIME']
['MALE', 'MEAL']
['MEAN', 'NAME']
['NOTE', 'TONE']
['POST', 'SPOT', 'STOP'] <- should handle this case, but since this won't be answer, pass.
['RATE', 'TEAR']
['SHUT', 'THUS']
['SIGN', 'SING']
['SURE', 'USER']
['ACT', 'CAT']
['DOG', 'GOD']
['EAT', 'TEA']
['HOW', 'WHO']
['ITS', 'SIT']
['NOW', 'OWN']
['NO', 'ON']
'''

# then, find square
l = 9
sq_list = [int(i**2) for i in range(int((10**(l-1))**0.5), int((10**l)**0.5)) if len(set(str(int(i**2)))) == l]
done = False
for pair in words_pair:
	str_map = [pair[0].index(pair[1][i]) for i in range(len(pair[0]))]
	length = len(pair[0])
	# update sq_list when length changes
	if(l != length):
		if(done):
			break
		l = length
		sq_list = [int(i**2) for i in range(int((10**(l-1))**0.5), int((10**l)**0.5)) if len(set(str(int(i**2)))) == l]
	# process
	for i in sq_list:
		anag = int(''.join([str(i)[ind] for ind in str_map]))
		if(anag in sq_list):
			print(i, anag)
			done = True

'''
this prints '17689 18769'
'''
