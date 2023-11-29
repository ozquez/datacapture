class DataCapture:
    """Class to capture and store data for statistical analysis."""

    def __init__(self) -> None:
        """
        Initialize an array to store the counts of each number.
        The size is set to 1000.
        """
        self.SIZE: int = 10
        self.data: list[int] = [0] * self.SIZE

    def add(self, number: int) -> None:
        """
        Increments the value at the specified index in the data list by 1.

        :param number: The index of the element to be incremented.
        :raises ValueError: If the number is outside the valid range.
        """
        if 0 <= number < len(self.data):
            self.data[number] += 1
        else:
            raise ValueError(
                f"Number need to be greater than 0 and less than {len(self.data)}"
            )
