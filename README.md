# Background and Definitions
## Middling Divisors
The divisors of a number $n$ come in pairs which multiply to $n$; in general if $a|n$ then $a$ and $n/a$ are paired divisors. The pair whose values are closest together are called _middling divisors_. These smaller of the two is denoted $\mathcal{M}(n)$ and the larger is denoted $\mathcal{M}'(n)$.

## Square Numbers' Middling Divisors
A square number has non-distinct middling divisors; and conversely any number whose middling divisors are equal is square. Symbolically: $\mathcal{M}(n)=\mathcal{M}'(n)$ iff $n$ is square.

## Prime Numbers' Middling Divisors
A prime number's middling divisors are $\mathcal{M}(n)=1$ and $\mathcal{M}'(n)=n$. This is the most extreme relative gap between the middling divisors possible. In this particular sense, square numbers can be considered _opposite_ to square numbers. There lies a spectrum of squareness-primeness. We here investigate this spectrum and two ways to measure it.

## Arithmetic Squareness
The _arithmetic squareness_ of a number $n>1$ is defined as
$$s_a(n)=1-\frac{\mathcal{M}'(n)-\mathcal{M}(n)}{n-1}.$$
Note $s_a(n)=1$ for a square number, and $s(p)= 0$ for a prime $p$. These the the bounds, so $0\leq s_a(n)\leq 1$.

## Geometric Squareness
The _geometric squareness_ is defined as the ratio
$$s_g(n)=\frac{\mathcal{M}(n)}{\mathcal{M}'(n)}.$$
Again, $s_g(n)=1$ for a square number, and $s_g(p_n)\to 0$ for the primes $p_n$ as $n\to\infty$. Hence, $0 \lt s_g(n) \leq 1$.

## Investigation
The purpose of this repository is to investigate both notions of squareness. How do they plot as sequences? Is there any interesting structure to them warranting further investigation?

# Configuration
Pytest is used for tests, create a .env file with PYTHONPATH = ./src to allow for importing of the
squareness package in the tests.
