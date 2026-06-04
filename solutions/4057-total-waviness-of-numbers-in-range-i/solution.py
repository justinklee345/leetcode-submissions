class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        waviness = 0
        for i in range(num1, num2 + 1):
            digits = [int(d) for d in str(i)]
            if len(digits) < 3:
                continue
            for j in range(1, len(digits) - 1):
                if digits[j] > digits[j - 1] and digits[j] > digits[j+1]:
                    waviness += 1
                    continue
                if digits[j] < digits[j - 1] and digits[j] < digits[j+1]:
                    waviness += 1
                    continue

        return waviness
