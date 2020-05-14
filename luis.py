import luis

# Use the URL LUIS gives you when you publish your api
l = luis.Luis(url='https://https://api.projectoxford.ai/luis/...')

# Send text to be analyzed:
r = l.analyze('fly forward 10 feet')