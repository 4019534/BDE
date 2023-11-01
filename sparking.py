from pyspark.sql import SparkSession
from pyspark.sql.functions import when

# Initialize a Spark session
spark = SparkSession.builder.appName("Filter CSV").getOrCreate()

#read in the csv files 
hotels = spark.read.csv("hdfs://172.19.0.2:9000/hotels_latlong.csv", header=True, inferSchema=True)
rests = spark.read.csv("hdfs://172.19.0.2:9000/improved_restaurants.csv", header=True, inferSchema=True)

#configure columns using left join to merge address and address_x 
joinDF = hotels.join(rests, hotels['address'] == rests['address_x'], 'left')
#Add rests columns for restaurants
joinDF = joinDF.withColumn("rests", when(joinDF['restname'].isNotNull(), joinDF['restname']).otherwise(''))

#Include all relevant columns for the final csv
hotels_rests = joinDF.select("name","url","address","airport","distance","unit","rating","lat","long","rests")

#look only for hotels with restaurants
fourStarhotels = hotels_rests.filter(hotels_rests['rests'] != "")
#look only for hotels that are 4 star with restaurants
fourStarhotels = fourStarhotels.filter(fourStarhotels["rating"] == "4.0")

#save thse hotels in a new csv file and write it to hdfs
fourStarhotels.write.csv("hdfs://172.19.0.2:9000/onlyhotels_rests.csv", header=True, mode="overwrite")
#display 10 rows on screen when using spark-submit
fourStarhotels.show(10)
# Stop the Spark session
spark.stop()
