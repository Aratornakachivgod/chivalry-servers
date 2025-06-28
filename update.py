import json
import a2s
import socket

SERVERS = [
    ("95.165.129.226", 7777),
    ("45.138.25.18", 7777),
    # ...
]

def query_server(ip, port):
    try:
        print(f"Querying {ip}:{port}...")
        info = a2s.query_info((ip, port), timeout=2.0)
        return {
            "ip": ip,
            "port": port,
            "name": info.server_name,
            "map": info.map_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "region": guess_region(ip),
        }
    except Exception as e:
        print(f"[!] Failed {ip}:{port} — {e}")
        return None

def guess_region(ip):
    # как у тебя было
    ...

def main():
    result = []
    for ip, port in SERVERS:
        data = query_server(ip, port)
        if data:
            result.append(data)

    with open("data/servers.json", "w", encoding="utf-8") as f:
        json.dump(result, f, ensure_ascii=False, indent=2)

    print(f"✅ Updated {len(result)} servers")

if __name__ == "__main__":
    main()

