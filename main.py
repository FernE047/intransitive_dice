import dice_view
from dice import Die
import dice


def main() -> None:
    not_intransitive: list[Die] = []
    die_avg = (1, 0, -1)
    for m in range(1,41):
        n = m / 10
        die_a = Die((die_avg[0], die_avg[1] - n, die_avg[2] + n))
        die_b = Die((die_avg[0] + n, die_avg[1], die_avg[2] - n))
        die_c = Die((die_avg[0] - n, die_avg[1] + n, die_avg[2]))
        dice_set = dice.DiceSet(die_a, die_c, die_b)
        if dice_set.is_intransitive():
            dice_view.add_coordinates(dice_set)
        else:
            not_intransitive.append(dice_set)
    print(len(not_intransitive))
    dice_view.show_plot()


if __name__ == "__main__":
    main()
