import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import warnings
import seaborn.objects as so

def kde_plot(data=pd.read_csv('../mtcars.csv')):
    lst = list()
    for i in range(1, 9):
        hp_ = data.loc[data['carb'] == i, "hp"]
        lst.append(hp_)
        sns.distplot(hp_, hist = False, kde = True, label=f"{i}", kde_kws = {'linewidth': 3})
    plt.legend(title='as.factor(carb)')
    plt.show()

if __name__ == '__main__':
    kde_plot()
