# File for all Quakecraft related constants

# List of active stats and name conversions
quake_active_stats = {"barrel": "barrel", "case": "case", "killsound": "killsound", "sight": "laser",
    "muzzle": "muzzle", "beam": "beam", "selectedKillPrefix": "prefix_color", "trigger": "trigger"
    }

# List of gamemodes
quake_gamemodes = {"_teams": "teams", "_solo_tourney": "tournament", "": "solo"}

# General stats with name conversions
quake_stat_names = (
    "coins", "highest_killstreak", "dash_cooldown", "dash_power", "weekly_kills_a", "weekly_kills_b", "monthly_kills_a", "monthly_kills_b"
    )

# General stats without name conversions
quake_mode_stats = ("kills", "deaths", "killstreaks", "wins", "headshots", "distance_travelled", "shots_fired")

# List of cosmetic armor pieces
quake_hats = (
    ("exodiahat", 200000, "None"), ("discohat", 75000, "None"), ("radianthat", 50000, "None"), ("bouncyhat", 25000, "None"),
    ("crafterhat", 15000, "None"), ("explosivehat", 5000, "None"), ("librarianhat", 2500, "None"), ("hypixelhat", 2000, "None"),
    ("bobhat", 1500, "None"), ("ecologyhat", 1000, "None"), ("lighthat", 1000, "None"), ("engineeringhat", 1000, "None"),
    ("richyrichhat", 1000, "None"), ("jeeperscreepershat", 900, "None"), ("walkingdeadhat", 900, "None"), ("controlfreakhat", 850, "None"),
    ("cavemanhat", 850, "None"), ("hipsterhat", 850, "None"), ("majestichat", 700, "None"), ("tnt", 700, "None"), ("dispenser", 700, "None"),
    ("diamond", 700, "None"), ("redstone", 700, "None"), ("lantern", 700, "None"), ("spaceman", 700, "None"), ("melon", 350, "None"),
    ("cactus", 350, "None"), ("showoff", 0, "None")
    )
quake_chestplates = (
    ("exodiakit", 200000, "None"), ("discokit", 75000, "None"), ("swegkit", 4500, "None"), ("budderkit", 3375, "None"), ("medievalkit", 2750, "None"),
    ("fashionistakit", 2250, "None"), ("snowkit", 2250, "None"), ("slimekit", 2250, "None"), ("spacekit", 2250, "None"), ("revengekit", 2250, "None"),
    ("invaderkit", 2250, "None"), ("specopskit", 2250, "None"), ("swatkit", 2250, "None"), ("marinekit", 2250, "None"), ("commander", 2250, "None"),
    ("majestic", 2250, "None"), ("elite", 2250, "None"), ("soldier", 650, "None")
    )
quake_lowers = (
    ("exodia", 200000, "None"), ("disco", 75000, "None"), ("swegkit", 4500, "None"), ("budderkit", 3375, "None"), ("medievalkit", 2750, "None"),
    ("fashionistakit", 2250, "None"), ("snowkit", 2250, "None"), ("slimekit", 2250, "None"), ("spacekit", 2250, "None"), ("revengekit", 2250, "None"),
    ("invaderkit", 2250, "None"), ("specopskit", 2250, "None"), ("swatkit", 2250, "None"), ("marinekit", 2250, "None"), ("commander", 2250, "None"),
    ("majestic", 2250, "None"), ("elite", 2250, "None"), ("soldier", 650, "None")
    )

