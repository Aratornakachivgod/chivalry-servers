import json
import a2s
import socket

SERVERS = [
    ("95.165.129.226", 7777),
    ("45.138.25.18", 7777),
    ("45.144.155.106", 7777),
    ("185.189.255.40", 7777),
    ("5.252.100.74", 7777),
    ("178.252.2.44", 7777),
    ("185.117.153.196", 7777),
    ("185.189.255.67", 7777),
    ("185.189.255.134", 7777),
    ("45.91.124.132", 7777),
    ("213.183.52.163", 7777),
]

def query_server(ip, port):
    try:
        server_info = a2s.info((ip, port), timeout=2.0)
        return {
            "ip": ip,
            "port": port,
            "name": server_info.server_name,
            "map": server_info.map_name,
            "players": server_info.player_count,
            "max_players": server_info.max_players,
            "region": guess_region(ip),
        }
    except (socket.timeout, OSError):
        return None

def guess_region(ip):
    if ip.startswith("185.") or ip.startswith("178.") or ip.startswith("45.91"):
        return "EU"
    elif ip.startswith("95."):
        return "RU"
    elif ip.startswith("213."):
        return "CIS"
    else:
        return "??"

def main():
    result = []
    for ip, port in SERVERS:
        data = query_server(ip, port)
        if data:
            result.append(data)

    with open("servers.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()

