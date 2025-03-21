import random

def generate_random_stats(level):
    if 1 <= level <= 15:
        # Bagian 1
        hp = random.randint(500, 3000)
        atk = random.randint(100, 2000)
        defense = random.randint(100, 2000)
        spd = random.randint(80, 120)
        stm = random.randrange(50, 201, 10)
        mtx = random.randrange(50, 201, 10)
    elif 16 <= level <= 30:
        # Bagian 2
        hp = random.randint(2000, 5000)
        atk = random.randint(800, 4000)
        defense = random.randint(800, 4000)
        spd = random.randint(80, 120)
        stm = random.randrange(50, 201, 10)
        mtx = random.randrange(50, 201, 10)
    elif 31 <= level <= 45:
        # Bagian 3
        hp = random.randint(4000, 10000)
        atk = random.randint(2000, 6000)
        defense = random.randint(2000, 6000)
        spd = random.randint(100, 180)
        stm = random.randrange(100, 501, 10)
        mtx = random.randrange(100, 501, 10)
    elif 46 <= level <= 60:
        # Bagian 4
        hp = random.randint(8000, 30000)
        atk = random.randint(5000, 15000)
        defense = random.randint(5000, 15000)
        spd = random.randint(120, 300)
        stm = random.randrange(300, 801, 10)
        mtx = random.randrange(300, 801, 10)
    elif 61 <= level <= 70:
        # Bagian 5
        hp = random.randint(15000, 50000)
        atk = random.randint(8000, 30000)
        defense = random.randint(8000, 30000)
        spd = random.randint(200, 400)
        stm = random.randrange(600, 1501, 10)
        mtx = random.randrange(600, 1501, 10)
    elif 71 <= level <= 80:
        # Bagian 6 (Custom)
        hp = random.randint(30000, 70000)
        atk = random.randint(15000, 35000)
        defense = random.randint(15000, 35000)
        spd = random.randint(250, 450)
        stm = random.randrange(800, 2001, 10)
        mtx = random.randrange(800, 2001, 10)
    elif 81 <= level <= 90:
        # Bagian 7 (Custom)
        hp = random.randint(50000, 100000)
        atk = random.randint(20000, 50000)
        defense = random.randint(20000, 50000)
        spd = random.randint(300, 500)
        stm = random.randrange(1000, 2501, 10)
        mtx = random.randrange(1000, 2501, 10)
    elif 91 <= level <= 100:
        # Bagian 8 (Custom)
        hp = random.randint(70000, 150000)
        atk = random.randint(30000, 60000)
        defense = random.randint(30000, 60000)
        spd = random.randint(350, 600)
        stm = random.randrange(1500, 3001, 10)
        mtx = random.randrange(1500, 3001, 10)
    
    return {
        "HP": hp,
        "ATK": atk,
        "DEF": defense,
        "SPD": spd,
        "STM": stm,
        "MTX": mtx
    }

