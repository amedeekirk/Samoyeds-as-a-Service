dogs = {'Pekinese', 'Old_English_sheepdog', 'whippet', 'Japanese_spaniel', 'Walker_hound', 'Border_collie',
        'EntleBucher', 'Irish_terrier', 'schipperke', 'Tibetan_mastiff', 'Irish_water_spaniel', 'Bernese_mountain_dog',
        'bluetick', 'Lhasa', 'Newfoundland', 'Bouvier_des_Flandres', 'Samoyed', 'cairn', 'coyote', 'pug',
        'Norwich_terrier', 'bloodhound', 'toy_poodle', 'Welsh_springer_spaniel', 'Siberian_husky',
        'West_Highland_white_terrier', 'standard_schnauzer', 'Saluki', 'Weimaraner', 'Norfolk_terrier', 'affenpinscher',
        'German_shepherd', 'Greater_Swiss_Mountain_dog', 'flat-coated_retriever', 'silky_terrier', 'Leonberg', 'chow',
        'Tibetan_terrier', 'cocker_spaniel', 'Norwegian_elkhound', 'Sussex_spaniel', 'boxer', 'kuvasz', 'Airedale',
        'English_setter', 'dhole', 'Ibizan_hound', 'Great_Dane', 'malamute', 'Gordon_setter', 'African_hunting_dog',
        'Sealyham_terrier', 'Scotch_terrier', 'Irish_setter', 'clumber', 'redbone', 'malinois', 'toy_terrier',
        'Staffordshire_bullterrier', 'Shih-Tzu', 'Saint_Bernard', 'Mexican_hairless', 'English_springer',
        'curly-coated_retriever', 'Maltese_dog', 'French_bulldog', 'Labrador_retriever', 'standard_poodle',
        'Brittany_spaniel', 'white_wolf', 'Border_terrier', 'dalmatian', 'Dandie_Dinmont', 'Chihuahua', 'papillon',
        'Boston_bull', 'Pembroke', 'beagle', 'Chesapeake_Bay_retriever', 'Doberman', 'borzoi', 'Yorkshire_terrier',
        'Irish_wolfhound', 'Italian_greyhound', 'Cardigan', 'wire-haired_fox_terrier', 'dingo', 'basenji',
        'Great_Pyrenees', 'Australian_terrier', 'Kerry_blue_terrier', 'black-and-tan_coonhound', 'Eskimo_dog', 'collie',
        'komondor', 'miniature_poodle', 'English_foxhound', 'Rhodesian_ridgeback', 'vizsla', 'giant_schnauzer',
        'bull_mastiff', 'basset', 'Blenheim_spaniel', 'miniature_pinscher', 'Scottish_deerhound', 'golden_retriever',
        'otterhound', 'American_Staffordshire_terrier', 'kelpie', 'timber_wolf', 'groenendael', 'red_wolf',
        'German_short-haired_pointer', 'Afghan_hound', 'Bedlington_terrier', 'Appenzeller', 'keeshond',
        'Lakeland_terrier', 'miniature_schnauzer', 'briard', 'soft-coated_wheaten_terrier', 'Pomeranian', 'Rottweiler',
        'Shetland_sheepdog', 'Brabancon_griffon'}

