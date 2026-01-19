# type: ignore

import matplotlib.pyplot as plt

from dice import DiceSet, Die

PLOT_SIZE = 10
CoordinatesData = tuple[float, float, float]
LineData = tuple[CoordinatesData, CoordinatesData]

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


def add_dot(x: float, y: float, z: float, color: str) -> None:
    ax.scatter(  # type: ignore
        x,
        y,
        z,
        c=color,
        marker="o",
        s=5,
    )


def add_dots(coordinates: list[CoordinatesData], color: str) -> None:
    xs = [coord[0] for coord in coordinates]
    ys = [coord[1] for coord in coordinates]
    zs = [coord[2] for coord in coordinates]
    ax.scatter(xs, ys, zs, c=color, marker="o", s=5)


def add_lines(lines: list[LineData]) -> None:
    print(f"Adding {len(lines)} lines")
    for line in lines:
        coord_a, coord_b = line
        (x1, y1, z1) = coord_a
        if coord_a == coord_b:
            add_dot(x1, y1, z1, "green")
            continue
        (x2, y2, z2) = coord_b
        (x1, y1, z1), (x2, y2, z2) = line
        ax.plot([x1, x2], [y1, y2], [z1, z2], c="green", linewidth=2)


def find_lines(coordinates: list[CoordinatesData]) -> list[LineData]:
    # find coordinates that share the same Y and Z. X varies.
    x_lines: dict[tuple[float, float], list[CoordinatesData]] = {}
    for coord in coordinates:
        x, y, z = coord
        key = (y, z)
        if key not in x_lines:
            x_lines[key] = []
        x_lines[key].append(coord)
    lines: list[LineData] = []
    for coords in x_lines.values():
        lowest_x = min(coords, key=lambda c: c[0])
        highest_x = max(coords, key=lambda c: c[0])
        lines.append((lowest_x, highest_x))
    return lines


def add_coordinates(coordinates: list[CoordinatesData]) -> None:
    lines = find_lines(coordinates)
    add_lines(lines)


"""
    FUTURE IMPLEMENTATION
    squares = find_squares(coordinates)
    add_squares(squares)"""


def add_die(die: Die, color: str) -> None:
    coords = die.sides
    add_dot(coords[0], coords[1], coords[2], color)


def add_dieset(dice_set: DiceSet) -> None:
    add_die(dice_set.die_a, "red")
    add_die(dice_set.die_b, "orange")
    add_die(dice_set.die_c, "green")


def show_plot() -> None:
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    ax.set_title("3D Points from -10 to 10")

    plt.legend()
    plt.show()
