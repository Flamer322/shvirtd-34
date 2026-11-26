#!/usr/bin/env python3

import json
import os
import time
from datetime import datetime

PROC = "/proc"
LOG_DIR = "/var/log"


def get_cpu_usage():
    with open(f"{PROC}/stat") as f:
        cpu = list(map(int, f.readline().split()[1:]))

    idle = cpu[3] + cpu[4]
    total = sum(cpu)

    time.sleep(0.5)

    with open(f"{PROC}/stat") as f:
        cpu = list(map(int, f.readline().split()[1:]))

    idle_new = cpu[3] + cpu[4]
    total_new = sum(cpu)

    return round(100 * (1 - (idle_new - idle) / (total_new - total)), 2)


def get_memory():
    memory = {}

    with open(f"{PROC}/meminfo") as f:
        for line in f:
            key, value = line.split(":")
            memory[key] = int(value.strip().split()[0])

    total = memory["MemTotal"]
    available = memory["MemAvailable"]

    return {
        "ram_total_mb": round(total / 1024, 2),
        "ram_used_mb": round((total - available) / 1024, 2),
        "ram_usage_percent": round((total - available) / total * 100, 2)
    }


def collect_metrics():
    return {
        "timestamp": int(time.time()),
        "cpu_usage_percent": get_cpu_usage(),
        "ram": get_memory(),
    }


def main():
    os.makedirs(LOG_DIR, exist_ok=True)

    filename = datetime.now().strftime("%y-%m-%d-awesome-monitoring.log")
    filepath = os.path.join(LOG_DIR, filename)

    metrics = collect_metrics()

    with open(filepath, "a") as f:
        f.write(json.dumps(metrics) + "\n")


if __name__ == "__main__":
    main()
