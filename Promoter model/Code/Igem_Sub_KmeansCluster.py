import pandas as pd

df = pd.read_excel('Data01.xls')
Y = df['Promoter intensity'].values
Y = pd.DataFrame(Y, columns=['Promoter intensity'])

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=9)
y_predicted = kmeans.fit_predict(Y)

# #将intensity对应的cluster作为一列数据，排列在intensity旁边
Y['cluster'] = y_predicted
# 将分类的结果导出
Y.to_csv('K means cluster.csv')

Y = Y['cluster'].values