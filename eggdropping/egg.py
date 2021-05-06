class EggProblem:
    def __init__(self, negg, nfloors):
        self.eggs = negg
        self.floors = nfloors
    
    def define_strategy(self, func):
        # Strategy takes in current number of eggs, and the closed interval where the solution is (ie. with current information).
        # Strategy should return the floor to drop the next egg
        self.strategy = func
    
    def run_simulation():
        results = []
        for correct_floor in range(1, self.floors + 1):
            is_correct = False
            drop_count = 0
            floor_interval = [1, self.nfloors]

            current_eggs = self.negg

            while not is_correct:
                drop_floor = self.strategy(current_eggs, largest_known_floor)
                drop_count += 1
                
                if drop_floor < self.floors:
                    floor_interval[0] = action["drop"]
                else:
                    floor_interval[1] = action["drop"] - 1
                    current_eggs -= 1
                
                if floor_interval[0] == floor_interval[1]:
                    if floor_interval[0] == self.floors:
                        results.append(drop_count)
                    else:
                        print(f"You guessed the wrong floor for nfloors={self.floors}")
                        break
        
                




situation = EggProblem(negg=2, nfloors=100)
situation.define_strategy(func)