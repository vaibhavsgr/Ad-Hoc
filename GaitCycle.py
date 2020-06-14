import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.linear_model import LinearRegression as lr
from sklearn.model_selection import train_test_split as ttsplit
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error

def preProcessData(df):
    df['Angle'] = df['Unnamed: 0']
    df['Gait Cycle'] = df['Unnamed: 1']
    df['Young_Slow'] = df['Unnamed: 9']
    df['Young_Medium'] = df['Unnamed: 12']
    df['Young_Fast'] = df['Unnamed: 15']
    df['Adult_Slow'] = df['Unnamed: 36']
    df['Adult_Medium'] = df['Unnamed: 39']
    df['Adult_Fast'] = df['Unnamed: 42']


    df = df.drop({'Unnamed: 0', 'Unnamed: 1','Young', 'Unnamed: 3', 'Unnamed: 4',
    'Unnamed: 5', 'Unnamed: 6', 'Unnamed: 7', 'Unnamed: 8', 'Unnamed: 9',
    'Unnamed: 10', 'Unnamed: 11', 'Unnamed: 12', 'Unnamed: 13',
    'Unnamed: 14', 'Unnamed: 15', 'Unnamed: 16', 'Unnamed: 17',
    'Unnamed: 18', 'Unnamed: 19', 'Unnamed: 20', 'Unnamed: 21',
    'Unnamed: 22', 'Unnamed: 23', 'Unnamed: 24', 'Unnamed: 25',
    'Unnamed: 26', 'Unnamed: 27', 'Unnamed: 28', 'Adult', 'Unnamed: 30',
    'Unnamed: 31', 'Unnamed: 32', 'Unnamed: 33', 'Unnamed: 34',
    'Unnamed: 35', 'Unnamed: 36', 'Unnamed: 37', 'Unnamed: 38',
    'Unnamed: 39', 'Unnamed: 40', 'Unnamed: 41', 'Unnamed: 42',
    'Unnamed: 43', 'Unnamed: 44', 'Unnamed: 45', 'Unnamed: 46',
    'Unnamed: 47', 'Unnamed: 48', 'Unnamed: 49', 'Unnamed: 50',
    'Unnamed: 51', 'Unnamed: 52', 'Unnamed: 53', 'Unnamed: 54', 'Unnamed: 55'},axis=1)
    df = df.drop(0,axis=0)

    #Convert the gait cycle (fetched as numeric) to percentage
    df['Gait Cycle'] *= 100
    #df['Gait Cycle'].dtypes

    df_Angle = pd.get_dummies(df['Angle'])
    df = pd.concat([df,df_Angle],axis=1)
    df = df.drop('Angle',axis=1)

    return (df)


