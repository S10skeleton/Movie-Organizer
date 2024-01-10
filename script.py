import requests
import time


def get_movie_details(api_key, movie_title):
    url = f"http://www.omdbapi.com/?t={movie_title}&plot=full&apikey={api_key}"
    response = requests.get(url)
    data = response.json()
    plot = data.get('Plot', 'Plot Not Found')
    year = data.get('Year', 'Year Not Found')
    return plot, year

def escape_string(value):
    """ Escape single quotes in SQL values """
    return value.replace("'", "''")

def main():
    time.sleep(1)
    api_key = 'c0f1a8bb'
    with open('movies.txt', 'r') as file:
        movie_titles = [line.strip() for line in file]

    with open('seeds.sql', 'w') as sql_file:  # Open file in write mode
        for title in movie_titles:
            plot, year = get_movie_details(api_key, title)
            title_escaped = escape_string(title)
            plot_escaped = escape_string(plot)

            sql_statement = f"INSERT INTO movies (name, year, plot) VALUES ('{title_escaped}', '{year}', '{plot_escaped}');\n"
            sql_file.write(sql_statement)  # Write to file

if __name__ == "__main__":
    main()


