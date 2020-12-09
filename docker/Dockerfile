FROM python:3.8-slim
LABEL maintainer  UV <uvwild@gmail.com>

RUN pip install --upgrade pip
RUN pip install tutor-openedx==10.5.2

CMD ["tutor"]
ENTRYPOINT ["/bin/bash", "-c"]
