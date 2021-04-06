import pandas as pd
import numpy as np
df = pd.read_excel('Datensatz/Hausarbeit_Datensatz_COVID19_LK_v0.5.xlsx')
row = 0
while(row < len(df['LOINC CODE'])):
    #marital
    if(str(df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')]) == 'M'):
        df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')] = 87915002
    if(str(df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')]) == 'S'):
        df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')] = 125681006
    if(np.isnan(df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')])):
        df.loc[row, ('SCTID:365581002 | Finding of marital or partnership status (finding)')] = 160504008
    #race
    if(str(df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')]) == 'asian'):
        df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')] = 315280000
    if(str(df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')]) == 'black'):
        df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')] = 315240009
    if(str(df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')]) == 'native'):
        df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')] = 66920001
    if(str(df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')]) == 'white'):
        df.loc[row, ('SCTID:372148003 | Ethnic group (ethnic group)')] = 185984009
    #gender
    if(str(df.loc[row, ('SCTID:365873007 | Gender finding (finding)')]) == 'F'):
        df.loc[row, ('SCTID:365873007 | Gender finding (finding)')] = 703118005
    if(str(df.loc[row, ('SCTID:365873007 | Gender finding (finding)')]) == 'M'):
        df.loc[row, ('SCTID:365873007 | Gender finding (finding)')] = 703117000
    
    #loinc code
    current_loinc = str(df.loc[row, ('LOINC CODE')])
    if('L' in current_loinc):
        df.loc[row, ('LOINC CODE')] = np.nan
        if(current_loinc == 'DALY'):
            df.loc[row, ('SCTID:273249006 | Assessment scales (assessment scale)')] = 273249006
        if(current_loinc == 'QALY'):
            df.loc[row, ('SCTID:273249006 | Assessment scales (assessment scale)')] = 273724008
        if(current_loinc == 'QOLS'):
            df.loc[row, ('SCTID:273249006 | Assessment scales (assessment scale)')] = 273725009
    row+=1
df.to_excel('Datensatz/Hausarbeit_Datensatz_COVID19_LK_v1.xlsx')
