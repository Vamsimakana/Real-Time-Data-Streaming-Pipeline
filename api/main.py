# api/main.py
from fastapi import FastAPI
import psycopg2
from psycopg2.extras import RealDictCursor

app = FastAPI(title="Streaming Aggregates API")

def get_conn():
    return psycopg2.connect(dbname="events", user="postgres", password="postgres", host="localhost")

@app.get("/aggregates")
def aggregates(limit: int = 100):
    conn = get_conn()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT window_start, window_end, event_type, cnt, avg_value FROM event_aggregates ORDER BY window_start DESC LIMIT %s", (limit,))
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@app.get("/health")
def health():
    return {"status":"ok"}
