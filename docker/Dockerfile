FROM python:3.8-slim
LABEL maintainer  UV <uvwild@gmail.com>

# As per https://github.com/docker/compose/issues/3918
COPY --from=library/docker:19.03 /usr/local/bin/docker /usr/bin/docker
COPY --from=docker/compose:1.24.0 /usr/local/bin/docker-compose /usr/bin/docker-compose

RUN pip install --upgrade pip
RUN pip install tutor-openedx==11.0.2
RUN mkdir /opt/tutor
ENV TUTOR_ROOT /opt/tutor

EXPOSE 80
EXPOSE 443

CMD ["tutor"]
ENTRYPOINT ["/bin/bash", "-c"]
