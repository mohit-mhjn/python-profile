import time

# Cases
# 1. Functions in same file
# 2. Functions from other file
from my_other_file import read_movies, is_duplicate

# Cprofile
# import cProfile, pstats                    #
# from io import StringIO                    # UNCOMMENT THESE LINES FOR CPROFILE
# pr = cProfile.Profile()                    # ACTIVATE PROFILE
# pr.enable()                                #

############################## YOUR CODE STARTS HERE #################################################################

start = time.time()

# Memory Profiler
from memory_profiler import profile

@profile  #>>  Decorator for the target function  >> Uncomment this for memory profile
def find_duplicate_movies(src= 'movie_metadata.txt'):
    movies = read_movies(src)
    movies = [movie.lower() for movie in movies]
    duplicates = []
    while movies:
        this_movie = movies.pop()
        if this_movie in movies:
            duplicates.append(this_movie)
    return duplicates

duplicates = find_duplicate_movies()
print ("Number of Duplicates : ",len(duplicates))

end = time.time()
print("exec_time = ",end-start," sec." )

############################# YOUR CODE ENDS HERE ###########################################################################

# pr.disable()                                            #
# s = StringIO()                                          #
# sortby = 'cumulative'                                   #
# ps = pstats.Stats(pr, stream=s).sort_stats(sortby)      # UNCOMMENT THESE FOR CPROFILE
# ps.print_stats()                                        # END PROFILE
# print(s.getvalue())                                     #
