"""
flatten_json_spark.py
~~~~~~~~~~
This Python module explodes a json file from nested to a flat structure.

This python script can be executed as follows,
    $SPARK_HOME/bin/spark-submit \
    --master local[*] \
    --py-files dependencies.zip \
    --files etl_config.json \
    etl_job.py
"""
# imports from Python Standard Library
from os import listdir, path
from json import loads


# imports downloaded from spark
from pyspark import SparkFiles
from pyspark.sql import SparkSession
from pyspark.sql.types import *
from dependencies.logging import Log4j


def main():
    """ Main script

    :return: None
    """
    # start Spark application and get Spark session, logger and config
    spark, app_log = start_spark(
        app_name='flatten_json_spark')

    # log that main ETL job is starting
    app_log.warn('flatten_json_data job is up-and-running')

    """execute the pipeline here
        1. Read Json Data as spark DataFrame
        2. Flatten the DataFrame
        3. Load the flattened DataFrame to a database
    """
    # Read the json data
    input_df = json_to_df(spark)
    input_df.show()
    input_df.printSchema()

    # explode the json data
    # flat_df = flatten_all(input_df).show()
    flat_df = input_df.select(flatten(input_df.schema))
    flat_df.show()
    flat_df.printSchema()

    flat_df1 = flat_df.select(flat_df.aliases[0].alias("aliases.0"),
                              flat_df.aliases[1].alias("aliases.1"),
                              "name",
                              "height_in",
                              "weight_lb",
                              "wood_chucked_lbs"
                              )
    flat_df1.show()
    flat_df1.printSchema()

    # load the data to Nosql or RDBMS
    # load_data(flat_df)

    # log the success and terminate Spark application
    app_log.warn('test_etl_job is finished')
    # stop the spark context
    spark.stop()

    return None


def json_to_df(spark):
    """ turning JSON strings into DataFrames

    :param spark: Spark session object.
    :return:
    """
    input_file = "file:///Users/gangadharkadam/PycharmProjects/parse-json-data/woodchuk.json"
    df = spark\
        .read\
        .option("multiLine", "true")\
        .json(input_file)
    return df


def flatten(schema, prefix=None):
    """Flatten the spark DataFrame
    The recursive function should return an Array[Column].
    Every time the function hits a StructType,
    it would call itself and append the returned Array[Column] to its own Array[Column].

    :param schema: schema of the DataFrame tot flatten
    :param prefix: prefix
    :return: Array of fields
    """
    fields = []

    for field in schema.fields:
        name = prefix + '.' + field.name if prefix else field.name
        dtype = field.dataType
        if isinstance(dtype, ArrayType):
            dtype = dtype.elementType

        if isinstance(dtype, StructType):
            fields += flatten(dtype, prefix=name)

        else:
            fields.append(name)

    return fields


def start_spark(app_name='flatten_json_spark',
                master='local[*]',
                jar_packages=None,
                files=None,
                spark_config=None):
    """Start Spark session, get the Spark logger and load config files.

    :param app_name: Name of the Spark.
    :param master: cluster connection details.
    :param jar_packages: List of Spark JAR package names.
    :param files: List of files to send to Spark cluster (master and workers).
    :param spark_config: Dictionary of config key-value pairs
    :return:A tuple of references to the Spark session, logger and
    config dict (only if available).
    """
    if spark_config is None:
        spark_config = {}

    if jar_packages is None:
        jar_packages = []

    if files is None:
        files = []

    if __name__ == '__main__':
        # get Spark session factory
        spark_builder = (
            SparkSession.builder.appName(app_name))
    else:
        # get Spark session factory
        spark_builder = (
            SparkSession.builder.appName(app_name).master(master))

        # create Spark JAR packages string
        spark_jars_packages = ','.join(list(jar_packages))
        spark_builder.config('spark.jars.packages', spark_jars_packages)

        # create file list to send it to master and worker
        spark_files = ','.join(list(files))
        spark_builder.config('spark.files', spark_files)

        # add config parameters if any
        for key, val in spark_config.items():
            spark_builder.config(key, val)

    # create session and retrieve Spark logger object
    spark = spark_builder.getOrCreate()
    logger = Log4j(spark)

    # get config file if sent to cluster with --files
    spark_files_dir = SparkFiles.getRootDirectory()
    config_files = [filename
                    for filename in listdir(spark_files_dir)
                    if filename.endswith('config.json')
                    ]
    if len(config_files) != 0:
        path_to_config_file = path.join(spark_files_dir, config_files[0])
        with open(path_to_config_file, 'r') as config_file:
            config_json = config_file.read().replace('\n', '')
        config_dict = loads(config_json)
        logger.warn('loaded config from ' + config_files[0])
    else:
        config_dict = None

    # build return tuple conditional on presence of config
    if config_dict is not None:
        return_tup = spark, logger, config_dict
    else:
        return_tup = spark, logger
    return return_tup


# entry point for PySpark application
if __name__ == '__main__':
    main()
