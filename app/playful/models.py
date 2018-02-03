from urllib.request import Request, urlopen
from urllib.error import HTTPError
import pandas as pd
import json
import numpy as np
from playful import gamedata
from playful.config import api_key


def convert_input_to_userid(input_id):
	""" 
	Take user input from app (Steam user ID or vanity URL) and output Steam user ID for further API calls ]
	"""
	req = Request('http://api.steampowered.com/ISteamUser/ResolveVanityURL/v0001/?key=%s&vanityurl=%s'%(api_key, input_id))

	try:
		data_raw = urlopen(req).read()
	except HTTPError:
		return input_id
	
	data_json = json.loads(data_raw)

	try:
		return int(data_json['response']['steamid'])
	except KeyError:
		return input_id


def get_user_games(user_id):
	""" 
	Take Steam ID and make an API call to return users's owned games and hours played 
	"""
	req = Request('http://api.steampowered.com/IPlayerService/GetOwnedGames/v0001/?key=%s&steamid=%s&format=json&include_played_free_games=True&include_appinfo=True'%(api_key, user_id))
	try:
		data_raw = urlopen(req).read()
		data_json = json.loads(data_raw)
		return data_json['response']['games']
	except:
		return []


def get_sorted_user_games_and_hours_played(user_game_info):
	"""
	Take output from get_user_games, sort it by hours played, and
	return two lists: the IDs of the user games and the hours played
	Games played more come earlier in the returned lists.
	"""
	user_game_ids = [app['appid'] for app in user_game_info]
	user_hours_played = [app['playtime_forever'] for app in user_game_info]
	userdf = pd.DataFrame({'appid': user_game_ids, 'hours_played' : user_hours_played})
	userdf = userdf.sort_values(by='hours_played', ascending=False) 
	return userdf.appid.values, userdf.hours_played.values


def idx_to_recs(game_idx, user_game_ids):
	"""
	Take a game index (its location in the game similarity matrix) and a user's games (as IDs)
	Return a list of game recommendations ranked by their similarity to the input game.
	"""
	game_recs_scores = gamedata.game_similarity_matrix[game_idx]
	df = pd.DataFrame({'game_idx':list(gamedata.idx_to_gamename.keys()), 'scores':game_recs_scores})
	df = df.sort_values(by='scores', ascending=False)
	df['game_id'] = [gamedata.idx_to_gameid[idx] for idx in df.game_idx]
	df['game_names'] = [gamedata.idx_to_gamename[idx] for idx in df.game_idx]

	# games where the image doesn't show up properly
	known_problem_games = ['Fallout: New Vegas', 'Dawn of Discovery'] 

	# filter out games already owned or known to have problems with the image
	df = df[~df.game_id.isin(user_game_ids)] 
	df = df[~df.game_names.isin(known_problem_games)]

	return df['game_names'].values


def get_recs_for_one_game(user_games):
	"""
	For use when a Steam user owns only 1 or 2 games.

	Take a list of games returned by function get_user_games
	Returns:
		1. Name of user's top game by hours played
		1. A ranked list of 12 recommended game names
		2. The recommended games' Steam IDs
	"""
	user_game_ids, user_hours_played = get_sorted_user_games_and_hours_played(user_games)

	try:
		if user_hours_played[0] > user_hours_played[1]:
			game_id = user_game_ids[0]
		else:
			game_id = user_game_ids[1]
	except IndexError:
		game_id = user_game_ids[0]

	user_top_game = gamedata.gameid_to_gamename[game_id]
	recs_gamenames = idx_to_recs(gamedata.gameid_to_idx[game_id], user_game_ids)[0:12]
	recs_gameids = [gamedata.gamename_to_gameid[gamename] for gamename in recs_gamenames]

	return user_top_game, recs_gamenames, recs_gameids


def get_user_recs(user_games, ngroups=3, nrecs_per_group=4):
	"""
	For use when a Steam user owns at least 3 games.

	Input: the list of user game info returned by get_user_games
	
	Arguments:
	ngroups = the number of games to make item-to-item recommendations for
	nrecs_per_group = the number of recommendations for each game
	For ngroups=3 and nrecs_per_group=4, a total of 12 recommendations will be returned.

	Returns:
		1. List of ngroups game names ranked by hours played
		2. List of names of the ngroups x nrecs_per_group recommended games
		3. List of the Steam IDs for the recommended games
	"""
	user_game_ids, user_hours_played = get_sorted_user_games_and_hours_played(user_games)	  
	
	games_already_recommended = []
	rec_names = []
	rec_ids = []
	users_top_games = []

	for n in range(ngroups):
		users_top_games.append(gamedata.gameid_to_gamename[user_game_ids[n]])
		user_game_id = user_game_ids[n]
		recs = idx_to_recs(gamedata.gameid_to_idx[user_game_id], user_game_ids)
		recs = [rec for rec in recs if rec not in games_already_recommended] 
		for rec in recs[0:nrecs_per_group]:
			games_already_recommended.append(rec)
			rec_names.append(rec)
			rec_ids.append(gamedata.gamename_to_gameid[rec])
	return users_top_games, rec_names, rec_ids


def gameids_to_images(game_ids):
  return [''.join(('http://cdn.steamstatic.com/steam/apps/', str(game_id), '/header.jpg')) for game_id in game_ids]


def gameids_to_links(game_ids):
  return [''.join(('http://store.steampowered.com/app/', str(game_id))) for game_id in game_ids]