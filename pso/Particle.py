from collections.abc import Callable
import random


class Particle:
    def __init__(
        self,
        dimensions: int,
        bounds: list[tuple[float, float]],
        objective_function: Callable[[list[float]], float],
    ) -> None:
        if dimensions <= 0:
            raise ValueError("dimensions must be greater than zero")
        if len(bounds) != dimensions:
            raise ValueError("bounds must contain one pair per dimension")
        if any(lower > upper for lower, upper in bounds):
            raise ValueError("each lower bound must be <= its upper bound")

        self._dimensions = dimensions
        self._bounds = bounds.copy()
        self._objective_function = objective_function
        self._position = [
            random.uniform(lower, upper) for lower, upper in bounds
        ]
        self._velocity = [
            random.uniform(lower, upper) for lower, upper in bounds
        ]
        self._p_best_position = self._position.copy()
        self._p_best_value = objective_function(self._position.copy())

    def get_dimensions(self) -> int:
        return self._dimensions

    def get_bounds(self) -> list[tuple[float, float]]:
        return self._bounds.copy()

    def get_position(self) -> list[float]:
        return self._position.copy()

    def get_velocity(self) -> list[float]:
        return self._velocity.copy()

    def get_objective_function(
        self,
    ) -> Callable[[list[float]], float]:
        return self._objective_function

    def get_p_best_position(self) -> list[float]:
        return self._p_best_position.copy()

    def get_p_best_value(self) -> float:
        return self._p_best_value