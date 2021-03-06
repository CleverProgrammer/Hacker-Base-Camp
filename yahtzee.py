import doctest

"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

ALL_HANDS = range(1, 7)


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of
    outcomes of given length.
    """

    answer_set = set([()])
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set
    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the
    upper section of the Yahtzee score card.

    hand: full yahtzee hand

    Returns an integer score

    >>> score((1, 5, 5, 2, 3))
    10
    >>> score((1, 4, 1, 4, 6))
    8
    >>> score((1, 1, 1, 1, 1))
    5
    >>> score((2, 3, 4, 5, 6))
    6
    """
    score = 0
    max_score = 0
    dice_counts = {}
    for die in hand:
        if die in dice_counts:
            dice_counts[die] += 1
        else:
            dice_counts[die] = 1
    for potential_die in ALL_HANDS:
        if potential_die in dice_counts:
            score = dice_counts[potential_die] * potential_die
            if score > max_score:
                max_score = score
    return max_score


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value based on held_dice given that there
    are num_free_dice to be rolled, each with num_die_sides.

    held_dice: dice that you will hold
    num_die_sides: number of sides on each die
    num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """
    new_score = 0
    total_score = 0.0

    all_possibilities_for_free_dice = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)
    for possibility in all_possibilities_for_free_dice:
        new_hand = possibility + held_dice
        print (new_hand, "-->", score(new_hand))
        new_score = score(new_hand)
        total_score += new_score

    return total_score / len(all_possibilities_for_free_dice)


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold.

    hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """

    hold_choices = []
    for length in range(1, len(hand) + 1):
        for held_cards in gen_all_sequences(hand, length):
            hold_choices.append(held_cards)
    return set(hold_choices)


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the
    discarded dice are rolled.

    hand: full yahtzee hand
    num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and
    the second element is a tuple of the dice to hold
    """
    max_expected = 0
    max_hand = None
    for hand in gen_all_holds(hand):
        expected_value = expected_value(hand, len(hand), num_die_sides)
        if expected_value > max_expected:
            max_expected = expected_value
            max_hand = hand

    return (max_expected, max_hand)


def run_example():
    """
    Compute the dice to hold and expected score for an example
    """

    print(expected_value((2, 2), 6, 2))
    print("3, 5, 2, --> ", gen_all_holds([3, 5, 2]))
    #print("2, 2, 2, 6, 1 --> ", gen_all_holds([2, 2, 2, 6, 1]))
    #print("5, 5, 6, 6, 1 --> ", gen_all_holds([5, 5, 6, 6, 1]))
    #print("1, 1, 6, 6, 1 --> ", gen_all_holds([1, 1, 6, 6, 1]))
    return

run_example()
