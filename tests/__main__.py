from pyTinder import Tinder

def main():
	function_dict = {'profile': tinder.profile, 'nearby': tinder.nearby,
					'matches': tinder.matches, 'help': tinder.help}
	while True:
		user_input = input('Enter: ')
		user_input.lower()
		if user_input in function_dict:
			print(function_dict[user_input]())
		elif user_input == 'like':
			_id = input('Enter tweet ID: ')
			print(tinder.like(_id))
		elif user_input == 'dislike':
			_id = input('Enter tweet ID: ')
			print(tinder.dislike(_id))
		else:
			print('Invalid Input')

if __name__ == '__main__':
	tinder = Tinder('TOKEN')
	main()