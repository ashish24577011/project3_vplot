import pandas as pd

input_file = "data/mapped.bed"
output_file = "coordinates_output_with_frequency.tsv"


df = pd.read_csv(input_file, sep='\t', header=None)

df.columns = [
    "Field1", "Chromosome1", "Start1", "End1", "Sequence", "Score", "Strand1", 
    "Chromosome2", "Start2", "End2", "FileInfo", "Length", "Strand2"
]

df['x_coordinate'] = ((df['Start2'] + df['End2']) / 2) - ((df['Start1'] + df['End1']) / 2) 
df['y_coordinate'] = df['Length']

df_frequency = df.groupby(['x_coordinate', 'y_coordinate']).size().reset_index(name='frequency')


df_frequency.to_csv(output_file, sep='\t', header=False, index=False)

