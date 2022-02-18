FROM tensorflow/tensorflow:2.4.2-gpu

WORKDIR /code

COPY requirements.txt /code

RUN pip install --no-cache-dir -r /code/requirements.txt

COPY sklearn /code/sklearn

COPY keras /code/keras
