import a2s
import json
import os

# IP и основной порт для каждого сервера
SERVERS = [
    ("95.165.129.226", 7777),
    ("45.138.25.18", 7777),
    # Добавь сюда ещё сервера, если нужно
]

def query_server(ip, port):
    try:
        info = a2s.info((ip, port), timeout=2.0)
        return {
            "name": info.server_name,
            "map": info.map_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "ip": ip,
            "port": port
        }
    except Exception as e:
        print(f"[!] Failed {ip}:{port} — {e}")
        return None

def main():
    print("🔄 Получаем список серверов...")

    results = []
    for ip, port in SERVERS:
        print(f"⚙️  Querying {ip}:{port}...")
        data = query_server(ip, port)
        if data:
            results.append(data)

    # Убедимся, что директория существует
    os.makedirs("data", exist_ok=True)

    # Сохраняем в data/servers.json
    with open("data/servers.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"✅ Обновлено: {len(results)} сервер(ов) найдено.")

if __name__ == "__main__":
    main()
