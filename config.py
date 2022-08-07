from pytrivia import Category, Diffculty

### Keys
api_key = '' # telegram bot api key
group_id = '' # telegram group id

### Database
data_base_name = "gameDataBase.db" # name for database file

### Game info
game_info = """
ℹ Welcome to Trivia Game!
ℹ️ You have to answer questions correctly to get points.
ℹ️ You can use /help to get more information.
"""

### Game config
question_interval = 20 # at what interval do you send a question ( integer )

question_points_hard = 100 # number of points for difficulty: hard questions ( integer )
question_points_medium = 80 # number of points for difficulty: medium questions ( integer )
question_points_easy = 60 # number of points for difficulty: easy questions ( integer )

question_points_time_coef = 1 # coefficient for number of points for time elapsed ( integer )

game_difficulty = None # difficulty of the game ( Diffculty )
                    # None = all questions
                    # Diffculty.Easy = easy questions
                    # Diffculty.Medium = medium questions
                    # Diffculty.Hard = hard questions

game_category = None # category of the game ( Category )
                    # None = all categories
                    # Category.General = general knowledge
                    # Category.Books = questions about books
                    # Category.Film = questions about film
                    # Category.Music = questions about music
                    # Category.Musicals_Theatres = questions about musicals and theatres
                    # Category.Tv = questions about television
                    # Category.Video_Games = questions about video games
                    # Category.Board_Games = questions about board games
                    # Category.Nature = questions about nature
                    # Category.Computers = questions about computers
                    # Category.Maths = questions about mathematics
                    # Category.Mythology = questions about mythology
                    # Category.Sports = questions about sports
                    # Category.Geography = questions about geography
                    # Category.History = questions about history
                    # Category.Politics = questions about politics
                    # Category.Art = questions about art
                    # Category.Celebrities = questions about celebrities
                    # Category.Animals = questions about animals
                    # Category.Vehicles = questions about vehicles
                    # Category.Comics = questions about comics
                    # Category.Gadgets = questions about gadgets
                    # Category.Anime_Manga = questions about anime and manga
                    # Category.Cartoon = questions about cartoon