import pandas as pd
import nltk
import json
from os import makedirs
from os.path import join
import argparse


def load_csv_data(csv_fname):
    with open(csv_fname, 'r') as file:
        df = pd.read_csv(file, usecols=['Title', 'TLDR', 'Abstract', 'Introduction', 'Conclusion'])
    return df


def write_json_files(dataframe):
    sections = {
        'A': ['Abstract'],
        'I': ['Introduction'],
        'C': ['Conclusion'],
        'AIC': ['Abstract', 'Introduction', 'Conclusion']
    }

    for key in sections:
        makedirs('BioTLDR-' + key, exist_ok=True)
        with open(join('BioTLDR-' + key, 'test.jsonl'), 'w') as file:
            for index, row in dataframe.iterrows():

                if row[sections[key]].isnull().values.any():
                    continue

                text = " ".join([row[section] for section in sections[key]])
                sentences = nltk.tokenize.sent_tokenize(text)

                json_object = {
                    'paper_id': index,
                    'title': row['Title'],
                    'source': sentences,
                    'target': [row['TLDR'].replace('\n', ' ')]
                }

                json.dump(json_object, file)
                file.write('\n')


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('csv_fname')
    args = parser.parse_args()

    nltk.download('punkt')

    biotldr = load_csv_data(args.csv_fname)
    write_json_files(biotldr)

