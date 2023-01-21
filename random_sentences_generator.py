import random

places = ['Burgas', 'Nesebar', 'Pomorie', 'Sozopol', 'Sunny Beach', 'Kavarna']
verbs = ['swims', 'eats', 'sleeps with', 'says', 'sees', 'drinks', 'code with']
nouns = ['computer', 'ice cream', 'fish', 'sun', 'sea', 'beer', 'sand']
adverbs = ['happily', 'warmly', 'dirty', 'funny', 'friendly', 'nearly']
details = ['on the beach', 'in the hotel', 'around the bar', 'at home', 'at work', 'on the seaside']


def get_random_choise(words):
    return random.choice(words)


while True:
    input_name = input("Write here one name: ")

    random_place = get_random_choise(places)
    random_verb = get_random_choise(verbs)
    random_noun = get_random_choise(nouns)
    random_adverb = get_random_choise(adverbs)
    random_detail = get_random_choise(details)
    print(f"{input_name} from {random_place} {random_verb} {random_noun} {random_adverb} {random_detail}.")
