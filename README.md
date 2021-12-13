# Take home project

This project is a test automation challenge.
It contains automated user interface tests for
[this mock online store](http://automationpractice.multiformis.com),
automated web API tests for the test environment of 
[OpenStreetMap](https://master.apis.dev.openstreetmap.org/api/0.6)
and automated load tests for this
[test website](https://jsonplaceholder.typicode.com/). 
It uses Python, Pytest, Pipenv, Playwright, Chrome and Locust.

## Prerequisites

You must have Git, Python and Pipenv installed on your system.
Also, you must have an active account on the test environment of 
[OpenStreetMap](https://master.apis.dev.openstreetmap.org/api/0.6)
web API.

## Getting started

Clone the repository and install the required dependencies with `pipenv install`.

## Running the tests

If running on a terminal, on the directory you cloned the project,
first enter pipenv with `pipenv shell`.

### Running the user interface and web API tests

1. Set up two environment variables (`USERNAME` and `PASSWORD`)
with the username and password for your account on the test environment of 
[OpenStreetMap](https://master.apis.dev.openstreetmap.org/api/0.6)
web API.
2. To execute the tests, run `pytest` (check [pytest's documentation](https://docs.pytest.org/en/6.2.x/usage.html)
for more execution options).
3. To generate an HTML report, run `pytest --html=report.html`.

#### CICD

A `.gitlab-cy.yml` file was added to the project to run the tests on GitLab's CICD
environment, but until now the settings page is not available, what has prevented this
feature to work properly.

### Running the load test
1. Run `locust`.
2. Open up a browser and point it to http://localhost:8089.
3. Click on the `Start swarming` button.

The load test will start creating users and making HTTP requests to simulate a
sudden load on the website. It will try to get posts and comments, create posts
and delete posts on the [jsonplaceholder test website](https://jsonplaceholder.typicode.com/).
It will spawn 50 users per second until it reaches the required 1,000 users.
After running it for 15 seconds, click on the stop button.

The tool will have charts and lists with statistics for the load test.
It will show which requests were made to which endpoints and the response
time for each and also for the total execution.
It will also show failures, if any occur. Some failures might happen on the 
create post test, but this is probably due to a security measure from the website
server that prevents a user from creating many posts in a short amount of time
as this is not a common use case and might represent a potential attack.

Load tests executed during the development of this project identified an
impact on the web application, reducing the response time at the beginning,
but quickly balancing it, probably from an automatic response from the server,
that provided more resources due to the increase in the traffic activity.

Most requests had a response time lower than 1s.

#### Optimal application response time for modern-day web applications

> **Response Times: The 3 Important Limits**
> 
> *by Jakob Nielsen on January 1, 1993*
> 
> **Summary**: There are 3 main time limits (which are determined by human perceptual abilities) to keep in mind when optimizing web and application performance.
> 
> Excerpt from Chapter 5 in my book [Usability Engineering](http://www.nngroup.com/books/usability-engineering/), from 1993:
> 
> The basic advice regarding response times has been about the same for thirty years [Miller 1968; Card et al. 1991]:
>
> - **0.1 second** is about the limit for having the user feel that the system is reacting instantaneously, meaning that no special feedback is necessary except to display the result.
> - **1.0 second** is about the limit for the user's flow of thought to stay uninterrupted, even though the user will notice the delay. Normally, no special feedback is necessary during delays of more than 0.1 but less than 1.0 second, but the user does lose the feeling of operating directly on the data.
> - **10 seconds** is about the limit for keeping the user's attention focused on the dialogue. For longer delays, users will want to perform other tasks while waiting for the computer to finish, so they should be given feedback indicating when the computer expects to be done. Feedback during the delay is especially important if the response time is likely to be highly variable, since users will then not know what to expect.

## Built With

* [Python](https://www.python.org/) - Programming language
* [pytest](https://docs.pytest.org/) - Test automation framework
* [pytest-html](https://pypi.org/project/pytest-html/) - pytest plugin for generating HTML reports
* [Pipenv](https://pypi.org/project/pipenv/) - Dependency and virtual environment manager
* [Playwright](https://playwright.dev/) - Browser automation tool
* [Locust](https://locust.io/) - Load test tool
