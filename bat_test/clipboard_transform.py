import pyperclip

def map_characters(text, mapping):
    mapped_text = ""
    for char in text:
        if char in mapping:
            mapped_text += mapping[char]
        else:
            mapped_text += char
    return mapped_text

def main():
    # Define your character mappings
    english_to_hebrew_mapping = {
        'a': 'ש',
        'b': 'נ',
        'c': 'ב',
        'd': 'ג',
        'e': 'ק',
        'f': 'כ',
        'g': 'ע',
        'h': 'י',
        'i': 'ן',
        'j': 'ח',
        'k': 'ל',
        'l': 'ך',
        'm': 'צ',
        'n': 'מ',
        'o': 'ם',
        'p': 'פ',
        'q': '/',
        'r': 'ר',
        's': 'ד',
        't': 'א',
        'u': 'ו',
        'v': 'ה',
        'w': '\'',
        'x': 'ס',
        'y': 'ט',
        'z': 'ז',
        '`': 'ף',
        ',': 'ת',
        '.': 'ץ',
        # Add more mappings as needed
    }
    
    hebrew_to_english_mapping = {value: key for key, value in english_to_hebrew_mapping.items()}
    
    # Get text from clipboard
    clipboard_text = pyperclip.paste()
    
    # Check if text is in Hebrew or English
    if any(english_char in clipboard_text for english_char in english_to_hebrew_mapping.keys()):
        # Text is in English, so transform to Hebrew
        transformed_text = map_characters(clipboard_text, english_to_hebrew_mapping)
    elif any(hebrew_char in clipboard_text for hebrew_char in hebrew_to_english_mapping.keys()):
        # Text is in Hebrew, so transform to English
        transformed_text = map_characters(clipboard_text, hebrew_to_english_mapping)
    else:
        print("Text does not contain recognized characters.")
        return
    
    # Put the transformed text back to the clipboard
    pyperclip.copy(transformed_text)
    print("Transformed text has been copied to clipboard.")

if __name__ == "__main__":
    main()
