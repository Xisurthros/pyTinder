# pyTinder

**pyTinder** is in the early stages of becoming a simple library used to communicate with the Tinder service directly.

## Contributing
> Check out [Contribution.md](https://github.com/Xisurthros/pyTinder/blob/master/Contribution.md) for how to get started with the Tinder API.

## Auth Token
> Check out [GetAuthToken.md](https://github.com/Xisurthros/pyTinder/blob/master/GetAuthToken.md) for a quick guide on getting your auth token.

## Main example:
```python
from tinder import Tinder

def main():
	function_dict = {'profile': tinder.profile, 'nearby': tinder.nearby,
					'matches': tinder.matches, 'like': tinder.like,
					'dislike': tinder.dislike, 'help': tinder.help}
	while True:
		user_input = input('Enter: ')
		user_input.lower()
		if user_input in function_dict:
			print(function_dict[user_input]())
		else:
			print('Invalid Input')

if __name__ == '__main__':
	tinder = Tinder('TOKEN')
	main()
```
TOKEN must be replaced with your TOKEN. Check out [AUTH Token](https://github.com/Xisurthros/pyTinder#auth-token) for details.

## Response example:
```python
>>> from tinder import Tinder

>>> tinder = Tinder('TOKEN')
>>> print(tinder.profile())
{'account_phone_number': '10000000000', 'account_email': 'Example@email.com', 'is_email_verified': True, 'apple_id_linked': False, 'facebook_id_linked': False, '_id': '00000000000000000000', 'age_filter_max': 1000, 'age_filter_min': 18, 'bio': "Example bio", 'birth_date': '2000-01-01T00:00:00.000Z', 'create_date': '2000-01-01T00:00:00.000Z'.....

>>> print(tinder.nearby())
[{'_id': '00000000000000000000', 'name': 'Example', 'bio': 'Example bio', 'gender': -1, 'birth_date': '2000-01-01T00:00:00.000Z', 'jobs': [], 'schools': [],.....

>>> print(tinder.help())
profile:         Get personal profile information.
nearby:          Get nearby profiles.
matches:         Get your 100 most recent matches.
like:            Like a certain user.
dislike:         Dislike a certain user.
```
pyTinder officially supports Python 3.7+.

## Supported Features
- [profile] - Get personal profile information.
- [nearby] - Get nearby profiles.
- [matches] - Get your 100 most recent matches.
- [like] - Like a certain user.
- [dislike] - Dislike a certain user.

## Data that can be gathered
#### - personal profile
> account_phone_number \
> account_email \
> is_email_verified \
> apple_id_linked \
> facebook_id_linked \
> _id \
> age_filter_max \
> age_filter_min \
> bio \
> birth_date \
> create_date \
> crm_id \
> pos_info \
> discoverable \
> distance_filter \
> global_mode \
> auto_expansion \
> gender \
> gender_filter \
> show_gender_on_profile \
> name \
> photos \
> photos_processing \
> photo_optimizer_enabled \
> ping_time \
> jobs \
> schools \
> badges \
> interested_in \
> pos \
> billing_info \
> autoplay_video \
> top_picks_discoverable \
> photo_tagging_enabled \
> city \
> show_orientation_on_profile \
> show_same_orientation_first \
> sexual_orientations \
> user_interests \
> recommended_sort_discoverable \
> selfie_verification \
> noonlight_protected \
> user_presence_disabled \
> sync_swipe_enabled \
> bumper_stickers \
> preference_filters

#### - nearby
> _id \
> name \
> bio \
> gender \
> birth_date \
> jobs \
> schools \
> badges \
> images

#### - matches
> seen \
> _id \
> closed \
> common_friend_count \
> common_like_count \
> created_date \
> dead \
> last_activity_date \
> message_count \
> messages \
> participants \
> pending \
> is_super_like \
> is_boost_match \
> is_super_boost_match \
> is_primetime_boost_match \
> is_experiences_match \
> is_fast_match \
> is_preferences_match \
> is_opener \
> has_shown_initial_interest \
> person \
> following \
> following_moments \
> readreceipt \
> is_archived

## Cloning the repository
```shell
git clone https://github.com/Xisurthros/pyTinder.git
```

## Furture plans
> Look into the automation for getting Auth Token. \
> Change profile information. \
> Publish as library to pypi.