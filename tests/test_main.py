
from fastapi.testclient import TestClient

from main import app

client = TestClient(app)


def test_health_endpoint():
    response = client.get("/health")

    assert response.status_code == 200
    assert response.json() == {"message": "API is running!"}


def test_metrics_endpoint():
    response = client.get("/metrics")

    assert response.status_code == 200

    data = response.json()

    # Top-level response
    assert "hostname" in data
    assert "datetime" in data
    assert "cpu" in data
    assert "memory" in data
    assert "disk" in data

    # CPU metrics
    assert "cpu_percent" in data["cpu"]
    assert "cpu_count" in data["cpu"]
    assert "load_avg_1m" in data["cpu"]
    assert "load_avg_5m" in data["cpu"]
    assert "load_avg_15m" in data["cpu"]

    # Memory metrics
    assert "memory_total_mb" in data["memory"]
    assert "memory_available_mb" in data["memory"]
    assert "memory_percent" in data["memory"]

    # Disk metrics
    assert "disk_mountpoint" in data["disk"]
    assert "disk_total_mb" in data["disk"]
    assert "disk_free_mb" in data["disk"]
    assert "disk_percent" in data["disk"]
