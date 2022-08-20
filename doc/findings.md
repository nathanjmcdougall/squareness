# Arithmetic Squareness
## Discrete curves
As shown in [arithmetic_squareness_to_5000_asymptotes.png](../src/img/graphs/arithmetic_squareness_to_5000_asymptotes.png), the squareness values tend to fall near a number of curves which asymptote to values of $\frac{0}{1}, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, ... \frac{k-1}{k}$. But why these values? And what determines which number will lie near which curve?

The first curve is the most straightfoward, which is 0. These points are the primes. But what about the points that seem to follow near $1/2$? These are the even semiprimes; i.e. the primes doubled (the only exception is 8, which is also included). Why do they tend to $1/2$? Because
$$s_a(2p) = 1 - \frac{p-2}{2p-1} = \frac{p+1}{2p-1}\to \frac{1}{2}.$$
In general, the $k$-th curve corresponds to those numbers $n$ for which $\mathcal{M}(n)=k$. In such a case we have
$$s_a(kq) = 1 - \frac{q-k}{kq-1} = \frac{(k-1)(q+1)}{kq-1}\to \frac{k-1}{k}.$$
The numbers in the first curve are the primes ([A000040](https://oeis.org/A000040)), the second are the semi-primes and 8 ([A161344](https://oeis.org/A161344)), and then the further sequences are [A161345](https://oeis.org/A161345), [A161424](https://oeis.org/A161424), [A161835](https://oeis.org/A161835), and then all the entries from [A162526](https://oeis.org/A162526) to [A162532](https://oeis.org/A162532) inclusive (i.e. up to the twelvth curve).

# Geometric Squareness
## Prime lines
On the graph [geometric_squareness_basic_to_50000.png](..\src\img\graphs\geometric_squareness_basic_to_50000.png) there are various lines of the form $s_g(n)= mn$ for various gradients $m$. On [geometric_squareness_basic_to_50000_lines.png](..\src\img\graphs\geometric_squareness_basic_to_50000_lines.png) these gradients are shown to correspond to $1/p^{2}$ for prime numbers $p$.

In fact, every point $(n, s_{g}(n))$ lies on _a_ line $s_g(n)= mn$, namely the one where $m=\frac{1}{\mathcal{M}'(n)^2}$. This follows from the facts that $s_g(n) = \frac{\mathcal{M}(n)}{\mathcal{M}'(n)}$, and $\mathcal{M}(n)\cdot \mathcal{M}'(n) =n$. But why do the lines where $\mathcal{M}'(n)$ is prime seem to stand out? Why do more points seem to lie on these lines than other lines? In other words, why do upper middling divisors seem to be disproportionately prime?