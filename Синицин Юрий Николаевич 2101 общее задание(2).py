import time
def test_function ():
    string_name=test_function.__name__
    print("Была вызвана функция",string_name)
    return 0
test_function()
print(time.perf_counter())
