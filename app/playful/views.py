from flask import render_template, request
from playful import app
from playful.models import get_user_recs, get_user_games, convert_input_to_userid, \
 						               get_recs_for_one_game, gameids_to_images,  gameids_to_links

@app.route('/')
@app.route('/index')
def popular_games():
  return render_template('index.html')


@app.route('/about_playful')
def about_playful():
    return render_template('about.html')


@app.route('/about_me')
def about_me():
    return render_template('me.html')


@app.route('/recommendations')
def get_recs():
  input_id = request.args.get("user_id")
  user_id = convert_input_to_userid(input_id)
  user_games = get_user_games(user_id)

  if len(user_games) == 0:
  	return render_template("no_user_games.html")

  elif len(user_games) < 3:
    users_top_game, rec_names, rec_ids = get_recs_for_one_game(user_games)
    images = gameids_to_images(rec_ids)
    links = gameids_to_links(rec_ids)
    return render_template("one_game.html", game=users_top_game, recs=rec_names, images=images, links=links)

  else:
    users_top_games, rec_names, rec_ids = get_user_recs(user_games)
    images = gameids_to_images(rec_ids)
    links = gameids_to_links(rec_ids)
    return render_template("recs.html", games=users_top_games, recs=rec_names, images=images, links=links)