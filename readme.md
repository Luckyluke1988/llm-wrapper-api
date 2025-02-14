**Build Docker Container** 

`docker build -t llm-wrapper-api .`

**Run Docker Container**

`docker run -d --name fastapi-zero-shot -p 8000:8000 llm-wrapper-api`