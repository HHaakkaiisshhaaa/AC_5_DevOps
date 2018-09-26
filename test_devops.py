def termial (n):
    if n == 0:
        return 0
    else: 
        return n + termial(n - 1)

def test_1():
    assert termial (5) == 15


   
  



