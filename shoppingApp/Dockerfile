FROM python:3
#non empty value ensures that the python output is sent straight to terminal (e.g.container log) without being first buffered
ENV PYTHONUNBUFFERED=1
WORKDIR ./ProductCatCode
COPY requirements.txt /ProductCatCode/
RUN pip install -r requirements.txt
COPY . /ProductCatCode/