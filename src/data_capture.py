class DataCapture:
    """
    Initializes an array to store each number's count and
    provides a method to increment the count at a specified index.
    """

    SIZE: int = 1000

    def __init__(self) -> None:
        """
        Initializes an array to store the counts of each number.
        The size is set to 1000.
        """
        self.data: list[int] = [0] * self.SIZE

    def add(self, number: int) -> None:
        """
        Increments the value at the specified index in the data list by 1.
        Accepts only positive numbers integers.

        :param number: The index of the element to be incremented.
        :raises ValueError: If the number is outside the valid range.
        """
        if 0 < number <= len(self.data):
            self.data[number] += 1
        else:
            raise ValueError(
                f"Number need to be greater than 0 and less or equal to {len(self.data)}"
            )

    def build_stats(self) -> "Stats":
        """
        Create and return a Stats object using the current data.

        :return: A Stats object for querying statistics.
        """
        return Stats(self.data)


class Stats:
    """Class to provide statistical analysis of DataCapture."""

    def __init__(self, data: list[int]) -> None:
        """
        Initialize the Stats object with the given data.
        Precompute the cumulative counts for efficient querying.

        :param data: The data from the DataCapture object.
        """
        self.data: list[int] = data
        self.cumulative_counts_below: list[int] = self._precompute_less()
        self.total_count: int = self.cumulative_counts_below[-1] + self.data[-1]

    def _precompute_less(self) -> list[int]:
        """
        Precompute the count of numbers less than each index.

        :return: A list of cumulative counts of numbers less than each index.
        """
        count: int = 0
        cumulative_counts_below: list[int] = []
        for value in self.data:
            cumulative_counts_below.append(count)
            count += value

        return cumulative_counts_below

    def _validate_threshold(self, threshold: int):
        """
        Validates the threshold.

        :param threshold: The value to be validated.
        :raises ValueError: If the threshold is not an integer or is out of the valid range.
        """

        if not isinstance(threshold, int):
            raise ValueError("Threshold must be an integer")

        if not (0 < threshold <= len(self.data)):
            raise ValueError(
                f"Threshold must be greater than 0 and less or equal to {len(self.data)}"
            )

    def less(self, threshold: int) -> int:
        """
        Return the number of elements less than the given threshold.

        :param threshold: The threshold value.
        :return: Count of numbers less than the threshold.
        """
        self._validate_threshold(threshold)
        return self.cumulative_counts_below[threshold]

    def greater(self, threshold: int) -> int:
        """
        Return the number of elements greater than the given threshold.

        :param threshold: The threshold value.
        :return: Count of numbers greater than the threshold.
        """
        self._validate_threshold(threshold)
        return self.total_count - self.less(threshold + 1)

    def between(self, lower: int, upper: int) -> int:
        """
        Return the number of elements between the lower and upper bounds, inclusive.

        :param lower: The lower bound.
        :param upper: The upper bound.
        :return: Count of numbers in the inclusive range [lower, upper].
        """
        self._validate_threshold(lower)
        self._validate_threshold(upper)

        # Count numbers less than or equal to 'upper'
        upper_count = self.less(upper + 1)

        # Count numbers strictly less than 'lower'
        lower_count = self.less(lower)

        return upper_count - lower_count
