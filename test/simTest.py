from simulations.martingaleSim import MartingaleSim

sim = MartingaleSim(1000,100)
sim.sim()
print(sim.history)