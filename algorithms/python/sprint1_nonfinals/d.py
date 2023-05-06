from typing import List


def get_weather_randomness(temperatures: List[int]) -> int:
    list = []
    counter = 0
    temperatures.reverse()
    temperatures.append(-273)
    temperatures.reverse()
    temperatures.append(-273)
    for i in range(len(temperatures)):
        if (temperatures[i] > temperatures[i-1]
           and temperatures[i] > temperatures[i+1]):
            list.append(temperatures[i])
            counter += 1
    return counter


def read_input() -> List[int]:
    n = int(input())
    temperatures = list(map(int, input().strip().split()))
    return temperatures


temperatures = read_input()
print(get_weather_randomness(temperatures))
