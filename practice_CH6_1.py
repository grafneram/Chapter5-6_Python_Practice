def filter_text(text, part_to_remove):
    filtered_text = text.replace(part_to_remove, "") #Removes the part from text
    return filtered_text

text = input("Please, enter a text to be filtered: ")
part_to_remove = input("Please, enter the text part to be removed from the text: ")
filtered_text = filter_text(text, part_to_remove)

print(f"The text after filtration is: {filtered_text}")
