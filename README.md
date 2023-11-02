# BIG DATA ENGINEERING INDIVIDUAL ASSIGNMENT

#Code

A number of .py sacripts were used to webscrape data from the websites listed in the report. Our sparking.py script uses a SparkSession to write a csv that filter out all hotels that have restaurants and are 4-star and then write it into another csv file that is sent to the Hadoop Distributed File System.

We used scraping.py-scraping5.py to het hotels and accompanying information such as address from our websites. getrests.py - getRests16.py was used to scrape 1000 restaurants at a time. After much processing in Hadoop and PySpark, we used timeshours.py to scrape the operating hours of the restaurants in hotels. sparking.py was used to determine which hotels had restaurants and whre 4-star.

#Hadoop, Docker, and PySpark

Hadoop is set up on an Ubuntu virtual machine. We used a github repository mentioned in our report to set this up on a single machine with three nodes contained in Docker containers. After which, we downloaded Apache spark and used this platform to process our data using sparking.py and then saved and send the results called "only_hotels_rests.csv" into our HDFS to be downloaded so we could scrape the restaurants' operating hours. We then sent that back into our HDFS and used PySpark to display it so we could use the data in our collectData.py script that would use the data inputted, our apis and calculate an estimate of the delivery times for our South African trucks to deliver wine to these hotels. 
