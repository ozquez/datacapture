class DataCapture:
    """Class to capture and store data for statistical analysis."""

    def __init__(self) -> None:
        """
        Initialize an array to store the counts of each number.
        The size is set to 1000.
        """
        self.SIZE: int = 1000
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
        self.cumulative_counts_above: list[int] = self._precompute_greater()

    def _precompute_less(self) -> list[int]:
        """
        Precompute the count of numbers less than each index.

        :return: A list of cumulative counts of numbers less than each index.
        """
        count: int = 0
        cumulative_counts_below: list[int] = []
        for num in self.data:
            cumulative_counts_below.append(count)
            count += num

        return cumulative_counts_below

    def _precompute_greater(self) -> list[int]:
        """
        Precompute the count of numbers greater than each index.

        :return: A list of cumulative counts of numbers greater than each index.
        """
        count: int = 0
        cumulative_counts_above: list[int] = []
        for num in reversed(self.data):
            cumulative_counts_above.insert(0, count)
            count += num

        return cumulative_counts_above

    def less(self, threshold: int) -> int:
        """
        Return the number of elements less than the given threshold.

        :param threshold: The threshold value.
        :return: Count of numbers less than the threshold.
        """
        return self.cumulative_counts_below[threshold]

    def greater(self, threshold: int) -> int:
        """
        Return the number of elements greater than the given threshold.

        :param threshold: The threshold value.
        :return: Count of numbers greater than the threshold.
        """
        return self.cumulative_counts_above[threshold]

    def between(self, lower: int, upper: int) -> int:
        """
        Return the number of elements between the lower and upper bounds, inclusive.

        :param lower: The lower bound.
        :param upper: The upper bound.
        :return: Count of numbers in the inclusive range [lower, upper].
        """
        if lower == 0:
            # Include the count at 'upper' as the range is inclusive
            return self.cumulative_counts_below[upper] + self.data[upper]

        # Calculate the count in the range [lower, upper], inclusive
        return (
            self.cumulative_counts_below[upper]
            - self.cumulative_counts_below[lower]
            + self.data[upper]
        )
