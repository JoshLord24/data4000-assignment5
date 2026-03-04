# Inventory Reorder Analyzer

from random import seed

import requests

def main():

    # Get the student key and calculate the seed
    student_key = input("Enter your student key: ")
    seed = sum(ord(ch) for ch in student_key.strip()) 

    total_skus = 0
    reorder_count = 0

    #Threshold Requirements
    if seed % 3 == 0: 
        threshold = 15 
    elif seed % 3 == 1: 
        threshold = 12 
    else: threshold = 9

    #Loops to get SKU details
    while True:
        sku = input("Enter SKU (or 'done' to finish): ").strip()
        if sku.lower() == "done":
            break
        if sku == "":
            print("SKU cannot be empty. Please try again.")
            continue
        try:
            on_hand = int(input("Enter on-hand quantity: "))
            if on_hand <= 0:
                print("On-hand quantity must be > 0.")
                continue
        except ValueError:
            print("Invalid on-hand quantity. Please enter a number.")

        # Checks if the SKU is below the threshold and updates counts
        total_skus += 1
        if on_hand < threshold:
            reorder_count += 1
        
    if seed % 2 == 0:
        term = "weezer"
    else:
        term = "drake" 

    api_status = "OK"
    song_count = "N/A"

    try:
        response = requests.get(
            "https://itunes.apple.com/search", 
            params={"entity": "song", "limit": 5, "term": term}, timeout=5 )
        if response.status_code == 200:
            data = response.json()
            song_count = data.get("resultCount", "N/A")
        if song_count is None or not isinstance(song_count, int):
            api_status = "Invalid API Response;"
        else:
            api_status = f"Error: {response.status_code}"
    except Exception:
        api_status = "Invalid API Response"
    except Exception:
        api_status = "API Request Failed"

    print(f"Seed: {seed}")
    print(f"Threshold: {threshold}")
    print(f"Total SKUs: {total_skus}")
    print(f"Reorder flagged: {reorder_count}")
    print(f"Spotcheck term: {term}")
    print(f"API Status: {api_status}")
    print(f"Song Count: {song_count}")
main()
