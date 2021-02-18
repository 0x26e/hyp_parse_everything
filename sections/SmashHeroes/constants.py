# File for all Smash Heroes related constants

# General stats that need name conversions
smash_stat_name_conversions = {"smash_level_total": "smash_level", "games": "games_played", "smasher": "damage_kills", "smashed": "damage_deaths"}

# General stats that do not need name conversions
smash_stat_names = ["active_class", "coins", "wins", "losses", "kills", "deaths", "damage_dealt", "quits",
    "games_weekly_a", "games_weekly_b", "games_monthly_a", "games_monthly_b",
    "wins_weekly_a", "wins_weekly_b", "wins_monthly_a", "wins_monthly_b",
    "losses_weekly_a", "losses_weekly_b", "losses_monthly_a", "losses_monthly_b",
    "kills_weekly_a", "kills_weekly_b", "kills_monthly_a", "kills_monthly_b"]

# Class stats that need name conversions
smash_class_stat_conversions = {"smasher": "damage_kills", "smashed": "damage_deaths"}

# All classes (and name conversions)
smash_classes = {"THE_BULK": "bulk", "GENERAL_CLUCK": "generalcluck", "BOTMUN": "botmon", "CAKE_MONSTER": "cakemonster", "TINMAN": "tinman",
    "SKULLFIRE": "skullfire", "FROSTY": "cryomancer", "PUG": "pug", "MARAUDER": "marauder", "DUSK_CRAWLER": "voidcrawler", "SPODERMAN": "spooderman",
    "GOKU": "karakot", "SHOOP_DA_WHOOP": "shoop", "SANIC": "sanic", "SERGEANT_SHIELD": "sgtshield", "GREEN_HOOD": "greenhood"
    }

# Class stats that do not need name conversions
smash_class_stats = ["wins", "losses", "games", "kills", "deaths", "damage_dealt"]

# Gamemodes (and name conversions)
smash_gamemodes = {"normal": "1v1v1v1", "2v2": "2v2", "teams": "2v2v2"}

# Class-specific damaging abilities
smash_classes_abilities = {"THE_BULK": ("boulder", "monster_charge", "monster_mash", "seismic_slam"),
    "GENERAL_CLUCK": ("bazooka", "egg_bazooka", "reinforcements"),
    "BOTMUN": ("batarang", "grappling_hook", "botmubile"),
    "CAKE_MONSTER": ("swing_pin", "throw_cake", "cake_storm", "defecake"),
    "TINMAN": ("laser_cannon", "rocket_punch", "homing_missiles", "overload"),
    "SKULLFIRE": ("desert_eagle", "grenade", "flaming_desert_eagle"),
    "FROSTY": ("frostbolt", "freezing_breath"),
    "PUG": ("bite", "supersonic_bark", "werepug"),
    "MARAUDER": ("force_lightning", "force_pull"),
    "DUSK_CRAWLER": ("void_slash", "teleboom", "telepunch"),
    "SPODERMAN": ("spider_kick", "web_shot", "spooder_buddies"),
    "GOKU": ("ki_blast", "kame_beam"),
    "SHOOP_DA_WHOOP": ("static_laser", "charged_beam", "fir_ma_lazer", "ride_the_lightning"),
    "SANIC": ("dash", "boom", "onion_cannon"),
    "SERGEANT_SHIELD": ("shield_bash", "ricochet", "shield_quake"),
    "GREEN_HOOD": ("notched_bow", "flying_punch")
    }

# Class stats (and name conversions) that are from the general section
smash_class_stats_from_general = {"xp_": "real_xp", "lastLevel_": "level", "pg_": "prestige", "masterArmor_": "hasMasterArmor"}
