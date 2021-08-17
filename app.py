tedTalks = [
    {
		"id": 1,
		"tedTalk": "https://www.ted.com/talks/johann_hari_this_could_be_why_you_re_depressed_or_anxious"
	},
    {
		"id": 2,
		"tedTalk": "https://www.ted.com/talks/andrew_solomon_depression_the_secret_we_share?referrer=playlist-4_ted_talks_on_overcoming_depr"
	},
    {
		"id": 3,
		"tedTalk": "https://www.ted.com/talks/nikki_webber_allen_don_t_suffer_from_your_depression_in_silence?referrer=playlist-4_ted_talks_on_overcoming_depr"
	},
    {
		"id": 4,
		"tedTalk": "https://www.ted.com/talks/ruby_wax_what_s_so_funny_about_mental_illness?referrer=playlist-4_ted_talks_on_overcoming_depr"
	},
    {
		"id": 5,
		"tedTalk": "https://www.ted.com/talks/mariana_atencio_what_makes_you_special?language=en"
	},
    {
		"id": 6,
		"tedTalk": "https://www.ted.com/talks/carol_dweck_the_power_of_believing_that_you_can_improve?referrer=playlist-talks_for_when_you_feel_like_y"
	},
    {
		"id": 7,
		"tedTalk": "https://www.ted.com/talks/alain_de_botton_a_kinder_gentler_philosophy_of_success?referrer=playlist-talks_for_when_you_feel_like_y"
	},
    {
		"id": 8,
		"tedTalk": "https://www.ted.com/talks/shane_koyczan_to_this_day_for_the_bullied_and_beautiful?referrer=playlist-talks_for_when_you_feel_like_y"
	},
    {
		"id": 9,
		"tedTalk": "https://www.ted.com/talks/angela_lee_duckworth_grit_the_power_of_passion_and_perseverance?referrer=playlist-talks_for_when_you_feel_like_y"
	}
]

import flask
from flask import request, jsonify
import random

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return '''<h1>Distant Reading Archive</h1>
<p>A prototype API for distant reading of science fiction novels.</p>'''


@app.route('/api/songs/all', methods=['GET'])
def api_all():
    return jsonify(tedTalks)


@app.route('/api/songs/random', methods=['GET'])
def api_id():
    results = []
    r = random.randint(1,9)
    # r0 = str(r)
    # Loop through the data and match results that fit the requested ID.
    # IDs are unique, but other fields might return many results
    for talk in tedTalks:
        if talk['id'] == r:
            results.append(talk)

    # Use the jsonify function from Flask to convert our list of
    # Python dictionaries to the JSON format.
    return jsonify(results)
if __name__ == "__main__":
    app.run(debug = True, use_reloader=False)