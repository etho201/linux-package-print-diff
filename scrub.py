import re, argparse, pathlib

parser=argparse.ArgumentParser(prog='scrub.py', formatter_class=lambda prog: argparse.HelpFormatter(prog,max_help_position=40))
parser.add_argument('-i', '--input', help='Specify the file to scrub')
parser.add_argument('-1', '--scrub1', help='Specify the file to scrub', action='store_true')
parser.add_argument('-2', '--scrub2', help='Specify the file to scrub', action='store_true')
args=parser.parse_args()

with open(args.input, 'r+') as f:
    text = f.read()
    if args.scrub1:
        text = re.sub('\..*\n', '\n', text)
    elif args.scrub2:
        text = re.sub('-\d.*\n', '\n', text)

with open(f'{pathlib.Path(args.input).parent}/scrubbed-{pathlib.Path(args.input).name}', 'x') as f:
    f.seek(0)
    f.write(text)
    f.truncate()