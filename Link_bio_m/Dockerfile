FROM python:3.11

WORKDIR /app
COPY . .

ENV VIRTUAL_ENV=/app/.venv_docker
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN $uv venv

RUN pip install --upgrade pip
RUN $uv pip install --no-cache-dir -r requirements.txt
CMD reflex run --env prod --backend-only
