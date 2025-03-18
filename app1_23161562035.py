from collections import deque

def bfs_shortest_path(city_map, start, end):
    # Queue untuk menyimpan jalur yang sedang diproses
    queue = deque([(start, [start])])
    visited = set()

    while queue:
        current_place, path = queue.popleft()
        
        # Jika kita sudah sampai di tujuan, kembalikan jalurnya
        if current_place == end:
            return path
        
        # Tandai tempat sudah dikunjungi
        visited.add(current_place)
        
        # Proses setiap tempat yang terhubung dengan tempat saat ini
        for neighbor in city_map[current_place]:
            if neighbor not in visited:
                queue.append((neighbor, path + [neighbor]))

    # Jika tidak ada jalur yang ditemukan
    return None

# Contoh peta kota
city_map = {
    'Home': ['Mall', 'School'],
    'Mall': ['Gym', 'Hospital'],
    'School': ['Library'],
    'Gym': ['Hospital'],
    'Library': ['Hospital'],
    'Hospital': []
}

# Menemukan rute terpendek dari 'Home' ke 'Hospital'
start = 'Home'
end = 'Hospital'
shortest_path = bfs_shortest_path(city_map, start, end)
print(f"Rute terpendek dari {start} ke {end}: {shortest_path}")
