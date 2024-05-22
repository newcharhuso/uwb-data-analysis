from numpy import median
import pandas as pd

# Correct file paths with proper variable names
localization_error_path = (
    "/home/husnu/projects/uwb-data-analysis/20.05.2024/localization-error.csv"
)


# Read the CSV files into DataFrames
localization_data = pd.read_csv(localization_error_path)

# divide the columns
error_distance1 = localization_data["/SR5S1/error_distance1/data"]
error_distance2 = localization_data["/SR5S1/error_distance2/data"]
error_distance3 = localization_data["/SR5S1/error_distance3/data"]
localization_error = localization_data["/SR5S1/location_error/data"]
# drop empty rows

error_distance1 = error_distance1.dropna()
error_distance2 = error_distance2.dropna()
error_distance3 = error_distance3.dropna()
error_localization = localization_error.dropna()

# get absolute values
error_distance1 = error_distance1.abs()
error_distance2 = error_distance2.abs()
error_distance3 = error_distance3.abs()
error_localization = error_localization.abs()

# get min values of each column
min_error_distance1 = error_distance1.min()
min_error_distance2 = error_distance2.min()
min_error_distance3 = error_distance3.min()
min_error_localization = error_localization.min()

# get max values of each column
max_error_distance1 = error_distance1.max()
max_error_distance2 = error_distance2.max()
max_error_distance3 = error_distance3.max()
max_error_localization = error_localization.max()

# get mean values of each column
mean_error_distance1 = error_distance1.mean()
mean_error_distance2 = error_distance2.mean()
mean_error_distance3 = error_distance3.mean()
mean_error_localization = error_localization.mean()

# get std dev values of each column
std_dev_error_distance1 = error_distance1.std()
std_dev_error_distance2 = error_distance2.std()
std_dev_error_distance3 = error_distance3.std()
std_dev_error_localization = error_localization.std()

# get median values of each column
median_error_distance1 = error_distance1.median()
median_error_distance2 = error_distance2.median()
median_error_distance3 = error_distance3.median()
median_error_localization = error_localization.median()

# get mode values of each column
mode_error_distance1 = error_distance1.mode()
mode_error_distance2 = error_distance2.mode()
mode_error_distance3 = error_distance3.mode()
mode_error_localization = error_localization.mode()

# get variance values of each column
variance_error_distance1 = error_distance1.var()
variance_error_distance2 = error_distance2.var()
variance_error_distance3 = error_distance3.var()
variance_error_localization = error_localization.var()

# create a table to store all of the values

# Dictionary to store the summary statistics
summary_statistics = {
    "Statistic": ["Min", "Max", "Mean", "Std Dev", "Median", "Mode", "Variance"],
    "Error Distance 1": [
        min_error_distance1,
        max_error_distance1,
        mean_error_distance1,
        std_dev_error_distance1,
        median_error_distance1,
        mode_error_distance1[0],
        variance_error_distance1,  # Using [0] to select the first mode
    ],
    "Error Distance 2": [
        min_error_distance2,
        max_error_distance2,
        mean_error_distance2,
        std_dev_error_distance2,
        median_error_distance2,
        mode_error_distance2[0],
        variance_error_distance2,
    ],
    "Error Distance 3": [
        min_error_distance3,
        max_error_distance3,
        mean_error_distance3,
        std_dev_error_distance3,
        median_error_distance3,
        mode_error_distance3[0],
        variance_error_distance3,
    ],
    "Localization Error": [
        min_error_localization,
        max_error_localization,
        mean_error_localization,
        std_dev_error_localization,
        median_error_localization,
        mode_error_localization[0],
        variance_error_localization,
    ],
}

# Convert dictionary to DataFrame
summary_df = pd.DataFrame(summary_statistics)

# Optionally, save the DataFrame to a CSV file
summary_df.to_csv(
    "/home/husnu/projects/uwb-data-analysis/20.05.2024/summary_statistics.csv",
    index=False,
)

# Print the DataFrame
print(summary_df)
