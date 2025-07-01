import os, psutil, numpy as np
from flask import Flask, jsonify, send_file
import matplotlib.pyplot as plt
from io import BytesIO

app = Flask(__name__)

def get_sysinfo():
    return {
        "cpu_percent": psutil.cpu_percent(interval=1),
        "ram_total": psutil.virtual_memory().total // (1024**2),
        "ram_used": psutil.virtual_memory().used // (1024**2),
        "disk_total": psutil.disk_usage('/').total // (1024**3),
        "disk_used": psutil.disk_usage('/').used // (1024**3),
        "process_count": len(psutil.pids()),
        "platform": os.name
    }

@app.route('/system/info')
def api_info():
    return jsonify(get_sysinfo())

@app.route('/system/stats')
def api_stats():
    cpu_data = np.array([psutil.cpu_percent(interval=0.1) for _ in range(20)])
    result = {
        "mean_cpu": float(np.mean(cpu_data)),
        "std_cpu": float(np.std(cpu_data)),
        "max_cpu": float(np.max(cpu_data)),
        "min_cpu": float(np.min(cpu_data)),
        "all": cpu_data.tolist()
    }
    return jsonify(result)

@app.route('/system/plot')
def api_plot():
    cpu_data = np.array([psutil.cpu_percent(interval=0.1) for _ in range(20)])
    plt.figure(figsize=(7,2))
    plt.plot(cpu_data, marker='o')
    plt.title('CPU Usage')
    plt.xlabel('Sample')
    plt.ylabel('CPU %')
    plt.tight_layout()
    img = BytesIO()
    plt.savefig(img, format='png')
    img.seek(0)
    plt.close()
    return send_file(img, mimetype='image/png')

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='System Analyzer')
    parser.add_argument('--cli', action='store_true', help='CLI Systeminfo anzeigen')
    parser.add_argument('--stats', action='store_true', help='CLI Statistik anzeigen')
    parser.add_argument('--api', action='store_true', help='Web API starten')
    args = parser.parse_args()

    if args.cli:
        print("Systeminformationen:")
        for k,v in get_sysinfo().items():
            print(f"{k:>14}: {v}")
    elif args.stats:
        cpu_data = np.array([psutil.cpu_percent(interval=0.1) for _ in range(20)])
        print(f"CPU-Last (20 Samples): {cpu_data}")
        print(f"Durchschnitt: {np.mean(cpu_data):.2f} %, Standardabw.: {np.std(cpu_data):.2f} %")
    elif args.api:
        print("Starte System Analyzer API auf http://127.0.0.1:5000")
        app.run(debug=True)
    else:
        parser.print_help()
