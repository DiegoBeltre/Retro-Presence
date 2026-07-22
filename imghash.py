import os
import imagehash
from PIL import Image

def build_library():
    library = {}

    for file in os.listdir("LibAssets"):
        if file.startswith('.'):
            continue
            
        path = os.path.join("LibAssets", file)
        game_name = os.path.splitext(file)[0]

        with Image.open(path) as img:

            p_hash = imagehash.phash(img)
            d_hash = imagehash.dhash(img)

        library[game_name] = (p_hash, d_hash)

    return library


def find_best_match(current_hashes, library):
    current_p, current_d = current_hashes
    
    best_game = None
    best_score = 999

    for game, (lib_p, lib_d) in library.items():
        p_score = current_p - lib_p
        d_score = current_d - lib_d
        
        total_score = (p_score * 2) + d_score
        
        print(f"{game} -> phash_dist: {p_score}, dhash_dist: {d_score} | Weighted Total: {total_score}")

        if total_score < best_score:
            best_score = total_score
            best_game = game

    return best_game, best_score
