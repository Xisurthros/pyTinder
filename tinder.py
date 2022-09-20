import requests, json, sys

# Base tinder api url
TINDER_URL = "https://api.gotinder.com"

# Check if user has bio. Bio Error can occur otherwise
def bio(match):

	try:
		return(match['person']['bio'])
	except KeyError:
		return 'No Bio'

# Handles all errors
def errorHandling(token = None, profile = None, nearby = None, matches = None, like = None, dislike = None):
	if token:
		print('Error: Invalid token.')
		sys.exit(1)

	elif profile:
		return 'Error: No information available. This may be due to issues on Tinder server side.'

	elif nearby:
		return 'Error: No information available. This may be Tinder server issues or a lack of users nearby.'

	elif matches:
		return 'Error: No information available. This may be Tinder server issues or a lack matches.'

	elif like or dislike:
		return 'Error: Invalid value _id. User ID passed to function is not a valid user ID.'

# Check to confirm if token is valid
def confirmToken(token):
	try:
		requests.get(f'{TINDER_URL}/v2/profile?include=account%2Cuser', headers={'X-Auth-Token': token}).json()
		return(token)
	except ValueError:
		errorHandling(token = True)

class Tinder:

	def __init__(self, token):
		self.token = confirmToken(token) # Send token to function to confirm if valid
		self.headers = {'X-Auth-Token': self.token}

	def profile(self):
		try:
			data = requests.get(f'{TINDER_URL}/v2/profile?include=account%2Cuser', headers=self.headers).json()
			account = data['data']['account']
			user = data['data']['user']
			user_profile = {
				'account_phone_number': account['account_phone_number'],
				'account_email': account['account_email'],
				'is_email_verified': account['is_email_verified'],
				'apple_id_linked': account['apple_id_linked'],
				'facebook_id_linked': account['facebook_id_linked'],
				'_id': user['_id'],
				'age_filter_max': user['age_filter_max'],
				'age_filter_min': user['age_filter_min'],
				'bio': user['bio'],
				'birth_date': user['birth_date'],
				'create_date': user['create_date'],
				'crm_id': user['crm_id'],
				'pos_info': user['pos_info'],
				'discoverable': user['discoverable'],
				'distance_filter': user['distance_filter'],
				'global_mode': user['global_mode'],
				'auto_expansion': user['auto_expansion'],
				'gender': user['gender'],
				'gender_filter': user['gender_filter'],
				'show_gender_on_profile': user['show_gender_on_profile'],
				'name': user['name'],
				'photos': user['photos'],
				'photos_processing': user['photos_processing'],
				'photo_optimizer_enabled': user['photo_optimizer_enabled'],
				'ping_time': user['ping_time'],
				'jobs': user['jobs'],
				'schools': user['schools'],
				'badges': user['badges'],
				'interested_in': user['interested_in'],
				'pos': user['pos'],
				'billing_info': user['billing_info'],
				'autoplay_video': user['autoplay_video'],
				'top_picks_discoverable': user['top_picks_discoverable'],
				'photo_tagging_enabled': user['photo_tagging_enabled'],
				'city': user['city'],
				'show_orientation_on_profile': user['show_orientation_on_profile'],
				'show_same_orientation_first': user['show_same_orientation_first'],
				'sexual_orientations': user['sexual_orientations'],
				'user_interests': user['user_interests'],
				'recommended_sort_discoverable': user['recommended_sort_discoverable'],
				'selfie_verification': user['selfie_verification'],
				'noonlight_protected': user['noonlight_protected'],
				'user_presence_disabled': user['user_presence_disabled'],
				'sync_swipe_enabled': user['sync_swipe_enabled'],
				'bumper_stickers': user['bumper_stickers'],
				'preference_filters': user['preference_filters']
			}
			return user_profile
		except ValueError:
			errorHandling(profile = True)

	def nearby(self):
		try:
			data = requests.get(f'{TINDER_URL}/v2/recs/core', headers=self.headers).json()
			users = []
			for person in data['data']['results']:
				user = {
					'_id': person['user']['_id'],
					'name': person['user']['name'],
					'bio': person['user']['bio'],
					'gender': person['user']['gender'],
					'birth_date': person['user']['birth_date'],
					'jobs': person['user']['jobs'],
					'schools': person['user']['schools'],
					'badges': person['user']['badges'],
					'images': [image['url'] for image in person['user']['photos']]
				}
				users.append(user)
			return users
		except ValueError:
			errorHandling(neary = True)

	def matches(self):
		try:
			data = requests.get(f'{TINDER_URL}/v2/matches?locale=en&count=100&message=1&is_tinder_', headers=self.headers).json()
			users = []
			for match in data['data']['matches']:
				user = {
					'name': match['person']['name'],
					'bio': bio(match),
					'birth_date': match['person']['birth_date'],
					'photos': [photo['url'] for photo in match['person']['photos'][0]['processedFiles']],
					'seen': match['seen'],
					'_id': match['_id'],
					'closed': match['closed'],
					'common_friend_count': match['common_friend_count'],
					'common_like_count': match['common_like_count'],
					'created_date': match['created_date'],
					'dead': match['dead'],
					'last_activity_date': match['last_activity_date'],
					'message_count': match['message_count'],
					'messages': match['messages'],
					'participants': match['participants'],
					'pending': match['pending'],
					'is_super_like': match['is_super_like'],
					'is_boost_match': match['is_boost_match'],
					'is_super_boost_match': match['is_super_boost_match'],
					'is_primetime_boost_match': match['is_primetime_boost_match'],
					'is_experiences_match': match['is_experiences_match'],
					'is_fast_match': match['is_fast_match'],
					'is_preferences_match': match['is_preferences_match'],
					'is_opener': match['is_opener'],
					'has_shown_initial_interest': match['has_shown_initial_interest'],
					'person': match['person'],
					'following': match['following'],
					'following_moments': match['following_moments'],
					'readreceipt': match['readreceipt'],
					'is_archived': match['is_archived'],
				}
				users.append(user)
			return users
		except ValueError:
			return errorHandling(matches = True)

	def like(self, _id = None):
		try:
			if _id is not None and _id != '':
				requests.get(f'{TINDER_URL}/like/{_id}', headers=self.headers).json()
				return f'Liked {_id}.'
			else:
				return 'Missing vaule: _id (user ID must be declared).'
		except ValueError:
			return errorHandling(like = True)

	def dislike(self, _id = None):
		try:
			if _id is not None and _id != '':
				requests.get(f'{TINDER_URL}/pass/{_id}', headers=self.headers).json()
				return f'Disliked {_id}'
			else:
				return 'Missing vaule: _id (user ID must be declared).'
		except ValueError:
			return errorHandling(dislike = True)

	def help(self):
		return 'profile:\t\t Get personal profile information.\n'\
			   'nearby:\t\t\t Get nearby profiles.\n'\
			   'matches:\t\t Get your 100 most recent matches.\n'\
			   'like(_id):\t\t Like a certain user.\n'\
			   'dislike(_id):\t\t Dislike a certain user.'