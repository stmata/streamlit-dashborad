import pandas as pd
# import streamlit as st
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix

path = 'dataset_train.csv'

data = pd.read_csv(path)

class_distribution = data['gpsQuality'].value_counts(normalize=True)
print(class_distribution)
total_rows = data.shape[0]
chunk_size = int(total_rows * 0.01)

chunks = []

for class_label, proportion in class_distribution.items():
    class_rows = data[data['gpsQuality'] == class_label]
    class_chunk_size = int(proportion * chunk_size)
    class_chunk = class_rows.sample(class_chunk_size)
    chunks.append(class_chunk)

result = pd.concat(chunks)
print(result.head(5))
print(f'Shape: {result.shape}')
df = result.drop(result.columns[0], axis=1)
print('-------------')
print(df.head(5))
print(f'Shape: {result.shape}')
df.to_csv('maintenance_dataset_v2.csv', index=[0])
print('CSV saved successfully!')


# # Create the Streamlit dashboard
# st.title(" :red[Tableau de bord - Maintenance Preventive]")
# st.write("#")
# st.write(":orange[Peek at Data]")
# st.write(data.head(200))
# st.write(":orange[Data Dimension]")
# st.write(data.shape)
# st.write(":orange[Data Types]")
# st.write(data.dtypes)
# st.write(":orange[Missing Values]")
# st.write(data.isnull().sum())
# st.write(":orange[Descriptive Stats]")
# st.write(data.describe())
# st.write(":orange[Correlation]")
# st.write(data.corr(numeric_only=True))

# st.write(":orange[Class Distribution]")
# st.write(data.groupby('gpsQuality').size())
# st.write(":orange[Model Evaluation]")
# X = data.values[ : , 1:-1]
# Y = data.values[ : , -1].astype('int')
# X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.3, random_state=5)
# model = KNeighborsClassifier()
# print(Y_train)
# model.fit(X_train, Y_train)
# results = model.score(X_test, Y_test)
# predicted = model.predict(Y_test)
# matrix = confusion_matrix(Y_test, predicted)
# report = classification_report(Y_test, predicted)
# st.write('Accurcy : {results}')
# st.write(":orange[Confusion Matrix]")
# st.write(matrix)
# st.write(":orange[Classification Report]")
# st.write(report)
