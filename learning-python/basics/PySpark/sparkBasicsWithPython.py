from pyspark.sql import SparkSession

spark = SparkSession \
.builder \
.appName("Datacamp Pyspark Tutorial") \
.config("spark.memory.offHeap.enabled","true") \
.config("spark.memory.offHeap.size","10g") \
.getOrCreate()

df = spark.range(1,10)
df.show(100)






