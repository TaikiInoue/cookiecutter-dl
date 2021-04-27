FROM taikiinoue45/mvtec:base
ENV DEBIAN_FRONTEND=noninteractive \
    LC_ALL=C.UTF-8 \
    LANG=C.UTF-8 \
    PYTHONPATH=/app/{{cookiecutter.upper_project_name}}:$PYTHONPATH
WORKDIR /app/{{cookiecutter.upper_project_name}}
COPY . .
