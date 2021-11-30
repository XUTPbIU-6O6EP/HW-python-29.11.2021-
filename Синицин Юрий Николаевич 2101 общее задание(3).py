import time

def test_function (func):
    string_name=test_function.__name__
    print("Была вызвана функция",string_name)
    
def time_rapoti(func):
    print (time.perf_counter())

@test_function
@time_raboti
def pusk(func):
    return()