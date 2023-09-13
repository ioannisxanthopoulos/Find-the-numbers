my_list = [2, 5, 8]
lives = 3

while my_list and lives > 0:
    user_input = int(input("Πληκτρολογήστε έναν αριθμό: "))

    if user_input in my_list:
        my_list.remove(user_input)
        print("Απομένουν " + str(len(my_list)) + " αριθμοί να βρείτε!")
    else:
        lives -= 1
        print("Αυτός ο αριθμός δεν υπάρχει στη λίστα, έχετε ακόμη " + str(lives) + " προσπάθειες.")

if not my_list:
    print("Κερδίσατε! Βρήκατε όλους τους αριθμούς.")
else:
    print("Χάσατε! Δεν είχατε άλλες προσπάθειες.")