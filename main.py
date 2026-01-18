from dice import Die
import dice


die_a = Die((2, 4, 9))
die_b = Die((1, 6, 8))
die_c = Die((3, 5, 7))
dice_set = dice.DiceSet(die_a, die_b, die_c)
print(dice_set.is_intransitive())