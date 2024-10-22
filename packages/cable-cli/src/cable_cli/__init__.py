from argparse import ArgumentParser

from cable_core import hello


def main():
    parser = get_argument_parser()
    args = parser.parse_args()
    print("Hi", args.name)


def get_argument_parser() -> ArgumentParser:
    parser = ArgumentParser(hello())
    parser.add_argument("name", help="Whom to greet")
    return parser


if __name__ == "__main__":
    main()
