import datetime
import socket

from fastapi import FastAPI

from metrics import get_cpu_metrics, get_disk_metrics, get_memory_metrics

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