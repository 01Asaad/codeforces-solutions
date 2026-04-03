from argparse import ArgumentParser


def get_parser() :
    parser = ArgumentParser(description='Run a solution')
    parser.add_argument('problem_id', type=str, help='Problem ID')
    parser.add_argument('input_file', type=str, nargs='?', 
                       help='Path to input file (optional, defaults to ./test_cases/{problem_id}.txt)')
    parser.add_argument('--profiler', '-p', action='store_true')
    return parser