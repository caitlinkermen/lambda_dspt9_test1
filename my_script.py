#from lambdata_caitlinkermen.my_mod import enlarge

#print("Hello")
#print(enlarge(8))

from lambdata_caitlinkermen.helper_functions import null_count, split_dates
import pandas as pd 
import numpy as np 
df = pd.DataFrame([np.NaN,1,5,7,0])

print(null_count(df))

dates = pd.Series(['1993/01/20','1990/12/08'])

print(split_dates(dates))
