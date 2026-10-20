import random

def roll_dice():
    """Roll a single die (1-6)"""
    return random.randint(1, 6)

def roll_multiple_dice(num):
    """Roll multiple dice"""
    if num <= 0:
        return []
    return [roll_dice() for _ in range(num)]

def main():
    print("Welcome to Dice Game!")
    print("Rolling one die...")
    result = roll_dice()
    print(f"You rolled: {result}")

if __name__ == "__main__":
    main()
