# DataCapture

The `DataCapture` module is designed to record small positive integers and provide quick statistical analysis. The module is optimized to achieve constant time complexity (O(1)) for querying statistics and linear time complexity (O(n)) for the build_stats operation.

#### Build Stats Operation O(n) 
The `build_stats` method, which is responsible for preparing the data for O(1) queries, operates in linear time O(n). Here's how it achieves this:

- **Single Pass**: The method makes a single pass over the array of counts to compute the cumulative_counts_below and cumulative_counts_above lists, which means it goes through the data only once.

- **Optimized Insertion**: The `cumulative_counts_above` list is done in reverse order, populating a pre-allocated list to maintain O(n) complexity.


#### Query Operations O(1) 

The methods `less`, `greater`, and `between` are designed to run in O(1) time and this is accomplished through the following strategies:

- **Precomputed Access**: These methods use the precomputed cumulative_counts_below and cumulative_counts_above arrays to return results in constant time.

- **Direct Access**: Results are retrieved by accessing array elements by index, which is independent of the size of the input data.


## Prerequisites

- Python 3.6 or higher

## Installation

To get started, clone the repository to your local machine:

```bash
git clone https://github.com/ozquez/datacapture.git
cd datacapture
```

## Usage
To use the DataCapture module, instantiate the DataCapture class, add numbers using the add method, and build stats for querying:

```python
from src.data_capture import DataCapture

# Instantiate DataCapture and add numbers
capture = DataCapture()
capture.add(3)
capture.add(9)
capture.add(3)
capture.add(4)
capture.add(6)

# Build stats from captured data
stats = capture.build_stats()

# Perform queries
print(stats.less(4))        # Output: 2
print(stats.between(3, 6))  # Output: 4
print(stats.greater(4))     # Output: 2
```

## Running Tests
```bash
python -m unittest discover tests
```