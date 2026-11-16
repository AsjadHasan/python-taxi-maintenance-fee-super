
"""
Project: Add Maintenance Fee in Child Class via super()
Description: Demonstrates inheritance, constructor chaining,
             and fare calculation using super() in Python.
"""


class Vehicle:
    """Parent class representing a vehicle with a base fare."""

    def __init__(self, base_fare: float):
        """Initialize the vehicle's base fare."""
        self.base_fare = base_fare


class Taxi(Vehicle):
    """Child class representing a taxi with a maintenance fee."""

    def __init__(self, base_fare: float):
        """Initialize taxi attributes using the parent constructor."""
        super().__init__(base_fare)

    def calculate_total_fare(self) -> float:
        """Calculate total fare including a 10% maintenance fee."""
        maintenance_fee = self.base_fare * 0.10
        total_fare = self.base_fare + maintenance_fee
        return total_fare


def main():
    """Create a Taxi object and display the total fare."""
    base_fare = 500
    taxi = Taxi(base_fare)

    print(
        f"Total fare with maintenance fee: "
        f"{taxi.calculate_total_fare()}"
    )


if __name__ == "__main__":
    main()
