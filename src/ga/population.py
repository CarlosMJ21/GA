# MIT License
#
# Copyright (c) 2020 Carlos Moreno
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""
Population class

"""

#######################################################################
# Imports area
#######################################################################

# Generic / Built-in


# Other Libs
import numpy as np


# Own Libs
from individual import Individual


#######################################################################


class Population():
    """
    Class to represent a population.

    Attributes
    ----------


    Methods
    ----------


    """
    def __init__(self, config: dict, fitnessFunc):
        """
        Constructor of a generic population.

        Parameters
        ----------
        config : dict
            Configuration of the population

        fitnessFunc : function
            Fitness function associated to individual

        Returns
        ----------

        """
        self.config = config
        self.fitnessFunc = fitnessFunc
        self.individuals = None
        self.numInd = None

    def initialise_population(self):
        """
        Initialise the individuals of a population.

        Parameters
        ----------

        Returns
        ----------

        """
        config = self.config
        self.individuals = []
        indAp = self.individuals.append

        for i in range(config['size_population']):
            chromosome = []

            indAp(Individual(self.fitnessFunc,
                             config['crossover'],
                             config['mutation'],
                             chromosome))

    def mutation(self):
        """
        Computes the mutation over the entire population.

        Parameters
        ----------

        Returns
        ----------

        """

        for i in range(self.numInd):
            self.individuals[i].mutate(self.config['pressure'])

    def _scores(self):
        """
        Computes the score for each individual chromosome against the
        fitness function

        Parameters
        ----------

        Returns
        ----------
        scores : list [float]


        """

        scores = [individual.fitness_function() for individual in
                  self.individuals]

        return scores
