# Arithmetic Squareness
## Discrete curves
As shown in [arithmetic_squareness_to_5000_asymptotes.png](../src/img/graphs/arithmetic_squareness_to_5000_asymptotes.png), the squareness values tend to fall near a number of curves which asymptote to values of $\frac{0}{1}, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, ... \frac{k-1}{k}$. But why these values? And what determines which number will lie near which curve?

The first curve is the most straightfoward, which is 0. These points are the primes. But what about the points that seem to follow near $1/2$? These are the even semiprimes; i.e. the primes doubled. Why do they tend to $1/2$? Because
$$s_a(2p) = 1 - \frac{p-2}{2p-1} = \frac{p+1}{2p-1}\to \frac{1}{2}.$$
In general, the $k$-th curve corresponds to those numbers $n$ whose largest prime factor is $n/k$. In such a case we have
$$s_a(kp) = 1 - \frac{p-k}{kp-1} = \frac{(k-1)(p+1)}{kp-1}\to \frac{k-1}{k}.$$

