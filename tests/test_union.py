from src.union import union
def test_union_simple():
    assert union({1,2}, {2,3}) == {1,2,3}
