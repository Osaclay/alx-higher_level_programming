{
n - Network #1
In this project, we studied how to use the urllib and requests Python libraries to send and receive HTTP messages to URL's. Key part of this project was the use of GET and POST requests, fetching JSON resources, and interacting with API's (the Star Wars API, GitHub API, and Twitter API).
Tasks 📃
•	0. What's my status? #0
o	0-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
o	Uses urllib.
•	1. Response header value #0
o	1-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
o	Usage: ./1-hbtn_header.py <URL>
	Uses urllib.
•	2. POST an email #0
o	2-post_email.py: Python script that sends a POST request to a given URL with a given email, and displays the response body.
o	Usage: ./2-post_email.py <URL> <email>.
	Uses urllib.
•	3. Error code #0
o	3-error_code.py: Python script sends a request to a given URL and displays the response body.
o	Handles HTTP errors.
	Uses urllib.
•	4. What's my status? #1
o	4-hbtn_status.py: Python script that fetches https://intranet.hbtn.io/status.
o	Uses requests.
•	5. Response header value #1
o	5-hbtn_header.py: Python script that displays the X-Request-Id response header variable of a request to a given URL.
o	Usage: ./5-hbtn_header.py <URL>
	Uses requests.
•	6. POST an email #1
o	6-post_email.py: Python script that sends a POST request to a given URL with a given email, and displays the response body.
o	Usage: ./6-post_email.py <URL> <email>.
	Uses requests.
•	7. Error code #1
o	7-error_code.py: Python script sends a request to a given URL and displays the response body.
o	Handles HTTP errors.
	Uses requests.
•	8. Search API
o	8-json_api.py: Python script that sends a POST request to http://0.0.0.0:5000/search_user with a letter passed as parameter.
o	Usage: ./8-json_api.py <letter>
	The letter is sent as the value of the variable q.
	If no letter is given, sets q="".
	If the response body is properly formatted and non-empty, displays it as [<id>] <name>.
o	Uses requests.
•	9. My Github!
o	10-my_github.py: Python script that takes GitHub credentials (username and password) and uses the Github API to display the corresponding ID.
o	Usage: ./10-my_github.py <username> <password>
	Uses requests.
•	10. Time for an interview!
o	100-github_commits.py: Python script that lists the 10 most recent comments of a given GitHub repository using the GitHub API.
o	Usage: ./100-github_commits.py <repository name> <owner name>
	Uses requests.



