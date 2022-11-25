FROM python:3.10


WORKDIR /online_inference
COPY setup.py requirements.txt ./
COPY rest_service/ ./rest_service/
RUN pip install .
EXPOSE 8000
ENV URL_TO_MODEL=https://drive.google.com/file/d/1zf5TWzifzDIS8Fl_kN4gunKPW42xJcva/view?usp=share_link


CMD ["/bin/bash", "-c", "cd rest_service;uvicorn main:app --host 0.0.0.0 --port 8000"]
