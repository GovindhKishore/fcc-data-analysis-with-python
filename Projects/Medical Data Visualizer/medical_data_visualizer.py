import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
df = pd.read_csv('medical_examination.csv')

# 2
bmi = df['weight'] / ((df['height'] / 100) ** 2)
df['overweight'] = bmi.apply(lambda x: 1 if x > 25 else 0)



# 3
df['cholesterol'] = df.cholesterol.apply(lambda x : 0 if x == 1 else 1)
df.gluc = df.gluc.apply(lambda x : 0 if x == 1 else 1)

# 4
def draw_cat_plot():
    # 5
    df_cat = pd.melt(
        df,
        id_vars=['cardio'],
        value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'] # bydefault var_name='variable', value_name='value'
    )



    # 6
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name = 'total')




    # 7

    # 8

    facetGridObject = sns.catplot(data=df_cat, x='variable', y='total', hue='value', col='cardio', kind='bar')
    fig = facetGridObject.figure

    # 9
    fig.savefig('catplot.png')
    return fig


# 10
def draw_heat_map():
    # 11
    # Representing step by step filtered ones as dfi where i = 1, 2, ...
    df1 = df.loc[(df['ap_lo'] <= df['ap_hi'])]
    height_low = df.height.quantile(0.025)
    height_high = df.height.quantile(0.975)
    weight_low = df.weight.quantile(0.025)
    weight_high = df.weight.quantile(0.975)
    df2 = df1.loc[(df1['height'] >= height_low) & (df1['height'] <= height_high)]
    df3 = df2.loc[(df2['weight'] >= weight_low) & (df2['weight'] <= weight_high)]
    df_heat = df3

    # 12
    corr = df_heat.corr()
    print(corr)


    # 13

    mask = pd.DataFrame(True, index=corr.index, columns=corr.columns)
    for i in range(len(corr)):
        for j in range(i):
            mask.iloc[i, j] = False


    # 14
    fig, ax = plt.subplots(figsize=(12, 9))

    # 15
    sns.heatmap(corr, mask = mask, annot = True)
    # 16

    fig.savefig('heatmap.png')
    return fig
draw_heat_map()
draw_heat_map().show()