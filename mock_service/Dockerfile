FROM python:3.13-slim

WORKDIR /app

# Версии синхронизированы с [dependency-groups].mock в pyproject.toml.
RUN pip install --no-cache-dir \
        'fastapi>=0.115.0' \
        'uvicorn[standard]>=0.32.0'

COPY . ./mock_service

EXPOSE 8000

HEALTHCHECK --interval=5s --timeout=3s --start-period=3s --retries=10 \
    CMD python -c "import urllib.request,sys; sys.exit(0 if urllib.request.urlopen('http://127.0.0.1:8000/health', timeout=2).status == 200 else 1)" || exit 1

CMD ["uvicorn", "mock_service.main:app", "--host", "0.0.0.0", "--port", "8000"]
