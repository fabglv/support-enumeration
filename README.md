# support-enumeration

An implementation of the support enumeration algorithm that computes all Nash equilibria of a non-degenerate two-player game in normal form, as described in [1]. Another similar description is available in section 3.2 of [2].

## Description

The algorithm enumerates all possible support combinations of the same size for the two players and checks whether a valid equilibrium strategy exists for each support pair by solving a linear program. If so, it records the corresponding strategies. The linear programs are solved using **SciPy**'s **linprog**.

This approach is suitable for small games due to the combinatorial explosion of support pairs in larger games. Other approaches, such as vertex enumeration or the Lemke-Howson algorithm, are more appropriate for larger games. 

## File structure

```
support_enumeration.py           # Core implementation of the support enumeration algorithm
demo.py                          # Script to demonstrate usage of the support enumeration algorithm
```

## References

[1] V. Bonifaci. Computational Game Theory (lecture notes) https://ricerca.matfis.uniroma3.it/users/vbonifaci/tcs/cgt1.pdf
[2] Nisan N, Roughgarden T, Tardos E, Vazirani VV, eds. Algorithmic Game Theory. Cambridge University Press; 2007.
