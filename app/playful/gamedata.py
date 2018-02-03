import pickle

path_to_data = 'playful//static//data//'

# pre-computed matrix of similarities between games
with open(''.join((path_to_data, 'item_similarity_matrix.p')), 'rb') as f:
	game_similarity_matrix = pickle.load(f)

# mapping dictionaries to switch between index, game ID, and game name
with open(''.join((path_to_data, 'gameid_to_gamename.p')), 'rb') as f:
	gameid_to_gamename = pickle.load(f)

with open(''.join((path_to_data, 'gamename_to_gameid.p')), 'rb') as f:
	gamename_to_gameid = pickle.load(f)

with open(''.join((path_to_data, '/gameid_to_idx.txt')), 'rb') as f:
    gameid_to_idx = pickle.load(f)    

with open(''.join((path_to_data, 'idx_to_gameid.txt')), 'rb') as f:
    idx_to_gameid = pickle.load(f)

with open(''.join((path_to_data, 'idx_to_gamename.p')), 'rb') as f:
	idx_to_gamename = pickle.load(f)

with open(''.join((path_to_data, 'gamename_to_idx.p')), 'rb') as f:
	gamename_to_idx = pickle.load(f)

