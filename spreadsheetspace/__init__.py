import pandas as pd


def table_to_content(table_url):
    df = pd.read_csv(table_url)
    content = []
    header = df.columns
    for row in df.rows:
        r = []
        for h in header:
            r.append(row[h])
        content.append(r)
    return content
