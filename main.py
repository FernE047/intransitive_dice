import dice_view
from dice import Die
import dice

ZOOM = 4
PLOT_SIZE = dice_view.PLOT_SIZE * ZOOM

#dice_view.plot_space()


def main() -> None:
    not_intransitive_count = 0
    intransitive_count = 0
    die_a = Die((2, 4, 9))
    die_b = Die((1, 6, 8))
    dice_view.add_die_coordinates(die_a, "red")
    dice_view.add_die_coordinates(die_b, "orange")
    for x in range(-PLOT_SIZE, PLOT_SIZE + 1):
        for y in range(x, PLOT_SIZE + 1):
            for z in range(y, PLOT_SIZE + 1):
                die_c = Die((x / ZOOM, y / ZOOM, z / ZOOM))
                dice_set = dice.DiceSet(die_a, die_b, die_c)
                if dice_set.is_intransitive():
                    dice_view.add_die_coordinates(die_c, "green")
                    intransitive_count += 1
                else:
                    not_intransitive_count += 1
    print(f"Not intransitive: {not_intransitive_count}")
    print(f"Intransitive: {intransitive_count}")
    dice_view.show_plot()


if __name__ == "__main__":
    main()
