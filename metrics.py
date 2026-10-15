import psutil




def get_cpu_metrics():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "cpu_count": psutil.cpu_count(logical=False),
        "load_avg": psutil.getloadavg(),
     }


def get_memory_metrics():
    memory = psutil.virtual_memory()
    return {
        "memory_total_mb": round(memory.total/(1024**2),2),
        "memory_available_mb": round(memory.available/(1024**2),2),
        "memory_percent": memory.percent,
    }
