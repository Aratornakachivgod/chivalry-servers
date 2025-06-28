import a2s
import json
import os

SERVERS = [
    ("95.165.129.226", 7777),
    ("45.138.25.18", 7777),
    # добавь сюда свои сервера, если нужно
]

def query_server(ip, port):
    try:
        info = a2s.info((ip, port), timeout=2.0)
        return {
            "ip": ip,
            "port": port,
            "name": info.server_name,
            "map": info.map_name,
            "players": f"{info.player_count}/{info.max_players}",
        }
    except Exception as e:
        print(f"[!] Failed {ip}:{port} — {e}")
        return {
            "ip": ip,
            "port": port,
            "error": str(e),
        }

def main():
    results = [query_server(ip, port) for ip, port in SERVERS]
    os.makedirs("data", exist_ok=True)
    with open("data/servers.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    main()
