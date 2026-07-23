FROM python:3.11-slim

WORKDIR /agenda

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

COPY agenda/requirements.txt /agenda/
RUN pip install --no-cache-dir -r requirements.txt

COPY agenda/ /agenda/

COPY entrypoint.sh /agenda/entrypoint.sh
RUN chmod +x /agenda/entrypoint.sh

EXPOSE 5000

ENTRYPOINT ["/agenda/entrypoint.sh"]
CMD ["python", "main.py"]