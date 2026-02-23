from calc import add

def test_add():
    assert add(2, 3) == 6  # wrong on purpose

test_add()  # 👈 THIS LINE IS THE FIX