def generate_random_minor_stats(level):
    if 1 <= level <= 10:
        # Bagian 1
        hp = random.randint(50, 200)
        atk = random.randint(5, 30)
        defense = random.randint(10, 30)
        spd = random.randint(20, 80)
        stm = random.randrange(10, 41, 10)
        mtx = random.randrange(10, 41, 10)
    elif 11 <= level <= 20:
        # Bagian 2
        hp = random.randint(200, 400)
        atk = random.randint(15, 40)
        defense = random.randint(15, 40)
        spd = random.randint(20, 80)
        stm = random.randrange(20, 61, 10)
        mtx = random.randrange(20, 61, 10)
    elif 21 <= level <= 30:
        # Bagian 3
        hp = random.randint(300, 800)
        atk = random.randint(30, 60)
        defense = random.randint(30, 60)
        spd = random.randint(60, 100)
        stm = random.randrange(50, 81, 10)
        mtx = random.randrange(50, 81, 10)
    elif 31 <= level <= 40:
        # Bagian 4
        hp = random.randint(500, 1200)
        atk = random.randint(50, 80)
        defense = random.randint(40, 80)
        spd = random.randint(60, 100)
        stm = random.randrange(60, 101, 10)
        mtx = random.randrange(60, 101, 10)
    elif 41 <= level <= 50:
        # Bagian 5
        hp = random.randint(500, 2000)
        atk = random.randint(50, 100)
        defense = random.randint(50, 100)
        spd = random.randint(80, 120)
        stm = random.randrange(80, 121, 10)
        mtx = random.randrange(80, 121, 10)
    elif 51 <= level <= 60:
        # Bagian 6
        hp = random.randint(800, 1200)
        atk = random.randint(60, 100)
        defense = random.randint(60, 100)
        spd = random.randint(80, 120)
        stm = random.randrange(100, 151, 10)
        mtx = random.randrange(100, 151, 10)
    elif 61 <= level <= 70:
        # Bagian 7
        hp = random.randint(1000, 2000)
        atk = random.randint(80, 120)
        defense = random.randint(80, 120)
        spd = random.randint(100, 180)
        stm = random.randrange(120, 201, 10)
        mtx = random.randrange(120, 201, 10)
    elif 71 <= level <= 80:
        # Bagian 8
        hp = random.randint(1250, 2750)
        atk = random.randint(100, 220)
        defense = random.randint(100, 320)
        spd = random.randint(100, 180)
        stm = random.randrange(150, 301, 10)
        mtx = random.randrange(150, 301, 10)
    elif 81 <= level <= 90:
        # Bagian 9
        hp = random.randint(1600, 3000)
        atk = random.randint(150, 300)
        defense = random.randint(150, 300)
        spd = random.randint(120, 200)
        stm = random.randrange(200, 351, 10)
        mtx = random.randrange(200, 351, 10)
    elif 91 <= level <= 100:
        # Bagian 10
        hp = random.randint(1800, 6000)
        atk = random.randint(150, 400)
        defense = random.randint(150, 400)
        spd = random.randint(150, 300)
        stm = random.randrange(250, 401, 10)
        mtx = random.randrange(250, 401, 10)

    return {
        "HP": hp,
        "ATK": atk,
        "DEF": defense,
        "SPD": spd,
        "STM": stm,
        "MTX": mtx
    }

def generate_stats(character_type, level):
    if character_type in ["min", "minlist", "e", "elist"]:
        stats = generate_random_minor_stats(level)
        if character_type in ["e", "elist"]:
            stats["HP"] += level * 20
            stats["ATK"] += level * 2
            stats["DEF"] += level * 2
            stats["SPD"] += level * 1
    else:
        stats = generate_random_stats(level)
    
    return stats

def main():
    print("== Random Stats Generator ==")

    while True:
        character_type = input("Masukkan tipe karakter ['exit' untuk keluar]: ").strip().lower()
        
        if character_type == "exit":
            break
        
        if character_type not in ["min", "std", "e", "minlist", "stdlist", "elist"]:
            print("Pilihan tidak valid, coba lagi.")
            continue
        
        while True:
            try:
                level = input("Masukkan level karakter (1-100): ")
                if level == "exit": break
                level = int(level)

                if not (1 <= level <= 100):
                    print("Level harus antara 1 dan 100.")
                    continue
                
                stats = generate_stats(character_type, level)

                print(f"\nCharacter [Level {level}]")
                for key, value in stats.items():
                    print(f"{key}: {value}")

                # Untuk tipe tunggal (min, std, e), tanya ulang input
                if character_type in ["min", "std", "e"]:
                    lagi = input("\nApakah ingin menginput level lagi? (y/n): ").strip().lower()
                    if lagi != 'y':
                        break
                else:
                    print()
            except ValueError:
                print("Harap masukkan angka yang valid.")

if __name__ == "__main__":
    main()