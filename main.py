import datetime
import socket

from fastapi import FastAPI, Response
from prometheus_client import CONTENT_TYPE_LATEST, generate_latest

from metrics import get_cpu_metrics, get_disk_metrics, get_memory_metrics
from prometheus_metrics import REGISTRY, update_metrics

app = FastAPI()


@app.get("/health")
def check_health():
    return {"message": "API is running!"}

@app.get("/metrics")
def get_metrics():
    return {
        "hostname": socket.gethostname(),
        "datetime": datetime.datetime.now(datetime.timezone.utc).isoformat(),
        "cpu": get_cpu_metrics(),
        "memory": get_memory_metrics(),
        "disk": get_disk_metrics()
    }

@app.get("/metrics/prometheus")
def prometheus_metrics_endpoint():
    update_metrics()

    return Response(
        content=generate_latest(REGISTRY),
        media_type=CONTENT_TYPE_LATEST,
    )
