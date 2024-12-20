import pandas as pd
import pysparql_anything as sa


def preprocess_csv(input_csv, output_csv):
    df = pd.read_csv(input_csv)

    df = df.iloc[:, 1:]
    df.insert(0, 'id', range(1, len(df) + 1))

    df.to_csv(output_csv, index=False)
    print(f"CSV preprocessato e salvato in: {output_csv}")


def main():
    input_csv = '../data/ModCorr.csv'
    processed_csv = '../data/processed.csv'
    query_file = '../queries/publisher.sparql'
    output_file = '../output/publisher.ttl'

    preprocess_csv(input_csv, processed_csv)
    engine = sa.SparqlAnything()

    try:
        engine.run(query=query_file, output=output_file, format='ttl')
        print(f'File di output creato con successo: {output_file}')
    except Exception as e:
        print(f'Errore durante l\'esecuzione: {e}')

if __name__ == "__main__":
    main()