# dogs = {'Chihuahua',
#         'Japanese spaniel',
#         'Maltese dog, Maltese terrier, Maltese',
#         'Pekinese, Pekingese, Peke',
#         'Shih-Tzu',
#         'Blenheim spaniel',
#         'papillon',
#         'toy terrier',
#         'Rhodesian ridgeback',
#         'Afghan hound, Afghan',
#         'basset, basset hound',
#         'beagle',
#         'bloodhound, sleuthhound',
#         'bluetick',
#         'black-and-tan coonhound',
#         'Walker hound, Walker foxhound',
#         'English foxhound',
#         'redbone',
#         'borzoi, Russian wolfhound',
#         'Irish wolfhound',
#         'Italian greyhound',
#         'whippet',
#         'Ibizan hound, Ibizan Podenco',
#         'Norwegian elkhound, elkhound',
#         'otterhound, otter hound',
#         'Saluki, gazelle hound',
#         'Scottish deerhound, deerhound',
#         'Weimaraner',
#         'Staffordshire bullterrier, Staffordshire bull terrier',
#         'American Staffordshire terrier, Staffordshire terrier, American pit bull terrier, pit bull terrier',
#         'Bedlington terrier',
#         'Border terrier',
#         'Kerry blue terrier',
#         'Irish terrier',
#         'Norfolk terrier',
#         'Norwich terrier',
#         'Yorkshire terrier',
#         'wire-haired fox terrier',
#         'Lakeland terrier',
#         'Sealyham terrier, Sealyham',
#         'Airedale, Airedale terrier',
#         'cairn, cairn terrier',
#         'Australian terrier',
#         'Dandie Dinmont, Dandie Dinmont terrier',
#         'Boston bull, Boston terrier',
#         'miniature schnauzer',
#         'giant schnauzer',
#         'standard schnauzer',
#         'Scotch terrier, Scottish terrier, Scottie',
#         'Tibetan terrier, chrysanthemum dog',
#         'silky terrier, Sydney silky',
#         'soft-coated wheaten terrier',
#         'West Highland white terrier',
#         'Lhasa, Lhasa apso',
#         'flat-coated retriever',
#         'curly-coated retriever',
#         'golden retriever',
#         'Labrador retriever',
#         'Chesapeake Bay retriever',
#         'German short-haired pointer',
#         'vizsla, Hungarian pointer',
#         'English setter',
#         'Irish setter, red setter',
#         'Gordon setter',
#         'Brittany spaniel',
#         'clumber, clumber spaniel',
#         'English springer, English springer spaniel',
#         'Welsh springer spaniel',
#         'cocker spaniel, English cocker spaniel, cocker',
#         'Sussex spaniel',
#         'Irish water spaniel',
#         'kuvasz',
#         'schipperke',
#         'groenendael',
#         'malinois',
#         'briard',
#         'kelpie',
#         'komondor',
#         'Old English sheepdog, bobtail',
#         'Shetland sheepdog, Shetland sheep dog, Shetland',
#         'collie',
#         'Border collie',
#         'Bouvier des Flandres, Bouviers des Flandres',
#         'Rottweiler',
#         'German shepherd, German shepherd dog, German police dog, alsatian',
#         'Doberman, Doberman pinscher',
#         'miniature pinscher',
#         'Greater Swiss Mountain dog',
#         'Bernese mountain dog',
#         'Appenzeller',
#         'EntleBucher',
#         'boxer',
#         'bull mastiff',
#         'Tibetan mastiff',
#         'French bulldog',
#         'Great Dane',
#         'Saint Bernard, St Bernard',
#         'Eskimo dog, husky',
#         'malamute, malemute, Alaskan malamute',
#         'Siberian husky',
#         'dalmatian, coach dog, carriage dog',
#         'affenpinscher, monkey pinscher, monkey dog',
#         'basenji',
#         'pug, pug-dog',
#         'Leonberg',
#         'Newfoundland, Newfoundland dog',
#         'Great Pyrenees',
#         'Samoyed, Samoyede',
#         'Pomeranian',
#         'chow, chow chow',
#         'keeshond',
#         'Brabancon griffon',
#         'Pembroke, Pembroke Welsh corgi',
#         'Cardigan, Cardigan Welsh corgi',
#         'toy poodle',
#         'miniature poodle',
#         'standard poodle',
#         'Mexican hairless',
#         'timber wolf, grey wolf, gray wolf, Canis lupus',
#         'white wolf, Arctic wolf, Canis lupus tundrarum',
#         'red wolf, maned wolf, Canis rufus, Canis niger',
#         'coyote, prairie wolf, brush wolf, Canis latrans',
#         'dingo, warrigal, warragal, Canis dingo',
#         'dhole, Cuon alpinus',
#         'African hunting dog, hyena dog, Cape hunting dog, Lycaon pictus'
#         }
#
#
