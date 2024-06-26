import os
import pygame

import ujson
from scripts.cat.names import names
from scripts.game_structure.game_essentials import game

class Sprites():
    cat_tints = {}
    white_patches_tints = {}

    def __init__(self, size=None):
        """Class that handles and hold all spritesheets. 
        Size is normall automatically determined by the size
        of the lineart. If a size is passed, it will override 
        this value. """
        self.size = None
        self.spritesheets = {}
        self.images = {}
        self.sprites = {}

        # Shared empty sprite for placeholders
        self.blank_sprite = None
        
        self.load_tints()

    def load_tints(self):
        try:
            with open("sprites/dicts/tint.json", 'r') as read_file:
                self.cat_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading Tints")

        try:
            with open("sprites/dicts/white_patches_tint.json", 'r') as read_file:
                self.white_patches_tints = ujson.loads(read_file.read())
        except:
            print("ERROR: Reading White Patches Tints")
            
    def spritesheet(self, a_file, name):
        """
        Add spritesheet called name from a_file.

        Parameters:
        a_file -- Path to the file to create a spritesheet from.
        name -- Name to call the new spritesheet.
        """
        self.spritesheets[name] = pygame.image.load(a_file).convert_alpha()

    def make_group(self,
                   spritesheet,
                   pos,
                   name,
                   sprites_x=6,
                   sprites_y=8,
                   no_index=False):  # pos = ex. (2, 3), no single pixels
        """
        Divide sprites on a spritesheet into groups of sprites that are easily accessible
        :param spritesheet: Name of spritesheet file
        :param pos: (x,y) tuple of offsets. NOT pixel offset, but offset of other sprites
        :param name: Name of group being made
        :param sprites_x: default 3, number of sprites horizontally
        :param sprites_y: default 3, number of sprites vertically
        :param no_index: default False, set True if sprite name does not require cat pose index
        """
        group_x_ofs = pos[0] * sprites_x * self.size
        group_y_ofs = pos[1] * sprites_y * self.size
        i = 0

        # splitting group into singular sprites and storing into self.sprites section
        for y in range(sprites_y):
            for x in range(sprites_x):
                if no_index:
                    full_name = f"{name}"
                else:
                    full_name = f"{name}{i}"
                try:
                    new_sprite = pygame.Surface.subsurface(
                        self.spritesheets[spritesheet],
                        group_x_ofs + x * self.size,
                        group_y_ofs + y * self.size,
                        self.size, self.size
                    )
                except ValueError:
                    # Fallback for non-existent sprites
                    if not self.blank_sprite:
                        self.blank_sprite = pygame.Surface(
                            (self.size, self.size),
                            pygame.HWSURFACE | pygame.SRCALPHA
                        )
                    new_sprite = self.blank_sprite
                while f'{name}{i}' in self.sprites:
                    i+=1
                self.sprites[full_name] = new_sprite
                i += 1

    def load_all(self):
        # get the width and height of the spritesheet
        lineart = pygame.image.load('sprites/lineart.png')
        width, height = lineart.get_size()
        del lineart # unneeded

        # if anyone changes lineart for whatever reason update this
        if isinstance(self.size, int):
            pass
        elif width / 6 == height / 8:
            self.size = width / 6
        else:
            self.size = 50 # default, what base clangen uses
            print(f"lineart.png is not 3x7, falling back to {self.size}")
            print(f"if you are a modder, please update scripts/cat/sprites.py and do a search for 'if width / 3 == height / 7:'")

        del width, height # unneeded

        for x in [
            'lineart', 'singlecolours', 'speckledcolours', 'tabbycolours', 'tortiesmoss',
            'whitepatches', 'whitepatches2', 'whitepatchesmoss', 'eyes', 'eyes2', 'skin', 'scars', 'missingscars',
            'collars', 'bellcollars', 'bowcollars', 'nyloncollars',
            'bengalcolours', 'marbledcolours', 'rosettecolours', 'smokecolours', 'tickedcolours', 
            'mackerelcolours', 'classiccolours', 'sokokecolours', 'agouticolours', 'singlestripecolours',
            'maskedcolours', 
            'shadersnewwhite', 'lineartdead', 'tortiepatchesmasks', 
            'medcatherbs', 'lineartdf', 'lightingnew', 'fademask',
            'fadestarclan', 'fadedarkforest', 'abyssiniancolours', 'braidedcolours', 'brindlecolours',
            'fadedcolours', 'sabercolours', 'splotchcolours', 'mossherbs', 'bloodcollars', 'fogcolours', 'mistcolours',
            'kittypetacc', 'smudgecolours', 'brokenmackerelcolours', 'longdancolours', 'brokenbraidedcolours',
            'charcoalbengalcolours', 'dustcolours',

            #OHDANS
            'flower_accessories', 'plant2_accessories', 'snake_accessories', 'smallAnimal_accessories', 'deadInsect_accessories',
            'aliveInsect_accessories', 'fruit_accessories', 'crafted_accessories', 'tail2_accessories',

            #WILDS
            'wildacc', 'wildaccextra', 'wildacc2', 'wildacc2extra',

            #SUPERARTSI
            'superartsi',

            #coffee
            'coffee',

            'eragona',

            "crowns",

            "wooddragon",

            "springwinter",

            "raincoat",

            "poptabs",

            "fazbear",

            "bears",

            "tide",

            "chimes",

            "moipa"

        ]:
            if 'lineart' in x and game.config['fun']['april_fools']:
                self.spritesheet(f"sprites/aprilfools{x}.png", x)
            else:
                self.spritesheet(f"sprites/{x}.png", x)

        # Line art
        self.make_group('lineart', (0, 0), 'lines')
        self.make_group('shadersnewwhite', (0, 0), 'shaders')
        self.make_group('lightingnew', (0, 0), 'lighting')

        self.make_group('lineartdead', (0, 0), 'lineartdead')
        self.make_group('lineartdf', (0, 0), 'lineartdf')

        # Fading Fog
        for i in range(0, 3):
            self.make_group('fademask', (i, 0), f'fademask{i}')
            self.make_group('fadestarclan', (i, 0), f'fadestarclan{i}')
            self.make_group('fadedarkforest', (i, 0), f'fadedf{i}')

        # Define eye colors
        eye_colors = [
            ['YELLOW', 'AMBER', 'HAZEL', 'PALE GREEN', 'GREEN', 'BLUE'],
            ['DARK BLUE', 'GREY', 'CYAN', 'EMERALD', 'HEATHER BLUE', 'SUN-LIT ICE'],
            ['COPPER', 'SAGE', 'BRIGHT BLUE', 'PALE BLUE', 'LAVENDER', 'DARK GREY'],
            ['PALE YELLOW', 'GOLD', 'LIME', 'HAZELNUT', 'DARK AMBER', 'SLATE'],
            ['RUBY', 'LILAC', 'LIGHT GREY', 'PINK', 'DARK HAZEL', 'CHOCOLATE']
        ]

        for row, colors in enumerate(eye_colors):
            for col, color in enumerate(colors):
                self.make_group('eyes', (col, row), f'eyes{color}')

        eye_patterns = [
            ['TRUE', 'CENTRAL', 'QUARTER', 'SLIVER', 'SPECKLES', 'FROSTED'],
            ['RING', 'HALFCENTRAL', 'HALFRING', 'BUBBLE', 'OUTRING', 'SWAP']
        ]

        for row, patterns in enumerate(eye_patterns):
            for col, pattern in enumerate(patterns):
                self.make_group('eyes', (col, row), f'eyes2{pattern}')

        # Define white patches
        white_patches = [
            ['FULLWHITE', 'ANY', 'TUXEDO', 'LITTLE', 'COLOURPOINT', 'VAN', 'ANYTWO', 'MOON', 'PHANTOM', 'POWDER',
             'BLEACHED', 'SAVANNAH', 'FADESPOTS', 'PEBBLESHINE'],
            ['EXTRA', 'ONEEAR', 'BROKEN', 'LIGHTTUXEDO', 'BUZZARDFANG', 'RAGDOLL', 'LIGHTSONG', 'VITILIGO', 'BLACKSTAR',
             'PIEBALD', 'CURVED', 'PETAL', 'SHIBAINU', 'OWL'],
            ['TIP', 'FANCY', 'FRECKLES', 'RINGTAIL', 'HALFFACE', 'PANTSTWO', 'GOATEE', 'VITILIGOTWO', 'PAWS', 'MITAINE',
             'BROKENBLAZE', 'SCOURGE', 'DIVA', 'BEARD'],
            ['TAIL', 'BLAZE', 'PRINCE', 'BIB', 'VEE', 'UNDERS', 'HONEY', 'FAROFA', 'DAMIEN', 'MISTER', 'BELLY',
             'TAILTIP', 'TOES', 'TOPCOVER'],
            ['APRON', 'CAPSADDLE', 'MASKMANTLE', 'SQUEAKS', 'STAR', 'TOESTAIL', 'RAVENPAW', 'PANTS', 'REVERSEPANTS',
             'SKUNK', 'KARPATI', 'HALFWHITE', 'APPALOOSA', 'DAPPLEPAW']
        ]

        white_patches2 = [
            ['HEART', 'LILTWO', 'GLASS', 'MOORISH', 'SEPIAPOINT', 'MINKPOINT', 'SEALPOINT', 'MAO', 'LUNA', 'CHESTSPECK',
             'WINGS', 'PAINTED', 'HEARTTWO', 'WOODPECKER'],
            ['BOOTS', 'MISS', 'COW', 'COWTWO', 'BUB', 'BOWTIE', 'MUSTACHE', 'REVERSEHEART', 'SPARROW', 'VEST',
             'LOVEBUG', 'TRIXIE', 'SAMMY', 'SPARKLE'],
            ['RIGHTEAR', 'LEFTEAR', 'ESTRELLA', 'SHOOTINGSTAR', 'EYESPOT', 'REVERSEEYE', 'FADEBELLY', 'FRONT',
             'BLOSSOMSTEP', 'PEBBLE', 'TAILTWO', 'BUDDY', 'BACKSPOT', 'EYEBAGS'],
            ['BULLSEYE', 'FINN', 'DIGIT', 'KROPKA', 'FCTWO', 'FCONE', 'MIA', 'SCAR', 'BUSTER', 'SMOKEY', 'HAWKBLAZE',
             'CAKE', 'ROSINA', 'PRINCESS'],
            ['LOCKET', 'BLAZEMASK', 'TEARS', 'DOUGIE']
        ]

        white_patches_moss = [
            ['CHANCE', 'MOSSY', 'MOTH', 'NIGHTMIST', 'FALCON', 'VENUS', 'RETSUKO', 'TIDAL', 'DIAMOND', 'ECLIPSE', 'SNOWSTORM', 'PEPPER', 'COWTHREE', 'COWFOUR'],
            ['COWFIVE', 'COWSIX', 'COWSEVEN', 'COWEIGHT', 'COWNINE', 'COWTEN', 'COWELEVEN', 'FRECKLEMASK', 'SPLAT', 'BATWING', 'SMALLPATCHES']
        ]

        for row, patches in enumerate(white_patches):
            for col, patch in enumerate(patches):
                self.make_group('whitepatches', (col, row), f'white{patch}')
        for row, patches in enumerate(white_patches2):
            for col, patch in enumerate(patches):
                self.make_group('whitepatches2', (col, row), f'white{patch}')
        for row, patches in enumerate(white_patches_moss):
            for col, patch in enumerate(patches):
                self.make_group('whitepatchesmoss', (col, row), f'white{patch}')

        # Define colors and categories
        color_categories = [
            ['WHITE', 'SNOW WHITE', 'GRAY', 'SLATE', 'DARK GRAY', 'DARK SLATE', 'PALE BLUE', 'BLUE', 'PALE LILAC',
             'LILAC', 'SILVER', 'BLACK', 'SOOT BLACK', 'OBSIDIAN', 'GHOST'],

            ['PALE BROWN', 'ALMOND', 'ACORN', 'LIGHT BROWN', 'BROWN', 'DARK BROWN', 'PALE CINNAMON', 'CINNAMON',
                'SABLE', 'DARK SABLE', 'BIRCH', 'PALE LAVENDER', 'LAVENDER', 'DARK LAVENDER', 'DARK ORANGE'],

            ['PALE FIRE', 'FIRE', 'DARK FIRE', 'PALE GINGER', 'GINGER', 'DARK GINGER', 'PALE GOLD', 'YELLOW',
             'GOLD', 'BRONZE', 'ROSE', 'LIGHT CREAM', 'CREAM', 'DARK CREAM', 'DARK GOLD']
        ]

        color_types = [
            'singlecolours', 'tabbycolours', 'marbledcolours', 'rosettecolours',
            'smokecolours', 'tickedcolours', 'speckledcolours', 'bengalcolours',
            'mackerelcolours', 'classiccolours', 'sokokecolours', 'agouticolours',
            'singlestripecolours', 'maskedcolours',

            'abyssiniancolours', 'braidedcolours', 'brindlecolours', 'fadedcolours',
            'sabercolours', 'splotchcolours', 'fogcolours', 'mistcolours', 'smudgecolours',
            'brokenmackerelcolours', 'longdancolours', 'brokenbraidedcolours', 'charcoalbengalcolours', 'dustcolours'
        ]

        for row, colors in enumerate(color_categories):
            for col, color in enumerate(colors):
                for color_type in color_types:
                    self.make_group(color_type, (col, row), f'{color_type[:-7]}{color}')

        # tortiepatchesmasks
        tortiepatchesmasks = [
            ['ONE', 'TWO', 'THREE', 'FOUR', 'REDTAIL', 'DELILAH', 'HALF', 'STREAK', 'MASK', 'SMOKE'],
            ['MINIMALONE', 'MINIMALTWO', 'MINIMALTHREE', 'MINIMALFOUR', 'OREO', 'SWOOP', 'CHIMERA', 'CHEST', 'ARMTAIL',
             'GRUMPYFACE'],
            ['MOTTLED', 'SIDEMASK', 'EYEDOT', 'BANDANA', 'PACMAN', 'STREAMSTRIKE', 'SMUDGED', 'DAUB', 'EMBER', 'BRIE'],
            ['ORIOLE', 'ROBIN', 'BRINDLE', 'PAIGE', 'ROSETAIL', 'SAFI', 'DAPPLENIGHT', 'BLANKET', 'BELOVED', 'BODY'],
            ['SHILOH', 'FRECKLED', 'HEARTBEAT']
        ]

        tortiepatchesmasksmoss = [
            ['VIPER', 'SKULL', 'POINTS', 'DITTO', 'TABBY', 'SPECKLED', 'BENGAL', 'CLASSIC', 'MACKEREL', 'MARBLED'],
            ['SABER', 'ROSETTE', 'MASKED', 'DUST', 'MAXIMUMONE', 'MAXIMUMTWO', 'MAXIMUMTHREE', 'MAXIMUMFOUR', 'MAXIMUMFIVE', 'MAXIMUMSIX'],
            ['MAXIMUMSEVEN', 'MAXIMUMEIGHT']
        ]

        for row, masks in enumerate(tortiepatchesmasks):
            for col, mask in enumerate(masks):
                self.make_group('tortiepatchesmasks', (col, row), f"tortiemask{mask}")

        for row, masks in enumerate(tortiepatchesmasksmoss):
            for col, mask in enumerate(masks):
                self.make_group('tortiesmoss', (col, row), f"tortiemask{mask}")

        # Define skin colors 
        skin_colors = [
            ['BLACK', 'RED', 'PINK', 'DARKBROWN', 'BROWN', 'LIGHTBROWN'],
            ['DARK', 'DARKGREY', 'GREY', 'DARKSALMON', 'SALMON', 'PEACH'],
            ['DARKMARBLED', 'MARBLED', 'LIGHTMARBLED', 'DARKBLUE', 'BLUE', 'LIGHTBLUE']
        ]

        for row, colors in enumerate(skin_colors):
            for col, color in enumerate(colors):
                self.make_group('skin', (col, row), f"skin{color}")

        self.load_scars()

    def load_scars(self):
        """
        Loads scar sprites and puts them into groups.
        """
        # Define scars
        scars_data = [
            ["ONE", "TWO", "THREE", "MANLEG", "BRIGHTHEART", "MANTAIL", "BRIDGE", "RIGHTBLIND", "LEFTBLIND",
             "BOTHBLIND", "BURNPAWS", "BURNTAIL"],
            ["BURNBELLY", "BEAKCHEEK", "BEAKLOWER", "BURNRUMP", "CATBITE", "RATBITE", "FROSTFACE", "FROSTTAIL",
             "FROSTMITT", "FROSTSOCK", "QUILLCHUNK", "QUILLSCRATCH"],
            ["TAILSCAR", "SNOUT", "CHEEK", "SIDE", "THROAT", "TAILBASE", "BELLY", "TOETRAP", "SNAKE", "LEGBITE",
             "NECKBITE", "FACE"],
            ["HINDLEG", "BACK", "QUILLSIDE", "SCRATCHSIDE", "TOE", "BEAKSIDE", "CATBITETWO", "SNAKETWO", "FOUR"]
        ]

        # define missing parts
        missing_parts_data = [
            ["LEFTEAR", "RIGHTEAR", "NOTAIL", "NOLEFTEAR", "NORIGHTEAR", "NOEAR", "HALFTAIL", "NOPAW"]
        ]

        # scars 
        for row, scars in enumerate(scars_data):
            for col, scar in enumerate(scars):
                self.make_group('scars', (col, row), f'scars{scar}')
        # missing parts
        for row, missing_parts in enumerate(missing_parts_data):
            for col, missing_part in enumerate(missing_parts):
                self.make_group('missingscars', (col, row), f'scars{missing_part}')

        # accessories
        medcatherbs_data = [
            ["MAPLE LEAF", "HOLLY", "BLUE BERRIES", "FORGET ME NOTS", "RYE STALK", "LAUREL"],
            ["BLUEBELLS", "NETTLE", "POPPY", "LAVENDER", "HERBS", "PETALS"],
            [],  # Empty row because this is the wild data, except dry herbs.
            ["OAK LEAVES", "CATMINT", "MAPLE SEED", "JUNIPER"]
        ]

        wild_data = [
            ["RED FEATHERS", "BLUE FEATHERS", "JAY FEATHERS", "MOTH WINGS", "CICADA WINGS"]
        ]

        collars_data = [
            ["CRIMSON", "BLUE", "YELLOW", "CYAN", "RED", "LIME"],
            ["GREEN", "RAINBOW", "BLACK", "SPIKES", "WHITE"],
            ["PINK", "PURPLE", "MULTI", "INDIGO"]
        ]

        bellcollars_data = [
            ["CRIMSONBELL", "BLUEBELL", "YELLOWBELL", "CYANBELL", "REDBELL", "LIMEBELL"],
            ["GREENBELL", "RAINBOWBELL", "BLACKBELL", "SPIKESBELL", "WHITEBELL"],
            ["PINKBELL", "PURPLEBELL", "MULTIBELL", "INDIGOBELL"]
        ]

        bowcollars_data = [
            ["CRIMSONBOW", "BLUEBOW", "YELLOWBOW", "CYANBOW", "REDBOW", "LIMEBOW"],
            ["GREENBOW", "RAINBOWBOW", "BLACKBOW", "SPIKESBOW", "WHITEBOW"],
            ["PINKBOW", "PURPLEBOW", "MULTIBOW", "INDIGOBOW"]
        ]

        nyloncollars_data = [
            ["CRIMSONNYLON", "BLUENYLON", "YELLOWNYLON", "CYANNYLON", "REDNYLON", "LIMENYLON"],
            ["GREENNYLON", "RAINBOWNYLON", "BLACKNYLON", "SPIKESNYLON", "WHITENYLON"],
            ["PINKNYLON", "PURPLENYLON", "MULTINYLON", "INDIGONYLON"]
        ]

        mossherb_data = [
            ["LUNA MOTH", "ATLAS MOTH", "BIRD SKULL", "IVY", "DAISY", "BUTTERFLIES"],
            ["CLOVER", "ANTLERS", "STICK", "FIREFLIES", "WREATH", "FLOWER WREATH"],
            ["SPROUT", "MUSHROOM", "LILAC", "SEAWEED", "LILY PAD", "MONSTERA"],
            ["WILD FLOWERS", "TWIGS", "SHELL", "CRYSTAL", "SERPENT", "MOSS BALL"]
        ]

        kittypetacc_data = [
            ["SUNGLASSES", "BLUE BANDANA", "YELLOW BANDANA", "GREEN BANDANA", "RED BANDANA", "ORANGE BANDANA"],
            ["PURPLE BANDANA", "WHITE BANDANA", "BLACK BANDANA", "PINK BANDANA", "RED HARNESS", "ORANGE HARNESS"],
            ["YELLOW HARNESS", "GREEN HARNESS", "BLUE HARNESS", "PURPLE HARNESS", "WHITE HARNESS", "BLACK HARNESS"],
            ["PINK HARNESS", "COWBOY HAT"]
        ]

        bloodcollars_data = [
            ["CRIMSONFANG", "BLUEFANG", "YELLOWFANG", "CYANFANG", "REDFANG", "LIMEFANG"],
            ["GREENFANG", "RAINBOWFANG", "BLACKFANG", "SPIKESFANG", "WHITEFANG"],
            ["PINKFANG", "PURPLEFANG", "MULTIFANG", "INDIGOFANG"]
        ]

        # medcatherbs
        for row, herbs in enumerate(medcatherbs_data):
            for col, herb in enumerate(herbs):
                self.make_group('medcatherbs', (col, row), f'acc_herbs{herb}')
        self.make_group('medcatherbs', (5, 2), 'acc_herbsDRY HERBS')

        # wild
        for row, wilds in enumerate(wild_data):
            for col, wild in enumerate(wilds):
                self.make_group('medcatherbs', (col, 2), f'acc_wild{wild}')

        # collars
        for row, collars in enumerate(collars_data):
            for col, collar in enumerate(collars):
                self.make_group('collars', (col, row), f'collars{collar}')

        # bellcollars
        for row, bellcollars in enumerate(bellcollars_data):
            for col, bellcollar in enumerate(bellcollars):
                self.make_group('bellcollars', (col, row), f'collars{bellcollar}')

        # bowcollars
        for row, bowcollars in enumerate(bowcollars_data):
            for col, bowcollar in enumerate(bowcollars):
                self.make_group('bowcollars', (col, row), f'collars{bowcollar}')

        # nyloncollars
        for row, nyloncollars in enumerate(nyloncollars_data):
            for col, nyloncollar in enumerate(nyloncollars):
                self.make_group('nyloncollars', (col, row), f'collars{nyloncollar}')

        # mossherbs
        for row, mossherbs in enumerate(mossherb_data):
            for col, mossherb in enumerate(mossherbs):
                self.make_group('mossherbs', (col, row), f'acc_moss{mossherb}')

        # kittypetacc
        for row, kittypetaccs in enumerate(kittypetacc_data):
            for col, kittypetacc in enumerate(kittypetaccs):
                self.make_group('kittypetacc', (col, row), f'acc_kitty{kittypetacc}')

        # bloodcollars
        for row, bloodcollars in enumerate(bloodcollars_data):
            for col, bloodcollar in enumerate(bloodcollars):
                self.make_group('bloodcollars', (col, row), f'dogcollars{bloodcollar}')


            # ohdan's accessories
        for a, i in enumerate([
            "DAISY", "DIANTHUS", "BLEEDING HEARTS", "FRANGIPANI", "BLUE GLORY", "CATNIP FLOWER", "BLANKET FLOWER", "ALLIUM", "LACELEAF", "PURPLE GLORY"]):
            self.make_group('flower_accessories', (a, 0), f'acc_flower{i}')
        for a, i in enumerate([
            "YELLOW PRIMROSE", "HESPERIS", "MARIGOLD", "WISTERIA"]):
            self.make_group('flower_accessories', (a, 1), f'acc_flower{i}')
        
        for a, i in enumerate([
            "CLOVER", "STICK", "PUMPKIN", "MOSS", "IVY", "ACORN", "MOSS PELT", "REEDS", "BAMBOO"]):
            self.make_group('plant2_accessories', (a, 0), f'acc_plant2{i}')

        for a, i in enumerate([
            "GRASS SNAKE", "BLUE RACER", "WESTERN COACHWHIP", "KINGSNAKE"]):
            self.make_group('snake_accessories', (a, 0), f'acc_snake{i}')
            
        for a, i in enumerate([
            "GRAY SQUIRREL", "RED SQUIRREL", "CRAB", "WHITE RABBIT", "BLACK RABBIT", "BROWN RABBIT", "INDIAN GIANT SQUIRREL", "FAWN RABBIT", "BROWN AND WHITE RABBIT", "BLACK AND WHITE RABBIT"]):
            self.make_group('smallAnimal_accessories', (a, 0), f'acc_smallAnimal{i}')
        for a, i in enumerate([
            "WHITE AND FAWN RABBIT", "BLACK VITILIGO RABBIT", "BROWN VITILIGO RABBIT", "FAWN VITILIGO RABBIT", "BLACKBIRD", "ROBIN", "JAY", "THRUSH", "CARDINAL", "MAGPIE"]):
            self.make_group('smallAnimal_accessories', (a, 1), f'acc_smallAnimal{i}')
        for a, i in enumerate([
            "CUBAN TROGON", "TAN RABBIT", "TAN AND WHITE RABBIT", "TAN VITILIGO RABBIT", "RAT", "WHITE MOUSE", "BLACK MOUSE", "GRAY MOUSE", "BROWN MOUSE", "GRAY RABBIT"]):
            self.make_group('smallAnimal_accessories', (a, 2), f'acc_smallAnimal{i}')
        for a, i in enumerate([
            "GRAY AND WHITE RABBIT", "GRAY VITILIGO RABBIT"]):
            self.make_group('smallAnimal_accessories', (a, 3), f'acc_smallAnimal{i}')
            
        for a, i in enumerate([
            "LUNAR MOTH", "ROSY MAPLE MOTH", "MONARCH BUTTERFLY", "DAPPLED MONARCH", "POLYPHEMUS MOTH", "MINT MOTH"]):
            self.make_group('deadInsect_accessories', (a, 0), f'acc_deadInsect{i}')
            
        for a, i in enumerate([
            "BROWN SNAIL", "RED SNAIL", "WORM", "BLUE SNAIL", "ZEBRA ISOPOD", "DUCKY ISOPOD", "DAIRY COW ISOPOD", "BEETLEJUICE ISOPOD", "BEE", "RED LADYBUG"]):
            self.make_group('aliveInsect_accessories', (a, 0), f'acc_aliveInsect{i}')
        for a, i in enumerate([
            "ORANGE LADYBUG", "YELLOW LADYBUG"]):
            self.make_group('aliveInsect_accessories', (a, 1), f'acc_aliveInsect{i}')
        
        for a, i in enumerate([
            "RASPBERRY", "BLACKBERRY", "GOLDEN RASPBERRY", "CHERRY", "YEW"]):
            self.make_group('fruit_accessories', (a, 0), f'acc_fruit{i}')
        
        for a, i in enumerate([
            "WILLOWBARK BAG", "CLAY DAISY POT", "CLAY AMANITA POT", "CLAY BROWNCAP POT", "BIRD SKULL", "LEAF BOW"]):
            self.make_group('crafted_accessories', (a, 0), f'acc_crafted{i}')
        
        for a, i in enumerate([
            "SEAWEED", "DAISY CORSAGE"]):
            self.make_group('tail2_accessories', (a, 0), f'acc_tail2{i}')

       # wild's accessories
        for a, i in enumerate([
            "LILYPAD", "LARGE DEATHBERRY", "SMALL DEATHBERRY", "ACORN2", "PINECONE", "VINE"]):
            sprites.make_group('wildacc', (a, 0), f'acc_herbs{i}',sprites_x=3,sprites_y=3)
            sprites.make_group('wildaccextra', (a, 0),
                               f'acc_herbs{i}',sprites_x=3,sprites_y=2)
        for a, i in enumerate(
                ["CHERRY2", "BLEEDING HEARTS", "SHELL PACK", "FERNS", "GOLD FERNS"]):
            sprites.make_group('wildacc', (a, 1), f'acc_herbs{i}',sprites_x=3,sprites_y=3)
            sprites.make_group('wildaccextra', (a, 1),
                               f'acc_herbs{i}',sprites_x=3,sprites_y=2)
        for a, i in enumerate(["WHEAT", "BLACK WHEAT"]):
            sprites.make_group('wildacc', (a, 2), f'acc_herbs{i}',sprites_x=3,sprites_y=3)
            sprites.make_group('wildaccextra', (a, 2),
                               f'acc_herbs{i}',sprites_x=3,sprites_y=2)    

        for a, i in enumerate([
            "BERRIES", "CLOVERS", "CLOVER", "MOSS", "FLOWER MOSS", "MUSHROOMS"]):
            sprites.make_group('wildacc2', (a, 0), f'acc_herbs{i}',sprites_x=3,sprites_y=3)
            sprites.make_group('wildacc2extra', (a, 0),
                               f'acc_herbs{i}',sprites_x=3,sprites_y=2)
        for a, i in enumerate(
                ["LARGE LUNA", "LARGE COMET", "SMALL LUNA", "SMALL COMET", "LADYBUG"]):
            sprites.make_group('wildacc2', (a, 1), f'acc_wild{i}', sprites_x=3,sprites_y=3)
            sprites.make_group('wildacc2extra', (a, 1),
                               f'acc_wild{i}',sprites_x=3,sprites_y=2)
        for a, i in enumerate(["MUD PAWS", "ASHY PAWS"]):
            sprites.make_group('wildacc2', (a, 2), f'acc_wild{i}',sprites_x=3,sprites_y=3)
            sprites.make_group('wildacc2extra', (a, 2),
                               f'acc_wild{i}',sprites_x=3,sprites_y=2)
        
        # superartsi's accessories

        for a, i in enumerate([
            "ORANGEBUTTERFLY", "BLUEBUTTERFLY", "BROWNPELT", "GRAYPELT", "BROWNMOSSPELT", "GRAYMOSSPELT"]):
            self.make_group('superartsi', (a, 0), f'acc_wild{i}')
        for a, i in enumerate([
            "FERN", "MOREFERN", "BLEEDINGHEART", "LILY"]):
            self.make_group('superartsi', (a, 1), f'acc_wild{i}')

        # coffee's accessories
        for a, i in enumerate([
            "PINKFLOWERCROWN", "YELLOWFLOWERCROWN", "BLUEFLOWERCROWN", "PURPLEFLOWERCROWN"]):
            self.make_group('coffee', (a, 0), f'acc_flower{i}')

        # eragona rose's accessories

        for a, i in enumerate([
            "REDHARNESS", "NAVYHARNESS", "YELLOWHARNESS", "TEALHARNESS", "ORANGEHARNESS", "GREENHARNESS"]):
            self.make_group('eragona', (a, 0), f'collars{i}')
        for a, i in enumerate([
            "MOSSHARNESS", "RAINBOWHARNESS", "BLACKHARNESS", "BEEHARNESS", "CREAMHARNESS"]):
            self.make_group('eragona', (a, 1), f'collars{i}')
        for a, i in enumerate([
            "PINKHARNESS", "MAGENTAHARNESS", "PEACHHARNESS", "VIOLETHARNESS"]):
            self.make_group('eragona', (a, 2), f'collars{i}')

        for a, i in enumerate([
            "YELLOWCROWN", "REDCROWN", "LILYPADCROWN"]):
            self.make_group('crowns', (a, 0), f'acc_wild{i}')

        for a, i in enumerate([
            "WOODDRAGON"]):
            self.make_group('wooddragon', (a, 0), f'acc_wild{i}')


        for a, i in enumerate(["CHERRYBLOSSOM","TULIPPETALS","CLOVERFLOWER","PANSIES","BELLFLOWERS","SANVITALIAFLOWERS","EGGSHELLS","BLUEEGGSHELLS","EASTEREGG","FORSYTHIA"]):
            self.make_group('springwinter', (a, 0), f'acc_wild{i}')
        for a, i in enumerate([
            "MINTLEAF","STICKS","SPRINGFEATHERS","SNAILSHELL","MUD","CHERRYPLUMLEAVES","CATKIN","HONEYCOMB","FLOWERCROWN","LILIESOFTHEVALLEY"]):
            self.make_group('springwinter', (a, 1), f'acc_wild{i}')
        for a, i in enumerate([
            "STRAWMANE","MISTLETOE","REDPOINSETTIA","WHITEPOINSETTIA","COTONEASTERWREATH","YEWS","HEATHER","TEETHCOLLAR","DRIEDORANGE","ROESKULL"]):
            self.make_group('springwinter', (a, 2), f'acc_wild{i}')
        for a, i in enumerate([
            "WOODENOAKANTLERS","WOODENBIRCHANTLERS","DOGWOOD","GRAYWOOL","BLACKWOOL","CREAMWOOL","WHITEWOOL","FIRBRANCHES","CORALBELLS","SLIVERDUSTPLANT"]):
            self.make_group('springwinter', (a, 3), f'acc_wild{i}')

        for a, i in enumerate([
            "RAINCOAT"]):
            self.make_group('raincoat', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "POPTABS"]):
            self.make_group('poptabs', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "FAZBEAR"]):
            self.make_group('fazbear', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "WHITEBEAR", "PANDA", "BEAR", "BROWNBEAR"]):
            self.make_group('bears', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "TIDE"]):
            self.make_group('tide', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "CELESTIALCHIMES", "STARCHIMES", "LUNARCHIMES", "SILVERLUNARCHIMES"]):
            self.make_group('chimes', (a, 0), f'acc_crafted{i}')

        for a, i in enumerate([
            "FIDDLEHEADS", "LANTERNS", "HEARTCHARMS", "CHIMES"]):
            self.make_group('moipa', (a, 0), f'acc_crafted{i}')
        
# CREATE INSTANCE
sprites = Sprites()