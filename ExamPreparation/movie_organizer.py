def movie_organizer(*args: tuple) -> str:
    result = ""
    movies = {}
    for arg in args:
        if arg[1] not in movies:
            movies[arg[1]] = []
        movies[arg[1]].append(arg[0])

    for key in movies:
        movies[key].sort()

    print(movies)

    sorted_movies = dict(sorted(movies.items(), key=lambda kvp: (-len(kvp[1]), kvp[0])))

    for genre, movie_list in sorted_movies.items():
        result += f"{genre} - {len(movie_list)}\n"
        for movie in movie_list:
            result += f"* {movie}\n"

    # result = "\n".join(
    #     f"{genre} - {len(movie_list)}\n" + "\n".join(f"* {movie}" for movie in movie_list)
    #     for genre, movie_list in sorted_movies.items()
    # )

    return result
