import random
import json


class Simulation:
    def __init__(self, initial_state_file=None, size=[10, 10]):
        if initial_state_file:
            initial_state = self.load_initial_state_file(initial_state_file)
            self.rows = len(initial_state)
            self.columns = len(initial_state[0])
            self.world = World(self.rows, self.columns, initial_state)
        
        else:
            self.rows = size[0]
            self.columns = size[1]
            self.world = World(self.rows, self.columns)

        print('Initial World state')
        self.world.print_board()
        self.progess_int = [self.world.get_integer_state()]

    def run(self, generations=100):
        for i in range(generations):
            self.world.evolve()
            self.progess_int.append(self.world.get_integer_state())
            print(f'Generation {i+1}')
            self.world.print_board()
            # input("Press Enter to continue...")

    def load_initial_state_file(self, filepath):
        initial_state = []
        with open(filepath, 'r') as f:
            for line in f:
                line_list = [Cell(status='Dead') if x.strip() == '_' else Cell(status='Live') for x in line.replace('\n', '')]
                initial_state.append(line_list)
        return initial_state

    def save_run(self, filepath='data/result.json'):
        with open(filepath, 'w') as f:
            json.dump(self.progess_int, f)
        print(f'Saved simulation to {filepath}.')
            

class World:
    def __init__(self, rows, columns, initial_state=None):
        self.rows = rows
        self.columns = columns
        if initial_state:
            self.state = initial_state
        else:
            self.state = self.initial_state_random()

    def initial_state_random(self, live_pop=0.2):
        grid = []
        for i in range(self.rows):
            line = random.choices([Cell(status='Dead'), Cell(status='Live')], weights=[1-live_pop, live_pop], k=self.columns)
            grid.append(line)
        return grid

    def print_board(self):
        for line in self.state:
            for cell in line:
                print(cell.get_print_symbol(), end='')
            print('')
        print('\n')

    def get_integer_state(self):
        converted_state = []
        for line in self.state:
            converted_line = []
            for cell in line:
                converted_line.append(cell.get_integer_value())
            converted_state.append(converted_line)
        return converted_state

    def evolve(self):
        # Lists of cells that go dead or go alive
        goes_dead = []
        goes_alive = []

        for i in range(self.rows):
            for j in range(self.columns):
                cell = self.state[i][j]
                n_live_neighbours = self.get_n_live_neighbours(i, j)
                if cell.is_live():
                    if (n_live_neighbours < 2) or (n_live_neighbours > 3):
                        goes_dead.append(cell)
                else:
                    if n_live_neighbours == 3:
                        goes_alive.append(cell)

        for cell in goes_dead:
            cell.dies()

        for cell in goes_alive:
            cell.lives()

    def get_n_live_neighbours(self, x, y):
        count = 0
        top_margin, bottom_margin, left_margin, right_margin = False, False, False, False

        if x == 0 and y == 0:
            top_margin, left_margin = True, True
        elif x == 0 and y == (self.columns - 1):
            top_margin, right_margin = True, True
        elif x == (self.rows - 1) and y == 0:
            bottom_margin, left_margin = True, True
        elif x == (self.rows - 1) and y == (self.columns - 1):
            bottom_margin, right_margin = True, True
        elif x == 0:
            top_margin = True
        elif x == (self.rows - 1):
            bottom_margin = True
        elif y == 0:
            left_margin = True
        elif y == (self.columns - 1):
            right_margin = True

        if not top_margin:
            if self.state[x - 1][y].is_live():
                count += 1
        if not bottom_margin:        
            if self.state[x + 1][y].is_live():
                count += 1
        if not left_margin:
            if self.state[x][y - 1].is_live():
                count += 1
        if not right_margin:
            if self.state[x][y + 1].is_live():
                count += 1
        if not top_margin and not left_margin:
            if self.state[x - 1][y - 1].is_live():
                count += 1
        if not bottom_margin and not right_margin:
            if self.state[x + 1][y + 1].is_live():
                count += 1
        if not bottom_margin and not left_margin:
            if self.state[x + 1][y - 1].is_live():
                count += 1
        if not top_margin and not right_margin:
            if self.state[x - 1][y + 1].is_live():
                count += 1
        
        return count

class Cell:
    def __init__(self, status='Dead'):
        self.status = status

    def lives(self):
        self.status = 'Live'

    def dies(self):
        self.status = 'Dead'

    def is_live(self):
        if self.status == 'Live':
            return True
        return False

    def get_print_symbol(self):
        if self.is_live():
            return '█'
        return '_'
    
    def get_integer_value(self):
        if self.is_live():
            return 1
        return 0


if __name__ == '__main__':
    print("Conway's Game of Life Simulation", end='\n\n')

    sim = Simulation(initial_state_file='data/pulsar.txt')
    sim.run(generations=15)
    sim.save_run()
