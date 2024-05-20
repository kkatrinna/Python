import random


class environment:
    def generate_environment(width, height):
        environment = [[random.randint(0, 1)
                         for _ in range(width)] for _ in range(height)]
        for i in range(1, width - 1):
            for j in range(1, height - 1):
                if environment[i][j] == 1 and (
                    environment[i - 1][j] == 0 or
                    environment[i + 1][j] == 0 or
                    environment[i][j - 1] == 0 or
                    environment[i][j + 1] == 0
                ):
                    environment[i][j] = 0
        return environment