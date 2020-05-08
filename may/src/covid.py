import matplotlib.pyplot as plt


import argparse
import sys
import urllib.request as req

def fetch_url(url, fname):
    """
    Save a url to a local file.
    """
    fin = req.urlopen(url)
    data = fin.read()
    with open(fname, mode='wb') as fout:
        fout.write(data)
    # upon unindent file is closed


def read_csv(fname):
    #import pdb; pdb.set_trace()
    with open(fname, encoding='utf8') as fin:
        rows = []
        for i, line in enumerate(fin):
            values = line.strip().split(',')
            if i == 0:
                #print(values, rows)
                headers = values
            else:
                for j, val in enumerate(values):
                    try:
                        val = int(val)
                    except ValueError:
                        pass
                    else:
                        values[j] = val
                rows.append(dict(zip(headers, values)))
    return rows


def filter(rows, state):
    res = []
    for row in rows:
        if row['state'] == state:
            res.append(row)
    return res

def sortby(rows, col_name):
    def get_col_name(row):
        return row[col_name]
    return sorted(rows, key=get_col_name)

def get_value(rows, col_name):
    res = []
    for row in rows:
        res.append(row[col_name])
    return res

def plot_state(state, csvname, plotname):
    res = read_csv(csvname)
    state_res = filter(res, state)
    state_res = sortby(state_res, 'date')
    fig, ax = plt.subplots()
    ax.plot(get_value(state_res, 'death'))
    ax.plot(get_value(state_res, 'positive'))
    ax.plot(get_value(state_res, 'hospitalized'))
    fig.savefig(plotname)


def main(args):
    ap = argparse.ArgumentParser()
    ap.add_argument('-s', '--state')
    ap.add_argument('-c', '--csv')
    ap.add_argument('-o', '--output',
                    help='PNG filename')
    opt = ap.parse_args(args)
    if opt.state:
        plot_state(opt.state, opt.csv, opt.output)


if __name__ == '__main__':
    main(sys.argv[1:])
