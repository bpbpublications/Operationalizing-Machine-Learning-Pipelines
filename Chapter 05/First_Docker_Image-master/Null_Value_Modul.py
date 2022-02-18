import pandas as pd
import argparse

parser = argparse.ArgumentParser(
                            description = 'Train Random \
                                            Forest Classifier')
parser.add_argument('--filename', type=str,\
                     help = 'Full path of file to be \
                             processed ')

args = parser.parse_args()

try:
    df_data=pd.read_csv(args.filename)
    df_null_count=pd.DataFrame(df_data.isnull().\
                            sum()).reset_index()

    df_null_count.columns=['Column_Name','Null_Val_Count']

    df_null_count.to_csv('null_value_report.csv',index=False)
    print ("Process Complete")
except:
    print ("File is not readable by Pandas")
    
