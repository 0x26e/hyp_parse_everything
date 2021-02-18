from .constants import *

# Returns formatted Quake stats
# ! # Add shop stats
def getQuakecraft(raw_stats, achievements):

    # Setup container to hold stats
    sorted_stats = {}

    # Set general stats
    sorted_stats["general"] = {
        q_stat: int(raw_stats.get(q_stat, 0))
        for q_stat in quake_stat_names
        }

    # Set gamemode stats
    for gm, gm_proper in quake_gamemodes.items():
        sorted_stats[gm_proper] = {
            q_stat: raw_stats.get(f"{q_stat}{gm}", 0)
            for q_stat in quake_mode_stats
            }

    # Set active stats
    sorted_stats["active"] = {
        q_stat_proper: raw_stats.get(q_stat, 0)
        for q_stat, q_stat_proper in quake_active_stats.items()
        }

    # Set general stats
    sorted_stats["general"].update({
        q_stat: sum( [ sorted_stats["solo"].get(q_stat, 0), sorted_stats["teams"].get(q_stat, 0), sorted_stats["tournament"].get(q_stat, 0) ] )
        for q_stat in quake_mode_stats
        })

    # Fix post_update stats
    sorted_stats["solo"]["post_update_kills"] = raw_stats.get("kills_since_update_feb_2017", 0)
    sorted_stats["teams"]["post_update_kills"] = raw_stats.get("kills_since_update_feb_2017_teams", 0)

    # Fix dash cooldown and power
    sorted_stats["general"]["dash_cooldown"] += 1
    sorted_stats["general"]["dash_power"] += 1

    # Add stats from tiered achievements
    sorted_stats["general"]["godlikes"] = achievements.get("quake_godlikes", 0)
    sorted_stats["general"]["weapons"] = achievements.get("quake_weapon_arsenal", 0)

    # Resolve for best hat
    best_quake_hat = raw_stats.get("hat", False)
    if(not best_quake_hat):
        for q_hat in quake_hats:
            if(q_hat[0] in raw_stats["packages"]):
                best_quake_hat = q_hat[0]
                break

    if(not best_quake_hat):
        best_quake_hat = "NONE"

    # Resolve for best chestplate
    best_quake_chestplate = raw_stats.get("armor", False)
    if(not best_quake_chestplate):
        for q_chest in quake_chestplates:
            if(q_chest[0] in raw_stats["packages"]):
                best_quake_chestplate = q_chest[0]
                break

    if(not best_quake_chestplate):
        best_quake_chestplate = "NONE"

    # Resolve for best leggings
    best_quake_leggings = raw_stats.get("leggings", False)
    if(not best_quake_leggings):
        for q_lower in quake_lowers:
            if(f"{q_lower[0]}_leggings" in raw_stats["packages"]):
                best_quake_leggings = f"{q_lower[0]}_leggings"
                break

    if(not best_quake_leggings):
        best_quake_leggings = "NONE"

    # Resolve for best boots
    best_quake_boots = raw_stats.get("boots", False)
    if(not best_quake_boots):
        for q_lower in quake_lowers:
            if(f"{q_lower[0]}_boots" in raw_stats["packages"]):
                best_quake_boots = f"{q_lower[0]}_boots"
                break

    if(not best_quake_boots):
        best_quake_boots = "NONE"

    # Get best armor set
    sorted_stats["active"]["armor"] = {
        "hat": best_quake_hat,
        "chestplate": best_quake_chestplate,
        "leggings": best_quake_leggings,
        "boots": best_quake_boots,
        }

    # Setup for weapon
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

    # Setup case prefixes
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

    # Setup laser prefixes
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

    # Setup muzzle suffixes
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

    # Setup trigger suffixes
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

    # Setup barrel suffixes
    quake_barrel_suffixes = {
        "SMALL_BALL": "(S)",
        "LARGE_BALL": "(L)",
        "CREEPER": "(C)",
        "BURST": "(B)",
        "STAR": "(*)"
        }

    # Current weapon build
    quake_current_weapon_parts = (
        sorted_stats["active"]["case"],
        sorted_stats["active"]["laser"],
        sorted_stats["active"]["barrel"],
        sorted_stats["active"]["muzzle"],
        sorted_stats["active"]["trigger"]
        )

    # Get current weapon name
    for q_weapon, q_weapon_parts in quake_weapons.items():
        if(quake_current_weapon_parts == q_weapon_parts):
            sorted_stats["active"]["weapon"] = q_weapon

    if("weapon" not in sorted_stats["active"]):
        q_weapon_name = ""
        q_weapon_name += quake_case_prefixes[sorted_stats["active"].get("case", "WOOD_HOE")] + " "
        q_weapon_name += quake_laser_prefixes[sorted_stats["active"].get("laser", "YELLOW")] + " Railgun "
        q_weapon_name += quake_muzzle_suffixes[sorted_stats["active"].get("muzzle", "NONE")]
        q_weapon_name += quake_trigger_suffixes[sorted_stats["active"].get("trigger", "ONE_POINT_THREE")]
        q_weapon_name += quake_barrel_suffixes[sorted_stats["active"].get("barrel", "SMALL_BALL")]
        sorted_stats["active"]["weapon"] = q_weapon_name

    # # Resolve for max shop (and rank)

    # Setup for cosmetics purchased
    total_items_purchased = {"None": 0, "VIP": 0, "VIP+": 0, "MVP": 0, "MVP+": 0}

    # Add hats to cosmetic totals
    for q_hat in quake_hats:
        if(q_hat[0] in raw_stats["packages"]):
            total_items_purchased[q_hat[2]] += 1

    # Total coins spent on chestplates
    for q_chest in quake_chestplates:
        if(q_chest[0] in raw_stats["packages"]):
            total_items_purchased[q_chest[2]] += 1

    sorted_stats["items_purchased"] = total_items_purchased

    # Return cleaned up stats
    return sorted_stats
