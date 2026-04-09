import subprocess
import sys
import time
from pathlib import Path
from io import StringIO

from parser import get_parser
from utils import add_profiler

def run_solution(solution_file, input_file, use_profiler = False):
    with open(input_file, 'r') as f:
        input_data = f.read()
    
    original_stdin = sys.stdin
    original_stdout = sys.stdout
    
    captured_output = StringIO()
    
    sys.stdin = StringIO(input_data)
    sys.stdout = captured_output
    
    solution_globals = {}
    
    with open(solution_file, 'r') as f:
        solution_code = f.read()
    if use_profiler : solution_code = add_profiler(solution_code)
    start_time = time.perf_counter()
    try :
        exec(solution_code, solution_globals)
    except :
        output = captured_output.getvalue()
        print(output)
        raise    
    end_time = time.perf_counter()
    
    execution_time = end_time - start_time
    
    output = captured_output.getvalue()
    
    sys.stdin = original_stdin
    sys.stdout = original_stdout

    return output, execution_time

def main():
    parser = get_parser()
    
    args = parser.parse_args()
    
    # solution_file = Path("./problems") / (args.problem_id + ".py")
    problem_dir = Path("./problemscpp") if args.cpp else Path("./problems")
    matching_files = list(problem_dir.glob(f"{args.problem_id}*"))
    assert matching_files
    solution_file = matching_files[0]
    
    input_file = Path(args.input_file) if args.input_file else Path("./test_cases") / (args.problem_id + ".txt")
    
    assert solution_file.exists() and input_file.exists()
    if args.cpp :
        if not args.skip_compilation :
            start = time.perf_counter()
            subprocess.run(["g++", solution_file, "-o", Path("./cppexe") / args.problem_id], check=True)
            compiled_t = time.perf_counter()
        with open(input_file, "r", encoding="utf-8") as f :
            execstart = time.perf_counter()
            res = subprocess.check_output([Path("./cppexe") / args.problem_id], stdin=f, text=True)
        end = time.perf_counter()
        print(str(res))
        print("-" * 50)
        if not args.skip_compilation : print(f"COMPILATION TIME: {(compiled_t - start) * 1000:.3f} milliseconds")
        print(f"EXECUTION TIME: {(end - execstart) * 1000:.3f} milliseconds")

    else :
        print(f"Running {solution_file} with input from {input_file}")
        print("-" * 50)
        
        output, exec_time = run_solution(solution_file, input_file, use_profiler=args.profiler)
        
        print("OUTPUT:")
        print(output)
        print("-" * 50)
        print(f"EXECUTION TIME: {exec_time:.6f} seconds; {exec_time * 1000:.3f} milliseconds")

if __name__ == "__main__":
    main()