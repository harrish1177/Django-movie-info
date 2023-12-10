# Django-movie-info
Files and Folders in this repository:</br>
The Django project is created in a virtual environment. The source code of the project is in 'myvirtualenv' folder.
A script to send request to the API is in 'api_request.py' script
A sample API response is in 'api_response.jpg' file

Assumptions:
A new movie is updated in database every 1 min.

Note:
Authentication is provided via tokens which must be sent with api request.
Separate thread queries DB every 1 minute and caches the latest movie response, and the movie info in this cache is then sent back as response for every API request. Hence we don't query for every API request we receive.

