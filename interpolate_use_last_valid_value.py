"""_summary_
If you want to use the last valid value for interpolation, you can use the `ffill` method in `pandas`. The `ffill` method fills the missing values with the last valid value in the time series. Here's an example code that demonstrates how to use `ffill` to interpolate time series data that is sampled every 5 minutes to a higher frequency of every 1 minute:

In this code, we generate an example time series data `ts` that is sampled every 5 minutes, using the `np.random.randint` function to generate random integer values between 10 and 20. We use the `pd.date_range` function to create a datetime index that spans 5 periods, starting from January 1, 2022, and sampled every 5 minutes. We create a Pandas Series object `ts` by passing the data and index to the `pd.Series` function.

We then use the `resample` method to resample the time series data to a higher frequency of every 1 minute, using the '1min' frequency string. The `ffill` method is used to fill in the missing values with the last valid value in the time series.

Finally, we print the original and interpolated time series data using the `print` function. The interpolated time series data `ts_interpolated` should have 4 times as many data points as the original data `ts`, with the missing values filled in using the last valid value.

Note that using the last valid value for interpolation may not be appropriate for all types of data, as it assumes that the time series data is stationary and does not change rapidly between adjacent time points. If the data is highly variable or has sudden changes, using the last valid value for interpolation may lead to inaccurate results. In such cases, linear interpolation or other interpolation methods may be more appropriate.
"""

import pandas as pd
import numpy as np

# Generate example time series data that is sampled every 5 minutes
data = [np.random.randint(10, 20) for _ in range(5)]
index = pd.date_range('2022-01-01', periods=5, freq='5min')
ts = pd.Series(data, index=index)

# Interpolate the data to a higher frequency of every 1 minute using last valid value
ts_interpolated = ts.resample('1min').ffill()

# Print the original and interpolated time series data
print("Original data:\n", ts)
print("\nInterpolated data:\n", ts_interpolated)
