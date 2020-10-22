from collections import Counter
from re import findall
from numpy import sign
import csv

chunks = []

with open('./01-2013.pgn', 'r') as file:
	
	#filter into chunks representing individual games
	begin_chunk = '[Event'
	chunk = ''
	#features = []
	for line in file:
		if line[0:6] != begin_chunk:
			chunk += line
		else:
			chunks.append(chunk[0:len(chunk)-2].split('\n'))
			chunk = line
	

	# filter by games with eval
	eval_chunks = [c for c in chunks if '{' in c[-1][0:10]]
	# write eval chunks to filtered pgn file
	with open('./filtered.pgn', 'w') as filtered:
		for chunk in eval_chunks:
			for e in chunk:
				filtered.write(str(e) + '\n')
			filtered.write('\n\n')

	# feature extraction
	feature_vectors = []
	for c in eval_chunks:
		# game_type, white_elo, black_elo, termination_type, move_seq
		features = [c[0].split()[2], c[7], c[8], c[14], c[16]]
		features[1] = int(features[1].split()[1].strip('"]'))
		features[2] = int(features[2].split()[1].strip('"]'))
		features[3] = features[3].split()[1].strip('"]')
		features[4] = [x.strip('\%eval []') for x in findall(r'\%eval.{1,5}', features[4])]
		feature_vectors.append(features)
		# now in format str, int, int, str, list[str]

	#print(feature_vectors[0])
	# let's get the eval into a more meaningful format
	for v in feature_vectors:
		v[4] = [float(x) if x[0] != '#' else sign(float(x[1:]))*100 for x in v[4]]
		diffs = [round(v[4][x] - v[4][x+1], 2) for x in range(0,len(v[4])-1)]
		v.append(diffs)

	print(Counter([f[0] for f in feature_vectors]))
	print(feature_vectors[0])

	with open('games.csv', 'w') as games:
		writer = csv.writer(games)
		writer.writerows(feature_vectors)




