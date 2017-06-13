from __future__ import division
from agent import Agent
from killer import Killer
from abce import Simulation, gui


                             # commend out simulation.graphs() and uncomment
                             # this line to run the simulation with a Graphical
#@gui # User Interface
def main():
        simulation = Simulation(rounds=100, name='name')
        simulation.declare_round_endowment(resource='labor_endowment',
                                           units=1,
                                           product='labor')
        simulation.declare_perishable(good='labor')

        simulation.aggregate('agent', possessions=[], variables=['count'])
        simulation.panel('agent', possessions=[], variables=['idn'])

        agents = simulation.build_agents(Agent, 'agent',
                       number=100)
        killers = simulation.build_agents(Killer, 'killer',
                       number=1)
        for r in simulation.next_round():
            killers.do('kill')
            agents.do('am_I_dead')
            killers.do('send_message')
            agents.do('aggregate')
            agents.do('panel')


        simulation.graphs()

if __name__ == '__main__':
    main()

