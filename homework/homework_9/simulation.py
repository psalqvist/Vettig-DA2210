import matplotlib.pyplot as plt
from random import sample
from statistics import mean

class Simulation():

    def play_game(self, turn, win):
        flip = sample([0,1], 1)[0]
        if(flip):
            win = win + 2**turn
            return self.play_game(turn+1, win)
        else:
            return win
    # avarage payoff from last n games
    def simulate(self, number_of_games):
        average = [0]*number_of_games
        for i in range(1, number_of_games):
            res = self.play_game(1, 1)
            # use previous average to calculate running average
            average[i] = average[i-1] + (res-average[i-1])/i
        return average

if __name__ == "__main__":
    Simulation = Simulation()
    number_of_games = 1000000
    X = range(number_of_games)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.plot(X, Y)
    Y = Simulation.simulate(number_of_games)
    plt.xlabel('N')
    plt.yticks(range(0, 100, 20))
    plt.ylim(0, 100)
    plt.ylabel('Avarage payoff')
    plt.title('Average payoff over the last n games played')
    plt.plot(X, Y)
    plt.show()



