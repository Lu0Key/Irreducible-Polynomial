# Irreducible-Polynomial
判断有限域上不可约多项式

## 原理

$F_q$ 上的 $n\;(\geqslant2)$ 次多项式 $f(x)$ 的为不可约多项式的充要条件是：  
- $\displaystyle f(x)\bigg|x^{q^n-1}-1$
- 对任意 $\displaystyle c\in F_q,\;f(c)\not=0$
- 对任意的 $\displaystyle n_i\;(n_i|n)$ 均有 $\displaystyle\gcd(x^{q^{n_i}-1}-1,\;f(x))=1$