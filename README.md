# FastAPI ML Deployment

Here I'm deploying a simple ML model in [Heroku](https://heroku.com/) platform using [FastAPI](https://fastapi.tiangolo.com/).

Deployment Link: [Swagger UI](https://fastapi-ml-demo.herokuapp.com/docs)

# Run

1. Directly running the `app.py` file:
```
py app.py
```
2. Running `app.py` using `uvicorn` CLI:
```
uvicorn app:app --reload --port 5000 --host 127.0.0.1
```

# Snapshots

### Index Page <br>
![Index Page](./images/index.jpg)

### Random String Input <br>
![Random String Input](./images/string.jpg)

### ML Model Request Message <br>
![ML Model Request Message](./images/predict_request.jpg)

### ML Model Response Message <br>
![ML Model Response Message](./images/predict_response.jpg)

The last two images are from the Swagger UI/OpenAPI UI provided by FastAPI.

## Contact Author

Name : Rahul Bordoloi <br>
Website : https://rahulbordoloi.me <br>
Email : rahulbordoloi24@gmail.com <br>

[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://gitHub.com/rahulbordoloi/)