import random

from pandas import DataFrame

from Code.constants import *


def get_stats(df: DataFrame) -> dict:
    stats = get_stats_dict()
    groups = df.groupby(SCORE).size().reset_index(name=COUNT)

    for _, group in groups.iterrows():
        score = group[SCORE]
        count = group[COUNT]
        score = 0 if score <= 0 else score
        score = 15 if score >= 15 else score
        major = SCORE_TO_TIER[score][0]
        minor = SCORE_TO_TIER[score][1]

        stats[Statistics.TIERS][major][minor][Tier.TOTAL] += count
        stats[Statistics.TIERS][major][minor][Tier.LEFT] += count

    return stats


def get_stats_dict() -> dict:
    return {
        Statistics.CORRECT: 0,
        Statistics.INCORRECT: 0,
        Statistics.TIERS: {
            Tier.BEGINNER: {
                Tier.LOWER: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.MIDDLE: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.UPPER: {Tier.TOTAL: 0, Tier.LEFT: 0},
            },
            Tier.PRE_INTERMEDIATE: {
                Tier.LOWER: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.MIDDLE: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.UPPER: {Tier.TOTAL: 0, Tier.LEFT: 0},
            },
            Tier.INTERMEDIATE: {
                Tier.LOWER: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.MIDDLE: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.UPPER: {Tier.TOTAL: 0, Tier.LEFT: 0},
            },
            Tier.UPPER_INTERMEDIATE: {
                Tier.LOWER: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.MIDDLE: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.UPPER: {Tier.TOTAL: 0, Tier.LEFT: 0},
            },
            Tier.ADVANCED: {
                Tier.LOWER: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.MIDDLE: {Tier.TOTAL: 0, Tier.LEFT: 0},
                Tier.UPPER: {Tier.TOTAL: 0, Tier.LEFT: 0},
            },
        },
        Statistics.CURRENT_TIER: [Tier.BEGINNER, Tier.LOWER],
    }


def get_random_word(main) -> None:
    df = main.snapshot

    current_tier = main.stats[Statistics.CURRENT_TIER]
    max_score = [_ for _, value in SCORE_TO_TIER.items() if value == current_tier][0]

    if max_score == 0:
        words_on_this_tier = df.loc[df.Score <= max_score]
    elif max_score == 15:
        words_on_this_tier = df.loc[df.Score >= max_score]
    else:
        words_on_this_tier = df.loc[df.Score == max_score]

    if len(words_on_this_tier.groupby(SCORE)) != 1:
        available_groups = list(words_on_this_tier.groupby(SCORE).groups.keys())
        for group in available_groups:
            words_on_this_tier = df.loc[df.Score == group]
            break

    random_number = random.randint(0, len(words_on_this_tier) - 1)
    random_word = words_on_this_tier.iloc[random_number]

    main.word.finnish = random_word.Finnish
    main.word.english = random_word.English
