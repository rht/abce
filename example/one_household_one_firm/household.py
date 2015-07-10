from __future__ import division  # makes division work correctly
import abce
from abce.tools import is_zero, is_positive, is_negative, NotEnoughGoods


class Household(abce.Agent, abce.Household):
    def init(self, simulation_parameters, agent_parameters):
        """ 1. labor_endowment, which produces, because of w.declare_resource(...)
        in start.py one unit of labor per month
        2. Sets the utility function to utility = consumption of good "GOOD"
        """
        self.create('adult', 1)
        self.set_cobb_douglas_utility_function({"GOOD": 1})

    def sell_labor(self):
        """ offers one unit of labor to firm 0, for the price of 1 "money" """
        self.sell('firm', 0, "labor", 1, 1)

    def buy_goods(self):
        """ receives the offers and accepts them one by one """
        oo = self.get_offers("GOOD")
        for offer in oo:
            self.accept(offer)

    def consumption(self):
        """ consumes_everything and logs the aggregate utility. current_utiliy
        """
        current_utiliy = self.consume_everything()
        self.log_value('HH', current_utiliy)

