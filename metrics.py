import psutil




def get_cpu_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count(logical=False),
        "cpu_count_logical": psutil.cpu_count(logical=True),
        "load_avg_1m": psutil.getloadavg()[0],
        "load_avg_5m": psutil.getloadavg()[1],
        "load_avg_15m": psutil.getloadavg()[2],
     }


def get_memory_metrics():
    memory = psutil.virtual_memory()
    return {
        "memory_total_mb": round(memory.total/(1024**2),2),
        "memory_available_mb": round(memory.available/(1024**2),2),
        "memory_percent": memory.percent,
    }

def get_disk_metrics():
    disk = psutil.disk_usage('/')
    return {
        "disk_mountpoint": "/",
        "disk_total_mb": round(disk.total/(1024**2),2),
        "disk_free_mb": round(disk.free/(1024**2),2),
        "disk_percent": disk.percent,
    }

