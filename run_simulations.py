from life import Simulation
from visualization import display_state, animate_simulation_v2


# Random simulation
# sim = Simulation(size=[20, 20])
# sim.run(generations=100)
# animate_simulation_v2(sim.progess_int, outfile='figures/random.mp4', colors=['w', '#27ae60'])

# Still lifes
# sim0 = Simulation(initial_state_file='data/still-lifes.txt')
# sim0.run(generations=5)
# animate_simulation_v2(sim0.progess_int, outfile='figures/still.mp4', colors=['w', '#27ae60'])

# Simple oscillators
# sim1 = Simulation(initial_state_file='data/oscillators.txt')
# sim1.run(generations=5)
# display_state(sim1.progess_int[0], outfile='figures/oscillators1.png', colors=['w', '#27ae60'])
# display_state(sim1.progess_int[1], outfile='figures/oscillators2.png', colors=['w', '#27ae60'])
# display_state(sim1.progess_int[0], outfile='figures/oscillators1_grid.png', colors=['w', '#27ae60'], grid=False)
# display_state(sim1.progess_int[1], outfile='figures/oscillators2_grid.png', colors=['w', '#27ae60'], grid=False)
# animate_simulation_v2(sim1.progess_int, outfile='figures/oscillators.mp4', colors=['w', '#27ae60'])

# Pulsar
# sim2 = Simulation(initial_state_file='data/pulsar.txt')
# sim2.run(generations=15)
# display_state(sim2.progess_int[0], outfile='figures/pulsar1.png', colors=['w', '#27ae60'])
# display_state(sim2.progess_int[1], outfile='figures/pulsar2.png', colors=['w', '#27ae60'])
# display_state(sim2.progess_int[2], outfile='figures/pulsar3.png', colors=['w', '#27ae60'])
# animate_simulation_v2(sim2.progess_int, outfile='figures/pulsar.mp4', colors=['w', '#27ae60'])

# Pentadecathlon
# sim3 = Simulation(initial_state_file='data/pentadecathlon.txt')
# sim3.run(generations=30)
# display_state(sim3.progess_int[0], outfile='figures/pentadecathlon1.png', colors=['w', '#27ae60'])
# display_state(sim3.progess_int[1], outfile='figures/pentadecathlon2.png', colors=['w', '#27ae60'])
# display_state(sim3.progess_int[2], outfile='figures/pentadecathlon3.png', colors=['w', '#27ae60'])
# animate_simulation_v2(sim3.progess_int, outfile='figures/pentadecathlon.mp4', colors=['w', '#27ae60'])

# Glider
# sim4 = Simulation(initial_state_file='data/glider.txt')
# sim4.run(generations=120)
# animate_simulation_v2(sim4.progess_int, outfile='figures/glider.mp4', colors=['w', '#27ae60'], frame_interval=100)


# Gosper Glider Gun
# sim5 = Simulation(initial_state_file='data/gosper-glider-gun.txt')
# sim5.run(generations=250)
# animate_simulation_v2(sim5.progess_int, outfile='figures/gosper-glider-gun.mp4', colors=['w', '#27ae60'], frame_interval=100)

# Known
sim6 = Simulation(initial_state_file='data/known.txt')
sim6.run(generations=100)
animate_simulation_v2(sim6.progess_int, outfile='figures/known.mp4', colors=['w', '#27ae60'], frame_interval=250)
