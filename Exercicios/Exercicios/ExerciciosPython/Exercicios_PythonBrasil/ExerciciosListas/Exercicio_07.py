"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a multiplicação e os números.
"""

nums = []

for i in range(5):
    num = int(input("Digite um número: "))
    nums.append(num)

print()
print(f"Os números: {nums}")
print(f"A soma é: {sum(nums)}")
print(f"A multiplicação é: {nums[0] * nums[1] * nums[2] * nums[3] * nums[4]}")
