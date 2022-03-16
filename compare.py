import argparse, pathlib

parser=argparse.ArgumentParser(prog='compare.py', formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=40))
parser.add_argument('-a', '--input1', help='Specify the first file')
parser.add_argument('-b', '--input2', help='Specify the second file')
args=parser.parse_args()

with open(args.input1, 'r+') as f:
    input1 = f.readlines()

with open(args.input2, 'r+') as f:
    input2 = f.readlines()

delta = [item for item in input1 if item not in input2]

with open(f'{pathlib.Path(args.input1).parent}/missing-{pathlib.Path(args.input1).name}.txt', 'x') as f:
    f.seek(0)
    f.write(f"{pathlib.Path(args.input2).name} is missing {len(delta)} packages that were listed in {pathlib.Path(args.input1).name}\n")
    f.write("-----------------------------------------------------------------------------------------------------------\n")
    for item in delta:
        f.write("%s" % item)
    f.truncate()
