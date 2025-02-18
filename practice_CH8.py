def corrected_info(filename):
    try:
        with open(filename, 'r') as file:
            data = file.read()

        incorrect = (
            "There can be no more than 4 football team players on the field at once. 2 players on offense and 2 players on defense can be on the field at one time.")
        correct = (
            "There can be no more than 22 football team players on the field at once. 11 players on offense and 11 players on defense can be on the field at one time.")

        if incorrect in data:
            update = data.replace(incorrect, correct)

            with open(filename, 'w') as file:
                file.write(update)
            print("Updated data, check file")
        else:
            print("No correction needed")

    except FileNotFoundError:
        print("File not found")

corrected_info('data.txt')