def read_movies(src):
    with open(src) as datafile:
        return datafile.read().splitlines()

def is_duplicate(needle,haystack):
    for movie in haystack:
        if needle.lower() == movie.lower():
            return True
    return False
