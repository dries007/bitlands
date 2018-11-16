import os, re, math

'''
	A script to auto-generate Bitlands creature raws.
	Place the objects folder next to this script to generate patches.
'''

# Tile and color of each creature
creature_data = {
	'TOAD':('CRE_ANURA', 'OLIVE'),
	'TOAD_MAN':('MAN_ANURA', 'OLIVE'),
	'GIANT_TOAD':('CRE_ANURA', 'OLIVE'),
	'WORM':('CRE_TUBE', 'PINK'),
	'WORM_MAN':('MAN_TUBE', 'PINK'),
	'BIRD_BLUEJAY':('CRE_BIRD_SMALL', 'BLUE'),
	'BLUEJAY_MAN':('MAN_BIRD_SMALL', 'BLUE'),
	'GIANT_BLUEJAY':('CRE_BIRD_SMALL', 'BLUE'),
	'BIRD_CARDINAL':('CRE_BIRD_SMALL', 'RED'),
	'CARDINAL_MAN':('MAN_BIRD_SMALL', 'RED'),
	'GIANT_CARDINAL':('CRE_BIRD_SMALL', 'RED'),
	'BIRD_GRACKLE':('CRE_BIRD_SMALL', 'GREEN'),
	'GRACKLE_MAN':('MAN_BIRD_SMALL', 'GREEN'),
	'GIANT_GRACKLE':('CRE_BIRD_SMALL', 'GREEN'),
	'BIRD_ORIOLE':('CRE_BIRD_SMALL', 'YELLOW'),
	'ORIOLE_MAN':('MAN_BIRD_SMALL', 'YELLOW'),
	'GIANT_ORIOLE':('CRE_BIRD_SMALL', 'YELLOW'),
	'BIRD_RW_BLACKBIRD':('CRE_BIRD_SMALL', 'NAVY'),
	'RW_BLACKBIRD_MAN':('MAN_BIRD_SMALL', 'NAVY'),
	'GIANT_RW_BLACKBIRD':('CRE_BIRD_SMALL', 'NAVY'),
	'BIRD_PENGUIN':('CRE_BIRD_NOFLY', 'WHITE'),
	'BIRD_PENGUIN_LITTLE':('CRE_BIRD_NOFLY', 'NAVY'),
	'BIRD_PENGUIN_EMPEROR':('CRE_BIRD_NOFLY', 'WHITE'),
	'PENGUIN MAN':('CRE_BIRD_NOFLY', 'WHITE'),
	'BIRD_PENGUIN_GIANT':('CRE_BIRD_NOFLY', 'WHITE'),
	'BIRD_FALCON_PEREGRINE':('CRE_BIRD_SMALL', 'OLIVE'),
	'PEREGRINE FALCON MAN':('MAN_BIRD_SMALL', 'OLIVE'),
	'GIANT PEREGRINE FALCON':('CRE_BIRD_SMALL', 'OLIVE'),
	'BIRD_KIWI':('CRE_BIRD_SMALL', 'OLIVE'),
	'KIWI MAN':('MAN_BIRD_SMALL', 'OLIVE'),
	'BIRD_KIWI_GIANT':('CRE_BIRD_SMALL', 'OLIVE'),
	'BIRD_OSTRICH':('CRE_BIRD_TALL', 'SILVER'),
	'OSTRICH MAN':('MAN_BIRD_TALL', 'SILVER'),
	'BIRD_OSTRICH_GIANT':('CRE_BIRD_TALL', 'SILVER'),
	'BIRD_CROW':('CRE_BIRD_SMALL', 'BLUE'),
	'CROW_MAN':('MAN_BIRD_SMALL', 'BLUE'),
	'GIANT_CROW':('CRE_BIRD_SMALL', 'BLUE'),
	'BIRD_RAVEN':('CRE_BIRD_SMALL', 'PURPLE'),
	'RAVEN_MAN':('MAN_BIRD_SMALL', 'PURPLE'),
	'GIANT_RAVEN':('CRE_BIRD_SMALL', 'PURPLE'),
	'BIRD_CASSOWARY':('CRE_BIRD_TALL', 'CYAN'),
	'CASSOWARY_MAN':('MAN_BIRD_TALL', 'CYAN'),
	'GIANT_CASSOWARY':('CRE_BIRD_TALL', 'CYAN'),
	'BIRD_KEA':('CRE_BIRD_BIG', 'OLIVE'),
	'KEA_MAN':('MAN_BIRD_BIG', 'OLIVE'),
	'GIANT_KEA':('CRE_BIRD_BIG', 'OLIVE'),
	'BIRD_OWL_SNOWY':('CRE_BIRD_BIG', 'WHITE'),
	'SNOWY_OWL_MAN':('MAN_BIRD_BIG', 'WHITE'),
	'GIANT_SNOWY_OWL':('CRE_BIRD_BIG', 'WHITE'),
	'SPARROW':('CRE_BIRD_BIG', 'WHITE'),
	'SPARROW_MAN':('MAN_BIRD_BIG', 'WHITE'),
	'GIANT_SPARROW':('CRE_BIRD_BIG', 'WHITE'),
	'BIRD_STORK_WHITE':('CRE_BIRD_TALL', 'WHITE'),
	'WHITE_STORK_MAN':('MAN_BIRD_TALL', 'WHITE'),
	'GIANT_WHITE_STORK':('CRE_BIRD_TALL', 'WHITE'),
	'BIRD_LOON':('CRE_BIRD_TALL', 'GRAY'),
	'LOON_MAN':('MAN_BIRD_TALL', 'GRAY'),
	'GIANT_LOON':('CRE_BIRD_TALL', 'GRAY'),
	'BIRD_OWL_BARN':('CRE_BIRD_BIG', 'OLIVE'),
	'BARN_OWL_MAN':('MAN_BIRD_BIG', 'OLIVE'),
	'GIANT_BARN_OWL':('CRE_BIRD_BIG', 'OLIVE'),
	'BIRD_PARAKEET':('CRE_BIRD_BIG', 'LIME'),
	'PARAKEET_MAN':('MAN_BIRD_BIG', 'LIME'),
	'GIANT_PARAKEET':('CRE_BIRD_BIG', 'LIME'),
	'BIRD_KAKAPO':('CRE_BIRD_BIG', 'GREEN'),
	'KAKAPO_MAN':('MAN_BIRD_BIG', 'GREEN'),
	'GIANT_KAKAPO':('CRE_BIRD_BIG', 'GREEN'),
	'BIRD_PARROT_GREY':('CRE_BIRD_BIG', 'GRAY'),
	'GREY_PARROT_MAN':('MAN_BIRD_BIG', 'GRAY'),
	'GIANT_GREY_PARROT':('CRE_BIRD_BIG', 'GRAY'),
	'BIRD_PUFFIN':('CRE_BIRD_BIG', 'NAVY'),
	'PUFFIN_MAN':('MAN_BIRD_BIG', 'NAVY'),
	'GIANT_PUFFIN':('CRE_BIRD_BIG', 'NAVY'),
	'BIRD_SWAN':('CRE_BIRD_TALL', 'WHITE'),
	'SWAN_MAN':('MAN_BIRD_TALL', 'WHITE'),
	'GIANT_SWAN':('CRE_BIRD_TALL', 'WHITE'),
	'BIRD_LORIKEET':('CRE_BIRD_BIG', 'RED'),
	'LORIKEET_MAN':('MAN_BIRD_BIG', 'RED'),
	'GIANT_LORIKEET':('CRE_BIRD_BIG', 'RED'),
	'BIRD_WREN':('CRE_BIRD_SMALL', 'OLIVE'),
	'WREN_MAN':('MAN_BIRD_SMALL', 'OLIVE'),
	'GIANT_WREN':('CRE_BIRD_SMALL', 'OLIVE'),
	'BIRD_OSPREY':('CRE_BIRD_BIG', 'MAROON'),
	'OSPREY_MAN':('MAN_BIRD_BIG', 'MAROON'),
	'GIANT_OSPREY':('CRE_BIRD_BIG', 'MAROON'),
	'BIRD_EMU':('CRE_BIRD_TALL', 'GRAY'),
	'EMU_MAN':('MAN_BIRD_TALL', 'GRAY'),
	'GIANT_EMU':('CRE_BIRD_TALL', 'GRAY'),
	'BIRD_COCKATIEL':('CRE_BIRD_BIG', 'YELLOW'),
	'COCKATIEL_MAN':('MAN_BIRD_BIG', 'YELLOW'),
	'GIANT_COCKATIEL':('CRE_BIRD_BIG', 'YELLOW'),
	'BIRD_LOVEBIRD_PEACH-FACED':('CRE_BIRD_BIG', 'LIME'),
	'PEACH-FACED_LOVEBIRD_MAN':('MAN_BIRD_BIG', 'LIME'),
	'GIANT_PEACH-FACED_LOVEBIRD':('CRE_BIRD_BIG', 'LIME'),
	'BIRD_MAGPIE':('CRE_BIRD_SMALL', 'NAVY'),
	'MAGPIE_MAN':('MAN_BIRD_SMALL', 'NAVY'),
	'GIANT_MAGPIE':('CRE_BIRD_SMALL', 'NAVY'),
	'BIRD_KESTREL':('CRE_BIRD_BIG', 'OLIVE'),
	'KESTREL_MAN':('MAN_BIRD_BIG', 'OLIVE'),
	'GIANT_KESTREL':('CRE_BIRD_BIG', 'OLIVE'),
	'BIRD_ALBATROSS':('CRE_BIRD_TALL', 'WHITE'),
	'ALBATROSS_MAN':('MAN_BIRD_TALL', 'WHITE'),
	'GIANT_ALBATROSS':('CRE_BIRD_TALL', 'WHITE'),
	'BIRD_OWL_GREAT_HORNED':('CRE_BIRD_BIG', 'OLIVE'),
	'GREAT_HORNED_OWL_MAN':('MAN_BIRD_BIG', 'OLIVE'),
	'GIANT_GREAT_HORNED_OWL':('CRE_BIRD_BIG', 'OLIVE'),
	'BIRD_EAGLE':('CRE_BIRD_BIG', 'MAROON'),
	'EAGLE_MAN':('MAN_BIRD_BIG', 'MAROON'),
	'GIANT_EAGLE':('CRE_BIRD_BIG', 'MAROON'),
	'BIRD_HORNBILL':('CRE_BIRD_BIG', 'NAVY'),
	'HORNBILL_MAN':('MAN_BIRD_BIG', 'NAVY'),
	'GIANT_HORNBILL':('CRE_BIRD_BIG', 'NAVY'),
	'BIRD_LOVEBIRD_MASKED':('CRE_BIRD_BIG', 'CYAN'),
	'MASKED_LOVEBIRD_MAN':('MAN_BIRD_BIG', 'CYAN'),
	'GIANT_MASKED_LOVEBIRD':('CRE_BIRD_BIG', 'CYAN'),
	'BIRD_BUSHTIT':('CRE_BIRD_SMALL', 'OLIVE'),
	'BUSHTIT_MAN':('MAN_BIRD_SMALL', 'OLIVE'),
	'GIANT_BUSHTIT':('CRE_BIRD_SMALL', 'OLIVE'),
	'DAMSELFLY':('CRE_BUG_FLY', 'CYAN'),
	'DAMSELFLY_MAN':('MAN_BUG_FLY', 'CYAN'),
	'GIANT_DAMSELFLY':('CRE_BUG_FLY', 'CYAN'),
	'MOTH':('CRE_BUG_FLY', 'OLIVE'),
	'MOTH_MAN':('MAN_BUG_FLY', 'OLIVE'),
	'GIANT_MOTH':('CRE_BUG_FLY', 'OLIVE'),
	'GRASSHOPPER':('CRE_BUG_GROUND', 'LIME'),
	'GRASSHOPPER_MAN':('MAN_BUG_GROUND', 'LIME'),
	'GIANT_GRASSHOPPER':('CRE_BUG_GROUND', 'LIME'),
	'BARK_SCORPION':('CRE_BUG_GROUND', 'OLIVE'),
	'BARK_SCORPION_MAN':('MAN_BUG_GROUND', 'OLIVE'),
	'GIANT_BARK_SCORPION':('CRE_BUG_GROUND', 'OLIVE'),
	'MANTIS':('CRE_BUG_GROUND', 'LIME'),
	'MANTIS_MAN':('MAN_BUG_GROUND', 'LIME'),
	'GIANT_MANTIS':('CRE_BUG_GROUND', 'LIME'),
	'TICK':('CRE_BUG_GROUND', 'MAROON'),
	'TICK_MAN':('MAN_BUG_GROUND', 'MAROON'),
	'GIANT_TICK':('CRE_BUG_GROUND', 'MAROON'),
	'LOUSE':('CRE_BUG_GROUND', 'GRAY'),
	'LOUSE_MAN':('MAN_BUG_GROUND', 'GRAY'),
	'GIANT_LOUSE':('CRE_BUG_GROUND', 'GRAY'),
	'THRIPS':('CRE_BUG_GROUND', 'OLIVE'),
	'THRIPS_MAN':('MAN_BUG_GROUND', 'OLIVE'),
	'GIANT_THRIPS':('CRE_BUG_GROUND', 'OLIVE'),
	'SLUG':('CRE_TUBE', 'MAROON'),
	'SLUG_MAN':('MAN_TUBE', 'MAROON'),
	'GIANT_SLUG':('CRE_TUBE', 'MAROON'),
	'MOSQUITO':('CRE_BUG_FLY', 'MAROON'),
	'MOSQUITO_MAN':('MAN_BUG_FLY', 'MAROON'),
	'GIANT_MOSQUITO':('CRE_BUG_FLY', 'MAROON'),
	'SPIDER_JUMPING':('CRE_BUG_GROUND', 'OLIVE'),
	'JUMPING_SPIDER_MAN':('MAN_BUG_GROUND', 'OLIVE'),
	'GIANT_JUMPING_SPIDER':('CRE_BUG_GROUND', 'OLIVE'),
	'TERMITE':('CRE_BUG_GROUND', 'WHITE'),
	'MOON_SNAIL':('CRE_SHELLED', 'WHITE'),
	'MOON_SNAIL_MAN':('MAN_SHELLED', 'WHITE'),
	'GIANT_MOON_SNAIL':('CRE_SHELLED', 'WHITE'),
	'SPIDER_BROWN_RECLUSE':('CRE_BUG_GROUND', 'MAROON'),
	'BROWN_RECLUSE_SPIDER_MAN':('MAN_BUG_GROUND', 'MAROON'),
	'GIANT_BROWN_RECLUSE_SPIDER':('CRE_BUG_GROUND', 'MAROON'),
	'SNAIL':('CRE_SHELLED', 'OLIVE'),
	'SNAIL_MAN':('MAN_SHELLED', 'OLIVE'),
	'GIANT_SNAIL':('CRE_SHELLED', 'OLIVE'),
	'GECKO_LEOPARD':('CRE_LIZARD', 'YELLOW'),
	'LEOPARD_GECKO_MAN':('MAN_LIZARD', 'YELLOW'),
	'GIANT_LEOPARD_GECKO':('CRE_LIZARD', 'YELLOW'),
	'DESERT TORTOISE':('CRE_SHELLED', 'OLIVE'),
	'DESERT_TORTOISE_MAN':('MAN_SHELLED', 'OLIVE'),
	'GIANT_DESERT_TORTOISE':('CRE_SHELLED', 'OLIVE'),
	'GILA_MONSTER':('CRE_LIZARD', 'RED'),
	'GILA_MONSTER_MAN':('MAN_LIZARD', 'RED'),
	'GIANT_GILA_MONSTER':('CRE_LIZARD', 'RED'),
	'DOG':('CRE_CANINE', 'YELLOW'),
	'CAT':('CRE_FELINE', 'SILVER'),
	'MULE':('CRE_EQUINE', 'OLIVE'),
	'DONKEY':('CRE_EQUINE', 'GRAY'),
	'HORSE':('CRE_EQUINE', 'MAROON'),
	'COW':('CRE_EQUINE', 'WHITE'),
	'SHEEP':('CRE_EQUINE', 'WHITE'),
	'PIG':('CRE_BULKY', 'PINK'),
	'GOAT':('CRE_EQUINE', 'MAROON'),
	'BIRD_CHICKEN':('CRE_BIRD_SMALL', 'WHITE'),
	'CAVY':('CRE_RODENT', 'MAROON'),
	'BIRD_DUCK':('CRE_BIRD_TALL', 'WHITE'),
	'WATER_BUFFALO':('CRE_EQUINE', 'NAVY'),
	'REINDEER':('CRE_EQUINE', 'MAROON'),
	'BIRD_GOOSE':('CRE_BIRD_TALL', 'GRAY'),
	'YAK':('CRE_EQUINE', 'MAROON'),
	'LLAMA':('CRE_EQUINE', 'SILVER'),
	'ALPACA':('CRE_EQUINE', 'YELLOW'),
	'BIRD_GUINEAFOWL':('CRE_BIRD_TALL', 'TEAL'),
	'BIRD_PEAFOWL_BLUE':('CRE_BIRD_TALL', 'BLUE'),
	'BIRD_TURKEY':('CRE_BIRD_TALL', 'MAROON'),
	'RABBIT':('CRE_RODENT', 'WHITE'),
	'EQUIPMENT_WAGON':('CRE_VEHICLE', 'OLIVE'),
	'CHIMERA':('CRE_FELINE', 'YELLOW'),
	'CENTAUR':('MAN_EQUINE', 'MAROON'),
	'GRIFFON':('CRE_FELINE', 'OLIVE'),
	'FLY':('CRE_BUG_FLY', 'NAVY'),
	'FLY_MAN':('MAN_BUG_FLY', 'NAVY'),
	'GIANT_FLY':('CRE_BUG_FLY', 'NAVY'),
	'ROACH_LARGE':('CRE_BUG_GROUND', 'MAROON'),
	'ROACH_MAN':('MAN_BUG_GROUND', 'MAROON'),
	'GIANT_ROACH':('CRE_BUG_GROUND', 'MAROON'),
	'BEETLE':('CRE_BUG_GROUND', 'NAVY'),
	'BEETLE_MAN':('MAN_BUG_GROUND', 'NAVY'),
	'GIANT_BEETLE':('CRE_BUG_GROUND', 'NAVY'),
	'ANT':('CRE_BUG_GROUND', 'MAROON'),
	'BUTTERFLY_MONARCH':('CRE_BUG_FLY', 'RED'),
	'BUTTERFLY_MONARCH_MAN':('MAN_BUG_FLY', 'RED'),
	'GIANT_BUTTERFLY_MONARCH':('CRE_BUG_FLY', 'RED'),
	'FIREFLY':('CRE_BUG_FLY', 'YELLOW'),
	'FIREFLY_MAN':('MAN_BUG_FLY', 'YELLOW'),
	'GIANT_FIREFLY':('CRE_BUG_FLY', 'YELLOW'),
	'DRAGONFLY':('CRE_BUG_FLY', 'RED'),
	'DRAGONFLY_MAN':('MAN_BUG_FLY', 'RED'),
	'GIANT_DRAGONFLY':('CRE_BUG_FLY', 'RED'),
	'HONEY_BEE':('CRE_BUG_FLY', 'OLIVE'),
	'BUMBLEBEE':('CRE_BUG_FLY', 'YELLOW'),
	'GOAT_MOUNTAIN':('CRE_EQUINE', 'WHITE'),
	'GOAT_MOUNTAIN_MAN':('MAN_EQUINE', 'WHITE'),
	'GIANT_GOAT_MOUNTAIN':('CRE_EQUINE', 'WHITE'),
	'MARMOT_HOARY':('CRE_RODENT', 'SILVER'),
	'MARMOT_HOARY_MAN':('MAN_RODENT', 'SILVER'),
	'GIANT_MARMOT_HOARY':('CRE_RODENT', 'SILVER'),
	'GNOME_MOUNTAIN':('CRE_HOMINID', 'GRAY'),
	'GNOME_DARK':('CRE_HOMINID', 'TEAL'),
	'WALRUS':('CRE_PINNIPED', 'OLIVE'),
	'WALRUS_MAN':('MAN_PINNIPED', 'OLIVE'),
	'GIANT_WALRUS':('CRE_PINNIPED', 'OLIVE'),
	'FISH_LAMPREY_SEA':('CRE_TUBE', 'OLIVE'),
	'SHARK_GREAT_WHITE':('CRE_FISH_BIG', 'SILVER'),
	'SHARK_FRILL':('CRE_TUBE', 'GRAY'),
	'SHARK_SPINY_DOGFISH':('CRE_FISH_BIG', 'OLIVE'),
	'SHARK_WOBBEGONG_SPOTTED':('CRE_FISH_FLAT', 'OLIVE'),
	'SHARK_WHALE':('CRE_FISH_BIG', 'MAROON'),
	'SHARK_BASKING':('CRE_FISH_BIG', 'GRAY'),
	'SHARK_NURSE':('CRE_FISH_BIG', 'MAROON'),
	'SHARK_MAKO_SHORTFIN':('CRE_FISH_BIG', 'SILVER'),
	'SHARK_MAKO_LONGFIN':('CRE_FISH_BIG', 'BLUE'),
	'SHARK_TIGER':('CRE_FISH_BIG', 'OLIVE'),
	'SHARK_BULL':('CRE_FISH_BIG', 'GRAY'),
	'SHARK_REEF_BLACKTIP':('CRE_FISH_BIG', 'OLIVE'),
	'SHARK_REEF_WHITETIP':('CRE_FISH_BIG', 'GRAY'),
	'SHARK_BLUE':('CRE_FISH_BIG', 'CYAN'),
	'SHARK_HAMMERHEAD':('CRE_FISH_BIG', 'OLIVE'),
	'SHARK_ANGEL':('CRE_FISH_FLAT', 'OLIVE'),
	'FISH_SKATE_COMMON':('CRE_FISH_FLAT', 'OLIVE'),
	'FISH_RAY_MANTA':('CRE_FISH_FLAT', 'NAVY'),
	'FISH_STINGRAY':('CRE_FISH_FLAT', 'GRAY'),
	'FISH_COELACANTH':('CRE_FISH_LONG', 'GRAY'),
	'FISH_STURGEON':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_CONGER_EEL':('CRE_TUBE', 'NAVY'),
	'FISH_MILKFISH':('CRE_FISH_LONG', 'WHITE'),
	'FISH_COD':('CRE_FISH_LONG', 'YELLOW'),
	'FISH_OPAH':('CRE_FISH_SMALL', 'RED'),
	'FISH_GROUPER_GIANT':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_BLUEFISH':('CRE_FISH_LONG', 'WHITE'),
	'FISH_SUNFISH_OCEAN':('CRE_FISH_SMALL', 'WHITE'),
	'FISH_SWORDFISH':('CRE_FISH_LONG', 'SILVER'),
	'FISH_MARLIN':('CRE_FISH_LONG', 'BLUE'),
	'FISH_HALIBUT':('CRE_FISH_SMALL', 'OLIVE'),
	'FISH_BARRACUDA_GREAT':('CRE_FISH_LONG', 'CYAN'),
	'FISH_TUNA_BLUEFIN':('CRE_FISH_SMALL', 'SILVER'),
	'NARWHAL':('CRE_PINNIPED', 'GRAY'),
	'NARWHAL MAN':('MAN_PINNIPED', 'GRAY'),
	'NARWHAL, GIANT':('CRE_PINNIPED', 'GRAY'),
	'HIPPO':('CRE_BULKY', 'GRAY'),
	'HIPPO_MAN':('MAN_BULKY', 'GRAY'),
	'GIANT_HIPPO':('CRE_BULKY', 'GRAY'),
	'FISH_GAR_LONGNOSE':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_CARP':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_TIGERFISH':('CRE_FISH_LONG', 'SILVER'),
	'FISH_PIKE':('CRE_FISH_LONG', 'YELLOW'),
	'PLATYPUS':('CRE_RODENT', 'MAROON'),
	'PLATYPUS MAN':('MAN_RODENT', 'MAROON'),
	'PLATYPUS, GIANT':('CRE_RODENT', 'MAROON'),
	'BEAR_GRIZZLY':('CRE_BULKY', 'MAROON'),
	'BEAR_GRIZZLY_MAN':('MAN_BULKY', 'MAROON'),
	'GIANT_BEAR_GRIZZLY':('CRE_BULKY', 'MAROON'),
	'BEAR_BLACK':('CRE_BULKY', 'NAVY'),
	'BEAR_BLACK_MAN':('MAN_BULKY', 'NAVY'),
	'GIANT_BEAR_BLACK':('CRE_BULKY', 'NAVY'),
	'DEER':('CRE_EQUINE', 'OLIVE'),
	'DEER_MAN':('MAN_EQUINE', 'OLIVE'),
	'GIANT_DEER':('CRE_EQUINE', 'OLIVE'),
	'FOX':('CRE_CANINE', 'RED'),
	'FOX_MAN':('MAN_CANINE', 'RED'),
	'GIANT_FOX':('CRE_CANINE', 'RED'),
	'RACCOON':('CRE_CANINE', 'GRAY'),
	'RACCOON_MAN':('MAN_CANINE', 'GRAY'),
	'GIANT_RACCOON':('CRE_CANINE', 'GRAY'),
	'MACAQUE_RHESUS':('CRE_PRIMATE', 'OLIVE'),
	'MACAQUE_RHESUS_MAN':('MAN_PRIMATE', 'OLIVE'),
	'GIANT_MACAQUE_RHESUS':('CRE_PRIMATE', 'OLIVE'),
	'COUGAR':('CRE_FELINE', 'OLIVE'),
	'COUGAR_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_COUGAR':('CRE_FELINE', 'OLIVE'),
	'WOLF':('CRE_CANINE', 'GRAY'),
	'WOLF_MAN':('MAN_CANINE', 'GRAY'),
	'GIANT_WOLF':('CRE_CANINE', 'GRAY'),
	'GROUNDHOG':('CRE_RODENT', 'OLIVE'),
	'GROUNDHOG_MAN':('MAN_RODENT', 'OLIVE'),
	'GIANT_GROUNDHOG':('CRE_RODENT', 'OLIVE'),
	'ALLIGATOR':('CRE_LIZARD', 'NAVY'),
	'ALLIGATOR_MAN':('MAN_LIZARD', 'NAVY'),
	'GIANT_ALLIGATOR':('CRE_LIZARD', 'NAVY'),
	'BIRD_BUZZARD':('CRE_BIRD_BIG', 'MAROON'),
	'BUZZARD_MAN':('MAN_BIRD_BIG', 'MAROON'),
	'GIANT_BUZZARD':('CRE_BIRD_BIG', 'MAROON'),
	'PANDA':('CRE_BULKY', 'WHITE'),
	'PANDA, GIGANTIC':('MAN_BULKY', 'WHITE'),
	'PANDA MAN':('CRE_BULKY', 'WHITE'),
	'CAPYBARA':('CRE_RODENT', 'OLIVE'),
	'CAPYBARA, GIANT':('MAN_RODENT', 'OLIVE'),
	'CAPYBARA MAN':('CRE_RODENT', 'OLIVE'),
	'BADGER':('CRE_CANINE', 'GRAY'),
	'BADGER MAN':('MAN_CANINE', 'GRAY'),
	'BADGER, GIANT':('CRE_CANINE', 'GRAY'),
	'MOOSE':('CRE_EQUINE', 'MAROON'),
	'MOOSE MAN':('MAN_EQUINE', 'MAROON'),
	'MOOSE, GIANT':('CRE_EQUINE', 'MAROON'),
	'RED PANDA':('CRE_CANINE', 'RED'),
	'RED PANDA MAN':('MAN_CANINE', 'RED'),
	'RED PANDA, GIANT':('CRE_CANINE', 'RED'),
	'ELEPHANT':('CRE_BULKY', 'GRAY'),
	'ELEPHANT_MAN':('MAN_BULKY', 'GRAY'),
	'GIANT_ELEPHANT':('CRE_BULKY', 'GRAY'),
	'WARTHOG':('CRE_BULKY', 'MAROON'),
	'WARTHOG_MAN':('MAN_BULKY', 'MAROON'),
	'GIANT_WARTHOG':('CRE_BULKY', 'MAROON'),
	'LION':('CRE_CANINE', 'YELLOW'),
	'LION_MAN':('MAN_CANINE', 'YELLOW'),
	'GIANT_LION':('CRE_CANINE', 'YELLOW'),
	'LEOPARD':('CRE_CANINE', 'YELLOW'),
	'LEOPARD_MAN':('MAN_CANINE', 'YELLOW'),
	'GIANT_LEOPARD':('CRE_CANINE', 'YELLOW'),
	'JAGUAR':('CRE_CANINE', 'NAVY'),
	'JAGUAR_MAN':('MAN_CANINE', 'NAVY'),
	'GIANT_JAGUAR':('CRE_CANINE', 'NAVY'),
	'TIGER':('CRE_FELINE', 'YELLOW'),
	'TIGER_MAN':('MAN_FELINE', 'YELLOW'),
	'GIANT_TIGER':('CRE_FELINE', 'YELLOW'),
	'CHEETAH':('CRE_FELINE', 'OLIVE'),
	'CHEETAH_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_CHEETAH':('CRE_FELINE', 'OLIVE'),
	'GAZELLE':('CRE_EQUINE', 'OLIVE'),
	'GAZELLE_MAN':('MAN_EQUINE', 'OLIVE'),
	'GIANT_GAZELLE':('CRE_EQUINE', 'OLIVE'),
	'MANDRILL':('CRE_PRIMATE', 'OLIVE'),
	'MANDRILL_MAN':('MAN_PRIMATE', 'OLIVE'),
	'GIANT_MANDRILL':('CRE_PRIMATE', 'OLIVE'),
	'CHIMPANZEE':('CRE_PRIMATE', 'NAVY'),
	'BONOBO':('CRE_PRIMATE', 'NAVY'),
	'GORILLA':('CRE_PRIMATE', 'NAVY'),
	'ORANGUTAN':('CRE_PRIMATE', 'MAROON'),
	'GIBBON_SIAMANG':('CRE_PRIMATE', 'NAVY'),
	'GIBBON_WHITE_HANDED':('CRE_PRIMATE', 'YELLOW'),
	'GIBBON_BLACK_HANDED':('CRE_PRIMATE', 'MAROON'),
	'GIBBON_GRAY':('CRE_PRIMATE', 'GRAY'),
	'GIBBON_SILVERY':('CRE_PRIMATE', 'SILVER'),
	'GIBBON_PILEATED':('CRE_PRIMATE', 'WHITE'),
	'GIBBON_BILOU':('CRE_PRIMATE', 'NAVY'),
	'GIBBON_WHITE_BROWED':('CRE_PRIMATE', 'WHITE'),
	'GIBBON_BLACK_CRESTED':('CRE_PRIMATE', 'RED'),
	'CAMEL_1_HUMP':('CRE_EQUINE', 'OLIVE'),
	'CAMEL_1_HUMP_MAN':('MAN_EQUINE', 'OLIVE'),
	'GIANT_CAMEL_1_HUMP':('CRE_EQUINE', 'OLIVE'),
	'CAMEL_2_HUMP':('CRE_EQUINE', 'MAROON'),
	'CAMEL_2_HUMP_MAN':('MAN_EQUINE', 'MAROON'),
	'GIANT_CAMEL_2_HUMP':('CRE_EQUINE', 'MAROON'),
	'CROCODILE_SALTWATER':('CRE_LIZARD', 'OLIVE'),
	'CROCODILE_SALTWATER_MAN':('MAN_LIZARD', 'OLIVE'),
	'GIANT_CROCODILE_SALTWATER':('CRE_LIZARD', 'OLIVE'),
	'BIRD_VULTURE':('CRE_BIRD_BIG', 'NAVY'),
	'VULTURE_MAN':('MAN_BIRD_BIG', 'NAVY'),
	'GIANT_VULTURE':('CRE_BIRD_BIG', 'NAVY'),
	'RHINOCEROS':('CRE_BULKY', 'GRAY'),
	'RHINOCEROS_MAN':('MAN_BULKY', 'GRAY'),
	'GIANT_RHINOCEROS':('CRE_BULKY', 'GRAY'),
	'GIRAFFE':('CRE_EQUINE', 'YELLOW'),
	'GIRAFFE_MAN':('MAN_EQUINE', 'YELLOW'),
	'GIANT_GIRAFFE':('CRE_EQUINE', 'YELLOW'),
	'HONEY BADGER':('CRE_RODENT', 'NAVY'),
	'HONEY BADGER MAN':('MAN_RODENT', 'NAVY'),
	'HONEY BADGER, GIANT':('CRE_RODENT', 'NAVY'),
	'GIANT TORTOISE':('CRE_SHELLED', 'OLIVE'),
	'GIANT TORTOISE MAN':('MAN_SHELLED', 'OLIVE'),
	'GIGANTIC TORTOISE':('CRE_SHELLED', 'OLIVE'),
	'ARMADILLO':('CRE_SHELLED', 'GRAY'),
	'ARMADILLO MAN':('MAN_SHELLED', 'GRAY'),
	'ARMADILLO, GIANT':('CRE_SHELLED', 'GRAY'),
	'MUSKOX':('CRE_EQUINE', 'MAROON'),
	'MUSKOX_MAN':('MAN_EQUINE', 'MAROON'),
	'GIANT_MUSKOX':('CRE_EQUINE', 'MAROON'),
	'ELK':('CRE_EQUINE', 'MAROON'),
	'ELK_MAN':('MAN_EQUINE', 'MAROON'),
	'GIANT_ELK':('CRE_EQUINE', 'MAROON'),
	'BEAR_POLAR':('CRE_BULKY', 'WHITE'),
	'BEAR_POLAR_MAN':('MAN_BULKY', 'WHITE'),
	'GIANT_BEAR_POLAR':('CRE_BULKY', 'WHITE'),
	'WOLVERINE':('CRE_BULKY', 'MAROON'),
	'WOLVERINE_MAN':('MAN_BULKY', 'MAROON'),
	'GIANT_WOLVERINE':('CRE_BULKY', 'MAROON'),
	'CHINCHILLA':('CRE_RODENT', 'GRAY'),
	'CHINCHILLA_MAN':('MAN_RODENT', 'GRAY'),
	'GIANT_CHINCHILLA':('CRE_RODENT', 'GRAY'),
	'FLOATING_GUTS':('CRE_BLOB', 'PINK'),
	'DRUNIAN':('CRE_EQUINE', 'SILVER'),
	'CREEPING_EYE':('MAN_CANINE', 'GRAY'),
	'VORACIOUS_CAVE_CRAWLER':('CRE_TUBE', 'BLUE'),
	'BLIND_CAVE_OGRE':('CRE_HOMINID_BIG', 'WHITE'),
	'CAP_HOPPER':('CRE_LIZARD', 'BLUE'),
	'MAGMA_CRAB':('CRE_BUG_GROUND', 'GRAY'),
	'CRUNDLE':('CRE_HOMINID', 'MAROON'),
	'HUNGRY_HEAD':('CRE_BUG_FLY', 'GRAY'),
	'FLESH_BALL':('CRE_BLOB', 'OLIVE'),
	'ELK_BIRD':('CRE_BIRD_TALL', 'TEAL'),
	'HELMET_SNAKE':('CRE_TUBE', 'WHITE'),
	'GREEN_DEVOURER':('MAN_BULKY', 'GREEN'),
	'RUTHERER':('CRE_BULKY', 'SILVER'),
	'CREEPY_CRAWLER':('CRE_BLOB', 'OLIVE'),
	'DRALTHA':('CRE_EQUINE', 'YELLOW'),
	'GIANT_EARTHWORM':('CRE_TUBE', 'PINK'),
	'BLOOD_MAN':('CRE_HOMINID', 'RED'),
	'BUGBAT':('CRE_BUG_FLY', 'PURPLE'),
	'MANERA':('CRE_EQUINE', 'OLIVE'),
	'MOLEMARIAN':('MAN_EQUINE', 'PINK'),
	'JABBERER':('CRE_BIRD_BIG', 'PINK'),
	'POND_GRABBER':('CRE_TENTACLES', 'BLUE'),
	'BLIND_CAVE_BEAR':('CRE_BULKY_BIG', 'WHITE'),
	'CAVE_DRAGON':('CRE_LIZARD', 'WHITE'),
	'REACHER':('CRE_HOMINID', 'GRAY'),
	'ELEMENTMAN_GABBRO':('CRE_HOMINID', 'GRAY'),
	'GORLAK':('CRE_HOMINID', 'GREEN'),
	'CAVE_FLOATER':('CRE_BUG_FLY', 'YELLOW'),
	'PLUMP_HELMET_MAN':('CRE_HOMINID', 'PURPLE'),
	'CAVE_BLOB':('CRE_BLOB', 'YELLOW'),
	'ELEMENTMAN_AMETHYST':('CRE_HOMINID', 'PINK'),
	'OCTOPUS':('CRE_TENTACLES', 'RED'),
	'OCTOPUS_MAN':('MAN_TENTACLES', 'RED'),
	'GIANT_OCTOPUS':('CRE_TENTACLES', 'RED'),
	'CRAB':('CRE_TENTACLES', 'RED'),
	'CRAB_MAN':('MAN_TENTACLES', 'RED'),
	'GIANT_CRAB':('CRE_TENTACLES', 'RED'),
	'LEOPARD_SEAL':('CRE_PINNIPED', 'GRAY'),
	'LEOPARD_SEAL_MAN':('MAN_PINNIPED', 'GRAY'),
	'GIANT_LEOPARD_SEAL':('CRE_PINNIPED', 'GRAY'),
	'CUTTLEFISH':('CRE_TENTACLES', 'WHITE'),
	'CUTTLEFISH_MAN':('MAN_TENTACLES', 'WHITE'),
	'GIANT_CUTTLEFISH':('CRE_TENTACLES', 'WHITE'),
	'ORCA':('CRE_FISH_BIG', 'WHITE'),
	'ORCA_MAN':('MAN_PINNIPED', 'WHITE'),
	'GIANT_ORCA':('CRE_FISH_BIG', 'WHITE'),
	'SPONGE':('CRE_BLOB', 'RED'),
	'SPONGE_MAN':('MAN_PINNIPED', 'RED'),
	'GIANT_SPONGE':('CRE_BLOB', 'RED'),
	'HORSESHOE_CRAB':('CRE_FISH_FLAT', 'MAROON'),
	'HORSESHOE_CRAB_MAN':('MAN_PINNIPED', 'MAROON'),
	'GIANT_HORSESHOE_CRAB':('CRE_FISH_FLAT', 'MAROON'),
	'SPERM_WHALE':('CRE_FISH_BIG', 'GRAY'),
	'SPERM_WHALE_MAN':('MAN_PINNIPED', 'GRAY'),
	'GIANT_SPERM_WHALE':('CRE_FISH_BIG', 'GRAY'),
	'ELEPHANT_SEAL':('CRE_PINNIPED', 'GRAY'),
	'ELEPHANT_SEAL_MAN':('MAN_PINNIPED', 'GRAY'),
	'GIANT_ELEPHANT_SEAL':('CRE_PINNIPED', 'GRAY'),
	'HARP_SEAL':('CRE_PINNIPED', 'WHITE'),
	'HARP_SEAL_MAN':('MAN_PINNIPED', 'WHITE'),
	'GIANT_HARP_SEAL':('CRE_PINNIPED', 'WHITE'),
	'NAUTILUS':('CRE_TENTACLES', 'WHITE'),
	'NAUTILUS_MAN':('MAN_PINNIPED', 'WHITE'),
	'GIANT_NAUTILUS':('CRE_TENTACLES', 'WHITE'),
	'FOXSQUIRREL':('CRE_RODENT', 'RED'),
	'MOGHOPPER':('CRE_ANURA', 'LIME'),
	'RAT_DEMON':('CRE_RODENT', 'RED'),
	'WAMBLER_FLUFFY':('CRE_HOMINID', 'WHITE'),
	'LIZARD_RHINO_TWO_LEGGED':('CRE_LIZARD', 'GRAY'),
	'WORM_KNUCKLE':('CRE_TUBE', 'BLUE'),
	'SPIDER_PHANTOM':('CRE_BUG_GROUND', 'WHITE'),
	'FLY_ACORN':('CRE_BUG_FLY', 'OLIVE'),
	'GNAT_BLOOD':('CRE_BUG_FLY', 'RED'),
	'LIZARD':('CRE_LIZARD', 'OLIVE'),
	'LIZARD_MAN':('MAN_LIZARD', 'OLIVE'),
	'GIANT_LIZARD':('CRE_LIZARD', 'OLIVE'),
	'SKINK':('CRE_LIZARD', 'YELLOW'),
	'SKINK_MAN':('MAN_LIZARD', 'YELLOW'),
	'GIANT_SKINK':('CRE_LIZARD', 'YELLOW'),
	'CHAMELEON':('CRE_LIZARD', 'LIME'),
	'CHAMELEON_MAN':('MAN_LIZARD', 'LIME'),
	'GIANT_CHAMELEON':('CRE_LIZARD', 'LIME'),
	'ANOLE':('CRE_LIZARD', 'LIME'),
	'ANOLE_MAN':('MAN_LIZARD', 'LIME'),
	'GIANT_ANOLE':('CRE_LIZARD', 'LIME'),
	'IGUANA':('CRE_LIZARD', 'GREEN'),
	'IGUANA_MAN':('MAN_LIZARD', 'GREEN'),
	'GIANT_IGUANA':('CRE_LIZARD', 'GREEN'),
	'RIVER OTTER':('CRE_FELINE', 'OLIVE'),
	'SEA OTTER':('MAN_FELINE', 'NAVY'),
	'OTTER_MAN':('CRE_FELINE', 'OLIVE'),
	'GIANT_OTTER':('CRE_FELINE', 'OLIVE'),
	'SNAPPING TURTLE':('CRE_SHELLED', 'OLIVE'),
	'ALLIGATOR SNAPPING TURTLE':('CRE_SHELLED', 'GRAY'),
	'SNAPPING_TURTLE_MAN':('MAN_SHELLED', 'OLIVE'),
	'GIANT_SNAPPING_TURTLE':('CRE_SHELLED', 'OLIVE'),
	'BEAVER':('CRE_RODENT', 'MAROON'),
	'BEAVER_MAN':('MAN_RODENT', 'MAROON'),
	'GIANT_BEAVER':('CRE_RODENT', 'MAROON'),
	'LEECH':('CRE_TUBE', 'GRAY'),
	'LEECH_MAN':('MAN_TUBE', 'GRAY'),
	'GIANT_LEECH':('CRE_TUBE', 'GRAY'),
	'AXOLOTL':('CRE_LIZARD', 'WHITE'),
	'AXOLOTL_MAN':('MAN_LIZARD', 'WHITE'),
	'GIANT_AXOLOTL':('CRE_LIZARD', 'WHITE'),
	'MINK':('CRE_RODENT', 'NAVY'),
	'MINK_MAN':('MAN_RODENT', 'NAVY'),
	'GIANT_MINK':('CRE_RODENT', 'NAVY'),
	'POND_TURTLE':('CRE_SHELLED', 'GREEN'),
	'POND_TURTLE_MAN':('MAN_SHELLED', 'GREEN'),
	'GIANT_POND_TURTLE':('CRE_SHELLED', 'GREEN'),
	'RAT':('CRE_RODENT', 'GRAY'),
	'RAT_MAN':('MAN_RODENT', 'GRAY'),
	'SQUIRREL_GRAY':('CRE_RODENT', 'GRAY'),
	'SQUIRREL_GRAY_MAN':('MAN_RODENT', 'GRAY'),
	'GIANT_SQUIRREL_GRAY':('CRE_RODENT', 'GRAY'),
	'SQUIRREL_RED':('CRE_RODENT', 'RED'),
	'SQUIRREL_RED_MAN':('MAN_RODENT', 'RED'),
	'GIANT_SQUIRREL_RED':('CRE_RODENT', 'RED'),
	'CHIPMUNK':('CRE_RODENT', 'OLIVE'),
	'CHIPMUNK_MAN':('MAN_RODENT', 'OLIVE'),
	'GIANT_CHIPMUNK':('CRE_RODENT', 'OLIVE'),
	'HAMSTER':('CRE_RODENT', 'OLIVE'),
	'HAMSTER_MAN':('MAN_RODENT', 'OLIVE'),
	'GIANT_HAMSTER':('CRE_RODENT', 'OLIVE'),
	'HEDGEHOG':('CRE_SHELLED', 'OLIVE'),
	'HEDGEHOG_MAN':('MAN_SHELLED', 'OLIVE'),
	'GIANT_HEDGEHOG':('CRE_SHELLED', 'OLIVE'),
	'SQUIRREL_FLYING':('CRE_RODENT', 'GRAY'),
	'FLYING_SQUIRREL_MAN':('MAN_RODENT', 'GRAY'),
	'GIANT_FLYING_SQUIRREL':('CRE_RODENT', 'GRAY'),
	'MUSSEL':('CRE_BLOB', 'NAVY'),
	'OYSTER':('CRE_BLOB', 'OLIVE'),
	'FISH_SALMON':('CRE_FISH_LONG', 'RED'),
	'FISH_CLOWNFISH':('CRE_FISH_SMALL', 'RED'),
	'FISH_HAGFISH':('CRE_TUBE', 'GRAY'),
	'FISH_LAMPREY_BROOK':('CRE_TUBE', 'OLIVE'),
	'FISH_RAY_BAT':('CRE_FISH_FLAT', 'GRAY'),
	'FISH_RAY_THORNBACK':('CRE_FISH_FLAT', 'OLIVE'),
	'FISH_RATFISH_SPOTTED':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_HERRING':('CRE_FISH_SMALL', 'CYAN'),
	'FISH_SHAD':('CRE_FISH_SMALL', 'WHITE'),
	'FISH_ANCHOVY':('CRE_FISH_LONG', 'CYAN'),
	'FISH_TROUT_STEELHEAD':('CRE_FISH_LONG', 'PINK'),
	'FISH_HAKE':('CRE_FISH_LONG', 'YELLOW'),
	'FISH_SEAHORSE':('CRE_TUBE', 'YELLOW'),
	'FISH_GLASSEYE':('CRE_FISH_SMALL', 'RED'),
	'FISH_PUFFER_WHITE_SPOTTED':('CRE_FISH_SMALL', 'WHITE'),
	'FISH_SOLE':('CRE_FISH_SMALL', 'MAROON'),
	'FISH_FLOUNDER':('CRE_FISH_SMALL', 'MAROON'),
	'FISH_MACKEREL':('CRE_FISH_SMALL', 'CYAN'),
	'JELLYFISH_SEA_NETTLE':('CRE_TENTACLES', 'PINK'),
	'SQUID':('CRE_TENTACLES', 'SILVER'),
	'SQUID MAN':('MAN_TENTACLES', 'SILVER'),
	'GIGANTIC SQUID':('CRE_TENTACLES', 'SILVER'),
	'FISH_LUNGFISH':('MAN_TENTACLES', 'GRAY'),
	'FISH_LOACH_CLOWN':('CRE_FISH_LONG', 'WHITE'),
	'FISH_BULLHEAD_BROWN':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_BULLHEAD_YELLOW':('CRE_FISH_LONG', 'YELLOW'),
	'FISH_BULLHEAD_BLACK':('CRE_FISH_LONG', 'NAVY'),
	'FISH_KNIFEFISH_BANDED':('CRE_FISH_LONG', 'OLIVE'),
	'FISH_CHAR':('CRE_FISH_LONG', 'RED'),
	'FISH_TROUT_RAINBOW':('CRE_FISH_LONG', 'PINK'),
	'FISH_MOLLY_SAILFIN':('CRE_FISH_SMALL', 'YELLOW'),
	'FISH_GUPPY':('CRE_FISH_SMALL', 'NAVY'),
	'FISH_PERCH':('CRE_FISH_SMALL', 'LIME'),
	'DWARF':('CRE_DWARF', 'RED'),
	'HUMAN':('CRE_HOMINID', 'YELLOW'),
	'ELF':('CRE_HOMINID', 'OLIVE'),
	'GOBLIN':('CRE_HOMINID', 'LIME'),
	'KOBOLD':('MAN_LIZARD', 'SILVER'),
	'GREMLIN':('CRE_HOMINID', 'LIME'),
	'TROLL':('CRE_HOMINID_BIG', 'TEAL'),
	'OGRE':('CRE_HOMINID_BIG', 'YELLOW'),
	'UNICORN':('CRE_EQUINE', 'WHITE'),
	'DRAGON':('CRE_LIZARD', 'RED'),
	'SATYR':('CRE_EQUINE', 'OLIVE'),
	'COLOSSUS_BRONZE':('CRE_HOMINID_BIG', 'OLIVE'),
	'GIANT':('CRE_HOMINID_BIG', 'YELLOW'),
	'CYCLOPS':('CRE_HOMINID_BIG', 'YELLOW'),
	'ETTIN':('CRE_HOMINID_BIG', 'YELLOW'),
	'MINOTAUR':('MAN_EQUINE', 'MAROON'),
	'YETI':('CRE_HOMINID_BIG', 'WHITE'),
	'SASQUATCH':('CRE_HOMINID_BIG', 'OLIVE'),
	'BLIZZARD_MAN':('CRE_HOMINID', 'CYAN'),
	'WOLF_ICE':('CRE_CANINE', 'WHITE'),
	'FAIRY':('CRE_BUG_FLY', 'CYAN'),
	'PIXIE':('CRE_BUG_FLY', 'LIME'),
	'BEAK_DOG':('CRE_BIRD_BIG', 'PINK'),
	'GRIMELING':('CRE_HOMINID', 'GREEN'),
	'BLENDEC_FOUL':('MAN_EQUINE', 'GRAY'),
	'STRANGLER':('CRE_HOMINID', 'NAVY'),
	'NIGHTWING':('MAN_BIRD_BIG', 'MAROON'),
	'HARPY':('MAN_BIRD_BIG', 'OLIVE'),
	'HYDRA':('CRE_LIZARD', 'RED'),
	'MERPERSON':('MAN_TUBE', 'GREEN'),
	'SEA_SERPENT':('CRE_TUBE', 'TEAL'),
	'SEA_MONSTER':('CRE_TENTACLES', 'NAVY'),
	'BIRD_ROC':('CRE_BIRD_BIG', 'MAROON'),
	'CROCODILE_CAVE':('CRE_LIZARD', 'SILVER'),
	'TOAD_GIANT_CAVE':('CRE_ANURA', 'OLIVE'),
	'OLM_GIANT':('CRE_LIZARD', 'WHITE'),
	'BAT_GIANT':('CRE_BUG_FLY', 'MAROON'),
	'RAT_GIANT':('CRE_RODENT', 'GRAY'),
	'RAT_LARGE':('CRE_RODENT', 'GRAY'),
	'MOLE_DOG_NAKED':('CRE_RODENT', 'PINK'),
	'TROGLODYTE':('CRE_HOMINID', 'YELLOW'),
	'MOLE_GIANT':('CRE_RODENT', 'GRAY'),
	'IMP_FIRE':('CRE_HOMINID', 'YELLOW'),
	'SPIDER_CAVE_GIANT':('CRE_BUG_FLY', 'OLIVE'),
	'SPIDER_CAVE':('CRE_BUG_FLY', 'WHITE'),
	'FISH_CAVE':('CRE_FISH_SMALL', 'WHITE'),
	'CAVE_FISH_MAN':('MAN_PINNIPED', 'WHITE'),
	'LOBSTER_CAVE':('CRE_BUG_GROUND', 'WHITE'),
	'SNAKE_FIRE':('CRE_TUBE', 'YELLOW'),
	'OLM':('CRE_LIZARD', 'WHITE'),
	'OLM_MAN':('MAN_LIZARD', 'WHITE'),
	'BAT':('CRE_BUG_FLY', 'MAROON'),
	'BAT_MAN':('MAN_BIRD_BIG', 'MAROON'),
	'MAGGOT_PURRING':('CRE_TUBE', 'WHITE'),
	'ELEMENTMAN_FIRE':('CRE_HOMINID', 'YELLOW'),
	'ELEMENTMAN_MAGMA':('CRE_HOMINID', 'RED'),
	'ELEMENTMAN_IRON':('CRE_HOMINID', 'GRAY'),
	'ELEMENTMAN_MUD':('CRE_HOMINID', 'OLIVE'),
	'BIRD_SWALLOW_CAVE':('CRE_BIRD_SMALL', 'OLIVE'),
	'CAVE_SWALLOW_MAN':('MAN_BIRD_SMALL', 'OLIVE'),
	'BIRD_SWALLOW_CAVE_GIANT':('CRE_BIRD_SMALL', 'OLIVE'),
	'AMPHIBIAN_MAN':('MAN_ANURA', 'GREEN'),
	'REPTILE_MAN':('MAN_LIZARD', 'GREEN'),
	'SERPENT_MAN':('MAN_TUBE', 'WHITE'),
	'ANT_MAN':('MAN_BUG_GROUND', 'MAROON'),
	'RODENT MAN':('MAN_RODENT', 'NAVY'),
	'WILD_BOAR':('CRE_BULKY', 'NAVY'),
	'WILD_BOAR_MAN':('MAN_BULKY', 'NAVY'),
	'GIANT_WILD_BOAR':('CRE_BULKY', 'NAVY'),
	'COYOTE':('CRE_CANINE', 'OLIVE'),
	'COYOTE_MAN':('MAN_CANINE', 'OLIVE'),
	'GIANT_COYOTE':('CRE_CANINE', 'OLIVE'),
	'KANGAROO':('CRE_BULKY', 'RED'),
	'KANGAROO_MAN':('MAN_BULKY', 'RED'),
	'GIANT_KANGAROO':('CRE_BULKY', 'RED'),
	'KOALA':('CRE_RODENT', 'GRAY'),
	'KOALA_MAN':('MAN_RODENT', 'GRAY'),
	'GIANT_KOALA':('CRE_RODENT', 'GRAY'),
	'ADDER':('CRE_TUBE', 'GRAY'),
	'ADDER_MAN':('MAN_TUBE', 'GRAY'),
	'GIANT_ADDER':('CRE_TUBE', 'GRAY'),
	'ECHIDNA':('CRE_SHELLED', 'MAROON'),
	'ECHIDNA_MAN':('MAN_SHELLED', 'MAROON'),
	'GIANT_ECHIDNA':('CRE_SHELLED', 'MAROON'),
	'PORCUPINE':('CRE_SHELLED', 'NAVY'),
	'PORCUPINE_MAN':('MAN_SHELLED', 'NAVY'),
	'GIANT_PORCUPINE':('CRE_SHELLED', 'NAVY'),
	'KINGSNAKE':('CRE_TUBE', 'RED'),
	'KINGSNAKE_MAN':('MAN_TUBE', 'RED'),
	'GIANT_KINGSNAKE':('CRE_TUBE', 'RED'),
	'GRAY_LANGUR':('CRE_PRIMATE', 'WHITE'),
	'GRAY_LANGUR_MAN':('MAN_PRIMATE', 'WHITE'),
	'GIANT_GRAY_LANGUR':('CRE_PRIMATE', 'WHITE'),
	'BOBCAT':('CRE_FELINE', 'OLIVE'),
	'BOBCAT_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_BOBCAT':('CRE_FELINE', 'OLIVE'),
	'SKUNK':('CRE_RODENT', 'NAVY'),
	'SKUNK_MAN':('MAN_RODENT', 'NAVY'),
	'GIANT_SKUNK':('CRE_RODENT', 'NAVY'),
	'GREEN_TREE_FROG':('CRE_ANURA', 'LIME'),
	'GREEN_TREE_FROG_MAN':('MAN_ANURA', 'LIME'),
	'GIANT_GREEN_TREE_FROG':('CRE_ANURA', 'LIME'),
	'HARE':('CRE_RODENT', 'OLIVE'),
	'HARE_MAN':('MAN_RODENT', 'OLIVE'),
	'GIANT_HARE':('CRE_RODENT', 'OLIVE'),
	'RATTLESNAKE':('CRE_TUBE', 'OLIVE'),
	'RATTLESNAKE_MAN':('MAN_TUBE', 'OLIVE'),
	'GIANT_RATTLESNAKE':('CRE_TUBE', 'OLIVE'),
	'WEASEL':('CRE_FELINE', 'MAROON'),
	'WEASEL_MAN':('MAN_FELINE', 'MAROON'),
	'GIANT_WEASEL':('CRE_FELINE', 'MAROON'),
	'COPPERHEAD_SNAKE':('CRE_TUBE', 'MAROON'),
	'COPPERHEAD_SNAKE_MAN':('MAN_TUBE', 'MAROON'),
	'GIANT_COPPERHEAD_SNAKE':('CRE_TUBE', 'MAROON'),
	'IBEX':('CRE_EQUINE', 'MAROON'),
	'IBEX_MAN':('MAN_EQUINE', 'MAROON'),
	'GIANT_IBEX':('CRE_EQUINE', 'MAROON'),
	'WOMBAT':('CRE_RODENT', 'GRAY'),
	'WOMBAT_MAN':('MAN_RODENT', 'GRAY'),
	'GIANT_WOMBAT':('CRE_RODENT', 'GRAY'),
	'DINGO':('CRE_CANINE', 'RED'),
	'DINGO_MAN':('MAN_CANINE', 'RED'),
	'GIANT_DINGO':('CRE_CANINE', 'RED'),
	'COATI':('CRE_FELINE', 'MAROON'),
	'COATI_MAN':('MAN_FELINE', 'MAROON'),
	'GIANT_COATI':('CRE_FELINE', 'MAROON'),
	'OPOSSUM':('CRE_RODENT', 'WHITE'),
	'OPOSSUM_MAN':('MAN_RODENT', 'WHITE'),
	'GIANT_OPOSSUM':('CRE_RODENT', 'WHITE'),
	'MONGOOSE':('CRE_FELINE', 'OLIVE'),
	'MONGOOSE_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_MONGOOSE':('CRE_FELINE', 'OLIVE'),
	'HYENA':('CRE_FELINE', 'MAROON'),
	'HYENA_MAN':('MAN_FELINE', 'MAROON'),
	'GIANT_HYENA':('CRE_FELINE', 'MAROON'),
	'ANACONDA':('CRE_TUBE', 'OLIVE'),
	'ANACONDA_MAN':('MAN_TUBE', 'OLIVE'),
	'GIANT_ANACONDA':('CRE_TUBE', 'OLIVE'),
	'MONITOR_LIZARD':('CRE_LIZARD', 'NAVY'),
	'MONITOR_LIZARD_MAN':('MAN_LIZARD', 'NAVY'),
	'GIANT_MONITOR_LIZARD':('CRE_LIZARD', 'NAVY'),
	'KING_COBRA':('CRE_TUBE', 'OLIVE'),
	'KING_COBRA_MAN':('MAN_TUBE', 'OLIVE'),
	'GIANT_KING_COBRA':('CRE_TUBE', 'OLIVE'),
	'OCELOT':('CRE_FELINE', 'OLIVE'),
	'OCELOT_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_OCELOT':('CRE_FELINE', 'OLIVE'),
	'JACKAL':('CRE_CANINE', 'RED'),
	'JACKAL_MAN':('MAN_CANINE', 'RED'),
	'GIANT_JACKAL':('CRE_CANINE', 'RED'),
	'CAPUCHIN':('CRE_PRIMATE', 'NAVY'),
	'CAPUCHIN_MAN':('MAN_PRIMATE', 'NAVY'),
	'GIANT_CAPUCHIN':('CRE_PRIMATE', 'NAVY'),
	'SLOTH':('CRE_PRIMATE', 'GRAY'),
	'SLOTH_MAN':('MAN_PRIMATE', 'GRAY'),
	'GIANT_SLOTH':('CRE_PRIMATE', 'GRAY'),
	'SPIDER_MONKEY':('CRE_PRIMATE', 'MAROON'),
	'SPIDER_MONKEY_MAN':('MAN_PRIMATE', 'MAROON'),
	'GIANT_SPIDER_MONKEY':('CRE_PRIMATE', 'MAROON'),
	'PANGOLIN':('CRE_SHELLED', 'GRAY'),
	'PANGOLIN_MAN':('MAN_SHELLED', 'GRAY'),
	'GIANT_PANGOLIN':('CRE_SHELLED', 'GRAY'),
	'BLACK_MAMBA':('CRE_TUBE', 'NAVY'),
	'BLACK_MAMBA_MAN':('MAN_TUBE', 'NAVY'),
	'GIANT_BLACK_MAMBA':('CRE_TUBE', 'NAVY'),
	'BEAR_SLOTH':('CRE_BULKY', 'NAVY'),
	'SLOTH_BEAR_MAN':('MAN_BULKY', 'NAVY'),
	'GIANT_SLOTH_BEAR':('CRE_BULKY', 'NAVY'),
	'AYE-AYE':('CRE_PRIMATE', 'GRAY'),
	'AYE-AYE_MAN':('MAN_PRIMATE', 'GRAY'),
	'GIANT_AYE-AYE':('CRE_PRIMATE', 'GRAY'),
	'BUSHMASTER':('CRE_TUBE', 'RED'),
	'BUSHMASTER_MAN':('MAN_TUBE', 'RED'),
	'GIANT_BUSHMASTER':('CRE_TUBE', 'RED'),
	'PYTHON':('CRE_TUBE', 'YELLOW'),
	'PYTHON_MAN':('MAN_TUBE', 'YELLOW'),
	'GIANT_PYTHON':('CRE_TUBE', 'YELLOW'),
	'TAPIR':('CRE_BULKY', 'MAROON'),
	'TAPIR_MAN':('MAN_BULKY', 'MAROON'),
	'GIANT_TAPIR':('CRE_BULKY', 'MAROON'),
	'IMPALA':('CRE_EQUINE', 'RED'),
	'IMPALA_MAN':('MAN_EQUINE', 'RED'),
	'GIANT_IMPALA':('CRE_EQUINE', 'RED'),
	'AARDVARK':('CRE_BULKY', 'OLIVE'),
	'AARDVARK_MAN':('MAN_BULKY', 'OLIVE'),
	'GIANT_AARDVARK':('CRE_BULKY', 'OLIVE'),
	'LION_TAMARIN':('CRE_PRIMATE', 'RED'),
	'LION_TAMARIN_MAN':('MAN_PRIMATE', 'RED'),
	'GIANT_LION_TAMARIN':('CRE_PRIMATE', 'RED'),
	'STOAT':('CRE_FELINE', 'OLIVE'),
	'STOAT_MAN':('MAN_FELINE', 'OLIVE'),
	'GIANT_STOAT':('CRE_FELINE', 'OLIVE'),
	'LYNX':('CRE_FELINE', 'GRAY'),
	'LYNX_MAN':('MAN_FELINE', 'GRAY'),
	'GIANT_LYNX':('CRE_FELINE', 'GRAY')
}

