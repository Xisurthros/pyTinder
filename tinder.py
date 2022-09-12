import requests

TINDER_URL = "https://api.gotinder.com"

class Tinder:

	def __init__(self, token):
		self.token = token
		self.headers = {'X-Auth-Token': self.token}

	def profile(self):
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

	def nearby(self):
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