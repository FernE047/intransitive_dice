import dice_view
from dice import Die
import dice


def main() -> None:
    die_a = Die((2, 4, 9))
    die_b = Die((3, 5, 7))
    die_c = Die((1, 6, 8))
    dice_set = dice.DiceSet(die_a, die_c, die_b)
    print(dice_set.is_intransitive())
    
    dice_view.add_coordinates(dice_set)
    dice_view.show_plot()


if __name__ == "__main__":
    main()