racelist = ('DWARF', 'HUMAN', 'ELF')
altlist = ('MAGGOT_PURRING')
eyelist1 = ('CREEPING_EYE')
eyelist2 = ('BLIZZARD_MAN', 'GOBLIN', 'KOBOLD')
regex = re.compile('\[CREATURE:(.*)\]')

os.makedirs(os.path.dirname('../objects_patch/'), exist_ok=True)
for inname in (i for i in os.listdir('objects') if 'creature' in i):
	creaturelist = []
	with open('objects/' + inname, 'r') as infile:
		intext = infile.read()
		creaturelist = regex.findall(intext)

	with open('../objects_patch/' + inname, 'w') as outfile:
		for name in creaturelist:

			creature = creature_data[name]
			outfile.write('[CREATURE:%s]\n' % name)
			outfile.write('\t[CREATURE_TILE:%s]\n' % creature[0])

			if name in racelist:
				outfile.write('\t[CREATURE_SOLDIER_TILE:%s]\n' % creature[0])
			if name in altlist:
				outfile.write('\t[ALTTILE:%s]\n' % creature[0])
			if name in eyelist1:
				outfile.write('\t[GLOWTILE:149]\n')
			if name in eyelist2:
				outfile.write('\t[GLOWTILE:148]\n')

			color = 'LIME' if creature[1] == 'GREEN' else creature[1]
			color = 'CYAN' if color == 'TEAL' else color
			outfile.write('\t[COLOR:%s:0:0]\n' % color)