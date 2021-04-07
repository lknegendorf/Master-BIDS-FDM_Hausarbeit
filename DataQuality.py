import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import datetime
df = pd.read_excel('Datensatz/Hausarbeit_Datensatz_COVID19_LK_v1.5.xlsx')
df2 = df[['LOINC CODE', 'LOINC VALUE', 'LOINC UNITS']].dropna()
for actual_code in df2['LOINC CODE'].unique():
    sns.boxplot(x=np.array(df2[df2['LOINC CODE'] == actual_code]['LOINC VALUE'].values, dtype=np.float32))
    plt.savefig('Graphs/'+actual_code+'.png')
    plt.clf()
df3 = df[['SCTID:273249006 | Assessment scales (assessment scale)', 'LOINC VALUE', 'LOINC UNITS']].dropna()
for actual_code in df3['SCTID:273249006 | Assessment scales (assessment scale)'].unique():
    sns.boxplot(x=np.array(df3[df3['SCTID:273249006 | Assessment scales (assessment scale)'] == actual_code]['LOINC VALUE'].values, dtype=np.float32))
    plt.savefig('Graphs/'+str(actual_code)+'.png')
    plt.clf()