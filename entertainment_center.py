import media
import fresh_tomatoes

crash = media.Movie('Crash', 'https://www.youtube.com/watch?v=durNwe9pL0E')
troy = media.Movie('Troy', 'https://youtu.be/QpikTTSOHXc')
dark_knight = media.Movie('The Dark Knight', 'https://youtu.be/EXeTwQWrcwY')
iron_man = media.Movie('Iron Man', 'https://youtu.be/8OCJRbzdzaU')
movie_list = [crash, troy, dark_knight, iron_man]



fresh_tomatoes.open_movies_page(movie_list)