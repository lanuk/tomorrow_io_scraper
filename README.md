### Overview:

This container pings TomorrowIO to pull historical (past 24 hours) and forecast (next 5 days) weather metrics for 10 selected locations. The container, once running, will pull these metrics at the beginning of each hour.

### Stack:

For the Python component, I used Python + Alpine. I chose Alpine as it was the least painful way of pulling in psycopg2, which was required to integrate with Postgres. SQLAlchemy was used as it's pretty agnostic of SQL flavor. It also made building the table more programatic, hopefully reducing the chances of user (aka me) error.

I used the datascience Jupyter image to bring in packages such as pandas and sqlalchemy to help simplify the connection and querying process.

### How to Run:

Before running, create a file called .env in the root folder (where docker-compose.yml is found). In the .env file, create a variable API_KEY and set it equal to your tomorrow.io api key, and then save the file:

```
API_KEY = "your_api_key_here"
```


Run the entire application:
```bash
docker compose up --build
```

Run only the scraper:
```bash
docker-compose start pythonapp
```

Run only the notebook:
```bash
docker-compose start jupyter

```
Then navigate to http://127.0.0.1:8888/ from a browser. Open Notebook.ipynb, found in the work folder.