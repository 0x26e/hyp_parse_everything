from .constants import *

# Returns formatted Quake stats
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

    # Add chestplates to cosmetic totals
    for q_chest in quake_chestplates:
        if(q_chest[0] in raw_stats["packages"]):
            total_items_purchased[q_chest[2]] += 1

    # Add leggings and boots to cosmetic totals
    for q_lower in quake_lowers:
        if(f"{q_chest[0]}_leggings" in raw_stats["packages"]):
            total_items_purchased[q_chest[2]] += 1
        if(f"{q_chest[0]}_boots" in raw_stats["packages"]):
            total_items_purchased[q_chest[2]] += 1

    # Add killsounds to cosmetic totals
    for q_ks, q_ks_type in quake_killsounds.items():
        if(q_ks in raw_stats["packages"]):
            total_items_purchased[q_ks_type] += 1

    # Add quake parts to shop totals
    for q_part, q_part_rank in quake_parts_ranks.items():
        if(q_part in raw_stats["packages"]):
            total_items_purchased[q_part_rank] += 1

    sorted_stats["items_purchased"] = total_items_purchased

    # Return cleaned up stats
    return sorted_stats
