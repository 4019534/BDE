from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Initialize a Spark session
spark = SparkSession.builder.appName("CSV Merge").getOrCreate()

# Read the first CSV file (file1) into a DataFrame
file1_df = spark.read.csv("hdfs://172.19.0.2:9000/hotels_latlong.csv", header=True, inferSchema=True)
# Read the second CSV file (file2) into a DataFrame
file2_df = spark.read.csv("hdfs://172.19.0.2:9000/improved_restaurants.csv", header=True, inferSchema=True)

# Perform a left join based on the 'address' column
joinDF = file1_df.join(file2_df, file1_df['address'] == file2_df['address_x'], 'left')

# Add a new column 'rests' with restnames where available
joinDF = joinDF.withColumn("rests", when(joinDF['restname'].isNotNull(), joinDF['restname']).otherwise(''))

# Select the desired columns from the resulting DataFrame
hotels_rests = joinDF.select(
    "name",
    "url",
    "address",
    "airport",
    "distance",
    "unit",
    "rating",
    "lat",
    "long",
    "rests"
)

# Save the updated DataFrame to a new CSV file or overwrite the original
hotels_rests.write.csv("hotels_rests.csv", header=True, mode="overwrite")

# Stop the Spark session

# Initialize a Spark session
spark = SparkSession.builder.appName("CSV Merge").getOrCreate()

# Read the CSV file (file1_updated) into a DataFrame
file1_updated_df = spark.read.csv("hotels_rests.csv", header=True, inferSchema=True)

# Filter the DataFrame to exclude rows where 'rests' is empty
filtered_df = file1_updated_df.filter(file1_updated_df['rests'] != "")
filtered_df = filtered_df.filter(filtered_df["rating"] == "4.0")
# Save the filtered DataFrame to a new CSV file
filtered_df.write.csv("hdfs://172.19.0.2:9000/onlyhotels_rests.csv", header=True, mode="overwrite")

filtered_df.show(10)


# Stop the Spark session
spark.stop()
