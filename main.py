#NITI 
import requests
import pyautogui
import time

def find_words_with_letters(letters, limit=5):
    api_url = f"https://api.datamuse.com/words?sp=*{letters}*"
    
    response = requests.get(api_url)
    words = response.json()

    if not words:
        return []

    matching_words = [word["word"] for word in words[:limit]]
    return matching_words

def main():
    three_letters = input("Enter three letters: ").lower()
    
    if len(three_letters) != 3 or not three_letters.isalpha(): #change letter count as per your wish
        print("Letter count doesn't mactch")
        return

    matching_words = find_words_with_letters(three_letters, limit=5) #change the limit as per you want this code to send words 
    
    if not matching_words:
        print(f"No words found with the letters {three_letters}.")
        return



    typing_location = (1402, 970)

    pyautogui.click(typing_location)

    for word in matching_words:

        time.sleep(0.2)


        pyautogui.write(word)

      
        time.sleep(0.2)

        pyautogui.press('enter')

while True: # optional argument, if you are using this then you have to manually stop the code or some error occurrs else it will ask for input forever
    if __name__ == "__main__":
        main()
