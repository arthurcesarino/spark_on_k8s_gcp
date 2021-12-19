from pyspark.sql import SparkSession
from pyspark import SparkConf
from pyspark.sql.types import DateType, StringType, StructField, StructType, IntegerType, StringType, DateType



if __name__ == '__main__':

    spark = SparkSession \
            .builder \
            .appName('etl_teste_gcp') \
            .enableHiveSupport() \
            .getOrCreate()

    print(SparkConf().getAll())


    spark.sparkContext.setLogLevel('INFO')

    get_drivers_file = 'gs://dp-landing-zone/files/drivers/*.json'

    name_schema = StructType(fields=[
        StructField('forename', StringType(), True),
        StructField('surname', StringType(), True)
    ])

    drivers_schema = StructType(fields=[
        StructField('driverId', IntegerType(), False),
        StructField('driverRef', StringType(), True),
        StructField('number', IntegerType(), True),
        StructField('code', StringType(), True),
        StructField('name', name_schema),
        StructField('dob', DateType(), True),
        StructField('nationality', StringType(), True),
        StructField('url', StringType(), True)
    ])

    df_driver = spark.read \
                .schema(drivers_schema) \
                .json(get_drivers_file)

    df_driver.show()

    spark.stop()