def predictGaitCycle(df):

    X = df.drop({'Young_Slow', 'Young_Medium', 'Young_Fast', 'Adult_Slow',
           'Adult_Medium', 'Adult_Fast'},axis=1)
    YS = df['Young_Slow']
    YM = df['Young_Medium']
    YF = df['Young_Fast']
    AS = df['Adult_Slow']
    AM = df['Adult_Medium']
    AF = df['Adult_Fast']
    XYS = pd.concat([X,YM,YF],axis=1)
    XYM = pd.concat([X,YS,YF],axis=1)
    XYF = pd.concat([X,YS,YM],axis=1)
    XAS = pd.concat([X,AM,AF],axis=1)
    XAM = pd.concat([X,AS,AF],axis=1)
    XAF = pd.concat([X,AS,AM],axis=1)
    degree=2

    #young slow regreesion by polynomial method
    X_train,X_test,Y_train,Y_test = ttsplit(X,YS,test_size=0.3)
    poly=PolynomialFeatures(degree)
    printGraph(X_train, X_test, Y_train, Y_test, poly, X)
    x_poly_train=poly.fit_transform(X_train)
    x_poly_test=poly.fit_transform(X_test)
    poly.fit(x_poly_train,Y_train)
    reg=lr()
    reg.fit(x_poly_train, Y_train)
    y_pred=reg.predict(x_poly_test)
    mae=mean_absolute_error(Y_test,y_pred)
    mse=mean_squared_error(Y_test, y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(Y_test,y_pred)
    print(mae,mse,rmse,r2,sep=' ')

    #YOUNG SLOW WALK USING MEDIUM AND FAST WALK  by polynomial
    X_train,X_test,Y_train,Y_test = ttsplit(XYS,YS,test_size=0.3)
    poly=PolynomialFeatures(degree)
    x_poly_train=poly.fit_transform(X_train)
    x_poly_test=poly.fit_transform(X_test)
    poly.fit(x_poly_train,Y_train)
    reg=lr()
    reg.fit(x_poly_train, Y_train)
    y_pred=reg.predict(x_poly_test)
    mae=mean_absolute_error(Y_test,y_pred)
    mse=mean_squared_error(Y_test, y_pred)
    rmse=np.sqrt(mse)
    r2=r2_score(Y_test,y_pred)
    print(mae,mse,rmse,r2,sep=' ')

    return True

def printGraph(X_train, X_test, Y_train, Y_test, poly, X):
    x_poly_train=poly.fit_transform(X_train)
    x_poly_test=poly.fit_transform(X)
    poly.fit(x_poly_train,Y_train)
    reg=lr()
    reg.fit(x_poly_train, Y_train)
    # Prediction on whole dataset of 1414 rows
    y_pred=reg.predict(x_poly_test)

    #Converting the y_pred ndarray to dataframe
    y_pred_df = pd.DataFrame({'Column1': y_pred[0:]})

    # Fetchin rows of Foot Flex/Extension from the predicted dataframe : y_pred_df
    # To fetch for other muscle types, edit the indexes as follows:
    # Ankle Dorsi/Plantarflexion = y_pred_df[709:810]
    #'Foot Flex/Extension' = y_pred_df[1214:1315]
    #'Foot Int/External Rotation' = y_pred_df[1315:1416]
    # 'Hip Ad/Abduction' = y_pred_df[406:507]
    #'Hip Flex/Extension' =  y_pred_df[305:406]
    #'Hip Int/External Rotation' = y_pred_df[507:608]
    # 'Knee Flex/Extension' = y_pred_df[608:709]
    # 'Pelvic Ant/Posterior Tilt' = y_pred_df[2:103]
    # 'Pelvic Int/External Rotation' = y_pred_df[204:305]
    # 'Pelvic Up/Down Obliquity' = y_pred_df[103:204]
    # 'Shank  Ad/Abduction' =  y_pred_df[1113:1214]
    # 'Shank  Flex/Extension' = y_pred_df[1012:1112]
    # 'Thigh Ad/Abduction' = y_pred_df[911:1012]
    #'Thigh Flex/Extension' = y_pred_df[810:911]

    x_axis_pred = y_pred_df[1214:1315]

    #Creating new dataframe for x_axis and y_axis - Young Slow
    # Replace 'Foot Flex/Extension' with any of the following names
     # 'Ankle Dorsi/Plantarflexion', 'Foot Flex/Extension',	'Foot Int/External Rotation'
     # 'Hip Ad/Abduction', 'Hip Flex/Extension', 'Hip Int/External Rotation',
     # 'Knee Flex/Extension', 'Pelvic Ant/Posterior Tilt', 'Pelvic Int/External Rotation',
     # 'Pelvic Up/Down Obliquity', 'Shank  Ad/Abduction', 'Shank  Flex/Extension',
     # 'Thigh Ad/Abduction', 'Thigh Flex/Extension'


    x_axis = df.loc[df['Foot Flex/Extension'] == 1, ['Gait Cycle']]
    y_axis_ys = df.loc[df['Foot Flex/Extension'] == 1, ['Young_Slow']]
    y_axis_ym = df.loc[df['Foot Flex/Extension'] == 1, ['Young_Medium']]
    y_axis_yf = df.loc[df['Foot Flex/Extension'] == 1, ['Young_Fast']]
    y_axis_as = df.loc[df['Foot Flex/Extension'] == 1, ['Adult_Slow']]
    y_axis_am = df.loc[df['Foot Flex/Extension'] == 1, ['Adult_Medium']]
    y_axis_af = df.loc[df['Foot Flex/Extension'] == 1, ['Adult_Fast']]

    #Inserting predicted value column next to the original gait value column in x_axis df
    x_axis.insert(1, "Pred", x_axis_pred)
    x_axis.fillna(method='bfill')

    #Plotting Young Slow
    plt.plot(x_axis['Gait Cycle'],y_axis_ys, 'b-')
    plt.plot(x_axis['Pred'],y_axis_ys, 'r-')
    plt.show()

    #Plotting Young Medium
    plt.plot(x_axis['Gait Cycle'],y_axis_ym, 'b-')
    plt.plot(x_axis['Pred'],y_axis_ym, 'r-')
    plt.show()

    #Plotting Young  Fast
    plt.plot(x_axis['Gait Cycle'],y_axis_yf, 'b-')
    plt.plot(x_axis['Pred'],y_axis_yf, 'r-')
    plt.show()

    #Plotting Adult Slow
    plt.plot(x_axis['Gait Cycle'],y_axis_as, 'b-')
    plt.plot(x_axis['Pred'],y_axis_as, 'r-')
    plt.show()

    #Plotting Adult Medium
    plt.plot(x_axis['Gait Cycle'],y_axis_am, 'b-')
    plt.plot(x_axis['Pred'],y_axis_am, 'r-')
    plt.show()

    #Plotting Adult Fast
    plt.plot(x_axis['Gait Cycle'],y_axis_af, 'b-')
    plt.plot(x_axis['Pred'],y_axis_af, 'r-')
    plt.show()

    plt.show()

    return True






if __name__ == "__main__":
    df = pd.read_excel('FSN.xls',1)

    df = preProcessData(df)
    predictGaitCycle(df)
