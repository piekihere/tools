import matplotlib.pyplot as plt
import pandas as pd
import sys
import argparse



parser = argparse.ArgumentParser(
                    prog='plot.py',
                    description='Use in pipe to plot the data, eg. <sep data> | plot.py',
                    epilog='feel free to modify')

parser.add_argument('-c', '--columns', type=str, help="Columns separated by comma (default <0,1>).",
                    default="0,1", dest="columns", required=True)
parser.add_argument('-s','--separator', type=str, help="Column separator present in input data (default <\\t>).",
                    default="\t", dest="sep")
parser.add_argument('-o','--output', type=str, help="Name of the output .png file (default <output>).",
                    default="output", dest="out_name")
parser.add_argument('-t', '--type', choices=['plot','semilogx'], help="Type of the matplotlib plt (default <plot> ).",
                    default="plot", dest="plt_type")
parser.add_argument('d', '--dpi', type=int, help="Set png dpi (default <300>).", default=300, dest="dpi")

args=parser.parse_args()
#data prep
cols = [int(id) for id in args.columns.split(",")]
data = pd.read_csv(sys.stdin, sep="\t")
data = data.to_numpy()

#simple x-y plot
eval(f'plt.{args.plt_type}(data[:,cols[0]], data[:,cols[1]])')
plt.savefig(args.out_name+".png", dpi = args.dpi)
plt.close()
