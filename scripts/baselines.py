from transformers import pipeline
from os.path import join


if __name__ == '__main__':

    baselines = ['bart-large', 'bart-large-xsum']
    inputs = ['A', 'I', 'C', 'AIC']

    for model in baselines:
        summarizer = pipeline('summarization', model='facebook/' + model)

        for data_subset in inputs:
            with open(join('BioTLDR-Data', 'BioTLDR-' + data_subset, 'test.source'), 'r') as file:
                lines = [line.strip() for line in file.readlines()]
                test_set = [" ".join(line.split()[:500]) for line in lines]

            output = summarizer(test_set[:2], max_length=40)
            generated_summaries = [tldr['summary_text'] for tldr in output]

            output_fname = model + '_' + data_subset.lower() + '_baseline.hypo'
            with open(join('outputs', output_fname), 'wt', encoding="utf-8") as file:
                for tldr in generated_summaries:
                    file.write(tldr + '\n')