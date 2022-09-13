from tinder import Tinder

def main():
	function_dict = {'profile': tinder.profile, 'nearby': tinder.nearby,
					'matches': tinder.matches, 'like': tinder.like,
					'dislike': tinder.dislike}
	while True:
		user_input = input('Enter: ')
		user_input.lower()
		if user_input in function_dict:
			print(function_dict[user_input]())
		else:
			print('Invalid Input')

if __name__ == '__main__':
	tinder = Tinder('7cf84e76-f945-4988-85f7-788c57ca3463')
	main()