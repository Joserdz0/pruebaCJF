from pyspark.sql import SparkSession
from pyspark.ml.evaluation import RegressionEvaluator
from pyspark.ml.recommendation import ALS
from pyspark.sql import Row

# Iniciar sesión en Spark
spark = SparkSession.builder.appName('recommender').getOrCreate()

# Cargar los datos (asegúrate de tener el archivo 'ratings.csv' en tu directorio)
data = spark.read.csv('ratings.csv', inferSchema=True, header=True)

# Convertir las columnas al formato correcto
data = data.select(data['userId'].cast('int'), data['movieId'].cast('int'), data['rating'].cast('float'))

# Crear un objeto ALS y establecer los parámetros
als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")

# Ajustar el modelo ALS al conjunto de datos
model = als.fit(data)

# Crear un evaluador para medir el error cuadrático medio
evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")

# Realizar predicciones y evaluar el modelo
predictions = model.transform(data)
rmse = evaluator.evaluate(predictions)

# Imprimir el error cuadrático medio
print("Root-mean-square error = " + str(rmse))

# Generar las 10 mejores recomendaciones de películas para cada usuario
userRecs = model.recommendForAllUsers(10)
userRecs.show()