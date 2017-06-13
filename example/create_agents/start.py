from __future__ import division
from firm import Firm
from household import Household
from messenger import Messenger
from abce import Simulation, gui


                             # commend out simulation.graphs() and uncomment
                             # this line to run the simulation with a Graphical
#@gui(simulation_parameters) # User Interface
def main():
        simulation = Simulation(rounds=10, name='name')

        simulation.declare_round_endowment(resource='labor_endowment',
                                           units=1,
                                           product='labor')

        simulation.declare_perishable(good='labor')

        simulation.aggregate('household', possessions=[],  # put a list of household possessions to track here
                                      variables=['count']) # put a list of household possessions to track here

        simulation.aggregate('firm', possessions=[],  # put a list of household possessions to track here
                                      variables=['count']) # put a list of household possessions to track here

        firms = simulation.build_agents(Firm, 'firm',
                       number=1)

        households = simulation.build_agents(Household, 'household',
                       number=0)

        messengers = simulation.build_agents(Messenger, 'messenger', 1)

        for r in simulation.next_round():
            messengers.do('messaging')
            (firms+households).do('receive_message')
            firms.do('add_household')
            firms.do('add_firm')
            firms.do('print_id')
            households.do('print_id')
            # this instructs ABCE to save panel data as declared below
            (firms+households).do('aggregate')
        simulation.graphs()

if __name__ == '__main__':
    main()

