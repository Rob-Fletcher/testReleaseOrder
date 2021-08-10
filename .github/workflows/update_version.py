import argparse
import fileinput


def main(args):
    print(f"Got version: {args.version}")
    print(f"Got file: {args.file}")
    args.version = args.version.replace('refs/tags/', '')
    with fileinput.input(args.file, inplace=True) as f:
        for line in f:
            if line.startswith("__version__"):
                print(f'__version__ = "{args.version}"')
            else:
                print(line.rstrip())
        
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--version', '-v', required=True, type=str, help="The version to change this to. Must be semver.")
    parser.add_argument('--file', '-f', required=True, type=str, help="The location of the file with the version in it.")
    args = parser.parse_args()

    main(args)