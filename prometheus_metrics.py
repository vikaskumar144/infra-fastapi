import psutil
from prometheus_client import CollectorRegistry, Gauge

REGISTRY= CollectorRegistry()


cpu_usage=Gauge('infra_cpu_usage_percent', 
                'CPU usage in percent',
                registry=REGISTRY,
                )

memory_usage=Gauge('infra_memory_usage_percent', 
                'Memory usage in percent',
                registry=REGISTRY,
                )

disk_usage= Gauge('infra_disk_usage_percent', 
                'Disk usage in percent for root filesystem',
                registry=REGISTRY,
                )

def update_metrics():
    cpu_usage.set(psutil.cpu_percent(interval=0.1))
    memory = psutil.virtual_memory()
    memory_usage.set(memory.percent)
    disk_usage.set(psutil.disk_usage('/').percent)  # Assuming the root filesystem is '/'