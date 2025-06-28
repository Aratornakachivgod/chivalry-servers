import json
import a2s
from datetime import datetime

SERVERS = [
    ("134.119.187.18", 11729),
    ("185.107.96.212", 7777),
    ("65.109.87.226", 17833),
    ("208.115.196.100", 7004),
    ("65.109.87.226", 17843),
]

results = []

for ip, port in SERVERS:
    try:
        info = a2s.info((ip, port), timeout=2.0)
        results.append({
            "ip": ip,
            "port": port,
            "name": info.server_name,
            "map": info.map_name,
            "players": info.player_count,
            "max_players": info.max_players,
            "game": info.game,
            "updated": datetime.utcnow().isoformat() + "Z"
        })
    except Exception as e:
        results.append({
            "ip": ip,
            "port": port,
            "error": str(e),
            "updated": datetime.utcnow().isoformat() + "Z"
        })

with open("servers.json", "w", encoding="utf-8") as f:
    json.dump(results, f, indent=2, ensure_ascii=False)
