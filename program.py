from argparse import ArgumentParser


arg = ArgumentParser()
arg.add_argument('files', metavar='files', type=str, nargs=2)
arg.add_argument('--upper', action="store_true")
arg.add_argument('--lines', metavar='ln', default=[0], type=int, nargs=1)
args = arg.parse_args()
ln = args.lines[0]

a_file, b_file = open(args.files[0], 'r').read().split('\n'), open(args.files[1], 'w+')

if args.upper:
    for i in range(len(a_file)):
        a_file[i] = a_file[i].upper()

if ln:
    a_file = a_file[:ln]

b_file.write('\n'.join(a_file))
b_file.close()