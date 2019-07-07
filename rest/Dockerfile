FROM python:3.7
ARG project_dir=/app/
ADD reply.py $project_dir
ADD qiita.json $project_dir
WORKDIR $project_dir
RUN pip install flask
CMD ["python", "reply.py"]
