""" A simulation of the first Model of Ernesto Carrella's paper:
Sticky Prices Microfoundations in a Agent Based Supply Chain
Section 4 Firms and Production

Here we have one firm and one market agent. The market agent
has the demand function q = 102 - p

"""
from __future__ import division
from multiprocessing import freeze_support
from firm import Firm
from market import Market
from abce import Simulation, gui


@gui
def main(simulation_parameters):
    s = Simulation(rounds=3000, name='analytical', random_seed=None)

    firms = s.build_agents(Firm, 'firm', number=1)
    market = s.build_agents(Market, 'market', number=1)
    for r in s.next_round():
        firms.do('my_production')
        firms.do('selling')
        market.do('buying')
        firms.do('adjust_price')
        firms.do('adjust_quantity')
        market.do('consumption')

if __name__ == '__main__':
    main()
