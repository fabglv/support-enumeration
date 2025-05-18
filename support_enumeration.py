import numpy as np
import itertools
from scipy.optimize import linprog


def support_enumeration(A, B):
    """Computes the equilibria of a two-player game using support enumeration."""
    equilibria = []
    M, N = A.shape

    S1 = tuple(range(M)) 
    S2 = tuple(range(N))

    for t in range(1, min(M, N) + 1):

        supports_1 = list(itertools.combinations(S1, t))
        supports_2 = list(itertools.combinations(S2, t))

        for I, J in itertools.product(supports_1, supports_2):
            res = supports_program(A, B, S1, S2, I, J)
            if res.status == 0:
                x, y = res.x[: M], res.x[M: ]
                equilibria.append([I, J, x, y])
    
    return equilibria

def supports_program(A, B, S1, S2, I, J):
    """Solves the linear program for given supports I (player 1) and J (player 2)."""
    M, N = A.shape
    t = len(I)

    # Creation of A_ub
    # Right part
    A_NE = np.zeros(shape=(M * t, N), dtype=int)

    for r, (k, i) in enumerate(itertools.product(S1, I)):
        A_NE[r] = A[k] - A[i]

    A_NE[:, np.setdiff1d(S2, J)] = 0

    zeros_NW = np.zeros(shape=(A_NE.shape[0], M), dtype=int)

    A_ub_top = np.hstack([zeros_NW, A_NE])

    # Left Part
    B_SW = np.zeros(shape=(N * t, M), dtype = int) # already transposed

    for r, (k, j) in enumerate(itertools.product(S2, J)):
        B_SW[r] = B[:, k] - B[:, j]
 
    B_SW[:, np.setdiff1d(S1, I)] = 0      

    zeros_SE = np.zeros(shape=(B_SW.shape[0], N), dtype=int)
    A_ub_bottom = np.hstack([B_SW, zeros_SE])

    # Composition of A_ub
    A_ub = np.vstack([A_ub_top, A_ub_bottom])

    # Vector b_ub
    b_ub = np.zeros(A_ub.shape[0], dtype=int)

    # Creation of A_eq
    A_eq = np.zeros(shape=(4, M + N), dtype=int)
    A_eq[0, :M] = 1
    A_eq[1, M:] = 1
    A_eq[2, np.setdiff1d(S1, I)] = 1
    A_eq[3, M + np.setdiff1d(S2, J)] = 1

    # Vector b_eq
    b_eq = np.array([1, 1, 0, 0])

    # Vector c 
    c = np.zeros(M + N)

    res = linprog(c, A_ub, b_ub, A_eq, b_eq, bounds=(0, None), method='highs')

    return res

def show_final_results(equilibria):
    """Prints the equilibria of the game, showing the support sets and strategies for both players."""
    print('______________________RESULTS______________________')
    for i, result in enumerate(equilibria, 1):
        I, J, x, y = result
        print(f'\nEquilibrium {i}:')
        print(f'  Support P1 (I): {I}')
        print(f'  Support P2 (J): {J}')
        print(f'  Strategy of P1 (x): {[round(e, 4) for e in x]}')
        print(f'  Strategy of P2 (y): {[round(e, 4) for e in y]}')
        print('____________________________________________________')