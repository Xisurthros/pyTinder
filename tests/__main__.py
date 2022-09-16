from pyTinder import Tinder

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