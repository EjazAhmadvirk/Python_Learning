import random

player_roll = random.randint(1, 6)
computer_roll = random.randint(1, 6)

print("You rolled:", player_roll)
print("Computer rolled:", computer_roll)

if player_roll > computer_roll:
    print("🎉 You win!")
elif player_roll < computer_roll:
    print("💻 Computer wins!")
else:
    print("It's a tie!")
# Dice Roll Game
