movies = [  
    {  
        "name": "Usual Suspects",   
        "imdb": 7.0,  
        "category": "Thriller"  
    },  
    {  
        "name": "Hitman",  
        "imdb": 6.3,  
        "category": "Action"  
    },  
    {  
        "name": "Dark Knight",  
        "imdb": 9.0,  
        "category": "Adventure"  
    },  
    {  
        "name": "The Help",  
        "imdb": 8.0,  
        "category": "Drama"  
    },  
    {  
        "name": "The Choice",  
        "imdb": 6.2,  
        "category": "Romance"  
    },  
    {  
        "name": "Colonia",  
        "imdb": 7.4,  
        "category": "Romance"  
    },  
    {  
        "name": "Love",  
        "imdb": 6.0,  
        "category": "Romance"  
    },  
    {  
        "name": "Bride Wars",  
        "imdb": 5.4,  
        "category": "Romance"  
    },  
    {  
        "name": "AlphaJet",  
        "imdb": 3.2,  
        "category": "War"  
    },  
    {  
        "name": "Ringing Crime",  
        "imdb": 4.0,  
        "category": "Crime"  
    },  
    {  
        "name": "Joking muck",  
        "imdb": 7.2,  
        "category": "Comedy"  
    },  
    {  
        "name": "What is the name",  
        "imdb": 9.2,  
        "category": "Suspense"  
    },  
    {  
        "name": "Detective",  
        "imdb": 7.0,  
        "category": "Suspense"  
    },  
    {  
        "name": "Exam",  
        "imdb": 4.2,  
        "category": "Thriller"  
    },  
    {  
        "name": "We Two",  
        "imdb": 7.2,  
        "category": "Romance"  
    }  
]

# Function to check if a single movie's IMDB score is above 5.5  
def is_imdb_above_5_5(movie):  
    """Returns True if the movie's IMDB score is above 5.5, otherwise False."""  
    return movie['imdb'] > 5.5  

# Function to return a sublist of movies with IMDB score above 5.5  
def movies_above_5_5(movies):  
    """Returns a list of movies with an IMDB score above 5.5."""  
    return [movie for movie in movies if is_imdb_above_5_5(movie)]  

# Function to return movies by category  
def movies_by_category(movies, category_name):  
    """Returns a list of movies under the specified category."""  
    return [movie for movie in movies if movie['category'].lower() == category_name.lower()]  

# Function to compute the average IMDB score  
def average_imdb(movies):  
    """Computes the average IMDB score of the provided list of movies."""  
    if not movies:  # Check for empty list  
        return 0  
    total_score = sum(movie['imdb'] for movie in movies)  
    return total_score / len(movies)  

# Function to compute the average IMDB score for a specific category  
def average_imdb_by_category(movies, category_name):  
    """Computes the average IMDB score for movies in the specified category."""  
    category_movies = movies_by_category(movies, category_name)  
    return average_imdb(category_movies)



if __name__ == "__main__":  
    # Test is_imdb_above_5_5 function  
    print(is_imdb_above_5_5(movies[0]))  # Test with "Usual Suspects"  

    # Test movies_above_5_5 function  
    print("Movies with IMDB above 5.5:")  
    print(movies_above_5_5(movies))  

    # Test movies_by_category function  
    print("Romance movies:")  
    print(movies_by_category(movies, "Romance"))  

    # Test average_imdb function  
    print("Average IMDB score of all movies:")  
    print(average_imdb(movies))  

    # Test average_imdb_by_category function for "Romance"  
    print("Average IMDB score in the Romance category:")  
    print(average_imdb_by_category(movies, "Romance"))