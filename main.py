import time

def my_func_1():
    print("Function 1 başlıyor")
    time.sleep(5)
    print("Function 1 bitiyor")
    return 5

def my_func_2():
    print("Function 2 başlıyor")
    time.sleep(5)
    print("Function 2 bitiyor")
    return 10

if __name__ == "__main__":
    x=my_func_1()
    y=my_func_2()


    print(f"my_func_1 return değeri: {x}")
    print(f"my_func_2 return değeri: {y}")

# çalıştığında sırasıyla function 1 ve function 2 fonksiyonları çalışır ve 5 saniye bekler.