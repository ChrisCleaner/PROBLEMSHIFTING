
"""

READ META DATA OF TREATIES INTO DATAFRAME
Created on Sun Sep 12 20:33:58 2021

@author: chris
"""



import pandas as pd
import ast



meta_data = open("Downloads/Meta Data Treaties.txt", "r") #read txt file


#create dictionary, so that it can be converted later
meta_dict = {"Title":[], "Document type":[], "Reference Number":[], "Date":[], "Source":[], "Status":[], "Subject":[], "Meeting":[], "Treaty":[],"Website":[], "Field of application":[], "Abstract":[]}

for line in meta_data: #read each line of txt
    
    line = ast.literal_eval(line) #convert each line to dictionary
    for key in meta_dict: #loop over all the possible data points
        try:
            meta_dict[key].append(line[key]) #add data if found to meta dict
        except:
            meta_dict[key].append("No Data") #write No data if the data was not recovered

meta_df = pd.DataFrame(meta_dict)
meta_df.to_csv("Meta Data Treaties.csv")
print(meta_df)
print("Completed Successfully")
    
    
    