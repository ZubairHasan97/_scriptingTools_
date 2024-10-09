#import modules
import time #for calculating process runtime
import pandas as pd

initiating = time.process_time()

print('''
#################################################
## FILTER PROTEIN SEQUENCES BY MOLECULAR MASS ###
########### written_by: Zubair Hasan ############
########### python_version: 3.10.12  ############
###########  script_version: 1.0.0   ############
#################################################
''')
#input habdling
file_path = input("Enter file path (e.g. home/content/sequence.csv): ")
weight = int(input("Enter filtering Mass (e.g. 40000): "))
output_file = input("Enter output file name (e.g. output.csv or result.txt):")

#reading CSV file into dataframe
seq_df = pd.read_csv(file_path, sep = '\t')

#defining function for filtering SEQUENCES by MASS
def filter_aaseq_MW(df_obj, weight_filter,output_name):
    #filtering operation
    filtered_df = df_obj.loc[df_obj["Mass"] < weight_filter, "Entry"]
    #output screen and file handling
    print(f"Total Number of Filtered Proteins: {filtered_df.count()}\n")
    print("\nFirst few filtered protein IDs:\n", filtered_df.head())
    filtered_df.to_csv(output_file, index = False)
    time.sleep(2)
    print(f"\n[-------File Exported!! ==>> {output_name}-------]\n")

#datatype handling of the column Mass
#check if Mass column is integer/float/string
if (seq_df["Mass"].dtypes == int) or (seq_df["Mass"].dtypes == float):
    for mass_col in seq_df.columns:
        if mass_col == "Mass" or mass_col == "mass" or mass_col == "MASS":
            print(f"\n[----{mass_col} datatype: int/float || Script executed successfuly----]")
            break
    #invoking the filter function
    filter_aaseq_MW(seq_df, weight, output_file)
else:
    #converting Mass string data into integer
    seq_df["Mass"] = seq_df["Mass"].str.replace(",", "").astype(int)
    for mass_col in seq_df.columns:
        if mass_col == "Mass" or mass_col == "mass" or mass_col == "MASS":
            print(f"\n[----{mass_col} datatype: str || converted into int----]")
            break
    filter_aaseq_MW(seq_df, weight, output_file)


terminating = time.process_time()

print(f"processing_time: {terminating - initiating} ms")
