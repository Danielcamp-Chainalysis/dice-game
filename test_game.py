import game

def test_roll_dice():
    result = game.roll_dice()
    assert 1 <= result <= 6, f"Roll should be 1-6, got {result}"
    print("✅ test_roll_dice passed")

def test_roll_multiple_dice():
    results = game.roll_multiple_dice(3)
    assert len(results) == 3, f"Should roll 3 dice, got {len(results)}"
    assert all(1 <= r <= 6 for r in results), "All rolls should be 1-6"
    print("✅ test_roll_multiple_dice passed")

def test_roll_multiple_dice_zero():
    results = game.roll_multiple_dice(0)
    assert results == [], f"Rolling 0 dice should return empty list"
    print("✅ test_roll_multiple_dice_zero passed")

if __name__ == "__main__":
    test_roll_dice()
    test_roll_multiple_dice()
    test_roll_multiple_dice_zero()
    print("\n✅ All tests passed!")
