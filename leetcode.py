import sys
from utils.solvers import solve_leetcode
from utils.cli import run_testtaker

def solve(text: str):
    lang = sys.argv[1] if len(sys.argv) > 1 else None
    return solve_leetcode(text, lang)

run_testtaker(solve)
