import random
import string


class StringGeneticAlgorithm:
    def __init__(self, target, population_size=200, mutation_rate=0.05):
        self.__target = target
        self.__population_size = population_size
        self.__mutation_rate = mutation_rate
        self.__population = self.__initialise_population()
        self.__generation = 0

    def __initialise_population(self):
        alphabet = string.ascii_lowercase + string.ascii_uppercase + ' '
        return [
            ''.join(random.choice(alphabet) for _ in range(len(self.__target)))
            for _ in range(self.__population_size)
        ]

    def __fitness(self, candidate):
        return sum(1 for expected, actual in zip(self.__target, candidate) if expected == actual)

    def __selection(self):
        scored_population = sorted(
            ((self.__fitness(candidate), candidate) for candidate in self.__population),
            key=lambda item: item[0],
            reverse=True,
        )
        total_fitness = sum(score for score, _ in scored_population)

        if total_fitness == 0:
            return random.choice(self.__population)

        pick = random.randint(0, total_fitness)
        running_total = 0

        for score, candidate in scored_population:
            running_total += score
            if running_total >= pick:
                return candidate

        return scored_population[-1][1]

    def __crossover(self, parent_a, parent_b):
        if not parent_a or not parent_b:
            return parent_a or parent_b

        crossover_point = random.randint(1, len(self.__target) - 1)
        return parent_a[:crossover_point] + parent_b[crossover_point:]

    def __mutate(self, candidate):
        mutated = list(candidate)

        for index, char in enumerate(mutated):
            if random.random() < self.__mutation_rate:
                mutated[index] = random.choice(string.ascii_lowercase + string.ascii_uppercase + ' ')

        return ''.join(mutated)

    def __evolve(self):
        next_population = []
        elite_count = max(1, int(self.__population_size * 0.1))
        ranked_population = sorted(
            self.__population,
            key=lambda candidate: self.__fitness(candidate),
            reverse=True,
        )
        next_population.extend(ranked_population[:elite_count])

        while len(next_population) < self.__population_size:
            parent_a = self.__selection()
            parent_b = self.__selection()
            child = self.__crossover(parent_a, parent_b)
            child = self.__mutate(child)
            next_population.append(child)

        self.__population = next_population[:self.__population_size]
        self.__generation += 1

    def best_candidate(self):
        return max(self.__population, key=self.__fitness)

    def run(self, max_generations=500, print_every=50):
        best = self.best_candidate()
        best_score = self.__fitness(best)

        while self.__generation < max_generations and best_score < len(self.__target):
            self.__evolve()
            best = self.best_candidate()
            best_score = self.__fitness(best)

            if print_every and self.__generation % print_every == 0:
                print(f'Generation {self.__generation}: {best} ({best_score}/{len(self.__target)})')

        return best, best_score, self.__generation


if __name__ == '__main__':
    target = 'hello world'
    algorithm = StringGeneticAlgorithm(target)
    result, score, generation = algorithm.run(print_every=10)
    print(f'Target: {target}')
    print(f'Best match: {result}')
    print(f'Score: {score}/{len(target)}')
    print(f'Generations: {generation}')