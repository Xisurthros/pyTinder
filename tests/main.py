from tinder import Tinder

def main():
	function_dict = {'profile': tinder.profile, 'nearby': tinder.nearby,
					'matches': tinder.matches, 'setBio': tinder.setBio,
					'like': tinder.like, 'dislike': tinder.dislike}
	while True:
		user_input = input('Enter: ')
		user_input.lower()
		if user_input in function_dict:
			print(function_dict[user_input]())
		elif user_input == 'like':
			tinder.like
		else:
			print('Invalid Input')

if __name__ == '__main__':
	tinder = Tinder('TOKEN')
	main()