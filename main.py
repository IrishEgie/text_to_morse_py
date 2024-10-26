import art

program_title = art.title
print('='*80)
print(program_title)
print('='*80)

morse_code_dict = art.morse_code_dict


def text_to_morse(text):
    """Convert text to Morse code."""
    morse_code = []
    for char in text.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])
        elif char == ' ':
            morse_code.append(' ')  # Add space for word separation
        else:
            morse_code.append('?')  # Placeholder for unsupported characters
    return ' '.join(morse_code)


while True:
    text_input = input('Write a sentence to convert to Morse code, keep it short: \n')

    # Count the number of words
    word_count = len(text_input.split())

    if 1 <= word_count <= 10:
        # Proceed with Morse code conversion
        print(f'Input accepted: "{text_input}"')
        morse_output = text_to_morse(text_input)
        # Morse code conversion output
        print(f'Morse conversion: "{morse_output}"')
        print('='*80,'\n')
    else:
        print(f'Warning: Please enter between 1 and 10 words. You entered {word_count} word(s).')
        text_input = ''  # Reset the text input