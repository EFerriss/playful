import pickle
import numpy as np

path_to_data = 'playful//static//data//'

# pre-trained lightfm model created using implicit feedback
with open(''.join((path_to_data, 'model_final.p')), 'rb') as f:
	 model = pickle.load(f)

def get_item2item_matrix(model):
    itemitem = model.item_embeddings.dot(model.item_embeddings.T)
    normalizeto = np.array([np.sqrt(np.diagonal(itemitem))])
    itemitem = itemitem / normalizeto / normalizeto.T
    return itemitem

game_similarity_matrix = get_item2item_matrix(model)

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

