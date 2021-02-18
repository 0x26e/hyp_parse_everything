from .constants import *
# ! # Add stats from achievements
# Returns formatted Smash Heroes Stats
def getSmashHeroes(raw_stats, achievements):

    # Setup better naming
    CLASS_STATS = raw_stats.get("class_stats", {})

    # Setup container to hold stats
    sorted_stats = {"general": {}, "booster": {}}

    # Exp Booster stats
    sorted_stats["booster"]["active_exp_booster"] = raw_stats.get("expired_booster", False)
    sorted_stats["booster"]["exp_booster_count"] = sum(map(lambda x: raw_stats.get(f"expBooster_purchases_{str(x)}_plays",0) * x,[10,30,50,100]))


    sorted_stats["general"] = {
        stat_proper: raw_stats.get(stat, 0)
        for stat, stat_proper in smash_stat_name_conversions.items()
        }

    sorted_stats["general"].update({
        stat: raw_stats.get(stat, 0)
        for stat in smash_stat_names
        })

    # Setup class container
    sorted_stats.update({
        smash_class_proper: {"class_deaths": {}}
        for smash_class, smash_class_proper in smash_classes.items()
    })

    # For every class in smash classes
    for smash_class, smash_class_proper in smash_classes.items():

        # Add stats with default as 0
        sorted_stats[smash_class_proper]["overall"] = {
            smash_stat: CLASS_STATS[smash_class].get(smash_stat, 0)
            for smash_stat in smash_class_stats
            }

        # Add proper class stats with default as 0
        sorted_stats[smash_class_proper]["overall"].update({
            smash_stat_proper: CLASS_STATS[smash_class].get( smash_stat, 0)
            for smash_stat, smash_stat_proper in smash_class_stat_conversions.items()
            })

        # Add stats from general section with default as 0
        sorted_stats[smash_class_proper]["overall"].update({
            smash_stat_proper: int(raw_stats.get( (smash_stat + smash_class), 0))
            for smash_stat, smash_stat_proper in smash_class_stats_from_general.items()
            })

        # For every gamemode in gamemodes
        for gm, gm_proper in smash_gamemodes.items():
            # Add gamemode-specific stats with default as 0
            sorted_stats[smash_class_proper][gm_proper] = {
                smash_stat: CLASS_STATS[smash_class].get( f"{smash_stat}_{gm}", 0)
                for smash_stat in smash_class_stats
            }

        """
        class_deaths = {
            class_1: total_deaths_to_class_1,
            class_2: total_deaths_to_class_2,
            ...,
            class_n: total_deaths_to_class_n,
        }
        """
        def get_total_deaths_by_class(class_stats, killer_class):
            """
            class_stats: stats of the class which we want the total deaths of
            killer_class: the class that killed the class of `class_stats`
            """
            return sum(
                class_stats.get(ability, {}).get("smashed", 0)
                for ability in smash_classes_abilities.get(killer_class, {})
            )

        for c_smash_class, smash_class_proper in smash_classes.items():
            class_stats = CLASS_STATS[c_smash_class]

            sorted_stats[smash_class_proper]["class_deaths"] = {
                killer_class: get_total_deaths_by_class(class_stats, killer_class)
                for killer_class in smash_classes
            }

    # Return cleaned up stats
    return sorted_stats
