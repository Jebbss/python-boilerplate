import argparse


def setup_argparse():
    argparser = argparse.ArgumentParser(description='Description of project and program CLI')

    argparser.add_argument('required_arg',
                           type=str,
                           help='this is a required argument')

    argparser.add_argument('--optional_arg',
                           type=int,
                           default=1,
                           help='optional arg with default value')
    return argparser


if __name__ == "__main__":
    parser = setup_argparse()
    args = parser.parse_args()
    required_arg = args.required_arg
    optional_arg = args.optional_arg
