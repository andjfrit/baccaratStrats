from simulations.graphsim import GraphSim


def main():
    print("we are about to create a graph to help show how many hands is optimal using martingale strategy")
    players = input("enter num of players")
    hands = input("enter the max hands you want to see played by each player")

    x = GraphSim(players, hands)
    x.get_data()
    x.create_graph()


if __name__ == "__main__":
    main()
