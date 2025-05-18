import numpy as np
from support_enumeration import support_enumeration, show_final_results

def main():

    A = np.array([[3, 3],
                  [2, 5],
                  [0, 6]])

    B = np.array([[3, 2],
                  [2, 6],
                  [3, 1]])

    A = np.array([[5, 0],
                [1, 1]])
    B = np.array([[5, 1],
                [0, 1]])
    
    equilibria = support_enumeration(A,B)
    
    show_final_results(equilibria)

if __name__ == "__main__":
    main()