# List of premade weapons and their parts
quake_weapons = {
    "basic_railgun": ("WOOD_HOE", "YELLOW", "SMALL_BALL", "NONE", "ONE_POINT_FIVE"),
    "superior_railgun": ("IRON_HOE", "RED", "BURST", "NONE", "ONE_POINT_FOUR"),
    "hyper_beam_railgun": ("GOLD_HOE", "YELLOW", "STAR", "NONE", "ONE_POINT_THREE"),
    "creeper_railgun": ("DIAMOND_HOE", "GREEN", "CREEPER", "NONE", "ONE_POINT_TWO"),
    "bfg": ("SHINY_STONE_HOE", "BLUE", "LARGE_BALL", "NONE", "ONE_POINT_ONE"),
    "budder_slapper": ("SHINY_GOLD_HOE", "YELLOW", "SMALL_BALL", "GOLD", "ONE_POINT_FIVE"),
    "redstoner": ("SHINY_WOOD_HOE", "RED", "BURST", "REDSTONE", "ONE_POINT_TWO"),
    "bling_bling_thing": ("SHINY_DIAMOND_HOE", "PURPLE", "LARGE_BALL", "DIAMOND", "ONE_POINT_ZERO"),
    "the_turtle": ("IRON_HOE", "GREEN", "LARGE_BALL", "IRON", "TWO_POINT_FIVE"),
    "lovegun": ("SHINY_GOLD_HOE", "RED", "STAR", "REDSTONE", "NINE_POINT_THREE"),
    "the_harvester": ("STONE_HOE", "GREEN", "SMALL_BALL", "MELON", "ONE_POINT_FIVE"),
    "blue_lagoon": ("DIAMOND_HOE", "BLUE", "BURST", "PRISMARINE", "ONE_POINT_ONE"),
    "cookie_cannon": ("GOLD_HOE", "EMERALD", "BURST", "COMMAND_BLOCK", "ONE_POINT_ONE"),
    "the_worm": ("STONE_HOE", "GREEN", "SMALL_BALL", "NONE", "FIVE_POINT_ZERO"),
    "the_snail": ("STONE_HOE", "RED", "CREEPER", "WOOD", "NINE_POINT_ZERO"),
    "le_bizarre": ("SHINY_DIAMOND_HOE", "ORANGE", "SMALL_BALL", "LAPIS", "ONE_POINT_FOUR"),
    "fabled_railgun": ("SHINY_DIAMOND_HOE", "DIAMOND", "STAR", "PRISMARINE", "ONE_POINT_TWO"),
    "apple_corer": ("SHINY_IRON_HOE", "GOLD", "STAR", "OBSIDIAN", "ZERO_POINT_NINE"),
    "railgun_of_darkness": ("SHINY_GOLD_HOE", "BLACK", "LARGE_BALL", "OBSIDIAN", "ZERO_POINT_NINE"),
    "platinum_smelter": ("SHINY_IRON_HOE", "SILVER", "BURST", "IRON", "ZERO_POINT_EIGHT_FIVE"),
    "the_reaper": ("SHINY_DIAMOND_HOE", "BLACK", "LARGE_BALL", "SOUL_SAND", "ZERO_POINT_EIGHT_FIVE")
    }

# List of casing prefixes
quake_case_prefixes = {
    "WOOD_HOE": "Slightly",
    "STONE_HOE": "Mostly",
    "SHINY_WOOD_HOE": "Spectacularly",
    "SHINY_STONE_HOE": "Brilliant",
    "IRON_HOE": "Excellently",
    "GOLD_HOE": "Awesomely",
    "DIAMOND_HOE": "Undeniably",
    "SHINY_GOLD_HOE": "Luxury",
    "SHINY_DIAMOND_HOE": "Lucky",
    "SHINY_IRON_HOE": "Executive"
    }

# List of laser prefixes
quake_laser_prefixes = {
    "YELLOW": "Shining",
    "GREEN": "Glowing",
    "WHITE": "Lofty",
    "RED": "Radiant",
    "BLUE": "Resplendant",
    "PURPLE": "Majestic",
    "PINK": "Stunning",
    "GOLD": "Grandiose",
    "EMERALD": "Dignified",
    "DIAMOND": "Royal",
    "GRAY": "Pearly",
    "ORANGE": "Not-a-fruit",
    "SILVER": "Lustrous",
    "BLACK": "Absorbing"
    }

# List of muzzle suffixes
quake_muzzle_suffixes = {
    "NONE": "AK",
    "CLAY": "CL",
    "WOOD": "WO",
    "GOLD": "GD",
    "REDSTONE": "RED",
    "IRON": "IN",
    "ENDER_STONE": "EST",
    "DIAMOND": "DMD",
    "QUARTZ": "QA",
    "EMERALD": "EM",
    "LAPIS": "LA",
    "OBSIDIAN": "BBY",
    "SPONGE": "HYPE",
    "SEA_LANTERN": "SL",
    "COMMAND_BLOCK": "CMD",
    "PRISMARINE": "PRM",
    "MELON": "MEL",
    "PUMPKIN": "PMK",
    "SOUL_SAND": "SMS"
    }

# List of trigger suffixes
quake_trigger_suffixes = {
    "ONE_POINT_FIVE": "1.0",
    "NINE_POINT_ZERO": "WTF",
    "FIVE_POINT_ZERO": "5.0",
    "TWO_POINT_FIVE": "2.5",
    "ONE_POINT_FOUR": "2.0",
    "ONE_POINT_THREE": "3.0",
    "ONE_POINT_TWO": "1337",
    "ONE_POINT_ONE": "2013",
    "ONE_POINT_ZERO": "99",
    "ZERO_POINT_NINE": "-1",
    "ZERO_POINT_EIGHT_FIVE": "404"
    }

# List of barrel suffixes
quake_barrel_suffixes = {
    "SMALL_BALL": "(S)",
    "LARGE_BALL": "(L)",
    "CREEPER": "(C)",
    "BURST": "(B)",
    "STAR": "(*)"
    }
