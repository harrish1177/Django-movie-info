# Django-movie-info
**Files and Folders in this repository**:</br>
The Django project is created in a virtual environment. The source code of the project is in 'myvirtualenv' folder. </br>
A script to send request to the API is in 'api_request.py' script </br>
A sample API response is in 'api_response.jpg' file </br></br>

**Assumptions**:</br>
A new movie is updated in database every 1 min.</br></br>

**Note**:</br>
Authentication is provided via tokens. These tokens are shared with the systems that use our API by our application admin, and this token must be sent with api request.</br>
Separate thread queries DB every 1 minute and caches the latest movie response, and the movie info in this cache is then sent back as response for every API request. Hence we don't query for every API request we receive.</br>

