import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import impute

housing = pd.read_csv("data.csv")




corr_matrix = housing.corr()
# print(corr_matrix)

# print(corr_matrix.MEDV.sort_values(ascending = False)
# MEDV        1.000000
# RM          0.694856
# ZN          0.360445
# B           0.333461
# DIS         0.249929
# CHAS        0.175260
# AGE        -0.376955
# RAD        -0.381626
# CRIM       -0.388305
# NOX        -0.427321
# TAX        -0.468536
# INDUS      -0.483725
# PATRATIO   -0.507787
# LSTAT      -0.737663

housing['RmLstat'] = housing['RM'] / housing['LSTAT']

from sklearn.model_selection import StratifiedShuffleSplit
split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
for train_index, test_index in split.split(housing,housing['CHAS']):
    # print(train_index) -> prints an np.array  
    # print(test_index) -> prints an np.array
    strat_train_set = housing.loc[train_index]
    strat_test_set = housing.loc[test_index]

housing = strat_train_set.copy()



corr_matrix = housing.corr()

# print(corr_matrix.MEDV.sort_values(ascending = False))
# MEDV        1.000000
# RmLstat     0.821292


# plt.scatter(housing.RmLstat, housing.MEDV)
# plt.show()

housing = strat_train_set.drop("MEDV", axis = 1)
housing_labels = strat_train_set["MEDV"].copy()

# Now, we are going to fill all the NA values with median

from sklearn.impute import SimpleImputer

imputer = SimpleImputer(strategy='median')
imputer.fit(housing)
# print(imputer.statistics_) this prints saare columns k median
# [2.8673500e-01 0.0000000e+00 9.9000000e+00 0.0000000e+00 5.3800000e-01
#  6.2135000e+00 7.8200000e+01 3.1222000e+00 5.0000000e+00 3.3700000e+02
#  1.9000000e+01 3.9095500e+02 1.1570000e+01 2.1150000e+01 5.2691526e-01]

X = imputer.transform(housing)


housing_tr = pd.DataFrame(X, columns = housing.columns)

# print(housing_tr.info())

from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
my_pipeline = Pipeline([
    ('imputer',SimpleImputer(strategy="median")),
    #................ you can add as many as you want in your pipeline
    ('std_scaler',StandardScaler())
])

# housing_num_tr  is a numpy array, it is not a dataframe
housing_num_tr = my_pipeline.fit_transform(housing_tr)


from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

# model = LinearRegression()
# model = DecisionTreeRegressor()
model = RandomForestRegressor()

# fit() method takes numpy array as an argument
model.fit(housing_num_tr,housing_labels)

# 1 2 3 4 5 6 7 8 9 10
# 10 group me baat kar, 1 ko neglect kar k model ko check karna usme
from sklearn.model_selection import cross_val_score
scores = cross_val_score(model, housing_num_tr, housing_labels, scoring = "neg_mean_squared_error", cv = 10)
rmse_scores = np.sqrt(-scores)

def printScores(scores):
    print("Scores: ", scores)
    print("Mean: ", scores.mean())
    print("Standard Devaiation: ", scores.std())

printScores(rmse_scores)


from sklearn.metrics import mean_squared_error

X_test = strat_test_set.drop("MEDV", axis = 1)
Y_test = strat_test_set["MEDV"].copy()
X_test_prepared = my_pipeline.transform(X_test)
final_predictions = model.predict(X_test_prepared)
final_mse = mean_squared_error(Y_test, final_predictions)
final_rmse = np.sqrt(final_mse)

print(final_rmse)


