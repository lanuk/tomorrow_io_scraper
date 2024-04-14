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
Then navigate to http://127.0.0.1:8888/ from a browser.
Open Notebook.ipynb, found in the work folder.