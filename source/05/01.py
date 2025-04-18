sports = ['hockey', 'football']
favorite_sport = input('What is your favorite sport? ')
sports.append(favorite_sport)
sports.sort()
for sport in sports:
    print(sport)
