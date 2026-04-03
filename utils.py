def add_profiler(code : str) :
    start = """
import cProfile
import pstats
profiler = cProfile.Profile()
profiler.enable()
"""
    end = """
profiler.disable()
stats = pstats.Stats(profiler)
stats.sort_stats('cumulative')
stats.print_stats(10)
"""
    return start + code + end