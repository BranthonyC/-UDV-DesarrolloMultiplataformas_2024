FROM python:3.11.8-alpine3.19

ENV PYTHONUNBUFFERED=1

WORKDIR /app

COPY ./Requirements.txt ./
COPY ./entrypoint.sh ./

RUN pip install -r Requirements.txt

COPY ./ ./

# COPY ./entrypoint.sh ./  
# RUN chmod +x entrypoint.sh  
# RUN chmod 777 entrypoint.sh  

# COPY wait-for-it.sh ./

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
