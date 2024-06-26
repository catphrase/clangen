from random import choice
from scripts.cat.sprites import sprites
import random
from re import sub
from scripts.game_structure.game_essentials import game


    

class Pelt():
    
    sprites_names = {
        "SingleColour": 'single',
        'TwoColour': 'single',
        'Tabby': 'tabby',
        'Marbled': 'marbled',
        'Rosette': 'rosette',
        'Smoke': 'smoke',
        'Ticked': 'ticked',
        'Speckled': 'speckled',
        'Bengal': 'bengal',
        'Mackerel': 'mackerel',
        'Classic': 'classic',
        'Sokoke': 'sokoke',
        'Agouti': 'agouti',
        'Singlestripe': 'singlestripe',
        'Abyssinian': 'abyssinian',
        'Brindle': 'brindle',
        'Braided': 'braided',
        'Splotch': 'splotch',
        'Saber': 'saber',
        'Faded': 'faded',
        'Masked': 'masked',
        'Fog': 'fog',
        'Mist': 'mist',
        'Smudge': 'smudge',
        'BrokenMackerel': 'brokenmackerel',
        'Dust': 'dust',
        'CharcoalBengal': 'charcoalbengal',
        'BrokenBraided': 'brokenbraided',
        'Longdan': 'longdan',
        'Tortie': None,
        'Calico': None
    }
    
    # ATTRIBUTES, including non-pelt related
    pelt_colours = [
        'WHITE', 'SNOW WHITE', 'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]
    pelt_c_no_white = [
        'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]
    pelt_c_no_bw = [
        'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE',
        'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'SILVER',
        'PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER',
        'PALE GOLD', 'YELLOW', 'GOLD', 'BRONZE', 'ROSE',
        'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD',
        'PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN',
        'PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE', 'BIRCH',
        'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'
    ]


    tortiepatterns = ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE',
                      'MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL', 'GRUMPYFACE',
                      'MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE',
                      'ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED',
                      'VIPER', 'SKULL', 'POINTS', 'DITTO', 'BODY', 'SHILOH', 'TABBY', 'SPECKLED', 'BENGAL', 'CLASSIC', 'MACKEREL', 'MARBLED',
                      'SABER', 'ROSETTE', 'MASKED', 'DUST', 'MAXIMUMONE', 'MAXIMUMTWO', 'MAXIMUMTHREE', 'MAXIMUMFOUR', 'MAXIMUMFIVE',
                      'MAXIMUMSIX', 'MAXIMUMSEVEN', 'MAXIMUMEIGHT']

    tortiebases = ['single', 'tabby', 'bengal', 'marbled', 'ticked', 'smoke', 'rosette', 'speckled', 'mackerel',
                   'classic', 'sokoke', 'agouti', 'singlestripe', 'abyssinian', 'brindle', 'braided', 'splotch',
                   'saber', 'faded', 'masked', 'fog', 'mist', 'smudge', 'longdan', 'brokenmackerel', 'brokenbraided',
                   'charcoalbengal', 'dust']


    pelt_length = ["short", "medium", "long"]
    eye_colours = ['YELLOW', 'AMBER', 'HAZEL', 'PALE GREEN', 'GREEN', 'BLUE',
               'DARK BLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHER BLUE', 'SUN-LIT ICE',
               'COPPER', 'SAGE', 'BRIGHT BLUE', 'PALE BLUE', 'LAVENDER', 'DARK GREY',
               'PALE YELLOW', 'GOLD', 'LIME', 'HAZELNUT', 'DARK AMBER', 'SLATE',
               'RUBY', 'LILAC', 'LIGHT GREY', 'PINK', 'DARK HAZEL', 'CHOCOLATE']
    yellow_eyes = ['YELLOW', 'PALE YELLOW', 'GOLD']
    blue_eyes = ['BLUE', 'DARK BLUE', 'CYAN', 'SUN-LIT ICE', 'BRIGHT BLUE', 'PALE BLUE']
    green_eyes = ['HAZEL', 'PALE GREEN', 'GREEN', 'EMERALD', 'SAGE', 'LIME', 'DARK HAZEL']
    red_eyes = ['AMBER', 'COPPER', 'HAZELNUT', 'DARK AMBER', 'RUBY', 'CHOCOLATE']
    grey_eyes = ['GREY', 'DARK GREY', 'SLATE', 'LIGHT GREY']
    purple_eyes = ['HEATHER BLUE', 'LAVENDER', 'LILAC', 'PINK']
    # scars1 is scars from other cats, other animals - scars2 is missing parts - scars3 is "special" scars that could only happen in a special event
    # bite scars by @wood pank on discord
    scars1 = ["ONE", "TWO", "THREE", "TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY",
            "LEGBITE", "NECKBITE", "FACE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
            "BOTHBLIND", "BEAKCHEEK", "BEAKLOWER", "CATBITE", "RATBITE", "QUILLCHUNK", "QUILLSCRATCH", "HINDLEG",
            "BACK", "QUILLSIDE", "SCRATCHSIDE", "BEAKSIDE", "CATBITETWO", "FOUR"]
    scars2 = ["LEFTEAR", "RIGHTEAR", "NOTAIL", "HALFTAIL", "NOPAW", "NOLEFTEAR", "NORIGHTEAR", "NOEAR"]
    scars3 = ["SNAKE", "TOETRAP", "BURNPAWS", "BURNTAIL", "BURNBELLY", "BURNRUMP", "FROSTFACE", "FROSTTAIL", "FROSTMITT",
            "FROSTSOCK", "TOE", "SNAKETWO"]

    # make sure to add plural and singular forms of new accs to acc_display.json so that they will display nicely
    plant_accessories = ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL",
                        "BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS", "DRY HERBS",
                        "OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"
                        ]
    wild_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"
                        ]
    tail_accessories = ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS"]
    living_accessories = ["LUNA MOTH", "ATLAS MOTH", "BUTTERFLIES", "FIREFLIES"]
    plant2_accessories = ["DAISY", "IVY", "CLOVER", "WREATH", "FLOWER WREATH", "WILD FLOWERS", "LILAC", "MONSTERA"]
    wild2_accessories = ["BIRD SKULL", "ANTLERS", "TWIGS", "SERPENT"]
    beach_accessories = ["SEAWEED", "SHELL"]
    mountain_accessories = ["CRYSTAL"]
    plains_accessories = ["SPROUT"]
    forest_accessories = ["MUSHROOM"]
    special_accessories = ["STICK", "MOSS BALL", "LILY PAD"]
    collars = [
        "CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME", "GREEN", "RAINBOW",
        "BLACK", "SPIKES", "WHITE", "PINK", "PURPLE", "MULTI", "INDIGO", "CRIMSONBELL", "BLUEBELL",
        "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL", "GREENBELL",
        "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL", "PINKBELL", "PURPLEBELL",
        "MULTIBELL", "INDIGOBELL", "CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW",
        "LIMEBOW", "GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW", "PINKBOW",
        "PURPLEBOW", "MULTIBOW", "INDIGOBOW", "CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON",
        "REDNYLON", "LIMENYLON", "GREENNYLON", "RAINBOWNYLON",
        "BLACKNYLON", "SPIKESNYLON", "WHITENYLON", "PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON",
        "REDHARNESS", "NAVYHARNESS", "YELLOWHARNESS", "TEALHARNESS", "ORANGEHARNESS", "GREENHARNESS","MOSSHARNESS", "RAINBOWHARNESS", "BLACKHARNESS", "BEEHARNESS", "CREAMHARNESS","PINKHARNESS", "MAGENTAHARNESS", "PEACHHARNESS", "VIOLETHARNESS"
    ]
    dog_collars = ["CRIMSONFANG", "BLUEFANG", "YELLOWFANG", "CYANFANG", "REDFANG", "LIMEFANG", "GREENFANG", "RAINBOWFANG",
        "BLACKFANG", "SPIKESFANG", "WHITEFANG", "PINKFANG", "PURPLEFANG", "MULTIFANG", "INDIGOFANG"]
    kitty_accessories = ["SUNGLASSES", "RED BANDANA", "ORANGE BANDANA", "YELLOW BANDANA", "GREEN BANDANA", "BLUE BANDANA", "PURPLE BANDANA", "WHITE BANDANA", "BLACK BANDANA", "PINK BANDANA",
                         "RED HARNESS", "ORANGE HARNESS", "YELLOW HARNESS", "GREEN HARNESS", "BLUE HARNESS", "PURPLE HARNESS", "WHITE HARNESS", "BLACK HARNESS", "PINK HARNESS", "COWBOY HAT"]

    points = ["Ticked", "Agouti", "Smoke", "Mist", "Fog", "Dust"]
    spots = ["Speckled", "Rosette", "Bengal", "CharcoalBengal"]
    swirls = ["Tabby", "Classic", "Sokoke", "Marbled", "Smudge"]
    flats = ["SingleColour", "TwoColour", "Singlestripe", "Abyssinian"]
    stripes = ["Mackerel", "Braided", "Brindle", "BrokenMackerel", "BrokenBraided", "Masked"]
    exotic = ["Saber", "Faded", "Longdan", "Splotch"]
    # ohdan's accessories
    flower_accessories = ["DAISY", "DIANTHUS", "BLEEDING HEARTS", "FRANGIPANI", "BLUE GLORY",
                          "CATNIP FLOWER", "BLANKET FLOWER", "ALLIUM", "LACELEAF", "PURPLE GLORY",
                          "YELLOW PRIMROSE", "HESPERIS", "MARIGOLD", "WISTERIA", "PINKFLOWERCROWN", "YELLOWFLOWERCROWN", "BLUEFLOWERCROWN", "PURPLEFLOWERCROWN"]
    
    wild2_accessories = ["BIRD SKULL", "ANTLERS", "TWIGS", "SERPENT"]
    
    plant2_accessories = ["CLOVER", "STICK", "PUMPKIN", "MOSS", "IVY", "ACORN", "MOSS PELT", "REEDS", "BAMBOO"]

    snake_accessories = ["GRASS SNAKE", "BLUE RACER", "WESTERN COACHWHIP", "KINGSNAKE"]

    smallAnimal_accessories = ["GRAY SQUIRREL", "RED SQUIRREL", "CRAB", "WHITE RABBIT", "BLACK RABBIT",
                           "BROWN RABBIT", "INDIAN GIANT SQUIRREL", "FAWN RABBIT",
                           "BROWN AND WHITE RABBIT", "BLACK AND WHITE RABBIT", "WHITE AND FAWN RABBIT",
                           "BLACK VITILIGO RABBIT", "BROWN VITILIGO RABBIT", "FAWN VITILIGO RABBIT",
                           "BLACKBIRD", "ROBIN", "JAY", "THRUSH", "CARDINAL", "MAGPIE", "CUBAN TROGON",
                           "TAN RABBIT", "TAN AND WHITE RABBIT", "TAN VITILIGO RABBIT",
                           "RAT", "WHITE MOUSE", "BLACK MOUSE", "GRAY MOUSE", "BROWN MOUSE",
                           "GRAY RABBIT", "GRAY AND WHITE RABBIT", "GRAY VITILIGO RABBIT"]
    
    deadInsect_accessories = ["LUNAR MOTH", "ROSY MAPLE MOTH", "MONARCH BUTTERFLY", "DAPPLED MONARCH",
                              "POLYPHEMUS MOTH", "MINT MOTH"]
    
    aliveInsect_accessories = ["BROWN SNAIL", "RED SNAIL", "WORM", "BLUE SNAIL", "ZEBRA ISOPOD", "DUCKY ISOPOD", "DAIRY COW ISOPOD",
                               "BEETLEJUICE ISOPOD", "BEE", "RED LADYBUG", "ORANGE LADYBUG", "YELLOW LADYBUG"]
    
    fruit_accessories = ["RASPBERRY", "BLACKBERRY", "GOLDEN RASPBERRY", "CHERRY", "YEW"]

    crafted_accessories = ["WILLOWBARK BAG", "CLAY DAISY POT", "CLAY AMANITA POT", "CLAY BROWNCAP POT", "BIRD SKULL", "LEAF BOW", "RAINCOAT", "POPTABS", "FAZBEAR", "WHITEBEAR", "PANDA", "BEAR", "BROWNBEAR", "TIDE", "CELESTIALCHIMES", "LUNARCHIMES", "STARCHIMES", "SILVERLUNARCHIMES", "FIDDLEHEADS", "LANTERNS", "HEARTCHARMS", "CHIMES"]

    tail2_accessories = ["SEAWEED", "DAISY CORSAGE"]


    tabbies = ["Tabby", "Ticked", "Mackerel", "Classic", "Sokoke", "Agouti"]
    spotted = ["Speckled", "Rosette"]
    plain = ["SingleColour", "TwoColour", "Smoke", "Singlestripe"]
    exotic = ["Bengal", "Marbled", "Masked"]
    torties = ["Tortie", "Calico"]
    pelt_categories = [points, spots, swirls, flats, stripes, exotic, torties]

    # SPRITE NAMES
    single_colours = [
        'WHITE', 'SNOW WHITE', 'PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC', 'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE', 'SILVER',
        'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST', 'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'PALE GOLD', 'PALE GINGER', 'ROSE',
        'YELLOW', 'GOLD', 'BRONZE', 'DARK GOLD', 'PALE FIRE', 'FIRE', 'DARK FIRE', 'GINGER', 'DARK GINGER', 'DARK ORANGE',
        'PALE BROWN', 'ALMOND', 'BIRCH', 'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'PALE CINNAMON', 'CINNAMON', 'SABLE',
        'DARK SABLE', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN'
    ]
    white_colours = ['WHITE', 'SNOW WHITE']
    blue_colours = ['PALE BLUE', 'BLUE', 'PALE LILAC', 'LILAC']
    gray_colours = ['GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE', 'SILVER']
    black_colours = ['BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST']
    cream_colours = ['LIGHT CREAM', 'CREAM', 'DARK CREAM', 'PALE GOLD', 'PALE GINGER', 'ROSE']
    gold_colours = ['YELLOW', 'GOLD', 'BRONZE', 'DARK GOLD']
    fire_colours = ['PALE FIRE', 'FIRE', 'DARK FIRE']
    ginger_colours = ['GINGER', 'DARK GINGER', 'DARK ORANGE']
    coolbrown_colours = ['PALE BROWN', 'ALMOND', 'BIRCH']
    lavender_colours = ['PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER']
    warmbrown_colours = ['PALE CINNAMON', 'CINNAMON', 'SABLE', 'DARK SABLE']
    brown_colours = ['ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN']
    colour_categories = [white_colours, blue_colours, gray_colours, black_colours, cream_colours, gold_colours,
                     fire_colours, ginger_colours, coolbrown_colours, lavender_colours, warmbrown_colours,
                     brown_colours]
    eye_sprites = [
        'YELLOW', 'AMBER', 'HAZEL', 'PALE GREEN', 'GREEN', 'BLUE', 'DARK BLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHER BLUE',
        'SUN-LIT ICE', 'COPPER', 'SAGE', 'BRIGHT BLUE', 'PALE BLUE', 'LAVENDER', 'DARK GREY', 'PALE YELLOW', 'GOLD', 'LIME',
        'HAZELNUT', 'DARK AMBER', 'SLATE', 'RUBY', 'LILAC', 'LIGHT GREY', 'PINK', 'DARK HAZEL', 'CHOCOLATE'
    ]
    eye_patterns = ['TRUE', 'CENTRAL', 'QUARTER', 'SLIVER', 'SPECKLES', 'FROSTED', 'RING', 'HALFCENTRAL', 'HALFRING', 'BUBBLE', 'OUTRING', 'SWAP']
    little_white = ['LITTLE', 'LIGHTTUXEDO', 'BUZZARDFANG', 'TIP', 'BLAZE', 'BIB', 'VEE', 'PAWS',
                    'BELLY', 'TAILTIP', 'TOES', 'BROKENBLAZE', 'LILTWO', 'SCOURGE', 'TOESTAIL', 'RAVENPAW', 'HONEY',
                    'LUNA', 'EXTRA', 'MUSTACHE', 'REVERSEHEART', 'SPARKLE', 'RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'REVERSEEYE', 'BACKSPOT',
                    'EYEBAGS', 'LOCKET', 'BLAZEMASK', 'TEARS']
    mid_white = ['TUXEDO', 'FANCY', 'UNDERS', 'DAMIEN', 'SKUNK', 'MITAINE', 'SQUEAKS', 'STAR',
                 'WINGS', 'MOSSY', 'CHANCE', 'DIVA', 'SAVANNAH', 'FADESPOTS', 'BEARD', 'DAPPLEPAW', 'TOPCOVER', 'WOODPECKER', 'MISS', 'VENUS',
                 'BOWTIE', 'VEST', 'FADEBELLY', 'DIGIT', 'FCTWO', 'FCONE', 'MIA', 'ROSINA', 'PRINCESS', 'DOUGIE']
    high_white = ['ANY', 'ANYTWO', 'BROKEN', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO',
                  'GOATEE', 'PRINCE', 'FAROFA', 'MISTER', 'PANTS', 'REVERSEPANTS', 'HALFWHITE', 'APPALOOSA', 'PIEBALD',
                  'CURVED', 'GLASS', 'MASKMANTLE', 'MAO', 'PAINTED', 'NIGHTMIST', 'FALCON', 'RETSUKO', 'SHIBAINU',
                  'SNOWSTORM', 'PEPPER', 'OWL', 'BUB', 'SPARROW', 'TRIXIE',
                  'SAMMY', 'FRONT', 'BLOSSOMSTEP', 'BULLSEYE', 'COWTWO', 'COWFOUR', 'COWSIX', 'COWEIGHT', 'COWELEVEN',
                  'FINN', 'SCAR', 'BUSTER', 'HAWKBLAZE', 'CAKE']
    mostly_white = ['VAN', 'ONEEAR', 'LIGHTSONG', 'TAIL', 'HEART', 'MOORISH', 'APRON', 'CAPSADDLE',
                    'CHESTSPECK', 'BLACKSTAR', 'PETAL', 'HEARTTWO', 'MOTH', 'FRECKLEMASK', 'COW', 'TIDAL',
                    'DIAMOND', 'ECLIPSE', 'PEBBLESHINE', 'BOOTS', 'COWTHREE', 'COWFIVE', 'COWSEVEN', 'COWNINE', 'COWTEN',
                    'LOVEBUG', 'SHOOTINGSTAR', 'EYESPOT', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BATWING', 'KROPKA', "SMALLPATCHES"]
    point_markings = ['COLOURPOINT', 'RAGDOLL', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']
    vit = ['VITILIGO', 'VITILIGOTWO', 'MOON', 'PHANTOM', 'KARPATI', 'POWDER', 'SPLAT', 'BLEACHED', 'SMOKEY']
    white_sprites = [
            little_white, mid_white, high_white, mostly_white, point_markings, vit, 'FULLWHITE']

    skin_sprites = ['BLACK',  'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN', 'DARK', 'DARKGREY', 'GREY', 'DARKSALMON',
                    'SALMON', 'PEACH', 'DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE', 'RED']

    """Holds all appearence information for a cat. """
    def __init__(self,
                 name:str="SingleColour",
                 length:str="short",
                 colour:str="WHITE",
                 white_patches:str=None,
                 eye_color:str="BLUE",
                 eye_colour2:str=None,
                 eye_pattern:str=None,
                 tortiebase:str=None,
                 tortiecolour:str=None,
                 pattern:str=None,
                 tortiepattern:str=None,
                 vitiligo:str=None,
                 points:str=None,
                 accessory:str=None,
                 paralyzed:bool=False,
                 opacity:int=100,
                 scars:list=None,
                 tint:str="none",
                 skin:str="BLACK",
                 white_patches_tint:str="none",
                 kitten_sprite:int=None,
                 adol_sprite:int=None,
                 adult_sprite:int=None,
                 senior_sprite:int=None,
                 para_adult_sprite:int=None,
                 reverse:bool=False,
                 accessories:list=None,
                 inventory:list=[]
                 ) -> None:
        self.name = name
        self.colour = colour
        self.white_patches = white_patches
        self.eye_colour = eye_color
        self.eye_colour2 = eye_colour2
        self.eye_pattern = eye_pattern
        self.tortiebase = tortiebase
        self.pattern = pattern
        self.tortiepattern = tortiepattern
        self.tortiecolour = tortiecolour
        self.vitiligo = vitiligo
        self.length=length
        self.points = points
        self.accessory = accessory
        self.accessories = accessories if accessories is not None else []
        self.inventory = inventory
        self.paralyzed = paralyzed
        self.opacity = opacity
        self.scars = scars if isinstance(scars, list) else []
        self.tint = tint
        self.white_patches_tint = white_patches_tint
        self.cat_sprites =  {
            "kitten": kitten_sprite if kitten_sprite is not None else 0,
            "adolescent": adol_sprite if adol_sprite is not None else 0,
            "young adult": adult_sprite if adult_sprite is not None else 0,
            "adult": adult_sprite if adult_sprite is not None else 0,
            "senior adult": adult_sprite if adult_sprite is not None else 0,
            "senior": senior_sprite if senior_sprite is not None else 0,
            "para_adult": para_adult_sprite if para_adult_sprite is not None else 0,
        }                                           
        self.cat_sprites['newborn'] = 38
        self.cat_sprites['para_young'] = 32
        self.cat_sprites["sick_adult"] = 36
        self.cat_sprites["sick_young"] = 37
        
        self.reverse = reverse
        self.skin = skin

        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    @staticmethod
    def generate_new_pelt(gender:str, parents:tuple=(), age:str="adult"):
        new_pelt = Pelt()
        
        pelt_white = new_pelt.init_pattern_color(parents, gender)
        new_pelt.init_white_patches(pelt_white, parents)
        new_pelt.init_sprite()
        new_pelt.init_scars(age)
        new_pelt.init_accessories(age)
        new_pelt.init_eyes(parents)
        new_pelt.init_pattern()
        new_pelt.init_tint()
        
        return new_pelt
    
    def check_and_convert(self, convert_dict):
        """Checks for old-type properties for the apperence-related properties
        that are stored in Pelt, and converts them. To be run when loading a cat in. """
        
        #First, convert from some old names that may be in white_patches. 
        if self.white_patches == 'POINTMARK':
            self.white_patches = "SEALPOINT"
        elif self.white_patches == 'PANTS2':
            self.white_patches = 'PANTSTWO'
        elif self.white_patches == 'ANY2':
            self.white_patches = 'ANYTWO'
        elif self.white_patches == "VITILIGO2":
            self.white_patches = "VITILIGOTWO"
            
        if self.vitiligo == "VITILIGO2":
            self.vitiligo = "VITILIGOTWO"
        
        # Move white_patches that should be in vit or points. 
        if self.white_patches in Pelt.vit:
            self.vitiligo = self.white_patches
            self.white_patches = None
        elif self.white_patches in Pelt.point_markings:
            self.points = self.white_patches
            self.white_patches = None

        
        if self.tortiepattern and "tortie" in self.tortiepattern:
            self.tortiepattern = sub("tortie", "", self.tortiepattern.lower())
            if self.tortiepattern == "solid":
                self.tortiepattern = "single"
                
        if self.white_patches in convert_dict["old_creamy_patches"]:
            self.white_patches = convert_dict["old_creamy_patches"][self.white_patches]
            self.white_patches_tint = "darkcream"
        elif self.white_patches in ['SEPIAPOINT', 'MINKPOINT', 'SEALPOINT']:
            self.white_patches_tint = "none"
        
        # Eye Color Convert Stuff
        if self.eye_colour == "BLUE2":
            self.eye_colour = "COBALT"
        if self.eye_colour2 == "BLUE2":
            self.eye_colour2 = "COBALT"
            
        if self.eye_colour in ["BLUEYELLOW", "BLUEGREEN"]:
            if self.eye_colour == "BLUEYELLOW":
                self.eye_colour2 = "YELLOW"
            elif self.eye_colour == "BLUEGREEN":
                self.eye_colour2 = "GREEN"
            self.eye_colour = "BLUE"
        
        if self.length == 'long':
            if self.cat_sprites['adult'] not in [15, 16, 17, 18, 19, 20, 21, 22, 23]:
                if self.cat_sprites['adult'] == 0:
                    self.cat_sprites['adult'] = 18
                elif self.cat_sprites['adult'] == 1:
                    self.cat_sprites['adult'] = 19
                elif self.cat_sprites['adult'] == 2:
                    self.cat_sprites['adult'] = 20
                elif self.cat_sprites['adult'] == 9:
                    self.cat_sprites['adult'] = 21
                elif self.cat_sprites['adult'] == 10:
                    self.cat_sprites['adult'] = 22
                elif self.cat_sprites['adult'] == 11:
                    self.cat_sprites['adult'] = 23
                self.cat_sprites['young adult'] = self.cat_sprites['adult']
                self.cat_sprites['senior adult'] = self.cat_sprites['adult']
                self.cat_sprites['para_adult'] = 31
            if self.cat_sprites['senior'] not in [24, 25, 26, 27, 28, 29]:
                if self.cat_sprites['senior'] == 3:
                    self.cat_sprites['senior'] = 27
                elif self.cat_sprites['senior'] == 4:
                    self.cat_sprites['senior'] = 28
                elif self.cat_sprites['senior'] == 5:
                    self.cat_sprites['senior'] = 29
                elif self.cat_sprites['senior'] == 12:
                    self.cat_sprites['senior'] = 27
                elif self.cat_sprites['senior'] == 13:
                    self.cat_sprites['senior'] = 28
                elif self.cat_sprites['senior'] == 14:
                    self.cat_sprites['senior'] = 29
            if self.cat_sprites['adolescent'] not in [6, 7, 8, 9, 10, 11]:
                if self.cat_sprites['adolescent'] == 3:
                    self.cat_sprites['adolescent'] = 9
                elif self.cat_sprites['adolescent'] == 4:
                    self.cat_sprites['adolescent'] = 10
                elif self.cat_sprites['adolescent'] == 5:
                    self.cat_sprites['adolescent'] = 11
            if self.cat_sprites['kitten'] not in [3, 4, 5]:
                if self.cat_sprites['kitten'] == 0:
                    self.cat_sprites['kitten'] = 3
                elif self.cat_sprites['kitten'] == 1:
                    self.cat_sprites['kitten'] = 4
                elif self.cat_sprites['kitten'] == 2:
                    self.cat_sprites['kitten'] = 5
        else:
            self.cat_sprites['para_adult'] = 30
        if self.cat_sprites['adult'] not in [15, 16, 17, 18, 19, 20, 21, 22, 23]:
            if self.cat_sprites['adult'] == 0:
                self.cat_sprites['adult'] = 12
            elif self.cat_sprites['adult'] == 1:
                self.cat_sprites['adult'] = 13
            elif self.cat_sprites['adult'] == 2:
                self.cat_sprites['adult'] = 14
            elif self.cat_sprites['adult'] == 6:
                self.cat_sprites['adult'] = 15
            elif self.cat_sprites['adult'] == 7:
                self.cat_sprites['adult'] = 16
            elif self.cat_sprites['adult'] == 8:
                self.cat_sprites['adult'] = 17
            self.cat_sprites['young adult'] = self.cat_sprites['adult']
            self.cat_sprites['senior adult'] = self.cat_sprites['adult']
        if self.cat_sprites['senior'] not in [24, 25, 26, 27, 28, 29]:
            if self.cat_sprites['senior'] == 3:
                self.cat_sprites['senior'] = 24
            elif self.cat_sprites['senior'] == 4:
                self.cat_sprites['senior'] = 25
            elif self.cat_sprites['senior'] == 5:
                self.cat_sprites['senior'] = 26
            elif self.cat_sprites['senior'] == 12:
                self.cat_sprites['senior'] = 24
            elif self.cat_sprites['senior'] == 13:
                self.cat_sprites['senior'] = 25
            elif self.cat_sprites['senior'] == 14:
                self.cat_sprites['senior'] = 26
        if self.cat_sprites['adolescent'] not in [6, 7, 8, 9, 10, 11]:
            if self.cat_sprites['adolescent'] == 3:
                self.cat_sprites['adolescent'] = 6
            elif self.cat_sprites['adolescent'] == 4:
                self.cat_sprites['adolescent'] = 7
            elif self.cat_sprites['adolescent'] == 5:
                self.cat_sprites['adolescent'] = 8                  
        if self.pattern in convert_dict["old_tortie_patches"]:
            old_pattern = self.pattern
            self.pattern = convert_dict["old_tortie_patches"][old_pattern][1]
            
            # If the pattern is old, there is also a change the base color is stored in
            # tortiecolour, and that may be different from the pelt color (main for torties
            # generated before the "ginger-on-ginger" update. If it was generated after that update,
            # tortiecolour and pelt_colour will be the same. Therefore, lets also re-set the pelt color
            self.colour = self.tortiecolour
            self.tortiecolour = convert_dict["old_tortie_patches"][old_pattern][0]
            
        if self.pattern == "MINIMAL1":
            self.pattern = "MINIMALONE"
        elif self.pattern == "MINIMAL2":
            self.pattern = "MINIMALTWO"
        elif self.pattern == "MINIMAL3":
            self.pattern = "MINIMALTHREE"
        elif self.pattern == "MINIMAL4":
            self.pattern = "MINIMALFOUR"
        elif self.pattern == "SPLIT":
            self.pattern = "HALF"
        
    def init_eyes(self, parents):
        if not parents:
            self.eye_colour = choice(Pelt.eye_colours)
        else:
            self.eye_colour = choice([i.pelt.eye_colour for i in parents] + [choice(Pelt.eye_colours)])
        
        #White patches must be initalized before eye color. 
        num = game.config["cat_generation"]["base_heterochromia"]
        if self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE'] or self.colour == 'WHITE' or self.colour == 'SNOW WHITE':
            num = num - 90
        if self.white_patches == 'FULLWHITE' or self.colour == 'WHITE' or self.colour == 'SNOW WHITE':
            num -= 10
        for _par in parents:
            if _par.pelt.eye_colour2:
                num -= 10
        
        if num < 0:
            num = 1
        hit = random.randint(0, num)
        if hit == 0:
            if self.eye_colour in Pelt.yellow_eyes:
                eye_choice = choice([Pelt.blue_eyes, Pelt.green_eyes, Pelt.red_eyes, Pelt.grey_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.blue_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.green_eyes, Pelt.red_eyes, Pelt.grey_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.green_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.red_eyes, Pelt.grey_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.red_eyes:
                eye_choice = choice([Pelt.blue_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.grey_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.grey_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.red_eyes, Pelt.purple_eyes])
                self.eye_colour2 = choice(eye_choice)
            elif self.eye_colour in Pelt.purple_eyes:
                eye_choice = choice([Pelt.yellow_eyes, Pelt.blue_eyes, Pelt.green_eyes, Pelt.red_eyes, Pelt.grey_eyes])
                self.eye_colour2 = choice(eye_choice)

        if hit == 0:
            self.eye_pattern = choice(Pelt.eye_patterns)
        else:
            self.eye_pattern = None
    def pattern_color_inheritance(self, parents: tuple=(), gender="female"):
        # setting parent pelt categories
        #We are using a set, since we don't need this to be ordered, and sets deal with removing duplicates.
        par_peltlength = set()
        par_peltcolours = set()
        par_peltnames = set()
        par_pelts = []
        par_white = []
        for p in parents:
            if p:
                # Gather pelt color.
                par_peltcolours.add(p.pelt.colour)

                # Gather pelt length
                par_peltlength.add(p.pelt.length)

                # Gather pelt name
                if p.pelt.name in Pelt.torties:
                    par_peltnames.add(p.pelt.tortiebase.capitalize())
                else:
                    par_peltnames.add(p.pelt.name)

                # Gather exact pelts, for direct inheritance.
                par_pelts.append(p.pelt)

                # Gather if they have white in their pelt.
                par_white.append(p.pelt.white)
            else:
                # If order for white patches to work correctly, we also want to randomly generate a "pelt_white"
                # for each "None" parent (missing or unknown parent)
                par_white.append(bool(random.getrandbits(1)))

                # Append None
                # Gather pelt color.
                par_peltcolours.add(None)
                par_peltlength.add(None)
                par_peltnames.add(None)

        # If this list is empty, something went wrong.
        if not par_peltcolours:
            print("Warning - no parents: pelt randomized")
            return self.randomize_pattern_color(gender)

        # There is a 1/10 chance for kits to have the exact same pelt as one of their parents
        if not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):  # 1/10 chance
            selected = choice(par_pelts)
            self.name = selected.name
            self.length = selected.length
            self.colour = selected.colour
            self.tortiebase = selected.tortiebase
            return selected.white

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        weights = [0, 0, 0, 0, 0,
                   0]  # Weights for each pelt group. It goes: (points, spots, swirls, flats, stripes, exotic)
        for p_ in par_peltnames:
            if p_ in Pelt.points:
                add_weight = (100, 5, 0, 25, 15, 0)
            elif p_ in Pelt.spots:
                add_weight = (5, 100, 0, 5, 0, 15)
            elif p_ in Pelt.swirls:
                add_weight = (0, 0, 100, 15, 30, 5)
            elif p_ in Pelt.flats:
                add_weight = (25, 5, 0, 100, 5, 0)
            elif p_ in Pelt.stripes:
                add_weight = (5, 0, 35, 5, 100, 5)
            elif p_ in Pelt.exotic:
                add_weight = (30, 15, 0, 0, 0, 100)
            elif p_ is None:  # If there is at least one unknown parent, a None will be added to the set.
                add_weight = (20, 10, 15, 50, 10, 5)
            else:
                add_weight = (0, 0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        #A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1, 1, 1, 1]

        # Now, choose the pelt category and pelt. The extra 0 is for the tortie pelts,
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=weights + [0], k = 1)[0]
        )

        # Tortie chance
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"]  # There is a default chance for female tortie
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        for p_ in par_pelts:
            if p_.name in Pelt.torties:
                tortie_chance_f = int(tortie_chance_f / 2)
                tortie_chance_m = tortie_chance_m - 1
                break

        # Determine tortie:
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#
        # Weights for each colour group. It goes: (white_colours, blue_colours, gray_colours, black_colours,
        # cream_colours, gold_colours, fire_colours, ginger_colours, coolbrown_colours, lavender_colours, warmbrown_colours,
        # brown_colours)
        weights = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        for p_ in par_peltcolours:
            if p_ in Pelt.white_colours:
                add_weight = (200, 90, 50, 5, 10, 5, 5, 5, 5, 10, 5, 5)
            elif p_ in Pelt.blue_colours:
                add_weight = (90, 200, 50, 70, 10, 5, 5, 5, 5, 10, 0, 5)
            elif p_ in Pelt.gray_colours:
                add_weight = (30, 30, 200, 70, 5, 10, 5, 5, 10, 5, 10, 5)
            elif p_ in Pelt.black_colours:
                add_weight = (5, 30, 50, 200, 5, 5, 5, 5, 5, 5, 5, 5)
            elif p_ in Pelt.cream_colours:
                add_weight = (5, 5, 10, 5, 200, 50, 70, 70, 5, 10, 5, 5)
            elif p_ in Pelt.gold_colours:
                add_weight = (30, 5, 5, 5, 30, 200, 70, 70, 10, 5, 10, 5)
            elif p_ in Pelt.fire_colours:
                add_weight = (5, 5, 5, 5, 30, 50, 200, 90, 5, 5, 5, 10)
            elif p_ in Pelt.ginger_colours:
                add_weight = (5, 5, 5, 5, 30, 50, 90, 200, 5, 5, 5, 10)
            elif p_ in Pelt.coolbrown_colours:
                add_weight = (5, 5, 10, 5, 5, 10, 5, 5, 200, 30, 90, 70)
            elif p_ in Pelt.lavender_colours:
                add_weight = (10, 10, 5, 5, 10, 5, 5, 5, 50, 200, 50, 70)
            elif p_ in Pelt.warmbrown_colours:
                add_weight = (5, 5, 10, 5, 5, 10, 5, 5, 90, 30, 200, 70)
            elif p_ in Pelt.brown_colours:
                add_weight = (5, 5, 5, 10, 5, 5, 10, 10, 50, 30, 50, 200)
            elif p_ is None:
                add_weight = (30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30, 30)
            else:
                add_weight = (0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

            # A quick check to make sure all the weights aren't 0
            if all([x == 0 for x in weights]):
                weights = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

        chosen_pelt_color = choice(
            random.choices(Pelt.colour_categories, weights=weights, k=1)[0]
        )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#

        weights = [0, 0, 0]  # Weights for each length. It goes (short, medium, long)
        for p_ in par_peltlength:
            if p_ == "short":
                add_weight = (50, 10, 2)
            elif p_ == "medium":
                add_weight = (25, 50, 25)
            elif p_ == "long":
                add_weight = (2, 10, 50)
            elif p_ is None:
                add_weight = (10, 10, 10)
            else:
                add_weight = (0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weight[x]

        # A quick check to make sure all the weights aren't 0
        if all([x == 0 for x in weights]):
            weights = [1, 1, 1]

        chosen_pelt_length = random.choices(Pelt.pelt_length, weights=weights, k=1)[0]

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#

        # There is 94 percentage points that can be added by
        # parents having white. If we have more than two, this
        # will keep that the same.
        percentage_add_per_parent = int(94 / len(par_white))
        chance = 3
        for p_ in par_white:
            if p_:
                chance += percentage_add_per_parent

        chosen_white = random.randint(1, 100) <= chance

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        # SET THE PELT
        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        return chosen_white

    def randomize_pattern_color(self, gender):
        # ------------------------------------------------------------------------------------------------------------#
        #   PELT
        # ------------------------------------------------------------------------------------------------------------#

        # Determine pelt.
        chosen_pelt = choice(
            random.choices(Pelt.pelt_categories, weights=(35, 20, 30, 15, 20, 15, 0), k=1)[0]
        )

        # Tortie chance
        # There is a default chance for female tortie, slightly increased for completely random generation.
        tortie_chance_f = game.config["cat_generation"]["base_female_tortie"] - 1
        tortie_chance_m = game.config["cat_generation"]["base_male_tortie"]
        if gender == "female":
            torbie = random.getrandbits(tortie_chance_f) == 1
        else:
            torbie = random.getrandbits(tortie_chance_m) == 1

        chosen_tortie_base = None
        if torbie:
            # If it is tortie, the chosen pelt above becomes the base pelt.
            chosen_tortie_base = chosen_pelt
            if chosen_tortie_base in ["TwoColour", "SingleColour"]:
                chosen_tortie_base = "Single"
            chosen_tortie_base = chosen_tortie_base.lower()
            chosen_pelt = random.choice(Pelt.torties)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT COLOUR
        # ------------------------------------------------------------------------------------------------------------#

        chosen_pelt_color = choice(
            random.choices(Pelt.colour_categories, k=1)[0]
        )

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT LENGTH
        # ------------------------------------------------------------------------------------------------------------#


        chosen_pelt_length = random.choice(Pelt.pelt_length)

        # ------------------------------------------------------------------------------------------------------------#
        #   PELT WHITE
        # ------------------------------------------------------------------------------------------------------------#


        chosen_white = random.randint(1, 100) <= 40

        # Adjustments to pelt chosen based on if the pelt has white in it or not.
        if chosen_pelt in ["TwoColour", "SingleColour"]:
            if chosen_white:
                chosen_pelt = "TwoColour"
            else:
                chosen_pelt = "SingleColour"
        elif chosen_pelt == "Calico":
            if not chosen_white:
                chosen_pelt = "Tortie"

        self.name = chosen_pelt
        self.colour = chosen_pelt_color
        self.length = chosen_pelt_length
        self.tortiebase = chosen_tortie_base   # This will be none if the cat isn't a tortie.
        return chosen_white

    def init_pattern_color(self, parents, gender) -> bool:
        """Inits self.name, self.colour, self.length, 
            self.tortiebase and determines if the cat 
            will have white patche or not. 
            Return TRUE is the cat should have white patches, 
            false is not. """
        
        if parents:
            #If the cat has parents, use inheritance to decide pelt.
            chosen_white = self.pattern_color_inheritance(parents, gender)
        else:
            chosen_white = self.randomize_pattern_color(gender)
        
        return chosen_white

    def init_sprite(self):
        self.cat_sprites = {
            'newborn': 38,
            'sick_young': 37,
            'sick_adult': 36
        }
        self.reverse = choice([True, False])
        # skin chances
        self.skin = choice(Pelt.skin_sprites)

        if self.length != 'long':
            self.cat_sprites['kitten'] = random.randint(0, 2)
            self.cat_sprites['adolescent'] = random.randint(6, 8)
            self.cat_sprites['adult'] = random.randint(12, 17)
            self.cat_sprites['senior'] = random.randint(24, 26)
            self.cat_sprites['para_adult'] = 30
        else:
            self.cat_sprites['kitten'] = random.randint(3, 5)
            self.cat_sprites['adolescent'] = random.randint(9, 11)
            self.cat_sprites['adult'] = random.randint(18, 23)
            self.cat_sprites['senior'] = random.randint(27, 29)
            self.cat_sprites['para_adult'] = 31
        self.cat_sprites['young adult'] = self.cat_sprites['adult']
        self.cat_sprites['senior adult'] = self.cat_sprites['adult']

    def init_scars(self, age):
        if age == "newborn":
            return
        
        if age in ['kitten', 'adolescent']:
            scar_choice = random.randint(0, 50)
        elif age in ['young adult', 'adult']:
            scar_choice = random.randint(0, 20)
        else:
            scar_choice = random.randint(0, 15)

        if scar_choice == 1:
            self.scars.append(choice([
                choice(Pelt.scars1),
                choice(Pelt.scars3)
            ]))

        if 'NOTAIL' in self.scars and 'HALFTAIL' in self.scars:
            self.scars.remove('HALFTAIL')

    def init_accessories(self, age):
        if age == "newborn": 
            self.accessory = None
            return
        
        acc_display_choice = random.randint(0, 80)
        if age in ['kitten', 'adolescent']:
            acc_display_choice = random.randint(0, 180)
        elif age in ['young adult', 'adult']:    
            acc_display_choice = random.randint(0, 100)
        
        if acc_display_choice == 1:
            self.accessory = choice([
                choice(Pelt.plant_accessories),
                choice(Pelt.wild_accessories),
                choice(Pelt.flower_accessories),
                choice(Pelt.plant2_accessories),
                choice(Pelt.wild2_accessories),
                choice(Pelt.snake_accessories),
                choice(Pelt.smallAnimal_accessories),
                choice(Pelt.deadInsect_accessories),
                choice(Pelt.aliveInsect_accessories),
                choice(Pelt.fruit_accessories),
                choice(Pelt.crafted_accessories),
                choice(Pelt.tail2_accessories)
            ])
        else:
            self.accessory = None

    def init_pattern(self):
        if self.name in Pelt.torties:
            if not self.tortiebase:
                self.tortiebase = choice(Pelt.tortiebases)
            if not self.pattern:
                self.pattern = choice(Pelt.tortiepatterns)

            wildcard_chance = game.config["cat_generation"]["wildcard_tortie"]
            if self.colour:
                # The "not wildcard_chance" allows users to set wildcard_tortie to 0
                # and always get wildcard torties.
                if not wildcard_chance or random.getrandbits(wildcard_chance) == 1:
                    # This is the "wildcard" chance, where you can get funky combinations.
                    # people are fans of the print message so I'm putting it back
                    print("Wildcard tortie!")

                    # Allow any pattern:
                    self.tortiepattern = choice(Pelt.tortiebases)

                    # Allow any colors that aren't the base color.
                    possible_colors = Pelt.pelt_colours.copy()
                    possible_colors.remove(self.colour)
                    self.tortiecolour = choice(possible_colors)

                else:
                    # Normal generation
                    if self.tortiebase in ["singlestripe", "smoke", "single"]:
                        self.tortiepattern = choice(['tabby', 'mackerel', 'classic', 'single', 'smoke', 'agouti',
                                                    'ticked'])
                    else:
                        self.tortiepattern = random.choices([self.tortiebase, 'single'], weights=[97, 3], k=1)[0]

                    if self.tortiebase in ["single"]:
                        self.tortiepattern = choice(['tabby', 'mackerel', 'classic', 'single', 'masked', 'brindle',
                                                     'marbled', 'saber', 'bengal', 'rosette', 'speckled', 'sokoke',
                                                     'brokenmackerel', 'charcoalbengal', 'brokenbraided'])
                    else:
                        self.tortiepattern = random.choices([self.tortiebase, 'single'], weights=[97, 3], k=1)[0]

                    possible_colors = Pelt.pelt_colours.copy()
                    possible_colors.remove(self.colour)

                    # Ginger is often duplicated to increase its chances
                    if self.colour in Pelt.black_colours:
                        self.tortiecolour = choice(Pelt.blue_colours + Pelt.gold_colours + (Pelt.fire_colours * 4) + (
                                    Pelt.ginger_colours * 4) + Pelt.coolbrown_colours + Pelt.lavender_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.white_colours:
                        self.tortiecolour = choice((Pelt.cream_colours * 2) + (Pelt.blue_colours * 2) + Pelt.black_colours)
                    elif self.colour in Pelt.blue_colours:
                        self.tortiecolour = choice(Pelt.black_colours + (
                                    Pelt.cream_colours * 4) + Pelt.gold_colours + Pelt.fire_colours + Pelt.ginger_colours + Pelt.warmbrown_colours + Pelt.coolbrown_colours)
                    elif self.colour in Pelt.gray_colours:
                        self.tortiecolour = choice(Pelt.gold_colours + (Pelt.fire_colours * 4) + (
                                    Pelt.ginger_colours * 4) + Pelt.lavender_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.cream_colours:
                        self.tortiecolour = choice((Pelt.blue_colours * 4) + Pelt.black_colours + (
                                    Pelt.cream_colours * 4) + Pelt.fire_colours + Pelt.ginger_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.gold_colours:
                        self.tortiecolour = choice(Pelt.blue_colours + Pelt.gray_colours + (
                                    Pelt.black_colours * 4) + Pelt.ginger_colours + Pelt.coolbrown_colours + Pelt.lavender_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.fire_colours:
                        self.tortiecolour = choice(Pelt.blue_colours + Pelt.gray_colours + (
                                    Pelt.black_colours * 4) + Pelt.cream_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.ginger_colours:
                        self.tortiecolour = choice(Pelt.blue_colours + (Pelt.gray_colours * 4) + (
                                    Pelt.black_colours * 4) + Pelt.cream_colours + Pelt.gold_colours + Pelt.fire_colours + Pelt.coolbrown_colours + Pelt.lavender_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.coolbrown_colours:
                        self.tortiecolour = choice(
                            Pelt.gray_colours + Pelt.black_colours + Pelt.gold_colours + Pelt.fire_colours + Pelt.ginger_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.lavender_colours:
                        self.tortiecolour = choice(
                            Pelt.gray_colours + Pelt.black_colours + Pelt.gold_colours + Pelt.fire_colours + Pelt.ginger_colours + Pelt.warmbrown_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.warmbrown_colours:
                        self.tortiecolour = choice(
                            Pelt.blue_colours + Pelt.gray_colours + (Pelt.black_colours * 4) + Pelt.cream_colours + Pelt.gold_colours + (
                                        Pelt.fire_colours * 4) + Pelt.ginger_colours + Pelt.brown_colours)
                    elif self.colour in Pelt.brown_colours:
                        self.tortiecolour = choice(
                            Pelt.blue_colours + Pelt.gray_colours + (Pelt.black_colours * 4) + Pelt.cream_colours + Pelt.gold_colours + (
                                        Pelt.fire_colours * 4) + (Pelt.ginger_colours * 4) + Pelt.coolbrown_colours)
                    else:
                        self.tortiecolour = "GOLD"

            else:
                self.tortiecolour = "GOLD"
        else:
            self.tortiebase = None
            self.tortiepattern = None
            self.tortiecolour = None
            self.pattern = None

    def white_patches_inheritance(self, parents: tuple):

        par_whitepatches = set()
        par_points = []
        for p in parents:
            if p:
                if p.pelt.white_patches:
                    par_whitepatches.add(p.pelt.white_patches)
                if p.pelt.points:
                    par_points.append(p.pelt.points)

        if not parents:
            print("Error - no parents. Randomizing white patches.")
            self.randomize_white_patches()
            return

        # Direct inheritance. Will only work if at least one parent has white patches, otherwise continue on.
        if par_whitepatches and not random.randint(0, game.config["cat_generation"]["direct_inheritance"]):
            # This ensures Torties and Calicos won't get direct inheritance of incorrect white patch types
            _temp = par_whitepatches.copy()
            if self.name == "Tortie":
                for p in _temp.copy():
                    if p in Pelt.high_white + Pelt.mostly_white + ["FULLWHITE"]:
                        _temp.remove(p)
            elif self.name == "Calico":
                for p in _temp.copy():
                    if p in Pelt.little_white + Pelt.mid_white:
                        _temp.remove(p)

            # Only proceed with the direct inheritance if there are white patches that match the pelt.
            if _temp:
                self.white_patches = choice(list(_temp))

                # Direct inheritance also effect the point marking.
                if par_points and self.name != "Tortie":
                    self.points = choice(par_points)
                else:
                    self.points = None

                return

        # dealing with points
        if par_points:
            chance = 10 - len(par_points)
        else:
            chance = 40

        if self.name != "Tortie" and not (random.random() * chance):
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None


        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]

        weights = [0, 0, 0, 0, 0]  # Same order as white_list
        for p_ in par_whitepatches:
            if p_ in Pelt.little_white:
                add_weights = (40, 20, 15, 5, 0)
            elif p_ in Pelt.mid_white:
                add_weights = (10, 40, 15, 10, 0)
            elif p_ in Pelt.high_white:
                add_weights = (15, 20, 40, 10, 1)
            elif p_ in Pelt.mostly_white:
                add_weights = (5, 15, 20, 40, 5)
            elif p_ == "FULLWHITE":
                add_weights = (0, 5, 15, 40, 10)
            else:
                add_weights = (0, 0, 0, 0, 0)

            for x in range(0, len(weights)):
                weights[x] += add_weights[x]


        # If all the weights are still 0, that means none of the parents have white patches.
        if not any(weights):
            if not all(parents):  # If any of the parents are None (unknown), use the following distribution:
                weights = [20, 10, 10, 5, 0]
            else:
                # Otherwise, all parents are known and don't have any white patches. Focus distribution on little_white.
                weights = [50, 5, 0, 0, 0]

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = weights[:2] + [0, 0, 0]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]
        elif self.name == "Calico":
            weights = [0, 0, 0] + weights[3:]
            # Another check to make sure not all the values are zero. This should never happen, but better
            # safe then sorry.
            if not any(weights):
                weights = [2, 1, 0, 0, 0]

        chosen_white_patches = choice(
            random.choices(white_list, weights=weights, k=1)[0]
        )

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def randomize_white_patches(self):

        # Points determination. Tortie can't be pointed
        if self.name != "Tortie" and not random.getrandbits(game.config["cat_generation"]["random_point_chance"]):
            # Cat has colorpoint!
            self.points = choice(Pelt.point_markings)
        else:
            self.points = None

        # Adjust weights for torties, since they can't have anything greater than mid_white:
        if self.name == "Tortie":
            weights = (2, 1, 0, 0, 0)
        elif self.name == "Calico":
            weights = (0, 0, 20, 15, 1)
        else:
            weights = (10, 10, 10, 10, 1)

        white_list = [Pelt.little_white, Pelt.mid_white, Pelt.high_white, Pelt.mostly_white, ['FULLWHITE']]
        chosen_white_patches = choice(
            random.choices(white_list, weights=weights, k=1)[0]
        )

        self.white_patches = chosen_white_patches
        if self.points and self.white_patches in [Pelt.high_white, Pelt.mostly_white, 'FULLWHITE']:
            self.points = None

    def init_white_patches(self, pelt_white, parents:tuple):
        # Vit can roll for anyone, not just cats who rolled to have white in their pelt. 
        par_vit = []
        for p in parents:
            if p:
                if p.pelt.vitiligo:
                    par_vit.append(p.pelt.vitiligo)
        
        vit_chance = max(game.config["cat_generation"]["vit_chance"] - len(par_vit), 0)
        if not random.getrandbits(vit_chance):
            self.vitiligo = choice(Pelt.vit)

        # If the cat was rolled previously to have white patches, then determine the patch they will have
        # these functions also handle points. 
        if pelt_white:
            if parents:
                self.white_patches_inheritance(parents)
            else:
                self.randomize_white_patches()
        else:
            self.white_patches = None
            self.points = None

    def init_tint(self):
        """Sets tint for pelt and white patches"""

        # PELT TINT
        # Basic tints as possible for all colors.
        base_tints = sprites.cat_tints["possible_tints"]["basic"]
        if self.colour in sprites.cat_tints["colour_groups"]:
            color_group = sprites.cat_tints["colour_groups"].get(self.colour, "warm")
            color_tints = sprites.cat_tints["possible_tints"][color_group]
        else:
            color_tints = []
        
        if base_tints or color_tints:
            self.tint = choice(base_tints + color_tints)
        else:
            self.tint = "none"

        # WHITE PATCHES TINT
        if self.white_patches or self.points:
            #Now for white patches
            base_tints = sprites.white_patches_tints["possible_tints"]["basic"]
            if self.colour in sprites.cat_tints["colour_groups"]:
                color_group = sprites.white_patches_tints["colour_groups"].get(self.colour, "white")
                color_tints = sprites.white_patches_tints["possible_tints"][color_group]
            else:
                color_tints = []
            
            if base_tints or color_tints:
                self.white_patches_tint = choice(base_tints + color_tints)
            else:
                self.white_patches_tint = "none"    
        else:
            self.white_patches_tint = "none"

    @property
    def white(self):
        return self.white_patches or self.points
    
    @white.setter
    def white(self, val):
        print("Can't set pelt.white")
        return    

    @staticmethod
    def describe_appearance(cat, short=False):
        
        # Define look-up dictionaries
        if short:
            renamed_colors = {
                "white": "white",
                "snow white": "white",
                "gray": "gray",
                "slate": "gray",
                "dark gray": "gray",
                "dark slate": "gray",
                "pale blue": "blue",
                "blue": "blue",
                "lilac": "lilac",
                "pale lilac": "lilac",
                "silver": "silver",
                "black": "black",
                "soot black": "black",
                "obsidian": "black",
                "ghost": "black",
                "pale brown": "brown",
                "almond": "brown",
                "acorn": "brown",
                "light brown": "brown",
                "brown": "brown",
                "dark brown": "brown",
                "pale cinnamon": "ginger",
                "cinnamon": "ginger",
                "sable": "brown",
                "dark sable": "brown",
                "birch": "cream",
                "pale lavender": "lilac",
                "lavender": "lilac",
                "dark lavender": "lilac",
                "dark orange": "ginger",
                "pale fire": "ginger",
                "fire": "ginger",
                "dark fire": "ginger",
                "pale ginger": "ginger",
                "ginger": "ginger",
                "dark ginger": "ginger",
                "pale gold": "cream",
                "yellow": "cream",
                "gold": "gold",
                "bronze": "ginger",
                "rose": "ginger",
                "light cream": "cream",
                "cream": "cream",
                "dark cream": "cream",
                "dark gold": "gold"

            }
        else:
            renamed_colors = {
                "white": "white",
                "snow white": "snow white",
                "gray": "gray",
                "slate": "slate",
                "dark gray": "dark gray",
                "dark slate": "dark slate",
                "pale blue": "pale blue",
                "blue": "blue",
                "lilac": "lilac",
                "pale lilac": "pale lilac",
                "silver": "silver",
                "black": "black",
                "soot black": "soot black",
                "obsidian": "obsidian",
                "ghost": "ghost",
                "pale brown": "pale brown",
                "almond": "almond",
                "acorn": "acorn",
                "light brown": "light brown",
                "brown": "brown",
                "dark brown": "dark brown",
                "pale cinnamon": "pale cinnamon",
                "cinnamon": "cinnamon",
                "sable": "sable",
                "dark sable": "dark sable",
                "birch": "birch",
                "pale lavender": "pale lavender",
                "lavender": "lavender",
                "dark lavender": "dark lavender",
                "dark orange": "dark orange",
                "pale fire": "pale fire-red",
                "fire": "fire-red",
                "dark fire": "dark fire-red",
                "pale ginger": "pale ginger",
                "ginger": "ginger",
                "dark ginger": "dark ginger",
                "pale gold": "pale gold",
                "yellow": "yellow",
                "gold": "gold",
                "bronze": "bronze",
                "rose": "rose",
                "light cream": "light cream",
                "cream": "cream",
                "dark cream": "dark cream",
                "dark gold": "dark gold"
            }

        pattern_des = {
            "Tabby": "c_n tabby",
            "Speckled": "speckled c_n",
            "Bengal": "c_n bengal",
            "Marbled": "c_n marbled tabby",
            "Ticked": "c_n ticked tabby",
            "Smoke": "c_n smoke",
            "Mackerel": "c_n mackerel tabby",
            "Classic": "c_n classic tabby",
            "Agouti": "c_n agouti tabby",
            "Singlestripe": "dorsal-striped c_n",
            "Rosette": "rosetted c_n",
            "Sokoke": "c_n sokoke tabby",
            "Abyssinian": "c_n abyssinian",
            "Brindle": "c_n brindle",
            "Braided": "c_n braided tabby",
            "Splotch": "unusually splotched c_n",
            "Saber": "c_n saber tabby",
            "Faded": "c_n faded tabby",
            "Masked": "c_n masked tabby",
            "Fog": "c_n foggy tabby",
            "Mist": "c_n misted tabby",
            "Smudge": "c_n smudge tabby",
            "BrokenMackerel": "c_n broken mackerel tabby",
            "Longdan": "c_n longdan tiger tabby",
            "BrokenBraided": "c_n broken braided tabby",
            "CharcoalBengal": "c_n charcoal bengal",
            "Dust": "c_n dust"
        }

        # Start with determining the base color name. 
        color_name = str(cat.pelt.colour).lower()
        if color_name in renamed_colors:
            color_name = renamed_colors[color_name]
        
        # Replace "white" with "pale" if the cat is 
        if cat.pelt.name not in ["SingleColour", "TwoColour", "Tortie", "Calico"] and color_name == "white":
            color_name = "pale"

        # Time to descibe the pattern and any additional colors. 
        if cat.pelt.name in pattern_des:
            color_name = pattern_des[cat.pelt.name].replace("c_n", color_name)
        elif cat.pelt.name in Pelt.torties:
            # Calicos and Torties need their own desciptions. 
            if short:
                # If using short, don't add describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                # If using short, don't describe the colors of calicos and torties. Just call them calico, tortie, or mottled. 
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                    color_name = "mottled"
                else:
                    color_name = cat.pelt.name.lower()
            else:
                base = cat.pelt.tortiebase.lower()
                if base in Pelt.stripes + ['bengal', 'rosette', 'speckled', 'faded', 'saber', 'tabby', 'classic', 'sokoke', 'marbled', 'masked', 'brokenmackerel', 'longdan', 'smudge', 'brokenbraided']:
                    base = 'tabby'
                else:
                    base = ''

                patches_color = cat.pelt.tortiecolour.lower()
                if patches_color in renamed_colors:
                    patches_color = renamed_colors[patches_color]
                color_name = f"{color_name}/{patches_color}"
                
                if cat.pelt.colour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours and \
                    cat.pelt.tortiecolour in Pelt.black_colours + Pelt.brown_colours + Pelt.white_colours:
                        color_name = f"{color_name} mottled"
                else:
                    color_name = f"{color_name} {cat.pelt.name.lower()}"

        if cat.pelt.white_patches:
            if cat.pelt.white_patches_tint == "black":
                if cat.pelt.white_patches == "FULLWHITE":
                    # If the cat is fullwhite, discard all other information. They are just white.
                    color_name = "black"
                if cat.pelt.white_patches in Pelt.mostly_white and cat.pelt.name != "Calico":
                    color_name = f"black and {color_name}"
                elif cat.pelt.name != "Calico":
                    color_name = f"{color_name} and black"
            else:
                if cat.pelt.white_patches == "FULLWHITE":
                    # If the cat is fullwhite, discard all other information. They are just white.
                    color_name = "white"
                if cat.pelt.white_patches in Pelt.mostly_white and cat.pelt.name != "Calico":
                    color_name = f"white and {color_name}"
                elif cat.pelt.name != "Calico":
                    color_name = f"{color_name} and white"

        if cat.pelt.points:
            color_name = f"{color_name} point"
            if "ginger point" in color_name:
                color_name.replace("ginger point", "flame point")

        if "white and white" in color_name:
            color_name = color_name.replace("white and white", "white")

        if "black and black" in color_name:
            color_name = color_name.replace("black and black", "black")

        # Now it's time for gender
        if cat.genderalign in ["female", "trans female"]:
            color_name = f"{color_name} she-cat"
        elif cat.genderalign in ["male", "trans male"]:
            color_name = f"{color_name} tom"
        else:
            color_name = f"{color_name} cat"

        # Here is the place where we can add some additional details about the cat, for the full non-short one
        # These include notable missing limbs, vitiligo, long-furred-ness, and 3 or more scars
        if not short:

            scar_details = {
                "NOTAIL": "no tail", 
                "HALFTAIL": "half a tail", 
                "NOPAW": "three legs", 
                "NOLEFTEAR": "a missing ear", 
                "NORIGHTEAR": "a missing ear",
                "NOEAR": "no ears"
            }

            additional_details = []
            if cat.pelt.vitiligo:
                additional_details.append("vitiligo")
            for scar in cat.pelt.scars:
                if scar in scar_details and scar_details[scar] not in additional_details:
                    additional_details.append(scar_details[scar])
            
            if len(additional_details) > 1:
                color_name = f"{color_name} with {', '.join(additional_details[:-1])} and {additional_details[-1]}"
            elif additional_details:
                color_name = f"{color_name} with {additional_details[0]}"
        
        
            if len(cat.pelt.scars) >= 3:
                color_name = f"scarred {color_name}"
            if cat.pelt.length == "long":
                color_name = f"long-furred {color_name}"

        return color_name
    
    def get_sprites_name(self):
        return Pelt.sprites_names[self.name]
