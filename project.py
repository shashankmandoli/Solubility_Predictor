import pandas as pd

# load data
url = "https://raw.githubusercontent.com/dataprofessor/data/refs/heads/master/delaney_solubility_with_descriptors.csv"
df = pd.read_csv(url)

# data preparation
y = df['logS']
x = df.drop('logS',axis=1)
print(df)

# Data Spliting
from sklearn.model_selection import train_test_split

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=100)
print(x_train)
print(x_test)