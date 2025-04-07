import asyncio

async def my_func_1():
    print("Function 1 başlıyor")
    await asyncio.sleep(5)  #non blocking delay simülasyonu
    print("Function 1 bitiyor")
    return 5

async def my_func_2():
    print("Function 2 başlıyor")
    await asyncio.sleep(5)  #non blocking delay simülasyonu
    print("Function 2 bitiyor")
    return 10


async def main():
    task1 = asyncio.create_task(my_func_1())
    task2 = asyncio.create_task(my_func_2())
    x= await task1
    y= await task2

if __name__ == "__main__":

    """ x=my_func_1() #bu şekilde çalıştırırsak hata alırız çünkü async fonksiyonlar await ile çalıştırılmalıdır.
         y=my_func_2()

    print(x)
    print(y) """

    asyncio.run(main())  #async main sayesinde iki fonksiyon aynı anda çalışır ve 5 saniye beklerler.

