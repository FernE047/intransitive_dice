import random

"""We are only dealing with 3 sided dice for now"""

OutcomesData = list[tuple[list[float], float]]


class Die:
    """Base class for all dice types."""

    def __init__(self, sides: tuple[float, float, float]) -> None:
        if len(sides) < 2:
            raise ValueError("A die must have at least two sides.")
        if len(sides) > 3:
            raise ValueError("This implementation only supports up to 3-sided dice.")
        self.sides = sorted(sides, reverse=True)

    def roll(self) -> float:
        return random.choice(self.sides)

    def simulate_rolls(self, num_rolls: int) -> list[float]:
        """Simulate multiple rolls of the dice."""
        return [self.roll() for _ in range(num_rolls)]

    def get_outcomes(self) -> OutcomesData:
        outcomes: OutcomesData = []
        for side in self.sides:
            outcomes.append(([side], side))
        return outcomes

    def print_outcomes(self) -> None:
        outcomes = self.get_outcomes()
        for rolls, result in outcomes:
            rolls_str = ", ".join(str(roll) for roll in rolls)
            print(f"Rolls: [{rolls_str}] => Result: {result}")

    def get_probabilities(self) -> dict[float, float]:
        outcomes = self.get_outcomes()
        counts: dict[float, int] = {}
        for _, result in outcomes:
            counts[result] = counts.get(result, 0) + 1
        total_outcomes = len(outcomes)
        return {side: count / total_outcomes for side, count in counts.items()}

    def print_probabilities(self) -> None:
        probabilities = self.get_probabilities()
        for side in sorted(probabilities.keys()):
            print(f"Side {side}: {probabilities[side]:.2%}")

    def compare_dice(self, other: "Die") -> dict[str, float]:
        outcomes_self = self.get_outcomes()
        outcomes_other = other.get_outcomes()
        wins_self = 0
        wins_other = 0
        ties = 0
        for _, result_self in outcomes_self:
            for _, result_other in outcomes_other:
                if result_self > result_other:
                    wins_self += 1
                elif result_self < result_other:
                    wins_other += 1
                else:
                    ties += 1
        return {
            "self_win": wins_self,
            "other_win": wins_other,
            "tie": ties,
            "total": wins_self - wins_other + 0 * ties,
        }

    def __repr__(self) -> str:
        return f"Die({self.sides})"
    
    def __str__(self) -> str:
        return f"Die with sides: {self.sides}"

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] == 0

    def __lt__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] < 0

    def __le__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] <= 0

    def __gt__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] > 0

    def __ge__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] >= 0

    def __ne__(self, value: object) -> bool:
        if not isinstance(value, Die):
            return NotImplemented
        comparision = self.compare_dice(value)
        return comparision["total"] != 0

class DiceSet():
    """A set of three dice to check for intransitivity."""
    def __init__(self, die_a: Die, die_b: Die, die_c: Die) -> None:
        self.die_a = die_a
        self.die_b = die_b
        self.die_c = die_c

    def is_intransitive(self) -> bool:
        if self.die_a > self.die_b and self.die_b > self.die_c and self.die_c > self.die_a:
            return True
        if self.die_a < self.die_b and self.die_b < self.die_c and self.die_c < self.die_a:
            return True
        return False

