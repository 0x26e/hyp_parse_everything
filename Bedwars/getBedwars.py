from .constants import *

# ! # Known bugs: Losses need to be fixed
# ! # Add stats from achievements
# Returns formatted Bedwars stats
def getBedwars(raw_stats, achievements):

    # Setup container to hold stats
    sorted_stats = {"general": {}, "cosmetic_boxes": {}}

    # List of active stats
    bedwars_active_stats = {"activeProjectileTrail": "projectile_trail", "spray_storage_new": "sprays", "activeIslandTopper": "island_topper",
        "activeDeathCry": "death_cry", "activeNPCSkin": "npc_skin", "glyph_storage_new": "glyphs", "activeKillMessages": "kill_messages",
        "activeKillEffect": "kill_effect", "activeVictoryDance": "victory_dance", "selected_ultimate": "ultimate"
        }

    # List of gamemodes
    bedwars_gamemodes = {"eight_one": "one", "eight_two": "two", "four_three": "three", "four_four": "four", "castle": "castle",
        "eight_one_ultimate": "one_ultimate", "eight_two_ultimate": "two_ultimate", "four_four_ultimate": "four_ultimate",
        "eight_one_rush": "one_rush", "four_four_rush": "four_rush",
        "eight_two_voidless": "two_voidless", "four_four_voidless": "four_voidless",
        "eight_two_lucky": "two_lucky", "four_four_lucky": "four_lucky"
        }

    # Setup proper name conversions
    bedwars_stat_name_conversions = {"winstreak": "winstreak", "losses": "losses", "wins_bedwars": "wins", "games_played_bedwars": "games_played",
        "beds_lost_bedwars": "beds_lost", "beds_broken_bedwars": "beds_broken", "permanent _items_purchased_bedwars": "permament_items_purchased",
        "kills": {
            "kills": "total",
            "projectile_kills_bedwars": "projectile",
            "void_kills_bedwars": "void",
            "fall_kills_bedwars": "fall_damage",
            "entity_explosion_kills_bedwars": "explosion",
            "entity_attacK_kills_bedwars": "mob"},
        "final_kills": {
            "final_kills_bedwars": "total",
            "projectile_final_kills_bedwars": "projectile",
            "void_final_kills_bedwars": "void",
            "fall_final_kills_bedwars": "fall_damage",
            "entity_explosion_final_kills_bedwars": "explosion",
            "entity_attacK_final_kills_bedwars": "mob"},
        "deaths": {
            "deaths_bedwars": "total",
            "projectile_deaths_bedwars": "projectile",
            "void_deaths_bedwars": "void",
            "fall_deaths_bedwars": "fall_damage",
            "suffocation_deaths_bedwars": "suffocation",
            "entity_explosion_deaths_bedwars": "explosion",
            "entity_attacK_deaths_bedwars": "mob"},
        "final_deaths": {
            "final_deaths_bedwars": "total",
            "projectile_final_deaths_bedwars": "projectile",
            "void_final_deaths_bedwars": "void",
            "fall_final_deaths_bedwars": "fall_damage",
            "suffocation_deaths_bedwars": "suffocation",
            "entity_explosion_final_deaths_bedwars": "explosion",
            "entity_attack_final_deaths_bedwars": "mob"},
        "resources": {
            "resources_collected_bedwars": "total",
            "iron_resources_collected_bedwars": "iron",
            "gold_resources_collected_bedwars": "gold",
            "diamond_resources_collected_bedwars": "diamond",
            "emerald_resources_collected_bedwars": "emerald"}
        }
    # ! # games_played_bedwars_1, items_purchased_bedwars, _items_purchased_bedwars
    # ! # Kills: custom_kills_bedwars, fire_tick_kills_bedwars, contact_kills_bedwars, fire_kills_bedwars
    # ! # Final Kills: custom_final_kills_bedwars, fire_tick_final_kills_bedwars, contact_final_kills_bedwars, fire_final_kills_bedwars
    # ! # Deaths: custom_deaths_bedwars, fire_tick_deaths_bedwars, fire_deaths_bedwars
    # ! # Final Deaths: custom_deaths_bedwars, fire_tick_deaths_bedwars, fire_deaths_bedwars

    # Setup stat names
    bedwars_stat_names = {"coins": "coins", "Experience": "experience"}

    # Setup cosmetic stat names
    bedwars_cosmetic_stat_names = {"bedwars_box": "unopened", "bedwars_halloween_boxes": "halloween_opened",
        "bedwars_easter_boxes": "easter_opened", "bedwars_christmas_boxes": "christmas_opened", "bedwars_lunar_boxes": "lunar_opened",
        "bedwars_box_commons": "common", "bedwars_box_rares": "rare", "bedwars_box_epics": "epic", "bedwars_box_legendaries": "legendary"}
    # ! # bedwars_boxes (is it including unopened or not)
    # ! # Bedwars_openedChests, Bedwars_openedCommons, Bedwars_openedRares, Bedwars_openedLegendaries, spooky_open_ach

    # Cosmetic box stats
    sorted_stats["cosmetic_boxes"] = {
        cm_stat_proper: raw_stats.get(cm_stat, 0)
        for cm_stat, cm_stat_proper in bedwars_cosmetic_stat_names.items()
        }

    # Start general stats
    sorted_stats["general"] = {
        bw_stat_proper: raw_stats.get(bw_stat, 0)
        for bw_stat, bw_stat_proper in bedwars_stat_names.items()
        }

    # Finish general stats
    for bw_stat, bw_stat_proper in bedwars_stat_name_conversions.items():

        # Check if subsection of stats
        if( isinstance(bw_stat_proper, dict) ):
            sorted_stats["general"][bw_stat] = {
                sub_bw_stat_proper: raw_stats.get(sub_bw_stat, 0)
                for sub_bw_stat, sub_bw_stat_proper in bw_stat_proper.items()
                }

        # If individual stat
        else:
            sorted_stats["general"][bw_stat_proper] = raw_stats.get(bw_stat, 0)

    # Gamemode stats
    for gm, gm_proper in bedwars_gamemodes.items():

        # Initialize container for gamemode-specific stats
        sorted_stats[gm_proper] = {}

        # For every stat that can be gamemode-specific
        for bw_stat, bw_stat_proper in bedwars_stat_name_conversions.items():

            # If individual stat
            if(not isinstance(bw_stat_proper, dict)):

                # Get the stat, default to 0
                sorted_stats[gm_proper][bw_stat_proper] = raw_stats.get(f"{gm}_{bw_stat}", 0)

            # If substats
            else:

                # Create subdict of stats
                sorted_stats[gm_proper][bw_stat] = {
                sub_bw_stat_proper: raw_stats.get(f"{gm}_{sub_bw_stat}", 0)
                for sub_bw_stat, sub_bw_stat_proper in bw_stat_proper.items()
                }

    # Active stats
    sorted_stats["active"] = {
        a_stat_proper: raw_stats.get(a_stat, "")
        for a_stat, a_stat_proper in bedwars_active_stats.items()
        }



    # Return cleaned up stats
    return sorted_stats
