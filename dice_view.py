# type: ignore

import matplotlib.pyplot as plt

from dice import DiceSet

PLOT_SIZE = 10
points_x = []
points_y = []
points_z = []

for x in range(-PLOT_SIZE, PLOT_SIZE + 1):
    for y in range(x, PLOT_SIZE + 1):
        for z in range(y, PLOT_SIZE + 1):
            points_x.append(x)
            points_y.append(y)
            points_z.append(z)

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection="3d")

ax.scatter(points_x, points_y, points_z, c="blue", marker="o", s=10, alpha=0.6)


def add_coordinates(dice_set: DiceSet) -> None:
    ax.scatter(  # type: ignore
        dice_set.die_a.sides[0],
        dice_set.die_a.sides[1],
        dice_set.die_a.sides[2],
        c="red",
        marker="o",
        s=100,
        label="Die A",
    )
    ax.scatter(
        dice_set.die_b.sides[0],
        dice_set.die_b.sides[1],
        dice_set.die_b.sides[2],
        c="orange",
        marker="o",
        s=100,
        label="Die B",
    )
    ax.scatter(
        dice_set.die_c.sides[0],
        dice_set.die_c.sides[1],
        dice_set.die_c.sides[2],
        c="green",
        marker="o",
        s=100,
        label="Die C",
    )


def show_plot() -> None:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Points from -10 to 10")

    plt.legend()
    plt.show()
