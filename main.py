import dice_view
from dice import DiceSet, Die

ZOOM = 5
PLOT_SIZE = dice_view.PLOT_SIZE * ZOOM

# dice_view.plot_space()

points: list[dice_view.CoordinatesData] = []


def main() -> None:
    not_intransitive_count = 0
    intransitive_count = 0
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 6, 8), (2, 4, 9)) #infinite cuboid and tetrahedron Y
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 6, 8), (0, 4, 9)) #house and tetrahedron Z
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 5, 9), (2, 6, 7)) #same as above Z
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 7, 8), (3, 5, 6)) #house case, only the house X
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 6, 8), (4, 5, 7)) #house case X
    #dices: tuple[dice_view.CoordinatesData,dice_view.CoordinatesData] = ((1, 7, 8), (2, 3, 9)) #cuboid case Y
    die_a = Die(dices[0])
    die_b = Die(dices[1])
    dice_view.add_die(die_a, "red")
    dice_view.add_die(die_b, "orange")
    for x in range(-PLOT_SIZE, PLOT_SIZE + 1):
        for y in range(x, PLOT_SIZE + 1):
            for z in range(y, PLOT_SIZE + 1):
                coordinates: dice_view.CoordinatesData = (x / ZOOM, y / ZOOM, z / ZOOM)
                die_c = Die(coordinates)
                dice_set = DiceSet(die_a, die_b, die_c)
                if dice_set.is_intransitive():
                    points.append(coordinates)
                    intransitive_count += 1
                else:
                    not_intransitive_count += 1
    print(f"Not intransitive: {not_intransitive_count}")
    print(f"Intransitive: {intransitive_count}")
    dice_view.add_coordinates(points)
    dice_view.show_plot()

if __name__ == "__main__":
    main()

"""when die A = (2,4,9) and die B = (1,6,8)
it forms 2 3D Cuboid limiting areas
one is a finite region with 2 2D special lines
and the other is an infinite region

######

the finite area is bounded by a quadrilateral on a Y = 5.999... but not 6 (because at 6 it becomes transitive)
the quadrilateral is defined by the points:
([2-6], 5.999..., [6-8])
and another quadrilateral at Y = 4.0000... but not 4 (because at 4 it becomes transitive) so the Y range of this area is 4 < Y < 6
the quadrilateral is defined by the points:
([2-4], 4.0000..., [4-8])


([2-6], 6, 6) finite line
(4, 4, [4-8]) finite line

######

the cuboid limiting area is defined by the points:
([1-],[6-4],[9-]) infinite cuboid 
so X > 1, 4 < Y < 6, Z > 9
"""


"""when die A = (0,4,9) and die B = (1,6,8)
it forms 2 regions, each one has one special 2D line and an limiting area
([-0], 9, 8.something) infinite line
(1, 1, [8-9]) finite line

the first region is a triangular prism
((1,1,Z),(1,4,Z),(4,4,Z)) for Z in (8,9)

the second region is a cuboid merged with a triangular prism, forming a complex shape
the limiting area is infinite in the negative X direction
the cuboid is defined by the points:
([-0], [6-8], [8-9]) X < 0, 6 < Y < 8, 8 < Z < 9
the triangular prism is defined by the points:
((X,8,8),(X,8,9),(X,9,9)) for X < 0
"""