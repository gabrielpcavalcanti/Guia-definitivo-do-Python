import time

def maior(*nums):
    print('-=' * 30)
    print("Analizando os valores passados...")
    cont = 0
    while cont < len(nums):
        print(nums[cont], end=' ', flush=True)
        time.sleep(0.5)
        cont += 1
    print(f"foram informados {len(nums)} valores ao todo")
    maxis = max(nums)
    print(f"O maior valor informado foi {maxis}")


maior(6)
