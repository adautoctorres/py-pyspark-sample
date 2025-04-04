from pyspark.sql import SparkSession
from pyspark.sql.types import StructType, StructField, StringType

# Inicializa a SparkSession
spark = SparkSession.builder.appName("PySpark-Sample").config("spark.jars.packages", "com.databricks:spark-xml_2.12:0.15.0").getOrCreate()

# Caminho para o arquivo XML
xml_file_path = "data/nfe.xml"

# Lê o arquivo XML
df = spark.read.format("com.databricks.spark.xml").option("rowTag", "NFe").load(xml_file_path)

# Mostra o esquema do DataFrame
df.printSchema()

# Mostra os dados
df.show()

# Finaliza a SparkSession
spark.stop()