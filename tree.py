#%%
from sklearn import tree

#%%
# [altura, peso, tamanho do sapato]
x = [[181,80,44],[177,70,43],[160,60,38],[154,54,37],[166,65,40],[190,90,47],[175,64,39],[177,70,40],[159,55,37],[171,75,42],[181,85,43]]
y = ['Man','Woman','Woman','Woman','Man','Man','Man','Woman','Woman','Man','Man']

#%% [Classification]
clfc = tree.DecisionTreeClassifier()

#%%
clfc = clfc.fit(x,y)

#%%
print(clfc.predict([[190,90,47]]))
