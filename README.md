# Weather and Outfit Recommender
#### Video Demo:(https://www.youtube.com/watch?v=UYDNP33RAd0)
#### Name: Emin
#### Location: Konya, Turkey
#### Description:

My final project for CS50P is a command-line Python application that fetches real-time weather data for a user-specified city and provides practical clothing recommendations. It evaluates the current temperature and weather conditions to suggest what to wear and whether to carry an umbrella.

The inspiration for this project comes directly from my daily life. I live in Konya, Turkey, a city known for its continental climate. Here, we experience sharp temperature fluctuations—not just from day to day, but especially between day and night. It can be very warm in the afternoon and freezing after sunset. Deciding what to wear before leaving the house is a constant challenge. I wanted to build a tool that solves this exact problem by quickly analyzing current conditions and giving a concrete outfit recommendation.

### File Structure and Functionality

The project consists of three main files to maintain a modular and testable architecture:

**1. `project.py`**
This is the core script. The `main` function handles user input, executes the API call to OpenWeatherMap using the `requests` library, and manages potential errors (like invalid city names or network issues). To keep the code clean and testable, I implemented three custom functions:
*   `build_api_url(city, api_key)`: Takes the user's city input, replaces spaces with `%20` for URL encoding, and constructs the API endpoint string. 
*   `recommend_outfit(temp_celsius)`: Evaluates the temperature (as a float) and returns a string with a clothing recommendation. It categorizes the weather into distinct tiers (e.g., below 10°C means a heavy coat, 18-25°C means a t-shirt).
*   `is_umbrella_needed(weather_condition)`: Analyzes the main weather description ("Rain", "Drizzle", "Snow", etc.) and returns a boolean indicating whether an umbrella is required.

**2. `test_project.py`**
This file contains the unit tests for my custom functions, using the `pytest` framework. A key design choice I made was to separate the API request logic from the data evaluation logic. Because of this separation, I was able to test `build_api_url`, `recommend_outfit`, and `is_umbrella_needed` independently without needing to make live network requests or use complex mocking during testing.

**3. `requirements.txt`**
Lists the pip dependencies required to run the project, which are `requests` for the API calls and `pytest` for running the test suite.

### Challenges and Future Plans

During the development process, one of the biggest challenges I faced was setting up the testing environment on Windows. Resolving Python environment path issues and getting `pytest` to run correctly in the terminal taught me a lot about how operating systems handle software dependencies and execution paths. It was a frustrating but highly educational process.

For future improvements, I plan to evolve this project beyond a command-line interface. Since I have a strong interest in GUI development, I would like to use the `CustomTkinter` library to build a modern desktop application for this tool. I also plan to incorporate additional weather metrics, such as wind speed, to make the outfit recommendations even more precise. 

Completing this project and the CS50P course has been incredibly rewarding. Seeing my code connect to the internet, fetch real data, and solve a real-life problem I face in Konya is a proud moment for me.
