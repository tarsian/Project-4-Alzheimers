VectorAssembler
VectorAssembler is a feature transformer provided by Spark MLlib that combines multiple columns into a single vector column. This is essential for preparing data to be used with Spark MLlib's machine learning algorithms, which typically require input data in vector format.

Key Features
Column Combination: Merges multiple input columns into a single output vector column.
Feature Vector Creation: Transforms input data into a single vector that can be used as input for machine learning algorithms
```python
from pyspark.ml.feature import VectorAssembler

# Define the input features
features = ['Age', 'SystolicBP', 'DiastolicBP', 'Cholesterol', 'MaxHeartRate']

# Create a VectorAssembler
assembler = VectorAssembler(inputCols=features, outputCol='features')

# Transform the data
assembled_data = assembler.transform(data)

```
