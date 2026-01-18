# type: ignore

import matplotlib.pyplot as plt

from dice import DiceSet, Die

PLOT_SIZE = 10

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")


def plot_space() -> None:
    points_x = []
    points_y = []
    points_z = []

    for x in range(-PLOT_SIZE, PLOT_SIZE + 1):
        for y in range(x, PLOT_SIZE + 1):
            for z in range(y, PLOT_SIZE + 1):
                points_x.append(x)
                points_y.append(y)
                points_z.append(z)
    ax.scatter(points_x, points_y, points_z, c="blue", marker="o", s=10, alpha=0.6)


def add_die_coordinates(die: Die, color: str) -> None:
    ax.scatter(  # type: ignore
        die.sides[0],
        die.sides[1],
        die.sides[2],
        c=color,
        marker="o",
        s=10,
    )


def add_coordinates(dice_set: DiceSet) -> None:
    add_die_coordinates(dice_set.die_a, "red")
    add_die_coordinates(dice_set.die_b, "orange")
    add_die_coordinates(dice_set.die_c, "green")


def show_plot() -> None:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Points from -10 to 10")

    plt.legend()
    plt.show()
