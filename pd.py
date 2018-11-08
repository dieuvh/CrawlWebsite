import pandas as pd
df = pd.DataFrame([[13,13]]*2,columns=list('AB'),index=['A','B'])
pd.DataFrame.to_csv(df,'test.csv')