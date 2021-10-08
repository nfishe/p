from ..utils.parser import parser
from . import preprocessing

if __name__ == "__main__":
    args = parser.parse_args()
    if args.command is None:
        parser.print_help()
    else:
        args.func(args)
