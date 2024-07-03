
本章主要介绍 $n$ 阶行列式的定义、性质及其计算方法. 此外还要介绍用 $n$ 阶行列式求解 $n$ 元线性方程组的克拉默 (Cramer) 法则.

## $\S 1$ 二阶与三阶行列式

## 一、二元线性方程组与二阶行列式

用消元法解二元线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}=b_{2} .
\end{array}\right.
$$

为消去未知数 $x_{2}$, 以 $a_{22}$ 与 $a_{12}$ 分别乘上列两方程的两端, 然后两个方程相减, 得

$$
\left(a_{11} a_{22}-a_{12} a_{21}\right) x_{1}=b_{1} a_{22}-a_{12} b_{2} \text {; }
$$

类似地, 消去 $x_{1}$, 得

$$
\left(a_{11} a_{22}-a_{12} a_{21}\right) x_{2}=a_{11} b_{2}-b_{1} a_{21} \text {. }
$$

当 $a_{11} a_{22}-a_{12} a_{21} \neq 0$ 时,求得方程组 (1) 的解为.

$$
x_{1}=\frac{b_{1} a_{22}-a_{12} b_{2}}{a_{11} a_{22}-a_{12} a_{21}}, \quad x_{2}=\frac{a_{11} b_{2}-b_{1} a_{21}}{a_{11} a_{22}-a_{12} a_{21}} \text {. }
$$

(2)式中的分子、分母都是四个数分两对相乘再相惐而得. 其中分母 $a_{11} a_{22}$ $-a_{12} a_{21}$ 是由方程组 (1) 的四个系数确定的, 把这四个数按它们在方程组 (1)中 的位置,排成二行二列 (横排称行、竖排称列)的数表

$$
\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22},
\end{array}
$$

表达式 $a_{11} a_{22}-a_{12} a_{21}$ 称为数表 (3) 所确定的三阶行列式,并记作

$$
\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|
$$

数 $a_{i j}(i=1,2 ; j=1,2)$ 称为行列式 (4) 的元素或元. 元素 $a_{i j}$ 的第一个下标 $i$ 称为行标, 表明该元素位于第 $i$ 行, 第二个下标 $j$ 称为烈标, 表明该元素位于第 $j$ 列. 位于第 $i$ 行第 $j$ 列的元素称为行列式 $(4)$ 的 $(i, j)$ 元.

上述二阶行列式的定义, 可用对角线法则来记忆. 参看图 1.1, 把 $a_{11}$ 到 $a_{22}$ 的实联线称为主对角线, $a_{12}$ 到 $a_{21}$ 的虚联线称为副对角线， 于是二阶行列式便是主对角线上的两元素之积减去副对角 线上两元素之积所得的差.

利用二阶行列式的概念, (2) 式中 $x_{1}, x_{2}$ 的分子也可写 成二阶行列式, 即

$$
b_{1} a_{22}-a_{12} b_{2}=\left|\begin{array}{ll}
b_{1} & a_{12} \\
b_{2} & a_{22}
\end{array}\right|, \quad a_{11} b_{2}-b_{1} a_{21}=\left|\begin{array}{ll}
a_{11} & b_{1} \\
a_{21} & b_{2}
\end{array}\right| \text {. }
$$

若记

$$
D=\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|, \quad D_{1}=\left|\begin{array}{ll}
b_{1} & a_{12} \\
b_{2} & a_{22}
\end{array}\right|, \quad D_{2}=\left|\begin{array}{ll}
a_{11} & b_{1} \\
a_{21} & b_{2}
\end{array}\right|,
$$

那么(2)式可写成

$$
x_{1}=\frac{D_{1}}{D}=\frac{\left|\begin{array}{ll}
b_{1} & a_{12} \\
b_{2} & a_{22}
\end{array}\right|}{\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|}, \quad x_{2}=\frac{D_{2}}{D}=\frac{\left|\begin{array}{ll}
a_{11} & b_{1} \\
a_{21} & b_{2}
\end{array}\right|}{\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|} .
$$

注意这里的分母 $D$ 是由方程组 (1) 的系数所确定的二阶行列式(称系数行 列式), $x_{1}$ 的分子 $D_{1}$ 是用常数项 $b_{1}, b_{2}$ 替换 $D$ 中 $x_{1}$ 的系数 $a_{11}, a_{21}$ 所得的二 阶行列式, $x_{2}$ 的分子 $D_{2}$ 是用常数项 $b_{1}, b_{2}$ 替换 $D$ 中 $x_{2}$ 的系数 $a_{12}, a_{22}$ 所得的 二阶行列式.

例 1 求解二元线性方程组

$$
\left\{\begin{array}{l}
3 x_{1}-2 x_{2}=12 \\
2 x_{1}+x_{2}=1
\end{array}\right.
$$

解 由于

$$
\begin{aligned}
& D=\left|\begin{array}{rr}
3 & -2 \\
2 & 1
\end{array}\right|=3-(-4)=7 \neq 0, \\
& D_{1}=\left|\begin{array}{rr}
12 & -2 \\
1 & 1
\end{array}\right|=12-(-2)=14, \\
& D_{2}=\left|\begin{array}{rr}
3 & 12 \\
2 & 1
\end{array}\right|=3-24=-21,
\end{aligned}
$$

因此

$$
x_{1}=\frac{D_{1}}{D}=\frac{14}{7}=2, \quad x_{2}=\frac{D_{2}}{D}=\frac{-21}{7}=-3 \text {. }
$$

## 二、三阶行列式

定义 设有 9 个数排成 3 行 3 列的数表

记

$$
\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33},
\end{array}
$$

$$
\begin{aligned}
& \left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right| \\
= & a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32}-a_{11} a_{23} a_{32} \\
& -a_{12} a_{21} a_{33}-a_{13} a_{22} a_{31},
\end{aligned}
$$

(6)式称为数表 (5) 所确定的三阶行列式.

上述定义表明三阶行列式含 6 项,每项均为不同行不同列的三个元素的乘 积再冠以正负号, 其规律遵循图 1.2 所示的对角线法则: 图中有三条实线看做是 平行于主对角线的联线, 三条虚线看做是平行于副对角线的联线, 实线上三元素 的乘积冠正号,虚线上三元䕀的乘积冠负号.

例 2 计算三阶行列式

$$
D=\left|\begin{array}{rrr}
1 & 2 & -4 \\
-2 & 2 & 1 \\
-3 & 4 & -2
\end{array}\right|
$$

解 按对角线法则, 有

$$
\begin{aligned}
D= & 1 \times 2 \times(-2)+2 \times 1 \times(-3)+(-4) \times(-2) \times 4 \\
& -1 \times 1 \times 4-2 \times(-2) \times(-2)-(-4) \times 2 \times(-3) \\
= & -4-6+32-4-8-24=-14 .
\end{aligned}
$$

例 3 求解方程 解 方程左端的三阶行列式

$$
\left|\begin{array}{lll}
1 & 1 & 1 \\
2 & 3 & x \\
4 & 9 & x^{2}
\end{array}\right|=0 .
$$

$$
\begin{aligned}
D & =3 x^{2}+4 x+18-9 x-2 x^{2}-12 \\
& =x^{2}-5 x+6,
\end{aligned}
$$

由 $x^{2}-5 x+6=0$ 解得 $x=2$ 或 $x=3$.

对角线法则只适用于二阶与三阶行列式, 为研究四阶及更高阶行列式, 下面 先介绍有关全排列的知识, 然后引出 $n$ 阶行列式的概念.

## $\S 2$ 全排列及其逆序数

先看一个例子.

引例 用 $1,2,3$ 三个数字, 可以组成多少个没有重复数字的三位数?

解 这个问题相当于说, 把三个数字分别放在百位、十位与个位上, 有几种 不同的放法?

显然, 百位上可以从 $1,2,3$ 三个数字中任选一个, 所以有 3 种放法; 十位上 只能从剩下的两个数字中选一个, 所以有 2 种放法; 而个位上只能放最后剩下的 一个数字,所以只有 1 种放法. 因此, 共有 $3 \times 2 \times 1=6$ 种放法.

这六个不同的三位数是:

$$
123,231,312,132,213,321 \text {. }
$$

在数学中,把考察的对象, 例如上例中的数字 $1,2,3$ 叫做元素. 上述问题就 是: 把 3 个不同的元素排成一列, 共有几种不同的排法?

对于 $n$ 个不同的元素, 也可以提出类似的问题: 把 $n$ 个不同的元素排成一 列, 共有几种不同的排法?

把 $n$ 个不同的元素排成一列, 叫做这 $n$ 个元素的全排列 (也简称排列).

$n$ 个不同元索的所有排列的种数, 通常用 $P_{n}$ 表示. 由引例的结果可知 $P_{3}=$ $3 \cdot 2 \cdot 1=6$.

为了得出计算 $P_{n}$ 的公式, 可以仿照引例进行讨论:

从 $n$ 个元素中任取一个放在第一个位置上,有 $n$ 种取法;

又从剩下的 $n-1$ 个元素中任取一个放在第二个位置上,有 $n-1$ 种取法;

这样继续下去, 直到最后只剩下一个元素放在第 $n$ 个位置上, 只有 1 种取 法.于是

$$
P_{n}=n \cdot(n-1) \cdot \cdots \cdot 3 \cdot 2 \cdot 1=n ! .
$$

对于 $n$ 个不同的元䋜, 先规定各元素之间有一个标准次序(例如 $n$ 个不同 的自然数, 可规定由小到大为标准次序), 于是在这 $n$ 个元素的任一排列中, 当 某两个元素的先后次序与标准次序不同时, 就说有 1 个逆序.一个排列中所有逆 序的总数叫做这个排列的逆序数.

逆序数为奇数的排列叫做奇排列, 逆序数为偶数的排列叫做偶排列.

下面来讨论计算排列的逆序数的方法.

不失一般性, 不妨设 $n$ 个元素为 1 至 $n$ 这 $n$ 个自然数, 并规定由小到大为 标准次序.设

$$
p_{1} p_{2} \cdots p_{n}
$$

为这 $n$ 个自然数的一个排列, 考虑元素 $p_{i}(i=1,2, \cdots, n)$, 如果比 $p_{i}$ 大的且排 在 $p_{i}$ 前面的元素有 $t_{i}$ 个, 就说 $p_{i}$ 这个元素的逆序数是 $t_{i}$. 全体元素的逆序数之 总和

即是这个排列的逆序数.

$$
t=t_{1}+t_{2}+\cdots+t_{n}=\sum_{i=1}^{n} t_{i}
$$

例 4 求排列 32514 的逆序数.

解 在排列 32514 中:

3 排在首位,逆序数为 0 ;

2 的前面比 2 大的数有一个(3), 故逆序数为 1 ;

5 是最大数,逆序数为 0 ;

1 的前面比 1 大的数有三个 $(3,2 、 5)$, 故逆序数为 3 ;

4 的前面比 4 大的数有一个 (5), 故逆序数为 1 , 于是这个排列的逆序数为

$$
t=0+1+0+3+1=5 \text {. }
$$

## § $3 n$ 阶行列式的定义

为了给出 $n$ 阶行列式的定义, 先来研究三阶行列式的结构. 三阶行列式定 义为

$$
\begin{aligned}
\left|\begin{array}{rrr}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|= & a_{11} a_{22} a_{33}+a_{12} a_{23} a_{31}+a_{13} a_{21} a_{32} \\
& -a_{11} a_{23} a_{32}-a_{12} a_{21} a_{33}-a_{13} a_{22} a_{31}
\end{aligned}
$$

容易看出:

(i) (6)式右边的每一项都恰是三个元素的乘积, 这三个元素位于不同的 行、不同的列. 因此, (6) 式右端的任一项除正负号外可以写成 $a_{1 p_{1}} a_{2 p_{2}} a_{3 p_{3}}$. 这 里第一个下标(行标)排成标准次序 123 , 而第二个下标(列标)排成 $p_{1} p_{2} p_{3}$, 它 是 $1,2,3$ 三个数的某个排列. 这样的排列共有 6 种, 对应(6)式右端共含 6 项.

（ii）各项的正负号与列标的排列对照.

带正号的三项列标排列是 $123,231,312$;

带负号的三项列标排列是 $132,213,321$.

经计算可知前三个排列都是偶排列，而后三个排列都是奇排列. 因此各项所 带的正负号可以表示为 $(-1)^{t}$, 其中 $t$ 为列标排列的逆序数.

总之,三阶行列式可以写成

$$
\left|\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23} \\
a_{31} & a_{32} & a_{33}
\end{array}\right|=\sum(-1)^{\prime} a_{1 p_{1}} a_{2 p_{2}} a_{3 p_{3}},
$$

其中 $t$ 为排列 $p_{1} p_{2} p_{3}$ 的逆序数, 之表示对 $1,2,3$ 三个数的所有排列 $p_{1} p_{2} p_{3}$ 取 和.

仿此,可以把行列式推广到一般情形.

定义 设有 $n^{2}$ 个数, 排成 $n$ 行 $n$ 列的数表

$$
\begin{array}{llll}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
& \cdots \cdots \cdots \cdots & \cdots \\
& \cdots & \cdots & \\
a_{n 1} & a_{n 2} & \cdots & a_{n n},
\end{array}
$$

作出表中位于不同行不同列的 $n$ 个数的乘积,并冠以符号 $(-1)^{t}$, 得到形如

$$
(-1)^{\prime} a_{1 p_{1}} a_{2 p_{2}} \cdots a_{n p_{n}}
$$

的项, 其中 $p_{1} p_{2} \cdots p_{n}$ 为自然数 $1,2, \cdots, n$ 的一个排列, $t$ 为这个排列的逆序数. 由于这样的排列共有 $n$ ! 个, 因而形如(7)式的项共有 $n$ ! 项. 所有这 $n$ ! 项的 代数和

$$
\sum(-1)^{t} a_{1 p_{1}} a_{2 p_{2}} \cdots a_{n p_{n}}
$$

称为 $\boldsymbol{n}$ 阶行列式, 记作

$$
D=\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|,
$$

简记作 $\operatorname{det}\left(a_{i j}\right)$,其中数 $a_{i j}$ 为行列式 $D$ 的 $(i, j)$ 元. 按此定义的二阶、三阶行列式,与 §1 中用对角线法则定义的二阶、三阶行 列式, 显然是一致的. 当 $n=1$ 时,一阶行列式 $|a|=a$, 注意不要与绝对值记号相 混消。

例 5 证明 $n$ 阶行列式

$$
\left|\begin{array}{llll}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{n}
\end{array}\right|=\lambda_{1} \lambda_{2} \cdots \lambda_{n},
$$

其中未写出的元素都是 0 .

证 第一式左端称为对角行列式,其结果是显然的,下面只证第二式.

在第二式左端中, $\lambda_{i}$ 为行列式的 $(i, n-i+1)$ 元, 故记 $\lambda_{i}=a_{i, n-i+1}$, 则依行 列式定义

其中 $t$ 为排列 $n(n-1) \cdots 21$ 的逆序数,故

$$
t=0+1+2+\cdots+(n-1)=\frac{n(n-1)}{2} \text {. }
$$

证毕

主对角线以下 (上) 的元郜都为 0 的行列式叫做上(下)三角形行列式, 它的 值与对角行列式一样.

例 6 证明下三角形行列式

$$
D=\left|\begin{array}{cccc}
a_{11} & & & 0 \\
a_{21} & a_{22} & & \\
\vdots & \vdots & \ddots & \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|=a_{11} a_{22} \cdots a_{n n} .
$$

证 由于当 $j>i$ 时, $a_{i j}=0$, 故 $D$ 中可能不为 0 的元素 $a_{i p_{i}}$, 其下标应有 $p_{i} \leqslant i$, 即 $p_{1} \leqslant 1, p_{2} \leqslant 2, \cdots, p_{n} \leqslant n$.

在所有排列 $p_{1} p_{2} \cdots p_{n}$ 中, 能满足上述关系的排列只有一个自然排列 $12 \cdots n$, 所以 $D$ 中可能不为 0 的项只有一项 $(-1)^{\prime} a_{11} a_{22} \cdots a_{n n}$. 此项的符号 $(-1)^{\prime}=$ $(-1)^{0}=1$, 所以

$$
D=a_{11} a_{22} \cdots a_{n n} .
$$

## $\S 4$ 对 换

为了研究 $n$ 阶行列式的性质,先来讨论对换以及它与排列的奇偶性的关系.

在排列中,将任意两个元甞对调，其余的元素不动，这种作出新排列的手续叫做对换. 将 相邻两个元拳对换, 叫做相邻对换.

定理 1 一个排列中的任意两个元串对换，排列改变奇偶性.

证 先证相邻对换的博形.

设排列为 $a_{1} \cdots a_{t} a b b_{1} \cdots b_{m}$, 对换 $a$ 与 $b$, 变为 $a_{1} \cdots a_{t} b a b_{1} \cdots b_{m}$. 显然, $a_{1}, \cdots, a_{t} ; b_{1}, \cdots$, $b_{m}$ 这些元素的逆序数经过对换并不改变,而 $a, b$ 两元素的逆序数改变为: 当 $a<b$ 时，经对 换后 $a$ 的逆序数增加 1 而 $b$ 的逆序数不变; 当 $a>b$ 时,经对换后 $a$ 的逆序数不变而 $b$ 的逆 序数减少 1 . 所以排列 $a_{1} \cdots a_{l} a b b_{1} \cdots b_{m}$ 与排列 $a_{1} \cdots a_{l} b a b_{1} \cdots b_{m}$ 的奇偶性不同.

再证一般对换的情形.

设排列为 $a_{1} \cdots a_{t} a b_{1} \cdots b_{m} b c_{1} \cdots c_{n}$, 把它作 $m$ 次相邻对换,变成 $a_{1} \cdots a_{t} a b b_{1} \cdots b_{m} c_{1} \cdots c_{n}$, 再作 $m+1$ 次相邻对换，变成 $a_{1} \cdots a_{l} b b_{1} \cdots b_{m} a c_{1} \cdots c_{n}$. 总之,经 $2 m+1$ 次相邻对换，排列 $a_{1} \cdots$ $a_{l} a b_{1} \cdots b_{m} b c_{1} \cdots c_{n}$ 变成排列 $a_{1} \cdots a_{b} b b_{1} \cdots b_{m} a c_{1} \cdots c_{n}$, 所以这两个排列的奇偶性相反.

推论 奇排列变成标准排列的对换次数为奇数，偶排列变成标准排列的对换次数为 偶数.

证 由定理 1 知对换的次数就是排列奇偶性的变化次数,而标准排列是偶排列(逆序数 为 0$)$, 因此知推论成立.

证毕

利用定理 I,下面来讨论行列式定义的另一种表示法.

对于行列式的任一项

$$
(-1)^{t} a_{1 p_{1}} \cdots a_{i p_{j}} \cdots a_{j p_{i}} \cdots a_{n p_{n}},
$$

其中 $i \cdots i \cdots j \cdots n$ 为自然排列,$\imath$ 为排列 $p_{1} \cdots p_{i} \cdots p_{j} \cdots p_{n}$ 的逆序数, 对换元繁 $a_{i p_{i}}$ 与 $a_{j p}$, 成

$$
(-1)^{t} a_{1 p_{1}} \cdots a_{i p_{j}} \cdots a_{i p_{1}} \cdots a_{n p_{n},},
$$

这时,这一项的值不变,而行标排列与列标排列同时作了一次相应的对换. 设新的行标排列 $1 \cdots j \cdots i \cdots n$ 的逆序数为 $r$, 则 $r$ 为奇数; 设新的列标排列 $p_{1} \cdots p_{j} \cdots p_{i} \cdots p_{n}$ 的逆序数为 $t_{1}$, 则

$$
(-1)^{t} t^{\prime}=-(-1)^{t} \text {. 故 }(-1)^{t}=(-1)^{r+t} \text {, }
$$

于是

这就表明，对换乘积中两元察的次序，从而行标排列与列标排列同时作了相应的对换,则 行标排列与列标排列的逆序数之和并不改变奇偶性. 经一次对换是如此,经多次对换当然还 是如此.于是,经过若干次对换,使: 列标排列 $p_{1} p_{2} \cdots p_{n}$ (逆序数为 $t$ ) 变为自然排列 (逆序数为 0 );

行标排列则相应的从自然排列变为某个新的排列, 设此新排列为 $q_{1} q_{2} \cdots q_{n}$, 其逆序数为 $s$, 则有

$$
(-1)^{f} a_{1 p_{1}} a_{2 p_{2}} \cdots a_{n p_{n}}=(-1)^{s} a_{q_{1}} a_{q_{2} 2} \cdots a_{q_{n}} \cdot
$$

又, 若 $p_{i}=j$, 则 $q_{j}=i$ (即 $a_{i p_{i}}=a_{i j}=a_{q_{j}}$ ). 可见排列 $q_{1} q_{2} \cdots q_{n}$ 由排列 $p_{1} p_{2} \cdots p_{n}$ 所惟一 确定.

由此可得

定理 $2 n$ 阶行列式也可定义为

$$
D=\Sigma(-1)^{t} a_{\rho_{1} 1} a_{p_{2} 2} \cdots a_{p_{n} n},
$$

其中 $t$ 为行标排列 $p_{1} p_{2} \cdots p_{n}$ 的逆序数.

证 按行列式定义有

记

$$
\begin{aligned}
& D=\sum(-1)^{\prime} a_{1 p_{1}} a_{2 p_{2}} \cdots a_{n p_{n}}, \\
& D_{1}=\sum(-1)^{\prime} a_{p_{1} 1} a_{p_{2} 2} \cdots a_{p_{n} n} .
\end{aligned}
$$

由上面讨论知: 对于 $D$ 中任一项 ( - 1 $)^{t} a_{1 p_{1}} a_{2 p_{2}} \cdots a_{n p_{n}}$, 总有且仅有 $D_{1}$ 中的某一项 $(-1)^{s} a_{q_{1}, 1} a_{q_{2}}{ }^{2} \cdots a_{q_{n} n}$ 与之对应并相等; 反之, 对于 $D_{1}$ 中的任一项 $(-1)^{\prime} a_{p_{1}} a_{p_{2}{ }^{2}} \cdots a_{p_{n} n}$, 也总 有且仅有 $D$ 中的某一项 $(-1)^{*} a_{1 q_{1}} a_{2 q_{2}} \cdots a_{n q_{n}}$ 与之对应并相等, 于是 $D$ 与 $D_{1}$ 中的项可以一 一对应并相等, 从而 $D=D_{1}$.

## $\S 5$ 行列式的性质

记

$$
D=\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|, D^{\mathrm{T}}=\left|\begin{array}{cccc}
a_{11} & a_{21} & \cdots & a_{n 1} \\
a_{12} & a_{22} & \cdots & a_{n 2} \\
\vdots & \vdots & & \vdots \\
a_{1 n} & a_{2 n} & \cdots & a_{n n}
\end{array}\right|,
$$

行列式 $D^{\mathrm{T}}$ 称为行列式 $D$ 的转置行列式.

性质 1 行列式与它的转置行列式相等.

证 记 $D=\operatorname{det}\left(a_{i}\right)$ 的转篮行列式

$$
D^{\mathrm{T}}=\left|\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & & \vdots \\
b_{n 1} & b_{n 2} & \cdots & b_{n n}
\end{array}\right|
$$

即 $D^{T}$ 的 $(i, j)$ 元为 $b_{i j}$, 则 $b_{n}=a_{j i}(i, j=1,2, \cdots, n)$, 按定义

$$
D^{\mathrm{T}}=\sum(-1)^{t} b_{1 p_{1}} b_{2 p_{2}} \cdots b_{n p_{n}}=\sum(-1)^{t} a_{p_{1} 1} a_{p_{2} 2} \cdots a_{p_{14} n} \text {. }
$$

而由定理 2,有

$$
D=\sum(-1)^{t} a_{p_{1} 1} a_{p_{2} 2} \cdots a_{p_{n} n} \text {, }
$$

故

$$
D^{\top}=D \text {. }
$$

由此性质可知,行列式中的行与列具有同等的地位,行列式的性质凡是对行 成立的对列也同样成立，反之亦然。

性质 2 互换行列式的两行 (列), 行列式变号.

证设行列式

$$
D_{1}=\left|\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & & \vdots \\
b_{n 1} & b_{n 2} & \cdots & b_{n n}
\end{array}\right|
$$

是由行列式 $D=\operatorname{det}\left(a_{i j}\right)$ 对换 $i, j$ 两行得到的, 即当 $k \neq i, j$ 时, $b_{k p}=a_{k p}$ ；当 $k=i, j$ 时, $b_{i p}=$ $a_{j p}, b_{j p}=a_{i p}$,于是

$$
\begin{aligned}
D_{1} & =\sum(-1)^{\prime} b_{1 p_{1}} \cdots b_{i p_{i}} \cdots b_{i p_{j}} \cdots b_{n p_{n}} \\
& =\sum(-1)^{\prime} a_{1 p_{1}} \cdots a_{i p_{i}} \cdots a_{i p_{j}} \cdots a_{n p_{n}} \\
& =\sum(-1)^{t} a_{1 p_{1}} \cdots a_{i p_{j}} \cdots a_{i p_{i}} \cdots a_{n p_{n}},
\end{aligned}
$$

其中 $1 \cdots i \cdots j \cdots n$ 为自然排列, $t$ 为排列 $p_{1} \cdots p_{i} \cdots p_{j} \cdots p_{n}$ 的逆序数. 设排列 $p_{1} \cdots p_{j} \cdots p_{i} \cdots p_{n}$ 的逆序数为 $t_{1}$, 则 $(-1)^{t}=-(-1)^{t}$, 故

$$
D_{1}=-\sum(-1)^{2} a_{1 \mu_{1}} \cdots a_{i p_{j}} \cdots a_{j p_{i}} \cdots a_{n p_{n}}=-D \text {. }
$$

证毕

以 $r_{i}$ 表示行列式的第 $i$ 行, 以 $c_{i}$ 表示第 $i$ 列. 交换 $i, j$ 两行记作 $r_{i} \leftrightarrow r_{j}$, 交 换 $i, j$ 两列记作 $c_{i} \leftrightarrow c_{j}$.

推论 如果行列式有两行(列)完全相同,则此行列式等于零.

证 把这两行互换,有 $D=-D$,故 $D=0$.

性质 3 行列式的某一行(列) 中所有的元韭都乘以同一数 $k$, 等于用数 $k$ 乘此行列式.

第 $i$ 行(或列)乘以 $k$,记作 $r_{i} \times k$ (或 $c_{i} \times k$ ).

推论 行列式中某一行(列)的所有元素的公因子可以提到行列式记号的外 面。

第 $i$ 行(或列)提出公因子 $k$, 记作 $r_{i} \div k$ (或 $c_{i} \div k$ ).

性质 4 行列式中如果有两行(列)元韭成比例,则此行列式等于雾.

性质 5 若行列式的某一列(行)的元素都是两数之和,例如第 $i$ 列的元素 都是两数之和:

$$
D=\left|\begin{array}{cccccc}
a_{11} & a_{12} & \cdots & \left(a_{1 i}+a_{1 i}^{\prime}\right) & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & \left(a_{2 i}+a_{2 i}^{\prime}\right) & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & \left(a_{n i}+a_{n i}^{\prime}\right) & \cdots & a_{n n}
\end{array}\right|,
$$

则 $D$ 等于下列两个行列式之和 :

$$
\begin{aligned}
D & =\left|\begin{array}{cccccc}
a_{11} & a_{12} & \cdots & a_{1 i} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 i} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n i} & \cdots & a_{n n}
\end{array}\right| \\
& +\left|\begin{array}{cccccc}
a_{11} & a_{12} & \cdots & a_{1 i}^{\prime} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 i}^{\prime} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n i}^{\prime} & \cdots & a_{n n}
\end{array}\right| .
\end{aligned}
$$

性质 6 把行列式的某一列(行)的各元素乘以同一数然后加到另一列 (行) 对应的元素上去,行列式不变.

例如以数 $k$ 乘第 $j$ 列加到第 $i$ 列上(记作 $c_{i}+k c_{j}$ ), 有

$$
\begin{aligned}
& \left|\begin{array}{ccccccc}
a_{11} & \cdots & a_{1 i} & \cdots & a_{1 j} & \cdots & a_{1 n} \\
a_{21} & \cdots & a_{2 i} & \cdots & a_{2 j} & \cdots & a_{2 n} \\
\vdots & & \vdots & & \vdots & & \vdots \\
a_{n 1} & \cdots & a_{n i} & \cdots & a_{n j} & \cdots & a_{n n}
\end{array}\right| \\
& \stackrel{c_{i}+k c_{j}}{\underline{a_{11}}} \begin{array}{ccccccc}
a_{21} & \cdots & \left(a_{1 i}+k a_{1 j}\right) & \cdots & a_{1 j} & \cdots & a_{1 n} \\
\left.a_{2 i}+k a_{2 j}\right) & \cdots & a_{2 j} & \cdots & a_{2 n} \\
a_{n 1} & \cdots & \left(a_{n i}+k a_{n j}\right) & \cdots & a_{n j} & \cdots & a_{n n}
\end{array} \mid \quad(i \neq j) .
\end{aligned}
$$

(以数 $k$ 乘第 $j$ 行加到第 $i$ 行上,记作 $r_{i}+k r_{j}$ )

以上诸性质请读者证明之.

上述性质 5 表明: 当某一行 (或列) 的元素为两数之和时,行列式关于该行 (或列)可分解为两个行列式.若 $n$ 阶行列式每个元素都表示成两数之和,则它 可分解成 2" 个行列式. 例如二阶行列式

$$
\begin{aligned}
& \left|\begin{array}{cc}
a+x & b+y \\
c+z & d+w
\end{array}\right|=\left|\begin{array}{cc}
a & b+y \\
c & d+w
\end{array}\right|+\left|\begin{array}{cc}
x & b+y \\
z & d+w
\end{array}\right| \\
= & \left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right|+\left|\begin{array}{ll}
a & y \\
c & w
\end{array}\right|+\left|\begin{array}{cc}
x & b \\
z & d
\end{array}\right|+\left|\begin{array}{cc}
x & y \\
z & w
\end{array}\right| .
\end{aligned}
$$

性质 2,3,6 介绍了行列式关于行和关于列的三种运算，即 $r_{i} \leftrightarrow r_{j}, r_{i} \times k$, $r_{i}+k r_{j}$ 和 $c_{i} \leftrightarrow c_{j}, c_{i} \times k, c_{i}+k c_{j}$, 利用这些运算可简化行列式的计算, 特别是利 用运算 $r_{i}+k r_{j}$ (或 $c_{i}+k c_{j}$ ) 可以把行列式中许多元素化为 0 . 计算行列式常用的 一种方法就是利用运算 $r_{i}+k r_{\text {j }}$ 把行列式化为上三角形行列式, 从而算得行列 式的值. 请看下例. 例 7 计算

$$
D=\left|\begin{array}{rrrr}
3 & 1 & -1 & 2 \\
-5 & 1 & 3 & -4 \\
2 & 0 & 1 & -1 \\
1 & -5 & 3 & -3
\end{array}\right|
$$

解

$$
\begin{aligned}
& D \stackrel{c_{1} \rightarrow c_{2}}{=}-\left|\begin{array}{rrrr}
1 & 3 & -1 & 2 \\
1 & -5 & 3 & -4 \\
0 & 2 & 1 & -1 \\
-5 & 1 & 3 & -3
\end{array}\right| \frac{r_{2}-r_{1}}{r_{4}+5 r_{1}}-\left|\begin{array}{rrrr}
1 & 3 & -1 & 2 \\
0 & -8 & 4 & -6 \\
0 & 2 & 1 & -1 \\
0 & 16 & -2 & 7
\end{array}\right|
\end{aligned}
$$

$$
\begin{aligned}
& \stackrel{r_{4}+\frac{5}{4} r_{3}}{=}\left|\begin{array}{rrrr}
1 & 3 & -1 & 2 \\
0 & 2 & 1 & -1 \\
0 & 0 & 8 & -10 \\
0 & 0 & 0 & \frac{5}{2}
\end{array}\right|=40 .
\end{aligned}
$$

上述解法中, 先用了运算 $c_{1} \leftrightarrow c_{2}$, 其目的是把 $a_{11}$ 换成 1 , 从而利用运算 $r_{i}-$ $a_{i 1} r_{1}$, 即可把 $a_{i 1}(i=2,3,4)$ 变为 0 . 如果不先作 $c_{1} \leftrightarrow c_{2}$, 则由于原式中 $a_{11}=3$, 需用运算 $r_{i}-\frac{a_{i 1}}{3} r_{1}$ 把 $a_{i 1}$ 变为 0 , 这样计算时就比较麻烦. 第二步把 $r_{2}-r_{1}$ 和 $r_{4}+5 r_{1}$ 写在一起,这是两次运算,并把第一次运算结果的书写省略了.

例 8 计算

$$
D=\left|\begin{array}{llll}
3 & 1 & 1 & 1 \\
1 & 3 & 1 & 1 \\
1 & 1 & 3 & 1 \\
1 & 1 & 1 & 3
\end{array}\right|
$$

解 这个行列式的特点是各列 4 个数之和都是 6 . 今把第 $2,3,4$ 行同时加 到第 1 行, 提出公因子 6 , 然后各行减去第一行:

$$
D \stackrel{r_{1}+r_{2}+r_{3}+r_{4}}{=}\left|\begin{array}{llll}
6 & 6 & 6 & 6 \\
1 & 3 & 1 & 1 \\
1 & 1 & 3 & 1 \\
1 & 1 & 1 & 3
\end{array}\right| \stackrel{r_{1} \div 6}{=} 6\left|\begin{array}{llll}
1 & 1 & 1 & 1 \\
1 & 3 & 1 & 1 \\
1 & 1 & 3 & 1 \\
1 & 1 & 1 & 3
\end{array}\right|
$$

例 9 计算

$$
D=\left|\begin{array}{cccc}
a & b & c & d \\
a & a+b & a+b+c & a+b+c+d \\
a & 2 a+b & 3 a+2 b+c & 4 a+3 b+2 c+d \\
a & 3 a+b & 6 a+3 b+c & 10 a+6 b+3 c+d
\end{array}\right| .
$$

解 从第 4 行开始, 后行减前行,

$$
\begin{aligned}
& D \stackrel{\substack{r_{4}-r_{3} \\
r_{3}-r_{2}}}{r_{2}-r_{1}}\left|\begin{array}{cccc}
a & b & c & d \\
0 & a & a+b & a+b+c \\
0 & a & 2 a+b & 3 a+2 b+c \\
0 & a & 3 a+b & 6 a+3 b+c
\end{array}\right| \\
& \stackrel{r_{4}-r_{3}}{\underline{r_{3}-r_{2}}}\left|\begin{array}{cccc}
a & b & c & d \\
0 & a & a+b & a+b+c \\
0 & 0 & a & 2 a+b \\
0 & 0 & a & 3 a+b
\end{array}\right| \\
& \stackrel{r_{4}-r_{3}}{=}\left|\begin{array}{cccc}
a & b & c & d \\
0 & a & a+b & a+b+c \\
0 & 0 & a & 2 a+b \\
0 & 0 & 0 & a
\end{array}\right|=a^{4} .
\end{aligned}
$$

上述诸例中都用到把几个运算写在一起的省略写法, 这里要注意各个运算 的次序一般不能颠倒,这是由于后一次运算是作用在前一次运算结果上的缘故. 例如

$$
\begin{aligned}
& \left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right| \underline{\underline{r_{1}+r_{2}}}\left|\begin{array}{cc}
a+c & b+d \\
c & d
\end{array}\right| \underline{\underline{r_{2}-r_{1}}}\left|\begin{array}{cc}
a+c & b+d \\
-a & -b
\end{array}\right|, \\
& \left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right| \stackrel{\underline{r_{2}-r_{1}}}{=} \begin{array}{cc}
a & b \\
c-a & d-b
\end{array}\left|\underline{\underline{r_{1}+r_{2}}}\right| \begin{array}{cc}
c & d \\
c-a & d-b
\end{array} \mid,
\end{aligned}
$$

可见两次运算当次序不同时所得结果不同. 忽视后一次运算是作用在前一 次运算的结果上, 就会出错, 例如

$$
\left|\begin{array}{ll}
a & b \\
c & d
\end{array}\right| \frac{r_{1}+r_{2}}{\overline{r_{2}-r_{1}}}\left|\begin{array}{cc}
a+c & b+d \\
c-a & d-b
\end{array}\right|,
$$

这样的运算是错误的,出错的原因在于第二次运算找错了对象.

此外还要注意运算 $r_{i}+r_{j}$ 与 $r_{j}+r_{i}$ 的区别, 记号 $r_{i}+k r_{j}$ 不能写作 $k r_{j}+r_{i}$ (这里不能套用加法的交换律).

上述诸例都是利用运算 $r_{i}+k r_{j}$ 把行列式化为上三角形行列式, 用归纳法 不难证明 (这里不证) 任何 $n$ 阶行列式总能利用运算 $r_{i}+k r_{j}$ 化为上三角形行列 式,或化为下三角形行列式 (这时要先把 $a_{1 n}, \cdots, a_{n-1, n}$ 化为 0 ). 类似地,利用列 运算 $c_{i}+k c_{j}$,也可把行列式化为上三角形行列式或下三角形行列式.

例 10 设

$$
\begin{gathered}
D=\left|\begin{array}{cccccc}
a_{11} & \cdots & a_{1 k} & & & \\
\vdots & & \vdots & & 0 & \\
a_{k 1} & \cdots & a_{k k} & & & \\
c_{11} & \cdots & c_{1 k} & b_{11} & \cdots & b_{1 n} \\
\vdots & & \vdots & \vdots & & \vdots \\
c_{n 1} & \cdots & c_{n k} & b_{n 1} & \cdots & b_{n n}
\end{array}\right|, \\
D_{1}=\operatorname{det}\left(a_{i j}\right)=\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 k} \\
\vdots & & \vdots \\
a_{k 1} & \cdots & a_{k k}
\end{array}\right|, \\
D_{2}=\operatorname{det}\left(b_{i j}\right)=\left|\begin{array}{ccc}
b_{11} & \cdots & b_{1 n} \\
\vdots & & \vdots \\
b_{n 1} & \cdots & b_{n n}
\end{array}\right|,
\end{gathered}
$$

证明 $D=D_{1} D_{2}$.

证 对 $D_{1}$ 作运算 $r_{i}+\lambda r_{j}$, 把 $D_{1}$ 化为下三角形行列式,设为

$$
D_{1}=\left|\begin{array}{ccc}
p_{11} & & 0 \\
\vdots & \ddots & \\
p_{k 1} & \cdots & p_{k k}
\end{array}\right|=p_{11} \cdots p_{k k},
$$

对 $D_{2}$ 作运算 $c_{1}+\lambda c_{j}$, 把 $D_{2}$ 化为下三角形行列式,设为

$$
D_{2}=\left|\begin{array}{ccc}
q_{11} & & 0 \\
\vdots & \ddots & \\
q_{n 1} & \cdots & q_{n n}
\end{array}\right|=q_{11} \cdots q_{n n} .
$$

于是,对 $D$ 的前 $k$ 行作运算 $r_{i}+\lambda r_{j}$, 再对后 $n$ 列作运算 $c_{i}+\lambda c_{j}$, 把 $D$ 化为 下三角形行列式

- 14 . $D=\left|\begin{array}{cccccc}p_{11} & & & & \\ \vdots & \ddots & & & 0 \\ p_{k 1} & \cdots & p_{k k} & & \\ c_{11} & \cdots & c_{1 k} & q_{11} & \\ \vdots & & \vdots & \vdots & \ddots & \\ c_{n 1} & \cdots & c_{n k} & q_{n 1} & \cdots & q_{n n}\end{array}\right|$,

故

$$
D=p_{11} \cdots \cdot p_{k k} \cdot q_{11} \cdots \cdot q_{m}=D_{1} D_{2} \text {. }
$$

例 11 计算 $2 n$ 阶行列式

其中末写出的元素为 0 .

解 把 $D_{2 n}$ 中的第 $2 n$ 行依次与第 $2 n-1$ 行、 $\cdots$ 、第 2 行对调 (作 $2 n-2$ 次 相邻对换),再把第 $2 n$ 列依次与第 $2 n-1$ 列、第 2 列对调,得

根据例 10 的结果, 有

$$
D_{2 n}=D_{2} D_{2(n-1)}=(a d-b c) D_{2(n-1)} .
$$

以此作递推公式, 即得

$$
\begin{aligned}
D_{2 n} & =(a d-b c)^{2} D_{2(n-2)}=\cdots=(a d-b c)^{n-1} D_{2} \\
& =(a d-b c)^{n} .
\end{aligned}
$$

## $\S 6$ 行列式按行(列)展开

一般说来,低阶行列式的计算比高阶行列式的计算要简便,于是,我们自然 地考虑用低阶行列式来表示高阶行列式的问题. 为此, 先引进余子式和代数余子 式的概念.

在 $n$ 阶行列式中,把 $(i, j)$ 元 $a_{i j}$ 所在的第 $i$ 行和第 $j$ 列划去后,留下来的 $n-1$ 阶行列式叫做 $(i, j)$ 元 $a_{i j}$ 的余子式, 记作 $M_{i j}$; 记

$$
A_{i j}=(-1)^{i+j} M_{i j} \text {, }
$$

$A_{i j}$ 叫做 $(i, j)$ 元 $a_{i j}$ 的代数余子式.

例如四阶行列式

$$
D=\left|\begin{array}{llll}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34} \\
a_{41} & a_{42} & a_{43} & a_{44}
\end{array}\right|
$$

中 $(3,2)$ 元 $a_{32}$ 的余子式和代数余子式分别为

$$
\begin{gathered}
M_{32}=\left|\begin{array}{lll}
a_{11} & a_{13} & a_{14} \\
a_{21} & a_{23} & a_{24} \\
a_{41} & a_{43} & a_{44}
\end{array}\right|, \\
A_{32}=(-1)^{3+2} M_{32}=-M_{32} .
\end{gathered}
$$

引理 一个 $n$ 阶行列式,如果其中第 $i$ 行所有元素除 $(i, j)$ 元 $a_{i j}$ 外都为零, 那么这行列式等于 $a_{i j}$ 与它的代数余子式的乘积, 即

$$
D=a_{i j} A_{i j} .
$$

证 先证 $(i, j)=(1,1)$ 的情形, 此时

$$
D=\left|\begin{array}{cccc}
a_{11} & 0 & \cdots & 0 \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|,
$$

这是例 10 中当 $k=1$ 时的特殊情形,按例 10 的结论, 即有

又

从而

$$
D=a_{11} M_{11} \text {, }
$$

$$
\begin{gathered}
A_{11}=(-1)^{1+1} M_{11}=M_{11}, \\
D=a_{11} A_{11} .
\end{gathered}
$$

再证一般情形,此时

$$
D=\left|\begin{array}{ccccc}
a_{11} & \cdots & a_{1 j} & \cdots & a_{1 n} \\
\vdots & & \vdots & & \vdots \\
0 & \cdots & a_{i j} & \cdots & 0 \\
\vdots & & \vdots & & \vdots \\
a_{n 1} & \cdots & a_{n j} & \cdots & a_{n n}
\end{array}\right| .
$$

为了利用前面的结果, 把 $D$ 的行列作如下调换: 把 $D$ 的第 $i$ 行依次与第 $i-1$ 行、第 $i-2$ 行、 $\cdots$ 、第 1 行对调, 这样数 $a_{i j}$ 就调成 $(1, j)$ 元, 调换的次数为 $i-1$. 再把第 $j$ 列依次与第 $j-1$ 列、第 $j-2$ 列、..、、第 1 列对调，这样数 $a_{i j}$ 就调 成 $(1,1)$ 元, 调换的次数为 $j-1$. 总之, 经 $i+j-2$ 次调换, 把数 $a_{i j}$ 调成 $(1,1)$ 元, 所得的行列式 $D_{1}=(-1)^{i+j-2} D=(-1)^{i+j} D$, 而 $D_{1}$ 中 $(1,1)$ 元的余子式就是 $D$ 中 $(i, j)$ 元的余子式 $M_{i j}$.

由于 $D_{1}$ 的 $(1,1)$ 元为 $a_{i j}$, 第 1 行其余元素都为 0 , 利用前面的结果,有

$$
D_{1}=a_{i j} M_{i j} \text {, }
$$

于是 $\quad D=(-1)^{i+j} D_{1}=(-1)^{i+j} a_{i j} M_{i j}=a_{i j} A_{i j}$.

定理 3 行列式等于它的任一行(列)的各元素与其对应的代数余子式乘积 之和, 即

$$
\text { 或 } \quad \begin{array}{ll}
D & =a_{i 1} A_{i 1}+a_{i 2} A_{i 2}+\cdots+a_{i n} A_{i n} \quad(i=1,2, \cdots, n), \\
D & =a_{1 j} A_{1 j}+a_{2 j} A_{2 j}+\cdots+a_{n j} A_{n j} \quad(j=1,2, \cdots, n) .
\end{array}
$$

证

$$
\begin{aligned}
& D=\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
\vdots & \vdots & & \vdots \\
a_{i 1}+0+\cdots+0 & 0+a_{i 2}+\cdots+0 & \cdots & 0+\cdots+0+a_{i n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right| \\
& =\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
\vdots & \vdots & & \vdots \\
a_{i 1} & 0 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|+\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
\vdots & \vdots & & \vdots \\
0 & a_{i 2} & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right| \\
& +\cdots+\left|\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & a_{i n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right|
\end{aligned}
$$

根据引理, 即得

$$
D=a_{i 1} A_{i 1}+a_{i 2} A_{i 2}+\cdots+a_{i n} A_{i n} \quad(i=1,2, \cdots, n) .
$$

类似地,若按列证明,可得

$$
D=a_{1 j} A_{1 j}+a_{2 j} A_{2 j}+\cdots+a_{n j} A_{n j} \quad(j=1,2, \cdots, n) .
$$

这个定理叫做行列式按行 (列) 展开法则. 利用这一法则并结合行列式的性 质,可以简化行列式的计算.

下面用此法则来计算例 7 的

$$
D=\left|\begin{array}{rrrr}
3 & 1 & -1 & 2 \\
-5 & 1 & 3 & -4 \\
2 & 0 & 1 & -1 \\
1 & -5 & 3 & -3
\end{array}\right| \text {. }
$$

保留 $a_{33}$,把第 3 行其余元素变为 0 ,然后按第 3 行展开,

$$
\begin{aligned}
D & \stackrel{c_{1}-2 c_{3}}{c_{4}+c_{3}}\left|\begin{array}{rrrr}
5 & 1 & -1 & 1 \\
-11 & 1 & 3 & -1 \\
0 & 0 & 1 & 0 \\
-5 & -5 & 3 & 0
\end{array}\right| \\
& =(-1)^{3+3}\left|\begin{array}{rrr}
5 & 1 & 1 \\
-11 & 1 & -1 \\
-5 & -5 & 0
\end{array}\right| \underline{\underline{r_{2}+r_{1}}}\left|\begin{array}{rrr}
5 & 1 & 1 \\
-6 & 2 & 0 \\
-5 & -5 & 0
\end{array}\right| \\
& =(-1)^{1+3}\left|\begin{array}{rr}
-6 & 2 \\
-5 & -5
\end{array}\right| \stackrel{c_{1}-c_{2}}{\underline{-8}}\left|\begin{array}{rr}
-8 \\
0 & -5
\end{array}\right|=40 .
\end{aligned}
$$

例 12 证明范德蒙德 (Vandermonde) 行列式

$$
D_{n}=\left|\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
x_{1} & x_{2} & \cdots & x_{n} \\
x_{1}^{2} & x_{2}^{2} & \cdots & x_{n}^{2} \\
\vdots & \vdots & & \vdots \\
x_{1}^{n-1} & x_{2}^{n-1} & \cdots & x_{n}^{n-1}
\end{array}\right|=\prod_{n \geqslant i>j \geqslant 1}\left(x_{i}-x_{j}\right),
$$

其中记号“II”表示全体同类因子的乘积.

证. 用数学归纳法. 因为

$$
D_{2}=\left|\begin{array}{cc}
1 & 1 \\
x_{1} & x_{2}
\end{array}\right|=x_{2}-x_{1}=\prod_{2 \geqslant i>j \geqslant 1}\left(x_{i}-x_{j}\right),
$$

所以当 $n=2$ 时 (8) 式成立. 现在假设 (8) 式对于 $n-1$ 阶范德蒙德行列式成立, 要证 (8) 式对 $n$ 阶范德蒙德行列式也成立.

为此, 设法把 $D_{n}$ 降阶: 从第 $n$ 行开始, 后行减去前行的 $x_{1}$ 倍, 有

$$
D_{n}=\left|\begin{array}{ccccc}
1 & 1 & 1 & \cdots & 1 \\
0 & x_{2}-x_{1} & x_{3}-x_{1} & \cdots & x_{n}-x_{1} \\
0 & x_{2}\left(x_{2}-x_{1}\right) & x_{3}\left(x_{3}-x_{1}\right) & \cdots & x_{n}\left(x_{n}-x_{1}\right) \\
\vdots & \vdots & \vdots & & \vdots \\
0 & x_{2}^{n-2}\left(x_{2}-x_{1}\right) & x_{3}^{n-2}\left(x_{3}-x_{1}\right) & \cdots & x_{n}^{n-2}\left(x_{n}-x_{1}\right)
\end{array}\right|,
$$

按第 1 列展开,并把每列的公因子 $\left(x_{i}-x_{1}\right)$ 提出, 就有

$$
D_{n}=\left(x_{2}-x_{1}\right)\left(x_{3}-x_{1}\right) \cdots\left(x_{n}-x_{1}\right)\left|\begin{array}{cccc}
1 & 1 & \cdots & 1 \\
x_{2} & x_{3} & \cdots & x_{n} \\
\vdots & \vdots & & \vdots \\
x_{2}^{n-2} & x_{3}^{n-2} & \cdots & x_{n}^{n-2}
\end{array}\right|,
$$

上式右端的行列式是 $n-1$ 阶范德蒙德行列式, 按归纳法假设, 它等于所有 $\left(x_{i}-x_{j}\right)$ 因子的乘积, 其中 $n \geqslant i>j \geqslant 2$. 故

$$
\begin{aligned}
D_{n} & =\left(x_{2}-x_{1}\right)\left(x_{3}-x_{1}\right) \cdots\left(x_{n}-x_{1}\right) \prod_{n \geqslant i>j \geqslant 2}\left(x_{i}-x_{j}\right) \\
& =\prod_{n \geqslant i>j \geqslant 1}\left(x_{i}-x_{j}\right) .
\end{aligned}
$$

证毕

例 11 和例 12 都是计算 $n$ 阶行列式. 计算 $n$ 阶行列式,常要使用数学归纳 法, 不过在比较简单的情形 (如例 11), 可省略归纳法的叙述格式, 但归纳法的主 要步骤是不可能省略的. 这主要步骤是: 导出递推公式(例 11 中导出 $D_{2 n}=$ $\left.(a d-b c) D_{2(n-1)}\right)$ 及检验 $n=1$ 时结论成立(例 11 中最后用到 $D_{2}=a d-b c$ ).

由定理 3 , 还可得下述重要推论.

推论 行列式某一行 (列)的元素与另一行(列)的对应元妻的代数余子式乘 积之和等于寒. 即

$$
\begin{aligned}
& a_{i 1} A_{j 1}+a_{i 2} A_{j 2}+\cdots+a_{i n} A_{j n}=0, \quad i \neq j, \\
& \text { 或 } \quad a_{1 i} A_{1 j}+a_{2 i} A_{2 j}+\cdots+a_{n i} A_{n j}=0, \quad i \neq j .
\end{aligned}
$$

证 把行列式 $D=\operatorname{det}\left(a_{i j}\right)$ 按第 $j$ 行展开,有

$$
a_{j 1} A_{j 1}+a_{j 2} A_{j 2}+\cdots+a_{j n} A_{j n}=\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{i 1} & \cdots & a_{i n} \\
\vdots & & \vdots \\
a_{j 1} & \cdots & a_{j n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right|,
$$

在上式中把 $a_{j k}$ 换成 $a_{i k}(k=1, \cdots, n)$, 可得

$$
a_{i 1} A_{j 1}+a_{i 2} A_{j 2}+\cdots+a_{i n} A_{m}=\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{i 1} & \cdots & a_{i n} \\
\vdots & & \vdots \\
a_{i 1} & \cdots & a_{i n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right| \leftarrow \text { 第 } i \text { 行 }
$$

当 $i \neq j$ 时, 上式右端行列式中有两行对应元素相同, 故行列式等于零, 即得

$$
a_{i 1} A_{j 1}+a_{i 2} A_{j 2}+\cdots+a_{i n} A_{n}=0(i \neq j) .
$$

上述证法如按列进行, 即可得

$$
a_{1 i} A_{1 j}+a_{2 i} A_{2}, \cdots+a_{n i} A_{n j}=0(i \neq j) \text {. }
$$

综合定理 3 及其推论, 有关于代数余子式的重要性质:

$$
\sum_{k=1}^{n} a_{k i} A_{k j}=D \delta_{i j}= \begin{cases}D, & \text { 当 } i=j, \\ 0, & \text { 当 } i \neq j ;\end{cases}
$$

或

$$
\sum_{k=1}^{n} a_{i k} A_{j k}=D \delta_{i j}= \begin{cases}D, & \text { 当 } i=j, \\ 0, & \text { 当 } i \neq j ;\end{cases}
$$

其中

$$
\delta_{i j}= \begin{cases}1, & \text { 当 } i=j, \\ 0, & \text { 当 } i \neq j .\end{cases}
$$

仿照上述推论证明中所用的方法, 在行列式 $\operatorname{det}\left(a_{i j}\right)$ 按第 $i$ 行展开的展开式

$$
\operatorname{det}\left(a_{i j}\right)=a_{i 1} A_{i 1}+a_{i 2} A_{i 2}+\cdots+a_{i n} A_{i n}
$$

中, 用 $b_{1}, b_{2}, \cdots, b_{n}$ 依次代替 $a_{i 1}, a_{i 2}, \cdots, a_{i n}$, 可得

$$
\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{i-1,1} & \cdots & a_{i-1, n} \\
b_{1} & \cdots & b_{n} \\
a_{i+1,1} & \cdots & a_{i+1, n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right|=b_{1} A_{i 1}+b_{2} A_{i 2}+\cdots+b_{n} A_{i n} .
$$

其实, 把(9)式左端行列式按第 $i$ 行展开, 注意到它的 $(i, j)$ 元的代数余子式 等于 $\operatorname{det}\left(a_{i j}\right)$ 中 $(i, j)$ 元的代数余子式 $A_{i j}(j=1,2, \cdots, n)$, 也可知(9)式成立.

类似地,用 $b_{1}, \cdots, b_{n}$ 代替 $\operatorname{det}\left(a_{i j}\right)$ 中的第 $j$ 列, 可得

$$
\left|\begin{array}{ccccccc}
a_{11} & \cdots & a_{1, j-1} & b_{1} & a_{1, j+1} & \cdots & a_{1 n} \\
\vdots & & \vdots & \vdots & \vdots & & \vdots \\
a_{n 1} & \cdots & a_{n, j-1} & b_{n} & a_{n, j-1} & \cdots & a_{n n}
\end{array}\right|=b_{1} A_{1 j}+b_{2} A_{2 j}+\cdots+b_{n} A_{n j} .
$$

例 13 设

$$
D=\left|\begin{array}{rrrr}
3 & -5 & 2 & 1 \\
1 & 1 & 0 & -5 \\
-1 & 3 & 1 & 3 \\
2 & -4 & -1 & -3
\end{array}\right|,
$$

$D$ 的 $(i, j)$ 元的余子式和代数余子式依次记作 $M_{i j}$ 和 $A_{i j}$, 求

$$
A_{11}+A_{12}+A_{13}+A_{14} \text { 及 } M_{11}+M_{21}+M_{31}+M_{41} \text {. }
$$

解 按 (9) 式可知 $A_{11}+A_{12}+A_{13}+A_{14}$ 等于用 $1,1,1,1$ 代替 $D$ 的第 1 行 所得的行列式, 即

$$
\begin{aligned}
& A_{11}+A_{12}+A_{13}+A_{14}=\left|\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & 1 & 0 & -5 \\
-1 & 3 & 1 & 3 \\
2 & -4 & -1 & -3
\end{array}\right| \frac{r_{4}+r_{3}}{=r_{3}-r_{1}}\left|\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & 1 & 0 & -5 \\
-2 & 2 & 0 & 2 \\
1 & -1 & 0 & 0
\end{array}\right| \\
& =\left|\begin{array}{rrr}
1 & 1 & -5 \\
-2 & 2 & 2 \\
1 & -1 & 0
\end{array}\right| \underline{\underline{c_{2}+c_{1}}}\left|\begin{array}{rrr}
1 & 2 & -5 \\
-2 & 0 & 2 \\
1 & 0 & 0
\end{array}\right| . \\
& =\left|\begin{array}{rr}
2 & -5 \\
0 & 2
\end{array}\right|=4 \text {. }
\end{aligned}
$$

按 (10) 式可知

$$
\begin{aligned}
& M_{11}+M_{21}+M_{31}+M_{41}=A_{11}-A_{21}+A_{31}-A_{41} \\
&=\left|\begin{array}{rrrr}
1 & -5 & 2 & 1 \\
-1 & 1 & 0 & -5 \\
1 & 3 & 1 & 3 \\
-1 & -4 & -1 & -3
\end{array}\right| \stackrel{r_{4}+r_{3}}{=}\left|\begin{array}{rrrr}
1 & -5 & 2 & 1 \\
-1 & 1 & 0 & -5 \\
1 & 3 & 1 & 3 \\
0 & -1 & 0 & 0
\end{array}\right| \\
&=(-1)\left|\begin{array}{rrr}
1 & 2 & 1 \\
-1 & 0 & -5 \\
1 & 1 & 3
\end{array}\right| \stackrel{r_{1}-2 r_{3}}{=}-\left|\begin{array}{rrrr}
-1 & 0 & -5 \\
-1 & 0 & -5 \\
1 & 1 & 3
\end{array}\right|=0 .
\end{aligned}
$$

## $\S 7$ 克拉默法则

含有 $n$ 个未知数 $x_{1}, x_{2}, \cdots, x_{n}$ 的 $n$ 个线性方程的方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=b_{2}, \\
\cdots \cdots \cdots \cdots \\
a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n}=b_{n}
\end{array}\right.
$$

与二、三元线性方程组相类似,它的解可以用 $n$ 阶行列式表示, 即有

克拉默法则 如果线性方程组 (11)的系数行列式不等于零,即

那么, 方程组 (11) 有惟一解

$$
D=\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right| \neq 0
$$

$$
x_{1}=\frac{D_{1}}{D}, \quad x_{2}=\frac{D_{2}}{D}, \cdots, \quad x_{n}=\frac{D_{n}}{D},
$$

其中 $D_{j}(j=1,2, \cdots, n)$ 是把系数行列式 $D$ 中第 $j$ 列的元素用方程组右端的常 数项代替后所得到的 $n$ 阶行列式, 即

$$
D_{j}=\left|\begin{array}{ccccccc}
a_{11} & \cdots & a_{1, j-1} & b_{1} & a_{1, j+1} & \cdots & a_{1 n} \\
\vdots & & \vdots & \vdots & \vdots & & \vdots \\
a_{n 1} & \cdots & a_{n, j-1} & b_{n} & a_{n, j+1} & \cdots & a_{n n}
\end{array}\right| .
$$

这个法则的证明在第二章中给出. 注意这里的 $D_{j}$ 有展开式 (10).

例 14 解线性方程组

$$
\left\{\begin{aligned}
2 x_{1}+x_{2}-5 x_{3}+x_{4} & =8 \\
x_{1}-3 x_{2}-6 x_{4} & =9 \\
2 x_{2}-x_{3}+2 x_{4} & =-5 \\
x_{1}+4 x_{2}-7 x_{3}+6 x_{4} & =0 .
\end{aligned}\right.
$$

解

$$
\begin{aligned}
D & =\left|\begin{array}{rrrr}
2 & 1 & -5 & 1 \\
1 & -3 & 0 & -6 \\
0 & 2 & -1 & 2 \\
1 & 4 & -7 & 6
\end{array}\right| \frac{r_{1}-2 r_{2}}{r_{4}-r_{2}}\left|\begin{array}{rrrr}
0 & 7 & -5 & 13 \\
1 & -3 & 0 & -6 \\
0 & 2 & -1 & 2 \\
0 & 7 & -7 & 12
\end{array}\right| \\
& =-\left|\begin{array}{rrr}
7 & -5 & 13 \\
2 & -1 & 2 \\
7 & -7 & 12
\end{array}\right| \frac{c_{1}+2 c_{2}}{\frac{c_{3}+2 c_{2}}{0}}-\left|\begin{array}{rrr}
-3 & -5 & 3 \\
0 & -1 & 0 \\
-7 & -7 & -2
\end{array}\right| \\
& =\left|\begin{array}{rr}
-3 & 3 \\
-7 & -2
\end{array}\right|=27,
\end{aligned}
$$

$$
\begin{aligned}
D_{1} & =\left|\begin{array}{rrrr}
8 & 1 & -5 & 1 \\
9 & -3 & 0 & -6 \\
-5 & 2 & -1 & 2 \\
0 & 4 & -7 & 6
\end{array}\right|=81, \\
D_{2} & =\left|\begin{array}{rrrr}
2 & 8 & -5 & 1 \\
1 & 9 & 0 & -6 \\
0 & -5 & -1 & 2 \\
1 & 0 & -7 & 6
\end{array}\right|=-108, \\
D_{3} & =\left|\begin{array}{rrrr}
2 & 1 & 8 & 1 \\
1 & -3 & 9 & -6 \\
0 & 2 & -5 & 2 \\
1 & 4 & 0 & 6
\end{array}\right|=-27, \\
D_{4} & =\left|\begin{array}{rrrr}
2 & 1 & -5 & 8 \\
1 & -3 & 0 & 9 \\
0 & 2 & -1 & -5 \\
1 & 4 & -7 & 0
\end{array}\right|=27, \\
x_{1} & =3, x_{2}=-4, x_{3}=-1, x_{4}=1 .
\end{aligned}
$$

于是得

例 15 设曲线 $y=a_{0}+a_{1} x+a_{2} x^{2}+a_{3} x^{3}$ 通过四点 $(1,3),(2,4),(3,3)$ ， $(4,-3)$, 求系数 $a_{0}, a_{1}, a_{2}, a_{3}$.

解 把四个点的坐标代人曲线方程, 得线性方程组

$$
\left\{\begin{array}{l}
a_{0}+a_{1}+a_{2}+a_{3}=3, \\
a_{0}+2 a_{1}+4 a_{2}+8 a_{3}=4, \\
a_{0}+3 a_{1}+9 a_{2}+27 a_{3}=3, \\
a_{0}+4 a_{1}+16 a_{2}+64 a_{3}=-3,
\end{array}\right.
$$

其系数行列式

$$
D=\left|\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & 2 & 4 & 8 \\
1 & 3 & 9 & 27 \\
1 & 4 & 16 & 64
\end{array}\right|
$$

是一个范德蒙德行列式, 按例 12 的结果 (例 12 中范德蒙德行列式取 $D^{\mathrm{T}}$ 的形 式), 可得

$$
D=1 \cdot 2 \cdot 3 \cdot 1 \cdot 2 \cdot 1=12
$$

www.TopSage.com 而

$$
\begin{aligned}
& D_{1}=\left|\begin{array}{rrrr}
3 & 1 & 1 & 1 \\
4 & 2 & 4 & 8 \\
3 & 3 & 9 & 27 \\
-3 & 4 & 16 & 64
\end{array}\right| \begin{array}{l}
c_{4}-c_{3} \\
c_{3}-c_{2} \\
\hline c_{1}-3 c_{2}
\end{array}\left|\begin{array}{rrrr}
0 & 1 & 0 & 0 \\
-2 & 2 & 2 & 4 \\
-6 & 3 & 6 & 18 \\
-15 & 4 & 12 & 48
\end{array}\right| \\
& =(-1)^{3}\left|\begin{array}{rrr}
-2 & 2 & 4 \\
-6 & 6 & 18 \\
-15 & 12 & 48
\end{array}\right| \underline{\underline{c_{1}+c_{2}}}-\left|\begin{array}{rrr}
0 & 2 & 4 \\
0 & 6 & 18 \\
-3 & 12 & 48
\end{array}\right| \\
& =-(-3)\left|\begin{array}{rr}
2 & 4 \\
6 & 18
\end{array}\right| \stackrel{r_{2}-3 r_{1}}{\underline{\underline{n}}} 3\left|\begin{array}{ll}
2 & 4 \\
0 & 6
\end{array}\right|=36 \text {; } \\
& D_{2}=\left|\begin{array}{rrrr}
1 & 3 & 1 & 1 \\
1 & 4 & 4 & 8 \\
1 & 3 & 9 & 27 \\
1 & -3 & 16 & 64
\end{array}\right|=-18 \\
& D_{3}=\left|\begin{array}{rrrr}
1 & 1 & 3 & 1 \\
1 & 2 & 4 & 8 \\
1 & 3 & 3 & 27 \\
1 & 4 & -3 & 64
\end{array}\right|=24 ; \\
& D_{4}=\left|\begin{array}{rrrr}
1 & 1 & 1 & 3 \\
1 & 2 & 4 & 4 \\
1 & 3 & 9 & 3 \\
1 & 4 & 16 & -3
\end{array}\right|=-6 .
\end{aligned}
$$

因此,按克拉默法则,得惟一解

$$
a_{0}=3, a_{1}=-3 / 2, a_{2}=2, a_{3}=-1 / 2,
$$

即曲线方程为

$$
y=3-\frac{3}{2} x+2 x^{2}-\frac{1}{2} x^{3} .
$$

撤开求解公式 (12)，克拉默法则可叙述为下面的定理：

定理 4 如果线性方程组 (11) 的系数行列式 $D \neq 0$, 则 (11)一定有解, 且解 是惟一的.

定理 4 的逆否定理为:

定理 4' 如果线性方程组 (11) 无解或有两个不同的解, 则它的系数行列式 必为零。

线性方程组 (11) 右端的常数项 $b_{1}, b_{2}, \cdots, b_{n}$ 不全为零时, 线性方程组 (11) 叫做非齐次线性方程组, 当 $b_{1}, b_{2}, \cdots, b_{n}$ 全为零时,线性方程组 (11) 叫做齐次线 性方程组. 对于齐次线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=0, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=0, \\
\cdots \cdots \cdots \cdots \\
a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n}=0,
\end{array}\right.
$$

$x_{1}=x_{2}=\cdots=x_{n}=0$ 一定是它的解, 这个解叫做齐次线性方程组 (13) 的零解. 如果一组不全为零的数是 (13) 的解, 则它叫做齐次线性方程组 (13) 的非零解. 齐 次线性方程组 (13) 一定有零解, 但不一定有非零解.

把定理 4 应用于齐次线性方程组 (13), 可得

定理 5 如果齐次线性方程组 (13) 的系数行列式 $D \neq 0$, 则齐次线性方程组 (13) 没有非零解.

定理 $5^{\prime}$ 如果齐次线性方程组 (13) 有非零解,则它的系数行列式必为零.

定理 5(或定理 $5^{\prime}$ ) 说明系数行列式 $D=0$ 是齐次线性方程组有非零解的必 要条件.在第三章中还将证明这个条件也是充分的.

例 16 问 $\lambda$ 取何值时,齐次线性方程组

$$
\left\{\begin{aligned}
(5-\lambda) x+2 y+2 z & =0, \\
2 x+(6-\lambda) y & =0, \\
2 x+(4-\lambda) z & =0
\end{aligned}\right.
$$

有非零解?

解 由定理 $5^{\prime}$ 可知, 若所给齐次线性方程组有非零解, 则其系数行列式 $D=0$. 而

$$
\begin{aligned}
D & =\left|\begin{array}{ccc}
5-\lambda & 2 & 2 \\
2 & 6-\lambda & 0 \\
2 & 0 & 4-\lambda
\end{array}\right| \\
& =(5-\lambda)(6-\lambda)(4-\lambda)-4(4-\lambda)-4(6-\lambda) \\
& =(5-\lambda)(2-\lambda)(8-\lambda),
\end{aligned}
$$

由 $D=0$, 得 $\lambda=2 、 \lambda=5$ 或 $\lambda=8$.

不难验证,当 $\lambda=2 、 5$ 或 8 时,所给齐次线性方程组确有非零解.



## 第二章

## 矩阵及其运算

## $\S 1$ 矩阵

定义 1 由 $m \times n$ 个数 $a_{i j}(i=1,2, \cdots, m ; j=1,2, \cdots, n)$ 排成的 $m$ 行 $n$ 列 的数表

$$
\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}
$$

称为 $m$ 行 $n$ 列矩阵; 简称 $m \times n$ 矩阵. 为表示它是一个整体, 总是加一个括弧, 并用大写黑体字母表示它,记作

$$
\boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right),
$$

这 $m \times n$ 个数称为矩阵 $\boldsymbol{A}$ 的元素,简称为元,数 $a_{i j}$ 位于矩阵 $\boldsymbol{A}$ 的第 $i$ 行第 $j$ 列, 称为矩阵 $\boldsymbol{A}$ 的 $(i, j)$ 元. 以数 $a_{i j}$ 为 $(i, j)$ 元的矩阵可简记作 $\left(a_{i j}\right)$ 或 $\left(a_{i j}\right)_{m \times n}$. $m \times n$ 矩阵 $\boldsymbol{A}$ 也记作 $\boldsymbol{A}_{m \times n}$.

元素是实数的矩阵称为实矩阵, 元素是复数的矩阵称为复矩阵, 本书中的矩 阵除特别说明者外,都指实矩阵.

行数与列数都等于 $n$ 的矩阵称为 $n$ 阶矩阵或 $n$ 阶方阵. $n$ 阶矩阵 $\boldsymbol{A}$ 也记作 $\boldsymbol{A}_{n}$. 只有一行的矩阵

$$
\boldsymbol{A}=\left(\begin{array}{llll}
a_{1} & a_{2} & \cdots & a_{n}
\end{array}\right)
$$

称为行榘阵, 又称行向量. 为避免元素间的混淆, 行矩阵也记作

$$
\boldsymbol{A}=\left(a_{1}, a_{2}, \cdots, a_{n}\right) \text {. }
$$

只有一列的矩阵

$$
\boldsymbol{B}=\left(\begin{array}{c}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{array}\right)
$$

称为列矩阵, 又称列向量.

两个矩阵的行数相等、列数也相等时, 就称它们是同型聟阵. 如果 $\boldsymbol{A}=\left(a_{i j}\right)$ 与 $\boldsymbol{B}=\left(b_{i j}\right)$ 是同型矩阵, 并且它们的对应元素相等, 即

$$
a_{i j}=b_{i j}(i=1,2, \cdots, m ; j=1,2, \cdots, n),
$$

那么就称矩阵 $\boldsymbol{A}$ 与矩阵 $\boldsymbol{B}$ 相等, 记作

$$
\boldsymbol{A}=\boldsymbol{B} \text {. }
$$

元素都是零的矩阵称为零矩阵,记作 $\boldsymbol{O}$. 注意不同型的零矩阵是不同的. 矩阵的应用非常广泛，下面仅举几例.

例 1 某厂向三个商店发送四种产品的数量可列成矩阵

$$
\boldsymbol{A}=\left(\begin{array}{llll}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34}
\end{array}\right),
$$

其中 $a_{i j}$ 为工厂向第 $i$ 店发送第 $j$ 种产品的数量.

这四种产品的单价及单件重量也可列成矩阵

$$
\boldsymbol{B}=\left(\begin{array}{ll}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
b_{31} & b_{32} \\
b_{41} & b_{42}
\end{array}\right),
$$

其中 $b_{i 1}$ 为第 $i$ 种产品的单价, $b_{i 2}$ 为第 $i$ 种产品的单件重量.

例 2 . 四个城市间的单向航线如图 2.1 所示. 若令

$$
a_{i j}=\left\{\begin{array}{l}
1, \text { 从 } i \text { 市到 } j \text { 市有 } 1 \text { 条单向航线, } \\
0, \text { 从 } i \text { 市到 } j \text { 市没有单向航线, }
\end{array}\right.
$$

则图 2.1 可用矩阵表示为

$$
\boldsymbol{A}=\left(a_{i j}\right)=\left(\begin{array}{llll}
0 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0
\end{array}\right) .
$$

一般的,若干个点之间的单向通道都可用这样的矩阵表示:

例 $3 n$ 个变量 $x_{1}, x_{2}, \cdots, x_{n}$ 与 $m$ 个变量 $y_{1}, y_{2}, \cdots, y_{m}$ 之间的关系式

$$
\left\{\begin{array}{l}
y_{1}=a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}, \\
y_{2}=a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}, \\
\cdots \cdots \cdots \cdots \\
y_{m}=a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n}
\end{array}\right.
$$

表示一个从变量 $x_{1}, x_{2}, \cdots, x_{n}$ 到变量 $y_{1}, y_{2}, \cdots, y_{m}$ 的线性变换, 其中 $a_{i j}$ 为常 数. 线性变换 (2) 的系数 $a_{i j}$ 构成矩阵 $\boldsymbol{A}=\left(a_{i j}\right)_{m \times n}$.

给定了线性变换 (2), 它的系数所构成的矩阵 (称为系数矩阵) 也就确定.反 之, 如果给出一个矩阵作为线性变换的系数矩阵, 则线性变换也就确定. 在这个 意义上,线性变换和矩阵之间存在着一一对应的关系。

例如线性变换

$$
\left\{\begin{array}{c}
y_{1}=x_{1} \\
y_{2}=x_{2} \\
\ldots \ldots \ldots \ldots \\
y_{n}=x_{n}
\end{array}\right.
$$

叫做恒等变换, 它对应的一个 $n$ 阶方阵

$$
\boldsymbol{E}=\left(\begin{array}{cccc}
1 & 0 & \cdots & 0 \\
0 & 1 & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & 1
\end{array}\right)
$$

叫做 $n$ 阶单位矩阵, 简称单位阵. 这个方阵的特点是: 从左上角到右下角的直线 (叫做 (主)对角线)上的元素都是 1 , 其他元案都是 0 . 即单位阵 $\boldsymbol{E}$ 的 $(i, j)$ 元为

$$
\delta_{i j}=\left\{\begin{array}{l}
1, \text { 当 } i=j, \\
0, \text { 当 } i \neq j
\end{array}(i, j=1,2, \cdots, n)\right. \text {. }
$$

又如线性变换

$$
\left\{\begin{array}{l}
y_{1}=\lambda_{1} x_{1} \\
y_{2}=\lambda_{2} x_{2} \\
\cdots \ldots \ldots \ldots \\
y_{n}=\lambda_{n} x_{n}
\end{array}\right.
$$

对应 $n$ 阶方阵

$$
\boldsymbol{\Lambda}=\left(\begin{array}{cccc}
\lambda_{1} & 0 & \cdots & 0 \\
0 & \lambda_{2} & \cdots & 0 \\
\vdots & \vdots & & \vdots \\
0 & 0 & \cdots & \lambda_{n}
\end{array}\right)
$$

这个方阵的特点是: 不在对角线上的元素都是 0 . 这种方阵称为对角矩阵, 简称对角阵. 对角阵也记作

$$
\boldsymbol{\Lambda}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}\right) .
$$

由于矩阵和线性变换之间存在一一对应的关系,因此可以利用矩阵来研究 线性变换,也可以利用线性变换来解释矩阵的含义.

例如矩阵 $\left(\begin{array}{ll}1 & 0 \\ 0 & 0\end{array}\right)$ 所对应的线性变换

$$
\left\{\begin{array}{l}
x_{1}=x, \\
y_{1}=0
\end{array}\right.
$$

可看作是 $x O y$ 平面上把向墨 $\overrightarrow{O P}=\left(\begin{array}{l}x \\ y\end{array}\right)$ 变为向量 $\overrightarrow{O P_{1}}=\left(\begin{array}{l}x_{1} \\ y_{1}\end{array}\right)=\left(\begin{array}{l}x \\ 0\end{array}\right)$ 的变换 (或 看作把点 $P$ 变为点 $P_{1}$ 的变换, 参看图 2.2), 由于向黑 $\overrightarrow{O P}$ 是向量 $\overrightarrow{O P}$ 在 $x$ 轴上 的投影向量(即点 $P_{1}$ 是点 $P$ 在 $x$ 轴上的投影), 因此这是一个投影变换.

又如矩阵 $\left(\begin{array}{rr}\cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi\end{array}\right)$ 对应的线性变换

$$
\left\{\begin{array}{l}
x_{1}=x \cos \varphi-y \sin \varphi, \\
y_{1}=x \sin \varphi+y \cos \varphi
\end{array}\right.
$$

把 $x O y$ 平面上的向量 $\overrightarrow{O P}=\left(\begin{array}{l}x \\ y\end{array}\right)$ 变为向量 $\overrightarrow{O P_{1}}=\left(\begin{array}{l}x_{1} \\ y_{1}\end{array}\right)$. 设 $\overrightarrow{O P}$ 的长度为 $r$, 辐角为 $\theta$, 即设 $x=r \cos \theta, y=r \sin \theta$, 那么

$$
\begin{aligned}
& x_{1}=r(\cos \varphi \cos \theta-\sin \varphi \sin \theta)=r \cos (\theta+\varphi), \\
& y_{1}=r(\sin \varphi \cos \theta+\cos \varphi \sin \theta)=r \sin (\theta+\varphi),
\end{aligned}
$$

表明 $\overrightarrow{O P_{1}}$ 的长度也为 $r$ 而辐角为 $\theta+\varphi$. 因此, 这是把向量 $\overrightarrow{O P}$ (依逆时针方向) 旋 转 $\varphi$ 角 (即把点 $P$ 以原点为中心逆时针旋转 $\varphi$ 角) 的旋转变换 (参看图 2.3).

## $\S 2$ 矩阵的运算

## 一、矩阵的加法

定义 2 设有两个 $m \times n$ 矩阵 $\boldsymbol{A}=\left(a_{i j}\right)$ 和 $\boldsymbol{B}=\left(b_{i j}\right)$, 那么矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 的和 记作 $\boldsymbol{A}+\boldsymbol{B}$, 规定为

$$
\boldsymbol{A}+\boldsymbol{B}=\left(\begin{array}{cccc}
a_{11}+b_{11} & a_{12}+b_{12} & \cdots & a_{1 n}+b_{1 n} \\
a_{21}+b_{21} & a_{22}+b_{22} & \cdots & a_{2 n}+b_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1}+b_{m 1} & a_{m 2}+b_{m 2} & \cdots & a_{m n}+b_{m n}
\end{array}\right) .
$$

应该注意, 只有当两个矩阵是同型矩阵时, 这两个矩阵才能进行加法运算.

矩阵加法满足下列运算规律 (设 $\boldsymbol{A}, \boldsymbol{B}, \boldsymbol{C}$ 都是 $m \times n$ 矩阵) :

(i) $A+B=B+A$;

(ii) $(\boldsymbol{A}+\boldsymbol{B})+\boldsymbol{C}=\boldsymbol{A}+(\boldsymbol{B}+\boldsymbol{C})$.

设矩阵 $\boldsymbol{A}=\left(a_{i j}\right)$, 记

$$
-\boldsymbol{A}=\left(-a_{i j}\right),
$$

$-\boldsymbol{A}$ 称为矩阵 $\boldsymbol{A}$ 的负聟阵,显然有

$$
\boldsymbol{A}+(-\boldsymbol{A})=\boldsymbol{O},
$$

由此规定矩阵的减法为

$$
\boldsymbol{A}-\boldsymbol{B}=\boldsymbol{A}+(-\boldsymbol{B})
$$

## 二、数与矩阵相乘

定义 3 数 $\lambda$ 与聟阵 $\boldsymbol{A}$ 的乘积记作 $\lambda \boldsymbol{A}$ 或 $\boldsymbol{A} \lambda$, 规定为

$$
\lambda \boldsymbol{A}=\boldsymbol{A} \lambda=\left(\begin{array}{cccc}
\lambda a_{11} & \lambda a_{12} & \cdots & \lambda a_{1 n} \\
\lambda a_{21} & \lambda a_{22} & \cdots & \lambda a_{2 n} \\
\vdots & \vdots & & \vdots \\
\lambda a_{m 1} & \lambda a_{m 2} & \cdots & \lambda a_{m n}
\end{array}\right) .
$$

数乘矩阵满足下列运算规律 (设 $\boldsymbol{A}, \boldsymbol{B}$ 为 $m \times n$ 矩阵, $\lambda, \mu$ 为数):

(i) $(\lambda \mu) A=\lambda(\mu \boldsymbol{A})$;

(ii) $(\lambda+\mu) \boldsymbol{A}=\lambda \boldsymbol{A}+\mu \boldsymbol{A}$;

(iii) $\lambda(\boldsymbol{A}+\boldsymbol{B})=\lambda \boldsymbol{A}+\lambda \boldsymbol{B}$.

矩阵相加与数乘矩阵合起来, 统称为矩阵的线性运算.

## 三、矩阵与矩阵相乘

设有两个线性变换

$$
\begin{aligned}
& \left\{\begin{array}{l}
y_{1}=a_{11} x_{1}+a_{12} x_{2}+a_{13} x_{3}, \\
y_{2}=a_{21} x_{1}+a_{22} x_{2}+a_{23} x_{3},
\end{array}\right. \\
& \left\{\begin{array}{l}
x_{1}=b_{11} t_{1}+b_{12} t_{2}, \\
x_{2}=b_{21} t_{1}+b_{22} t_{2}, \\
x_{3}=b_{31} t_{1}+b_{32} t_{2},
\end{array}\right.
\end{aligned}
$$

若想求出从 $t_{1}, t_{2}$ 到 $y_{1}, y_{2}$ 的线性变换, 可将(4)代人 (3), 便得

$$
\left\{\begin{array}{l}
y_{1}=\left(a_{11} b_{11}+a_{12} b_{21}+a_{13} b_{31}\right) t_{1}+\left(a_{11} b_{12}+a_{12} b_{22}+a_{13} b_{32}\right) t_{2}, \\
y_{2}=\left(a_{21} b_{11}+a_{22} b_{21}+a_{23} b_{31}\right) t_{1}+\left(a_{21} b_{12}+a_{22} b_{22}+a_{23} b_{32}\right) t_{2} .
\end{array}\right.
$$

线性变换 (5) 可看成是先作线性变换 (4) 再作线性变换 (3) 的结果. 我们把线 性变换 (5) 叫做线性变换 (3)与 (4) 的乘积, 相应的把 (5)所对应的矩阵定义为 (3) 与(4)所对应的矩阵的乘积, 即

$$
\begin{aligned}
& \left(\begin{array}{lll}
a_{11} & a_{12} & a_{13} \\
a_{21} & a_{22} & a_{23}
\end{array}\right)\left(\begin{array}{ll}
b_{11} & b_{12} \\
b_{21} & b_{22} \\
b_{31} & b_{32}
\end{array}\right) \\
= & \left(\begin{array}{ll}
a_{11} b_{11}+a_{12} b_{21}+a_{13} b_{31} & a_{11} b_{12}+a_{12} b_{22}+a_{13} b_{32} \\
a_{21} b_{11}+a_{22} b_{21}+a_{23} b_{31} & a_{21} b_{12}+a_{22} b_{22}+a_{23} b_{32}
\end{array}\right) .
\end{aligned}
$$

一般的,我们有

定义 4 设 $\boldsymbol{A}=\left(a_{i j}\right)$ 是一个 $m \times s$ 矩阵, $\boldsymbol{B}=\left(b_{i j}\right)$ 是一个 $s \times n$ 矩阵, 那么 规定矩阵 $\boldsymbol{A}$ 与矩阵 $\boldsymbol{B}$ 的乘积是一个 $m \times n$ 矩阵 $\boldsymbol{C}=\left(c_{i j}\right)$,其中

$$
\begin{array}{r}
c_{i j}=a_{i 1} b_{1 j}+a_{i 2} b_{2 j}+\cdots+a_{i s} b_{s j}=\sum_{k=1}^{s} a_{i k} b_{k j} \\
(i=1,2, \cdots, m ; j=1,2, \cdots, n),
\end{array}
$$

并把此乘积记作

$$
\boldsymbol{C}=\boldsymbol{A B} \text {. }
$$

按此定义, 一个 $1 \times s$ 行矩阵与一个 $s \times 1$ 列矩阵的乘积是一个 1 阶方阵, 也 就是一个数

$$
\left(a_{i 1}, a_{i 2}, \cdots, a_{i s}\right)\left(\begin{array}{c}
b_{1 j} \\
b_{2 j} \\
\vdots \\
b_{s j}
\end{array}\right)=a_{i 1} b_{1 j}+a_{i 2} b_{2 j}+\cdots+a_{i s} b_{s j}
$$

$$
=\sum_{k=1}^{s} a_{i k} b_{k j}=c_{i j},
$$

由此表明乘积矩阵 $\boldsymbol{A B}=\boldsymbol{C}$ 的 $(i, j)$ 元 $c_{i j}$ 就是 $\boldsymbol{A}$ 的第 $i$ 行与 $\boldsymbol{B}$ 的第 $j$ 列的乘积.

必须注意: 只有当第一个矩阵 (左矩阵) 的列数等于第二个矩阵(右矩阵) 的 行数时,两个矩阵才能相乘.

例 4 求矩阵

$$
\boldsymbol{A}=\left(\begin{array}{rrrr}
1 & 0 & 3 & -1 \\
2 & 1 & 0 & 2
\end{array}\right) \text { 与 } \boldsymbol{B}=\left(\begin{array}{rrr}
4 & 1 & 0 \\
-1 & 1 & 3 \\
2 & 0 & 1 \\
1 & 3 & 4
\end{array}\right)
$$

的乘积 $\boldsymbol{A B}$.

解 因为 $\boldsymbol{A}$ 是 $2 \times 4$ 矩阵, $\boldsymbol{B}$ 是 $4 \times 3$ 矩阵, $\boldsymbol{A}$ 的列数等于 $\boldsymbol{B}$ 的行数,所以矩 阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 可以相乘, 其乘积 $\boldsymbol{A B}=\boldsymbol{C}$ 是一个 $2 \times 3$ 矩阵. 按公式 (6)有

$$
\begin{aligned}
\boldsymbol{C} & =\boldsymbol{A} \boldsymbol{B}=\left(\begin{array}{rrrr}
1 & 0 & 3 & -1 \\
2 & 1 & 0 & 2
\end{array}\right)\left(\begin{array}{rrr}
4 & 1 & 0 \\
-1 & 1 & 3 \\
2 & 0 & 1 \\
1 & 3 & 4
\end{array}\right) \\
& \left(\begin{array}{ccc}
1 \times 4+0 \times(-1) & 1 \times 1+0 \times 1 & 1 \times 0+0 \times 3 \\
+3 \times 2 & +3 \times 0 & +3 \times 1 \\
+(-1) \times 1 & +(-1) \times 3 & +(-1) \times 4 \\
2 \times 4+1 \times(-1) & 2 \times 1+1 \times 1 & 2 \times 0+1 \times 3 \\
+0 \times 2 & +0 \times 0 & +0 \times 1 \\
+2 \times 1 & +2 \times 3 & +2 \times 4
\end{array}\right) \\
& =\left(\begin{array}{ccc}
9 & -2 & -1 \\
9 & 9 & 11
\end{array}\right) .
\end{aligned}
$$

例 5 求矩阵

$$
A=\left(\begin{array}{rr}
-2 & 4 \\
1 & -2
\end{array}\right) \text { 与 } B=\left(\begin{array}{rr}
2 & 4 \\
-3 & -6
\end{array}\right)
$$

的乘积 $\boldsymbol{A B}$ 及 $\boldsymbol{B A}$.

解 按公式(6),有

$$
\begin{aligned}
& \boldsymbol{A B}=\left(\begin{array}{rr}
-2 & 4 \\
1 & -2
\end{array}\right)\left(\begin{array}{rr}
2 & 4 \\
-3 & -6
\end{array}\right)=\left(\begin{array}{rr}
-16 & -32 \\
8 & 16
\end{array}\right), \\
& \boldsymbol{B} \boldsymbol{A}=\left(\begin{array}{rr}
2 & 4 \\
-3 & -6
\end{array}\right)\left(\begin{array}{rr}
-2 & 4 \\
1 & -2
\end{array}\right)=\left(\begin{array}{ll}
0 & 0 \\
0 & 0
\end{array}\right) .
\end{aligned}
$$

在例 4 中, $\boldsymbol{A}$ 是 $2 \times 4$ 矩阵, $B$ 是 $4 \times 3$ 矩阵,乘积 $\boldsymbol{A B}$ 有意义而 $\boldsymbol{B A}$ 却没有 意义. 由此可知, 在矩阵的乘法中必须注意矩阵相乘的顺序. $\boldsymbol{A B}$ 是 $\boldsymbol{A}$ 左乘 $\boldsymbol{B}(\boldsymbol{B}$ 被 $\boldsymbol{A}$ 左乘) 的乘积, $\boldsymbol{B A}$ 是 $\boldsymbol{A}$ 在乘 $\boldsymbol{B}$ 的乘积, $\boldsymbol{A B}$ 有意义时, $\boldsymbol{B A}$ 可以没有意义. 又若 $\boldsymbol{A}$ 是 $m \times n$ 矩阵, $\boldsymbol{B}$ 是 $n \times m$ 矩阵,则 $\boldsymbol{A B}$ 与 $\boldsymbol{B A}$ 都有意义,但 $\boldsymbol{A B}$ 是 $m \circ$ 阶 方阵, $\boldsymbol{B A}$ 是 $n$ 阶方阵, 当 $m \neq n$ 时 $\boldsymbol{A B} \neq \boldsymbol{B A}$. 即使 $m=n$, 即 $\boldsymbol{A}, \boldsymbol{B}$ 是同阶方阵, 如例 $5, A$ 与 $B$ 都是 2 阶方阵, 从而 $A B$ 与 $B A$ 也都是 2 阶方阵, 但 $A B$ 与 $B A$ 仍 然可以不相等. 总之,矩阵的乘法不满足交换律, 即在一般情形下, $\boldsymbol{A B} \neq \boldsymbol{B} \boldsymbol{A}$.

对于两个 $n$ 阶方阵 $\boldsymbol{A}, \boldsymbol{B}$, 若 $\boldsymbol{A B}=\boldsymbol{B A}$, 则称方阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 是可交换的.

例 5 还表明,矩阵 $A \neq O, B \neq O$, 但却有 $B A=O$. 这就提醒读者要特别注 意: 若有两个矩阵 $\boldsymbol{A}, \boldsymbol{B}$ 满足 $\boldsymbol{A B}=\boldsymbol{O}$, 不能得出 $\boldsymbol{A}=\boldsymbol{O}$ 或 $\boldsymbol{B}=\boldsymbol{O}$ 的结论; 若 $\boldsymbol{A} \neq$ $\boldsymbol{O}$ 而 $\boldsymbol{A}(\boldsymbol{X}-\boldsymbol{Y})=\boldsymbol{O}$, 也不能得出 $\boldsymbol{X}=\boldsymbol{Y}$ 的结论.

矩阵的乘法虽不满足交换律,但仍满足下列结合律和分配律(假设运算都是 可行的):

(i) $(\boldsymbol{A B}) \boldsymbol{C}=\boldsymbol{A}(\boldsymbol{B C})$;

(ii) $\lambda(\boldsymbol{A B})=(\lambda \boldsymbol{A}) \boldsymbol{B}=\boldsymbol{A}(\lambda \boldsymbol{B})$ (其中 $\lambda$ 为数);

(iii) $A(B+C)=A B+A C$,

$$
(B+C) A=B A+C A \text {. }
$$

对于单位矩阵 $E$, 容易验证

$$
\boldsymbol{E}_{m} \boldsymbol{A}_{m \times n}=\boldsymbol{A}_{m \times n}, \boldsymbol{A}_{m \times n} \boldsymbol{E}_{n}=\boldsymbol{A}_{m \times n},
$$

或简写成

$$
E A=A E=A \text {. }
$$

可见单位矩阵 $\boldsymbol{E}$ 在矩阵乘法中的作用类似于数 1. 矩阵

$$
\lambda \boldsymbol{E}=\left(\begin{array}{llll}
\lambda & & & \\
& \lambda & & \\
& & \ddots & \\
& & & \lambda
\end{array}\right)
$$

称为纯量阵. 由 $(\lambda E) A=\lambda A, A(\lambda E)=\lambda \boldsymbol{A}$, 可知纯量阵 $\lambda E$ 与矩阵 $\boldsymbol{A}$ 的乘积等 于数 $\lambda$ 与 $\boldsymbol{A}$ 的乘积. 并且当 $\boldsymbol{A}$ 为 $n$ 阶方阵时,有

$$
\left(\lambda E_{n}\right) A_{n}=\lambda A_{n}=A_{n}\left(\lambda E_{n}\right),
$$

表明纯量阵 $\lambda E$ 与任何同阶方阵都是可交换的.

有了矩阵的乘法, 就可以定义䓡阵的幂. 设 $\boldsymbol{A}$ 是 $n$ 阶方阵,定义

$$
A^{1}=A, A^{2}=A^{1} A^{1}, \cdots, A^{k+1}=A^{k} A^{1} \text {, }
$$

其中 $k$ 为正整数,这就是说, $\boldsymbol{A}^{k}$ 就是 $k$ 个 $\boldsymbol{A}$ 连乘. 显然只有方阵, 它的㝤才有意 义.

由于矩阵乘法适合结合律, 所以矩阵的幂满足以下运算规律:

$$
\boldsymbol{A}^{k} \boldsymbol{A}^{\prime}=\boldsymbol{A}^{k+1},\left(\boldsymbol{A}^{k}\right)^{\prime}=\boldsymbol{A}^{\mu},
$$

其中 $k, l$ 为正整数. 又因矩阵乘法一般不满足交换律, 所以对于两个 $n$ 阶矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$,一般说来 $(\boldsymbol{A B})^{k} \neq \boldsymbol{A}^{k} \boldsymbol{B}^{k}$, 只有当 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 可交换时, 才有 $(\boldsymbol{A B})^{k}=\boldsymbol{A}^{k} \boldsymbol{B}^{k}$. 类似可知, 例如 $(A+B)^{2}=A^{2}+2 A B+B^{2},(A-B)(A+B)=A^{2}-B^{2}$ 等公 式,也只有当 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 可交换时才成立.

上节例 1 中有一个向三个商店发送四种产品的数量所构成的矩阵 $\boldsymbol{A} 、$ 一个 四种产品的单价与单件重量所构成的矩阵 $\boldsymbol{B}$, 按矩阵相乘的定义, 可知 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 的乘积矩阵 $\boldsymbol{A B}=\boldsymbol{C}=\left(c_{i j}\right)_{3 \times 2}$ 为向三个商店所发产品的总值及总重墨所构成的 矩阵, 即 $c_{i 1}$ 为向第 $i$ 店所发产品的总值, $c_{i 2}$ 为向第 $i$ 店所发产品的总重墨.

上节例 2 中有一个四城市间的单向航线矩阵 $\boldsymbol{A}$, 由

$$
\boldsymbol{A}=\left(\begin{array}{llll}
0 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
1 & 0 & 1 & 0
\end{array}\right) \text {, 有 } \boldsymbol{A}^{2}=\left(\begin{array}{llll}
2 & 1 & 1 & 0 \\
0 & 1 & 1 & 1 \\
1 & 0 & 0 & 0 \\
0 & 2 & 1 & 1
\end{array}\right) \text {. }
$$

记 $\boldsymbol{A}^{2}=\left(b_{i j}\right)$, 则 $b_{i j}$ 为从 $i$ 市经一次中转到 $j$ 市的单向航线条数.

例如

$b_{23}=1$,显示从(2)市经一次中转到(3)市的单向航线有 1 条 (2) $\rightarrow$ (1) $\rightarrow$ (3), 参 看图 2.1);

$b_{42}=2$, 显示从(4)市经一次中转到(2)市的单向航线有 2 条 (4) $\rightarrow$ (1) $\rightarrow$ (2), (4) $\rightarrow$ (3) $\rightarrow$ (2));

$b_{11}=2$, 显示过(1)市的双向航线有 2 条 (1) $\rightarrow$ (2) $\rightarrow$ (1), (1) $\rightarrow$ (4) $\rightarrow$ (1) );

$b_{33}=0$,显示(3)市没有双向航线.

上节例 3 中的线性变换

$$
\left\{\begin{array}{l}
y_{1}=a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}, \\
y_{2}=a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}, \\
\cdots \cdots \cdots \cdots \\
y_{m}=a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n},
\end{array}\right.
$$

利用矩阵的乘法, 可记作

$$
\boldsymbol{Y}=\boldsymbol{A X},
$$

其中

$$
\boldsymbol{A}=\left(a_{i j}\right), \boldsymbol{X}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right), \boldsymbol{Y}=\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{m}
\end{array}\right) \text {. }
$$

这里,列向量(列矩阵) $\boldsymbol{X}$ 表示 $n$ 个变量 $x_{1}, x_{2}, \cdots, x_{n}$,列向量 $\boldsymbol{Y}$ 表示 $m$ 个 变量 $y_{1}, y_{2}, \cdots, y_{m}$. 线性变换 (2) 把 $\boldsymbol{X}$ 变成 $\boldsymbol{Y}$,相当于用矩阵 $\boldsymbol{A}$ 去左乘 $\boldsymbol{X}$ 得到 $\boldsymbol{Y}$.

用矩阵 $\boldsymbol{A}=\left(\begin{array}{ll}1 & 0 \\ 0 & 0\end{array}\right)$ 去左乘向量 $\overrightarrow{O P}=\left(\begin{array}{l}x \\ y\end{array}\right)$,相当于把向量 $\overrightarrow{O P}$ 投影到 $X$ 轴上 (参看图 2.2).

用矩阵 $\boldsymbol{A}=\left(\begin{array}{cc}\cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi\end{array}\right)$ 左乘向量 $\overrightarrow{O P}=\left(\begin{array}{l}x \\ y\end{array}\right)$, 相当于把向量 $\overrightarrow{O P}$ 旋转 $\varphi$ 角(参看图 2.3). 进一步还可推知, 以 $A^{n}=\left(\begin{array}{cc}\cos \varphi & -\sin \varphi \\ \sin \varphi & \cos \varphi\end{array}\right)^{n}$ 左乘向量 $\overrightarrow{O P}$, 应 把向量 $\overrightarrow{O P}$ 旋转 $n$ 个 $\varphi$ 角, 即旋转 $n \varphi$ 角, 而旋转 $n \varphi$ 角所对应的矩阵为 $\left(\begin{array}{cc}\cos n \varphi & -\sin n \varphi \\ \sin n \varphi & \cos n \varphi\end{array}\right)$.

例 6 证明

$$
\left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)^{n}=\left(\begin{array}{cc}
\cos n \varphi & -\sin n \varphi \\
\sin n \varphi & \cos n \varphi
\end{array}\right) .
$$

从前段说明已能推知本例的结论,下面按矩阵幂的定义来证明此结论.

证 用数学归纳法. 当 $n=1$ 时,等式显然成立. 设 $n=k$ 时成立,即设

要证 $n=k+1$ 时成立. 此时有

$$
\left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)^{k}=\left(\begin{array}{cc}
\cos k \varphi & -\sin k \varphi \\
\sin k \varphi & \cos k \varphi
\end{array}\right) \text {, }
$$

$$
\begin{aligned}
& \left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)^{k+1} \\
= & \left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)^{k}\left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right) \\
= & \left(\begin{array}{cc}
\cos k \varphi & -\sin k \varphi \\
\sin k \varphi & \cos k \varphi
\end{array}\right)\left(\begin{array}{cc}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right) \\
= & \left(\begin{array}{cc}
\cos k \varphi \cos \varphi-\sin k \varphi \sin \varphi & -\cos k \varphi \sin \varphi-\sin k \varphi \cos \varphi \\
\sin k \varphi \cos \varphi+\cos k \varphi \sin \varphi & -\sin k \varphi \sin \varphi+\cos k \varphi \cos \varphi
\end{array}\right) \\
= & \left(\begin{array}{cc}
\cos (k+1) \varphi & -\sin (k+1) \varphi \\
\sin (k+1) \varphi & \cos (k+1) \varphi
\end{array}\right),
\end{aligned}
$$

于是等式得证.

## 四、矩阵的转置

定义 5 把矩阵 $\boldsymbol{A}$ 的行换成同序数的列得到一个新矩阵, 叫做 $\boldsymbol{A}$ 的转置矩 阵, 记作 $\boldsymbol{A}^{\mathrm{T}}$. 例如矩阵

$$
\boldsymbol{A}=\left(\begin{array}{rrr}
1 & 2 & 0 \\
3 & -1 & 1
\end{array}\right)
$$

的转置矩阵为

$$
\boldsymbol{A}^{\mathrm{T}}=\left(\begin{array}{rr}
1 & 3 \\
2 & -1 \\
0 & 1
\end{array}\right) \text {. }
$$

矩阵的转置也是一种运算，满足下述运算规律 (假设运算都是可行的):

(i) $\left(\boldsymbol{A}^{\mathrm{T}}\right)^{\mathrm{T}}=\boldsymbol{A}$;

(ii) $(\boldsymbol{A}+\boldsymbol{B})^{\mathrm{T}}=\boldsymbol{A}^{\mathrm{T}}+\boldsymbol{B}^{\mathrm{T}}$;

(iii) $(\lambda \boldsymbol{A})^{\mathrm{T}}=\lambda \boldsymbol{A}^{\mathrm{T}}$;

(iv) $(\boldsymbol{A B})^{\mathrm{T}}=\boldsymbol{B}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}$.

这里仅证明 (iv). 设 $\boldsymbol{A}=\left(a_{i j}\right)_{m \times s}, \boldsymbol{B}=\left(b_{i j}\right)_{s \times n}$, 记 $\boldsymbol{A B}=\boldsymbol{C}=\left(c_{i j}\right)_{m \times n}$, $\boldsymbol{B}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}=\boldsymbol{D}=\left(d_{i j}\right)_{n \times m}$. 于是按公式(6), 有

$$
c_{j i}=\sum_{k=1}^{s} a_{j k} b_{k i},
$$

而 $\boldsymbol{B}^{\mathrm{T}}$ 的第 $i$ 行为 $\left(b_{1 i}, \cdots, b_{s i}\right), \boldsymbol{A}^{\mathrm{T}}$ 的第 $j$ 列为 $\left(a_{j 1}, \cdots, a_{j s}\right)^{\mathrm{T}}$, 因此

所以

$$
d_{i j}=\sum_{k=1}^{s} b_{k i} a_{j k}=\sum_{k=1}^{s} a_{j k} b_{k i},
$$

即 $\boldsymbol{D}=\boldsymbol{C}^{\mathrm{T}}$, 亦即

$$
d_{i j}=c_{j i} \quad(i=1,2, \cdots, n ; j=1,2, \cdots, m) \text {, }
$$

求 $(\boldsymbol{A B})^{\mathrm{T}}$.

$$
\boldsymbol{B}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}=(\boldsymbol{A B})^{\mathrm{T}}
$$

例 7 已知

$$
\boldsymbol{A}=\left(\begin{array}{rrr}
2 & 0 & -1 \\
1 & 3 & 2
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{rrr}
1 & 7 & -1 \\
4 & 2 & 3 \\
2 & 0 & 1
\end{array}\right)
$$

解法 1 因为

所以

$$
\begin{gathered}
\boldsymbol{A B}=\left(\begin{array}{rrr}
2 & 0 & -1 \\
1 & 3 & 2
\end{array}\right)\left(\begin{array}{rrr}
1 & 7 & -1 \\
4 & 2 & 3 \\
2 & 0 & 1
\end{array}\right)=\left(\begin{array}{ccc}
0 & 14 & -3 \\
17 & 13 & 10
\end{array}\right), \\
(\boldsymbol{A B})^{\mathrm{T}}=\left(\begin{array}{cc}
0 & 17 \\
14 & 13 \\
-3 & 10
\end{array}\right) .
\end{gathered}
$$

解法 2

$$
(\boldsymbol{A B})^{\mathrm{T}}=\boldsymbol{B}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}=\left(\begin{array}{rrr}
1 & 4 & 2 \\
7 & 2 & 0 \\
-1 & 3 & 1
\end{array}\right)\left(\begin{array}{rr}
2 & 1 \\
0 & 3 \\
-1 & 2
\end{array}\right)=\left(\begin{array}{rr}
0 & 17 \\
14 & 13 \\
-3 & 10
\end{array}\right)
$$

设 $\boldsymbol{A}$ 为 $n$ 阶方阵,如果满足 $\boldsymbol{A}^{\mathrm{T}}=\boldsymbol{A}$, 即

$$
a_{i j}=a_{j i}(i, j=1,2, \cdots, n),
$$

那么 $\boldsymbol{A}$ 称为对称矩阵, 简称对称阵. 对称阵的特点是: 它的元素以对角线为对称 轴对应相等.

例 8 设列矩阵 $\boldsymbol{X}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}}$ 满足 $\boldsymbol{X}^{\mathrm{T}} \boldsymbol{X}=1, \boldsymbol{E}$ 为 $n$ 阶单位阵, $\boldsymbol{H}$ $=\boldsymbol{E}-2 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}$, 证明 $\boldsymbol{H}$ 是对称阵, 且 $\boldsymbol{H} \boldsymbol{H}^{\mathrm{T}}=\boldsymbol{E}$.

证明前先提醒读者注意: $\boldsymbol{X}^{\mathrm{T}} \boldsymbol{X}=x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}$ 是一阶方阵, 也就是一个 数, 而 $\boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}$ 是 $n$ 阶方阵.

证

$$
\begin{aligned}
\boldsymbol{H}^{\mathrm{T}} & =\left(\boldsymbol{E}-2 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}\right)^{\mathrm{T}} \\
& =\boldsymbol{E}^{\mathrm{T}}-2\left(\boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}\right)^{\mathrm{T}} \\
& =\boldsymbol{E}-2 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}=\boldsymbol{H},
\end{aligned}
$$

所以 $\boldsymbol{H}$ 是对称阵.

$$
\begin{aligned}
\boldsymbol{H} \boldsymbol{H}^{\mathrm{T}} & =\boldsymbol{H}^{2}=\left(\boldsymbol{E}-2 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}\right)^{2} \\
& =\boldsymbol{E}-4 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}+4\left(\boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}\right)\left(\boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}\right) \\
& =\boldsymbol{E}-4 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}+4 \boldsymbol{X}\left(\boldsymbol{X}^{\mathrm{T}} \boldsymbol{X}\right) \boldsymbol{X}^{\mathrm{T}} \\
& =\boldsymbol{E}-4 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}+4 \boldsymbol{X} \boldsymbol{X}^{\mathrm{T}}=\boldsymbol{E} .
\end{aligned}
$$

## 五、方阵的行列式

定义 6 由 $n$ 阶方阵 $\boldsymbol{A}$ 的元素所构成的行列式 (各元素的位置不变), 称为 方阵 $\boldsymbol{A}$ 的行列式, 记作 $|\boldsymbol{A}|$ 或 $\operatorname{det} \boldsymbol{A}$.

应该注意, 方阵与行列式是两个不同的概念, $n$ 阶方阵是 $n^{2}$ 个数按一定方 式排成的数表,而 $n$ 阶行列式则是这些数(也就是数表 $\boldsymbol{A}$ ) 按一定的运算法则所 确定的一个数.

由 $\boldsymbol{A}$ 确定 $|\boldsymbol{A}|$ 的这个运算满足下述运算规律 (设 $\boldsymbol{A}, \boldsymbol{B}$ 为 $n$ 阶方阵, $\lambda$ 为 数):

(i) $\left|\boldsymbol{A}^{\mathrm{T}}\right|=|\boldsymbol{A}|$ (行列式性质 1);

(ii) $|\lambda \boldsymbol{A}|=\lambda^{n}|\boldsymbol{A}|$;

(iii) $|\boldsymbol{A B}|=|\boldsymbol{A}||\boldsymbol{B}|$.

我们仅证明(iii). 设 $\boldsymbol{A}=\left(a_{i j}\right), \boldsymbol{B}=\left(b_{i j}\right)$. 记 $2 n$ 阶行列式

$$
D=\left|\begin{array}{cccccc}
a_{11} & \cdots & a_{1 n} & & & \\
\vdots & & \vdots & & \boldsymbol{O} & \\
a_{n 1} & \cdots & a_{n n} & & & \\
-1 & & & b_{11} & \cdots & b_{1 n} \\
& \ddots & & \vdots & & \vdots \\
& & -1 & b_{n 1} & \cdots & b_{n n}
\end{array}\right|=\left|\begin{array}{cc}
\boldsymbol{A} & \boldsymbol{O} \\
-\boldsymbol{E} & \boldsymbol{B}
\end{array}\right|,
$$

由第一章例 10 可知 $D=|\boldsymbol{A}||\boldsymbol{B}|$, 而在 $D$ 中以 $b_{1 j}$ 乘第 1 列, $b_{2 j}$ 乘第 2 列, $\cdots$, $b_{n j}$ 乘第 $n$ 列, 都加到第 $n+j$ 列上 $(j=1,2, \cdots, n)$, 有

$$
D=\left|\begin{array}{rr}
\boldsymbol{A} & \boldsymbol{C} \\
-\boldsymbol{E} & \boldsymbol{O}
\end{array}\right|
$$

其中 $\boldsymbol{C}=\left(c_{i j}\right), c_{i j}=b_{1 j} a_{i 1}+b_{2 j} a_{i 2}+\cdots+b_{n j} a_{i n}$, 故 $\boldsymbol{C}=\boldsymbol{A B}$.

再对 $D$ 的行作 $r_{j} \leftrightarrow r_{n+j}(j=1,2, \cdots, n)$, 有

$$
D=(-1)^{n}\left|\begin{array}{rr}
-\boldsymbol{E} & \boldsymbol{O} \\
\boldsymbol{A} & \boldsymbol{C}
\end{array}\right|
$$

从而按第一章例 10 有

$$
D=(-1)^{n}|-\boldsymbol{E}||\boldsymbol{C}|=(-1)^{n}(-1)^{n}|\boldsymbol{C}|=|\boldsymbol{C}|=|\boldsymbol{A B}|,
$$

于是

$$
|\boldsymbol{A B}|=|\boldsymbol{A}||\boldsymbol{B}| \text {. }
$$

由(iii) 可知,对于 $n$ 阶矩阵 $\boldsymbol{A}, \boldsymbol{B}$, 一般来说 $\boldsymbol{A B} \neq \boldsymbol{B} \boldsymbol{A}$, 但总有

$$
|\boldsymbol{A B}|=|\boldsymbol{B A}| \text {. }
$$

例 9 行列式 $|\boldsymbol{A}|$ 的各个元素的代数余子式 $A_{i j}$ 所构成的如下的矩阵

$$
\boldsymbol{A}^{\cdot}=\left(\begin{array}{cccc}
A_{11} & A_{21} & \cdots & A_{n 1} \\
A_{12} & A_{22} & \cdots & A_{n 2} \\
\vdots & \vdots & & \vdots \\
A_{1 n} & A_{2 n} & \cdots & A_{n n}
\end{array}\right),
$$

称为矩阵 $\boldsymbol{A}$ 的伴随矩阵, 简称伴随阵. 试证

$$
\boldsymbol{A A} \boldsymbol{A}^{*}=\boldsymbol{A}^{*} \boldsymbol{A}=|\boldsymbol{A}| \boldsymbol{E} \text {. }
$$

证 设 $\boldsymbol{A}=\left(a_{i j}\right)$, 记 $\boldsymbol{A A}^{*}=\left(b_{i j}\right)$, 则

$$
b_{i j}=a_{i 1} A_{j 1}+a_{i 2} A_{j 2}+\cdots+a_{i n} A_{j n}=|A| \delta_{i j},
$$

故

$$
\boldsymbol{A A}^{*}=\left(|\boldsymbol{A}| \delta_{i j}\right)=|\boldsymbol{A}|\left(\delta_{i j}\right)=|\boldsymbol{A}| \boldsymbol{E} \text {. }
$$

类似有

$$
\boldsymbol{A}^{\cdot} \boldsymbol{A}=\left(\sum_{k=1}^{n} A_{k i} a_{k j}\right)=\left(\begin{array}{lll}
\mid \boldsymbol{A} & \mid \delta_{i j}
\end{array}\right)=|\boldsymbol{A}|\left(\delta_{i j}\right)=|\boldsymbol{A}| \boldsymbol{E} .
$$

## 六、共轭矩阵

当 $\boldsymbol{A}=\left(a_{i j}\right)$ 为复矩阵时, 用 $\bar{a}_{i j}$ 表示 $a_{i j}$ 的共轭复数,记

$$
\overline{\boldsymbol{A}}=\left(\bar{a}_{i j}\right),
$$

$\bar{A}$ 称为 $\boldsymbol{A}$ 的基轭矩阵.

共轮矩阵满足下述运算规律 (设 $\boldsymbol{A}, \boldsymbol{B}$ 为复矩阵， $\lambda$ 为复数，且运算都是可行的）；

(i) $\overline{\boldsymbol{A}+\boldsymbol{B}}=\overline{\boldsymbol{A}}+\bar{B}$;

(ii) $\overline{\lambda A}=\overline{\lambda A}$;

(iii) $\overline{\boldsymbol{A B}}=\overline{\boldsymbol{A}} \overline{\boldsymbol{B}}$.

## $\S 3$ 逆 矩 阵

设给定一个线性变换

$$
\left\{\begin{array}{l}
y_{1}=a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}, \\
y_{2}=a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}, \\
\cdots \cdots \cdots \cdots \\
y_{n}=a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n},
\end{array}\right.
$$

它的系数矩阵是一个 $n$ 阶矩阵 $\boldsymbol{A}$, 若记

$$
\boldsymbol{X}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right), \mathbf{Y}=\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right),
$$

则线性变换 (7) 可记作

$$
\boldsymbol{Y}=\boldsymbol{A} \boldsymbol{X} .
$$

以 $\boldsymbol{A}$ 的伴随阵 $\boldsymbol{A}$ *左乘上式两端,并利用例 9 的结果, 可得

$$
A^{*} \boldsymbol{Y}=\boldsymbol{A}^{*} \boldsymbol{A X} \text {, 即 } \boldsymbol{A}^{*} \boldsymbol{Y}=|\boldsymbol{A}| \boldsymbol{X} \text {, }
$$

当 $|A| \neq 0$ 时, 可解出

$$
\boldsymbol{X}=\frac{1}{|\boldsymbol{A}|^{*}} \boldsymbol{A}^{*} \boldsymbol{Y}
$$

记 $\boldsymbol{B}=\frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{*}$ ，上式可记作

$$
\boldsymbol{X}=\boldsymbol{B} \boldsymbol{Y} .
$$

(9)式表示一个从 $\boldsymbol{Y}$ 到 $\boldsymbol{X}$ 的线性变换,称为线性变换 (8) 的逆变换.

我们从 (8), (9) 两式分析变换所对应的方阵 $A$ 与逆变换所对应的方阵 B 之 间的关系.用(9)代人 $(8)$, 可得

$$
\boldsymbol{Y}=\boldsymbol{A}(\boldsymbol{B} \boldsymbol{Y})=(\boldsymbol{A B}) \boldsymbol{Y},
$$

可见 $\boldsymbol{A B}$ 为恒等变换所对应的矩阵, 故 $\boldsymbol{A B}=\boldsymbol{E}$. 用 $(8)$ 代人(9)得

$$
\boldsymbol{X}=\boldsymbol{B}(\boldsymbol{A X})=(\boldsymbol{B A}) \boldsymbol{X},
$$

知有 $\boldsymbol{B A}=\boldsymbol{E}$. 于是有

$$
\boldsymbol{A B}=\boldsymbol{B A}=\boldsymbol{E}:
$$

由此我们引人逆矩阵的定义.

定义 7 对于 $n$ 阶矩阵 $\boldsymbol{A}$, 如果有一个 $n$ 阶矩阵 $\boldsymbol{B}$, 使

$$
\boldsymbol{A B}=\boldsymbol{B A}=\boldsymbol{E},
$$

则说矩阵 $\boldsymbol{A}$ 是可逆的,并把矩阵 $\boldsymbol{B}$ 称为 $\boldsymbol{A}$ 的逆矩阵,简称逆阵.

如果矩阵 $\boldsymbol{A}$ 是可逆的,那么 $\boldsymbol{A}$ 的逆阵是惟一的. 这是因为: 设 $B, C$ 都是 $A$ 的逆阵, 则有

$$
B=B E=B(A C)=(B A) C=E C=C,
$$

所以 $\boldsymbol{A}$ 的逆阵是惟一的.

$\boldsymbol{A}$ 的逆阵记作 $\boldsymbol{A}^{-1}$. 即若 $\boldsymbol{A B}=\boldsymbol{B A}=\boldsymbol{E}$, 则 $\boldsymbol{B}=\boldsymbol{A}^{-1}$.

定理 1 著矩阵 $\boldsymbol{A}$ 可逆,则 $|\boldsymbol{A}| \neq 0$.

证 $\boldsymbol{A}$ 可逆, 即有 $\boldsymbol{A}^{-1}$, 使 $\boldsymbol{A A} \boldsymbol{A}^{-1}=\boldsymbol{E}$. 故 $|\boldsymbol{A}| \cdot\left|\boldsymbol{A}^{-1}\right|=|\boldsymbol{E}|=1$, 所以 $|\boldsymbol{A}|$ $\neq 0$.

定理 2 若 $|\boldsymbol{A}| \neq 0$, 则矩阵 $\boldsymbol{A}$ 可逆, 且

$$
A^{-1}=\frac{1}{|A|^{A}} \text {, }
$$

其中 $A^{*}$ 为矩阵 $A$ 的伴随阵.

证由例 9 知

$$
\boldsymbol{A A}^{*}=\boldsymbol{A}^{*} \boldsymbol{A}=|\boldsymbol{A}| \boldsymbol{E},
$$

因 $|\boldsymbol{A}| \neq 0$, 故有

$$
\boldsymbol{A} \frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{*}=\frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{:}: \boldsymbol{A}=\boldsymbol{E},
$$

所以,按逆阵的定义, 即知 $\boldsymbol{A}$ 可逆,且有

$$
\boldsymbol{A}^{-1}=\frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{*} \text {. }
$$

证毕

当 $|\boldsymbol{A}|=0$ 时, $\boldsymbol{A}$ 称为奇异䓡阵,否则称非奇异䓡阵. 由上面两定理可知: $\boldsymbol{A}$ 是可逆矩阵的充分必要条件是 $|\boldsymbol{A}| \neq 0$, 即可逆矩阵就是非奇异矩阵.

由定理 2 , 可得下述推论.

推论 若 $A B=E$ (或 $B A=E$ ), 则 $B=A^{-1}$.

证 $|\boldsymbol{A}| \cdot|\boldsymbol{B}|=|\boldsymbol{E}|=1$, 故 $|\boldsymbol{A}| \neq 0$, 因而 $\boldsymbol{A}^{-1}$ 存在, 于是

$$
B=E B=\left(A^{-1} A\right) B=A^{-1}(A B)=A^{-1} E=A^{-1} \text {. }
$$

证毕

方阵的逆阵满足下述运算规律: （i）若 $\boldsymbol{A}$ 可逆,则 $\boldsymbol{A}^{-1}$ 亦可逆,且 $\left(\boldsymbol{A}^{-1}\right)^{-1}=\boldsymbol{A}$.

(ii) 若 $A$ 可逆,数 $\lambda \neq 0$, 则 $\lambda A$ 可逆,且 $(\lambda A)^{-1}=\frac{1}{\lambda} A^{-1}$.

(iii) 若 $\boldsymbol{A}, \boldsymbol{B}$ 为同阶矩阵且均可逆,则 $\boldsymbol{A B}$ 亦可逆,且

$$
(A B)^{-1}=B^{-1} A^{-1} \text {. }
$$

证 $(\boldsymbol{A B})\left(\boldsymbol{B}^{-1} \boldsymbol{A}^{-1}\right)=\boldsymbol{A}\left(\boldsymbol{B B} \boldsymbol{B}^{-1}\right) \boldsymbol{A}^{-1}=\boldsymbol{A E A ^ { - 1 }}=\boldsymbol{A A} \boldsymbol{A}^{-1}=\boldsymbol{E}$, 由推论, 即 有 $(\boldsymbol{A B})^{-1}=\boldsymbol{B}^{-1} \boldsymbol{A}^{-1}$.

(iv) 若 $A$ 可逆,则 $\boldsymbol{A}^{\mathrm{T}}$ 亦可逆,且 $\left(\boldsymbol{A}^{\mathrm{T}}\right)^{-1}=\left(\boldsymbol{A}^{-1}\right)^{\mathrm{T}}$.

证

$$
\boldsymbol{A}^{\mathrm{T}}\left(\boldsymbol{A}^{-1}\right)^{\mathrm{T}}=\left(\boldsymbol{A}^{-1} \boldsymbol{A}\right)^{\mathrm{T}}=\boldsymbol{E}^{\mathrm{T}}=\boldsymbol{E},
$$

所以

$$
\left(A^{\mathrm{T}}\right)^{-1}=\left(A^{-1}\right)^{\mathrm{T}} \text {. }
$$

当 $\boldsymbol{A}$ 可逆时,还可定义

$$
\boldsymbol{A}^{0}=\boldsymbol{E}, \boldsymbol{A}^{-k}=\left(\boldsymbol{A}^{-1}\right)^{k},
$$

其中 $k$ 为正整数. 这样,当 $\boldsymbol{A}$ 可逆, $\lambda 、 \mu$ 为整数时, 有

$$
\boldsymbol{A}^{\lambda} \boldsymbol{A}^{\mu}=\boldsymbol{A}^{\lambda+\mu},\left(\boldsymbol{A}^{\lambda}\right)^{\mu}=\boldsymbol{A}^{\lambda \mu} \text { 。 }
$$

例 10 求二阶矩阵 $\boldsymbol{A}=\left(\begin{array}{ll}a & b \\ c & d\end{array}\right)$ 的逆阵.

解 $|\boldsymbol{A}|=a d-b c, \boldsymbol{A}^{*}=\left(\begin{array}{rr}d & -b \\ -c & a\end{array}\right)$,

利用逆阵公式 (10), 当 $|\boldsymbol{A}| \neq 0$ 时, 有

$$
\boldsymbol{A}^{-1}=\frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{*}=\frac{1}{a d-b c}\left(\begin{array}{rr}
d & -b \\
-c & a
\end{array}\right) .
$$

例 11 求方阵

$$
A=\left(\begin{array}{lll}
1 & 2 & 3 \\
2 & 2 & 1 \\
3 & 4 & 3
\end{array}\right)
$$

的逆阵.

解 求得 $|\boldsymbol{A}|=2 \neq 0$, 知 $\boldsymbol{A}^{-1}$ 存在. 再计算 $|\boldsymbol{A}|$ 的余子式

$$
\begin{gathered}
M_{11}=2, \quad M_{12}=3, \quad M_{13}=2, \\
M_{21}=-6, \quad M_{22}=-6, \quad M_{23}=-2, \\
M_{31}=-4, \quad M_{32}=-5, \quad M_{33}=-2, \\
A^{*}=\left(\begin{array}{rrr}
M_{11} & -M_{21} & M_{31} \\
-M_{12} & M_{22} & -M_{32} \\
M_{13} & -M_{23} & M_{33}
\end{array}\right)=\left(\begin{array}{rrr}
2 & 6 & -4 \\
-3 & -6 & 5 \\
2 & 2 & -2
\end{array}\right),
\end{gathered}
$$

所以

$$
\boldsymbol{A}^{-1}=\frac{1}{|\boldsymbol{A}|} \boldsymbol{A}^{*}=\left(\begin{array}{rrr}
1 & 3 & -2 \\
-\frac{3}{2} & -3 & \frac{5}{2} \\
1 & 1 & -1
\end{array}\right)
$$

例 12 设

## 求矩阵 $\boldsymbol{X}$ 使其满足

$$
A=\left(\begin{array}{lll}
1 & 2 & 3 \\
2 & 2 & 1 \\
3 & 4 & 3
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{ll}
2 & 1 \\
5 & 3
\end{array}\right), \boldsymbol{C}=\left(\begin{array}{ll}
1 & 3 \\
2 & 0 \\
3 & 1
\end{array}\right),
$$

$$
A X B=C .
$$

解 若 $\boldsymbol{A}^{-1}, \boldsymbol{B}^{-1}$ 存在, 则用 $\boldsymbol{A}^{-1}$ 左乘上式, $\boldsymbol{B}^{-1}$ 右乘上式,有

即

$$
\begin{gathered}
A^{-1} A X B B^{-1}=A^{-1} C B^{-1}, \\
X=A^{-1} C B^{-1} .
\end{gathered}
$$

由上例知 $|\boldsymbol{A}| \neq 0$, 而 $|\boldsymbol{B}|=1$, 故知 $\boldsymbol{A}, \boldsymbol{B}$ 都可逆,且

$$
\begin{aligned}
& \boldsymbol{A}^{-1}=\left(\begin{array}{rrr}
1 & 3 & -2 \\
-\frac{3}{2} & -3 & \frac{5}{2} \\
1 & 1 & -1
\end{array}\right), \boldsymbol{B}^{-1}=\left(\begin{array}{rr}
3 & -1 \\
-5 & 2
\end{array}\right), \\
& \boldsymbol{X}=\boldsymbol{A}^{-1} \boldsymbol{C} \boldsymbol{B}^{-1}=\left(\begin{array}{rrr}
1 & 3 & -2 \\
-\frac{3}{2} & -3 & \frac{5}{2} \\
1 & 1 & -1
\end{array}\right)\left(\begin{array}{rr}
1 & 3 \\
2 & 0 \\
3 & 1
\end{array}\right)\left(\begin{array}{rr}
3 & -1 \\
-5 & 2
\end{array}\right) \\
&=\left(\begin{array}{rr}
1 & 1 \\
0 & -2 \\
0 & 2
\end{array}\right)\left(\begin{array}{rr}
3 & -1 \\
-5 & 2
\end{array}\right)=\left(\begin{array}{rr}
-2 & 1 \\
10 & -4 \\
-10 & 4
\end{array}\right) .
\end{aligned}
$$

例 13 设 $P=\left(\begin{array}{ll}1 & 2 \\ 1 & 4\end{array}\right), \boldsymbol{\Lambda}=\left(\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right), \boldsymbol{A P}=P \Lambda$, 求 $\boldsymbol{A}^{\prime \prime}$.

解

$$
|\boldsymbol{P}|=2, \boldsymbol{P}^{-1}=\frac{1}{2}\left(\begin{array}{rr}
4 & -2 \\
-1 & 1
\end{array}\right)
$$

$$
\boldsymbol{A}=\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}^{-1}, \boldsymbol{A}^{2}=\boldsymbol{P} \boldsymbol{A} \boldsymbol{P}^{-1} \mathbf{P} \boldsymbol{A} \boldsymbol{P}^{-1}=\boldsymbol{P} \boldsymbol{\Lambda}^{2} \boldsymbol{P}^{-1}, \cdots, \boldsymbol{A}^{n}=\mathbf{P} \boldsymbol{\Lambda}^{n} \boldsymbol{P}^{-1},
$$

而 $\boldsymbol{\Lambda}=\left(\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right), \boldsymbol{\Lambda}^{2}=\left(\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right)\left(\begin{array}{ll}1 & 0 \\ 0 & 2\end{array}\right)=\left(\begin{array}{cc}1 & 0 \\ 0 & 2^{2}\end{array}\right), \cdots, \boldsymbol{\Lambda}^{n}=\left(\begin{array}{cc}1 & 0 \\ 0 & 2^{n}\end{array}\right)$,

故 $\quad A^{n}=\left(\begin{array}{ll}1 & 2 \\ 1 & 4\end{array}\right)\left(\begin{array}{cc}1 & 0 \\ 0 & 2^{n}\end{array}\right) \frac{1}{2}\left(\begin{array}{rr}4 & -2 \\ -1 & 1\end{array}\right)=\frac{1}{2}\left(\begin{array}{ll}1 & 2^{n+1} \\ 1 & 2^{n+2}\end{array}\right)\left(\begin{array}{rr}4 & -2 \\ -1 & 1\end{array}\right)$

$$
=\frac{1}{2}\left(\begin{array}{ll}
4-2^{n+1} & 2^{n+1}-2 \\
4-2^{n+2} & 2^{n+2}-2
\end{array}\right)=\left(\begin{array}{cc}
2-2^{n} & 2^{n}-1 \\
2-2^{n+1} & 2^{n+1}-1
\end{array}\right) \text {. }
$$

设

$$
\varphi(x)=a_{0}+a_{1} x+\cdots+a_{m} x^{m}
$$

为 $x$ 的 $m$ 次多项式, $\boldsymbol{A}$ 为 $n$ 阶矩阵, 记

$$
\varphi(\boldsymbol{A})=a_{0} \boldsymbol{E}+a_{1} \boldsymbol{A}+\cdots+a_{m} \boldsymbol{A}^{m},
$$

$\varphi(A)$ 称为矩阵 $A$ 的 $m$ 次多项式.

因为矩阵 $\boldsymbol{A}^{k}, \boldsymbol{A}^{l}$ 和 $\boldsymbol{E}$ 都是可交换的, 所以矩阵 $\boldsymbol{A}$ 的两个多项式 $\varphi(\boldsymbol{A})$ 和 $f(\boldsymbol{A})$ 总是可交换的, 即总有

$$
\varphi(\boldsymbol{A}) f(\boldsymbol{A})=f(\boldsymbol{A}) \varphi(\boldsymbol{A}),
$$

从而 $\boldsymbol{A}$ 的几个多项式可以像数 $x$ 的多项式一样相乘或分解因式.例如

$$
\begin{gathered}
(\boldsymbol{E}+\boldsymbol{A})(2 \boldsymbol{E}-\boldsymbol{A})=2 \boldsymbol{E}+\boldsymbol{A}-\boldsymbol{A}^{2}, \\
(\boldsymbol{E}-\boldsymbol{A})^{3}=\boldsymbol{E}-3 \boldsymbol{A}+3 \boldsymbol{A}^{2}-\boldsymbol{A}^{3} .
\end{gathered}
$$

我们常用例 13 中计算 $\boldsymbol{A}^{k}$ 的方法来计算 $\boldsymbol{A}$ 的多项式 $\varphi(\boldsymbol{A})$, 这就是:

(i) 如果 $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{\Lambda} \boldsymbol{P}^{-1}$, 则 $\boldsymbol{A}^{k}=\boldsymbol{P} \boldsymbol{\Lambda}^{k} \boldsymbol{P}^{-1}$, 从而

$$
\begin{aligned}
\varphi(\boldsymbol{A}) & =a_{0} \boldsymbol{E}+a_{1} \boldsymbol{A}+\cdots+a_{m} \boldsymbol{A}^{m} \\
& =\boldsymbol{P} a_{0} \boldsymbol{E} \boldsymbol{P}^{-1}+\boldsymbol{P} a_{1} \boldsymbol{\Lambda} \boldsymbol{P}^{-1}+\cdots+\boldsymbol{P} a_{m} \boldsymbol{\Lambda}^{m} \boldsymbol{P}^{-1} \\
& =\boldsymbol{P} \varphi(\boldsymbol{\Lambda}) \boldsymbol{P}^{-1} .
\end{aligned}
$$

(ii) 如果 $\boldsymbol{\Lambda}=\operatorname{diag}\left(\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}\right)$ 为对角阵, 则 $\boldsymbol{\Lambda}^{k}=\operatorname{diag}\left(\lambda_{1}^{k}, \lambda_{2}^{k}, \cdots, \lambda_{n}^{k}\right)$, 从

而

$$
\begin{aligned}
& \varphi(\boldsymbol{\Lambda})=a_{0} \boldsymbol{E}+a_{1} \boldsymbol{\Lambda}+\cdots+a_{m} \boldsymbol{\Lambda}^{m} \\
& =a_{0}\left(\begin{array}{llll}
1 & & & \\
& 1 & & \\
& & \ddots & \\
& & & 1
\end{array}\right)+a_{1}\left(\begin{array}{llll}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{n}
\end{array}\right)+\cdots+a_{m}\left(\begin{array}{llll}
\lambda_{1}^{m} & & & \\
& \lambda_{2}^{m} & & \\
& & \ddots & \\
& & & \lambda_{n}^{m}
\end{array}\right) \\
& =\left(\begin{array}{llll}
\varphi\left(\lambda_{1}\right) & & & \\
& \varphi\left(\lambda_{2}\right) & & \\
& & \ddots & \\
& & & \varphi\left(\lambda_{n}\right)
\end{array}\right) .
\end{aligned}
$$

例 14 设 $\boldsymbol{P}=\left(\begin{array}{rrr}-1 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 1 & -1\end{array}\right), \boldsymbol{\Lambda}=\left(\begin{array}{lll}1 & \\ & 2 & \\ & & -3\end{array}\right), \boldsymbol{A P}=\boldsymbol{P} \boldsymbol{\Lambda}$,

求 $\varphi(A)=A^{3}+2 A^{2}-3 A$.

解 $|\boldsymbol{P}|=\left|\begin{array}{rrr}-1 & 1 & 1 \\ 1 & 0 & 2 \\ 1 & 1 & -1\end{array}\right| \stackrel{r_{1}+r_{3}}{=}\left|\begin{array}{rrr}0 & 2 & 0 \\ 1 & 0 & 2 \\ 1 & 1 & -1\end{array}\right|=6$, 知 $\boldsymbol{P}$ 可逆,从而

$$
\boldsymbol{A}=\boldsymbol{P} \boldsymbol{\Lambda} \boldsymbol{P}^{-1}, \varphi(\boldsymbol{A})=\boldsymbol{P} \varphi(\boldsymbol{\Lambda}) \boldsymbol{P}^{-1} \text {. }
$$

而 $\varphi(1)=0, \varphi(2)=10, \varphi(-3)=0$, 故 $\varphi(\Lambda)=\operatorname{diag}(0,10,0)$.

$$
\begin{aligned}
\varphi(\boldsymbol{A}) & =\boldsymbol{P} \varphi(\boldsymbol{\Lambda}) \boldsymbol{P}^{-1}=\left(\begin{array}{rrr}
-1 & 1 & 1 \\
1 & 0 & 2 \\
1 & 1 & -1
\end{array}\right)\left(\begin{array}{ll}
0 & \\
& 10 \\
&
\end{array}\right) \frac{1}{|\vec{P}|} \boldsymbol{P}^{*} \\
& =\frac{10}{6}\left(\begin{array}{lll}
0 & 1 & 0 \\
0 & 0 & 0 \\
0 & 1 & 0
\end{array}\right)\left(\begin{array}{lll}
A_{11} & A_{21} & A_{31} \\
A_{12} & A_{22} & A_{32} \\
A_{13} & A_{23} & A_{33}
\end{array}\right)=\frac{5}{3}\left(\begin{array}{ccc}
A_{12} & A_{22} & A_{32} \\
0 & 0 & 0 \\
A_{12} & A_{22} & A_{32}
\end{array}\right),
\end{aligned}
$$

而 $A_{12}=-\left|\begin{array}{rr}1 & 2 \\ 1 & -1\end{array}\right|=3, A_{22}=\left|\begin{array}{rr}-1 & 1 \\ 1 & -1\end{array}\right|=0, A_{32}=-\left|\begin{array}{rr}-1 & 1 \\ 1 & 2\end{array}\right|=3$,

于是

$$
\varphi(A)=5\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 0 & 0 \\
1 & 0 & 1
\end{array}\right)
$$

## $\S 4$ 矩阵分块法

对于行数和列数较高的矩阵 $\boldsymbol{A}$, 运算时常采用分块法, 使大矩阵的运算化 成小矩阵的运算.我们将矩阵 $\boldsymbol{A}$ 用若干条纵线和横线分成许多个小矩阵, 每一 个小矩阵称为 $\boldsymbol{A}$ 的子块, 以子块为元素的形式上的矩阵称为分块矩阵.

例如将 $3 \times 4$ 矩阵

$$
\boldsymbol{A}=\left(\begin{array}{llll}
a_{11} & a_{12} & a_{13} & a_{14} \\
a_{21} & a_{22} & a_{23} & a_{24} \\
a_{31} & a_{32} & a_{33} & a_{34}
\end{array}\right)
$$

分成子块的分法很多,下面举出三种分块形式:

(i) $\left(\begin{array}{ll:ll}a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ \hdashline a_{31} & a_{32} & a_{33} & a_{34}\end{array}\right)$,(ii) $\left(\begin{array}{c:cc:c}a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ \hdashline a_{31} & a_{32} & a_{33} & a_{34}\end{array}\right)$,

(iii) $\left(\begin{array}{l:l:l:l}a_{11} & a_{12} & a_{13} & a_{14} \\ a_{21} & a_{22} & a_{23} & a_{24} \\ a_{31} & a_{32} & a_{33} & a_{34}\end{array}\right)$.

分法 (i) 可记为

$$
\boldsymbol{A}=\left(\begin{array}{ll}
\boldsymbol{A}_{11} & \boldsymbol{A}_{12} \\
\boldsymbol{A}_{21} & \boldsymbol{A}_{22}
\end{array}\right),
$$

其中

$$
\begin{aligned}
& \boldsymbol{A}_{11}=\left(\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right), \boldsymbol{A}_{12}=\left(\begin{array}{ll}
a_{13} & a_{14} \\
a_{23} & a_{24}
\end{array}\right), \\
& \boldsymbol{A}_{21}=\left(\begin{array}{ll}
a_{31} & a_{32}
\end{array}\right), \boldsymbol{A}_{22}=\left(\begin{array}{ll}
a_{33} & a_{34}
\end{array}\right),
\end{aligned}
$$

www.TopSage.com 即 $\boldsymbol{A}_{11}, \boldsymbol{A}_{12}, \boldsymbol{A}_{21}, \boldsymbol{A}_{22}$ 为 $\boldsymbol{A}$ 的子块, 而 $\boldsymbol{A}$ 形式上成为以这些子块为元素的分块 矩阵. 分法 (ii) 及 (iii) 的分块矩阵请读者写出.

本章第 2 节证明公式 $|\boldsymbol{A B}|=|\boldsymbol{A}||\boldsymbol{B}|$ 时出现的矩阵 $\left(\begin{array}{rr}\boldsymbol{A} & \boldsymbol{O} \\ -\boldsymbol{E} & \boldsymbol{B}\end{array}\right)$ 及 $\left(\begin{array}{rl}\boldsymbol{A} & \boldsymbol{A B} \\ -\boldsymbol{E} & \boldsymbol{O}\end{array}\right)$ 正是分块矩阵, 在那里是把四个矩阵拼成一个大矩阵, 这与把大矩 阵分成多个小矩阵是同一个概念的两个方面.

分块矩阵的运算规则与普通矩阵的运算规则相类似，分别说明如下:

(i) 设矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 的行数相同、列数相同, 采用相同的分块法, 有

$$
\boldsymbol{A}=\left(\begin{array}{ccc}
\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 r} \\
\vdots & & \vdots \\
\boldsymbol{A}_{s 1} & \cdots & \boldsymbol{A}_{s r}
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{ccc}
\boldsymbol{B}_{11} & \cdots & \boldsymbol{B}_{1 r} \\
\vdots & & \vdots \\
\boldsymbol{B}_{s 1} & \cdots & \boldsymbol{B}_{s r}
\end{array}\right),
$$

其中 $\boldsymbol{A}_{i j}$ 与 $\boldsymbol{B}_{i j}$ 的行数相同、列数相同, 那么

$$
A+B=\left(\begin{array}{ccc}
A_{11}+B_{11} & \cdots & A_{1 r}+B_{1 r} \\
\vdots & & \vdots \\
A_{s 1}+B_{s 1} & \cdots & A_{s r}+B_{s r}
\end{array}\right) .
$$

(ii) 设 $\boldsymbol{A}=\left(\begin{array}{ccc}\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 r} \\ \vdots & & \vdots \\ \boldsymbol{A}_{s 1} & \cdots & \boldsymbol{A}_{s r}\end{array}\right), \lambda$ 为数, 那么

$$
\lambda A=\left(\begin{array}{lll}
\lambda A_{11} & \cdots & \lambda A_{1 r} \\
\vdots & & \vdots \\
\lambda A_{s 1} & \cdots & \lambda A_{s r}
\end{array}\right) .
$$

(iii) 设 $\boldsymbol{A}$ 为 $m \times l$ 矩阵, $\boldsymbol{B}$ 为 $l \times n$ 矩阵,分块成

$$
\boldsymbol{A}=\left(\begin{array}{ccc}
\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 r} \\
\vdots & & \vdots \\
\boldsymbol{A}_{s 1} & \cdots & \boldsymbol{A}_{s t}
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{llr}
\boldsymbol{B}_{11} & \cdots & \boldsymbol{B}_{1 r} \\
\vdots & & \vdots \\
\boldsymbol{B}_{11} & \cdots & \boldsymbol{B}_{t r}
\end{array}\right),
$$

其中 $A_{i 1}, A_{i 2}, \cdots, A_{i r}$ 的列数分别等于 $B_{1 j}, B_{2 j}, \cdots, B_{i j}$ 的行数, 那么

$$
\boldsymbol{A B}=\left(\begin{array}{ccc}
C_{11} & \cdots & C_{1 r} \\
\vdots & & \vdots \\
C_{s 1} & \cdots & C_{s r}
\end{array}\right),
$$

其中

$$
\boldsymbol{C}_{i j}=\sum_{k=1}^{1} \boldsymbol{A}_{i k} \boldsymbol{B}_{k j}(i=1, \cdots, s ; j=1, \cdots, r) \text {. }
$$

例 15 设 求 $A B$.

$$
\boldsymbol{A}=\left(\begin{array}{rrrr}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
-1 & 2 & 1 & 0 \\
1 & 1 & 0 & 1
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{rrrr}
1 & 0 & 1 & 0 \\
-1 & 2 & 0 & 1 \\
1 & 0 & 4 & 1 \\
-1 & -1 & 2 & 0
\end{array}\right)
$$

解 把 $\boldsymbol{A}, \boldsymbol{B}$ 分块成

$$
\begin{aligned}
& \boldsymbol{A}=\left(\begin{array}{rr:rr}
1 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 \\
\hdashline-1 & 2 & 1 & 0 \\
1 & 1 & 0 & 1
\end{array}\right)=\left(\begin{array}{cc}
\boldsymbol{E} & \boldsymbol{O} \\
\boldsymbol{A}_{1} & \boldsymbol{E}
\end{array}\right) \\
& \boldsymbol{B}=\left(\begin{array}{rr:rr}
1 & 0 & 1 & 0 \\
-1 & 2 & 0 & 1 \\
\hdashline 1 & 0 & 4 & 1 \\
-1 & -1 & 2 & 0
\end{array}\right)=\left(\begin{array}{ll}
\boldsymbol{B}_{11} & \boldsymbol{E} \\
\boldsymbol{B}_{21} & \boldsymbol{B}_{22}
\end{array}\right),
\end{aligned}
$$

则 $\boldsymbol{A B}=\left(\begin{array}{cc}\boldsymbol{E} & \boldsymbol{O} \\ \boldsymbol{A}_{1} & \dot{E}\end{array}\right)\left(\begin{array}{ll}\boldsymbol{B}_{11} & \boldsymbol{E} \\ \boldsymbol{B}_{21} & \boldsymbol{B}_{22}\end{array}\right)$

$$
=\left(\begin{array}{cc}
\boldsymbol{B}_{11} & \boldsymbol{E} \\
\boldsymbol{A}_{1} \boldsymbol{B}_{11}+\boldsymbol{B}_{21} & \boldsymbol{A}_{1}+\boldsymbol{B}_{22}
\end{array}\right) \text {, }
$$

而

$$
\begin{aligned}
\boldsymbol{A}_{1} \boldsymbol{B}_{11}+\boldsymbol{B}_{21} & =\left(\begin{array}{rr}
-1 & 2 \\
1 & 1
\end{array}\right)\left(\begin{array}{rr}
1 & 0 \\
-1 & 2
\end{array}\right)+\left(\begin{array}{rr}
1 & 0 \\
-1 & -1
\end{array}\right) \\
& =\left(\begin{array}{rr}
-3 & 4 \\
0 & 2
\end{array}\right)+\left(\begin{array}{rr}
1 & 0 \\
-1 & -1
\end{array}\right)=\left(\begin{array}{ll}
-2 & 4 \\
-1 & 1
\end{array}\right), \\
\boldsymbol{A}_{1}+\boldsymbol{B}_{22} & =\left(\begin{array}{rr}
-1 & 2 \\
1 & 1
\end{array}\right)+\left(\begin{array}{ll}
4 & 1 \\
2 & 0
\end{array}\right)=\left(\begin{array}{ll}
3 & 3 \\
3 & 1
\end{array}\right),
\end{aligned}
$$

于是

$$
\boldsymbol{A B}=\left(\begin{array}{rr:rr}
1 & 0 & 1 & 0 \\
-1 & 2 & 0 & 1 \\
\hdashline-2 & 4 & 3 & 3 \\
-1 & 1 & 3 & 1
\end{array}\right)
$$

(iv) 设 $\boldsymbol{A}=\left(\begin{array}{lll}\boldsymbol{A}_{11} & \cdots & \boldsymbol{A}_{1 r} \\ \vdots & & \vdots \\ \boldsymbol{A}_{s 1} & \cdots & \boldsymbol{A}_{s r}\end{array}\right)$, 则 $\boldsymbol{A}^{\mathrm{T}}=\left(\begin{array}{lll}\boldsymbol{A}_{11}^{\mathrm{T}} & \cdots & \boldsymbol{A}_{s 1}^{\mathrm{T}} \\ \vdots & & \vdots \\ \boldsymbol{A}_{1 r}^{\mathrm{T}} & \cdots & \boldsymbol{A}_{s r}^{\mathrm{T}}\end{array}\right)$.

(v) 设 $\boldsymbol{A}$ 为 $n$ 阶矩阵,若 $\boldsymbol{A}$ 的分块矩阵只有在对角线上有非零子块, 其余 子块都为零矩阵, 且在对角线上的子块都是方阵, 即

$$
\boldsymbol{A}=\left(\begin{array}{rrrr}
\boldsymbol{A}_{1} & & & \boldsymbol{O} \\
& \boldsymbol{A}_{2} & \\
& \ddots & \\
& & & \boldsymbol{A}_{s}
\end{array}\right),
$$

其中 $\boldsymbol{A}_{i}(i=1,2, \cdots, s)$ 都是方阵,那么称 $\boldsymbol{A}$ 为分圤对角䓡阵.

分块对角矩阵的行列式具有下述性质

$$
|\boldsymbol{A}|=\left|\boldsymbol{A}_{1}\right|\left|\boldsymbol{A}_{2}\right| \cdots\left|\boldsymbol{A}_{s}\right| \text {. }
$$

由此性质可知, 若 $\left|\boldsymbol{A}_{i}\right| \neq 0(i=1,2, \cdots, s)$, 则 $|\boldsymbol{A}| \neq 0$, 并有

$$
\boldsymbol{A}^{-1}=\left(\begin{array}{ccc}
\boldsymbol{A}_{1}^{-1} & & \boldsymbol{O} \\
& \boldsymbol{A}_{2}^{-1} & \\
& \ddots & \\
& & \boldsymbol{A}_{s}^{-1}
\end{array}\right) .
$$

例 16 设 $\boldsymbol{A}=\left(\begin{array}{lll}5 & 0 & 0 \\ 0 & 3 & 1 \\ 0 & 2 & 1\end{array}\right)$, 求 $\boldsymbol{A}^{-1}$.

解

$$
\begin{aligned}
& \boldsymbol{A}=\left(\begin{array}{l:cc}
5 & 0 & 0 \\
\hdashline & 3 & 1 \\
0 & 2 & 1
\end{array}\right)=\left(\begin{array}{cc}
A_{1} & \boldsymbol{O} \\
\boldsymbol{O} & \boldsymbol{A}_{2}
\end{array}\right), \\
& \boldsymbol{A}_{1}=(5), \boldsymbol{A}_{1}^{-1}=\left(\frac{1}{5}\right), \\
& \boldsymbol{A}_{2}=\left(\begin{array}{ll}
3 & 1 \\
2 & 1
\end{array}\right), \boldsymbol{A}_{2}^{-1}=\left(\begin{array}{rr}
1 & -1 \\
-2 & 3
\end{array}\right), \\
& \boldsymbol{A}^{-1}=\left(\begin{array}{r:rr}
\frac{1}{5} & 0 & 0 \\
\hdashline 0 & 1 & -1 \\
0 & -2 & 3
\end{array}\right) .
\end{aligned}
$$

对矩阵分块时,有两种分块法应予特别重视, 这就是按行分块和按列分块. $m \times n$ 矩阵 $\boldsymbol{A}$ 有 $m$ 行, 称为矩阵 $\boldsymbol{A}$ 的 $m$ 个行向量. 若第 $i$ 行记作

则矩阵 $\boldsymbol{A}$ 便记为

$$
\boldsymbol{A}=\left(\begin{array}{c}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}}
\end{array}\right),
$$

$m \times n$ 矩阵 $\boldsymbol{A}$ 有 $n$ 列,称为矩阵 $\boldsymbol{A}$ 的 $n$ 个列向量,若第 $j$ 列记作

㱟表示, 如 $a^{\mathrm{T}}, \alpha^{\mathrm{T}}, x^{\mathrm{T}}$ 等.

$$
a_{j}=\left(\begin{array}{c}
a_{1 j} \\
a_{2 j} \\
\vdots \\
a_{m j}
\end{array}\right)
$$

则

$$
\boldsymbol{A}=\left(a_{1}, a_{2}, \cdots, a_{n}\right) .
$$

对于矩阵 $\boldsymbol{A}=\left(a_{i j}\right)_{m \times s}$ 与矩阵 $\boldsymbol{B}=\left(b_{i j}\right)_{s \times n}$ 的乘积矩阵 $\boldsymbol{A B}=\boldsymbol{C}=\left(c_{i j}\right)_{m \times n}$, 若把 $\boldsymbol{A}$ 按行分成 $m$ 块,把 $\boldsymbol{B}$ 按列分成 $n$ 块,便有

$$
\boldsymbol{A B}=\left(\begin{array}{c}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}}
\end{array}\right)\left(\boldsymbol{b}_{1}, b_{2}, \cdots, \boldsymbol{b}_{n}\right)=\left(\begin{array}{cccc}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} b_{1} & \boldsymbol{\alpha}_{1}^{\mathrm{T}} \boldsymbol{b}_{2} & \cdots & \boldsymbol{\alpha}_{1}^{\mathrm{T}} \boldsymbol{b}_{n} \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} \boldsymbol{b}_{1} & \boldsymbol{\alpha}_{2}^{\mathrm{T}} \boldsymbol{b}_{2} & \cdots & \boldsymbol{\alpha}_{2}^{\mathrm{T}} \boldsymbol{b}_{n} \\
\vdots & \vdots & & \vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}} \boldsymbol{b}_{1} & \boldsymbol{\alpha}_{m}^{\mathrm{T}} \boldsymbol{b}_{2} & \cdots & \boldsymbol{\alpha}_{m}^{\mathrm{T}} \boldsymbol{b}_{n}
\end{array}\right)=\left(c_{i j}\right)_{m \times n},
$$

其中

$$
c_{i j}=\boldsymbol{\alpha}_{i}^{\top} \boldsymbol{b}_{j}=\left(a_{i 1}, a_{i 2}, \cdots, a_{i s}\right)\left(\begin{array}{c}
b_{1 j} \\
b_{2 j} \\
\vdots \\
b_{s j}
\end{array}\right)=\sum_{k=1}^{s} a_{i k} b_{k j},
$$

由此可进一步领会矩阵相乘的定义.

以对角阵 $\Lambda_{m}$ 左乘矩阵 $\boldsymbol{A}_{m \times n}$ 时，把 $\boldsymbol{A}$ 按行分块,有

$$
\boldsymbol{A}_{m} \boldsymbol{A}_{m \times n}=\left(\begin{array}{cccc}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{m}
\end{array}\right)\left(\begin{array}{c}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}}
\end{array}\right)=\left(\begin{array}{c}
\lambda_{1} \boldsymbol{\alpha}_{1}^{\mathrm{T}} \\
\lambda_{2} \boldsymbol{\alpha}_{2}^{\mathrm{T}} \\
\vdots \\
\lambda_{m} \boldsymbol{\alpha}_{m}^{\mathrm{T}}
\end{array}\right),
$$

可见以对角阵 $\Lambda_{m}$ 左乘 $A$ 的结果是 $A$ 的每一行乘以 $\Lambda$ 中与该行对应的对角元.

以对角阵 $\boldsymbol{\Lambda}_{n}$ 右乘矩阵 $\boldsymbol{A}_{m \times n}$ 时, 把 $\boldsymbol{A}$ 按列分块, 有

$$
\boldsymbol{A} \mathbf{\Lambda}_{n}=\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\begin{array}{llll}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & \lambda_{n}
\end{array}\right)=\left(\lambda_{1} a_{1}, \lambda_{2} a_{2}, \cdots, \lambda_{n} a_{n}\right),
$$

可见以对角阵 $\Lambda$ 右乘 $A$ 的结果是 $A$ 的每一列乘以 $\Lambda$ 中与该列对应的对角元.

例 17 证明矩阵 $A=O$ 的充分必要条件是方阵 $A^{\mathrm{T}} A=O$.

证 条件的必要性是显然的,下面证明条件的充分性.

设 $\boldsymbol{A}=\left(a_{i j}\right)_{m \times n}$, 把 $\boldsymbol{A}$ 用列向墨表示为 $\boldsymbol{A}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{n}\right)$,则

$$
\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}=\left(\begin{array}{c}
\boldsymbol{a}_{1}^{\mathrm{T}} \\
\boldsymbol{a}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{a}_{n}^{\mathrm{T}}
\end{array}\right)\left(a_{1}, a_{2}, \cdots, a_{n}\right)=\left(\begin{array}{cccc}
\boldsymbol{a}_{1}^{\mathrm{T}} \boldsymbol{a}_{1} & \boldsymbol{a}_{1}^{\mathrm{T}} \boldsymbol{a}_{2} & \cdots & \boldsymbol{a}_{1}^{\mathrm{T}} \bar{a}_{n} \\
\boldsymbol{a}_{2}^{\mathrm{T}} \boldsymbol{a}_{1} & \boldsymbol{a}_{2}^{\mathrm{T}} \boldsymbol{a}_{2} & \cdots & \boldsymbol{a}_{2}^{\mathrm{T}} \boldsymbol{a}_{n} \\
\vdots & \vdots & 0 & \vdots \\
\boldsymbol{a}_{n}^{\mathrm{T}} \boldsymbol{a}_{1} & \boldsymbol{a}_{n}^{\mathrm{T}} \boldsymbol{a}_{2} & \cdots & \boldsymbol{a}_{n}^{\mathrm{T}} \boldsymbol{a}_{n}
\end{array}\right),
$$

即 $\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}$ 的 $(i, j)$ 元为 $\boldsymbol{a}_{i}^{\mathrm{T}} \boldsymbol{a}_{j}$, 因 $\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}=\boldsymbol{O}$, 故

$$
\boldsymbol{a}_{i}^{\mathrm{T}} \boldsymbol{a}_{j}=0(i, j=1,2, \cdots, n),
$$

特殊地, 有

$$
\boldsymbol{a}_{j}^{\mathrm{T}} \boldsymbol{a}_{j}=0(j=1,2, \cdots, n),
$$

而

$$
\boldsymbol{a}_{j}^{\mathrm{T}} \boldsymbol{a}_{j}=\left(a_{1 j}, a_{2 j}, \cdots, a_{m j}\right)\left(\begin{array}{c}
a_{1 j} \\
a_{2 j} \\
\vdots \\
a_{m j}
\end{array}\right)=a_{1 j}^{2}+a_{2 j}^{2}+\cdots+a_{m j}^{2},
$$

由 $a_{1 j}^{2}+a_{2 j}^{2}+\cdots+a_{m j}^{2}=0$, (因 $a_{i j}$ 为实数) 得

$$
a_{1 j}=a_{2 j}=\cdots=a_{m j}=0,(j=1,2, \cdots, n),
$$

即

$$
\boldsymbol{A}=\boldsymbol{O} \text {. }
$$

本例阐明了矩阵 $\boldsymbol{A}$ 与方阵 $\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}$ 之间的一种关系. 特别地, 当 $\boldsymbol{A}=\boldsymbol{a}$ 为列向 量时, 由于 $a^{\mathrm{T}} a$ 为 $1 \times 1$ 矩阵, 即 $a^{\mathrm{T}} a$ 是一个数,这时, 本例的结论可叙述为: 列向 量 $a=0$ 的充分必要条件是 $a^{\mathrm{T}} a=0$.

对于线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=b_{2}, \\
\cdots \cdots \cdots \cdots \\
a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n}=b_{m},
\end{array}\right.
$$

记 $\boldsymbol{A}=\left(a_{i j}\right), \boldsymbol{x}=\left(\begin{array}{c}x_{1} \\ x_{2} \\ \vdots \\ x_{n}\end{array}\right), \boldsymbol{b}=\left(\begin{array}{c}b_{1} \\ b_{2} \\ \vdots \\ b_{m}\end{array}\right), \boldsymbol{B}=\left(\begin{array}{ccccc}a_{11} & a_{12} & \cdots & a_{1 n} & b_{1} \\ a_{21} & a_{22} & \cdots & a_{2 n} & b_{2} \\ \vdots & \vdots & & \vdots & \vdots \\ a_{m 1} & a_{m 2} & \cdots & a_{m n} & b_{m}\end{array}\right)$,

其中 $\boldsymbol{A}$ 称为系数矩阵, $\boldsymbol{x}$ 称为末知数向量, $\boldsymbol{b}$ 称为常数项向量, $\boldsymbol{B}$ 称为增广矩阵. 按分块矩阵的记法,可记

$$
\boldsymbol{B}=(\boldsymbol{A} \vdots \boldsymbol{b}) \text {, 或 } \boldsymbol{B}=(\boldsymbol{A}, \boldsymbol{b})=\left(a_{1}, a_{2}, \cdots, a_{n}, \boldsymbol{b}\right) \text {. }
$$

利用矩阵的乘法, 此方程组可记作

$$
\boldsymbol{A x}=\boldsymbol{b},
$$

方程 (12) 以向量 $\boldsymbol{x}$ 为未知元, 它的解称为方程组 (11) 的㙰向量. 如果把系数矩阵 $\boldsymbol{A}$ 按行分成 $m$ 块, 则线性方程组 $\boldsymbol{A x}=\boldsymbol{b}$ 可记作

$$
\left(\begin{array}{c}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}}
\end{array}\right) x=\left(\begin{array}{c}
b_{1} \\
b_{2} \\
\vdots \\
b_{m}
\end{array}\right) \text {, 或 }\left\{\begin{array}{c}
\boldsymbol{\alpha}_{1}^{\mathrm{T}} x=b_{1}, \\
\boldsymbol{\alpha}_{2}^{\mathrm{T}} x=b_{2}, \\
\vdots \\
\boldsymbol{\alpha}_{m}^{\mathrm{T}} x=b_{m},
\end{array},\right.
$$

这就相当于把每个方程

$$
a_{i 1} x_{1}+a_{i 2} x_{2}+\cdots+a_{i n} x_{n}=b_{i}
$$

记作

$$
\boldsymbol{\alpha}_{i}^{\mathrm{T}} \boldsymbol{x}=b_{i}(i=1,2, \cdots, m) \text {. }
$$

如果把系数矩阵 $\boldsymbol{A}$ 按列分成 $\boldsymbol{n}$ 块,则与 $\boldsymbol{A}$ 相乘的 $\boldsymbol{x}$ 应对应地按行分成 $\boldsymbol{n}$ 块, 从而记作

即

$$
\left(a_{1}, a_{2}, \cdots, a_{n}\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)=\boldsymbol{b},
$$

$$
x_{1} a_{1}+x_{2} a_{2}+\cdots+x_{n} a_{n}=b .
$$

(12), (13), (14) 是线性方程组 (11) 的各种变形.今后,它们与(11) 将混同使 用而不加区分,并都称为线性方程组或线性方程. 解与解向量亦不加区别.

下面证明在第一章中介绍的克拉默法则 .

克拉默法则 对于 $n$ 个变量、 $n$ 个方程的线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=b_{2}, \\
\cdots \cdots \cdots \cdots \\
a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n}=b_{n},
\end{array}\right.
$$

如果它的系数行列式 $D \neq 0$, 则它有惟一解

$$
x_{j}=\frac{1}{D} D_{j}=\frac{1}{D}\left(b_{1} A_{1 j}+b_{2} A_{2 j}+\cdots+b_{n} A_{n j}\right)(j=1,2, \cdots, n) .
$$

证 把方程组 (15)写成矩阵方程

$$
A x=b,
$$

这里 $\boldsymbol{A}=\left(a_{i j}\right)_{n \times n}$ 为 $n$ 阶矩阵, 因 $|\boldsymbol{A}|=D \neq 0$, 故 $\boldsymbol{A}^{-1}$ 存在.

令 $\boldsymbol{x}=\boldsymbol{A}^{-1} \boldsymbol{b}$, 有

$$
\boldsymbol{A x}=\boldsymbol{A A ^ { - 1 } b = b ,}
$$

表明 $\boldsymbol{x}=\boldsymbol{A}^{-1} \boldsymbol{b}$ 是方程组 (15) 的解向量.

由 $\boldsymbol{A x}=\boldsymbol{b}$, 有 $\boldsymbol{A}^{-1} \boldsymbol{A x}=\boldsymbol{A}^{-1} \boldsymbol{b}$, 即 $\boldsymbol{x}=\boldsymbol{A}^{-1} \boldsymbol{b}$, 根据逆阵的惟一性, 知 $\boldsymbol{x}=$ $A^{-1} b$ 是方程组 (15) 的惟一的解向量. 由逆阵公式 $A^{-1}=\frac{1}{|A|} A^{*}$, 有 $x=A^{-1} b=\frac{1}{D} A^{*} b$, 即

$$
\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)=\frac{1}{D}\left(\begin{array}{cccc}
A_{11} & A_{21} & \cdots & A_{n 1} \\
A_{12} & A_{22} & \cdots & A_{n 2} \\
\vdots & \vdots & & \vdots \\
A_{1 n} & A_{2 n} & \cdots & A_{n n}
\end{array}\right)\left(\begin{array}{c}
b_{1} \\
b_{2} \\
\vdots \\
b_{n}
\end{array}\right)=\frac{1}{D}\left(\begin{array}{c}
b_{1} A_{11}+b_{2} A_{21}+\cdots+b_{n} A_{n 1} \\
b_{1} A_{12}+b_{2} A_{22}+\cdots+b_{n} A_{n 2} \\
\cdots \cdots \cdots \cdots \\
b_{1} A_{1 n}+b_{2} A_{2 n}+\cdots+b_{n} A_{n n}
\end{array}\right) \text {, }
$$

亦即 $x_{j}=\frac{1}{D}\left(b_{1} A_{1 j}+b_{2} A_{2 j}+\cdots+b_{n} A_{n j}\right)=\frac{1}{D} D_{j} \quad(j=1,2, \cdots, n)$.


## 第三章 <br> 矩阵的初等变换与线性方程组

本章先引进矩阵的初等变换, 建立矩阵的秩的概念,并利用初等变换讨论矩 阵的秩的性质; 然后利用矩阵的秩讨论线性方程组无解、有惟一解或有无穷多解 的充分必要条件,并介绍用初等变换解线性方程组的方法.

## $\S 1$ 矩阵的初等变换

矩阵的初等变换是矩阵的一种十分重要的运算, 它在解线性方程组、求逆阵 及矩阵理论的探讨中都可起重要的作用. 为引进矩阵的初等变换, 先来分析用消 元法解线性方程组的例子.

引例 求解线性方程组

$$
\left\{\begin{array}{r}
2 x_{1}-x_{2}-x_{3}+x_{4}=2,(1) \\
x_{1}+x_{2}-2 x_{3}+x_{4}=4,(2) \\
4 x_{1}-6 x_{2}+2 x_{3}-2 x_{4}=4,(3) \\
3 x_{1}+6 x_{2}-9 x_{3}+7 x_{4}=9 \text {. (4) }
\end{array}\right.
$$

解

$$
\begin{aligned}
& \text { (1) } \underset{(1) \rightarrow(3) \div 2}{\longrightarrow}\left\{\begin{array}{l}
x_{1}+x_{2}-2 x_{3}+x_{4}=4,(1) \\
2 x_{1}-x_{2}-x_{3}+x_{4}=2 \text {, (2) } \\
2 x_{1}-3 x_{2}+x_{3}-x_{4}=2, \text { (3) } \\
3 x_{1}+6 x_{2}-9 x_{3}+7 x_{4}=9 \text {, (4) }
\end{array}\right. \\
& \underset{(\text { (3) }-2 \text { (1) }-3(1)}{\longrightarrow}\left\{\begin{aligned}
& x_{1}+x_{2}-2 x_{3}+x_{4}= 4, \text { (1) } \\
& 2 x_{2}-2 x_{3}+2 x_{4}= 0, \text { (2) } \\
&-5 x_{2}+5 x_{3}-3 x_{4}=-6, \text { (3) } \\
& 3 x_{2}-3 x_{3}+4 x_{4}=-3,(4)
\end{aligned}\right.
\end{aligned}
$$

$$
\underset{(3) \leftrightarrow(4)}{(4)-2(3)}\left\{\begin{aligned}
x_{1}+x_{2}-2 x_{3}+x_{4} & =4, \\
x_{2}-x_{3}+x_{4} & =0 \\
x_{4} & =-3, \\
0 & =0 .
\end{aligned}\right.
$$

这里, (1) $\rightarrow\left(B_{1}\right)$ 是为消 $x_{1}$ 作准备. $\left(B_{1}\right) \rightarrow\left(B_{2}\right)$ 是保留(1)中的 $x_{1}$, 消去(2), (3),(4)中的 $x_{1} .\left(B_{2}\right) \rightarrow\left(B_{3}\right)$ 是保留(2)中的 $x_{2}$ 并把它的系数变为 1 , 然后消去(3), (4)中的 $x_{2}$, 在此同时恰好把 $x_{3}$ 也消去了. $\left(B_{3}\right) \rightarrow\left(B_{4}\right)$ 是消去 $x_{4}$, 在此同时佮 好把常数也消去了, 得到恒等式 $0=0$ (如果常数项不能消去, 就将得到矛盾方程 $0=1$, 则说明方程组无解). 至此消元完毕.

$\left(B_{4}\right)$ 是 4 个未知数 3 个有效方程的方程组,应有一个自由末知数, 由于方 程组 $\left(B_{4}\right)$ 呈阶梯形, 可把每个台阶的第一个未知数 (即 $x_{1}, x_{2}, x_{4}$ ) 选为非自由 未知数,剩下的 $x_{3}$ 选为自由未知数. 这样, 就只需用 “回代” 的方法便能求出解: 由(3)得 $x_{4}=-3$; 将 $x_{4}=-3$ 代人(2), 得 $x_{2}=x_{3}+3$; 以 $x_{4}=-3, x_{2}=x_{3}+3$ 代 人(1), 得 $x_{1}=x_{3}+4$. 于是解得

$$
\left\{\begin{array}{l}
x_{1}=x_{3}+4, \\
x_{2}=x_{3}+3, \\
x_{4}=-3,
\end{array}\right.
$$

其中 $x_{3}$ 可任意取值.或令 $x_{3}=c$,方程组的解可记作

$$
x=\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=\left(\begin{array}{c}
c+4 \\
c+3 \\
c \\
-3
\end{array}\right) \text {, 即 } x=c\left(\begin{array}{l}
1 \\
1 \\
1 \\
0
\end{array}\right)+\left(\begin{array}{r}
4 \\
3 \\
0 \\
-3
\end{array}\right) \text {, }
$$

其中 $c$ 为任意常数.

在上述消元过程中,始终把方程组看作一个整体,即不是着眼于某一个方程 的变形, 而是着眼于整个方程组变成另一个方程组. 其中用到三种变换, 即: (i) 交换方程次序 (i门与(1)相互替换); (ii) 以不等于 0 的数乘某个方程 (以（i) $\times k$ 替 换(i)）; (iii)一个方程加上另一个方程的 $k$ 倍 (以(i) $+k$ (1) 替换(i) ). 由于这三种 变换都是可逆的,即

$$
\begin{aligned}
& \text { 若 }(A) \stackrel{(1) \leftrightarrow(0)}{\longrightarrow}(B), \quad \text { 则 }(B) \stackrel{(1) \leftrightarrow(\text { Q }}{\longrightarrow}(A) \text {; } \\
& \text { 若 }(A) \stackrel{\text { (i) } \times k}{\longrightarrow}(B), \quad \text { 则 }(B) \stackrel{(i) \div k}{\longrightarrow}(A) \text {; } \\
& \text { 若 }(A) \stackrel{\stackrel{(i)+k @)}{\longrightarrow}}{\longrightarrow}(B), \quad \text { 则 }(B) \stackrel{(i)-k @}{\longrightarrow}(A) \text {. }
\end{aligned}
$$

因此变换前的方程组与变换后的方程组是同解的, 这三种变换都是方程组 的同解变换, 所以最后求得的解 (2) 是方程组 (1) 的全部解.

在上述变换过程中, 实际上只对方程组的系数和常数进行运算, 未知数并未 参与运算. 因此,若记方程组 (1) 的增广矩阵为

$$
\boldsymbol{B}=(\boldsymbol{A}, \boldsymbol{b})=\left(\begin{array}{rrrrr}
2 & -1 & -1 & 1 & 2 \\
1 & 1 & -2 & 1 & 4 \\
4 & -6 & 2 & -2 & 4 \\
3 & 6 & -9 & 7 & 9
\end{array}\right) \text {, }
$$

那么上述对方程组的变换完全可以转换为对矩阵 $\boldsymbol{B}$ 的变换. 把方程组的上述三 种同解变换移植到矩阵上, 就得到矩阵的三种初等变换.

定义 1 下面三种变换称为矩阵的初等行变换:

(i) 对调两行 (对调 $i, j$ 两行,记作 $r_{i} \leftrightarrow r_{j}$ );

(ii) 以数 $k \neq 0$ 乘某一行中的所有元䋈(第 $i$ 行乘 $k$, 记作 $r_{i} \times k$ );

(iii) 把某一行所有元素的 $k$ 倍加到另一行对应的元素上去（第 $j$ 行的 $k$ 倍 加到第 $i$ 行上, 记作 $r_{i}+k r_{j}$ ).

把定义中的“行”换成“列”, 即得矩阵的初等列变换的定义(所用记号是把 “ $r$ ”换成“ $c$ ”).

矩阵的初等行变换与初等列变换,统称初等变换.

显然,三种初等变换都是可逆的,且其逆变换是同一类型的初等变换;变换 $r_{i} \leftrightarrow r_{j}$ 的逆变换就是其本身; 变换 $r_{i} \times k$ 的逆变换为 $r_{i} \times\left(\frac{1}{k}\right)$ (或记作 $r_{i} \div k$ ); 变换 $r_{i}+k r_{j}$ 的逆变换为 $r_{i}+(-k) r_{j}$ (或记作 $r_{i}-k r_{j}$ ).

如果矩阵 $\boldsymbol{A}$ 经有限次初等行变换变成矩阵 $\boldsymbol{B}$, 就称矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 行等价, 记 作 $\boldsymbol{A} \sim \boldsymbol{\sim}$; 如果矩阵 $\boldsymbol{A}$ 经有限次初等列变换变成矩阵 $\boldsymbol{B}$, 就称矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 列等 柋, 记作 $\boldsymbol{A}-\boldsymbol{B}$; 如果矩阵 $\boldsymbol{A}$ 经有限次初等变换变成矩阵 $\boldsymbol{B}$, 就称䓡阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 等 柋, 记作 $\boldsymbol{A} \sim \boldsymbol{B}$.

矩阵之间的等价关系具有下列性质:

(i) 反身性 $\boldsymbol{A} \sim \boldsymbol{A}$;

(ii) 对称性 若 $A \sim B$, 则 $B \sim A$;

(iii) 传递性 若 $\boldsymbol{A} \sim \boldsymbol{B}, \boldsymbol{B} \sim \boldsymbol{C}$, 则 $\boldsymbol{A} \sim \boldsymbol{C}$.

下面用矩阵的初等行变换来解方程组 (1), 其过程可与方程组 (1) 的消元过 程一一对照

$$
\begin{aligned}
& \frac{r_{1}-r_{2}}{r_{3} \div 2}\left(\begin{array}{rrrrr}
1 & 1 & -2 & 1 & 4 \\
2 & -1 & -1 & 1 & 2 \\
2 & -3 & 1 & -1 & 2 \\
3 & 6 & -9 & 7 & 9
\end{array}\right)=\boldsymbol{B}_{1} \\
& \underset{\frac{r_{2}-r_{3}}{r_{3}-2 r_{1}}}{r_{4}-3 r_{1}}\left(\begin{array}{rrrrr}
1 & 1 & -2 & 1 & 4 \\
0 & 2 & -2 & 2 & 0 \\
0 & -5 & 5 & -3 & -6 \\
0 & 3 & -3 & 4 & -3
\end{array}\right)=\boldsymbol{B}_{2} \\
& \frac{r_{3} \div 2}{r_{4}-3 r_{2}}\left(\begin{array}{rrrrr}
1 & 1 & -2 & 1 & 4 \\
0 & 1 & -1 & 1 & 0 \\
0 & 0 & 0 & 2 & -6 \\
0 & 0 & 0 & 1 & -3
\end{array}\right)=\boldsymbol{B}_{3} \\
& \underset{r_{3}-2 r_{3}+r_{4}}{r_{3}}\left(\begin{array}{rrrrr}
1 & 1 & -2 & 1 & 4 \\
0 & 1 & -1 & 1 & 0 \\
0 & 0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)=\boldsymbol{B}_{4} .
\end{aligned}
$$

由方程组 $\left(B_{4}\right)$ 得到解 $(2)$ 的回代过程,也可用矩阵的初等行变换来完成,即

$$
\boldsymbol{B}_{4} \frac{r_{1}-r_{2}}{r_{2}-r_{3}}\left(\begin{array}{rrrrr}
1 & 0 & -1 & 0 & 4 \\
\hdashline 0 & 1 & -1 & 0 & 3 \\
0 & 0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)=\boldsymbol{B}_{5},
$$

$B_{5}$ 对应方程组

$$
\left\{\begin{array}{l}
x_{1}-x_{3}=4, \\
x_{2}-x_{3}=3, \\
x_{4}=-3,
\end{array}\right.
$$

取 $x_{3}$ 为自由未知数,并令 $x_{3}=c$, 即得

$$
\boldsymbol{x}=\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=\left(\begin{array}{c}
c+4 \\
c+3 \\
c \\
-3
\end{array}\right)=c\left(\begin{array}{l}
1 \\
1 \\
1 \\
0
\end{array}\right)+\left(\begin{array}{r}
4 \\
3 \\
0 \\
-3
\end{array}\right),
$$

其中 $c$ 为任意常数.

矩阵 $\boldsymbol{B}_{4}$ 和 $\boldsymbol{B}_{5}$ 都称为行阶梯形矩阵, 其特点是: 可画出一条阶梯线, 线的下 方全为 0 ; 每个台阶只有一行, 台阶数即是非零行的行数, 阶梯线的坚线 (每段坚 线的长度为一行)后面的第一个元素为非零元, 也就是非零行的第一个非零元. 行阶梯形矩阵 $\boldsymbol{B}_{5}$ 还称为行最简形矩阵,其特点是: 非零行的第一个非零元 为 1 ,且这些非零元所在的列的其他元素都为 0 .

用归纳法不难证明(这里不证): 对于任何矩阵 $\boldsymbol{A}_{m \times n}$, 总可经过有限次初等 行变换把它变为行阶梯形矩阵和行最简形矩阵.

利用初等行变换, 把一个矩阵化为行阶梯形矩阵和行最简形矩阵, 是一种很 重要的运算. 由引例可知, 要解线性方程组只需把增广矩阵化为行最简形矩阵.

由行最简形矩阵 $\boldsymbol{B}_{5}$, 即可写出方程组的解 (2), 反之, 由方程组的解 (2) 也可 写出矩阵 $\boldsymbol{B}_{5}$. 由此可猜想到一个矩阵的行最简形矩阵是惟一确定的 (行阶梯形 矩阵中非零行的行数也是惟一确定的).

对行最简形矩阵再施以初等列变换, 可变成一种形状更简单的矩阵, 称为禁 准形. 例如

$$
\boldsymbol{B}_{5}=\left(\begin{array}{rrrrr}
1 & 0 & -1 & 0 & 4 \\
0 & 1 & -1 & 0 & 3 \\
0 & 0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right) \underset{\substack{c_{3}-c_{4} \\
c_{4}+c_{1}+c_{2} \\
c_{5}-4 c_{1}-3 c_{2}+3 c_{3}}}{-1}\left(\begin{array}{lllll}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)=\boldsymbol{F},
$$

矩阵 $\boldsymbol{F}$ 称为矩阵 $\boldsymbol{B}$ 的标准形, 其特点是: $\boldsymbol{F}$ 的左上角是一个单位矩阵, 其余元素 全为 0 .

对于 $m \times n$ 矩阵 $\boldsymbol{A}$, 总可经过初等变换(行变换和列变换)把它化为标准形

$$
\boldsymbol{F}=\left(\begin{array}{ll}
E_{r} & \boldsymbol{O} \\
\boldsymbol{O} & \boldsymbol{O}
\end{array}\right)_{m \times n},
$$

此标准形由 $m, n, r$ 三个数完全确定, 其中 $r$ 就是行阶梯形矩阵中非零行的行 数. 所有与 $\boldsymbol{A}$ 等价的矩阵组成一个集合,标准形 $\boldsymbol{F}$ 是这个集合中形状最简单的 矩阵.

矩阵的初等变换是矩阵的一种最基本的运算, 为探讨它的应用, 需要研究它 的性质,下面介绍它的一个最基本的性质。

定理 1 设 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 为 $m \times n$ 矩阵,那么:

(i) $\stackrel{\boldsymbol{A} \sim \boldsymbol{B}}{\sim}$ 的充分必要条件是存在 $m$ 阶可逆矩阵 $\boldsymbol{P}$; 使 $\boldsymbol{P A}=\boldsymbol{B}$;

(ii) $\boldsymbol{A} \sim \boldsymbol{B}$ 的充分必要条件是存在 $n$ 阶可逆矩阵 $Q$, 便 $A Q=B$;

(iii) $\boldsymbol{A} \sim \boldsymbol{B}$ 的充分必要条件是存在 $m$ 阶可逆矩阵 $\boldsymbol{P}$ 及 $n$ 阶可逆矩阵 $Q$, 使 $P A Q=B$.

为证明定理 1 , 我们引进初等矩阵的知识.

定义 2 由单位阵 $E$ 经过一次初等变换得到的矩阵称为初等聟阵.

三种初等变换对应有三种初等矩阵.

(i) 把单位阵中第 $i, j$ 两行对调 (或第 $i, j$ 两列对调), 得初等矩阵

用 $m$ 阶初等矩阵 $\boldsymbol{E}_{n u}(i, j)$ 左乘矩阵 $\boldsymbol{A}=\left(a_{i j}\right)_{m \times n}$, 得

其结果相当于对矩阵 $\boldsymbol{A}$ 施行第一种初等行变换: 把 $\boldsymbol{A}$ 的第 $i$ 行与第 $j$ 行对调 $\left(r_{i} \leftrightarrow r_{j}\right)$. 类似地, 以 $n$ 阶初等矩阵 $\boldsymbol{E}_{n}(i, j)$ 右乘矩阵 $\boldsymbol{A}$, 其结果相当于对矩阵 $\boldsymbol{A}$ 施行第一种初等列变 换: 把 $\boldsymbol{A}$ 的第 $i$ 列与第 $j$ 列对调 $\left(c_{i} \leftrightarrow c_{,}\right)$.

(ii) 以数 $k \neq 0$ 乘单位阵的第 $i$ 行(或第 $i$ 列),得切等矩阵

$$
\boldsymbol{E}(i(k))=\left(\begin{array}{cccccc}
1 & & & & & \\
& \ddots & & & & \\
& & & & & \\
& & 1 & & & \\
& & k & & & \\
& & & 1 & & \\
& & & & \ddots & \\
& & & & & 1
\end{array}\right) \text { —第 } i \text { 行, }
$$

可以验知: 以 $\boldsymbol{E}_{m}(i(k))$ 左乘矩阵 $\boldsymbol{A}$, 其结果相当于以数 $k$ 乘 $\boldsymbol{A}$ 的第 $i$ 行 $\left(r_{i} \times k\right)$; 以 $\boldsymbol{E}_{n}(i(k))$ 右乘矩阵 $\boldsymbol{A}$,其结果相当于以数 $k$ 乘 $\boldsymbol{A}$ 的第 $i$ 列 $\left(c_{i} \times k\right)$.

(iii) 以 $k$ 乘 $\boldsymbol{E}$ 的第 $j$ 行加到第 $i$ 行上或以 $k$ 乘 $\boldsymbol{E}$ 的第 $i$ 列加到第 $j$ 列上，得初等矩阵

可以验知 : 以 $\boldsymbol{E}_{m}(i j(k))$ 左乘矩阵 $\boldsymbol{A}$, 其结果相当于把 $\boldsymbol{A}$ 的第 $j$ 行乘 $k$ 加到第 $i$ 行上 $\left(r_{i}+\right.$ $\left.k r_{j}\right)$, 以 $\boldsymbol{E}_{n}(i j(k))$ 右乘矩阵 $\boldsymbol{A}$, 其结果相当于把 $\boldsymbol{A}$ 的第 $i$ 列乘 $k$ 加到第 $j$ 列上 $\left(c_{j}+k c_{i}\right)$.

归纳上面的讨论,可得

性质 1 设 $A$ 是一个 $m \times n$ 矩阵, 对 $A$ 施行一次初等行变换, 相当于在 $A$ 的左边乘以相 应的 $m$ 阶初等矩阵; 对 $\boldsymbol{A}$ 施行一次初等列变换, 相当于在 $\boldsymbol{A}$ 的右边乘以相应的 $n$.阶初等矩 阵.

显然初等矩阵都是可逆的, 且其逆阵是同一类型的初等矩阵: $\boldsymbol{E}(i, j)^{-1}=\boldsymbol{E}(i, j)$; $\boldsymbol{E}(i(k))^{-1}=\boldsymbol{E}\left(i\left(\frac{1}{k}\right)\right) ; \boldsymbol{E}(i j(k))^{-1}=\boldsymbol{E}(i j(-k))$.

性质 2 方阵 $A$ 可逆的充分必要条件是存在有限个初等矩阵 $P_{1}, P_{2}, \cdots, P_{1}$, 使 $A=$ $P_{1} P_{2} \cdots P_{1}$.

证 先证充分性. 设 $A=P_{1} P_{2} \cdots P_{1}$, 因初等矩阵可逆,有限个可逆矩阵的乘积仍可逆. 故 $\boldsymbol{A}$ 可逆.

再证必要性. 设 $n$ 阶方阵 $\boldsymbol{A}$ 可逆,且 $\boldsymbol{A}$ 的标准形矩阵为 $\boldsymbol{F}$, 由于 $\boldsymbol{F} \sim \boldsymbol{A}$, 知 $\boldsymbol{F}$ 经有限次初 等变换可化为 $A$, 即有初等矩阵 $P_{1}, P_{2}, \cdots, P_{l}$, 使

$$
A=P_{1} \cdots P_{s} F P_{s+1} \cdots P_{t},
$$

$$
\boldsymbol{F}=\left(\begin{array}{cc}
E_{r} & O \\
O & O
\end{array}\right)_{n \times n}
$$

中的 $r<n$, 则 $|F|=0$, 与 $F$ 可逆矛盾, 因此必有 $r=n$, 即 $F=E$, 从而

$$
A=P_{1} P_{2} \cdots P_{1} \text {. }
$$

证毕

下面应用初等矩阵的知识来证明定理 1 .

定理 1 的证明:

(i) 依据 $\boldsymbol{A} \sim \boldsymbol{B}$ 的定义和初等矩阵的性质, 有

$\boldsymbol{A} \sim \boldsymbol{B} \Leftrightarrow \boldsymbol{A}$ 经有限次初等行变换变成 $B$

$\Leftrightarrow$ 存在有限个 $m$ 阶初等矩阵 $P_{1}, P_{2}, \cdots, P_{l}$, 使 $P_{1} \cdots P_{2} P_{1} A=B$

$\Leftrightarrow$ 存在 $m$ 阶可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P A}=\boldsymbol{B}$.

类似可证明 (ii)和 (iii).

证毕

定理 1 把矩阵的初等变换与矩阵的乘法联系了起来, 从而可以依据矩阵乘

法的运算规律得到初等变换的运算规律, 也可以利用矩阵的初等变换去研究矩 阵的乘法. 下面先给出定理 1 的一个推论,然后介绍一种利用初等变换求逆阵 的方法.

推论 方阵 $\boldsymbol{A}$ 可逆的充分必要条件是 $\boldsymbol{A} \sim \boldsymbol{r}$.

证 $A$ 可逆 $\Leftrightarrow$ 存在可逆矩阵 $P$,使 $P A=E$

$$
\Leftrightarrow \boldsymbol{A} \stackrel{r}{\sim} \boldsymbol{E}
$$

定理 1 表明, 如果 $\boldsymbol{A} \sim \boldsymbol{B}$, 即 $\boldsymbol{A}$ 经一系列初等行变换变为 $\boldsymbol{B}$, 则有可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P A}=\boldsymbol{B}$. 那么, 如何去求出这个可逆矩阵 $\boldsymbol{P}$ ?

由于 $P A=B \Leftrightarrow\left\{\begin{array}{l}P A=B, \\ P E=P\end{array} \Leftrightarrow P(A, E)=(B, P) \Leftrightarrow(A, E)(B, P)\right.$, 因 此, 如果对矩阵 $(\boldsymbol{A}, \boldsymbol{E})$ 作初等行变换, 那么, 当把 $\boldsymbol{A}$ 变为 $\boldsymbol{B}$ 时, $E$ 就变为 $P$. 于 是就得到所求的可逆矩阵 $\boldsymbol{P}$.

例 1 设 $\boldsymbol{A}=\left(\begin{array}{rrr}2 & -1 & -1 \\ 1 & 1 & -2 \\ 4 & -6 & 2\end{array}\right)$ 的行最简形矩阵为 $\boldsymbol{F}$, 求 $\boldsymbol{F}$, 并求一个可逆矩 阵 $\boldsymbol{P}$,使 $\boldsymbol{P A}=\boldsymbol{F}$.

解 把 $\boldsymbol{A}$ 用初等行变换化成行最简形,即为 $\boldsymbol{F}$. 但需求出 $\boldsymbol{P}$,故按上段所 述,对 $(\boldsymbol{A}, \boldsymbol{E})$ 作初等行变换把 $\boldsymbol{A}$ 化成行最简形,便同时得到 $\boldsymbol{F}$ 和 $\boldsymbol{P}$. 运算如下:

$$
\begin{aligned}
& (\boldsymbol{A}, \boldsymbol{E})=\left(\begin{array}{rrrrrr}
2 & -1 & -1 & 1 & 0 & 0 \\
1 & 1 & -2 & 0 & 1 & 0 \\
4 & -6 & 2 & 0 & 0 & 1
\end{array}\right) \begin{array}{l}
r_{3}-r_{2}-2 r_{2} \\
r_{2}-2 r_{1}
\end{array}\left(\begin{array}{rrrrrr}
1 & 1 & -2 & 0 & 1 & 0 \\
0 & -3 & 3 & 1 & -2 & 0 \\
0 & -4 & 4 & -2 & 0 & 1
\end{array}\right) \\
& \frac{r_{1}-r_{3}}{r_{3}+4 r_{2}}\left(\begin{array}{rrrrrr}
1 & 0 & -1 & -3 & 3 & 1 \\
0 & 1 & -1 & 3 & -2 & -1 \\
0 & 0 & 0 & 10 & -8 & -3
\end{array}\right) \text {, }
\end{aligned}
$$

故 $\boldsymbol{F}=\left(\begin{array}{rrr}1 & 0 & -1 \\ 0 & 1 & -1 \\ 0 & 0 & 0\end{array}\right)$ 为 $\boldsymbol{A}$ 的行最简形,而使 $\boldsymbol{P A}=\boldsymbol{F}$ 的可逆矩阵

$$
\boldsymbol{P}=\left(\begin{array}{rrr}
-3 & 3 & 1 \\
3 & -2 & -1 \\
10 & -8 & -3
\end{array}\right)
$$

注上述解中所得 $(\boldsymbol{F}, \boldsymbol{P})$, 可继续作初等行变换 $r_{3} \times k, r_{1}+k r_{3}, r_{2}+k r_{3}$, 则 $\boldsymbol{F}$ 不变 $\boldsymbol{P}$ 变. 由此可知本例中使 $\boldsymbol{P A}=\boldsymbol{F}$ 的可逆矩阵 $\boldsymbol{P}$ 不是惟一的.

例 2 设 $\boldsymbol{A}=\left(\begin{array}{rrr}0 & -2 & 1 \\ 3 & 0 & -2 \\ -2 & 3 & 0\end{array}\right)$, 证明 $\boldsymbol{A}$ 可逆,并求 $\boldsymbol{A}^{-1}$.

解 如同例 1,初等行变换把 $(\boldsymbol{A}, \boldsymbol{E})$ 化成 $(\boldsymbol{F}, \boldsymbol{P})$, 其中 $\boldsymbol{F}$ 为 $\boldsymbol{A}$ 的行最简形. 如果 $\boldsymbol{F}=\boldsymbol{E}$, 则 $\boldsymbol{A}$ 可逆,并由 $\boldsymbol{P A}=\boldsymbol{E}$, 知 $\boldsymbol{P}=\boldsymbol{A}^{-1}$. 运算如下:

$$
\begin{aligned}
& (\boldsymbol{A}, \boldsymbol{E})=\left(\begin{array}{rrrrrr}
0 & -2 & 1 & 1 & 0 & 0 \\
3 & 0 & -2 & 0 & 1 & 0 \\
-2 & 3 & 0 & 0 & 0 & 1
\end{array}\right) \\
& \underset{r_{1}+2 r_{2}}{r_{3} \times 3}\left(\begin{array}{rrrrrr}
3 & 0 & -2 & 0 & 1 & 0 \\
0 & -2 & 1 & 1 & 0 & 0 \\
0 & 9 & -4 & 0 & 2 & 3
\end{array}\right) \underset{r_{3}+9 r_{2}}{r_{3} \times 2}\left(\begin{array}{rrrrrr}
3 & 0 & -2 & 0 & 1 & 0 \\
0 & -2 & 1 & 1 & 0 & 0 \\
0 & 0 & 1 & 9 & 4 & 6
\end{array}\right)
\end{aligned}
$$

$$
\frac{r_{1}+2 r_{3}}{r_{2}-r_{3}}\left(\begin{array}{rrrrrr}
3 & 0 & 0 & 18 & 9 & 12 \\
0 & -2 & 0 & -8 & -4 & -6 \\
0 & 0 & 1 & 9 & 4 & 6
\end{array}\right) \underset{r_{2} \div(-2)}{r_{1} \div 3}\left(\begin{array}{llllll}
1 & 0 & 0 & 6 & 3 & 4 \\
0 & 1 & 0 & 4 & 2 & 3 \\
0 & 0 & 1 & 9 & 4 & 6
\end{array}\right),
$$

因 $\boldsymbol{A} \stackrel{\boldsymbol{r}}{\sim} \boldsymbol{E}$,故 $\boldsymbol{A}$ 可逆,且 $\boldsymbol{A}^{-1}=\left(\begin{array}{lll}6 & 3 & 4 \\ 4 & 2 & 3 \\ 9 & 4 & 6\end{array}\right)$.

例 3 求解矩阵方程 $\boldsymbol{A} \boldsymbol{X}=\boldsymbol{B}$, 其中 $\boldsymbol{A}=\left(\begin{array}{rrr}2 & 1 & -3 \\ 1 & 2 & -2 \\ -1 & 3 & 2\end{array}\right), \boldsymbol{B}=\left(\begin{array}{rr}1 & -1 \\ 2 & 0 \\ -2 & 5\end{array}\right)$.

解 设可逆矩阵 $\boldsymbol{P}$ 使 $\boldsymbol{P A}=\boldsymbol{F}$ 为行最简形,则

$$
P(A, B)=(F, P B),
$$

因此对矩阵 $(\boldsymbol{A}, \boldsymbol{B})$ 作初等行变换把 $\boldsymbol{A}$ 变为 $\boldsymbol{F}$, 同时把 $\boldsymbol{B}$ 变为 $\boldsymbol{P B}$. 若 $\boldsymbol{F}=\boldsymbol{E}$, 则 $A$ 可逆, 且 $P=A^{-1}$, 这时所给方程有惟一解 $X=P B=A^{-1} B$.

$$
\begin{gathered}
\left.(\boldsymbol{A}, \boldsymbol{B})=\left(\begin{array}{rrrrr}
2 & 1 & -3 & 1 & -1 \\
1 & 2 & -2 & 2 & 0 \\
-1 & 3 & 2 & -2 & 5
\end{array}\right) \stackrel{\substack{r_{1}-r_{2} \\
r_{2}-2 r_{1}}}{\frac{r_{3}+r_{1}}{1}} \begin{array}{rrrrr}
1 & 2 & -2 & 2 & 0 \\
0 & -3 & 1 & -3 & -1 \\
0 & 5 & 0 & 0 & 5
\end{array}\right) \\
\underset{r_{3} \rightarrow r_{2}-5}{r_{3}+3 r_{2}}\left(\begin{array}{rrrrr}
1 & 2 & -2 & 2 & 0 \\
0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & -3 & 2
\end{array}\right) r_{1}^{-2 r_{2}+2 r_{3}}\left(\begin{array}{rrrrr}
1 & 0 & 0 & -4 & 2 \\
0 & 1 & 0 & 0 & 1 \\
0 & 0 & 1 & -3 & 2
\end{array}\right),
\end{gathered}
$$

可见 $\boldsymbol{A} \stackrel{r}{\sim} \boldsymbol{E}$, 因此 $\boldsymbol{A}$ 可逆, 且

$$
\boldsymbol{X}=\boldsymbol{A}^{-1} \boldsymbol{B}=\left(\begin{array}{rr}
-4 & 2 \\
0 & 1 \\
-3 & 2
\end{array}\right)
$$

即为所给方程的惟一解.

例 2 和例 3 是一种用初等行变换求 $\boldsymbol{A}^{-1}$ 或 $\boldsymbol{A}^{-1} \boldsymbol{B}$ 的方法,当 $\boldsymbol{A}$ 为 3 阶或更 高阶的矩阵时, 求 $\boldsymbol{A}^{-1}$ 或 $\boldsymbol{A}^{-1} \boldsymbol{B}$ 通常都用此方法. 这是当 $\boldsymbol{A}$ 为可逆矩阵时, 求 解方程 $\boldsymbol{A X}=\boldsymbol{B}$ 的方法 (求 $\boldsymbol{A}^{-1}$ 也就是求方程 $\boldsymbol{A X}=\boldsymbol{E}$ 的解). 这方法就是把方 程 $\boldsymbol{A X}=\boldsymbol{B}$ 的增广矩阵 $(\boldsymbol{A}, \boldsymbol{B})$ 化为行最简形，从而求得方程的解. 这与求解线 性方程组 $\boldsymbol{A x}=\boldsymbol{b}$ 时把增广矩阵 $(\boldsymbol{A}, \boldsymbol{b})$ 化为行最简形的方法是一样的.

## $\S 2$ 矩阵 的 秩

上节中我们指出, 给定一个 $m \times n$ 矩阵 $\boldsymbol{A}$, 它的标准形

$$
\boldsymbol{F}=\left(\begin{array}{cc}
\boldsymbol{E} & \boldsymbol{O} \\
\boldsymbol{O} & \boldsymbol{O}
\end{array}\right)_{m \times n}
$$

www.TopSage.com 由数 $r$ 完全确定. 这个数也就是 $\boldsymbol{A}$ 的行阶梯形中非零行的行数,这个数便是矩 阵 $\boldsymbol{A}$ 的秩.但由于这个数的惟一性尚末证明,因此下面用另一种说法给出矩阵 的秩的定义.

定义 3 在 $m \times n$ 矩阵 $\boldsymbol{A}$ 中, 任取 $k$ 行与 $k$ 列 $(k \leqslant m, k \leqslant n)$, 位于这些行 列交叉处的 $k^{2}$ 个元素,不改变它们在 $\boldsymbol{A}$ 中所处的位置次序而得的 $k$ 阶行列式, 称为矩阵 $\boldsymbol{A}$ 的 $k$ 阶子式.

$m \times n$ 矩阵 $\boldsymbol{A}$ 的 $k$ 阶子式共有 $\mathrm{C}_{m}^{k} \cdot \mathrm{C}_{n}^{k}$ 个.

定义 4 设在矩阵 $\boldsymbol{A}$ 中有一个不等于 0 的 $r$ 阶子式 $D$, 且所有 $r+1$ 阶子式 (如果存在的话) 全等于 0 , 那么 $D$ 称为矩阵 $\boldsymbol{A}$ 的最高阶非零子式, 数 $r$ 称为矩 阵 $\boldsymbol{A}$ 的秩, 记作 $R(\boldsymbol{A})$. 并规定零矩阵的秩等于 0 .

由行列式的性质可知, 在 $\boldsymbol{A}$ 中当所有 $r+1$ 阶子式全等于 0 时,所有高于 $r$ +1 阶的子式也全等于 0 , 因此把 $r$ 阶非零子式称为最高阶非零子式,而 $\boldsymbol{A}$ 的秩 $R(\boldsymbol{A})$ 就是 $\boldsymbol{A}$ 的非零子式的最高阶数.

由于 $R(\boldsymbol{A})$ 是 $\boldsymbol{A}$ 的非零子式的最高阶数,因此,若矩阵 $\boldsymbol{A}$ 中有某个 $s$ 阶子 式不为 0 , 则 $R(\boldsymbol{A}) \geqslant s$; 若 $\boldsymbol{A}$ 中所有 $t$ 阶子式全为 0 , 则 $R(\boldsymbol{A})<t$.

显然, 若 $\boldsymbol{A}$ 为 $m \times n$ 矩阵, 则 $0 \leqslant R(\boldsymbol{A}) \leqslant \min \{m, n\}$.

由于行列式与其转置行列式相等, 因此 $\boldsymbol{A}^{\top}$ 的子式与 $\boldsymbol{A}$ 的子式对应相等, 从而 $R\left(\boldsymbol{A}^{\mathrm{T}}\right)=R(\boldsymbol{A})$.

对于 $n$ 阶矩阵 $\boldsymbol{A}$, 由于 $\boldsymbol{A}$ 的 $n$ 阶子式只有一个 $|\boldsymbol{A}|$, 故当 $|\boldsymbol{A}| \neq 0$ 时 $R(\boldsymbol{A})$ $=n$, 当 $|\boldsymbol{A}|=0$ 时 $R(\boldsymbol{A})<n$. 可见可逆矩阵的秩等于矩阵的阶数, 不可逆矩阵 的秩小于矩阵的阶数. 因此, 可逆矩阵又称满秩矩阵, 不可逆矩阵 (奇异矩阵) 又 称降秩矩阵.

例 4 求矩阵 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 的秩,其中

$$
\boldsymbol{A}=\left(\begin{array}{rrr}
1 & 2 & 3 \\
2 & 3 & -5 \\
4 & 7 & 1
\end{array}\right), \boldsymbol{B}=\left(\begin{array}{rrrrr}
2 & -1 & 0 & 3 & -2 \\
0 & 3 & 1 & -2 & 5 \\
0 & 0 & 0 & 4 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right) .
$$

解 在 $\boldsymbol{A}$ 中,容易看出一个 2 阶子式 $\left|\begin{array}{ll}1 & 2 \\ 2 & 3\end{array}\right| \neq 0, \boldsymbol{A}$ 的 3 阶子式只有一个 $|\boldsymbol{A}|$, 经计算可知 $|\boldsymbol{A}|=0$, 因此 $R(\boldsymbol{A})=2$.

$\boldsymbol{B}$ 是一个行阶梯形矩阵,其非零行有 3 行, 即知 $\boldsymbol{B}$ 的所有 4 阶子式全为零. 而以三个非零行的第一个非零元为对角元的 3 阶行列式

$$
\left|\begin{array}{rrr}
2 & -1 & 3 \\
0 & 3 & -2 \\
0 & 0 & 4
\end{array}\right|
$$

是一个上三角形行列式, 它显然不等于 0 , 因此 $R(\boldsymbol{B})=3$.

从本例可知, 对于一般的矩阵, 当行数与列数较高时, 按定义求秩是很麻烦 的. 然而对于行阶梯形矩阵, 它的秩就等于非零行的行数, 一看便知冊须计算. 因 此自然想到用初等变换把矩阵化为行阶梯形矩阵, 但两个等价矩阵的秋是否相 等呢? 下面的定理对此作出肯定的回答.

定理 2 若 $\boldsymbol{A} \sim \boldsymbol{B}$, 则 $R(\boldsymbol{A})=R(\boldsymbol{B})$.

证 先证明: 若 $\boldsymbol{A}$ 经一次初等行变换变为 $\boldsymbol{B}$, 则 $R(\boldsymbol{A}) \leqslant R(\boldsymbol{B})$.

设 $R(\boldsymbol{A})=r$,且 $\boldsymbol{A}$ 的某个 $r$ 阶子式 $D \neq 0$.

当 $A \stackrel{r}{-} B$ 或 $A \stackrel{r}{-} B$ 时, 在 $B$ 中总能找到与 $D$ 相对应的 $r$ 阶子式 $D_{1}$, 由于 $D_{1}=$ $D$ 或 $D_{1}=-D$ 或 $D_{1}=k D$, 因此 $D_{1} \neq 0$, 从而 $R(B) \geqslant r$.

当 $A \stackrel{r_{i}+k r_{j}}{-} B$ 时, 因为对于作变换 $r_{i} \leftrightarrow r_{j}$ 时结论成立, 所以只需考怎 $A \stackrel{r_{1}+k r_{2}}{-} B$ 这一特 殊情形. 分两种情形讨论: (1) $\boldsymbol{A}$ 的 $r$ 阶非零子式 $D$ 不包含 $A$ 的第 1 行, 这时 $D$ 也是 $B$ 的 $r$ 阶 非笭子式, 故 $R(\boldsymbol{B}) \geqslant r_{\text {; }}$ (2) $D$ 包含 $\boldsymbol{A}$ 的第 1 行, 这时把 $\boldsymbol{B}$ 中与 $D$ 对应的 $r$ 阶子式 $D_{1}$ 记作

$$
D_{1}=\left|\begin{array}{c}
r_{1}+k r_{2} \\
r_{p} \\
\vdots \\
r_{4}
\end{array}\right|=\left|\begin{array}{c}
r_{1} \\
r_{p} \\
\vdots \\
r_{4}
\end{array}\right|+k\left|\begin{array}{c}
r_{2} \\
r_{p} \\
\vdots \\
r_{4}
\end{array}\right|=D+k D_{2},
$$

若 $p=2$, 则 $D_{1}=D \neq 0$; 若 $p \neq 2$, 则 $D_{2}$ 也是 $B$ 的 $r$ 阶子式, 由 $D_{1}-k D_{2}=D \neq 0$, 知 $D_{1}$ 与 $D_{2}$ 不同时为 0 . 总之, $\boldsymbol{B}$ 中存在 $r$ 阶非零子式 $D_{1}$ 或 $D_{2}$, 故 $R(\boldsymbol{B}) \geqslant r$.

以上证明了若 $A$ 经一次初等行变换变为 $B$, 则 $R(A) \leqslant R(B)$. 由于 $B$ 亦可经一次初等 行变换变为 $\boldsymbol{A}$, 故也有 $R(\boldsymbol{B}) \leqslant R(\boldsymbol{A})$. 因此 $R(\boldsymbol{A})=R(\boldsymbol{B})$.

经一次初等行变换矩阵的秩不变, 即可知经有限次初等行变换矩阵的秩仍不变.

设 $\boldsymbol{A}$ 经初等列变换变为 $\boldsymbol{B}$, 则 $\boldsymbol{A}^{\mathrm{T}}$ 经初等行变换变为 $\boldsymbol{B}^{\mathrm{T}}$, 由上段证明知 $R\left(\boldsymbol{A}^{\mathrm{T}}\right)=R\left(\boldsymbol{B}^{\mathrm{T}}\right)$, 又 $R(\boldsymbol{A})=R\left(\boldsymbol{A}^{\mathrm{T}}\right), R(\boldsymbol{B})=R\left(\boldsymbol{B}^{\mathrm{T}}\right)$, 因此 $R(\boldsymbol{A})=R(\boldsymbol{B})$.

总之, 若 $A$ 经有限次初等变换变为 $B($ 即 $A-B)$, 则 $R(A)=R(B)$.

证毕

由于 $\boldsymbol{A} \sim \boldsymbol{B}$ 的充分必要条件是有可逆矩阵 $P, Q$, 使 $P A Q=B$, 因此可得

推论 若可逆矩阵 $\boldsymbol{P}, \boldsymbol{Q}$ 使 $\boldsymbol{P} \boldsymbol{A} Q=\boldsymbol{B}$, 则 $R(\boldsymbol{A})=R(\boldsymbol{B})$.

根据定理 2 , 为求矩阵的秩, 只要把矩阵用初等行变换变成行阶梯形矩阵, 行阶梯形矩阵中非零行的行数即是该矩阵的秩.

例 5 设 $\quad \boldsymbol{A}=\left(\begin{array}{rrrrr}3 & 2 & 0 & 5 & 0 \\ 3 & -2 & 3 & 6 & -1 \\ 2 & 0 & 1 & 5 & -3 \\ 1 & 6 & -4 & -1 & 4\end{array}\right)$,

求矩阵 $\boldsymbol{A}$ 的秩,并求 $\boldsymbol{A}$ 的一个最高阶非零子式.

解 先求 $\boldsymbol{A}$ 的秩, 为此对 $\boldsymbol{A}$ 作初等行变换变成行阶梯形矩阵

$$
\begin{aligned}
& \frac{r_{3}-3 r_{2}}{r_{1}-4 r_{2}}\left(\begin{array}{rrrrr}
1 & 6 & -4 & -1 & 4 \\
0 & -4 & 3 & 1 & -1 \\
0 & 0 & 0 & 4 & -8 \\
0 & 0 & 0 & 4 & -8
\end{array}\right) \stackrel{r_{1}-r_{3}}{=}\left(\begin{array}{rrrrr}
1 & 6 & -4 & -1 & 4 \\
0 & -4 & 3 & 1 & -1 \\
0 & 0 & 0 & 4 & -8 \\
0 & 0 & 0 & 0 & 0
\end{array}\right) \text {, }
\end{aligned}
$$

因为行阶梯形矩阵有 3 个非零行, 所以 $R(\boldsymbol{A})=3$.

再求 $\boldsymbol{A}$ 的一个最高阶非零子式. 因 $R(\boldsymbol{A})=3$, 知 $\boldsymbol{A}$ 的最高阶非零子式为 3 阶. $\boldsymbol{A}$ 的 3 阶子式共有 $\mathrm{C}_{4}^{3} \cdot \mathrm{C}_{5}^{3}=40$ 个, 要从 40 个子式中找出一个非零子式, 是 比较麻烦的. 考察 $\mathrm{A}$ 的行阶梯形矩阵, 记 $\mathrm{A}=\left(a_{1}, a_{2}, a_{3}, a_{4}, a_{5}\right)$, 则矩阵 $\boldsymbol{A}_{0}=$ $\left(a_{1}, a_{2}, a_{4}\right)$ 的行阶梯形矩阵为

$$
\left(\begin{array}{rrr}
1 & 6 & -1 \\
0 & -4 & 1 \\
0 & 0 & 4 \\
0 & 0 & 0
\end{array}\right)
$$

知 $R\left(\boldsymbol{A}_{0}\right)=3$, 故 $\boldsymbol{A}_{0}$ 中必有 3 阶非零子式. $\boldsymbol{A}_{0}$ 的 3 阶子式有 4 个,在 $\boldsymbol{A}_{0}$ 的 4 个 3 阶子式中找一个非零子式比在 $\boldsymbol{A}$ 中找非零子式要方便许多. 今计算 $\boldsymbol{A}_{0}$ 的 前三行构成的子式

$$
\left|\begin{array}{rrr}
3 & 2 & 5 \\
3 & -2 & 6 \\
2 & 0 & 5
\end{array}\right|=\left|\begin{array}{rrr}
3 & 2 & 5 \\
6 & 0 & 11 \\
2 & 0 & 5
\end{array}\right|=-2\left|\begin{array}{rr}
6 & 11 \\
2 & 5
\end{array}\right| \neq 0,
$$

因此这个子式便是 $\boldsymbol{A}$ 的一个最高阶非零子式.

例 6 设 $A=\left(\begin{array}{rrrr}1 & -2 & 2 & -1 \\ 2 & -4 & 8 & 0 \\ -2 & 4 & -2 & 3 \\ 3 & -6 & 0 & -6\end{array}\right), b=\left(\begin{array}{l}1 \\ 2 \\ 3 \\ 4\end{array}\right)$,

求矩阵 $A$ 及矩阵 $B=(A, b)$ 的秩.

解 对 $\boldsymbol{B}$ 作初等行变换变为行阶梯形矩阵, 设 $\boldsymbol{B}$ 的行阶梯形矩阵为 $\widetilde{\boldsymbol{B}}=$ $(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{b}})$, 则 $\tilde{\boldsymbol{A}}$ 就是 $\boldsymbol{A}$ 的行阶梯形矩阵, 故从 $\tilde{\boldsymbol{B}}=(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{b}})$ 中可同时看出 $R(\boldsymbol{A})$ 及 $R(B)$.

$$
\begin{gathered}
\boldsymbol{B}=\left(\begin{array}{rrrrr}
1 & -2 & 2 & -1 & 1 \\
2 & -4 & 8 & 0 & 2 \\
-2 & 4 & -2 & 3 & 3 \\
3 & -6 & 0 & -6 & 4
\end{array}\right) \underset{r_{2}-2 r_{1}+2 r_{1}}{r_{4}-3 r_{1}}\left(\begin{array}{rrrrr}
1 & -2 & 2 & -1 & 1 \\
0 & 0 & 4 & 2 & 0 \\
0 & 0 & 2 & 1 & 5 \\
0 & 0 & -6 & -3 & 1
\end{array}\right) \\
\underset{\frac{r_{2}+r_{2}}{r_{4}+3 r_{2}}}{\frac{r_{2}-r_{2}}{0}}\left(\begin{array}{rrrrr}
1 & -2 & 2 & -1 & 1 \\
0 & 0 & 2 & 1 & 0 \\
0 & 0 & 0 & 0 & 5 \\
0 & 0 & 0 & 1
\end{array}\right) \underset{r_{4} \div 5}{\frac{r_{4}-r_{3}}{1}}\left(\begin{array}{rrrrr}
1 & -2 & 2 & -1 & 1 \\
0 & 0 & 2 & 1 & 0 \\
0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0 & 0
\end{array}\right),
\end{gathered}
$$

因此,

$$
R(\boldsymbol{A})=2, R(\boldsymbol{B})=3 \text {. }
$$

从矩阵 $\boldsymbol{B}$ 的行阶梯形矩阵可知, 本例中的 $\boldsymbol{A}$ 与 $\boldsymbol{b}$ 所对应的线性方程组 $\boldsymbol{A x}=\boldsymbol{b}$ 是无解的,这是因为行阶梯形矩阵的第 3 行表示矛盾方程 $0=1$.

例 7 设 $\quad \boldsymbol{A}=\left(\begin{array}{rrrr}1 & 2 & -1 & 1 \\ 3 & 2 & \lambda & -1 \\ 5 & 6 & 3 & \mu\end{array}\right)$,

已知 $R(A)=2$, 求 $\lambda$ 与 $\mu$ 的值.

因 $R(\boldsymbol{A})=2$, 故

$$
\left\{\begin{array} { l } 
{ 5 - \lambda = 0 , } \\
{ \mu - 1 = 0 , }
\end{array} \text { 即 } \left\{\begin{array}{l}
\lambda=5, \\
\mu=1 .
\end{array}\right.\right.
$$

下面讨论矩阵的秩的性质.前面我们已经提出了矩阵秩的一些最基本的性 质,归纳起来有:

(1) $0 \leqslant R\left(\boldsymbol{A}_{m \times n}\right) \leqslant \min |m, n|$;

(2) $R\left(\boldsymbol{A}^{\mathrm{T}}\right)=R(\boldsymbol{A})$;

(3) 若 $\boldsymbol{A} \sim \boldsymbol{B}$, 则 $R(\boldsymbol{A})=R(\boldsymbol{B})$;

(4) 若 $\boldsymbol{P} 、 Q$ 可逆,则 $R(\boldsymbol{P A} Q)=R(\boldsymbol{A})$.

下面再介绍几个常用的矩阵秩的性质:

(5) $\max \{R(\boldsymbol{A}), R(\boldsymbol{B})\} \leqslant R(\boldsymbol{A}, \boldsymbol{B}) \leqslant R(\boldsymbol{A})+R(\boldsymbol{B})$,

特别地, 当 $B=b$ 为非零列向量时, 有

$$
R(\boldsymbol{A}) \leqslant R(\boldsymbol{A}, \boldsymbol{b}) \leqslant R(\boldsymbol{A})+1 .
$$

证 因为 $\boldsymbol{A}$ 的最高阶非零子式总是 $(\boldsymbol{A}, \boldsymbol{B})$ 的非零子式, 所以 $R(\boldsymbol{A}) \leqslant$ $R(\boldsymbol{A}, \boldsymbol{B})$. 同理有 $R(\boldsymbol{B}) \leqslant R(\boldsymbol{A}, \boldsymbol{B})$. 两式合起来, 即为

$$
\max \{R(\boldsymbol{A}), R(\boldsymbol{B})\} \leqslant R(\boldsymbol{A}, \boldsymbol{B}) .
$$

www.TopSage.com 设 $R(\boldsymbol{A})=r, R(\boldsymbol{B})=t$. 把 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 分别作列变换化为列阶梯形 $\widetilde{\boldsymbol{A}}$ 和 $\boldsymbol{B}$, 则 $\tilde{\boldsymbol{A}}$ 和 $\widetilde{\boldsymbol{B}}$ 中分别含 $r$ 个和 $t$ 个非零列,故可设

$$
\boldsymbol{A} \sim \tilde{\sim} \tilde{\boldsymbol{A}}=\left(\tilde{a}_{1}, \cdots, \tilde{a}_{r}, \mathbf{0}, \cdots, 0\right), \boldsymbol{B} \sim \tilde{\boldsymbol{B}}=\left(\tilde{b}_{1}, \cdots, \tilde{b}_{t}, 0, \cdots, 0\right),
$$

从而 $(\boldsymbol{A}, \boldsymbol{B}) \stackrel{\llcorner}{\sim}(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{B}})$,

由于 $(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{B}})$ 中只含 $r+t$ 个非零列, 因此 $R(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{B}}) \leqslant r+t$, 而 $R(\boldsymbol{A}, \boldsymbol{B})=$ $R(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{B}})$, 故 $R(\boldsymbol{A}, \boldsymbol{B}) \leqslant r+t$, 即

$$
R(\boldsymbol{A}, \boldsymbol{B}) \leqslant R(\boldsymbol{A})+R(\boldsymbol{B}) .
$$

(6) $R(\boldsymbol{A}+\boldsymbol{B}) \leqslant R(\boldsymbol{A})+R(\boldsymbol{B})$.

证 无妨设 $\boldsymbol{A} 、 \boldsymbol{B}$ 为 $m \times n$ 矩阵. 对矩阵 $(\boldsymbol{A}+\boldsymbol{B}, \boldsymbol{B})$ 作列变换 $c_{i}-c_{n+i}(i=$ $1, \cdots, n)$, 即得

$$
(\boldsymbol{A}+\boldsymbol{B}, \boldsymbol{B}) \stackrel{\sim}{\sim}(\boldsymbol{A}, \boldsymbol{B}),
$$

于是 $\quad R(\boldsymbol{A}+\boldsymbol{B}) \leqslant R(\boldsymbol{A}+\boldsymbol{B}, \boldsymbol{B})=R(\boldsymbol{A}, \boldsymbol{B}) \leqslant R(\boldsymbol{A})+R(\boldsymbol{B})$.

后面我们还要介绍两条常用的性质, 现先罗列于下:

(7) $R(\boldsymbol{A B}) \leqslant \min \{R(\boldsymbol{A}), R(\boldsymbol{B})\}$. (见下节定理 7)

(8) 若 $\boldsymbol{A}_{m \times n} \boldsymbol{B}_{n \times l}=\boldsymbol{O}$, 则 $R(\boldsymbol{A})+R(\boldsymbol{B}) \leqslant n$. (见下章例 13)

例 8 设 $\boldsymbol{A}$ 为 $n$ 阶矩阵, 证明 $R(\boldsymbol{A}+\boldsymbol{E})+R(\boldsymbol{A}-\boldsymbol{E}) \geqslant n$.

证 因 $(\boldsymbol{A}+\boldsymbol{E})+(\boldsymbol{E}-\boldsymbol{A})=2 \boldsymbol{E}$, 由性质 6, 有

$$
R(\boldsymbol{A}+\boldsymbol{E})+R(\boldsymbol{E}-\boldsymbol{A}) \geqslant R(2 \boldsymbol{E})=n,
$$

而 $R(\boldsymbol{E}-\boldsymbol{A})=R(\boldsymbol{A}-\boldsymbol{E})$, 所以

$$
R(\boldsymbol{A}+\boldsymbol{E})+R(\boldsymbol{A}-\boldsymbol{E}) \geqslant n .
$$

例 9 证明: 若 $\boldsymbol{A}_{m \times n} \boldsymbol{B}_{n \times l}=\boldsymbol{C}$, 且 $R(\boldsymbol{A})=n$, 则 $R(\boldsymbol{B})=R(\boldsymbol{C})$.

证因 $R(\boldsymbol{A})=n$, 知 $\boldsymbol{A}$ 的行最简形矩阵为 $\left(\begin{array}{c}\boldsymbol{E}_{n} \\ \boldsymbol{O}\end{array}\right)_{m \times n}$, 并有 $m$ 阶可逆矩阵 $P$,使 $P A=\left(\begin{array}{c}E_{n} \\ 0\end{array}\right)$. 于是

$$
P C=P A B=\left(\begin{array}{c}
E_{n} \\
O
\end{array}\right) B=\left(\begin{array}{c}
B \\
o
\end{array}\right) .
$$

由矩阵秩的性质 4 , 知 $R(\boldsymbol{C})=R(\boldsymbol{P C})$, 而 $R\left(\begin{array}{l}\boldsymbol{B} \\ \boldsymbol{O}\end{array}\right)=R(\boldsymbol{B})$, 故

$$
R(\boldsymbol{C})=R(\boldsymbol{B}) \text {. }
$$

本例中的矩阵 $\boldsymbol{A}$ 的秩等于它的列数,这样的矩阵称为列满秩矩阵. 当 $\boldsymbol{A}$ 为方阵时, 列满秩矩阵就成为满秩矩阵, 也就是可逆矩阵. 因此, 本例的结论当 $\boldsymbol{A}$ 为方阵这一特殊情形时就是矩阵秩的性质 4 .

本例另一种重要的特殊情形是 $C=O$, 这时结论为 设 $\boldsymbol{A B}=\boldsymbol{O}$, 若 $\boldsymbol{A}$ 为列满秩矩阵, 则 $\boldsymbol{B}=\boldsymbol{O}$.

这是因为, 按本例的结论, 这时有 $R(\boldsymbol{B})=0$, 故 $\boldsymbol{B}=\boldsymbol{O}$. 这一结论通常称为 矩阵乘法的消去律 .

## $\S 3$ 线性方程组的解

设有 $n$ 个未知数 $m$ 个方程的线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=b_{2}, \\
\cdots \cdots \cdots \cdots \\
a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n}=b_{m},
\end{array}\right.
$$

(3)式可以写成以向量 $x$ 为未知元的向量方程

$$
A \boldsymbol{x}=\boldsymbol{b} \text {, }
$$

第二章中已经说明, 线性方程组 (3) 与向量方程 (4)将混同使用而不加区分, 解与 解向量的名称亦不加区别.

线性方程组 (3) 如果有解, 就称它是相容的, 如果无解, 就称它不相容. 利用 系数矩阵 $\boldsymbol{A}$ 和增广矩阵 $\boldsymbol{B}=(\boldsymbol{A}, \boldsymbol{b})$ 的秩, 可以方便地讨论线性方程组是否有解 (即是否相容) 以及有解时解是否倠一等问题, 其结论是:

定理 $3 n$ 元线性方程组 $\boldsymbol{A x}=\boldsymbol{b}$

(i) 无解的充分必要条件是 $R(\boldsymbol{A})<R(\boldsymbol{A}, \boldsymbol{b})$;

(ii) 有惟一解的充分必要条件是 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{b})=n$;

(iii) 有无限多解的充分必要条件是 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{b})<n$.

证 只需证明条件的充分性,因为 (i), (ii),(iii)中条件的必要性依次是(ii) (iii)，(i)(iii)，(i)(ii)中条件的充分性的逆否命题.

设 $R(\boldsymbol{A})=r$. 为叙述方便, 无妨设 $\boldsymbol{B}=(\boldsymbol{A}, \boldsymbol{b})$ 的行最简形为

$$
\widetilde{\boldsymbol{B}}=\left(\begin{array}{cccccccc}
1 & 0 & \cdots & 0 & b_{11} & \cdots & b_{1, n-r} & d_{1} \\
0 & 1 & \cdots & 0 & b_{21} & \cdots & b_{2, n-r} & d_{2} \\
\vdots & \vdots & & \vdots & \vdots & & \vdots & \vdots \\
0 & 0 & \cdots & 1 & b_{r 1} & \cdots & b_{r, n-r} & d_{r} \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 & d_{r+1} \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 & 0 \\
\vdots & \vdots & & \vdots & \vdots & & \vdots & \vdots \\
0 & 0 & \cdots & 0 & 0 & \cdots & 0 & 0
\end{array}\right) .
$$

(i) 若 $R(\boldsymbol{A})<R(\boldsymbol{B})$, 则 $\widetilde{\boldsymbol{B}}$ 中的 $d_{r+1}=1$, 于是 $\widetilde{\boldsymbol{B}}$ 的第 $r+1$ 行对应矛盾方 程 $0=1$, 故方程 $(4)$ 无解. (ii) 若 $R(\boldsymbol{A})=R(\boldsymbol{B})=r=n$, 则 $\widetilde{\boldsymbol{B}}$ 中的 $d_{r+1}=0$ (或 $d_{r+i}$ 不出现), 且 $b_{i j}$ 都 不出现,于是 $\widetilde{B}$ 对应方程组

$$
\left\{\begin{array}{l}
x_{1}=d_{1}, \\
x_{2}=d_{2}, \\
\cdots \cdots \cdots \\
x_{u}=d_{n},
\end{array}\right.
$$

故方程 (4)有惟一解.

(iii) 若 $R(\boldsymbol{A})=R(\boldsymbol{B})=r<n$, 则 $\tilde{\boldsymbol{B}}$ 中的 $d_{r+1}=0$ (或 $d_{r+1}$ 不出现), $\tilde{\boldsymbol{B}}$ 对应 方程组

$$
\left\{\begin{array}{l}
x_{1}=-b_{11} x_{r+1}-\cdots-b_{1, n-r} x_{n}+d_{1}, \\
x_{2}=-b_{21} x_{r+1}-\cdots-b_{2, n-r} x_{n}+d_{2}, \\
\cdots \cdots \cdots \cdots \\
x_{r}=-b_{r 1} x_{r+1}-\cdots-b_{r, n-r} x_{n}+d_{r},
\end{array}\right.
$$

令自由末知数 $x_{r+1}=c_{1}, \cdots, x_{n}=c_{n-r}$, 即得方程 (4) 的含 $n-r$ 个参数的解

$$
\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{r} \\
x_{r+1} \\
\vdots \\
x_{n}
\end{array}\right)=\left(\begin{array}{c}
-b_{11} c_{1}-\cdots-b_{1, n-r} c_{n-r}+d_{1} \\
\vdots \\
-b_{r 1} c_{1}-\cdots-b_{r, n-r} c_{n-r}+d_{r} \\
c_{1} \\
\vdots \\
c_{n-r}
\end{array}\right),
$$

即

$$
\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{r} \\
x_{r+1} \\
\vdots \\
x_{n}
\end{array}\right)=c_{1}\left(\begin{array}{c}
-b_{11} \\
\vdots \\
-b_{r 1} \\
1 \\
\vdots \\
0
\end{array}\right)+\cdots+c_{n-r}\left(\begin{array}{c}
-b_{1, n-r} \\
\vdots \\
-b_{r, n-r} \\
0 \\
\vdots \\
1
\end{array}\right)+\left(\begin{array}{c}
d_{1} \\
\vdots \\
d_{r} \\
0 \\
\vdots \\
0
\end{array}\right) \text {, }
$$

由于参数 $c_{1}, \cdots, c_{n-r}$ 可任意取值,故方程 (4)有无限多个解.

当 $R(\boldsymbol{A})=R(\boldsymbol{B})=r<n$ 时, 由于含 $n-r$ 个参数的解(6)可表示线性方程 组 (5) 的任一解, 从而也可表示线性方程组 (3) 的任一解, 因此解 (6) 称为线性方 程组 (3) 的通解.

定理 3 的证明过程给出了求解线性方程组的步骤,这个步骤在第一节的引 例中也已显示了出来, 现将它归纳如下:

(i) 对于非齐次线性方程组,把它的增广矩阵 $B$ 化成行阶梯形, 从 $B$ 的行 阶梯形可同时看出 $R(\boldsymbol{A})$ 和 $R(\boldsymbol{B})$. 若 $R(\boldsymbol{A})<R(\boldsymbol{B})$, 则方程组无解. （ii）若 $R(\boldsymbol{A})=R(\boldsymbol{B})$, 则进一步把 $\boldsymbol{B}$ 化成行最简形, 而对于齐欢线性方程 组,则把系数矩阵 $\boldsymbol{A}$ 化成行最简形.

(iii) 设 $R(\boldsymbol{A})=R(\boldsymbol{B})=r$, 把行最简形中 $r$ 个非零行的非零首元所对应的 未知数取作非自由未知数, 其余 $n-r$ 个未知数取作自由末知数, 并令自由末知 数分别等于 $c_{1}, c_{2}, \cdots, c_{n-r}$, 由 $\boldsymbol{B}$ (或 $\boldsymbol{A}$ ) 的行最简形, 即可写出含 $n-r$ 个参数 的通解.

例 10 求解齐次线性方程组

$$
\left\{\begin{array}{r}
x_{1}+2 x_{2}+2 x_{3}+x_{4}=0, \\
2 x_{1}+x_{2}-2 x_{3}-2 x_{4}=0, \\
x_{1}-x_{2}-4 x_{3}-3 x_{4}=0 .
\end{array}\right.
$$

解 对系数矩阵 $\boldsymbol{A}$ 施行初等行变换变为行最简形矩阵

$$
\begin{gathered}
\boldsymbol{A}=\left(\begin{array}{rrrr}
1 & 2 & 2 & 1 \\
2 & 1 & -2 & -2 \\
1 & -1 & -4 & -3
\end{array}\right) \frac{r_{2}-2 r_{1}}{r_{3}-r_{1}}\left(\begin{array}{rrrr}
1 & 2 & 2 & 1 \\
0 & -3 & -6 & -4 \\
0 & -3 & -6 & -4
\end{array}\right) \\
\underset{r_{2} \div(-3)}{\frac{r_{3}-r_{2}}{\div(-3}}\left(\begin{array}{llll}
1 & 2 & 2 & 1 \\
0 & 1 & 2 & \frac{4}{3} \\
0 & 0 & 0 & 0
\end{array}\right) \stackrel{r_{1}-2 r_{2}}{=}\left(\begin{array}{rrrr}
1 & 0 & -2 & -\frac{5}{3} \\
0 & 1 & 2 & \frac{4}{3} \\
0 & 0 & 0 & 0
\end{array}\right),
\end{gathered}
$$

即得与原方程组同解的方程组

$$
\left\{\begin{array}{l}
x_{1}-2 x_{3}-\frac{5}{3} x_{4}=0, \\
x_{2}+2 x_{3}+\frac{4}{3} x_{4}=0,
\end{array}\right.
$$

由此即得

$$
\left\{\begin{array}{l}
x_{1}=2 x_{3}+\frac{5}{3} x_{4}, \\
x_{2}=-2 x_{3}-\frac{4}{3} x_{4}
\end{array}\left(x_{3}, x_{4} \text { 可任意取值 }\right) .\right.
$$

令 $x_{3}=c_{1}, x_{4}=c_{2}$, 把它写成通常的参数形式

$$
\left\{\begin{array}{l}
x_{1}=2 c_{1}+\frac{5}{3} c_{2}, \\
x_{2}=-2 c_{1}-\frac{4}{3} c_{2}, \\
x_{3}=c_{1}, \\
x_{4}=c_{2},
\end{array}\right.
$$

其中 $c_{1}, c_{2}$ 为任意实数,或写成向量形式

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=\left(\begin{array}{c}
2 c_{1}+\frac{5}{3} c_{2} \\
-2 c_{1}-\frac{4}{3} c_{2} \\
c_{1} \\
c_{2}
\end{array}\right)=c_{1}\left(\begin{array}{r}
2 \\
-2 \\
1 \\
0
\end{array}\right)+c_{2}\left(\begin{array}{r}
\frac{5}{3} \\
-\frac{4}{3} \\
0 \\
1
\end{array}\right) .
$$

例 11 求解非齐次线性方程组

$$
\left\{\begin{array}{l}
x_{1}-2 x_{2}+3 x_{3}-x_{4}=1, \\
3 x_{1}-x_{2}+5 x_{3}-3 x_{4}=2, \\
2 x_{1}+x_{2}+2 x_{3}-2 x_{4}=3 .
\end{array}\right.
$$

解 对增广矩阵 $\boldsymbol{B}$ 施行初等行变换

$$
\begin{gathered}
\boldsymbol{B}=\left(\begin{array}{rrrrr}
1 & -2 & 3 & -1 & 1 \\
3 & -1 & 5 & -3 & 2 \\
2 & 1 & 2 & -2 & 3
\end{array}\right) \\
\underset{r_{3}-2 r_{1}}{r_{2}-3 r_{1}}\left(\begin{array}{rrrrr}
1 & -2 & 3 & -1 & 1 \\
0 & 5 & -4 & 0 & -1 \\
0 & 5 & -4 & 0 & 1
\end{array}\right) \\
\stackrel{r_{3}-r_{2}}{=}\left(\begin{array}{rrrrr}
1 & -2 & 3 & -1 & 1 \\
0 & 5 & -4 & 0 & -1 \\
0 & 0 & 0 & 0 & 2
\end{array}\right),
\end{gathered}
$$

可见 $R(\boldsymbol{A})=2, R(\boldsymbol{B})=3$, 故方程组无解.

例 12 求解非齐次线性方程组

$$
\begin{gathered}
\left\{\begin{array}{r}
x_{1}+x_{2}-3 x_{3}-x_{4}=1, \\
3 x_{1}-x_{2}-3 x_{3}+4 x_{4}=4, \\
x_{1}+5 x_{2}-9 x_{3}-8 x_{4}=0
\end{array}\right. \\
\boldsymbol{B}=\left(\begin{array}{rrrrr}
1 & 1 & -3 & -1 & 1 \\
3 & -1 & -3 & 4 & 4 \\
1 & 5 & -9 & -8 & 0
\end{array}\right) . \\
\frac{r_{2}-3 r_{1}}{r_{3}-r_{1}}\left(\begin{array}{rrrrr}
1 & 1 & -3 & -1 & 1 \\
0 & -4 & 6 & 7 & 1 \\
0 & 4 & -6 & -7 & -1
\end{array}\right)
\end{gathered}
$$

$$
\begin{aligned}
& \frac{r_{3}+r_{2}}{r_{2}+(-4)}\left(\begin{array}{rrrrr}
1 & 1 & -3 & -1 & 1 \\
0 & 1 & -\frac{3}{2} & -\frac{7}{4} & -\frac{1}{4} \\
0 & 0 & 0 & 0 & 0
\end{array}\right) \\
& \stackrel{r_{1}-r_{2}}{r_{1}}\left(\begin{array}{rrrrr}
0 & -\frac{3}{2} & \frac{3}{4} & \frac{5}{4} \\
0 & 1 & -\frac{3}{2} & -\frac{7}{4} & -\frac{1}{4} \\
0 & 0 & 0 & 0 & 0
\end{array}\right), \\
& \left\{\begin{array}{l}
x_{1}=\frac{3}{2} x_{3}-\frac{3}{4} x_{4}+\frac{5}{4}, \\
x_{2}=\frac{3}{2} x_{3}+\frac{7}{4} x_{4}-\frac{1}{4}, \\
x_{3}=x_{3}, \\
x_{4}=x_{4},
\end{array}\right.
\end{aligned}
$$

例 13 设有线性方程组

$$
\left\{\begin{aligned}
(1+\lambda) x_{1}+x_{2}+x_{3} & =0, \\
x_{1}+(1+\lambda) x_{2}+x_{3} & =3, \\
x_{1}+x_{2}+(1+\lambda) x_{3} & =\lambda,
\end{aligned}\right.
$$

问 $\lambda$ 取何值时,此方程组 (1) 有惟一解; (2) 无解; (3) 有无限多个解? 并在有无 限多解时求其通解.

解法 1 对增广矩阵 $\boldsymbol{B}=(\boldsymbol{A}, \boldsymbol{b})$ 作初等行变换把它变为行阶梯形矩阵,有

$$
\begin{aligned}
& \frac{r_{2}-r_{1}}{r_{3}-(1+\lambda) r_{1}}\left(\begin{array}{cccc}
1 & 1 & 1+\lambda & \lambda \\
0 & \lambda & -\lambda & 3-\lambda \\
0 & -\lambda & -\lambda(2+\lambda) & -\lambda(1+\lambda)
\end{array}\right) \\
& \stackrel{r_{3}+r_{2}}{\sim}\left(\begin{array}{cccc}
1 & 1 & 1+\lambda & \lambda \\
0 & \lambda & -\lambda & 3-\lambda \\
0 & 0 & -\lambda(3+\lambda) & (1-\lambda)(3+\lambda)
\end{array}\right) \text {. }
\end{aligned}
$$

www.TopSage.com (1) 当 $\lambda \neq 0$ 且 $\lambda \neq-3$ 时, $R(\boldsymbol{A})=R(\boldsymbol{B})=3$, 方程组有惟一解;

（2）当 $\lambda=0$ 时, $R(\boldsymbol{A})=1, R(\boldsymbol{B})=2$,方程组无解;

(3) 当 $\lambda=-3$ 时, $R(\boldsymbol{A})=R(\boldsymbol{B})=2$, 方程组有无限多个解. 这时

$$
\begin{aligned}
\boldsymbol{B} & \sim\left(\begin{array}{rrrr}
1 & 1 & -2 & -3 \\
0 & -3 & 3 & 6 \\
0 & 0 & 0 & 0
\end{array}\right) \\
& \sim\left(\begin{array}{rrrr}
1 & 0 & -1 & -1 \\
0 & 1 & -1 & -2 \\
0 & 0 & 0 & 0
\end{array}\right),
\end{aligned}
$$

由此便得通解

即

$$
\begin{aligned}
& \left\{\begin{array}{l}
x_{1}=x_{3}-1, \\
x_{2}=x_{3}-2
\end{array}\left(x_{3} \text { 可任意取值 }\right),\right. \\
& \left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right)=c\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right)+\left(\begin{array}{r}
-1 \\
-2 \\
0
\end{array}\right)(c \in \mathbb{R}) .
\end{aligned}
$$

解法 2 因系数矩阵 $\boldsymbol{A}$ 为方阵,故方程有惟一解的充分必要条件是系数行 列式 $|\boldsymbol{A}| \neq 0$. 而

$$
\begin{aligned}
|\boldsymbol{A}| & =\left|\begin{array}{ccc}
1+\lambda & 1 & 1 \\
1 & 1+\lambda & 1 \\
1 & 1 & 1+\lambda
\end{array}\right|=(3+\lambda)\left|\begin{array}{ccc}
1 & 1 & 1 \\
1 & 1+\lambda & 1 \\
1 & 1 & 1+\lambda
\end{array}\right|=(3+\lambda)\left|\begin{array}{lll}
1 & 1 & 1 \\
0 & \lambda & 0 \\
0 & 0 & \lambda
\end{array}\right| \\
& =(3+\lambda) \lambda^{2},
\end{aligned}
$$

因此, 当 $\lambda \neq 0$ 且 $\lambda \neq-3$ 时, 方程组有惟一解.

当 $\lambda=0$ 时

$$
\boldsymbol{B}=\left(\begin{array}{llll}
1 & 1 & 1 & 0 \\
1 & 1 & 1 & 3 \\
1 & 1 & 1 & 0
\end{array}\right) \sim\left(\begin{array}{llll}
1 & 1 & 1 & 0 \\
0 & 0 & 0 & 1 \\
0 & 0 & 0 & 0
\end{array}\right),
$$

知 $R(A)=1, R(B)=2$, 故方程组无解.

当 $\lambda=-3$ 时

$$
\mathbf{B}=\left(\begin{array}{rrrr}
-2 & 1 & 1 & 0 \\
1 & -2 & 1 & 3 \\
1 & 1 & -2 & -3
\end{array}\right) \stackrel{r}{\sim}\left(\begin{array}{rrrr}
1 & 0 & -1 & -1 \\
0 & 1 & -1 & -2 \\
0 & 0 & 0 & 0
\end{array}\right),
$$

知 $R(A)=R(B)=2$, 故方程组有无限多个解, 且通解为

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right)=c\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right)+\left(\begin{array}{r}
-1 \\
-2 \\
0
\end{array}\right)(c \in \mathbb{R}) .
$$

比较解法 1 与解法 2 , 显见解法 2 较简单. 但解法 2 的方法只适用于系数矩 阵为方阵的情形.

对含参数的矩阵作初等变换时, 例如在本例中对矩阵 B 作初等变换时, 由 于 $\lambda+1, \lambda+3$ 等因式可以等于 0 , 故不宜做诸如 $r_{2}-\frac{1}{\lambda+1} r_{1}, r_{2} \times(\lambda+1)$, $r_{3} \div(\lambda+3)$ 这样的变换. 如果作了这种变换, 则需对 $\lambda+1=0$ (或 $\lambda+3=0$ ) 的情 形另作讨论. 因此,对含参数的矩阵作初等变换较不方便.

由定理 3 容易得出线性方程组理论中两个最基本的定理,这就是

定理 $4 n$ 元齐次线性方程组 $\boldsymbol{A x}=0$ 有非零解的充分必要条件是 $R(\boldsymbol{A})<n$.

定理 5 线性方程组 $\boldsymbol{A x}=\boldsymbol{b}$ 有解的充分必要条件是 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{b})$.

显然,定理 4 是定理 3(iii) 的特殊情形,而定理 5 就是定理 3(i).

为了下一章论述的需要,下面把定理 5 推广到矩阵方程.

定理 6 矩阵方程 $A X=B$ 有解的充分必要条件是 $R(A)=R(A, B)$.

证 设 $\boldsymbol{A}$ 为 $m \times n$ 矩阵, $\boldsymbol{B}$ 为 $m \times l$ 矩阵,则 $\boldsymbol{X}$ 为 $n \times l$ 矩阵. 把 $\boldsymbol{X}$ 和 $\boldsymbol{B}$ 按 列分块, 记为

$$
X=\left(x_{1}, x_{2}, \cdots, x_{l}\right), B=\left(b_{1}, b_{2}, \cdots, b_{l}\right),
$$

则矩阵方程 $\boldsymbol{A X}=\boldsymbol{B}$ 等价于 $l$ 个向量方程

$$
\boldsymbol{A x} \boldsymbol{x}_{i}=\boldsymbol{b}_{i}(i=1,2, \cdots, l) \text {. }
$$

又, 设 $R(\boldsymbol{A})=r$, 且 $\boldsymbol{A}$ 的行最简形为 $\tilde{\boldsymbol{A}}$, 则 $\tilde{\boldsymbol{A}}$ 有 $r$ 个非零行, 且 $\tilde{\boldsymbol{A}}$ 的后 $m-r$ 行全为零行 . 再设

$$
(\boldsymbol{A}, \boldsymbol{B})=\left(\boldsymbol{A}, \boldsymbol{b}_{1}, \boldsymbol{b}_{2}, \cdots, \boldsymbol{b}_{1}\right) \stackrel{r}{\sim}\left(\tilde{\boldsymbol{A}}, \tilde{b}_{1}, \bar{b}_{2}, \cdots, \tilde{b}_{1}\right),
$$

从而

$$
\left(\boldsymbol{A}, \boldsymbol{b}_{i}\right) \stackrel{r}{\sim}\left(\tilde{\boldsymbol{A}}, \tilde{\boldsymbol{b}}_{i}\right)(i=1,2, \cdots, l) .
$$

由上述讨论并依据定理 5, 可得

$$
\begin{aligned}
\boldsymbol{A} \boldsymbol{X}=\boldsymbol{B} \text { 有解 } & \Leftrightarrow \boldsymbol{A} \boldsymbol{x}_{i}=\boldsymbol{b}_{i} \text { 有解 }(i=1,2, \cdots, l) \\
& \Leftrightarrow R\left(\boldsymbol{A}, \boldsymbol{b}_{i}\right)=R(\boldsymbol{A})(i=1,2, \cdots, l) \\
& \Leftrightarrow \tilde{\boldsymbol{b}}_{i} \text { 的后 } m-r \text { 个元全为零 }(i=1,2, \cdots, l) \\
& \Leftrightarrow\left(\tilde{\boldsymbol{b}}_{1}, \tilde{\boldsymbol{b}}_{2}, \cdots, \tilde{\boldsymbol{b}}_{l}\right) \text { 的后 } m-r \text { 行全为零行 } \\
& \Leftrightarrow R(\boldsymbol{A}, \boldsymbol{B})=r=R(\boldsymbol{A}) .
\end{aligned}
$$

利用定理 6 , 容易得出矩阵的的性质 7, 即

定理 7 设 $\boldsymbol{A B}=\boldsymbol{C}$, 则 $R(\boldsymbol{C}) \leqslant \min \{R(\boldsymbol{A}), R(\boldsymbol{B})\}$. 证 因 $\boldsymbol{A B}=\boldsymbol{C}$, 知矩阵方程 $\boldsymbol{A X}=\boldsymbol{C}$ 有解 $\boldsymbol{X}=\boldsymbol{B}$, 于是据定理 6 有 $R\left(\boldsymbol{A}_{\boldsymbol{*}}\right)=$ $R(\boldsymbol{A}, \boldsymbol{C})$. 而 $R(\boldsymbol{C}) \leqslant R(\boldsymbol{A}, \boldsymbol{C})$, 因此 $R(\boldsymbol{C}) \leqslant R(\boldsymbol{A})$.

又 $\boldsymbol{B}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}=\boldsymbol{C}^{\mathrm{T}}$, 由上段证明知有 $R\left(\boldsymbol{C}^{\mathrm{T}}\right) \leqslant R\left(\boldsymbol{B}^{\mathrm{T}}\right)$, 即 $R(\boldsymbol{C}) \leqslant R(\boldsymbol{B})$.

综合便得 $R(\boldsymbol{C}) \leqslant \min \{R(\boldsymbol{A}), R(\boldsymbol{B})\}$.

定理 6 和 7 的应用,我们在下一章中讨论.

## 习 题 三

1. 用初等行变换把下列矩阵化为行最简形矩阵:
(1) $\left(\begin{array}{rrrr}1 & 0 & 2 & -1 \\ 2 & 0 & 3 & 1 \\ 3 & 0 & 4 & 3\end{array}\right)$;
(2) $\left(\begin{array}{rrrr}0 & 2 & -3 & 1 \\ 0 & 3 & -4 & 3 \\ 0 & 4 & -7 & -1\end{array}\right)$;
(3) $\left(\begin{array}{rrrrr}1 & -1 & 3 & -4 & 3 \\ 3 & -3 & 5 & -4 & 1 \\ 2 & -2 & 3 & -2 & 0 \\ 3 & -3 & 4 & -2 & -1\end{array}\right)$;
(4) $\left(\begin{array}{rrrrr}2 & 3 & 1 & -3 & -7 \\ 1 & 2 & 0 & -2 & -4 \\ 3 & -2 & 8 & 3 & 0 \\ 2 & -3 & 7 & 4 & 3\end{array}\right)$.
2. 设 $\boldsymbol{A}=\left(\begin{array}{llll}1 & 2 & 3 & 4 \\ 2 & 3 & 4 & 5 \\ 5 & 4 & 3 & 2\end{array}\right)$, 求一个可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P A}$ 为行最简形 .
3. 设 $A=\left(\begin{array}{rrr}-5 & 3 & 1 \\ 2 & -1 & 1\end{array}\right)$,

(1) 求可逆矩阵 $\boldsymbol{P}$,使 $\boldsymbol{P A}$ 为行最简形;

(2) 求一个可逆矩阵 $Q$, 使 $Q A^{\top}$ 为行最简形.

4. 试利用矩阵的初等变换,求下列方阵的逆阵:
(1) $\left(\begin{array}{lll}3 & 2 & 1 \\ 3 & 1 & 5 \\ 3 & 2 & 3\end{array}\right)$;
(2) $\left(\begin{array}{rrrr}3 & -2 & 0 & -1 \\ 0 & 2 & 2 & 1 \\ 1 & -2 & -3 & -2 \\ 0 & 1 & 2 & 1\end{array}\right)$.
5. (1) 设 $A=\left(\begin{array}{rrr}4 & 1 & -2 \\ 2 & 2 & 1 \\ 3 & 1 & -1\end{array}\right), B=\left(\begin{array}{rr}1 & -3 \\ 2 & 2 \\ 3 & -1\end{array}\right)$, 求 $\boldsymbol{X}$ 使 $\boldsymbol{A X}=\boldsymbol{B}$;

（2）设 $A=\left(\begin{array}{rrr}0 & 2 & 1 \\ 2 & -1 & 3 \\ -3 & 3 & -4\end{array}\right), B=\left(\begin{array}{rrr}1 & 2 & 3 \\ 2 & -3 & 1\end{array}\right)$, 求 $X$ 使 $X A=B$.

6. 设 $A=\left(\begin{array}{rrr}1 & -1 & 0 \\ 0 & 1 & -1 \\ -1 & 0 & 1\end{array}\right), A X=2 X+A$, 求 $X$.
7. 在秩是 $r$ 的矩阵中, 有没有等于 0 的 $r-1$ 阶子式? 有没有等于 0 的 $r$ 阶子式? 8. 从矩阵 $\boldsymbol{A}$ 中划去一行得到矩阵 $\boldsymbol{B}$, 问 $\boldsymbol{A}, \boldsymbol{B}$ 的秩的关系怎样?
8. 求作一个秩是 4 的方阵, 它的两个行向量是

$$
(1,0,1,0,0),(1,-1,0,0,0) \text {. }
$$

10. 求下列矩阵的秩, 并求一个暇高阶非零子式:
(1) $\left(\begin{array}{rrrr}3 & 1 & 0 & 2 \\ 1 & -1 & 2 & -1 \\ 1 & 3 & -4 & 4\end{array}\right)$;
(2) $\left(\begin{array}{rrrrr}3 & 2 & -1 & -3 & -1 \\ 2 & -1 & 3 & 1 & -3 \\ 7 & 0 & 5 & -1 & -8\end{array}\right)$;
(3) $\left(\begin{array}{rrrrr}2 & 1 & 8 & 3 & 7 \\ 2 & -3 & 0 & 7 & -5 \\ 3 & -2 & 5 & 8 & 0 \\ 1 & 0 & 3 & 2 & 0\end{array}\right)$.
11. 设 $\boldsymbol{A}, \boldsymbol{B}$ 都是 $m \times n$ 矩阵, 证明 $\boldsymbol{A} \sim \boldsymbol{B}$ 的充分必要条件是 $R(\boldsymbol{A})=R(\boldsymbol{B})$.
12. 设

$$
\boldsymbol{A}=\left(\begin{array}{rrr}
1 & -2 & 3 k \\
-1 & 2 k & -3 \\
k & -2 & 3
\end{array}\right),
$$

问 $k$ 为何值, 可使
(1) $R(\boldsymbol{A})=1$;
(2) $R(\boldsymbol{A})=2$;
(3) $R(A)=3$.

13. 求解下列齐次线性方程组:
(1) $\left\{\begin{aligned} x_{1}+x_{2}+2 x_{3}-x_{4} & =0, \\ 2 x_{1}+x_{2}+x_{3}-x_{4} & =0, \\ 2 x_{1}+2 x_{2}+x_{3}+2 x_{4} & =0 ;\end{aligned}\right.$
(2) $\left\{\begin{array}{r}x_{1}+2 x_{2}+x_{3}-x_{4}=0, \\ 3 x_{1}+6 x_{2}-x_{3}-3 x_{4}=0, \\ 5 x_{1}+10 x_{2}+x_{3}-5 x_{4}=0 ;\end{array}\right.$
(3) $\left\{\begin{array}{l}2 x_{1}+3 x_{2}-x_{3}-7 x_{4}=0, \\ 3 x_{1}+x_{2}+2 x_{3}-7 x_{4}=0, \\ 4 x_{1}+x_{2}-3 x_{3}+6 x_{4}=0, \\ x_{1}-2 x_{2}+5 x_{3}-5 x_{4}=0 ;\end{array}\right.$
(4) $\left\{\begin{array}{l}3 x_{1}+4 x_{2}-5 x_{3}+7 x_{4}=0, \\ 2 x_{1}-3 x_{2}+3 x_{3}-2 x_{4}=0, \\ 4 x_{1}+11 x_{2}-13 x_{3}+16 x_{4}=0, \\ 7 x_{1}-2 x_{2}+x_{3}+3 x_{4}=0 .\end{array}\right.$
14. 求解下列非齐次线性方程组:
(1) $\left\{\begin{aligned} 4 x_{1}+2 x_{2}-x_{3} & =2, \\ 3 x_{1}-x_{2}+2 x_{3} & =10, \\ 11 x_{1}+3 x_{2} & =8 ;\end{aligned}\right.$
(2) $\left\{\begin{aligned} 2 x+3 y+z & =4, \\ x-2 y+4 z & =-5, \\ 3 x+8 y-2 z & =13, \\ 4 x-y+9 z & =-6 ;\end{aligned}\right.$
(3) $\left\{\begin{array}{l}2 x+y-z+w=1, \\ 4 x+2 y-2 z+w=2, \\ 2 x+y-z-w=1\end{array}\right.$
(4) $\left\{\begin{aligned} 2 x+y-z+w & =1, \\ 3 x-2 y+z-3 w & =4, \\ x+4 y-3 z+5 w & =-2 .\end{aligned}\right.$
15. 写出一个以

$$
x=c_{1}\left(\begin{array}{r}
2 \\
-3 \\
1 \\
0
\end{array}\right)+c_{2}\left(\begin{array}{r}
-2 \\
4 \\
0 \\
1
\end{array}\right)
$$

- 为通解的齐次线性方程组.

16. $\lambda$ 取何值时, 非齐次线性方程组

$$
\left\{\begin{aligned}
\lambda x_{1}+x_{2}+x_{3} & =1 \\
x_{1}+\lambda x_{2}+x_{3} & =\lambda \\
x_{1}+x_{2}+\lambda x_{3} & =\lambda^{2}
\end{aligned}\right.
$$

（1）有倠一解; (2) 无解; (3) 有无穷多个解?

17. 非齐次线性方程组

$$
\left\{\begin{aligned}
-2 x_{1}+x_{2}+x_{3} & =-2 \\
x_{1}-2 x_{2}+x_{3} & =\lambda \\
x_{1}+x_{2}-2 x_{3} & =\lambda^{2}
\end{aligned}\right.
$$

当 $\lambda$ 取何值时有解? 并求出它的通解.

18. 设 $\left\{\begin{array}{crr}(2-\lambda) x_{1}+2 x_{2}-2 x_{3}= & 1, \\ 2 x_{1}+(5-\lambda) x_{2}-4 x_{3}= & 2, \\ -2 x_{1}-4 x_{2}+(5-\lambda) x_{3}= & -\lambda-1,\end{array}\right.$

问 $\lambda$ 为何值时,此方程组有倠一解、无解或有无穷多解? 并在有无穷多解时求其通解.

19. 证明 $R(A)=1$ 的充分必要条件是存在非零列向圤 $a$ 及非零行向䅉 $b^{T}$, 使 $A=a b^{T}$.
20. 设 $A$ 为列满矩阵, $A B=C$, 证明线性方程 $B x=0$ 与 $C x=0$ 同解.
21. 设 $A$ 为 $m \times n$ 矩阵, 证明

方程 $\boldsymbol{A X}=\boldsymbol{E}_{m}$ 有解的充分必要条件是 $R(\boldsymbol{A})=m$.

## 第四章

## 向量组的线性相关性

## $\S 1$ 向量组及其线性组合

第二章中我们已经介绍过向量的概念, 现再叙述如下.

定义 $1 n$ 个有次序的数 $a_{1}, a_{2}, \cdots, a_{n}$ 所组成的数组称为 $n$ 维向量,这 $n$ 个数称为该向量的 $n$ 个分量,第 $i$ 个数 $a_{i}$ 称为第 $i$ 个分量.

分量全为实数的向量称为实向量, 分量为复数的向量称为复向量. 本书中除 特别指明者外,一般只讨论实向量.

$n$ 维向量可写成一行, 也可写成一列. 按第二章中的规定, 分别称为行向量 和列向量, 也就是行矩阵和列矩阵, 并规定行向量与列向量都按矩阵的运算规则 进行运算. 因此, $n$ 维列向量

与 $n$ 维行向量

$$
a=\left(\begin{array}{c}
a_{1} \\
a_{2} \\
\vdots \\
a_{n}
\end{array}\right)
$$

$$
\boldsymbol{a}^{\mathrm{T}}=\left(a_{1}, a_{2}, \cdots, a_{n}\right)
$$

总看做是两个不同的向量 (按定义 $1, a$ 与 $\boldsymbol{a}^{\mathrm{T}}$ 应是同一个向量).

本书中,列向量用黑体小写字母 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{\alpha}, \boldsymbol{\beta}$ 等表示,行向量则用 $\boldsymbol{a}^{\mathrm{T}}, \boldsymbol{b}^{\mathrm{T}}, \boldsymbol{\alpha}^{\mathrm{T}}$, $\boldsymbol{\beta}^{\mathrm{T}}$ 等表示. 所讨论的向量在没有指明是行向量还是列向量时,都当作列向量.

在解析几何中, 我们把 “既有大小又有方向的量” 叫做向量, 并把可随意平行 移动的有向线段作为向量的几何形象. 在引进坐标系以后, 这种向量就有了坐标 表示式一三个有次序的实数, 也就是本书中的 3 维向量. 因此, 当 $n \leqslant 3$ 时, $n$ 维向量可以把有向线段作为几何形象, 但当 $n>3$ 时, $n$ 维向量就不再有这种几 何形象, 只是沿用一些几何术语罢了.

几何中, “空间”通常是作为点的集合, 即作为“空间” 的元素是点, 这样的空 间叫做点空间. 我们把 3 维向展的全体所组成的集合

$$
\mathbb{R}^{3}=\left\{r=(x, y, z)^{\mathrm{T}} \mid x, y, z \in \mathbb{R}\right\}
$$

www.TopSage.com 叫做三维向量空间.在点空间取定坐标系以后,空间中的点 $P(x, y, z)$ 与 3 维问 量 $\boldsymbol{r}=(x, y, z)^{\mathrm{T}}$ 之间有一一对应的关系, 因此, 向量空间可以类比为取定了坐 标系的点空间.在讨论向量的运算时,我们把向量看作有向线段; 在讨论向量集 时,则把向量 $\boldsymbol{r}$ 看作以 $\boldsymbol{r}$ 为向径的点 $P$, 从而把点 $P$ 的轨迹作为向量集的图形. 例如点集

$$
I=\{P(x, y, z) \mid a x+b y+c z=d\}
$$

是一个平面 $(a, b, c$ 不全为 0$)$, 于是向量集

$$
\left\{\boldsymbol{r}=(x, y, z)^{\mathrm{T}} \mid a x+b y+c z=d\right\}
$$

也叫做向量空间 $\mathbb{R}^{3}$ 中的平面,并把 $\Pi$ 作为它的图形.

类似地, $n$ 维向量的全体所组成的集合

$$
\mathbb{R}^{n}=\left\{\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

叫做 $n$ 维向量空间. $n$ 维向量的集合

$$
\left\{\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid a_{1} x_{1}+a_{2} x_{2}+\cdots+a_{n} x_{n}=b\right\}
$$

叫做 $n$ 维向量空间 $\mathbb{R}^{n}$ 中的 $n-1$ 维超平面.

若干个同维数的列向量(或同维数的行向量)所组成的集合叫做向墨组.例 如一个 $m \times n$ 矩阵的全体列向量是一个含 $n$ 个 $m$ 维列向量的向量组,它的全体 行向量是一个含 $m$ 个 $n$ 维行向量的向量组. 又如线性方程 $A_{m \times n} x=0$ 的全体解 当 $R(\boldsymbol{A})<n$ 时是一个含无限多个 $n$ 维列向量的向量组.

下面我们先讨论只含有限个向量的向量组, 以后再把讨论的结果推广到含 无限多个向量的向量组.

矩阵的列向量组和行向量组都是只含有限个向量的向墨组; 反之, 一个含有 限个向量的向量组总可以构成一个矩阵. 例如

$m$ 个 $n$ 维列向量所组成的向墨组 $A: \boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{m}$ 构成一个 $n \times m$ 矩阵

$$
A=\left(a_{1}, a_{2}, \cdots, a_{m}\right) ;
$$

$m$ 个 $n$ 维行向量所组成的向量组 $B: \boldsymbol{\beta}_{1}^{\mathrm{T}}, \boldsymbol{\beta}_{2}^{\mathrm{T}}, \cdots, \boldsymbol{\beta}_{m}^{\mathrm{T}}$, 构成一个 $m \times n$ 矩阵

$$
\boldsymbol{B}=\left(\begin{array}{c}
\boldsymbol{\beta}_{1}^{\mathrm{T}} \\
\boldsymbol{\beta}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\beta}_{m}^{\mathrm{T}}
\end{array}\right) .
$$

总之,含有限个向量的有序向量组可以与矩阵一一对应.

定义 2 给定向墨组 $A: a_{1}, a_{2}, \cdots, a_{m}$, 对于任何一组实数 $k_{1}, k_{2}, \cdots, k_{m}$, 表达式

$$
k_{1} a_{1}+k_{2} a_{2}+\cdots+k_{m} a_{m}
$$

称为向量组 $A$ 的一个线性组合, $k_{1}, k_{2}, \cdots, \dot{k}_{m}$ 称为这个线性组合的系数. 给定向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 和向量 $b$,如果存在一组数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$, 使

$$
b=\lambda_{1} a_{1}+\lambda_{2} a_{2}+\cdots+\lambda_{m} a_{m},
$$

则向量 $\boldsymbol{b}$ 是向量组 $A$ 的线性组合,这时称向量 $\boldsymbol{b}$ 熊由向量组 $A$ 线性表示.

向量 $\boldsymbol{b}$ 能由向量组 $A$ 线性表示, 也就是方程组

$$
x_{1} a_{1}+x_{2} a_{2}+\cdots+x_{m} a_{m}=b
$$

有解. 由上章定理 5 , 立即可得

定理 1 向量 $b$ 能由向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性表示的充分必要条件是 矩阵 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 的秩等于矩阵 $B=\left(a_{1}, a_{2}, \cdots, a_{m}, b\right)$ 的秩.

定义 3 设有两个向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 及 $B: b_{1}, b_{2}, \cdots, b_{l}$, 若 $B$ 组中的 每个向量都能由向量组 $A$ 线性表示, 则称向墨组 $B$ 能由向墨组 $A$ 线性表示. 若 向嗮组 $A$ 与向量组 $B$ 能相互线性表示,则称这两个向黨组等价.

把向量组 $A$ 和 $B$ 所构成的矩阵依次记作 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 和 $B=\left(b_{1}\right.$, $\left.\boldsymbol{b}_{2}, \cdots, \boldsymbol{b}_{l}\right), B$ 组能由 $A$ 组线性表示, 即对每个向量 $\boldsymbol{b}_{j}(j=1,2, \cdots, l)$ 存在数 $k_{1 j}, k_{2 j}, \cdots, k_{m j}$, 使

$$
\boldsymbol{b}_{j}=k_{1 j} \boldsymbol{a}_{1}+k_{2 j} \boldsymbol{a}_{2}+\cdots+k_{m j} \boldsymbol{a}_{m}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{m}\right)\left(\begin{array}{c}
k_{1 j} \\
k_{2 j} \\
\vdots \\
k_{m j}
\end{array}\right),
$$

从而

$$
\left(\boldsymbol{b}_{1}, \boldsymbol{b}_{2}, \cdots, \boldsymbol{b}_{l}\right)=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{m}\right)\left(\begin{array}{cccc}
k_{11} & k_{12} & \cdots & k_{1 l} \\
k_{21} & k_{22} & \cdots & k_{2 l} \\
\vdots & \vdots & & \vdots \\
k_{m 1} & k_{m 2} & \cdots & k_{m t}
\end{array}\right) .
$$

这里,矩阵 $\boldsymbol{K}_{m \times l}=\left(k_{i j}\right)$ 称为这一线性表示的系数矩阵.

由此可知,若 $\boldsymbol{C}_{m \times n}=\boldsymbol{A}_{m \times l} \boldsymbol{B}_{l \times n}$, 则矩阵 $\boldsymbol{C}$ 的列向墨组能由矩阵 $\boldsymbol{A}$ 的列向 量组线性表示, $B$ 为这一表示的系数矩阵:

$$
\left(c_{1}, c_{2}, \cdots, c_{n}\right)=\left(a_{1}, a_{2}, \cdots, a_{l}\right)\left(\begin{array}{cccc}
b_{11} & b_{12} & \cdots & b_{1 n} \\
b_{21} & b_{22} & \cdots & b_{2 n} \\
\vdots & \vdots & & \vdots \\
b_{l 1} & b_{l 2} & \cdots & b_{l n}
\end{array}\right) ;
$$

同时, $\boldsymbol{C}$ 的行向量组能由 $\boldsymbol{B}$ 的行向量组线性表示, $\boldsymbol{A}$ 为这一表示的系数矩阵:

$$
\left(\begin{array}{c}
\boldsymbol{\gamma}_{1}^{\mathrm{T}} \\
\boldsymbol{\gamma}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\gamma}_{m}^{\mathrm{T}}
\end{array}\right)=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 l} \\
a_{21} & a_{22} & \cdots & a_{2 l} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m l}
\end{array}\right)\left(\begin{array}{c}
\boldsymbol{\beta}_{1}^{\mathrm{T}} \\
\boldsymbol{\beta}_{2}^{\mathrm{T}} \\
\vdots \\
\boldsymbol{\beta}_{l}^{\mathrm{T}}
\end{array}\right) \text {. }
$$

设矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 行等价, 即矩阵 $\boldsymbol{A}$ 经初等行变换变成矩阵 $\boldsymbol{B}$, 则 $\boldsymbol{B}$ 的每个行 向量都是 $A$ 的行向量组的线性组合, 即 $B$ 的行向量组能由 $A$ 的行向量组线性 表示. 由于初等变换可逆,知矩阵 $\boldsymbol{B}$ 亦可经初等行变换变为 $\boldsymbol{A}$, 从而 $\boldsymbol{A}$ 的行向量 组也能由 $B$ 的行向量组线性表示. 于是 $\boldsymbol{A}$ 的行向量组与 $\boldsymbol{B}$ 的行向量组等价.

类似可知,若矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 列等价,则 $\boldsymbol{A}$ 的列向量组与 $\boldsymbol{B}$ 的列向量组等价.

向量组的线性组合、线性表示及等价等概念,也可移用于线性方程组: 对方 程组 $A$ 的各个方程作线性运算所得到的一个方程就称为方程组 $A$ 的一个线性 组合; 若方程组 $B$ 的每个方程都是方程组 $A$ 的线性组合, 就称方程组 $B$ 能由方 程组 $A$ 线性表示,这时方程组 $A$ 的解一定是方程组 $B$ 的解 ; 若方程组 $A$ 与方程 组 $B$ 能相互线性表示, 就称这两个方程组可互推, 可互推的线性方程组一定 同解.

按定义 3 , 向量组 $B: b_{1}, b_{2}, \cdots, b_{t}$ 能由向望组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性表示, 其含义是存在矩阵 $\boldsymbol{K}_{m} x_{1}$, 使 $\left(b_{1}, \cdots, b_{l}\right)=\left(a_{1}, \cdots, a_{m}\right) \boldsymbol{K}$, 也就是矩阵方程

$$
\left(a_{1}, a_{2}, \cdots, a_{m}\right) X=\left(b_{1}, b_{2}, \cdots, b_{l}\right)
$$

有解. 由上章定理 6 ,立即可得

定理 2 向量组 $B: b_{1}, b_{2}, \cdots, b_{1}$ 能由向盢组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性表示的 充分必要条件是矩阵 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 的秩等于矩阵 $(\boldsymbol{A}, \boldsymbol{B})=\left(a_{1}, \cdots, a_{m}\right.$, $\left.b_{1}, \cdots, b_{l}\right)$ 的秩, 即 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{B})$.

推论 向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 与向目组 $B: b_{1}, b_{2}, \cdots, b_{l}$ 等价的充分必要 条件是

$$
R(\boldsymbol{A})=R(\boldsymbol{B})=R(\boldsymbol{A}, \boldsymbol{B}),
$$

其中 $A$ 和 $B$ 是向貫组 $A$ 和 $B$ 所构成的矩阵.

证 因 $A$ 组与 $B$ 组能相互线性表示, 依据定理 2 , 知它们等价的充分必要 条件是

$$
R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{B}) \quad \text { 且 } \quad R(\boldsymbol{B})=R(\boldsymbol{B}, \boldsymbol{A}),
$$

而 $R(\boldsymbol{A}, \boldsymbol{B})=R(\boldsymbol{B}, \boldsymbol{A})$, 合起来即得充分必要条件为

$$
R(\boldsymbol{A})=R(\boldsymbol{B})=R(\boldsymbol{A}, \boldsymbol{B}) \text {. }
$$

例 1 设 $a_{1}=\left(\begin{array}{l}1 \\ 1 \\ 2 \\ 2\end{array}\right), a_{2}=\left(\begin{array}{l}1 \\ 2 \\ 1 \\ 3\end{array}\right), a_{3}=\left(\begin{array}{r}1 \\ -1 \\ 4 \\ 0\end{array}\right), b=\left(\begin{array}{l}1 \\ 0 \\ 3 \\ 1\end{array}\right)$, 证明向量 $b$ 能由向量组 $a_{1}, a_{2}, a_{3}$ 线性表示, 并求出表示式.

解 根据定理 1, 要证矩阵 $A=\left(a_{1}, a_{2}, a_{3}\right)$ 与 $B=(A, b)$ 的秩相等. 为此, 把 $\boldsymbol{B}$ 化成行最简形:

$$
\boldsymbol{B}=\left(\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
1 & 2 & -1 & 0 \\
2 & 1 & 4 & 3 \\
2 & 3 & 0 & 1
\end{array}\right) \underset{r_{3}-2 r_{1}}{r_{4}-2 r_{1}}\left(\begin{array}{rrrr}
1 & 1 & 1 & 1 \\
0 & 1 & -2 & -1 \\
0 & -1 & 2 & 1 \\
0 & 1 & -2 & -1
\end{array}\right) \dot{r}\left(\begin{array}{rrrr}
1 & 0 & 3 & 2 \\
0 & 1 & -2 & -1 \\
0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0
\end{array}\right),
$$

可见, $R(\boldsymbol{A})=R(\boldsymbol{B})$, 因此, 向量 $\boldsymbol{b}$ 能由向量组 $\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{3}$ 线性表示.

由上述行最简形,可得方程 $\left(a_{1}, a_{2}, a_{3}\right) x=b$ 的通解为

$$
\boldsymbol{x}=c\left(\begin{array}{r}
-3 \\
2 \\
1
\end{array}\right)+\left(\begin{array}{r}
2 \\
-1 \\
0
\end{array}\right)=\left(\begin{array}{c}
-3 c+2 \\
2 c-1 \\
c
\end{array}\right) \text {, }
$$

从而得表示式

$$
b=\left(a_{1}, a_{2}, a_{3}\right) x=(-3 c+2) a_{1}+(2 c-1) a_{2}+c a_{3},
$$

其中 $c$ 可任意取值.

例 2 设 $a_{1}=\left(\begin{array}{r}1 \\ -1 \\ 1 \\ -1\end{array}\right), a_{2}=\left(\begin{array}{l}3 \\ 1 \\ 1 \\ 3\end{array}\right), b_{1}=\left(\begin{array}{l}2 \\ 0 \\ 1 \\ 1\end{array}\right), b_{2}=\left(\begin{array}{l}1 \\ 1 \\ 0 \\ 2\end{array}\right), b_{3}=\left(\begin{array}{r}3 \\ -1 \\ 2 \\ 0\end{array}\right)$,

证明向量组 $a_{1}, a_{2}$ 与向量组 $b_{1}, b_{2}, b_{3}$ 等价.

证 记 $A=\left(a_{1}, a_{2}\right), B=\left(b_{1}, b_{2}, b_{3}\right)$. 根据定理 2 的推论, 只要证 $R(A)=$ $R(\boldsymbol{B})=R(\boldsymbol{A}, \boldsymbol{B})$. 为此把矩阵 $(\boldsymbol{A}, \boldsymbol{B})$ 化成行阶梯形:

$$
(\boldsymbol{A}, \boldsymbol{B})=\left(\begin{array}{rrrrr}
1 & 3 & 2 & 1 & 3 \\
-1 & 1 & 0 & 1 & -1 \\
1 & 1 & 1 & 0 & 2 \\
-1 & 3 & 1 & 2 & 0
\end{array}\right) \stackrel{\sim}{\sim}\left(\begin{array}{rrrrr}
1 & 3 & 2 & 1 & 3 \\
0 & 4 & 2 & 2 & 2 \\
0 & -2 & -1 & -1 & -1 \\
0 & 6 & 3 & 3 & 3
\end{array}\right) \sim\left(\begin{array}{lllll}
1 & 3 & 2 & 1 & 3 \\
0 & 2 & 1 & 1 & 1 \\
0 & 0 & 0 & 0 & 0 \\
0 & 0 & 0 & 0 & 0
\end{array}\right),
$$

可见, $R(\boldsymbol{A})=2, R(\boldsymbol{A}, \boldsymbol{B})=2$.

容易看出矩阵 $\boldsymbol{B}$ 中有不等于 0 的 2 阶子式,故 $R(\boldsymbol{B}) \geqslant 2$. 又

$$
R(\boldsymbol{B}) \leqslant R(\boldsymbol{A}, \boldsymbol{B})=2 \text {, }
$$

于是知 $R(B)=2$. 因此,

$$
R(\boldsymbol{A})=R(\boldsymbol{B})=R(\boldsymbol{A}, \boldsymbol{B}) .
$$

定理 3 设向量组 $B: b_{1}, b_{2}, \cdots, b_{l}$ 能由向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性表示, 则 $R\left(b_{1}, b_{2}, \cdots, b_{l}\right) \leqslant R\left(a_{1}, a_{2}, \cdots, a_{m}\right)$.

证 记 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right), B=\left(b_{1}, b_{2}, \cdots, b_{l}\right)$. 按定理的条件，根据定理 2 有 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{B})$, 而 $R(\boldsymbol{B}) \leqslant R(\boldsymbol{A}, \boldsymbol{B})$, 因此

$$
R(\boldsymbol{B}) \leqslant R(\boldsymbol{A}) .
$$

前面我们把定理 1 与上章定理 5 对应,把定理 2 与上章定理 6 对应,而定理 3 可与上章定理 7对应. 事实上, 按定理 3 的条件, 知有矩阵 $K$, 使 $B=A K$, 从而根 据上章定理 7, 即有 $R(B) \leqslant R(A)$.

上述各定理之间的对应,其基础是向量组与矩阵的对应，从而有下述对应：

向量组 $B: b_{1}, b_{2}, \cdots, b_{1}$ 能由向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性表示

$\Leftrightarrow$ 有矩阵 $\boldsymbol{K}$, 使 $\boldsymbol{B}=\boldsymbol{A K}$

$\Leftrightarrow$ 方程 $\boldsymbol{A X}=\boldsymbol{B}$ 有解.

上述对应的三种叙述都可对应到充分必要条件: $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{B})$, 并都有 必要条件: $R(\boldsymbol{A}) \geqslant R(\boldsymbol{B})$. 这里, 第一种可称为几何语言, 后两种以及充分必要 条件和必要条件则都是矩阵语言. 我们要掌握用矩阵语言表述几何问题,还要掌 握用几何语言来解释矩阵表述的结论.

上一章中把线性方程组写成矩阵形式, 通过矩阵的运算求得它的解, 还用矩 阵的语言给出了线性方程组有解、有唯一解的充分必要条件; 本章中将向荲组的 问题表述成矩阵形式,通过矩阵的运算得出结果, 然后把矩阵形式的结果 “翻译” 成几何问题的结论. 这种用矩阵来表述问题, 并通过矩阵的运算解决问题的方 法, 通常叫做矩阵方法, 这正是线性代数的基本方法, 读者应有意识地去加强这 一方法的练习.

例 3 设 $n$ 维向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 构成 $n \times m$ 矩阵 $A=\left(a_{1}, a_{2}, \cdots\right.$, $\left.a_{m}\right), n$ 阶单位矩阵 $E=\left(e_{1}, e_{2}, \cdots, e_{n}\right)$ 的列向埋叫做 $n$ 维单位坐标向量. 证明: $n$ 维单位坐标向量组 $e_{1}, e_{2}, \cdots, e_{n}$ 能由向量组 $A$ 线性表示的充分必要条件是 $R(\boldsymbol{A})=n$.

证 根据定理 2, 向量组 $e_{1}, e_{2}, \cdots, e_{n}$ 能由向量组 $A$ 线性表示的充分必要 条件是 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{E})$.

而 $R(\boldsymbol{A}, \boldsymbol{E}) \geqslant R(\boldsymbol{E})=n$, 又矩阵 $(\boldsymbol{A}, \boldsymbol{E})$ 含 $n$ 行, 知 $R(\boldsymbol{A}, \boldsymbol{E}) \leqslant n$, 合起来 有 $R(\boldsymbol{A}, \boldsymbol{E})=n$. 因此条件 $R(\boldsymbol{A})=R(\boldsymbol{A}, \boldsymbol{E})$ 就是 $R(\boldsymbol{A})=n$.

本例所证结论用矩阵语言可叙述为

对矩阵 $\boldsymbol{A}_{n \times m}$, 存在矩阵 $\boldsymbol{K}_{m \times n}$, 使 $\boldsymbol{A K}=\boldsymbol{E}_{n}$ 的充分必要条件是 $R(\boldsymbol{A})=n$. 也可叙述为

矩阵方程 $\boldsymbol{A}_{n \times m} \boldsymbol{X}=\boldsymbol{E}_{n}$ 有解的充分必要条件是 $R(\boldsymbol{A})=n$ (参见上章习题第 21 题).

## $\S 2$ 向量组的线性相关性

定义 4 给定向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$, 如果存在不全为零的数 $k_{1}, k_{2}, \cdots$, $k_{m}$, 使

$$
k_{1} a_{1}+k_{2} a_{2}+\cdots+k_{m} a_{m}=\mathbf{0},
$$

则称向量组 $A$ 是线性相关的,否则称它线性无关.

说向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 线性相关, 通常是指 $m \geqslant 2$ 的情形, 但定义 4 也适 用于 $m=1$ 的情形. 当 $m=1$ 时, 向量组只含一个向量, 对于只含一个向量 $a$ 的 向量组, 当 $a=0$ 时是线性相关的, 当 $a \neq 0$ 时是线性无关的. 对于含 2 个向量 $a_{1}$, $a_{2}$ 的向量组,它线性相关的充分必要条件是 $a_{1}, a_{2}$ 的分黑对应成比例, 其几何 意义是两向量共线.3个向墨线性相关的几何意义是三向量共面.

向量组 $A: \boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{m}(m \geqslant 2)$ 线性相关, 也就是在向量组 $A$ 中至少有一 个向量能由其余 $m-1$ 个向量线性表示. 这是因为:

如果向墨组 $A$ 线性相关, 则有不全为 0 的数 $k_{1}, k_{2}, \cdots, k_{m}$ 使 $k_{1} a_{1}+$ $k_{2} a_{2}+\cdots+k_{m} a_{m}=0$. 因 $k_{1}, k_{2}, \cdots, k_{m}$ 不全为 0 , 不妨设 $k_{1} \neq 0$, 于是便有

$$
a_{1}=\frac{-1}{k_{1}}\left(k_{2} a_{2}+\cdots+k_{m} a_{m}\right) \text {, }
$$

即 $a_{1}$ 能由 $a_{2}, \cdots, a_{m}$ 线性表示.

如果向量组 $A$ 中有某个向墨能由其余 $m-1$ 个向量线性表示, 不妨设 $a_{m}$ 能由 $a_{1}, \cdots, a_{m-1}$ 线性表示, 即有 $\lambda_{1}, \cdots, \lambda_{m-1}$ 使 $a_{m}=\lambda_{1} a_{1}+\cdots+\lambda_{m-1} a_{m-1}$, 于 是

$$
\lambda_{1} a_{1}+\cdots+\lambda_{m-1} a_{m-1}+(-1) a_{m}=0,
$$

因为 $\lambda_{1}, \cdots, \lambda_{m-1},-1$ 这 $m$ 个数不全为 0 (至少 $-1 \neq 0$ ), 所以向量组 $A$ 线性 相关.

向量组的线性相关与线性无关的概念也可移用于线性方程组. 当方程组中 有某个方程是其余方程的线性组合时, 这个方程就是多余的, 这时称方程组 (各 个方程) 是线性相关的; 当方程组中没有多余方程,就称该方程组 (各个方程)线 性无关(或线性独立).

向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 构成矩阵 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$, 向量组 $A$ 线性相 关, 就是齐次线性方程组

$$
x_{1} a_{1}+x_{2} a_{2}+\cdots+x_{m} a_{m}=0 \text {, 即 } A x=0
$$

有非零解. 由上章定理 4 , 立即可得

定理 4 向甪组 $a_{1}, a_{2}, \cdots, a_{m}$ 线性相关的充分必要条件是它所构成的矩 阵 $\boldsymbol{A}=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 的秩小于向胃个数 $m$; 向量组线性无关的充分必要条件 是 $R(\boldsymbol{A})=m$.

例 4 试讨论 $n$ 维单位坐标向量组的线性相关性.

解 $n$ 维单位坐标向量组构成的矩阵

$$
E=\left(e_{1}, e_{2}, \cdots, e_{n}\right)
$$

是 $n$ 阶单位矩阵. 由 $|\boldsymbol{E}|=1 \neq 0$, 知 $R(\boldsymbol{E})=n$, 即 $R(\boldsymbol{E})$ 等于向量组中向望个 数,故由定理 4 知此向堅组是线性无关的.

例 5 已知

$$
a_{14}=\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right), a_{2}=\left(\begin{array}{l}
0 \\
2 \\
5
\end{array}\right), a_{3}=\left(\begin{array}{l}
2 \\
4 \\
7
\end{array}\right),
$$

试讨论向量组 $a_{1}, a_{2}, a_{3}$ 及向量组 $a_{1}, a_{2}$ 的线性相关性.

解 对矩阵 $\left(a_{1}, a_{2}, a_{3}\right)$ 施行初等行变换变成行阶梯形矩阵,即可同时看出 矩阵 $\left(a_{1}, a_{2}, a_{3}\right)$ 及 $\left(a_{1}, a_{2}\right)$ 的秩,利用定理 4 即可得出结论.

$$
\left(a_{1}, a_{2}, a_{3}\right)=\left(\begin{array}{lll}
1 & 0 & 2 \\
1 & 2 & 4 \\
1 & 5 & 7
\end{array}\right) \underset{r_{3}-r_{1}}{\frac{r_{2}-r_{1}}{r}}\left(\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 2 \\
0 & 5 & 5
\end{array}\right) \stackrel{r_{3}-\frac{5}{2} r_{2}}{=}\left(\begin{array}{lll}
1 & 0 & 2 \\
0 & 2 & 2 \\
0 & 0 & 0
\end{array}\right),
$$

可见 $R\left(a_{1}, a_{2}, a_{3}\right)=2$, 故向墨组 $a_{1}, a_{2}, a_{3}$ 线性相关; 同时可见 $R\left(a_{1}, a_{2}\right)=$ 2 , 故向㫪组 $a_{1}, a_{2}$ 线性无关.

例 6 已知向量组 $a_{1}, a_{2}, a_{3}$ 线性无关, $b_{1}=a_{1}+a_{2}, b_{2}=a_{2}+a_{3}, b_{3}=a_{3}$ $+a_{1}$, 试证向量组 $b_{1}, b_{2}, b_{3}$ 线性无关.

证一 把已知的三个向量等式写成一个矩阵等式

$$
\left(b_{1}, b_{2}, b_{3}\right)=\left(a_{1}, a_{2}, a_{3}\right)\left(\begin{array}{lll}
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right),
$$

记作 $B=A K$. 设 $B x=0$, 以 $B=A K$ 代人得 $A(K x)=0$. 因为矩阵 $A$ 的列向量 组线性无关, 根据向量组线性无关的定义, 知 $\boldsymbol{K} \boldsymbol{x}=\mathbf{0}$. 又因 $|\boldsymbol{K}|=2 \neq 0$, 知方程 $K x=0$ 只有零解 $\boldsymbol{x}=\mathbf{0}$. 所以矩阵 $\boldsymbol{B}$ 的列向量组 $b_{1}, b_{2}, b_{3}$ 线性无关.

证二 把已知条件合写成

$$
\left(b_{1}, b_{2}, b_{3}\right)=\left(a_{1}, a_{2}, a_{3}\right)\left(\begin{array}{lll}
1 & 0 & 1 \\
1 & 1 & 0 \\
0 & 1 & 1
\end{array}\right),
$$

记作 $\boldsymbol{B}=\boldsymbol{A K}$. 因 $|\boldsymbol{K}|=2 \neq 0$, 知 $\boldsymbol{K}$ 可逆, 根据上章所述矩阵积的性质 4 知 $R(\boldsymbol{B})=R(\boldsymbol{A})$.

因为 $\boldsymbol{A}$ 的列向量组线性无关, 根据定理 4 知 $R(\boldsymbol{A})=3$, 从而 $R(\boldsymbol{B})=3$, 再 由定理 4 知 $B$ 的 3 个列向量线性无关,即 $b_{1}, b_{2}, b_{3}$ 线性无关.

本例给出两种证法, 这两种证法都是常用的, 证明时首先是把已知条件表述 成矩阵形式. 证一的关键是: 按定义 4 把证明向量组线性无关转化为证明齐次方 程没有非零解, 因而去考察方程 $\boldsymbol{B} \boldsymbol{x}=\mathbf{0}$. 证二用了矩阵的秩的有关知识, 还用了 定理 4 , 从而可以不涉及线性方程而直接证得结论.

线性相关性是向量组的一个重要性质,下面介绍与之有关的一些简单的结 论.

定理 5 (1) 若向然组 $A: a_{1}, \cdots, a_{m}$ 线性相关, 则向显组 $B: a_{1}, \cdots, a_{m}$, $a_{m+1}$ 也线性相关. 反言之, 若向迅组 $B$ 线性无关, 则向量组 $A$ 也线性无关.

(2) $m$ 个 $n$ 维向置组成的向量组, 当维数 $n$ 小于向貫个数 $m$ 时一定线性相 关. 特别地, $n+1$ 个 $n$ 维向量一定线性相关.

(3) 设向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 线性无关, 而向量组 $B: a_{1}, \cdots, a_{m}, b$ 线性 相关,则向量 $b$ 必能由向量组 $A$ 线性表示,且表示式是惟一的.

证 这些结论都可利用定理 4 来证明.

（1）记 $\boldsymbol{A}=\left(\boldsymbol{a}_{1}, \cdots, \boldsymbol{a}_{m}\right), \boldsymbol{B}=\left(\boldsymbol{a}_{1}, \cdots, \boldsymbol{a}_{m}, a_{m+1}\right)$, 有 $R(\boldsymbol{B}) \leqslant R(\boldsymbol{A})+1$. 因 向量组 $A$ 线性相关, 故根据定理 4 , 有 $R(A)<m$, 从而 $R(B) \leqslant R(A)+1<m$ +1 , 因此根据定理 4 知向量组 $B$ 线性相关.

结论 (1) 是对向量组增加 1 个向量而言的,增加多个向量结论也仍然成立. 即设向量组 $A$ 是向量组 $B$ 的一部分 (这时称 $A$ 组是 $B$ 组的部分组), 于是结论 (1) 可一般的叙述为:一个向量组若有线性相关的部分组,则该向照组线性相关. 特别地, 含零向量的向量组必线性相关.一个向量组若线性无关, 则它的任何部 分组都线性无关.

（2） $m$ 个 $n$ 维向量 $a_{1}, a_{2}, \cdots, a_{m}$ 构成矩阵 $A_{n \times m}=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$, 有 $R(\boldsymbol{A}) \leqslant n$. 当 $n<m$ 时,有 $R(\boldsymbol{A})<m$, 故 $m$ 个向望 $a_{1}, a_{2}, \cdots, a_{m}$ 线性相关.

（3）记 $\boldsymbol{A}=\left(a_{1}, \cdots, a_{m}\right), \boldsymbol{B}=\left(a_{1}, \cdots, a_{m}, b\right)$, 有 $R(\boldsymbol{A}) \leqslant R(\boldsymbol{B})$. 因 $A$ 组线 性无关, 有 $R(\boldsymbol{A})=m$; 因 $B$ 组线性相关, 有 $R(\boldsymbol{B})<m+1$. 所以 $m \leqslant R(\boldsymbol{B})<$ $m+1$, 即有 $R(\boldsymbol{B})=m$.

由 $R(\boldsymbol{A})=R(\boldsymbol{B})=m$, 根据上章定理 3, 知方程组

$$
\left(a_{1}, \cdots, a_{m}\right) x=b
$$

有倠一解, 即向量 $\boldsymbol{b}$ 能由向量组 $A$ 线性表示, 且表示式是惟一的.

例 7 设向墨组 $a_{1}, a_{2}, a_{3}$ 线性相关, 向量组 $a_{2}, a_{3}, a_{4}$ 线性无关,证明:

(1) $a_{1}$ 能由 $a_{2}, a_{3}$ 线性表示;

（2） $a_{4}$ 不能由 $a_{1}, a_{2}, a_{3}$ 线性表示.

证 (1) 因 $a_{2}, a_{3}, a_{4}$ 线性无关, 由定理 5(1) 知 $a_{2}, a_{3}$ 线性无关, 而 $a_{1}$, $a_{2}, a_{3}$ 线性相关, 由定理 5(3) 知 $a_{1}$ 能由 $a_{2}, a_{3}$ 线性表示.

（2）用反证法. 假设 $a_{4}$ 能由 $a_{1}, a_{2}, a_{3}$ 表示, 而由(1)知 $a_{1}$ 能由 $a_{2}, a_{3}$ 表 示,因此 $a_{4}$ 能由 $a_{2}, a_{3}$ 线性表示, 这与 $a_{2}, a_{3}, a_{4}$ 线性无关矛盾.

## $\S 3$ 向量组的秩

上两节在讨论向量组的线性组合和线性相关性时, 矩阵的秩起了十分重要 的作用. 为使讨论进一步深人,下面把秩的概念引进向量组.

定义 5 设有向墨组 $A$, 如果在 $A$ 中能选出 $r$ 个向量 $a_{1}, a_{2}, \cdots, a_{r}$, 满足

(i) 向量组 $A_{0}: a_{1}, a_{2}, \cdots, a_{r}$ 线性无关;

(ii) 向量组 $A$ 中任意 $r+1$ 个向量 (如果 $A$ 中有 $r+1$ 个向量的话)都线性 相关,

那么称向量组 $A_{0}$ 是向量组 $A$ 的一个最大线性无关向量组 (简称最大无关 组); 最大无关组所含向量个数 $r$ 称为向量组 $A$ 的秩, 记作 $R_{A}$.

只含零向晊的向量组没有最大无关组,规定它的秩为 0 .

对于只含有限个向量的向量组 $A: a_{1}, a_{2}, \cdots, a_{m}$, 它可以构成矩阵 $A=$ $\left(a_{1}, a_{2}, \cdots, a_{m}\right)$. 把定义 5 与上章矩阵的最高阶非零子式及矩阵的秩的定义作 比较,容易想到向量组 $A$ 的秩就等于矩阵 $\boldsymbol{A}$ 的秩, 即有

定理 6 矩阵的秩等于它的列向量组的秩, 也等于它的行向量组的秩.

证 设 $\boldsymbol{A}=\left(a_{1}, a_{2}, \cdots, a_{m}\right), R(\boldsymbol{A})=r$, 并设 $r$ 阶子式 $D_{r} \neq 0$. 根据定理 4, 由 $D_{r} \neq 0$ 知 $D_{r}$ 所在的 $r$ 列线性无关; 又由 $\boldsymbol{A}$ 中所有 $r+1$ 阶子式均为零, 知 $\boldsymbol{A}$ 中任意 $r+1$ 个列向量都线性相关. 因此 $D_{r}$ 所在的 $r$ 列是 $\boldsymbol{A}$ 的列向量组的一个 最大无关组，所以列向量组的秩等于 $r$.

类似可证矩阵 $\boldsymbol{A}$ 的行向量组的秩也等于 $R(\boldsymbol{A})$.

今后向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 的秋也记作 $R\left(a_{1}, a_{2}, \cdots, a_{m}\right)$.

从上述证明中可见: 若 $D_{r}$ 是矩阵 $\boldsymbol{A}$ 的一个最高阶非零子式,则 $D_{r}$ 所在的 $r$ 列即是 $\boldsymbol{A}$ 的列向量组的一个最大无关组, $D_{r}$ 所在的 $r$ 行即是 $\boldsymbol{A}$ 的行向量组的 一个最大无关组.

向量组的最大无关组一般不是惟一的.如例 5

$$
\left(a_{1}, a_{2}, a_{3}\right)=\left(\begin{array}{lll}
1 & 0 & 2 \\
1 & 2 & 4 \\
1 & 5 & 7
\end{array}\right),
$$

由 $R\left(a_{1}, a_{2}\right)=2$, 知 $a_{1}, a_{2}$ 线性无关; 由 $R\left(a_{1}, a_{2}, a_{3}\right)=2$ 知 $a_{1}, a_{2}, a_{3}$ 线性相 关,因此 $a_{1}, a_{2}$ 是向量组 $a_{1}, a_{2}, a_{3}$ 的一个最大无关组.

此外, 由 $R\left(a_{1}, a_{3}\right)=2$ 及 $R\left(a_{2}, a_{3}\right)=2$ 可知 $a_{1}, a_{3}$ 和 $a_{2}, a_{3}$ 都是向量组 $a_{1}, a_{2}, a_{3}$ 的最大无关组.

例 8 全体 $n$ 维向量构成的向量组记作 $\mathbb{R}^{n}$, 求 $\mathbb{R}^{n}$ 的一个最大无关组及 $\mathbb{R}^{n}$ 的秩.

解 在例 4 中, 我们证明了 $n$ 维单位坐标向量构成的向量组

$$
E: e_{1}, e_{2}, \cdots, e_{n}
$$

是线性无关的, 又根据定理 5 的结论 (2), 知 $\mathbb{R}^{n}$ 中的任意 $n+1$ 个向量都线性相 关,因此向量组 $E$ 是 $\mathbb{R}^{n}$ 的一个最大无关组,且 $\mathbb{R}^{n}$ 的秩等于 $n$.

显然, $\mathbb{R}^{n}$ 的最大无关组很多, 任何 $n$ 个线性无关的 $n$ 维向量都是 $\mathbb{R}^{n}$ 的最大 无关组

向量组 $A$ 和它自己的最大无关组 $A_{0}$ 是等价的. 这是因为 $A_{0}$ 组是 $A$ 组的 一个部分组,故 $A_{0}$ 组总能由 $A$ 组线性表示 ( $A$ 中每个向量都能由 $A$ 组表示); 而由定义 5 的条件 (ii) 知, 对于 $A$ 中任一向量 $a, r+1$ 个向量 $a_{1}, \cdots, a_{r}, a$ 线性 相关, 而 $a_{1}, \cdots, a_{r}$ 线性无关, 根据定理 5(3) 知 $\boldsymbol{a}$ 能由 $a_{1}, \cdots, a_{r}$ 线性表示, 即 $A$ 组能由 $A_{0}$ 组线性表示. 所以 $A$ 组与 $A_{0}$ 组等价.

上述结论的逆命题也是成立的,现把它作为定理 3 的推论叙述如下.

推论 (最大无关组的等价定义) 设向量组 $A_{0}: a_{1}, a_{2}, \cdots, a_{r}$ 是向量组 $A$ 的一个部分组,且满足

(i) 向量组 $A_{0}$ 线性无关;

(ii) 向圈组 $A$ 的任一向量都能由向量组 $A_{0}$ 线性表示, 那么向量组 $A_{0}$ 便是向壆组 $A$ 的一个最大无关组，

证 只要证向量组 $A$ 中任意 $r+1$ 个向量线性相关. 设 $b_{1}, b_{2}, \cdots, b_{r+1}$ 是 $A$ 中任意 $r+1$ 个向量, 由条件 (ii) 知这 $r+1$ 个向量能由向量组 $A_{0}$ 线性表示, 从 而根据定理 3, 有

$$
R\left(b_{1}, b_{2}, \cdots, b_{r+1}\right) \leqslant R\left(a_{1}, a_{2}, \cdots, a_{r}\right)=r,
$$

再据定理 4 知 $r+1$ 个向量 $b_{1}, b_{2}, \cdots, b_{r+1}$ 线性相关. 因此向量组 $A_{0}$ 满足定义 5 所规定的最大无关组的条件.

例 9 设齐次线性方程组

$$
\left\{\begin{aligned}
x_{1}+2 x_{2}+x_{3}-2 x_{4} & =0 \\
2 x_{1}+3 x_{2}-x_{4} & =0 \\
x_{1}-x_{2}-5 x_{3}+7 x_{4} & =0
\end{aligned}\right.
$$

的全体解向量构成的向量组为 $S$, 求 $S$ 的秩.

解 先解方程,为此把系数矩阵 $\boldsymbol{A}$ 化成行最简形:

$$
\boldsymbol{A}=\left(\begin{array}{rrrr}
1 & 2 & 1 & -2 \\
2 & 3 & 0 & -1 \\
1 & -1 & -5 & 7
\end{array}\right) \frac{r_{2}-2 r_{1}}{r_{3}-r_{1}}\left(\begin{array}{rrrr}
1 & 2 & 1 & -2 \\
0 & -1 & -2 & 3 \\
0 & -3 & -6 & 9
\end{array}\right) \frac{r_{1}+2 r_{2}-3 r_{2}}{r_{2} \times(-1)}\left(\begin{array}{rrrr}
1 & 0 & -3 & 4 \\
0 & 1 & 2 & -3 \\
0 & 0 & 0 & 0
\end{array}\right) \text {, }
$$

得

$$
\left\{\begin{array}{l}
x_{1}=3 x_{3}-4 x_{4}, \\
x_{2}=-2 x_{3}+3 x_{4},
\end{array}\right.
$$

令自由末知数 $x_{3}=c_{1}, x_{4}=c_{2}$, 得通解

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=c_{1}\left(\begin{array}{r}
3 \\
-2 \\
1 \\
0
\end{array}\right)+c_{2}\left(\begin{array}{r}
-4 \\
3 \\
0 \\
1
\end{array}\right),
$$

把上式记作 $\boldsymbol{x}=c_{1} \boldsymbol{\xi}_{1}+c_{2} \boldsymbol{\xi}_{2}$, 知

$$
S=\left\{\boldsymbol{x}=c_{1} \boldsymbol{\xi}_{1}+c_{2} \boldsymbol{\xi}_{2} \mid c_{1}, c_{2} \in \mathbb{R}\right\},
$$

即 $S$ 能由向量组 $\xi_{1}, \xi_{2}$ 线性表示. 又因 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}$ 的四个分量显然不成比例, 故 $\boldsymbol{\xi}_{1}$, $\boldsymbol{\xi}_{2}$ 线性无关. 因此根据最大无关组的等价定义知 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}$ 是 $S$ 的最大无关组, 从 而 $R_{s}=2$.

设向墨组 $A: a_{1}, a_{2}, \cdots, a_{m}$ 构成矩阵 $A=\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ ，根据向量组的秩 的定义及定理 6 , 有

$$
R_{A}=R\left(a_{1}, a_{2}, \cdots, a_{m}\right)=R(A) .
$$

由此可知,前面介绍的定理 $1,2,3,4$ 中出现的矩阵的秩都可改为向量组的秩. 例 如定理 2 可叙述为

定理 2' 向量组 $b_{1}, b_{2}, \cdots, b_{1}$ 能由向贯组 $a_{1}, a_{2}, \cdots, a_{m}$ 线性表示的充分 必要条件是

$$
R\left(a_{1}, a_{2}, \cdots, a_{m}\right)=R\left(a_{1}, \cdots, a_{m}, b_{1}, \cdots, b_{l}\right) .
$$

这里记号 $R\left(a_{1}, a_{2}, \cdots, a_{m}\right)$ 既可理解为矩阵的秩, 也可理解成向量组的秩.

前面我们建立定理 $1,2,3$ 时, 限制向量组只含有限个向量, 现在我们要去掉 这一限制, 把定理 1,2,3 推广到一般情形. 推广的方法是利用向量组的䍚大无关 组作过渡.下面仅推广定理 3,定理 1 和 2 的推广请读者自行完成.

定理 $3^{\prime}$ 若向期组 $B$ 能由向盟组 $A$ 线性表示, 则 $R_{B} \leqslant R_{A}$. 证 设 $R_{A}=s, R_{B}=t$, 并设向量组 $A$ 和 $B$ 的最大无关组依次为

$$
A_{0}: a_{1}, a_{2}, \cdots, a_{s} \text { 和 } B_{0}: b_{1}, b_{2}, \cdots, b_{t},
$$

由于 $B_{0}$ 组能由 $B$ 组表示, $B$ 组能由 $A$ 组表示, $A$ 组能由 $A_{0}$ 组表示, 因此 $B_{0}$ 组 能由 $A_{0}$ 组表示, 根据定理 3 , 有

$$
R\left(b_{1}, b_{2}, \cdots, b_{t}\right) \leqslant R\left(a_{1}, a_{2}, \cdots, a_{s}\right),
$$

即 $t \leqslant s$.

今后, 定理 3 与 $3^{\prime}$ 将不加区别, 都称定理 3. 定理 1 和 2 与推广后的定理也 不加区别.

例 10 设向量组 $B$ 能由向量组 $A$ 线性表示,且它们的秩相等,证明向量组 $A$ 与向量组 $B$ 等价.

证 设向量组 $A$ 和 $B$ 合并成向量组 $C$, 根据定理 2, 因 $B$ 组能由 $A$ 组表示, 故 $R_{A}=R_{C}$, 又已知 $R_{B}=R_{A}$, 故有 $R_{A}=R_{B}=R_{C}$. 根据定理 2 的推论, 知 $A$ 组 与 $B$ 组等价.

例 11 设矩阵

$$
\boldsymbol{A}=\left(\begin{array}{rrrrr}
2 & -1 & -1 & 1 & 2 \\
1 & 1 & -2 & 1 & 4 \\
4 & -6 & 2 & -2 & 4 \\
3 & 6 & -9 & 7 & 9
\end{array}\right),
$$

求矩阵 $\boldsymbol{A}$ 的列向量组的一个最大无关组,并把不属于最大无关组的列向量用最 大无关组线性表示.

解 对 $\boldsymbol{A}$ 施行初等行变换变为行阶梯形矩阵 (参看第三章 § 1 引例)

$$
\boldsymbol{A} \sim\left(\begin{array}{rrrrr}
1 & 1 & -2 & 1 & 4 \\
\hdashline 0 & 1 & -1 & 1 & 0 \\
0 & 0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

知 $R(\boldsymbol{A})=3$, 故列向量组的最大无关组含 3 个向量. 而三个非零行的非零首元 在 $1,2,4$ 三列, 故 $a_{1}, a_{2}, a_{4}$ 为列向量组的一个最大无关组. 这是因为

$$
\left(a_{1}, a_{2}, a_{4}\right) \stackrel{\sim}{\sim}\left(\begin{array}{lll}
1 & 1 & 1 \\
0 & 1 & 1 \\
0 & 0 & 1 \\
0 & 0 & 0
\end{array}\right),
$$

知 $R\left(a_{1}, a_{2}, a_{4}\right)=3$, 故 $a_{1}, a_{2}, a_{4}$ 线性无关.

为把 $a_{3}, a_{5}$ 用 $a_{1}, a_{2}, a_{4}$ 线性表示, 把 $\boldsymbol{A}$ 再变成行最简形矩阵

$$
\boldsymbol{A} \sim\left(\begin{array}{rrrrr}
1 & 0 & -1 & 0 & 4 \\
0 & 1 & -1 & 0 & 3 \\
0 & 0 & 0 & 1 & -3 \\
0 & 0 & 0 & 0 & 0
\end{array}\right)
$$

把上列行最简形矩阵记作 $B=\left(b_{1}, b_{2}, b_{3}, b_{4}, b_{5}\right)$, 由于方程 $A x=0$ 与 $B x=0$ 同 解, 即方程

$$
\text { 与 } \begin{aligned}
& x_{1} a_{1}+x_{2} a_{2}+x_{3} a_{3}+x_{4} a_{4}+x_{5} a_{5}=\mathbf{0} \\
& x_{1} b_{1}+x_{2} b_{2}+x_{3} b_{3}+x_{4} b_{4}+x_{5} b_{5}=\mathbf{0}
\end{aligned}
$$

同解, 因此向量 $a_{1}, a_{2}, a_{3}, a_{4}, a_{5}$ 之间的线性关系与向龧 $b_{1}, b_{2}, b_{3}, b_{4}, b_{5}$ 之间 的线性关系是相同的. 现在

$$
\begin{aligned}
& b_{3}=\left(\begin{array}{r}
-1 \\
-1 \\
0 \\
0
\end{array}\right)=(-1)\left(\begin{array}{l}
1 \\
0 \\
0 \\
0
\end{array}\right)+(-1)\left(\begin{array}{l}
0 \\
1 \\
0 \\
0
\end{array}\right)=-b_{1}-b_{2}, \\
& b_{3}=4 b_{1}+3 b_{2}-3 b_{4},
\end{aligned}
$$

因此

$$
\begin{aligned}
& a_{3}=-a_{1}-a_{2}, \\
& a_{5}=4 a_{1}+3 a_{2}-3 a_{4} .
\end{aligned}
$$

本例的解法表明: 如果矩阵 $\boldsymbol{A}_{m \times n}$ 与 $\boldsymbol{B}_{i \times n}$ 的行向量组等价 (这时齐次线性方 程组 $A x=0$ 与 $B x=0$ 可互推), 则方程 $A x=0$ 与 $B x=0$ 同解, 从而 $A$ 的列向量组 各向量之间与 $\boldsymbol{B}$ 的列向量组各向量之间有相同的线性关系. 如果 $\boldsymbol{B}$ 是一个行最 简形矩阵, 则容易看出 $\boldsymbol{B}$ 的列向墨组各向些之间的线性关系, 从而也就得到 $\boldsymbol{A}$ 的列向量组各向量之间的线性关系 (一个向量组的这种线性关系一般很多, 但只 要求出这个向量组的最大无关组及不属于最大无关组的向量用最大无关组线性 表示的表示式,有了这些, 就能推知其余的线性关系).

## $\S 4$ 线性方程组的解的结构

在上一章中, 我们已经介绍了用矩阵的初等变换解线性方程组的方法, 并建 立了两个重要定理, 即

(1) $n$ 个未知数的齐次线性方程组 $\boldsymbol{A x}=\mathbf{0}$ 有非零解的充分必要条件是系数 矩阵的秩 $R(\boldsymbol{A})<n$.

(2) $n$ 个未知数的非齐次线性方程组 $A \boldsymbol{x}=\boldsymbol{b}$ 有解的充分必要条件是系数 矩阵 $\boldsymbol{A}$ 的秩等于增广矩阵 $\boldsymbol{B}$ 的秩, 且当 $R(\boldsymbol{A})=R(\boldsymbol{B})=n$ 时方程组有惟一解, 当 $R(\boldsymbol{A})=R(\boldsymbol{B})=r<n$ 时方程组有无限多个解.

下面我们用向量组线性相关性的理论来讨论线性方程组的解. 先讨论齐次 线性方程组.

设有齐次线性方程组

记

$$
\begin{aligned}
& \left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=0, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=0, \\
\cdots \cdots \cdots \cdots \cdots \\
a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n}=0,
\end{array}\right. \\
& \boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right), \boldsymbol{x}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right),
\end{aligned}
$$

则(1)式可写成向量方程

$$
\boldsymbol{A x}=\mathbf{0} \text {. }
$$

若 $x_{1}=\xi_{11}, x_{2}=\xi_{21}, \cdots, x_{n}=\xi_{n 1}$ 为 (1) 的解, 则

$$
x=\xi_{1}=\left(\begin{array}{c}
\xi_{11} \\
\xi_{21} \\
\vdots \\
\xi_{n 1}
\end{array}\right)
$$

称为方程组 (1) 的解向量, 它也就是向量方程 (2)的解.

根据向量方程 (2), 我们来讨论解向量的性质.

性质 1 若 $x=\xi_{1}, x=\xi_{2}$ 为 (2) 的解, 则 $x=\xi_{1}+\xi_{2}$ 也是 (2) 的解.

证 只要验证 $x=\xi_{1}+\xi_{2}$ 满足方程 (2):

$$
A\left(\xi_{1}+\xi_{2}\right)=A \xi_{1}+A \xi_{2}=0+0=0 .
$$

证

$$
\boldsymbol{A}\left(k \boldsymbol{\xi}_{1}\right)=k\left(\boldsymbol{A} \boldsymbol{\xi}_{1}\right)=k \mathbf{0}=\mathbf{0} \text {. }
$$

证毕

把方程 (2) 的全体解所组成的集合记作 $S$, 如果能求得解集 $S$ 的一个最大 无关组 $S_{0}: \boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{1}$, 那么方程 (2) 的任一解都可由最大无关组 $S_{0}$ 线性表 示; 另一方面,由上述性质 1,2 可知,最大无关组 $S_{0}$ 的任何线性组合

$$
\boldsymbol{x}=k_{1} \boldsymbol{\xi}_{1}+k_{2} \boldsymbol{\xi}_{2}+\cdots+k_{1} \boldsymbol{\xi}_{\text {, }}
$$

都是方程 (2) 的解,因此上式便是方程 (2)的通解.

齐次线性方程组的解集的最大无关组称为该齐次线性方程组的基础解系. 由上面的讨论可知,要求齐次线性方程组的通解, 只需求出它的基础解系.

上一章我们用初等变换的方法求线性方程组的通解, 下面我们用同一方法 来求齐次线性方程组的基础解系.

设方程组 (1) 的系数矩阵 $\boldsymbol{A}$ 的秩为 $r$,并不妨设 $\boldsymbol{A}$ 的前 $r$ 个列向量线性无 关,于是 $\boldsymbol{A}$ 的行最简形矩阵为

$$
\boldsymbol{B}=\left(\begin{array}{cccccc}
1 & \cdots & 0 & b_{11} & \cdots & b_{1, n-r} \\
\vdots & & \vdots & \vdots & & \vdots \\
0 & \cdots & 1 & b_{r 1} & \cdots & b_{r, n-r} \\
0 & & & \cdots & & 0 \\
\vdots & & & & & \vdots \\
0 & & & \cdots & & 0
\end{array}\right),
$$

与 $B$ 对应, 即有方程组

$$
\left\{\begin{array}{l}
x_{1}=-b_{11} x_{r+1}-\cdots-b_{1, n-r} x_{n}, \\
\cdots \cdots \cdots \cdots \\
x_{r}=-b_{r 1} x_{r+1}-\cdots-b_{r, n-r} x_{n},
\end{array}\right.
$$

把 $x_{r+1}, \cdots, x_{n}$ 作为自由末知数, 并令它们依次等于 $c_{1}, \cdots, c_{n-r}$, 可得方程组 (1) 的通解

$$
\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{r} \\
x_{r+1} \\
x_{r+2} \\
\vdots \\
x_{n}
\end{array}\right)=c_{1}\left(\begin{array}{c}
-b_{11} \\
\vdots \\
-b_{r 1} \\
1 \\
0 \\
\vdots \\
0
\end{array}\right)+c_{2}\left(\begin{array}{c}
-b_{12} \\
\vdots \\
-b_{r 2} \\
0 \\
1 \\
\vdots \\
0
\end{array}\right)+\cdots+c_{n-r}\left(\begin{array}{c}
-b_{1, n-r} \\
\vdots \\
-b_{r, n-r} \\
0 \\
0 \\
\vdots \\
1
\end{array}\right) .
$$

把上式记作

$$
\boldsymbol{x}=c_{1} \boldsymbol{\xi}_{1}+c_{2} \boldsymbol{\xi}_{2}+\cdots+c_{n-r} \boldsymbol{\xi}_{n-r},
$$

可知解集 $S$ 中的任一向量 $\boldsymbol{x}$ 能由 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-r}$ 线性表示, 又因为矩阵 ( $\boldsymbol{\xi}_{1}$, $\left.\boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-r}\right)$ 中有 $n-r$ 阶子式 $\left|\boldsymbol{E}_{n-r}\right| \neq 0$ 故 $R\left(\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-r}\right)=n-r$, 所以 $\xi_{1}, \xi_{2}, \cdots, \xi_{n-r}$ 线性无关. 根据最大无关组的等价定义, 即知 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-r}$ 是 解集 $S$ 的最大无关组，即 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-}$, 是方程组(1)的基础解系.

在上面的讨论中, 我们先求出齐次线性方程组的通解, 再从通解求得基础解 系. 其实我们也可先求基础解系, 再写出通解. 这只需在得到方程组 (3) 以后, 令 自由末知数 $x_{r+1}, x_{r+2}, \cdots, x_{n}$ 取下列 $n-r$ 组数

$$
\left(\begin{array}{c}
x_{r+1} \\
x_{r+2} \\
\vdots \\
x_{n}
\end{array}\right)=\left(\begin{array}{c}
1 \\
0 \\
\vdots \\
0
\end{array}\right),\left(\begin{array}{c}
0 \\
1 \\
\vdots \\
0
\end{array}\right), \cdots,\left(\begin{array}{c}
0 \\
0 \\
\vdots \\
1
\end{array}\right),
$$

由(3) 即依次可得

$$
\left(\begin{array}{c}
x_{1} \\
\vdots \\
x_{r}
\end{array}\right)=\left(\begin{array}{c}
-b_{11} \\
\vdots \\
-b_{r 1}
\end{array}\right),\left(\begin{array}{c}
-b_{12} \\
\vdots \\
-b_{r 2}
\end{array}\right), \cdots,\left(\begin{array}{c}
-b_{1, n-r} \\
\vdots \\
-b_{r, n-r}
\end{array}\right),
$$

合起来便得基础解系

$$
\xi_{1}=\left(\begin{array}{c}
-b_{11} \\
\vdots \\
-b_{r 1} \\
1 \\
0 \\
\vdots \\
0
\end{array}\right), \xi_{2}=\left(\begin{array}{c}
-b_{12} \\
\vdots \\
-b_{r 2} \\
0 \\
1 \\
\vdots \\
0
\end{array}\right), \cdots, \xi_{n-r}=\left(\begin{array}{c}
-b_{1, n-r} \\
\vdots \\
-b_{r, n-r} \\
0 \\
0 \\
\vdots \\
1
\end{array}\right) .
$$

依据以上的讨论, 还可推得

定理 7 设 $m \times n$ 矩阵 $\boldsymbol{A}$ 的秩 $R(\boldsymbol{A})=r$, 则 $n$ 元齐次线性方程组 $\boldsymbol{A x}=\mathbf{0}$ 的 解集 $S$ 的秩 $R_{S}=n-r$.

当 $R(\boldsymbol{A})=n$ 时,方程 (1) 只有零解, 没有基础解系 (此时解集 $S$ 只含一个 零向量); 当 $R(\boldsymbol{A})=r<n$ 时, 由定理 7 可知方程组(1) 的基础解系含 $n-r$ 个 向量. 因此, 由最大无关组的性质可知,方程组 (1) 的任何 $n-r$ 个线性无关的解 都可构成它的基础解系. 并由此可知齐次线性方程组的基础解系并不是惟一的, 它的通解的形式也不是惟一的.

例 12 求齐次线性方程组

$$
\left\{\begin{aligned}
x_{1}+x_{2}-x_{3}-x_{4} & =0 \\
2 x_{1}-5 x_{2}+3 x_{3}+2 x_{4} & =0 \\
7 x_{1}-7 x_{2}+3 x_{3}+x_{4} & =0
\end{aligned}\right.
$$

的基础解系与通解.

解 对系数矩阵 $\boldsymbol{A}$ 作初等行变换,变为行最简形矩阵,有

$$
\boldsymbol{A}=\left(\begin{array}{rrrr}
1 & 1 & -1 & -1 \\
2 & -5 & 3 & 2 \\
7 & -7 & 3 & 1
\end{array}\right) \frac{r_{2}-2 r_{1}}{r_{3}-7 r_{1}}\left(\begin{array}{rrrr}
1 & 1 & -1 & -1 \\
0 & -7 & 5 & 4 \\
0 & -14 & 10 & 8
\end{array}\right)
$$

$$
\begin{aligned}
\stackrel{r_{3}-2 r_{2}}{\sim}\left(\begin{array}{rrrr}
1 & 1 & -1 & -1 \\
0 & -7 & 5 & 4 \\
0 & 0 & 0 & 0
\end{array}\right) \frac{r_{2} \div(-7)}{r_{1}-r_{2}}\left(\begin{array}{rrrr}
1 & 0 & -\frac{2}{7} & -\frac{3}{7} \\
0 & 1 & -\frac{5}{7} & -\frac{4}{7} \\
0 & 0 & 0 & 0
\end{array}\right), \\
\left\{\begin{array}{l}
x_{1}=\frac{2}{7} x_{3}+\frac{3}{7} x_{4}, \\
x_{2}=\frac{5}{7} x_{3}+\frac{4}{7} x_{4},
\end{array}\right.
\end{aligned}
$$

便得

令 $\left(\begin{array}{l}x_{3} \\ x_{4}\end{array}\right)=\left(\begin{array}{l}1 \\ 0\end{array}\right)$ 及 $\left(\begin{array}{l}0 \\ 1\end{array}\right)$, 则对应有 $\left(\begin{array}{l}x_{1} \\ x_{2}\end{array}\right)=\left(\begin{array}{l}\frac{2}{7} \\ \frac{5}{7}\end{array}\right)$ 及 $\left(\begin{array}{l}\frac{3}{7} \\ \frac{4}{7}\end{array}\right)$, 即得基础解系

$$
\xi_{1}=\left(\begin{array}{c}
\frac{2}{7} \\
\frac{5}{7} \\
1 \\
0
\end{array}\right), \quad \xi_{2}=\left(\begin{array}{c}
\frac{3}{7} \\
\frac{4}{7} \\
0 \\
1
\end{array}\right) \text {, }
$$

并由此写出通解

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=c_{1}\left(\begin{array}{c}
\frac{2}{7} \\
\frac{5}{7} \\
1 \\
0
\end{array}\right)+c_{2}\left(\begin{array}{c}
\frac{3}{7} \\
\frac{4}{7} \\
0 \\
1
\end{array}\right) \quad\left(c_{1}, c_{2} \in \mathbb{R}\right) .
$$

上一章中线性方程组的解法是从(*)式写出通解 (从通解的表达式即可得 基础解系), 现在从 (*)式先取基础解系, 再写出通解, 两种解法其实没有多少 差别.

根据 $(*)$ 式, 如果取

$$
\left(\begin{array}{l}
x_{3} \\
x_{4}
\end{array}\right)=\left(\begin{array}{l}
1 \\
1
\end{array}\right) \text { 及 }\left(\begin{array}{r}
1 \\
-1
\end{array}\right) \text {, 对应得 }\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right)=\left(\begin{array}{l}
\frac{5}{7} \\
\frac{9}{7}
\end{array}\right) \text { 及 }\left(\begin{array}{r}
-\frac{1}{7} \\
\frac{1}{7}
\end{array}\right) \text {, }
$$

即得不同的基础解系

$$
\boldsymbol{\eta}_{1}=\left(\begin{array}{c}
\frac{5}{7} \\
\frac{9}{7} \\
1 \\
1
\end{array}\right), \quad \boldsymbol{\eta}_{2}=\left(\begin{array}{r}
-\frac{1}{7} \\
\frac{1}{7} \\
1 \\
-1
\end{array}\right)
$$

从而得通解

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=k_{1}\left(\begin{array}{l}
\frac{5}{7} \\
\frac{9}{7} \\
1 \\
1
\end{array}\right)+k_{2}\left(\begin{array}{r}
-\frac{1}{7} \\
\frac{1}{7} \\
1 \\
-1
\end{array}\right) \quad\left(k_{1}, k_{2} \in \mathbb{R}\right) .
$$

显然 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}$ 与 $\boldsymbol{\eta}_{1}, \boldsymbol{\eta}_{2}$ 是等价的, 两个通解虽然形式不一样, 但都含两个任意常 数,且都可表示方程组的任一解.

上述解法中, 由于行最简形矩阵的结构, $x_{1}$ 总是选为非自由末知数. 对于解 方程来说, $x_{1}$ 当然也可选为自由未知数. 如果要选 $x_{1}$ 为自由未知数, 那么就不 能采用上述化系数矩阵为行最简形矩阵的 “标准程序”, 而要稍作变化, 对系数矩 阵 $\boldsymbol{A}$ 作初等行变换时, 先把其中某一列 (不一定是第一列) 化为 $(1,0,0)^{\mathrm{T}}$. 如本 例中第四列数值较简, 容易化出两个 0 :

$$
\begin{aligned}
\boldsymbol{A} & =\left(\begin{array}{rrrr}
1 & 1 & -1 & -1 \\
2 & -5 & 3 & 2 \\
7 & -7 & 3 & 1
\end{array}\right) \underset{\substack{r_{2}+2 r_{1} \\
r_{1}+r_{1}}}{r_{1} \div(-1)}\left(\begin{array}{rrrr}
-1 & -1 & 1 & 1 \\
4 & -3 & 1 & 0 \\
8 & -6 & 2 & 0
\end{array}\right) \\
& \frac{r_{3}-2 r_{2}}{r_{1}-r_{2}}\left(\begin{array}{rrrr}
-5 & 2 & 0 & 1 \\
4 & -3 & 1 & 0 \\
0 & 0 & 0 & 0
\end{array}\right),
\end{aligned}
$$

上式最后一个矩阵虽不是行最简形矩阵, 但也具备行最简形矩阵的功能. 按照这 个矩阵,取 $x_{1}, x_{2}$ 为自由末知数,便可写出通解

$$
\begin{aligned}
& \left\{\begin{array}{l}
x_{3}=-4 x_{1}+3 x_{2}, \\
x_{4}=5 x_{1}-2 x_{2},
\end{array}\left(x_{1}, x_{2} \text { 可任意取值 }\right)\right. \\
& {\left[\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right]=c_{1}\left(\begin{array}{r}
1 \\
0 \\
-4 \\
5
\end{array}\right)+c_{2}\left(\begin{array}{r}
0 \\
1 \\
3 \\
-2
\end{array}\right) \quad\left(c_{1}, c_{2} \in \mathbb{R}\right),}
\end{aligned}
$$

而对应的基础解系为

$$
\left(\begin{array}{r}
1 \\
0 \\
-4 \\
5
\end{array}\right),\left(\begin{array}{r}
0 \\
1 \\
3 \\
-2
\end{array}\right)
$$

定理 7 不仅是线性方程组各种解法的理论基础,在讨论向量组的线性相关 性时也很有用.

例 13 设 $\boldsymbol{A}_{m \times n} \boldsymbol{B}_{n \times l}=\boldsymbol{O}$, 证明 $R(\boldsymbol{A})+R(\boldsymbol{B}) \leqslant n$.

证 记 $B=\left(b_{1}, b_{2}, \cdots, b_{l}\right)$, 则

$$
A\left(b_{1}, b_{2}, \cdots, b_{l}\right)=(0,0, \cdots, 0) \text {, }
$$

即

$$
\boldsymbol{A} \boldsymbol{b}_{i}=\mathbf{0}(i=1,2, \cdots, l),
$$

表明矩阵 $\boldsymbol{B}$ 的 $l$ 个列向量都是齐次方程 $\boldsymbol{A x}=0$ 的解. 记方程 $\boldsymbol{A x}=\mathbf{0}$ 的解集为 $S$, 由 $b_{i} \in S$, 知有 $R\left(b_{1}, b_{2}, \cdots, b_{l}\right) \leqslant R_{S}$, 即 $R(B) \leqslant R_{S}$. 而由定理 7 有 $R(\boldsymbol{A})+$ $R_{S}=n$, 故 $R(\boldsymbol{A})+R(\boldsymbol{B}) \leqslant n$.

例 14 设 $n$ 元齐次线性方程组 $\boldsymbol{A x}=0$ 与 $\boldsymbol{B x}=0$ 同解, 证明 $R(\boldsymbol{A})=R(\boldsymbol{B})$.

证 由于方程组 $\boldsymbol{A x}=\mathbf{0}$ 与 $\boldsymbol{B} \boldsymbol{x}=\mathbf{0}$ 有相同的解集, 设为 $S$, 则由定理 7 即有 $R(\boldsymbol{A})=n-R_{S}, R(B)=n-R_{S}$. 因此 $R(A)=R(B)$.

本例的结论表明, 当矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 的列数相等时, 要证 $R(\boldsymbol{A})=R(\boldsymbol{B})$, 只需 证明齐次方程 $A x=0$ 与 $B x=0$ 同解.

例 15 证明 $R\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right)=R(\boldsymbol{A})$.

证 根据例 14 的结论, 往证齐次方程 $\boldsymbol{A x}=0$ 与 $\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}=0$ 同解:

若 $\boldsymbol{x}$ 满足 $\boldsymbol{A x}=\mathbf{0}$, 则有 $\boldsymbol{A}^{\mathrm{T}}(\boldsymbol{A} \boldsymbol{x})=\mathbf{0}$, 即 $\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}=\mathbf{0}$;

若 $\boldsymbol{x}$ 满足 $\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}=\mathbf{0}$, 则 $\boldsymbol{x}^{\mathrm{T}}\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}=0$, 即 $(\boldsymbol{A x})^{\mathrm{T}}(\boldsymbol{A x})=0$, 从而 $\boldsymbol{A x}=0$ (参看第二章例 17 ).

综上可知方程组 $\boldsymbol{A x}=0$ 与 $\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right) \boldsymbol{x}=0$ 同解, 因此 $R\left(\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}\right)=R(\boldsymbol{A})$.

下面讨论非齐次线性方程组.

设有非齐次线性方程组

$$
\left\{\begin{array}{l}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}=b_{1}, \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}=b_{2}, \\
\cdots \cdots \cdots \cdots \\
a_{m 1} x_{1}+a_{m 2} x_{2}+\cdots+a_{m n} x_{n}=b_{m},
\end{array}\right.
$$

它也可写作向量方程

$$
\boldsymbol{A x}=\boldsymbol{b},
$$

向量方程 (5)的解也就是方程组 (4) 的解向量,它具有 性质 3 设 $x=\eta_{1}$ 及 $x=\eta_{2}$ 都是 (5) 的解, 则 $x=\eta_{1}-\eta_{2}$ 为对应的齐次线 性方程组

$$
\boldsymbol{A x}=\mathbf{0}
$$

的解.

证

$$
\boldsymbol{A}\left(\boldsymbol{\eta}_{1}-\boldsymbol{\eta}_{2}\right)=\boldsymbol{A} \boldsymbol{\eta}_{1}-\boldsymbol{A} \boldsymbol{\eta}_{2}=\boldsymbol{b}-\boldsymbol{b}=\mathbf{0},
$$

即 $\boldsymbol{x}=\boldsymbol{\eta}_{1}-\boldsymbol{\eta}_{2}$ 满足方程 (6).

性质 4 设 $x=\boldsymbol{\eta}$ 是方程 (5) 的解, $x=\xi$ 是方程 (6) 的解, 则 $x=\xi+\eta$ 仍是 方程 (5) 的解.

证

$$
\boldsymbol{A}(\boldsymbol{\xi}+\boldsymbol{\eta})=\boldsymbol{A} \boldsymbol{\xi}+\boldsymbol{A} \boldsymbol{\eta}=\mathbf{0}+\boldsymbol{b}=\boldsymbol{b},
$$

即 $\boldsymbol{x}=\boldsymbol{\xi}+\boldsymbol{\eta}$ 满足方程 (5).

证毕

由性质 3 可知,若求得 (5)的一个解 $\boldsymbol{\eta}^{*}$, 则 (5) 的任一解总可表示为

$$
\boldsymbol{x}=\boldsymbol{\xi}+\boldsymbol{\eta}^{*},
$$

其中 $\boldsymbol{x}=\boldsymbol{\xi}$ 为方程 (6) 的解, 又若方程 (6) 的通解为 $\boldsymbol{x}=k_{1} \xi_{1}+\cdots+k_{n-r} \xi_{n-r}$, 则 方程 (5) 的任一解总可表示为

$$
\boldsymbol{x}=k_{1} \boldsymbol{\xi}_{1}+\cdots+\dot{k}_{n-r} \boldsymbol{\xi}_{n-\boldsymbol{r}}+\boldsymbol{\eta}^{*} .
$$

而由性质 4 可知,对任何实数 $k_{1}, \cdots, k_{n-r}$, 上式总是方程 (5) 的解. 于是方 程 (5) 的通解为

$$
\boldsymbol{x}=k_{1} \boldsymbol{\xi}_{1}+\cdots+k_{n-r} \boldsymbol{\xi}_{n-r}+\boldsymbol{\eta}^{*}\left(k_{1}, \cdots, k_{n-r} \text { 为任意实数 }\right) \text {. }
$$

其中 $\xi_{1}, \cdots, \xi_{n-r}$ 是方程组 (6) 的基础解系.

例 16 求解方程组

$$
\left\{\begin{array}{l}
x_{1}-x_{2}-x_{3}+x_{4}=0, \\
x_{1}-x_{2}+x_{3}-3 x_{4}=1, \\
x_{1}-x_{2}-2 x_{3}+3 x_{4}=-\frac{1}{2} .
\end{array} .\right.
$$

解 对增广矩阵 B 施行初等行变换：

$$
\begin{gathered}
\boldsymbol{B}=\left(\begin{array}{rrrrr}
1 & -1 & -1 & 1 & 0 \\
1 & -1 & 1 & -3 & 1 \\
1 & -1 & -2 & 3 & -\frac{1}{2}
\end{array}\right) \frac{r_{2}-r_{1}}{r_{3}-r_{1}}\left(\begin{array}{rrrrr}
1 & -1 & -1 & 1 & 0 \\
0 & 0 & 2 & -4 & 1 \\
0 & 0 & -1 & 2 & -\frac{1}{2}
\end{array}\right) \\
\left.\frac{\substack{r_{1}-r_{3} \\
r_{2} \div 2 \\
r_{3}+r_{2}}}{1} \begin{array}{llllr}
1 & 0 & -1 & \frac{1}{2} \\
0 & 0 & 1 & -2 & \frac{1}{2} \\
0 & 0 & 0 & 0 & 0
\end{array}\right),
\end{gathered}
$$

可见 $R(\boldsymbol{A})=R(\boldsymbol{B})=2$, 故方程组有解, 并有

$$
\left\{\begin{array}{l}
x_{1}=x_{2}+x_{4}+\frac{1}{2}, \\
x_{3}=2 x_{4}+\frac{1}{2} .
\end{array}\right.
$$

取 $x_{2}=x_{4}=0$, 则 $x_{1}=x_{3}=\frac{1}{2}$, 即得方程组的一个解

在对应的齐次线性方程组 $\left\{\begin{array}{l}x_{1}=x_{2}+x_{4}, \\ x_{3}=2 x_{4}\end{array}\right.$ 中, 取

$$
\eta^{*}=\left(\begin{array}{c}
\frac{1}{2} \\
0 \\
\frac{1}{2} \\
0
\end{array}\right)
$$

即得对应的齐次线性方程组的基础解系

$$
\left(\begin{array}{l}
x_{2} \\
x_{4}
\end{array}\right)=\left(\begin{array}{l}
1 \\
0
\end{array}\right) \text { 及 }\left(\begin{array}{l}
0 \\
1
\end{array}\right) \text {, 则 }\left(\begin{array}{l}
x_{1} \\
x_{3}
\end{array}\right)=\left(\begin{array}{l}
1 \\
0
\end{array}\right) \text { 及 }\left(\begin{array}{l}
1 \\
2
\end{array}\right) \text {, }
$$

$$
\xi_{1}=\left(\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right), \xi_{2}=\left(\begin{array}{l}
1 \\
0 \\
2 \\
1
\end{array}\right),
$$

于是所求通解为

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right)=c_{1}\left(\begin{array}{l}
1 \\
1 \\
0 \\
0
\end{array}\right)+c_{2}\left(\begin{array}{l}
1 \\
0 \\
2 \\
1
\end{array}\right)+\left(\begin{array}{c}
\frac{1}{2} \\
0 \\
\frac{1}{2} \\
0
\end{array}\right) \quad\left(c_{1}, c_{2} \in \mathbb{R}\right) .
$$

## $\S 5$ 向量空间

本章 1 中把 $n$ 维向量的全体所构成的集合 $\mathbb{R}^{n}$ 叫做 $n$ 维向量空间.下面介 绍向墨空间的有关知识.

定义 6 设 $V$ 为 $n$ 维向量的集合, 如果集合 $V$ 非空,且集合 $V$ 对于向荲的 加法及乘数两种运算封闭,那么就称集合 $V$ 为向量空间.

所谓封闭, 是指在集合 $V$ 中可以进行向量的加法及乘数两种运算. 具体地 说, 就是: 若 $a \in V, b \in V$, 则 $a+b \in V$; 若 $a \in V, \lambda \in \mathbb{R}$, 则 $\lambda a \in V$.

例 173 维向量的全体 $\mathbb{R}^{3}$, 就是一个向量空间. 因为任意两个 3 维向量之和 仍然是 3 维向量,数 $\lambda$ 乘 3 维向量也仍然是 3 维向量, 它们都属于 $\mathbb{R}^{3}$. 我们可以 用有向线段形象地表示 3 维向量, 从而向量空间 $\mathbb{R}^{3}$ 可形象地看作以坐标原点为 起点的有向线段的全体. 由于以原点为起点的有向线段与其终点一一对应, 因此 $\mathbb{R}^{3}$ 也可看作取定坐标原点的点空间.

类似地, $n$ 维向壆的全体 $\mathbb{R}^{n}$,也是一个向量空间. 不过当 $n>3$ 时,它没有直 观的几何意义.

例 18 集合

$$
V=\left\{x=\left(0, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

是一个向量空间. 因为若 $a=\left(0, a_{2}, \cdots, a_{n}\right)^{\mathrm{T}} \in V, \boldsymbol{b}=\left(0, b_{2}, \cdots, b_{n}\right)^{\mathrm{T}} \in V$, 则 $\boldsymbol{a}+\boldsymbol{b}=\left(0, a_{2}+b_{2}, \cdots, a_{n}+b_{n}\right)^{\mathrm{T}} \in V, \lambda \boldsymbol{a}=\left(0, \lambda a_{2}, \cdots, \lambda a_{n}\right)^{\mathrm{T}} \in V$.

例 19 集合

$$
V=\left\{x=\left(1, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

不是向量空间, 因为若 $a=\left(1, a_{2}, \cdots, a_{n}\right)^{\mathrm{T}} \in V$, 则

$$
2 a=\left(2,2 a_{2}, \cdots, 2 a_{n}\right)^{\mathrm{T}} \notin V .
$$

例 20 齐次线性方程组的解集

$$
S=\{\boldsymbol{x} \mid \boldsymbol{A x}=\mathbf{0}\}
$$

是一个向量空间 (称为齐次线性方程组的解空间). 因为由齐次线性方程组的解 的性质 1.2 ,即知其解集 $S$ 对向量的线性运算封闭.

例 21 非齐次线性方程组的解集

$$
S=\{\boldsymbol{x} \mid \boldsymbol{A x}=\boldsymbol{b}\}
$$

不是向量空间. 因为当 $S$ 为空集时, $S$ 不是向量空间; 当 $S$ 非空时, 若 $\boldsymbol{\eta} \in S$, 则 $\boldsymbol{A}(2 \boldsymbol{\eta})=2 \boldsymbol{b} \neq \boldsymbol{b}$, 知 $2 \boldsymbol{\eta} \notin S$.

例 22 设 $a, b$ 为两个已知的 $n$ 维向量,集合

$$
L=\{x=\lambda a+\mu b \mid \lambda, \mu \in \mathbb{R}\}
$$

是一个向量空间. 因为若 $x_{1}=\lambda_{1} a+\mu_{1} b, x_{2}=\lambda_{2} a+\mu_{2} b$, 则有

$$
\begin{gathered}
\boldsymbol{x}_{1}+\boldsymbol{x}_{2}=\left(\lambda_{1}+\lambda_{2}\right) \boldsymbol{a}+\left(\mu_{1}+\mu_{2}\right) \boldsymbol{b} \in L, \\
\dddot{k} \boldsymbol{x}_{1}=\left(k \lambda_{1}\right) \boldsymbol{a}+\left(k \mu_{1}\right) b \in L,
\end{gathered}
$$

这个向量空间称为由向量 $a, b$ 所生成的向量空间.

一般的, 由向量组 $a_{1}, a_{2} ; \cdots, a_{m}$ 所生成的向墨空间为

$$
L=\left\{x=\lambda_{1} a_{1}+\lambda_{2} a_{2}+\cdots+\lambda_{m} a_{m} \mid \lambda_{1}, \lambda_{2}, \cdots, \lambda_{m} \in \mathbb{R}\right\} .
$$

例 23 设向量组 $a_{1}, \cdots, a_{m}$ 与向量组 $b_{1}, \cdots, b$, 等价, 记

$$
L_{1}=\left\{x=\lambda_{1} a_{1}+\cdots+\lambda_{m} a_{m} \mid \lambda_{1}, \cdots, \lambda_{m} \in \mathbb{R}\right\},
$$

$$
L_{2}=\left\{x=\mu_{1} b_{1}+\cdots+\mu_{s} b_{s}\left|\mu_{1}, \cdots, \mu_{s} \in \mathbb{R}\right|,\right.
$$

试证 $L_{1}=L_{2}$.

证 设 $x \in L_{1}$, 则 $\boldsymbol{x}$ 可由 $a_{1}, \cdots, a_{m}$ 线性表示. 因 $a_{1}, \cdots, a_{m}$ 可由 $b_{1}, \cdots, b s$ 线性表示, 故 $\boldsymbol{x}$ 可由 $\boldsymbol{b}_{1}, \cdots, \boldsymbol{b}_{s}$ 线性表示, 所以 $\boldsymbol{x} \in L_{2}$. 这就是说, 若 $\boldsymbol{x} \in L_{1}$, 则 $\boldsymbol{x}$ $\in L_{2}$, 因此 $L_{1} \subset L_{2}$.

类似地可证: 若 $x \in L_{2}$, 则 $x \in L_{1}$, 因此 $L_{2} \subset L_{1}$.

因为 $L_{1} \subset L_{2}, L_{2} \subset L_{1}$, 所以 $L_{1}=L_{2}$.

定义 7 设 $V$ 为向量空间, 如果 $r$ 个向量 $a_{1}, a_{2}, \cdots, a_{r} \in V$, 且满足

(i) $a_{1}, a_{2}, \cdots, a_{r}$ 线性无关;

（ii） $V$ 中任一向量都可由 $a_{1}, a_{2}, \cdots, a_{r}$ 线性表示,

那么,向量组 $a_{1}, a_{2}, \cdots, a_{r}$ 就称为向量空间 $V$ 的一个基, $r$ 称为向量空间 $V$ 的 维数,并称 $V$ 为 $r$ 维向量空间.

如果向量空间 $V$ 没有基,那么 $V$ 的维数为 0.0 维向量空间只含一个零向 量 0.

若把向量空间 $V$ 看作向量组，则由最大无关组的等价定义可知, $V$ 的基就 是向墨组的最大无关组, $V$ 的维数就是向里组的秩.

例如, 由例 8 知, 任何 $n$ 个线性无关的 $n$ 维向量都可以是向量空间 $\mathbb{R}^{n}$ 的一 个基,且由此可知 $\mathbb{R}^{n}$ 的维数为 $n$. 所以我们把 $\mathbb{R}^{n}$ 称为 $n$ 维向量空间.

又如,向墨空间

$$
V=\left\{\boldsymbol{x}=\left(0, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

的一个基可取为: $e_{2}=(0,1,0, \cdots, 0)^{\mathrm{T}}, \cdots, e_{n}=(0, \cdots, 0,1)^{\mathrm{T}}$. 并由此可知它是 $n-1$ 维向量空间.

由向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 所生成的向量空间

$$
L=\left\{x=\lambda_{1} a_{1}+\lambda_{2} a_{2}+\cdots+\lambda_{m} a_{m} \mid \lambda_{1}, \lambda_{2}, \cdots, \lambda_{m} \in \mathbb{R}\right\},
$$

显然向量空间 $L$ 与向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 等价,所以向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 的最 大无关组就是 $L$ 的一个基, 向晴组 $a_{1}, a_{2}, \cdots, a_{m}$ 的秩就是 $L$ 的维数.

若向量组 $\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \cdots, \boldsymbol{a}_{r}$ 是向量空间 $V$ 的一个基,则 $V$ 可表示为

$$
V=\left\{x=\lambda_{1} a_{1}+\cdots+\lambda_{r} a_{r}\left|\lambda_{1}, \cdots, \lambda_{r} \in \mathbb{R}\right|,\right.
$$

即 $V$ 是基所生成的向墨空间,这就较清楚地显示出向量空间 $V$ 的构造.

例如齐次线性方程组的解空间 $S=\{\boldsymbol{x} \mid \boldsymbol{A x}=\mathbf{0}\}$, 若能找到解空间的一个基 $\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}, \cdots, \boldsymbol{\xi}_{n-r}$, 则解空间可表示为

$$
S=\left\{x=c_{1} \xi_{1}+c_{2} \xi_{2}+\cdots+c_{n-r} \xi_{n-r} \mid c_{1}, c_{2}, \cdots, c_{n-r} \in \mathbb{R}\right\} .
$$

定义 8 如果在向墨空间 $V$ 中取定一个基 $a_{1}, a_{2}, \cdots, a_{r}$, 那么 $V$ 中任一向 量 $\boldsymbol{x}$ 可惟一地表示为

$$
\boldsymbol{x}=\lambda_{1} a_{1}+\lambda_{2} a_{2}+\cdots+\lambda_{r} a_{r},
$$

数组 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{r}$ 称为向量 $\boldsymbol{x}$ 在基 $a_{1}, a_{2}, \cdots, a_{r}$ 中的坐标.

特别地, 在 $n$ 维向量空间 $\mathbb{R}^{n}$ 中取单位坐标向照组 $e_{1}, e_{2}, \cdots, e_{n}$ 为基, 则以 $x_{1}, x_{2}, \cdots, x_{n}$ 为分量的向量 $x$, 可表示为

$$
x=x_{1} e_{1}+x_{2} e_{2}+\cdots+x_{n} e_{n},
$$

可见向量在基 $e_{1}, e_{2}, \cdots, e_{n}$ 中的坐标就是该向量的分量. 因此, $e_{1}, e_{2}, \cdots, e_{n}$ 叫 做 $\mathbb{R}^{n}$ 中的息然基.

例 24 设 $A=\left(a_{1}, a_{2}, a_{3}\right)=\left(\begin{array}{rrr}2 & 2 & -1 \\ 2 & -1 & 2 \\ -1 & 2 & 2\end{array}\right)$,

$$
B=\left(b_{1}, b_{2}\right)=\left(\begin{array}{rr}
1 & 4 \\
0 & 3 \\
-4 & 2
\end{array}\right) \text {. }
$$

验证 $a_{1}, a_{2}, a_{3}$ 是 $\mathbb{R}^{3}$ 的一个基,并求 $b_{1}, b_{2}$ 在这个基中的坐标.

解 要证 $a_{1}, a_{2}, a_{3}$ 是 $\mathbb{R}^{3}$ 的一个基, 只要证 $a_{1}, a_{2}, a_{3}$ 线性无关, 即只要证 $\boldsymbol{A} \sim \boldsymbol{E}$.

设 $b_{1}=x_{11} a_{1}+x_{21} a_{2}+x_{31} a_{3}, b_{2}=x_{12} a_{1}+x_{22} a_{2}+x_{32} a_{3}$ 即

$$
\left(b_{1}, b_{2}\right)=\left(a_{1}, a_{2}, a_{3}\right)\left(\begin{array}{ll}
x_{11} & x_{12} \\
x_{21} & x_{22} \\
x_{31} & x_{32}
\end{array}\right) \text {, 记作 } \boldsymbol{B}=\boldsymbol{A X} \text {. }
$$

对矩阵 $(A, B)$ 施行初等行变换, 若 $A$ 能变为 $E$, 则 $a_{1}, a_{2}, a_{3}$ 为 $\mathbb{R}^{3}$ 的一个 基,且当 $\boldsymbol{A}$ 变为 $E$ 时, $B$ 变为 $X=A^{-1} B$.

$$
\begin{gathered}
(\boldsymbol{A}, \boldsymbol{B})=\left(\begin{array}{rrrrr}
2 & 2 & -1 & 1 & 4 \\
2 & -1 & 2 & 0 & 3 \\
-1 & 2 & 2 & -4 & 2
\end{array}\right) \frac{\frac{1}{3}\left(r_{1}+r_{2}+r_{3}\right)}{\frac{r_{2}-2 r_{1}}{r_{3}+r_{1}}}\left(\begin{array}{rrrrr}
1 & 1 & 1 & -1 & 3 \\
0 & -3 & 0 & 2 & -3 \\
0 & 3 & 3 & -5 & 5
\end{array}\right) \\
\frac{r_{2} \div(-3)}{r_{3} \div 3}\left(\begin{array}{rrrrr}
1 & 1 & 1 & -1 & 3 \\
0 & 1 & 0 & -\frac{2}{3} & 1 \\
0 & 1 & 1 & -\frac{5}{3} & \frac{5}{3}
\end{array}\right){ }_{\frac{r_{1}-r_{3}}{r_{3}-r_{2}}}\left(\begin{array}{llllll}
1 & 0 & 0 & \frac{2}{3} & \frac{4}{3} \\
0 & 1 & 0 & -\frac{2}{3} & 1 \\
0 & 0 & 1 & -1 & \frac{2}{3}
\end{array}\right) .
\end{gathered}
$$

因有 $\boldsymbol{A} \sim \boldsymbol{E}$, 故 $\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{3}$ 为 $\mathbb{R}^{3}$ 的一个基,且

$$
\left(b_{1}, b_{2}\right)=\left(a_{1}, a_{2}, a_{3}\right)\left(\begin{array}{rr}
\frac{2}{3} & \frac{4}{3} \\
-\frac{2}{3} & 1 \\
-1 & \frac{2}{3}
\end{array}\right),
$$

即 $b_{1}, b_{2}$ 在基 $a_{1}, a_{2}, a_{3}$ 中的坐标依次为

$$
\frac{2}{3},-\frac{2}{3},-1 \text { 和 } \frac{4}{3}, 1, \frac{2}{3} \text {. }
$$

例 25 在 $\mathbb{R}^{3}$ 中取定一个基 $a_{1}, a_{2}, a_{3}$, 再取一个新基 $b_{1}, b_{2}, b_{3}$, 设 $A=$ $\left(a_{1}, a_{2}, a_{3}\right), B=\left(b_{1}, b_{2}, b_{3}\right)$. 求用 $a_{1}, a_{2}, a_{3}$ 表示 $b_{1}, b_{2}, b_{3}$ 的表示式(基变换 公式),并求向量在两个基中的坐标之间的关系式(坐㷊恋换公式).

解

$$
\left(a_{1}, a_{2}, a_{3}\right)=\left(e_{1}, e_{2}, e_{3}\right) A, \quad\left(e_{1}, e_{2}, e_{3}\right)=\left(a_{1}, a_{2}, a_{3}\right) A^{-1} \text {. }
$$

故

$$
\left(b_{1}, b_{2}, b_{3}\right)=\left(e_{1}, e_{2}, e_{3}\right) B=\left(a_{1}, a_{2}, a_{3}\right) A^{-1} B \text {, }
$$

即基变换公式为

$$
\left(b_{1}, b_{2}, b_{3}\right)=\left(a_{1}, a_{2}, a_{3}\right) P,
$$

其中表示式的系数矩阵 $\boldsymbol{P}=\boldsymbol{A}^{-1} \boldsymbol{B}$ 称为从旧基到新基的过洨聟阵.

设向量 $x$ 在旧基和新基中的坐标分别为 $y_{1}, y_{2}, y_{3}$ 和 $z_{1}, z_{2}, z_{3}$, 即

$$
\boldsymbol{x}=\left(\boldsymbol{a}_{1}, \boldsymbol{a}_{2}, \boldsymbol{a}_{3}\right)\left(\begin{array}{l}
y_{1} \\
y_{2} \\
y_{3}
\end{array}\right), \quad \boldsymbol{x}=\left(\boldsymbol{b}_{1}, \boldsymbol{b}_{2}, \boldsymbol{b}_{3}\right)\left(\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right),
$$

故

$$
\boldsymbol{A}\left(\begin{array}{l}
y_{1} \\
y_{2} \\
y_{3}
\end{array}\right)=\boldsymbol{B}\left(\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right) \text {, 得 } \quad\left(\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right)=\boldsymbol{B}^{-1} \boldsymbol{A}\left(\begin{array}{l}
y_{1} \\
y_{2} \\
y_{3}
\end{array}\right) \text {, }
$$

即

$$
\left(\begin{array}{l}
z_{1} \\
z_{2} \\
z_{3}
\end{array}\right)=\boldsymbol{P}^{-1}\left(\begin{array}{l}
y_{1} \\
y_{2} \\
y_{3}
\end{array}\right) \text {, }
$$

这就是从旧坐标到新坐标的坐标变换公式.

## 习 题 四

$$
A: a_{1}=\left(\begin{array}{l}
0 \\
1 \\
2 \\
3
\end{array}\right), a_{2}=\left(\begin{array}{l}
3 \\
0 \\
1 \\
2
\end{array}\right), a_{3}=\left(\begin{array}{l}
2 \\
3 \\
0 \\
1
\end{array}\right) ; B: b_{1}=\left(\begin{array}{l}
2 \\
1 \\
1 \\
2
\end{array}\right), b_{2}=\left(\begin{array}{r}
0 \\
-2 \\
1 \\
1
\end{array}\right), b_{3}=\left(\begin{array}{l}
4 \\
4 \\
1 \\
3
\end{array}\right),
$$

证明 $B$ 组能由 $A$ 组线性表示, 但 $A$ 组不能由 $B$ 组线性表示.

2. 已知向些组

$$
A: a_{1}=\left(\begin{array}{l}
0 \\
1 \\
1
\end{array}\right), a_{2}=\left(\begin{array}{l}
1 \\
1 \\
0
\end{array}\right) ; \quad B: b_{1}=\left(\begin{array}{r}
-1 \\
0 \\
1
\end{array}\right), b_{2}=\left(\begin{array}{l}
1 \\
2 \\
1
\end{array}\right), b_{3}=\left(\begin{array}{r}
3 \\
2 \\
-1
\end{array}\right) \text {, }
$$

证明 $A$ 组与 $B$ 组等价.

3. 已知 $R\left(a_{1}, a_{2}, a_{3}\right)=2, R\left(a_{2}, a_{3}, a_{4}\right)=3$, 证明

(1) $a_{1}$ 能由 $a_{2}, a_{3}$ 线性表示;

（2） $a_{4}$ 不能由 $a_{1}, a_{2}, a_{3}$ 线性表示.

4. 判定下列向些组是线性相关还是线性无关:
(1) $\left(\begin{array}{r}-1 \\ 3 \\ 1\end{array}\right),\left(\begin{array}{l}2 \\ 1 \\ 0\end{array}\right),\left(\begin{array}{l}1 \\ 4 \\ 1\end{array}\right)$;
(2) $\left(\begin{array}{l}2 \\ 3 \\ 0\end{array}\right),\left(\begin{array}{r}-1 \\ 4 \\ 0\end{array}\right),\left(\begin{array}{l}0 \\ 0 \\ 2\end{array}\right)$.
5. 问 $a$ 取什么值时下列向基组线性相关?

$$
a_{1}=\left(\begin{array}{l}
a \\
1 \\
1
\end{array}\right), a_{2}=\left(\begin{array}{r}
1 \\
a \\
-1
\end{array}\right), a_{3}=\left(\begin{array}{r}
1 \\
-1 \\
a
\end{array}\right) .
$$

6. 设 $a_{1}, a_{2}$ 线性无关, $a_{1}+b, a_{2}+b$ 线性相关, 求向䭪 $b$ 用 $a_{1}, a_{2}$ 线性表示的表示式.
7. 设 $a_{1}, a_{2}$ 线性相关, $b_{1}, b_{2}$ 也线性相关, 问 $a_{1}+b_{1}, a_{2}+b_{2}$ 是否一定线性相关? 试举 例说明之.
8. 举例说明下列各命题是错误的:

（1）若向俥组 $a_{1}, a_{2}, \cdots, a_{m}$ 是线性相关的,则 $a_{1}$ 可由 $a_{2}, \cdots, a_{m}$ 线性表示.

(2) 若有不全为 0 的数 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$, 使

$$
\lambda_{1} a_{1}+\cdots+\lambda_{m} a_{m}+\lambda_{1} b_{1}+\cdots+\lambda_{m} b_{m}=0
$$

成立, 则 $a_{1}, \cdots, a_{m}$ 线性相关, $b_{1}, \cdots, b_{m}$ 亦线性相关.

(3) 若只有当 $\lambda_{1}, \cdots, \lambda_{m}$ 全为 0 时, 等式

$$
\lambda_{1} a_{1}+\cdots+\lambda_{m} a_{m}+\lambda_{1} b_{1}+\cdots+\lambda_{m} b_{m}=0
$$

才能成立, 则 $\boldsymbol{a}_{1}, \cdots, \boldsymbol{a}_{m}$ 线性无关, $\boldsymbol{b}_{1}, \cdots, \boldsymbol{b}_{m}$ 亦线性无关.

（4）若 $a_{1}, \cdots, a_{m}$ 线性相关, $b_{1}, \cdots, b_{m}$ 亦线性相关, 则有不全为 0 的数 $\lambda_{1}, \cdots, \lambda_{m}$, 使

$$
\lambda_{1} a_{1}+\cdots+\lambda_{m} a_{m}=0, \lambda_{1} b_{1}+\cdots+\lambda_{m} b_{m}=0
$$

同时成立.

9. 设 $b_{1}=a_{1}+a_{2}, b_{2}=a_{2}+a_{3}, b_{3}=a_{3}+a_{4}, b_{4}=a_{4}+a_{1}$, 证明向些组 $b_{1}, b_{2}, b_{3}, b_{4}$ 线 性相关. 10. 设 $b_{1}=a_{1}, b_{2}=a_{1}+a_{2}, \cdots, b_{r}=a_{1}+a_{2}+\cdots+a_{r}$, 且向望组 $a_{1}, a_{2}, \cdots, a_{r}$ 线性无 关，证明向量组 $b_{1}, b_{2}, \cdots, b_{r}$ 线性无关.
10. 求下列向望组的秩,并求一个最大无关组:

$$
\begin{aligned}
& \text { (1) } a_{1}=\left(\begin{array}{r}
1 \\
2 \\
-1 \\
4
\end{array}\right), a_{2}=\left(\begin{array}{c}
9 \\
100 \\
10 \\
4
\end{array}\right), a_{3}=\left(\begin{array}{r}
-2 \\
-4 \\
2 \\
-8
\end{array}\right) ; \\
& \text { (2) } a_{1}=\left(\begin{array}{l}
1 \\
2 \\
1 \\
3
\end{array}\right), a_{2}=\left(\begin{array}{r}
4 \\
-1 \\
-5 \\
-6
\end{array}\right), a_{3}=\left(\begin{array}{r}
1 \\
-3 \\
-4 \\
-7
\end{array}\right) .
\end{aligned}
$$

12. 利用初等行变换求下列矩阵的列向量组的一个最大无关组,并把其余列向些用最大 无关组线性表示:

(1) $\left(\begin{array}{rrrr}25 & 31 & 17 & 43 \\ 75 & 94 & 53 & 132 \\ 75 & 94 & 54 & 134 \\ 25 & 32 & 20 & 48\end{array}\right)$; (2) $\left(\begin{array}{rrrrr}1 & 1 & 2 & 2 & 1 \\ 0 & 2 & 1 & 5 & -1 \\ 2 & 0 & 3 & -1 & 3 \\ 1 & 1 & 0 & 4 & -1\end{array}\right)$.

13. 设向量组

$$
\left(\begin{array}{l}
a \\
3 \\
1
\end{array}\right),\left(\begin{array}{l}
2 \\
b \\
3
\end{array}\right),\left(\begin{array}{l}
1 \\
2 \\
1
\end{array}\right),\left(\begin{array}{l}
2 \\
3 \\
1
\end{array}\right)
$$

的秩为 2 , 求 $a, b$.

14. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是一组 $n$ 维向理,已知 $n$ 维单位坐标向量 $e_{1}, e_{2}, \cdots, e_{n}$ 能由它们线 性表示, 证明 $a_{1}, a_{2}, \cdots, a_{n}$ 线性无关.
15. 设 $a_{1}, a_{2}, \cdots, a_{n}$ 是一组 $n$ 维向量,证明它们线性无关的充分必要条件是: 任一 $n$ 维 向量都可由它们线性表示.
16. 设向量组 $a_{1}, a_{2}, \cdots, a_{m}$ 线性相关, 且 $a_{1} \neq \mathbf{0}$, 证明存在某个向量 $\boldsymbol{a}_{k}(2 \leqslant k \leqslant m)$, 使 $a_{k}$ 能由 $a_{1}, \cdots, a_{k-1}$ 线性表示.
17. 设向量组 $B: b_{1}, \cdots, b_{r}$ 能由向量组 $A: a_{1}, \cdots, a_{s}$ 线性表示为

$$
\left(b_{1}, \cdots, b_{r}\right)=\left(a_{1}, \cdots, a_{s}\right) K,
$$

其中 $\boldsymbol{K}$ 为 $s \times r$ 矩阵, 且 $A$ 组线性无关. 证明 $B$ 组线性无关的充分必要条件是矩阵 $\boldsymbol{K}$ 的秩 $R(\boldsymbol{K})=r$.

18. 设 $\left\{\begin{array}{l}\beta_{1}=\quad \alpha_{2}+\alpha_{3}+\cdots+\alpha_{n}, \\ \beta_{2}=\alpha_{1} \quad+\alpha_{3}+\cdots+\alpha_{n}, \\ \cdots \cdots \cdots \cdots \\ \beta_{n}=\alpha_{1}+\alpha_{2}+\cdots+\alpha_{n-1},\end{array}\right.$ 证明向郍组 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 与向但组 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}$ 等价.
19. 已知 3 阶矩阵 $A$ 与 3 维列向垭 $x$ 满足 $A^{3} x=3 A x-A^{2} x$, 且向然组 $x, A x, A^{2} x$ 线性 无关:

(1) 记 $y=A x, z=A y, P=(x, y, z)$, 求 3 阶矩阵 $\boldsymbol{B}$, 使 $A P=P B$; (2) 求 $|\boldsymbol{A}|$.

20. 求下列齐次线性方程组的基础解系:

(1) $\left\{\begin{aligned} x_{1}-8 x_{2}+10 x_{3}+2 x_{4}=0, \\ 2 x_{1}+4 x_{2}+5 x_{3}-x_{4}=0, \\ 3 x_{1}+8 x_{2}+6 x_{3}-2 x_{4}=0 ;\end{aligned}\right.$ （2) $\left\{\begin{array}{l}2 x_{1}-3 x_{2}-2 x_{3}+x_{4}=0, \\ 3 x_{1}+5 x_{2}+4 x_{3}-2 x_{4}=0, \\ 8 x_{1}+7 x_{2}+6 x_{3}-3 x_{4}=0 ;\end{array}\right.$

(3) $n x_{1}+(n-1) x_{2}+\cdots+2 x_{n-1}+x_{n}=0$.

21. 设 $\boldsymbol{A}=\left(\begin{array}{llll}2 & -2 & 1 & 3 \\ 9 & -5 & 2 & 8\end{array}\right)$, 求一个 $4 \times 2$ 矩阵 $\boldsymbol{B}$, 使 $\boldsymbol{A B}=\boldsymbol{O}$, 且 $R(\boldsymbol{B})=2$.
22. 求一个齐次线性方程组,使它的基础解系为

$$
\xi_{1}=(0,1,2,3)^{\mathrm{T}}, \xi_{2}=(3,2,1,0)^{\mathrm{T}} .
$$

23. 设四元齐次线性方程组

$$
\mathrm{I}:\left\{\begin{array}{l}
x_{1}+x_{2}=0, \\
x_{2}-x_{4}=0 ;
\end{array} \quad \text { II }:\left\{\begin{array}{l}
x_{1}-x_{2}+x_{3}=0, \\
x_{2}-x_{3}+x_{4}=0,
\end{array}\right.\right.
$$

求: (1)方程组 I 与 II 的基础解系; (2) I 与 II 的公共解.

24. 设 $n$ 阶矩阵 $\boldsymbol{A}$ 满足 $\boldsymbol{A}^{2}=\boldsymbol{A}, \boldsymbol{E}$ 为 $n$ 阶单位阵, 证明

$$
R(\boldsymbol{A})+R(\boldsymbol{A}-\boldsymbol{E})=n \text {. }
$$

提示: 利用矩阵的性质 6 和 8 .

25. 设 $\boldsymbol{A}$ 为 $n$ 阶矩阵 $(n \geqslant 2), \boldsymbol{A}^{*}$ 为 $\boldsymbol{A}$ 的伴随阵, 证明

$$
R\left(\boldsymbol{A}^{*}\right)= \begin{cases}n, & \text { 当 } R(\boldsymbol{A})=n, \\ 1, & \text { 当 } R(\boldsymbol{A})=n-1, \\ 0, & \text { 当 } R(\boldsymbol{A}) \leqslant n-2 .\end{cases}
$$

26. 求下列非齐次方程组的一个解及对应的齐次方程组的基础解系:

$$
\text { (1) }\left\{\begin{array} { r l } 
{ x _ { 1 } + x _ { 2 } } & { = 5 , } \\
{ 2 x _ { 1 } + x _ { 2 } + x _ { 3 } + 2 x _ { 4 } } & { = 1 , } \\
{ 5 x _ { 1 } + 3 x _ { 2 } + 2 x _ { 3 } + 2 x _ { 4 } } & { = 3 ; }
\end{array} \text { ; } \left\{\begin{array}{rl}
x_{1}-5 x_{2}+2 x_{3}-3 x_{4} & =11, \\
5 x_{1}+3 x_{2}+6 x_{3}-x_{4} & =-1, \\
2 x_{1}+4 x_{2}+2 x_{3}+x_{4} & =-6 .
\end{array}\right.\right.
$$

27. 设四元非齐次线性方程组的系数矩阵的秩为 3 , 已知 $\eta_{1}, \eta_{2}, \eta_{3}$ 是它的三个解向贯,且

$$
\eta_{1}=\left(\begin{array}{l}
2 \\
3 \\
4 \\
5
\end{array}\right), \eta_{2}+\eta_{3}=\left(\begin{array}{l}
1 \\
2 \\
3 \\
4
\end{array}\right),
$$

求该方程组的通解.

28. 设有向量组 $A: a_{1}=\left(\begin{array}{c}\alpha \\ 2 \\ 10\end{array}\right), a_{2}=\left(\begin{array}{r}-2 \\ 1 \\ 5\end{array}\right), a_{3}=\left(\begin{array}{r}-1 \\ 1 \\ 4\end{array}\right)$, 及向些 $b=\left(\begin{array}{r}1 \\ \beta \\ -1\end{array}\right)$, 问 $\alpha, \beta$ 为 何值时： (1) 向些 $b$ 不能由向盘组 $A$ 线性表示;

(2) 向辇 $b$ 能由向些组 $A$ 线性表示,且表示式倠一;

（3）向量 $\boldsymbol{b}$ 能由向然组 $\boldsymbol{A}$ 线性表示,且表示式不惟一,并求一般表示式.

29. 设

$$
\boldsymbol{a}=\left(\begin{array}{l}
a_{1} \\
a_{2} \\
a_{3}
\end{array}\right), \boldsymbol{b}=\left(\begin{array}{l}
b_{1} \\
b_{2} \\
b_{3}
\end{array}\right), \boldsymbol{c}=\left(\begin{array}{l}
c_{1} \\
c_{2} \\
c_{3}
\end{array}\right)
$$

相交于一点的充分必要条件为: 向量组 $\boldsymbol{a}, \boldsymbol{b}$ 线珄无关,且向坦组 $\boldsymbol{a}, \boldsymbol{b}, \boldsymbol{c}$ 线性相关.

30. 设矩阵 $A=\left(a_{1}, a_{2}, a_{3}, a_{4}\right)$, 其中 $a_{2}, a_{3}, a_{4}$ 线性无关, $a_{1}=2 a_{2}-a_{3}$. 向量 $b=a_{1}+$ $a_{2}+a_{3}+a_{4}$, 求方程 $A x=b$ 的通解.

的一个基础解系.证明:

(1) $\boldsymbol{\eta}^{*}, \boldsymbol{\xi}_{1}, \cdots, \boldsymbol{\xi}_{n-r}$ 线性无关;

(2) $\boldsymbol{\eta}^{*}, \boldsymbol{\eta}^{*}+\boldsymbol{\xi}_{1}, \cdots, \boldsymbol{\eta}^{*}+\boldsymbol{\xi}_{n-r}$ 线性无关.

$+\cdots+k_{s}=1$. 证明

$$
\boldsymbol{x}=k_{1} \boldsymbol{\eta}_{1}+k_{2} \boldsymbol{\eta}_{2}+\cdots+k_{s} \boldsymbol{\eta}_{s}
$$

也是它的解.

33. 设非齐次线性方程组 $\boldsymbol{A x}=\boldsymbol{b}$ 的系数矩阵的秩为 $r, \boldsymbol{\eta}_{1}, \cdots, \boldsymbol{\eta}_{n-r+1}$ 是它的 $n-r+1$ 个线性无关的解 (由题 31 知它确有 $n-r+1$ 个线性无关的解). 试证它的任一解可表示为

$$
\boldsymbol{x}=k_{1} \boldsymbol{\eta}_{1}+\cdots+k_{n-r+1} \boldsymbol{\eta}_{n-r+1} \quad \text { (其中 } k_{1}+\cdots+k_{n-r+1}=1 \text { ). }
$$

34. 设 $V_{1}=\left\{\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{1}, \cdots, x_{n} \in \mathbb{R}\right.$ 满足 $\left.x_{1}+\cdots+x_{n}=0\right\}$,

$$
V_{2}=\left\{x=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{1}, \cdots, x_{n} \in \mathbb{R} \text { 满足 } x_{1}+\cdots+x_{n}=1\right\} \text { ， }
$$

问 $V_{1}, V_{2}$ 是不是向舟空间? 为什么?

35. 试证由 $a_{1}=(0,1,1)^{\mathrm{T}}, a_{2}=(1,0,1)^{\mathrm{T}}, a_{3}=(1,1,0)^{\mathrm{T}}$ 所生成的向椠空间就是 $\mathbb{R}^{3}$.
36. 由 $a_{1}=(1,1,0,0)^{\mathrm{T}}, a_{2}=(1,0,1,1)^{\mathrm{T}}$ 所生成的向些空间记作 $L_{1}$, 由 $b_{1}=(2,-1,3$, $3)^{\mathrm{T}}, \boldsymbol{b}_{2}=(0,1,-1,-1)^{\mathrm{T}}$ 所生成的向提空间记作 $L_{2}$, 试证 $L_{1}=L_{2}$.
37. 验证 $a_{1}=(1,-1,0)^{\top}, a_{2}=(2,1,3)^{\mathrm{\top}}, a_{3}=(3,1,2)^{\top}$ 为 $\mathbb{R}^{3}$ 的一个基, 并把 $v_{1}=(5,0$, $7)^{\mathrm{T}}, v_{2}=(-9,-8,-13)^{\mathrm{T}}$ 用这个基线性表示.
38. 已知 $\mathbb{R}^{3}$ 的两个基为

$$
a_{1}=\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right), a_{2}=\left(\begin{array}{r}
1 \\
0 \\
-1
\end{array}\right), a_{3}=\left(\begin{array}{l}
1 \\
0 \\
1
\end{array}\right) \text { 及 } b_{1}=\left(\begin{array}{l}
1 \\
2 \\
1
\end{array}\right), b_{2}=\left(\begin{array}{l}
2 \\
3 \\
4
\end{array}\right), b_{3}=\left(\begin{array}{l}
3 \\
4 \\
3
\end{array}\right),
$$

求由基 $a_{1}, a_{2}, a_{3}$ 到基 $b_{1}, b_{2}, b_{3}$ 的过䜤矩阵 $P$.

## 第五章 <br> 相似矩阵及二次型

本章主要讨论方阵的特征值与特征向量、方阵的相似对角化和二次型的化 简等问题. 其中涉及向量的内积、长度及正交等知识,下面先介绍这些知识.

## $\S 1$ 向量的内积、长度及正交性

定义 1 设有 $n$ 维向量

$$
\boldsymbol{x}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right), \boldsymbol{y}=\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right),
$$

令

$$
[\boldsymbol{x}, \boldsymbol{y}]=x_{1} y_{1}+x_{2} y_{2}+\cdots+x_{n} y_{n},
$$

$[\boldsymbol{x}, \boldsymbol{y}]$ 称为向量 $\boldsymbol{x}$ 与 $\boldsymbol{y}$ 的内积.

内积是两个向量之间的一种运算,其结果是一个实数,用矩阵记号表示, 当 $x$ 与 $y$ 都是列向量时,有

$$
[x, y]=x^{\top} y .
$$

内积具有下列性质 (其中 $x, y, z$ 为 $n$ 维向量, $\lambda$ 为实数):

(i) $[\boldsymbol{x}, \boldsymbol{y}]=[\boldsymbol{y}, \boldsymbol{x}]$;

(ii) $[\lambda x, y]=\lambda[x, y]$;

(iii) $[x+y, z]=[x, z]+[y, z]$;

(iv) 当 $x=0$ 时, $[x, x]=0$; 当 $x \neq 0$ 时, $[x, x]>0$.

这些性质可根据内积定义直接证明, 请读者给出相关证明.利用这些性质, 还可证明施瓦茨(Schwarz)不等式 (这里不证)

$$
[x, y]^{2} \leqslant[x, x][y, y] .
$$

在解析几何中,我们曾引进向量的数量积

$$
\boldsymbol{x} \cdot \boldsymbol{y}=|\boldsymbol{x}||\boldsymbol{y}| \cos \theta,
$$

且在直角坐标系中, 有

$$
\left(x_{1}, x_{2}, x_{3}\right) \cdot\left(y_{1}, y_{2}, y_{3}\right)=x_{1} y_{1}+x_{2} y_{2}+x_{3} y_{3},
$$

$n$ 维向量的内积是数量积的一种推广. 但 $n$ 维向量没有 3 维向量那样直观的长 度和夹角的概念, 因此只能按数量积的直角坐标计算公式来推广. 并且反过来, 利用内积来定义 $n$ 维向量的长度和夹角:

定义 2 令

$$
\|\boldsymbol{x}\|=\sqrt{[\boldsymbol{x}, \boldsymbol{x}]}=\sqrt{x_{1}^{2}+x_{2}^{2}+\cdots+x_{n}^{2}},
$$

$\|\boldsymbol{x}\|$ 称为 $n$ 维向量 $\boldsymbol{x}$ 的长度(或范数).

当 $\|\boldsymbol{x}\|=1$ 时,称 $x$ 为单位向量.

向䭪的长度具有下述性质:

(i) 非负性 当 $x \neq 0$ 时, $\|x\|>0$; 当 $x=0$ 时, $\|x\|=0$;

(ii) 齐次性 $\|\lambda \boldsymbol{x}\|=|\lambda|\|\boldsymbol{x}\|$;

(iii) 三角不等式 $\|x+y\| \leqslant\|x\|+\|y\|$.

证 (i) 与 (ii) 是显然的,下面证明 (iii).

$$
\|x+y\|^{2}=[x+y, x+y]=[x, x]+2[x, y]+[y, y],
$$

由施瓦茨不等式,有

$$
[x, y] \leqslant \sqrt{[x, x][y, y]},
$$

从而 $\|x+y\|^{2} \leqslant[x, x]+2 \sqrt{[x, x][y, y]}+[y, y]$

$$
=\|x\|^{2}+2\|x\|\|y\|+\|y\|^{2}=(\|x\|+\|y\|)^{2},
$$

即

$$
\|x+y\| \leqslant\|x\|+\|y\| \text {. }
$$

证毕

由施瓦茨不等式,有

$$
|[x, y]| \leqslant\|x\|\|y\|,
$$

故

$$
\left|\frac{[x, y]}{\|x\|\|y\|}\right| \leqslant 1 \quad \text { (当 }\|x\|\|y\| \neq 0 \text { 时), }
$$

于是有下面的定义:

当 $x \neq 0, y \neq 0$ 时,

$$
\theta=\arccos \frac{[x, y]}{\|x\|\|y\|}
$$

称为 $n$ 维向量 $\boldsymbol{x}$ 与 $\boldsymbol{y}$ 的夹角.

当 $[x, y]=0$ 时,称向量 $x$ 与 $y$ 正交. 显然, 若 $x=0$, 则 $x$ 与任何向量都 正交.

下面讨论正交向量组的性质.所谓正交向量组,是指一组两两正交的非零 向量.

定理 1 若 $n$ 维向貫 $a_{1}, a_{2}, \cdots, a_{r}$ 是一组两两正交的非零向望, 则 $a_{1}$, $a_{2}, \cdots, a_{r}$ 线性无关.

证 设有 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{r}$ 使

$$
\lambda_{1} a_{1}+\lambda_{2} a_{2}+\cdots+\lambda_{r} a_{r}=0,
$$

以 $\boldsymbol{a}_{1}^{\mathrm{T}}$ 左乘上式两端, 因当 $i \geqslant 2$ 时, $\boldsymbol{a}_{1}^{\mathrm{T}} \boldsymbol{a}_{i}=0$, 故得

$$
\lambda_{1} a_{1}^{\mathrm{T}} a_{1}=0,
$$

因 $a_{1} \neq 0$, 故 $a_{1}^{\mathrm{T}} a_{1}=\left\|a_{1}\right\|^{2} \neq 0$, 从而必有 $\lambda_{1}=0$. 类似可证 $\lambda_{2}=0, \cdots, \lambda_{r}=0$. 于是向量组 $a_{1}, a_{2}, \cdots, a_{r}$ 线性无关.

例 1 已知 3 维向量空间 $\mathbb{R}^{3}$ 中两个向量

$$
a_{1}=\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right), a_{2}=\left(\begin{array}{r}
1 \\
-2 \\
1
\end{array}\right)
$$

正交,试求一个非零向量 $a_{3}$, 使 $a_{1}, a_{2}, a_{3}$ 两两正交.

$$
\text { 解 记 } A=\left(\begin{array}{l}
a_{1}^{\top} \\
a_{2}^{\mathrm{T}}
\end{array}\right)=\left(\begin{array}{rrr}
1 & 1 & 1 \\
1 & -2 & 1
\end{array}\right) \text {, }
$$

$a_{3}$ 应满足齐次线性方程 $A x=0$, 即

$$
\left(\begin{array}{rrr}
1 & 1 & 1 \\
1 & -2 & 1
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right)=\left(\begin{array}{l}
0 \\
0
\end{array}\right)
$$

由

$$
\boldsymbol{A} \sim\left(\begin{array}{rrr}
1 & 1 & 1 \\
0 & -3 & 0
\end{array}\right) \sim\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 0
\end{array}\right)
$$

得 $\left\{\begin{array}{l}x_{1}=-x_{3} \\ x_{2}=0\end{array}\right.$,从而有基础解系 $\left(\begin{array}{r}-1 \\ 0 \\ 1\end{array}\right)$. 取 $a_{3}=\left(\begin{array}{r}-1 \\ 0 \\ 1\end{array}\right)$ 即合所求.

定义 3 设 $n$ 维向量 $e_{1}, e_{2}, \cdots, e_{r}$ 是向空间 $V\left(V \subset \mathbb{R}^{n}\right)$ 的一个基, 如果 $e_{1}, \cdots, e_{r}$ 两两正交,且都是单位向盟,则称 $e_{1}, \cdots, e_{r}$ 是 $V$ 的一个规范正交基.

例如 $\quad e_{1}=\left(\begin{array}{c}\frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}} \\ 0 \\ 0\end{array}\right), \quad e_{2}=\left(\begin{array}{c}\frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}} \\ 0 \\ 0\end{array}\right), \quad e_{3}=\left(\begin{array}{c}0 \\ 0 \\ \frac{1}{\sqrt{2}} \\ \frac{1}{\sqrt{2}}\end{array}\right), \quad e_{4}=\left(\begin{array}{c}0 \\ 0 \\ \frac{1}{\sqrt{2}} \\ -\frac{1}{\sqrt{2}}\end{array}\right)$

就是 $\mathbb{R}^{4}$ 的一个规范正交基.

若 $e_{1}, \cdots, e_{r}$ 是 $V$ 的一个规范正交基,那么 $V$ 中任一向量 $a$ 应能由 $e_{1}, \cdots$, $e_{r}$ 线性表示, 设表示式为

$$
a=\lambda_{1} e_{1}+\lambda_{2} e_{2}+\cdots+\lambda_{r} e_{r},
$$

为求其中的系数 $\lambda_{i}(i=1, \cdots, r)$, 可用 $\boldsymbol{e}_{i}^{\mathrm{T}}$ 左乘上式, 有 即

$$
\begin{gathered}
\boldsymbol{e}_{i}^{\mathrm{T}} \boldsymbol{a}=\lambda_{i} \boldsymbol{e}_{i}^{\mathrm{T}} \boldsymbol{e}_{i}=\lambda_{i}, \\
\lambda_{i}=\boldsymbol{e}_{i}^{\mathrm{T}} a=\left[\boldsymbol{a}, \boldsymbol{e}_{i}\right],
\end{gathered}
$$

这就是向量在规范正交基中的坐标的计算公式.利用这个公式能方便地求得向 量的坐标,因此,我们在给向量空间取基时常常取规范正交基.

设 $a_{1}, \cdots, a_{r}$ 是向量空间 $V$ 的一个基, 要求 $V$ 的一个规范正交基. 这也就 是要找一组两两正交的单位向量 $e_{1}, \cdots, e_{r}$, 使 $e_{1}, \cdots, e_{r}$ 与 $a_{1}, \cdots, a_{r}$ 等价. 这样 一个问题,称为把 $a_{1}, \cdots, a_{r}$ 这个基规范正交化.

我们可以用以下办法把 $a_{1}, \cdots, a_{r}$ 规范正交化: 取

$$
\begin{aligned}
& b_{1}=a_{1} ; \\
& b_{2}=a_{2}-\frac{\left[b_{1}, a_{2}\right]}{\left[b_{1}, b_{1}\right]} b_{1} ; \\
& \ldots \ldots \ldots \ldots \\
& b_{r}=a_{r}-\frac{\left[b_{1}, a_{r}\right]}{\left[b_{1}, b_{1}\right]} b_{1}-\frac{\left[b_{2}, a_{r}\right]}{\left[b_{2}, b_{2}\right]} b_{2}-\cdots-\frac{\left[b_{r-1}, a_{r}\right]}{\left[b_{r-1}, b_{r-1}\right]} b_{r-1},
\end{aligned}
$$

容易验证 $b_{1}, \cdots, b_{r}$ 两两正交, 且 $b_{1}, \cdots, b_{r}$ 与 $a_{1}, \cdots, a_{r}$ 等价.

然后只要把它们单位化, 即取

就是 $V$ 的一个规范正交基.

上述从线性无关向量组 $a_{1}, \cdots, a_{r}$ 导出正交向量组 $b_{1}, \cdots, b_{r}$ 的过程称为施 密特 (Schimidt) 正交化过程. 它不仅满足 $b_{1}, \cdots, b_{r}$ 与 $a_{1}, \cdots, a_{r}$ 等价, 还满足: 对 任何 $k(1 \leqslant k \leqslant r)$, 向量组 $\boldsymbol{b}_{1}, \cdots, \boldsymbol{b}_{k}$ 与 $\boldsymbol{a}_{1}, \cdots, \boldsymbol{a}_{\boldsymbol{k}}$ 等价.

例 2 设 $a_{1}=\left(\begin{array}{r}1 \\ 2 \\ -1\end{array}\right), a_{2}=\left(\begin{array}{r}-1 \\ 3 \\ 1\end{array}\right), a_{3}=\left(\begin{array}{r}4 \\ -1 \\ 0\end{array}\right)$, 试用施密特正交化过程把这 组向量规范正交化.

解 取 $b_{1}=a_{1}$;

$$
\begin{gathered}
b_{2}=a_{2}-\frac{\left[a_{2}, b_{1}\right]}{\left\|b_{1}\right\|^{2}} b_{1}=\left(\begin{array}{r}
-1 \\
3 \\
1
\end{array}\right)-\frac{4}{6}\left(\begin{array}{r}
1 \\
2 \\
-1
\end{array}\right)=\frac{5}{3}\left(\begin{array}{r}
-1 \\
1 \\
1
\end{array}\right) ; \\
b_{3}=a_{3}-\frac{\left[a_{3}, b_{1}\right]}{\left\|b_{1}\right\|^{2} b_{1}-\frac{\left[a_{3}, b_{2}\right]}{\left\|b_{2}\right\|^{2}} b_{2}} \\
=\left(\begin{array}{r}
4 \\
-1 \\
0
\end{array}\right)-\frac{1}{3}\left(\begin{array}{r}
1 \\
2 \\
-1
\end{array}\right)+\frac{5}{3}\left(\begin{array}{r}
-1 \\
1 \\
1
\end{array}\right)=2\left(\begin{array}{l}
1 \\
0 \\
1
\end{array}\right) .
\end{gathered}
$$

再把它们单位化, 取

$$
e_{1}=\frac{b_{1}}{\| b_{1}} \|=\frac{1}{\sqrt{6}}\left(\begin{array}{r}
1 \\
2 \\
-1
\end{array}\right), e_{2}=\frac{b_{2}}{\left\|b_{2}\right\|}=\frac{1}{\sqrt{3}}\left(\begin{array}{r}
-1 \\
1 \\
1
\end{array}\right), e_{3}=\frac{b_{3}}{\left\|b_{3}\right\|}=\frac{1}{\sqrt{2}}\left(\begin{array}{l}
1 \\
0 \\
1
\end{array}\right),
$$

$e_{1}, e_{2}, e_{3}$ 即合所求.

本例中各向量如图 5.1 所示. 用解析几何的术语解释如下:

$b_{2}=a_{2}-c_{2}$, 而 $c_{2}$ 为 $a_{2}$ 在 $b_{1}$ 上的投影向 量, 即

$$
c_{2}=\left[a_{2}, \frac{b_{1}}{\left\|b_{1}\right\|}\right]\left\|b_{1} b_{1}\right\|=\frac{\left[a_{2}, b_{1}\right]}{\left\|b_{1}\right\|^{2} b_{1}} .
$$

$b_{3}=a_{3}-c_{3}$, 而 $c_{3}$ 为 $a_{3}$ 在平行于 $b_{1}, b_{2}$ 的 平面上的投影向量, 由于 $b_{1} \perp b_{2}$, 故 $c_{3}$ 等于 $a_{3}$ 分别在 $b_{1}, b_{2}$ 上的投影向量 $c_{31}$ 及 $c_{32}$ 之和, 即

$$
c_{3}=c_{31}+c_{32}=\frac{\left[a_{3}, b_{1}\right]}{\left\|b_{1}\right\|^{2}} b_{1}+\frac{\left[a_{3}, b_{2}\right]}{\left\|b_{2}\right\|^{2}} b_{2} \text {. }
$$

例 3 已知 $a_{1}=\left(\begin{array}{l}1 \\ 1 \\ 1\end{array}\right)$, 求一组非零向量 $a_{2}, a_{3}$, 使 $a_{1}, a_{2}, a_{3}$ 两两正交.

解 $a_{2}, a_{3}$ 应满足方程 $a_{1}^{\mathrm{T}} x=0$, 即

$$
x_{1}+x_{2}+x_{3}=0 \text {, }
$$

它的基础解系为

$$
\xi_{1}=\left(\begin{array}{r}
1 \\
0 \\
-1
\end{array}\right), \xi_{2}=\left(\begin{array}{r}
0 \\
1 \\
-1
\end{array}\right),
$$

把基础解系正交化,即合所求.亦即取

$$
a_{2}=\xi_{1}, a_{3}=\xi_{2}-\frac{\left[\xi_{1}, \xi_{2}\right]}{\left[\xi_{1}, \xi_{1}\right]} \xi_{1},
$$

其中 $\left[\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{2}\right]=1,\left[\boldsymbol{\xi}_{1}, \boldsymbol{\xi}_{1}\right]=2$, 于是得

$$
a_{2}=\left(\begin{array}{r}
1 \\
0 \\
-1
\end{array}\right), a_{3}=\left(\begin{array}{r}
0 \\
1 \\
-1
\end{array}\right)-\frac{1}{2}\left(\begin{array}{r}
1 \\
0 \\
-1
\end{array}\right)=\frac{1}{2}\left(\begin{array}{r}
-1 \\
2 \\
-1
\end{array}\right) \text {. }
$$

定义 4 如果 $n$ 阶矩阵 $\boldsymbol{A}$ 满足

$$
\boldsymbol{A}^{\mathrm{T}} \boldsymbol{A}=\boldsymbol{E} \quad \text { (即 } \boldsymbol{A}^{-1}=\boldsymbol{A}^{\mathrm{T}} \text { ), }
$$

那么称 $\boldsymbol{A}$ 为正交矩阵,简称正交阵. 上式用 $\boldsymbol{A}$ 的列向量表示, 即是

$$
\left(\begin{array}{c}
a_{1}^{\mathrm{T}} \\
a_{2}^{\mathrm{T}} \\
\vdots \\
a_{n}^{\mathrm{T}}
\end{array}\right)\left(a_{1}, a_{2}, \cdots, a_{n}\right)=E,
$$

亦即

$$
\left(a_{i}^{\top} a_{j}\right)=\left(\delta_{i j}\right),
$$

这也就是 $n^{2}$ 个关系式

$$
a_{i}^{\mathrm{T}} a_{j}=\delta_{i j}=\left\{\begin{array}{l}
1, \text { 当 } i=j, \\
0, \text { 当 } i \neq j
\end{array} \quad(i, j=1,2, \cdots, n),\right.
$$

这就说明: 方阵 $\boldsymbol{A}$ 为正交阵的充分必要条件是 $\boldsymbol{A}$ 的列向量都是单位向量,且两 两正交.

由此可见, $n$ 阶正交阵 $\boldsymbol{A}$ 的 $n$ 个列(行)向量构成向量空间 $\mathbb{R}^{n}$ 的一个规范正 交基.

例 4 验证矩阵

$$
P=\left(\begin{array}{rrrr}
\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} & -\frac{1}{2} \\
\frac{1}{2} & -\frac{1}{2} & -\frac{1}{2} & \frac{1}{2} \\
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & 0 & 0 \\
0 & 0 & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}}
\end{array}\right)
$$

是正交阵.

证 $\boldsymbol{P}$ 的每个列向量都是单位向量,且两两正交,所以 $\boldsymbol{P}$ 是正交阵.

正交矩阵有下述性质:

(i) 若 $\boldsymbol{A}$ 为正交阵,则 $\boldsymbol{A}^{-1}=\boldsymbol{A}^{\mathrm{T}}$ 也是正交阵,且 $|\boldsymbol{A}|=1$ 或 $(-1)$;

(ii) 若 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 都是正交阵,则 $\boldsymbol{A B}$ 也是正交阵.

这些性质都可根据正交阵的定义直接证得, 请读者证明之.

定义 5 若 $P$ 为正交矩阵,则线性变换 $\boldsymbol{y}=\boldsymbol{P x}$ 称为正交变换.

设 $y=P x$ 为正交变换, 则有

$$
\|y\|=\sqrt{y^{\mathrm{T}} y}=\sqrt{x^{\mathrm{T}} \boldsymbol{P}^{\mathrm{T} P x}}=\sqrt{x^{\mathrm{T}} \boldsymbol{x}}=\|x\| .
$$

由于 $\|x\|$ 表示向量的长度,相当于线段的长度,因此 $\|\boldsymbol{y}\|=\|\boldsymbol{x}\|$ 说明经 正交变换线段长度保持不变 (从而三角形的形状保持不变), 这是正交变换的优 良特性.

## $\S 2$ 方阵的特征值与特征向量

工程技术中的一些问题，如振动问题和稳定性问题，常可归结为求一个方阵 的特征值和特征向量的问题. 数学中诸如方阵的对角化及解微分方程组等问题, 也都要用到特征值的理论.

定义 6 设 $\boldsymbol{A}$ 是 $n$ 阶矩阵,如果数 $\lambda$ 和 $n$ 维非零列向黑 $\boldsymbol{x}$ 使关系式

$$
\boldsymbol{A} \boldsymbol{x}=\lambda \boldsymbol{x}
$$

成立,那么,这样的数 $\lambda$ 称为矩阵 $\boldsymbol{A}$ 的特征值,非零向量 $\boldsymbol{x}$ 称为 $\boldsymbol{A}$ 的对应于特征 值 $\lambda$ 的特征向量.

(1) 式也可写成

$$
(\boldsymbol{A}-\lambda \boldsymbol{E}) \boldsymbol{x}=\mathbf{0},
$$

这是 $n$ 个未知数 $n$ 个方程的齐次线性方程组,它有非零解的充分必要条件是系 数行列式

即

$$
\left|\begin{array}{cccc}
a_{11}-\lambda & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22}-\lambda & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}-\lambda
\end{array}\right|=0 .
$$

上式是以 $\lambda$ 为末知数的一元 $n$ 次方程, 称为矩阵 $\boldsymbol{A}$ 的特征方程. 其左端 $|\boldsymbol{A}-\lambda \boldsymbol{E}|$ 是 $\lambda$ 的 $n$ 次多项式,记作 $f(\lambda)$, 称为矩阵 $\boldsymbol{A}$ 的特征多项式. 显然, $\boldsymbol{A}$ 的特征值就是特征方程的解. 特征方程在复数范围内恒有解, 其个数为方程的次 数 (重根按重数计算), 因此, $n$ 阶矩阵 $\boldsymbol{A}$ 在复数范围内有 $n$ 个特征值.

设 $n$ 阶矩阵 $\boldsymbol{A}=\left(a_{i j}\right)$ 的特征值为 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$, 不难证明 ${ }^{\Phi}$

(i) $\lambda_{1}+\lambda_{2}+\cdots+\lambda_{n}=a_{11}+a_{22}+\cdots+a_{n n}$;

(ii) $\lambda_{1} \lambda_{2} \cdots \lambda_{n}=|\boldsymbol{A}|$.

设 $\lambda=\lambda_{i}$ 为矩阵 $\boldsymbol{A}$ 的一个特征值, 则由方程

$$
\left(\boldsymbol{A}-\lambda_{i} E\right) \boldsymbol{x}=\mathbf{0}
$$

可求得非零解 $x=p_{i}$, 那么 $p_{i}$ 便是 $A$ 的对应于特征值 $\lambda_{i}$ 的特征向量. (若 $\lambda_{i}$ 为

(1) $f(\lambda)=\left(\lambda_{1}-\lambda\right)\left(\lambda_{2}-\lambda\right) \cdots\left(\lambda_{n}-\lambda\right)$, 其中 $\lambda^{0}$ 和 $\lambda^{n-1}$ 的系数依次为 $\lambda_{1} \lambda_{2} \cdots \lambda_{n}$ 租 $(-1)^{n-1}\left(\lambda_{1}+\right.$ $\left.\lambda_{2}+\cdots+\lambda_{n}\right)$, 故只霜证明多项式 $|\boldsymbol{A}-\lambda \boldsymbol{E}|$ 中 $\lambda^{0}$ 和 $\lambda^{n-1}$ 的系数依炏为 $|\boldsymbol{A}|$ 和 $(-1)^{n-1}\left(a_{11}+a_{22}+\cdots+\right.$ $\left.a_{n n}\right)$. 实数,则 $\boldsymbol{p}_{i}$ 可取实向䤚; 若 $\lambda_{i}$ 为复数, 则 $\boldsymbol{p}_{i}$ 为复向量.)

例 5 求矩阵 $A=\left(\begin{array}{rr}3 & -1 \\ -1 & 3\end{array}\right)$ 的特征值和特征向量.

解 $\boldsymbol{A}$ 的特征多项式为

$$
\begin{aligned}
|\boldsymbol{A}-\lambda \boldsymbol{E}| & =\left|\begin{array}{cc}
3-\lambda & -1 \\
-1 & 3-\lambda
\end{array}\right|=(3-\lambda)^{2}-1=8-6 \lambda+\lambda^{2} \\
& =(4-\lambda)(2-\lambda),
\end{aligned}
$$

所以 $\boldsymbol{A}$ 的特征值为 $\lambda_{1}=2, \lambda_{2}=4$.

当 $\lambda_{1}=2$ 时,对应的特征向量应满足

$$
\left(\begin{array}{rc}
3-2 & -1 \\
-1 & 3-2
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right)=\left(\begin{array}{l}
0 \\
0
\end{array}\right) \text {, 即 }\left(\begin{array}{rr}
1 & -1 \\
-1 & 1
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right)=\left(\begin{array}{l}
0 \\
0
\end{array}\right) \text {, }
$$

解得 $x_{1}=x_{2}$, 所以对应的特征向量可取为

$$
p_{1}=\left(\begin{array}{l}
1 \\
1
\end{array}\right) \text {. }
$$

当 $\lambda_{2}=4$ 时, 由

$$
\left(\begin{array}{cc}
3-4 & -1 \\
-1 & 3-4
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right)=\left(\begin{array}{l}
0 \\
0
\end{array}\right) \text {, 即 }\left(\begin{array}{ll}
-1 & -1 \\
-1 & -1
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2}
\end{array}\right)=\left(\begin{array}{l}
0 \\
0
\end{array}\right) \text {, }
$$

解得 $x_{1}=-x_{2}$, 所以对应的特征向量可取为

$$
p_{2}=\left(\begin{array}{r}
-1 \\
1
\end{array}\right) \text {. }
$$

显然,若 $\boldsymbol{p}_{i}$ 是矩阵 $\boldsymbol{A}$ 的对应于特征值 $\lambda_{i}$ 的特征向量,则 $k p_{i}(k \neq 0)$ 也是对 应于 $\lambda_{i}$ 的特征向量.

例 6 求矩阵

$$
\boldsymbol{A}=\left(\begin{array}{rrr}
-1 & 1 & 0 \\
-4 & 3 & 0 \\
1 & 0 & 2
\end{array}\right)
$$

的特征值和特征向量.

解 $\boldsymbol{A}$ 的特征多项式为

$$
|\boldsymbol{A}-\lambda \boldsymbol{E}|=\left|\begin{array}{ccc}
-1-\lambda & 1 & 0 \\
-4 & 3-\lambda & 0 \\
1 & 0 & 2-\lambda
\end{array}\right|=(2-\lambda)(1-\lambda)^{2},
$$

所以 $\boldsymbol{A}$ 的特征值为 $\lambda_{1}=2, \lambda_{2}=\lambda_{3}=1$.

当 $\lambda_{1}=2$ 时,解方程 $(\boldsymbol{A}-2 \boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$. 由

$$
\left.\boldsymbol{A}-2 \boldsymbol{E}=\left(\begin{array}{ccc}
-3 & 1 & 0 \\
-4 & 1 & 0 \\
1 & 0 & 0
\end{array}\right) \stackrel{\sim}{\sim} \begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{array}\right)
$$

得基础解系

$$
p_{1}=\left(\begin{array}{l}
0 \\
0 \\
1
\end{array}\right) \text {, }
$$

所以 $k p_{1}(k \neq 0)$ 是对应于 $\lambda_{1}=2$ 的全部特征向量.

当 $\lambda_{2}=\lambda_{3}=1$ 时,解方程 $(\boldsymbol{A}-\boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$. 由

$$
\boldsymbol{A}-\boldsymbol{E}=\left(\begin{array}{rrr}
-2 & 1 & 0 \\
-4 & 2 & 0 \\
1 & 0 & 1
\end{array}\right) \sim\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 2 \\
0 & 0 & 0
\end{array}\right),
$$

得基础解系

$$
p_{2}=\left(\begin{array}{r}
-1 \\
-2 \\
1
\end{array}\right) \text {, }
$$

所以 $k p_{2}(k \neq 0)$ 是对应于 $\lambda_{2}=\lambda_{3}=1$ 的全部特征向量.

例 7 求矩阵

$$
A=\left(\begin{array}{rrr}
-2 & 1 & 1 \\
0 & 2 & 0 \\
-4 & 1 & 3
\end{array}\right)
$$

的特征值和特征向量.

解

$$
\begin{aligned}
|\boldsymbol{A}-\lambda \boldsymbol{E}| & =\left|\begin{array}{ccc}
-2-\lambda & 1 & 1 \\
0 & 2-\lambda & 0 \\
-4 & 1 & 3-\lambda
\end{array}\right| \\
& =(2-\lambda)\left|\begin{array}{cc}
-2-\lambda & 1 \\
-4 & 3-\lambda
\end{array}\right| \\
& =(2-\lambda)\left(\lambda^{2}-\lambda-2\right) \\
& =-(\lambda+1)(\lambda-2)^{2},
\end{aligned}
$$

所以 $\boldsymbol{A}$ 的特征值为 $\lambda_{1}=-1, \lambda_{2}=\lambda_{3}=2$.

当 $\lambda_{1}=-1$ 时,解方程 $(\boldsymbol{A}+\boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$. 由

得基础解系

$$
\boldsymbol{A}+\boldsymbol{E}=\left(\begin{array}{rrr}
-1 & 1 & 1 \\
0 & 3 & 0 \\
-4 & 1 & 4
\end{array}\right) \sim\left(\begin{array}{rrr}
1 & 0 & -1 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{array}\right),
$$

$$
p_{1}=\left(\begin{array}{l}
1 \\
0 \\
1
\end{array}\right) \text {, }
$$

所以对应于 $\lambda_{1}=-1$ 的全部特征向量为 $k p_{1}(k \neq 0)$.

当 $\lambda_{2}=\lambda_{3}=2$ 时,解方程 $(\boldsymbol{A}-2 \boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$. 由

得基础解系

$$
\begin{gathered}
\boldsymbol{A}-2 \boldsymbol{E}=\left(\begin{array}{rrr}
-4 & 1 & 1 \\
0 & 0 & 0 \\
-4 & 1 & 1
\end{array}\right) \underset{\sim}{r}\left[\begin{array}{rrr}
-4 & 1 & 1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right], \\
\boldsymbol{p}_{2}=\left(\begin{array}{r}
0 \\
1 \\
-1
\end{array}\right), \boldsymbol{p}_{3}=\left(\begin{array}{l}
1 \\
0 \\
4
\end{array}\right),
\end{gathered}
$$

所以对应于 $\lambda_{2}=\lambda_{3}=1$ 的全部特征向量为

$$
k_{2} \boldsymbol{p}_{2}+k_{3} \boldsymbol{p}_{3} \quad\left(k_{2}, k_{3} \text { 不同时为 } 0\right) \text {. }
$$

例 8 设 $\lambda$ 是方阵 $\boldsymbol{A}$ 的特征值,证明

(1) $\lambda^{2}$ 是 $A^{2}$ 的特征值;

(2) 当 $A$ 可逆时, $\frac{1}{\lambda}$ 是 $A^{-1}$ 的特征值.

证 因 $\lambda$ 是 $A$ 的特征值, 故有 $p \neq 0$ 使 $A p=\lambda p$.于是

$$
\boldsymbol{A}^{2} \boldsymbol{p}=\boldsymbol{A}(\boldsymbol{A p})=\boldsymbol{A}(\lambda \boldsymbol{p})=\lambda(\boldsymbol{A p})=\lambda^{2} p,
$$

所以 $\lambda^{2}$ 是 $A^{2}$ 的特征值.

（2）当 $\boldsymbol{A}$ 可逆时, 由 $\boldsymbol{A p}=\lambda \boldsymbol{p}$, 有 $\boldsymbol{p}=\lambda \boldsymbol{A}^{-1} \boldsymbol{p}$, 因 $\boldsymbol{p} \neq \mathbf{0}$, 知 $\lambda \neq 0$, 故

$$
\boldsymbol{A}^{-1} \boldsymbol{p}=\frac{1}{\lambda} \boldsymbol{p},
$$

所以 $\frac{1}{\lambda}$ 是 $A^{-1}$ 的特征值.

按此例类推,不难证明: 若 $\lambda$ 是 $\boldsymbol{A}$ 的特征值, 则 $\lambda^{k}$ 是 $\boldsymbol{A}^{k}$ 的特征值; $\varphi(\lambda)$ 是 $\varphi(\boldsymbol{A})$ 的特征值(其中 $\varphi(\lambda)=a_{0}+a_{1} \lambda+\cdots+a_{m} \lambda^{m}$ 是 $\lambda$ 的多项式, $\varphi(\boldsymbol{A})=a_{0} \boldsymbol{E}$ $+a_{1} \boldsymbol{A}+\cdots+a_{m n} \boldsymbol{A}^{\prime \prime}$ 是矩阵 $\boldsymbol{A}$ 的多项式).

例 9 设 3 阶矩阵 $\boldsymbol{A}$ 的特征值为 $1,-1,2$, 求 $\boldsymbol{A}^{*}+3 \boldsymbol{A}-2 \boldsymbol{E}$ 的特征值.

解 因 $\boldsymbol{A}$ 的特征值全不为 0 , 知 $\boldsymbol{A}$ 可逆, 故 $\boldsymbol{A}^{*}=|\boldsymbol{A}| \boldsymbol{A}^{-1}$. 而 $|\boldsymbol{A}|=$ $\lambda_{1} \lambda_{2} \lambda_{3}=-2$, 所以

$$
\boldsymbol{A}^{*}+3 \boldsymbol{A}-2 \boldsymbol{E}=-2 \boldsymbol{A}^{-1}+3 \boldsymbol{A}-2 \boldsymbol{E} .
$$

把上式记作 $\varphi(\boldsymbol{A})$, 有 $\varphi(\lambda)=-\frac{2}{\lambda}+3 \lambda-2$. 这里, $\varphi(\boldsymbol{A})$ 虽不是矩阵多项式, 但 也具有矩阵多项式的特性, 从而可得 $\varphi(\boldsymbol{A})$ 的特征值为 $\varphi(1)=-1$, $\varphi(-1)=-3, \varphi(2)=3$.

定理 2 设 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$ 是方阵 $\boldsymbol{A}$ 的 $m$ 个特征值, $\boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \cdots, \boldsymbol{p}_{m}$ 依次是与 之对应的特征向量，如果 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{m}$ 各不相等，则 $p_{1}, p_{2}, \cdots, p_{m}$ 线性无关. 证用数学归纳法.

当 $m=1$ 时,因特征向量 $p_{1} \neq 0$, 故只含一个向㨁的向量组 $\boldsymbol{p}_{1}$ 线性无关.

假设当 $m=k-1$ 时结论成立，要证当 $m=k$ 时结论也成立. 即假设向轸组 $p_{1}, p_{2}, \cdots$, $p_{k-1}$ 线性无关, 要证向较组 $p_{1}, p_{2}, \cdots, p_{k}$ 线性无关. 为此, 令

$$
x_{1} p_{1}+x_{2} p_{2}+\cdots+x_{k-1} p_{k-1}+x_{k} p_{k}=0 \text {, }
$$

用 $\boldsymbol{A}$ 左乘上式,得

$$
\begin{gathered}
x_{1} \boldsymbol{A} p_{1}+x_{2} \boldsymbol{A} p_{2}+\cdots+x_{k-1} \boldsymbol{A} p_{k-1}+x_{k} \boldsymbol{A} p_{k}=\mathbf{0}, \\
x_{1} \lambda_{1} p_{1}+x_{2} \lambda_{2} p_{2}+\cdots+x_{k-1} \lambda_{k-1} p_{k-1}+x_{k} \lambda_{k} p_{k}=\mathbf{0} .
\end{gathered}
$$

(3) 式城去(2)式的 $\lambda_{k}$ 倍,得

$$
x_{1}\left(\lambda_{1}-\lambda_{k}\right) p_{1}+x_{2}\left(\lambda_{2}-\lambda_{k}\right) p_{2}+\cdots+x_{k-1}\left(\lambda_{k-1}-\lambda_{k}\right) p_{k-1}=0 .
$$

按归纳法假设 $p_{1}, p_{2}, \cdots, p_{k-1}$ 线性无关,故 $x_{i}\left(\lambda_{i}-\lambda_{k}\right)=0(i=1,2, \cdots, k-1)$. 而 $\lambda_{i}-\lambda_{k} \neq 0$ $(i=1,2, \cdots, k-1)$, 于是得 $x_{i}=0(i=1,2, \cdots, k-1)$, 代人(2) 式得 $x_{k} p_{k}=0$, 而 $p_{k} \neq 0$, 得 $x_{k}=0$. 因此，向量组 $p_{1}, p_{2}, \cdots, p_{k}$ 线性无关.

例 10 设 $\lambda_{1}$ 和 $\lambda_{2}$ 是矩阵 $\boldsymbol{A}$ 的两个不同的特征值,对应的特征向嫼依次为 $p_{1}$ 和 $p_{2}$, 证明 $p_{1}+p_{2}$ 不是 $A$ 的特征向量.

证 按题设,有 $A p_{1}=\lambda_{1} p_{1}, A p_{2}=\lambda_{2} p_{2}$, 故

$$
\boldsymbol{A}\left(\boldsymbol{p}_{1}+\boldsymbol{p}_{2}\right)=\lambda_{1} \boldsymbol{p}_{1}+\lambda_{i} \boldsymbol{p}_{2} \text {. }
$$

用反证法, 假设 $p_{1}+p_{2}$ 是 $A$ 的特征向硨, 则应存在数 $\lambda$, 使 $A\left(p_{1}+p_{2}\right)=$ $\lambda\left(p_{1}+p_{2}\right)$, 于是

$$
\lambda\left(\boldsymbol{p}_{1}+\boldsymbol{p}_{2}\right)=\lambda_{1} \boldsymbol{p}_{1}+\lambda_{2} \boldsymbol{p}_{2} \text {, 即 }\left(\lambda_{1}-\lambda\right) \boldsymbol{p}_{1}+\left(\lambda_{2}-\lambda\right) \boldsymbol{p}_{2}=\mathbf{0},
$$

因 $\lambda_{1} \neq \lambda_{2}$, 按定理 2 知 $\boldsymbol{p}_{1}, \boldsymbol{p}_{2}$ 线性无关, 故由上式得 $\lambda_{1}-\lambda=\lambda_{2}-\lambda=0$, 即 $\lambda_{1}$ $=\lambda_{2}$, 与题设矛盾. 因此 $\boldsymbol{p}_{1}+\boldsymbol{p}_{2}$ 不是 $\boldsymbol{A}$ 的特征向量.

## $\S 3$ 相 似 矩 阵

定义 7 设 $\boldsymbol{A}, \boldsymbol{B}$ 都是 $n$ 阶矩阵,若有可逆矩阵 $\boldsymbol{P}$,使

$$
\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{B},
$$

则称 $\boldsymbol{B}$ 是 $\boldsymbol{A}$ 的相似矩阵, 或说矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相似. 对 $\boldsymbol{A}$ 进行运算 $P^{-1} \boldsymbol{A P}$ 称为对 $\boldsymbol{A}$ 进行相似变换,可逆矩阵 $\boldsymbol{P}$ 称为把 $\boldsymbol{A}$ 变成 $\boldsymbol{B}$ 的相似变换矩阵.

定理 3 若 $n$ 阶矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相似, 则 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 的特征多项式相同, 从而 $\boldsymbol{A}$ 与 $B$ 的特征值亦相同.

证 因 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 相似, 即有可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{B}$. 故

$$
|\boldsymbol{B}-\lambda \boldsymbol{E}|=\left|\boldsymbol{P}^{-1} \boldsymbol{A P}-\boldsymbol{P}^{-1}(\lambda \boldsymbol{E}) \boldsymbol{P}\right|=\left|\boldsymbol{P}^{-1}(\boldsymbol{A}-\lambda \boldsymbol{E}) \boldsymbol{P}\right|
$$

$$
=\left|\boldsymbol{P}^{-1}\right||\boldsymbol{A}-\lambda \boldsymbol{E}||\boldsymbol{P}|=|\boldsymbol{A}-\lambda \boldsymbol{E}| .
$$

推论 若 $n$ 阶矩阵 $A$ 与对角阵

$$
\boldsymbol{\Lambda}=\left(\begin{array}{llll}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{n}
\end{array}\right)
$$

相似, 则 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 即是 $\boldsymbol{A}$ 的 $n$ 个特征值.

证 因 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 即是 $\boldsymbol{\Lambda}$ 的 $n$ 个特征值, 由定理 3 知 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 也就 是 $\boldsymbol{A}$ 的 $n$ 个特征值.

证毕

在第二章中我们曾指出: 若 $\boldsymbol{A}=\boldsymbol{P B P} \boldsymbol{P}^{-1}$, 则 $\boldsymbol{A}^{k}=\boldsymbol{P} \boldsymbol{B}^{k} \boldsymbol{P}^{-1} \cdot \boldsymbol{A}$ 的多项式

$$
\varphi(A)=P \varphi(B) P^{-1} \text {. }
$$

特别, 若有可逆矩阵 $\boldsymbol{P}$ 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$ 为对角阵, 则

$$
\boldsymbol{A}^{k}=\boldsymbol{P} \boldsymbol{\Lambda}^{k} \boldsymbol{P}^{-1}, \varphi(\boldsymbol{A})=\boldsymbol{P} \varphi(\boldsymbol{\Lambda}) \boldsymbol{P}^{-1} .
$$

而对于对角阵 $\Lambda$, 有

$$
\boldsymbol{\Lambda}^{k}=\left(\begin{array}{llll}
\lambda_{1}^{k} & & & \\
& \lambda_{2}^{k} & & \\
& & \ddots & \\
& & & \lambda_{n}^{k}
\end{array}\right), \varphi(\boldsymbol{\Lambda})=\left(\begin{array}{llll}
\varphi\left(\lambda_{1}\right) & & & \\
& \varphi\left(\lambda_{2}\right) & & \\
& & \ddots & \\
& & & \varphi\left(\lambda_{n}\right)
\end{array}\right),
$$

由此可方便地计算 $\boldsymbol{A}$ 的多项式 $\varphi(\boldsymbol{A})$.

有一个很有趣的结论: 设 $f(\lambda)$ 是矩阵 $\boldsymbol{A}$ 的特征多项式, 则 $f(\boldsymbol{A})=\boldsymbol{O}$. 这个 结论的证明比较困难, 但若 $\boldsymbol{A}$ 与对角阵相似, 则容易证明此结论. 这是因为: 若 $\boldsymbol{A}$ 与对角阵相似, 即有可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{A}=\operatorname{diag}\left(\lambda_{1}, \cdots, \lambda_{n}\right)$, 其中 $\lambda_{i}$ 为 $\boldsymbol{A}$ 的特征值,有 $f\left(\lambda_{i}\right)=0$. 于是, 由 $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{\Lambda} \boldsymbol{P}^{-1}$, 有

$$
\begin{aligned}
f(\boldsymbol{A}) & =\boldsymbol{P} f(\boldsymbol{\Lambda}) \boldsymbol{P}^{-1}=\boldsymbol{P}\left(\begin{array}{lll}
f\left(\lambda_{1}\right) & & \\
& \ddots & \\
& & f\left(\lambda_{n}\right)
\end{array}\right) \boldsymbol{P}^{-1} \\
& =\boldsymbol{P} O \boldsymbol{P}^{-1}=\boldsymbol{O} .
\end{aligned}
$$

下面我们要讨论的主要问题是: 对 $n$ 阶矩阵 $\boldsymbol{A}$, 寻求相似变换矩阵 $\boldsymbol{P}$, 使 $P^{-1} A P=i \Lambda$ 为对角阵, 这就称为把矩阵 $\boldsymbol{A}$ 对角华.

假设已经找到可逆矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$ 为对角阵,我们来讨论 $\boldsymbol{P}$ 应满足 什么关系。

把 $\boldsymbol{P}$ 用其列向量表示为

$$
P=\left(p_{1}, p_{2}, \cdots, p_{n}\right),
$$

由 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$, 得 $\boldsymbol{A P}=\boldsymbol{P \Lambda}$, 即

$$
\begin{aligned}
\boldsymbol{A}\left(\boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \cdots, \boldsymbol{p}_{n}\right) & =\left(\boldsymbol{p}_{1}, \boldsymbol{p}_{2}, \cdots, \boldsymbol{p}_{n}\right)\left(\begin{array}{llll}
\lambda_{1} & & & \\
& \lambda_{2} & & \\
& & \ddots & \\
& & & \lambda_{n}
\end{array}\right) \\
& =\left(\lambda_{1} \boldsymbol{p}_{1}, \lambda_{2} \boldsymbol{p}_{2}, \cdots, \lambda_{n} \boldsymbol{p}_{n}\right),
\end{aligned}
$$

于是有

$$
\boldsymbol{A} \boldsymbol{p}_{i}=\lambda_{i} \boldsymbol{p}_{i} \quad(i=1,2, \cdots, n) .
$$

可见 $\lambda_{i}$ 是 $\boldsymbol{A}$ 的特征值,而 $\boldsymbol{P}$ 的列向量 $\boldsymbol{p}_{i}$ 就是 $\boldsymbol{A}$ 的对应于特征值 $\lambda_{i}$ 的特征向 量.

反之, 由上节知 $\boldsymbol{A}$ 佮好有 $n$ 个特征值, 并可对应地求得 $n$ 个特征向量, 这 $n$ 个特征向量即可构成矩阵 $\boldsymbol{P}$, 使 $\boldsymbol{A P}=\boldsymbol{P A}$. (因特征向量不是惟一的, 所以矩阵 $\boldsymbol{P}$ 也不是惟一的,并且 $\boldsymbol{P}$ 可能是复矩阵.)

余下的问题是: $P$ 是否可逆? 即 $p_{1}, p_{2}, \cdots, p_{n}$ 是否线性无关? 如果 $P$ 可 逆, 那么便有 $P^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$, 即 $\boldsymbol{A}$ 与对角阵相似.

由上面的讨论即有

定理 $4 n$ 阶矩阵 $A$ 与对角阵相似 (即 $A$ 能对角化) 的充分必要条件是 $A$ 有 $n$ 个线性无关的特征向量.

联系定理 2 , 可得

推论 如果 $n$ 阶矩阵 $\boldsymbol{A}$ 的 $n$ 个特征值互不相等,则 $\boldsymbol{A}$ 与对角阵相似.

当 $\boldsymbol{A}$ 的特征方程有重根时, 就不一定有 $n$ 个线性无关的特征向量,从而不 一定能对角化.例如在例 6 中 $\boldsymbol{A}$ 的特征方程有重根,确实找不到 3 个线性无关 的特征向量,因此例 6 中的 $\boldsymbol{A}$ 不能对角化; 而在例 7 中 $A$ 的特征方程也有重 根,但能找到 3 个线性无关的特征向量,因此例 7 中的 $\boldsymbol{A}$ 能对角化.

例 11 设 $A=\left(\begin{array}{ccc}0 & 0 & 1 \\ 1 & 1 & x \\ 1 & 0 & 0\end{array}\right)$,

问 $x$ 为何值时,矩阵 $\boldsymbol{A}$ 能对角化?

$$
\text { 解 } \begin{aligned}
|\boldsymbol{A}-\lambda \boldsymbol{E}| & =\left|\begin{array}{ccc}
-\lambda & 0 & 1 \\
1 & 1-\lambda & x \\
1 & 0 & -\lambda
\end{array}\right|=(1-\lambda)\left|\begin{array}{cc}
-\lambda & 1 \\
1 & -\lambda
\end{array}\right| \\
& =-(\lambda-1)^{2}(\lambda+1),
\end{aligned}
$$

得 $\lambda_{1}=-1, \lambda_{2}=\lambda_{3}=1$.

对应单根 $\lambda_{1}=-1$, 可求得线性无关的特征向量恰有 1 个,故矩阵 $\boldsymbol{A}$ 可对角 化的充分必要条件是对应重根 $\lambda_{2}=\lambda_{3}=1$, 有 2 个线性无关的特征向量,即方程 $(\boldsymbol{A}-\boldsymbol{E}) \boldsymbol{x}=0$ 有 2 个线性无关的解, 亦即系数矩阵 $\boldsymbol{A}-\boldsymbol{E}$ 的秩 $R(\boldsymbol{A}-\boldsymbol{E})=1$. 由

$$
\boldsymbol{A}-\boldsymbol{E}=\left(\begin{array}{rrr}
-1 & 0 & 1 \\
1 & 0 & x \\
1 & 0 & -1
\end{array}\right) \sim\left(\begin{array}{ccc}
1 & 0 & -1 \\
0 & 0 & x+1 \\
0 & 0 & 0
\end{array}\right),
$$

要 $R(\boldsymbol{A}-\boldsymbol{E})=1$, 得 $x+1=0$, 即 $x=-1$.

因此,当 $x=-1$ 时,矩阵 $\boldsymbol{A}$ 能对角化.

## $\S 4$ 对称矩阵的对角化

一个 $n$ 阶矩阵具备什么条件才能对角化? 这是一个较复杂的问题. 我们对 此不进行一般性的讨论,而仅讨论当 $\boldsymbol{A}$ 为对称阵的情形.

定理 5 对称阵的特征值为实数.

证 设复数 $\lambda$ 为对称阵 $A$ 的特征值，复向值 $x$ 为对应的特征向里，即 $A x=\lambda x, x \neq 0$.

用 $\bar{\lambda}$ 表示 $\lambda$ 的共轭复数, $\bar{x}$ 表示 $\boldsymbol{x}$ 的共轮复向量, 而 $\boldsymbol{A}$ 为实矩阵,有 $\boldsymbol{A}=\overline{\boldsymbol{A}}$, 故 $\boldsymbol{A} \overline{\boldsymbol{x}}=$ $\bar{A} \bar{x}=(\overline{A x})=(\overline{\lambda x})=\bar{\lambda} \bar{x}$.于是有

及

$$
\overline{\boldsymbol{x}}^{\mathrm{T}} A \boldsymbol{x}=\overline{\boldsymbol{x}}^{\mathrm{T}}(\boldsymbol{A x})=\overline{\boldsymbol{x}}^{\mathrm{T}} \lambda \boldsymbol{x}=\lambda \overline{\boldsymbol{x}}^{\mathrm{T}} \boldsymbol{x},
$$

两式相减，得

$$
\overline{\boldsymbol{x}}^{\mathrm{T}} \boldsymbol{A x}=\left(\bar{x}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}\right) \boldsymbol{x}=(\boldsymbol{A} \bar{x})^{\mathrm{T}} \boldsymbol{x}=(\bar{\lambda} \bar{x})^{\mathrm{T}} \boldsymbol{x}=\bar{\lambda} \overline{\boldsymbol{x}}^{\mathrm{T}} \boldsymbol{x},
$$

但因 $\boldsymbol{x} \neq \mathbf{0}$, 所以

$$
(\lambda-\bar{\lambda}) \bar{x}^{\top} x=0 \text {, }
$$

故 $\lambda-\bar{\lambda}=0$, 即 $\lambda=\bar{\lambda}$, 这就说明 $\lambda$ 是实数.

$$
\overline{\boldsymbol{x}}^{\mathrm{\top}} \dot{x}=\sum_{i=1}^{n} \bar{x}_{i} x_{i}=\sum_{i=1}^{n}\left|x_{i}\right|^{2} \neq 0,
$$

显然,当特征值 $\lambda_{i}$ 为实数时,齐次线性方程组

$$
\left(\boldsymbol{A}-\lambda_{i} \boldsymbol{E}\right) \boldsymbol{x}=\mathbf{0}
$$

是实系数方程组, 由 $\left|\boldsymbol{A}-\lambda_{i} \boldsymbol{E}\right|=0$ 知必有实的基础解系, 所以对应的特征向量 可以取实向量.

定理 6 设 $\lambda_{1}, \lambda_{2}$ 是对称阵 $A$ 的两个特征值, $p_{1}, p_{2}$ 是对应的特征向量. 著 $\lambda_{1} \neq \lambda_{2}$, 则 $p_{1}$ 与 $p_{2}$ 正交.

证 $\lambda_{1} p_{1}=A p_{1}, \lambda_{2} p_{2}=A p_{2}, \lambda_{1} \neq \lambda_{2}$.

因 $\boldsymbol{A}$ 对称,故 $\lambda_{1} p_{1}^{\mathrm{T}}=\left(\lambda_{1} \boldsymbol{p}_{1}\right)^{\mathrm{T}}=\left(\boldsymbol{A} \boldsymbol{p}_{1}\right)^{\mathrm{T}}=\boldsymbol{p}_{1}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}}=\boldsymbol{p}_{1}^{\mathrm{T}} \boldsymbol{A}$, 于是

$$
\lambda_{1} p_{1}^{\mathrm{T}} \boldsymbol{p}_{2}=\boldsymbol{p}_{1}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{p}_{2}=\boldsymbol{p}_{1}^{\mathrm{T}}\left(\lambda_{2} \boldsymbol{p}_{2}\right)=\lambda_{2} \boldsymbol{p}_{1}^{\mathrm{T}} \boldsymbol{p}_{2} \text {, }
$$

即

$$
\left(\lambda_{3}-\lambda_{2}\right) p_{1}^{\mathrm{T}} p_{2}=0 \text {. }
$$

但 $\lambda_{1} \neq \lambda_{2}$, 故 $p_{1}^{\top} p_{2}=0$, 即 $p_{1}$ 与 $p_{2}$ 正交.

定理 7 设 $A$ 为 $n$ 阶对称阵, 则必有正交阵 $P$, 便 $P^{-1} A P=P^{\mathrm{T}} A P=\Lambda$, 其 中 $\Lambda$ 是以 $A$ 的 $n$ 个特征值为对角元的对角阵.

此定理不予证明。 推论 设 $\boldsymbol{A}$ 为 $n$ 阶对称阵, $\lambda$ 是 $\boldsymbol{A}$ 的特征方程的 $k$ 重根, 则矩阵 $\boldsymbol{A}-\lambda \boldsymbol{E}$ 的 秩 $R(\boldsymbol{A}-\lambda \boldsymbol{E})=n-k$, 从而对应特征值 $\lambda$ 恰有 $k$ 个线性无关的特征向是.

证 按定理 7 知对称阵 $\boldsymbol{A}$ 与对角阵 $\boldsymbol{\Lambda}=\operatorname{diag}\left(\lambda_{1}, \cdots, \lambda_{n}\right)$ 相似, 从而 $\boldsymbol{A}-\lambda \boldsymbol{E}$ 与 $\boldsymbol{\Lambda}-\lambda \boldsymbol{E}=\operatorname{diag}\left(\lambda_{1}-\lambda, \cdots, \lambda_{n}-\lambda\right)$ 相似. 当 $\lambda$ 是 $\boldsymbol{A}$ 的 $k$ 重特征根时, $\lambda_{1}, \cdots, \lambda_{n}$ 这 $n$ 个特征值中有 $k$ 个等于 $\lambda$, 有 $n-k$ 个不等于 $\lambda$, 从而对角阵 $\boldsymbol{\Lambda}-\lambda \boldsymbol{E}$ 的对角 元恰有 $k$ 个等于 0 ,于是 $R(\boldsymbol{A}-\lambda \boldsymbol{E})=n-k$. 而 $R(\boldsymbol{A}-\lambda \boldsymbol{E})=R(\boldsymbol{A}-\lambda \boldsymbol{E})$, 所以 $R(\boldsymbol{A}-\lambda \boldsymbol{E})=n-k$.

证毕

依据定理 7 及其推论,我们有下述把对称阵 $\boldsymbol{A}$ 对角化的步骤:

(i) 求出 $\boldsymbol{A}$ 的全部互不相等的特征值 $\lambda_{1}, \cdots, \lambda_{s}$, 它们的重数依次为 $k_{1}, \cdots$, $k_{s}\left(k_{1}+\cdots+k_{s}=n\right)$.

- (ii) 对每个 $k_{i}$ 重特征值 $\lambda_{i}$, 求方程 $\left(\boldsymbol{A}-\lambda_{i} \boldsymbol{E}\right) \boldsymbol{x}=\mathbf{0}$ 的基础解系, 得 $k_{i}$ 个线 性无关的特征向量.再把它们正交化、单位化,得 $k_{i}$ 个两两正交的单位特征向 量. 因 $k_{1}+\cdots+k_{s}=n$, 故总共可得 $n$ 个两两正交的单位特征向量.

(iii) 把这 $n$ 个两两正交的单位特征向埋构成正交阵 $\boldsymbol{P}$, 便有 $\boldsymbol{P}^{-1} \boldsymbol{A P}=$ $\boldsymbol{P}^{\mathrm{T}} \boldsymbol{A P}=\boldsymbol{\Lambda}$. 注意 $\boldsymbol{\Lambda}$ 中对角元的排列次序应与 $\boldsymbol{P}$ 中列向望的排列次序相对应.

例 12 设 $A=\left(\begin{array}{rrr}0 & -1 & 1 \\ -1 & 0 & 1 \\ 1 & 1 & 0\end{array}\right)$, 求一个正交阵 $P$, 使 $P^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$ 为对角阵.

解 由

$$
\begin{aligned}
|\boldsymbol{A}-\lambda \boldsymbol{E}| & =\left|\begin{array}{rrr}
-\lambda & -1 & 1 \\
-1 & -\lambda & 1 \\
1 & 1 & -\lambda
\end{array}\right| \underline{\underline{r_{1}-r_{2}}}\left|\begin{array}{ccc}
1-\lambda & \lambda-1 & 0 \\
-1 & -\lambda & 1 \\
1 & 1 & -\lambda
\end{array}\right| \stackrel{\underline{c_{2}+c_{1}}}{\mid}\left|\begin{array}{ccc}
1-\lambda & 0 & 0 \\
-1 & -1-\lambda & 1 \\
1 & 2 & -\lambda
\end{array}\right| \\
& =(1-\lambda)\left(\lambda^{2}+\lambda-2\right)=-(\lambda-1)^{2}(\lambda+2),
\end{aligned}
$$

求得 $\boldsymbol{A}$ 的特征值为 $\lambda_{1}=-2, \lambda_{2}=\lambda_{3}=1$.

对应 $\lambda_{1}=-2$, 解方程 $(\boldsymbol{A}+2 E) x=0$, 由

$$
\boldsymbol{A}+2 \boldsymbol{E}=\left(\begin{array}{rrr}
2 & -1 & 1 \\
-1 & 2 & 1 \\
1 & 1 & 2
\end{array}\right) \sim\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 1 \\
0 & 0 & 0
\end{array}\right)
$$

得基础解系 $\xi_{1}=\left(\begin{array}{r}-1 \\ -1 \\ 1\end{array}\right)$. 将 $\xi_{1}$ 单位化，得 $p_{1}=\frac{1}{\sqrt{3}}\left(\begin{array}{r}-1 \\ -1 \\ 1\end{array}\right)$.

对应 $\lambda_{2}=\lambda_{3}=1$, 解方程 $(\boldsymbol{A}-\boldsymbol{E}) \boldsymbol{x}=\mathbf{0}$, 由

$$
\boldsymbol{A}-\boldsymbol{E}=\left(\begin{array}{rrr}
-1 & -1 & 1 \\
-1 & -1 & 1 \\
1 & 1 & -1
\end{array}\right) \sim\left(\begin{array}{rrr}
1 & 1 & -1 \\
0 & 0 & 0 \\
0 & 0 & 0
\end{array}\right),
$$

得基础解系 $\xi_{2}=\left(\begin{array}{r}-1 \\ 1 \\ 0\end{array}\right), \xi_{3}=\left(\begin{array}{l}1 \\ 0 \\ 1\end{array}\right)$.

将 $\xi_{2}, \xi_{3}$ 正交化: 取 $\eta_{2}=\xi_{2}$,

$$
\boldsymbol{\eta}_{3}=\xi_{3}-\frac{\left[\boldsymbol{\eta}_{2}, \xi_{3}\right]}{\left\|\boldsymbol{\eta}_{2}\right\|^{2}} \boldsymbol{\eta}_{2}=\left(\begin{array}{l}
1 \\
0 \\
1
\end{array}\right)+\frac{1}{2}\left(\begin{array}{r}
1 \\
1 \\
0
\end{array}\right)=\frac{1}{2}\left(\begin{array}{l}
1 \\
1 \\
2
\end{array}\right) \text {. }
$$

再将 $\boldsymbol{\eta}_{2}, \boldsymbol{\eta}_{3}$ 单位化，得 $p_{2}=\frac{1}{\sqrt{2}}\left(\begin{array}{r}-1 \\ 1 \\ 0\end{array}\right), p_{3}=\frac{1}{\sqrt{6}}\left(\begin{array}{l}1 \\ 1 \\ 2\end{array}\right)$.

将 $p_{1}, p_{2}, p_{3}$ 构成正交矩阵

有

$$
\begin{aligned}
& \boldsymbol{P}=\left(p_{1}, p_{2}, p_{3}\right)=\left(\begin{array}{ccc}
-\frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
-\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
\frac{1}{\sqrt{3}} & 0 & \frac{2}{\sqrt{6}}
\end{array}\right), \\
& \boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{P}^{\mathrm{T}} \boldsymbol{A P}=\boldsymbol{\Lambda}=\left(\begin{array}{rrr}
-2 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) .
\end{aligned}
$$

例 13 设 $A=\left(\begin{array}{rr}2 & -1 \\ -1 & 2\end{array}\right)$, 求 $A^{n}$.

解 因 $\boldsymbol{A}$ 对称, 故 $\boldsymbol{A}$ 可对角化, 即有可逆矩阵 $\boldsymbol{P}$ 及对角阵 $\boldsymbol{\Lambda}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=$ $\boldsymbol{\Lambda}$. 于是 $\boldsymbol{A}=\boldsymbol{P} \boldsymbol{\Lambda} \boldsymbol{P}^{-1}$, 从而 $\boldsymbol{A}^{n}=\boldsymbol{P} \boldsymbol{A}^{n} \boldsymbol{P}^{-1}$.

由 $|\boldsymbol{A}-\lambda \boldsymbol{E}|=\left|\begin{array}{cc}2-\lambda & -1 \\ -1 & 2-\lambda\end{array}\right|=\lambda^{2}-4 \lambda+3=(\lambda-1)(\lambda-3)$,

得 $\boldsymbol{A}$ 的特征值 $\lambda_{1}=1, \lambda_{2}=3$. 于是

$$
\boldsymbol{\Lambda}=\left(\begin{array}{ll}
1 & 0 \\
0 & 3
\end{array}\right), \boldsymbol{\Lambda}^{n}=\left(\begin{array}{cc}
1 & 0 \\
0 & 3^{n}
\end{array}\right) .
$$

对应 $\lambda_{1}=1$, 由 $A-E=\left(\begin{array}{rr}1 & -1 \\ -1 & 1\end{array}\right) \sim\left(\begin{array}{rr}1 & -1 \\ 0 & 0\end{array}\right)$, 得 $\xi_{1}=\left(\begin{array}{l}1 \\ 1\end{array}\right)$; 对应 $\lambda_{2}=3$, 由 $A-3 E=\left(\begin{array}{ll}-1 & -1 \\ -1 & -1\end{array}\right) \sim\left(\begin{array}{ll}1 & 1 \\ 0 & 0\end{array}\right)$, 得 $\xi_{2}=\left(\begin{array}{r}1 \\ -1\end{array}\right)$.

并有 $\boldsymbol{P}=\left(\xi_{1}, \xi_{2}\right)=\left(\begin{array}{rr}1 & 1 \\ 1 & -1\end{array}\right)$, 再求出 $\boldsymbol{P}^{-1}=\frac{1}{2}\left(\begin{array}{rr}1 & 1 \\ 1 & -1\end{array}\right)$. 于是

$$
\boldsymbol{A}^{n}=\boldsymbol{P} \boldsymbol{\Lambda}^{n} \boldsymbol{P}^{-1}=\frac{1}{2}\left(\begin{array}{rr}
1 & 1 \\
1 & -1
\end{array}\right)\left(\begin{array}{rr}
1 & 0 \\
0 & 3^{n}
\end{array}\right)\left(\begin{array}{rr}
1 & 1 \\
1 & -1
\end{array}\right)=\frac{1}{2}\left(\begin{array}{ll}
1+3^{n} & 1-3^{n} \\
1-3^{n} & 1+3^{n}
\end{array}\right) \text {. }
$$

## $\S 5$ 二次型及其标准形

在解析几何中, 为了便于研究二次曲线

$$
a x^{2}+b x y+c y^{2}=1
$$

的几何性质, 可以选择适当的坐标旋转变换

把方程化为标准形

$$
\left\{\begin{array}{l}
x=x^{\prime} \cos \theta-y^{\prime} \sin \theta, \\
y=x^{\prime} \sin \theta+y^{\prime} \cos \theta
\end{array}\right.
$$

$$
m x^{\prime 2}+n y^{\prime 2}=1 .
$$

(4) 式的左边是一个二次齐次多项式,从代数学的观点看,化标准形的过程 就是通过变量的线性变换化简一个二次齐次多项式, 使它只含有平方项. 这样一 个问题, 在许多理论问题或实际问题中常会遇到. 现在我们把这类问题一般化, 讨论 $n$ 个变量的二次齐次多项式的化简问题.

定义 8 含有 $n$ 个变量 $x_{1}, x_{2}, \cdots, x_{n}$ 的二次齐次函数

$$
\begin{aligned}
& f\left(x_{1}, x_{2}, \cdots, x_{n}\right)=a_{11} x_{1}^{2}+a_{22} x_{2}^{2}+\cdots+a_{n n} x_{n}^{2} \\
& \quad+2 a_{12} x_{1} x_{2}+2 a_{13} x_{1} x_{3}+\cdots+2 a_{n-1, n} x_{n-1} x_{n}
\end{aligned}
$$

称为二次型.

取 $a_{j i}=a_{i j}$, 则 $2 a_{i j} x_{i} x_{j}=a_{i j} x_{i} x_{j}+a_{j i} x_{j} x_{i}$,于是(5)式可写成

$$
\begin{aligned}
f= & a_{11} x_{1}^{2}+a_{12} x_{1} x_{2}+\cdots+a_{1 n} x_{1} x_{n} \\
& +a_{21} x_{2} x_{1}+a_{22} x_{2}^{2}+\cdots+a_{2 n} x_{2} x_{n} \\
& +\cdots+a_{n 1} x_{n} x_{1}+a_{n 2} x_{n} x_{2}+\cdots+a_{n n} x_{n}^{2} \\
= & \sum_{i, j=1}^{n} a_{i j} x_{i} x_{j} .
\end{aligned}
$$

对于二次型,我们讨论的主要问题是: 寻求可逆的线性变换

$$
\left\{\begin{array}{l}
x_{1}=c_{11} y_{1}+c_{12} y_{2}+\cdots+c_{1 n} y_{n}, \\
x_{2}=c_{21} y_{1}+c_{22} y_{2}+\cdots+c_{2 n} y_{n}, \\
\cdots \cdots \cdots \cdots \cdots \cdots \\
x_{n}=c_{n 1} y_{1}+c_{n 2} y_{2}+\cdots+c_{n n} y_{n}
\end{array}\right.
$$

使二次型只含平方项, 也就是用 (7) 代人 (5), 能使

$$
f=k_{1} y_{1}^{2}+k_{2} y_{2}^{2}+\cdots+k_{n} y_{n}^{2},
$$

这种只含平方项的二次型,称为二次型的标准形 (或法式).

如果标准形的系数 $k_{1}, k_{2}, \cdots, k_{n}$ 只在 $1,-1,0$ 三个数中取值, 也就是用 (7) 代人(5),能使

$$
f=y_{1}^{2}+\cdots+y_{p}^{2}-y_{p+1}^{2}-\cdots-y_{r}^{2},
$$

则称上式为二次型的规范形.

当 $a_{i j}$ 为复数时, $f$ 称为复二次型; 当 $a_{i j}$ 为实数时, $f$ 称为实二资型. 这里,我 们仅讨论实二次型,所求的线性变换(7)也限于实系数范围.

由 (6)式,利用矩阵,二次型可表示为

$$
\begin{aligned}
f= & x_{1}\left(a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n}\right) \\
& +x_{2}\left(a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n}\right) \\
& +\cdots+x_{n}\left(a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n}\right) \\
= & \left(x_{1}, x_{2}, \cdots, x_{n}\right)\left(\begin{array}{c}
a_{11} x_{1}+a_{12} x_{2}+\cdots+a_{1 n} x_{n} \\
a_{21} x_{1}+a_{22} x_{2}+\cdots+a_{2 n} x_{n} \\
\vdots \\
a_{n 1} x_{1}+a_{n 2} x_{2}+\cdots+a_{n n} x_{n}
\end{array}\right) \\
= & \left(x_{1}, x_{2}, \cdots, x_{n}\right)\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right),
\end{aligned}
$$

记

则二次型可记作

$$
\boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right), \boldsymbol{x}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right),
$$

$$
f=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x},
$$

其中 $\boldsymbol{A}$ 为对称阵.

例如, 二次型 $f=x^{2}-3 z^{2}-4 x y+y z$ 用矩阵记号写出来, 就是

$$
f=(x, y, z)\left(\begin{array}{rrr}
1 & -2 & 0 \\
-2 & 0 & \frac{1}{2} \\
0 & \frac{1}{2} & -3
\end{array}\right)\left(\begin{array}{l}
x \\
y \\
z
\end{array}\right) .
$$

任给一个二次型, 就惟一地确定一个对称阵; 反之, 任给一个对称阵, 也可惟 一地确定一个二次型. 这样, 二次型与对称阵之间存在一一对应的关系. 因此, 我 们把对称阵 $\boldsymbol{A}$ 叫做二次型 $f$ 的矩阵, 也把 $f$ 叫做对称阵 $\boldsymbol{A}$ 的二次型. 对称阵 $\boldsymbol{A}$ 的秩就叫做二次型 $f$ 的秩.

记 $\boldsymbol{C}=\left(c_{i j}\right)$,把可逆变换 $(7)$ 记作

$$
\boldsymbol{x}=\boldsymbol{C y},
$$

代人 (8), 有 $f=x^{\mathrm{T}} A \boldsymbol{x}=(\boldsymbol{C y})^{\mathrm{T}} A C y=y^{\mathrm{T}}\left(C^{\mathrm{T}} A C\right) \boldsymbol{y}$.

定义 9 设 $\boldsymbol{A}$ 和 $\boldsymbol{B}$ 是 $n$ 阶矩阵, 若有可逆矩阵 $\boldsymbol{C}$, 使 $\boldsymbol{B}=\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}$, 则称矩阵 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 合同.

显然, 若 $\boldsymbol{A}$ 为对称阵, 则 $\boldsymbol{B}=\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}$ 也为对称阵, 且 $R(\boldsymbol{B})=R(\boldsymbol{A})$. 事实 上,

$$
B^{\mathrm{T}}=\left(\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}\right)^{\mathrm{T}}=\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A}^{\mathrm{T}} \boldsymbol{C}=\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}=\boldsymbol{B},
$$

即 $B$ 为对称阵. 又因 $B=C^{\mathrm{T}} A C$, 而 $C$ 可逆, 从而 $C^{\mathrm{T}}$ 也可逆, 由矩阵秩的性质 即知 $R(\boldsymbol{B})=R(\boldsymbol{A})$.

由此可知,经可逆变换 $\boldsymbol{x}=\boldsymbol{C y}$ 后,二次型 $f$ 的矩阵由 $\boldsymbol{A}$ 变为与 $\boldsymbol{A}$ 合同的矩 阵 $\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}$, 且二次型的秩不变.

要使二次型 $f$ 经可逆变换 $\boldsymbol{x}=\boldsymbol{C y}$ 变成标准形,这就是要使

$$
\begin{aligned}
\boldsymbol{y}^{\mathrm{T}} \boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C} \boldsymbol{y} & =k_{1} y_{1}^{2}+k_{2} y_{2}^{2}+\cdots+k_{n} y_{n}^{2} \\
& =\left(y_{1}, y_{2}, \cdots, y_{n}\right)\left(\begin{array}{cccc}
k_{1} & & & \\
& k_{2} & & \\
& & \ddots & \\
& & & k_{n}
\end{array}\right)\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{n}
\end{array}\right),
\end{aligned}
$$

也就是要使 $\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}$ 成为对角阵. 因此, 我们的主要问题就是: 对于对称阵 $\boldsymbol{A}$, 寻 求可逆矩阵 $\boldsymbol{C}$,使 $\boldsymbol{C}^{\mathrm{T}} \boldsymbol{A C}$ 为对角阵.这个问题称为把对称阵 $A$ 合同对角化.

由上节定理 7 知, 任给对称阵 $\boldsymbol{A}$, 总有正交阵 $\boldsymbol{P}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$, 即 $\boldsymbol{P}^{\mathrm{T}} \boldsymbol{A P}$ $=\boldsymbol{\Lambda}$. 把此结论应用于二次型，即有

定理 8 任给二次型 $f=\sum_{i, j=1}^{n} a_{i j} x_{i} x_{j}\left(a_{i j}=a_{j i}\right)$, 总有正交变换 $\boldsymbol{x}=\boldsymbol{P} \boldsymbol{y}$,使 $f$ 化为标准形

$$
f=\lambda_{1} y_{1}^{2}+\lambda_{2} y_{2}^{2}+\cdots+\lambda_{n} y_{n}^{2},
$$

其中 $\lambda_{1}, \lambda_{2}, \cdots, \lambda_{n}$ 是 $f$ 的矩阵 $\boldsymbol{A}=\left(a_{i j}\right)$ 的特征值.

推论 任给 $n$ 元二次型 $f(\boldsymbol{x})=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A} \boldsymbol{x}\left(\boldsymbol{A}^{\mathrm{T}}=\boldsymbol{A}\right)$, 总有可逆变换 $\boldsymbol{x}=\boldsymbol{C z}$, 使 $f(C z)$ 为规范形.

证 按定理 8 ,有

$$
f(\boldsymbol{P} \boldsymbol{y})=\boldsymbol{y}^{\mathrm{T}} \boldsymbol{\Lambda} \boldsymbol{y}=\lambda_{1} y_{1}^{2}+\cdots+\lambda_{n} y_{n}^{2},
$$

设二次型 $f$ 的秩为 $r$, 则特征值 $\lambda_{i}$ 中恰有 $r$ 个不为 0 , 无妨设 $\lambda_{1}, \cdots, \lambda_{r}$ 不等于 $0, \lambda_{r+1}=\cdots=\lambda_{n}=0$, 令

$$
\boldsymbol{K}=\left(\begin{array}{llll}
k_{1} & & & \\
& k_{2} & & \\
& & \ddots & \\
& & & k_{n}
\end{array}\right) \text {, 其中 } k_{i}=\left\{\begin{array}{cc}
\frac{1}{\sqrt{\left|\lambda_{i}\right|}}, i \leqslant r, \\
1, i>r,
\end{array}\right.
$$

则 $\boldsymbol{K}$ 可逆,变换 $\boldsymbol{y}=\boldsymbol{K} \boldsymbol{z}$ 把 $f(\boldsymbol{P y})$ 化为

而

$$
\begin{gathered}
f(\boldsymbol{P} \boldsymbol{K} \boldsymbol{z})=\boldsymbol{z}^{\mathrm{T}} \boldsymbol{K}^{\mathrm{T}} \boldsymbol{P}^{\mathrm{T}} \boldsymbol{A P K z}=\boldsymbol{z}^{\mathrm{T}} \boldsymbol{K}^{\mathrm{T}} \boldsymbol{\Lambda} \boldsymbol{K} \boldsymbol{z}, \\
\boldsymbol{K}^{\mathrm{T}} \boldsymbol{\Lambda} \boldsymbol{K}=\operatorname{diag}\left(\frac{\lambda_{1}}{\left|\lambda_{1}\right|}, \cdots, \frac{\lambda_{r}}{\left|\lambda_{r}\right|}, 0, \cdots, 0\right),
\end{gathered}
$$

记 $\boldsymbol{C}=\boldsymbol{P K}$, 即知可逆变换 $\boldsymbol{x}=\boldsymbol{C z}$ 把 $f$ 化成规范形

$$
f(C z)=\frac{\lambda_{1}}{\left|\lambda_{1}\right|} z_{1}^{2}+\cdots+\frac{\lambda_{r}}{\left|\lambda_{r}\right|} z_{r}^{2} .
$$

例 14 求一个正交变换 $\boldsymbol{x}=\boldsymbol{P} \boldsymbol{y}$,把二次型

$$
f=-2 x_{1} x_{2}+2 x_{1} x_{3}+2 x_{2} x_{3} \text {. }
$$

化为标准形.

解 二次型的矩阵为

$$
A=\left(\begin{array}{rrr}
0 & -1 & 1 \\
-1 & 0 & 1 \\
1 & 1 & 0
\end{array}\right),
$$

这与例 12 所给矩阵相同. 按例 12 的结果,有正交阵

$$
\boldsymbol{P}=\left(\begin{array}{rrr}
-\frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
-\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
\frac{1}{\sqrt{3}} & 0 & \frac{2}{\sqrt{6}}
\end{array}\right) \text {, 使 } \boldsymbol{P}^{\mathrm{T}} \boldsymbol{A P}=\boldsymbol{\Lambda}=\left(\begin{array}{rrr}
-2 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 1
\end{array}\right) \text {, }
$$

于是有正交变换

$$
\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3}
\end{array}\right)=\left(\begin{array}{rrr}
-\frac{1}{\sqrt{3}} & -\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
-\frac{1}{\sqrt{3}} & \frac{1}{\sqrt{2}} & \frac{1}{\sqrt{6}} \\
\frac{1}{\sqrt{3}} & 0 & \frac{2}{\sqrt{6}}
\end{array}\right)\left(\begin{array}{l}
y_{1} \\
y_{2} \\
y_{3}
\end{array}\right)
$$

把二次型 $f$ 化成标准形

$$
f=-2 y_{1}^{2}+y_{2}^{2}+y_{3}^{2} \text {. }
$$

如果要把二次型 $f$ 化成规范形, 只需令

即得 $f$ 的规范形

$$
\left\{\begin{array}{l}
y_{1}=\frac{1}{\sqrt{2}} z_{1}, \\
y_{2}=z_{2}, \\
y_{3}=z_{3},
\end{array}\right.
$$

$$
f=-z_{1}^{2}+z_{2}^{2}+z_{3}^{2} .
$$

## $\S 6$ 用配方法化二次型成标准形

用正交变换化二次型成标准形,具有保持几何形状不变的优点. 如果不限于 用正交变换, 那么还可以有多种方法 (对应有多个可逆的线性变换) 把二次型化 成标准形.这里只介绍拉格朗日配方法.下面举例来说明这种方法.

例 15 化二次型

$$
f=x_{1}^{2}+2 x_{2}^{2}+5 x_{3}^{2}+2 x_{1} x_{2}+2 x_{1} x_{3}+6 x_{2} x_{3}
$$

成标准形,并求所用的变换矩阵.

解 由于 $f$ 中含变量 $x_{1}$ 的平方项,故把含 $x_{1}$ 的项归并起来, 配方可得

$$
\begin{aligned}
f & =x_{1}^{2}+2 x_{1} x_{2}+2 x_{1} x_{3}+2 x_{2}^{2}+5 x_{3}^{2}+6 x_{2} x_{3} \\
& =\left(x_{1}+x_{2}+x_{3}\right)^{2}-x_{2}^{2}-x_{3}^{2}-2 x_{2} x_{3}+2 x_{2}^{2}+5 x_{3}^{2}+6 x_{2} x_{3} \\
& =\left(x_{1}+x_{2}+x_{3}\right)^{2}+x_{2}^{2}+4 x_{2} x_{3}+4 x_{3}^{2},
\end{aligned}
$$

上式右端除第一项外已不再含 $x_{1}$. 继续配方,可得

$$
\begin{gathered}
f=\left(x_{1}+x_{2}+x_{3}\right)^{2}+\left(x_{2}+2 x_{3}\right)^{2} . \\
\text { 令 }\left\{\begin{array} { l } 
{ y _ { 1 } = x _ { 1 } + x _ { 2 } + x _ { 3 } , } \\
{ y _ { 2 } = \quad x _ { 2 } + 2 x _ { 3 } , } \\
{ y _ { 3 } = } \\
{ x _ { 3 } , }
\end{array} \text { 即 } \left\{\begin{array}{lr}
x_{1}=y_{1}-y_{2}+y_{3}, \\
x_{2}= & y_{2}-2 y_{3}, \\
x_{3}= & y_{3},
\end{array}\right.\right.
\end{gathered}
$$

就把 $f$ 化成标准形 (规范形) $f=y_{1}^{2}+y_{2}^{2}$, 所用变换矩阵为

$$
C=\left(\begin{array}{rrr}
1 & -1 & 1 \\
0 & 1 & -2 \\
0 & 0 & 1
\end{array}\right)(|C|=1 \neq 0) \text {. }
$$

例 16 化二次型

$$
f=2 x_{1} x_{2}+2 x_{1} x_{3}-6 x_{2} x_{3}
$$

成规范形,并求所用的变换矩阵. 解 在 $f$ 中不含平方项. 由于含有 $x_{1} x_{2}$ 乘积项, 故令

代人可得

$$
\left\{\begin{array}{l}
x_{1}=y_{1}+y_{2}, \\
x_{2}=y_{1}-y_{2}, \\
x_{3}=y_{3},
\end{array}\right.
$$

再配方, 得

$$
f=2 y_{1}^{2}-2 y_{2}^{2}-4 y_{1} y_{3}+8 y_{2} y_{3} \text {. }
$$

$$
\text { 令 }\left\{\begin{array} { l } 
{ z _ { 1 } = \sqrt { 2 } ( y _ { 1 } - y _ { 3 } ) , } \\
{ z _ { 2 } = \sqrt { 2 } ( y _ { 2 } - 2 y _ { 3 } ) , } \\
{ z _ { 3 } = \sqrt { 6 } y _ { 3 } , }
\end{array} \text { 即 } \left\{\begin{array}{l}
y_{1}=\frac{1}{\sqrt{2}} z_{1}+\frac{1}{\sqrt{6}} z_{3}, \\
y_{2}=\frac{1}{\sqrt{2}} z_{2}+\frac{2}{\sqrt{6}} z_{3}, \\
y_{3}=\frac{1}{\sqrt{6}} z_{3},
\end{array}\right.\right.
$$

就把 $f$ 化成规范形

$$
f=z_{1}^{2}-z_{2}^{2}+z_{3}^{2}
$$

所用变换矩阵为

$$
\begin{aligned}
& C=\left(\begin{array}{rrr}
1 & 1 & 0 \\
1 & -1 & 0 \\
0 & 0 & 1
\end{array}\right)\left(\begin{array}{ccc}
\frac{1}{\sqrt{2}} & 0 & \frac{1}{\sqrt{6}} \\
0 & \frac{1}{\sqrt{2}} & \frac{2}{\sqrt{6}} \\
0 & 0 & \frac{1}{\sqrt{6}}
\end{array}\right)=\left(\begin{array}{ccc}
\frac{1}{\sqrt{2}} & \frac{1}{\sqrt{2}} & \frac{3}{\sqrt{6}} \\
\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{2}} & -\frac{1}{\sqrt{6}} \\
0 & 0 & \frac{1}{\sqrt{6}}
\end{array}\right) \\
&\left(|C|=-\frac{1}{\sqrt{6}} \neq 0\right) .
\end{aligned}
$$

一般的,任何二次型都可用上面两例的方法找到可逆变换,把二次型化成标 准形(或规范形).

## $\S 7$ 正定二次型

二次型的标准形显然不是惟一的, 只是标准形中所含项数是确定的 (即是二 次型的秩). 不仅如此, 在限定变换为实变换时, 标准形中正系数的个数是不变的 (从而负系数的个数也不变),也就是有

定理 9 设有二次型 $f=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A x}$, 它的秩为 $r$, 有两个可逆变换

使

及

$$
\boldsymbol{x}=\mathrm{Cy} \quad \text { 及 } \boldsymbol{x}=\mathrm{Pz}
$$

$$
\begin{array}{ll}
f=k_{1} y_{1}^{2}+k_{2} y_{2}^{2}+\cdots+k_{r} y_{r}^{2} & \left(k_{i} \neq 0\right), \\
f=\lambda_{1} z_{1}^{2}+\lambda_{2} z_{2}^{2}+\cdots+\lambda_{r} z_{r}^{2} & \left(\lambda_{i} \neq 0\right),
\end{array}
$$

则 $k_{1}, \cdots, k_{r}$ 中正数的个数与 $\lambda_{1}, \cdots, \lambda_{r}$ 中正数的个数相等.

这个定理称为惯性定理,这里不予证明.

二次型的标准形中正系数的个数称为二次型的正惯性指数,负系数的个数 称为负惯性指数. 若二次型 $f$ 的正惯性指数为 $p$, 秩为 $r$, 则 $f$ 的规范形便可确 定为

$$
f=y_{1}^{2}+\cdots+y_{p}^{2}-y_{p+1}^{2}-\cdots-y_{r}^{2} .
$$

科学技术上用得较多的二次型是正惯性指数为 $n$ 或负惯性指数为 $n$ 的 $n$ 元二次型,我们有下述定义.

定义 10 设有二次型 $f(x)=x^{\mathrm{T}} \boldsymbol{A x}$, 如果对任何 $\boldsymbol{x} \neq \mathbf{0}$, 都有 $f(\boldsymbol{x})>0$ (显 然 $f(0)=0)$, 则称 $f$ 为正定二次型, 并称对称阵 $A$ 是正定的; 如果对任何 $\boldsymbol{x} \neq 0$ 都有 $f(\boldsymbol{x})<0$, 则称 $f$ 为负定二次型,并称对称阵 $\boldsymbol{A}$ 是负定的.

定理 $10 n$ 元二次型 $f=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A x}$ 为正定的充分必要条件是: 它的标准形的 $n$ 个系数全为正,即它的规范形的 $n$ 个系数全为 1 , 亦即它的正惯性指数等于 $n$.

证 设可逆变换 $\boldsymbol{x}=\mathrm{Cy}$ 使

$$
f(\boldsymbol{x})=f(\boldsymbol{C y})=\sum_{i=1}^{n} k_{i} y_{i}^{2} .
$$

先证充分性. 设 $k_{i}>0(i=1, \cdots, n)$. 任给 $\boldsymbol{x} \neq \mathbf{0}$, 则 $\boldsymbol{y}=\boldsymbol{C}^{-1} \boldsymbol{x} \neq \mathbf{0}$, 故

$$
f(x)=\sum_{i=1}^{n} k_{i} y_{i}^{2}>0 \text {. }
$$

再证必要性. 用反证法. 假设有 $k_{s} \leqslant 0$, 则当 $y=e_{s}$ (单位坐标向量) 时, $f\left(\mathrm{Ce}_{s}\right)=k_{s} \leqslant 0$. 显然 $\mathrm{Ce}_{s} \neq \mathbf{0}$, 这与 $f$ 为正定相矛盾. 这就证明了 $k_{i}>0$ $(i=1, \cdots, n)$.

推论 对称阵 $\boldsymbol{A}$ 为正定的充分必要条件是: $\boldsymbol{A}$ 的特征值全为正.

定理 11 对称阵 $A$ 为正定的充分必要条件是: $A$ 的各阶主子式都为正, 即

$$
a_{11}>0,\left|\begin{array}{cc}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|>0, \cdots,\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 n} \\
\vdots & & \vdots \\
a_{n 1} & \cdots & a_{n n}
\end{array}\right|>0,
$$

对称阵 $\boldsymbol{A}$ 为负定的充分必要条件是: 奇数阶主子式为负,而偶数阶主子式为正, 即

$$
(-1)^{r}\left|\begin{array}{ccc}
a_{11} & \cdots & a_{1 r} \\
\vdots & & \vdots \\
a_{r 1} & \cdots & a_{r r}
\end{array}\right|>0(r=1,2, \cdots, n) .
$$

这个定理称为㛢尔维茨定理,这里不予证明.

例 17 判定二次型 $f=-5 x^{2}-6 y^{2}-4 z^{2}+4 x y+4 x z$ 的正定性. 解 $f$ 的矩阵为

$$
\begin{gathered}
A=\left(\begin{array}{rrr}
-5 & 2 & 2 \\
2 & -6 & 0 \\
2 & 0 & -4
\end{array}\right), \\
a_{11}=-5<0,\left|\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right|=\left|\begin{array}{rr}
-5 & 2 \\
2 & -6
\end{array}\right|=26>0, \\
|\boldsymbol{A}|=-80<0,
\end{gathered}
$$

根据定理 11 知 $f$ 为负定.

设 $f(x, y)$ 是二元正定二次型, 则 $f(x, y)=c(c>0$ 为常数 $)$ 的图形是以原 点为中心的椭圆. 当把 $c$ 看作任意常数时则是一族椭圆. 这族椭圆随着 $c \rightarrow 0$ 而 收缩到原点. 当 $f$ 为三元正定二次型时, $f(x, y, z)=c(c>0)$ 的图形是一族椭 球.

## 习 题 五

1. 设 $a=\left(\begin{array}{r}1 \\ 0 \\ -2\end{array}\right), b=\left(\begin{array}{r}-4 \\ 2 \\ 3\end{array}\right), c$ 与 $a$ 正交, 且 $b=\lambda a+c$, 求 $\lambda$ 和 $c$.
2. 试用施密特法把下列向是组正交化:

(1) $\left(a_{1}, a_{2}, a_{3}\right)=\left(\begin{array}{lll}1 & 1 & 1 \\ 1 & 2 & 4 \\ 1 & 3 & 9\end{array}\right)$;

(2) $\left(a_{1}, a_{2}, a_{3}\right)=\left(\begin{array}{rrr}1 & 1 & -1 \\ 0 & -1 & 1 \\ -1 & 0 & 1 \\ 1 & 1 & 0\end{array}\right)$.

3. 下列矩阵是不是正交矩阵? 并说明理由:

(1) $\left(\begin{array}{rrr}1 & -\frac{1}{2} & \frac{1}{3} \\ -\frac{1}{2} & 1 & \frac{1}{2} \\ \frac{1}{3} & \frac{1}{2} & -1\end{array}\right) ; \quad$ (2) $\left(\begin{array}{rrr}\frac{1}{9} & -\frac{8}{9} & -\frac{4}{9} \\ -\frac{8}{9} & \frac{1}{9} & -\frac{4}{9} \\ -\frac{4}{9} & -\frac{4}{9} & \frac{7}{9}\end{array}\right)$.

4. 设 $x$ 为 $n$ 维列向证, $x^{\mathrm{T}} x=1$, 令 $H=E-2 x x^{\mathrm{T}}$, 证明 $\boldsymbol{H}$ 是对称的正交阵.
5. 设 $A, B$ 都是正交阵,证明 $A B$ 也是正交阵.
6. 求下列矩阵的特征值和特征向措:
(1) $\left(\begin{array}{rrr}2 & -1 & 2 \\ 5 & -3 & 3 \\ -1 & 0 & -2\end{array}\right)$;
(2) $\left(\begin{array}{lll}1 & 2 & 3 \\ 2 & 1 & 3 \\ 3 & 3 & 6\end{array}\right)$;
$(3)\left(\begin{array}{llll}0 & 0 & 0 & 1 \\ 0 & 0 & 1 & 0 \\ 0 & 1 & 0 & 0 \\ 1 & 0 & 0 & 0\end{array}\right)$
7. 设 $\boldsymbol{A}$ 为 $n$ 阶矩阵,证明 $\boldsymbol{A}^{\mathrm{T}}$ 与 $\boldsymbol{A}$ 的特征值相同.
8. 设 $n$ 阶矩阵 $\boldsymbol{A}, \boldsymbol{B}$ 满足 $R(A)+R(\boldsymbol{B})<n$, 证明 $\boldsymbol{A}$ 与 $\boldsymbol{B}$ 有公共的特征值, 有公共的特 征向量.
9. 设 $A^{2}-3 A+2 E=O$, 证明 $\boldsymbol{A}$ 的特征值只能取 1 或 2 .
10. 设 $A$ 为正交阵,且 $|A|=-1$, 证明 $\lambda=-1$ 是 $A$ 的特征值.
11. 设 $\lambda \neq 0$ 是 $m$ 阶矩阵 $\boldsymbol{A}_{m \times n} \boldsymbol{B}_{n \times m}$ 的特征值, 证明 $\lambda$ 也是 $n$ 阶矩阵 $\boldsymbol{B} A$ 的特征值.
12. 已知 3 阶矩阵 $A$ 的特征值为 $1,2,3$, 求 $\left|A^{3}-5 A^{2}+7 A\right|$.
13. 已知 3 阶矩阵 $A$ 的特征值为 $1,2,-3$, 求 $\left|A^{*}+3 A+2 E\right|$.
14. 设 $\boldsymbol{A}, \boldsymbol{B}$ 都是 $n$ 阶矩阵, 且 $\boldsymbol{A}$ 可逆,证明 $\boldsymbol{A B}$ 与 $\boldsymbol{B A}$ 相似.
15. 设矩阵 $A=\left(\begin{array}{lll}2 & 0 & 1 \\ 3 & 1 & x \\ 4 & 0 & 5\end{array}\right)$ 可相似对角化,求 $x$.
16. 已知 $\boldsymbol{p}=\left(\begin{array}{r}1 \\ 1 \\ -1\end{array}\right)$ 是矩阵 $\boldsymbol{A}=\left(\begin{array}{rrr}2 & -1 & 2 \\ 5 & a & 3 \\ -1 & b & -2\end{array}\right)$ 的一个特征向量.

(1) 求参数 $a, b$ 及特征向量 $p$ 所对应的特征值;

(2) 问 $\boldsymbol{A}$ 能不能相似对角化? 并说明理由.

17. 设 $\boldsymbol{A}=\left(\begin{array}{rrr}1 & 4 & 2 \\ 0 & -3 & 4 \\ 0 & 4 & 3\end{array}\right)$, 求 $\boldsymbol{A}^{100}$.
18. 在某国, 每年有比例为 $p$ 的农村居民移居城镇, 有比例为 $q$ 的城镇居民移居农村. 假 设该国总人口数不变, 且上述人口迁移的规律也不变. 把 $n$ 年后农村人口和城镇人口占总人 口的比例依次记为 $x_{n}$ 和 $y_{n}\left(x_{n}+y_{n}=1\right)$.

(1) 求关系式 $\left(\begin{array}{l}x_{n+1} \\ y_{n+1}\end{array}\right)=\boldsymbol{A}\left(\begin{array}{l}x_{n} \\ y_{n}\end{array}\right)$ 中的矩阵 $\boldsymbol{A}$;

（2）设目前农村人口与城镇人口相等, 即 $\left(\begin{array}{l}x_{0} \\ y_{0}\end{array}\right)=\left(\begin{array}{l}0.5 \\ 0.5\end{array}\right)$, 求 $\left(\begin{array}{l}x_{n} \\ y_{n}\end{array}\right)$.

19. 试求一个正交的相似变换矩阵,将下列对称阵化为对角阵:

(1) $\left(\begin{array}{rrr}2 & -2 & 0 \\ -2 & 1 & -2 \\ 0 & -2 & 0\end{array}\right)$; (2) $\left(\begin{array}{rrr}2 & 2 & -2 \\ 2 & 5 & -4 \\ -2 & -4 & 5\end{array}\right)$.

20. 设矩阵 $\boldsymbol{A}=\left(\begin{array}{rrr}1 & -2 & -4 \\ -2 & x & -2 \\ -4 & -2 & 1\end{array}\right)$ 与 $\boldsymbol{\Lambda}=\left(\begin{array}{lll}5 & \\ & -4 & \\ & & y\end{array}\right)$ 相似, 求 $x, y$; 并求一个正交阵 $\boldsymbol{P}$, 使 $\boldsymbol{P}^{-1} \boldsymbol{A P}=\boldsymbol{\Lambda}$.
21. 设 3 阶矩阵 $\boldsymbol{A}$ 的特征值为 $\lambda_{1}=2, \lambda_{2}=-2, \lambda_{3}=1$; 对应的特征向量依次为

$$
p_{1}=\left(\begin{array}{l}
0 \\
1 \\
1
\end{array}\right), p_{2}=\left(\begin{array}{l}
1 \\
1 \\
1
\end{array}\right), p_{3}=\left(\begin{array}{l}
1 \\
1 \\
0
\end{array}\right) \text {, }
$$

求 $\boldsymbol{A}$.

22. 设 3 阶对称阵 $A$ 的特征值为 $\lambda_{1}=1, \lambda_{2}=-1, \lambda_{3}=0$; 对应 $\lambda_{1}, \lambda_{2}$ 的特征向些依次为

$$
p_{1}=\left(\begin{array}{l}
1 \\
2 \\
2
\end{array}\right), p_{2}=\left(\begin{array}{r}
2 \\
1 \\
-2
\end{array}\right) \text {, }
$$

求 $\boldsymbol{A}$.

23. 设 3 阶对称阵 $A$ 的特征值为 $\lambda_{1}=6, \lambda_{2}=\lambda_{3}=3$, 与特征值 $\lambda_{1}=6$ 对应的特征向焦为 $p_{1}=(1,1,1)^{\top}$, 求 $\boldsymbol{A}$.
24. 设 $a=\left(a_{1}, a_{2}, \cdots, a_{n}\right)^{\mathrm{T}}, a_{1} \neq 0, \boldsymbol{A}=\boldsymbol{a} a^{\mathrm{T}}$,

(1) 证明 $\lambda=0$ 是 $A$ 的 $n-1$ 重特征值;

（2）求 $\boldsymbol{A}$ 的非零特征值及 $n$ 个线性无关的特征向量.

25.（1）设 $A=\left(\begin{array}{rr}3 & -2 \\ -2 & 3\end{array}\right)$, 求 $\varphi(A)=A^{10}-5 A^{9}$;

(2) 设 $\boldsymbol{A}=\left(\begin{array}{lll}2 & 1 & 2 \\ 1 & 2 & 2 \\ 2 & 2 & 1\end{array}\right)$, 求 $\varphi(A)=A^{10}-6 A^{9}+5 A^{8}$.

26. 用矩阵记号表示下列二次型:

(1) $f=x^{2}+4 x y+4 y^{2}+2 x z+z^{2}+4 y z$;

(2) $f=x^{2}+y^{2}-7 z^{2}-2 x y-4 x z-4 y z$;

(3) $f=x_{1}^{2}+x_{2}^{2}+x_{3}^{2}-2 x_{1} x_{2}+6 x_{2} x_{3}$.

27. 写出下列二次型的矩阵:

$$
\text { (1) } f(x)=x^{T}\left(\begin{array}{ll}
2 & 1 \\
3 & 1
\end{array}\right) x ; \quad \text { (2) } f(x)=x^{T}\left(\begin{array}{lll}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{array}\right) x \text {. }
$$

28. 求一个正交变换化下列二次型成标准形:

(1) $f=2 x_{1}^{2}+3 x_{2}^{2}+3 x_{3}^{2}+4 x_{2} x_{3}$;

(2) $f=x_{1}^{2}+x_{3}^{2}+2 x_{1} x_{2}-2 x_{2} x_{3}$.

29. 求一个正交变换把二次曲面的方程

$$
3 x^{2}+5 y^{2}+5 z^{2}+4 x y-4 x z-10 y z=1
$$

化成标准方程.

30. 证明: 二次型 $f=\boldsymbol{x}^{\mathrm{T}} \boldsymbol{A x}$ 在 $\|\boldsymbol{x}\|=1$ 时的取大值为矩阵 $\boldsymbol{A}$ 的取大特征值.
31. 用配方法化下列二次型成规范形,并写出所用变换的矩阵:

(1) $f\left(x_{1}, x_{2}, x_{3}\right)=x_{1}^{2}+3 x_{2}^{2}+5 x_{3}^{2}+2 x_{1} x_{2}-4 x_{1} x_{3}$; (2) $f\left(x_{1}, x_{2}, x_{3}\right)=x_{1}^{2}+2 x_{3}^{2}+2 x_{1} x_{3}+2 x_{2} x_{3}$;

(3) $f\left(x_{1}, x_{2}, x_{3}\right)=2 x_{1}^{2}+x_{2}^{2}+4 x_{3}^{2}+2 x_{1} x_{2}-2 x_{2} x_{3}$.

32. 设 $f=x_{1}^{2}+x_{2}^{2}+5 x_{3}^{2}+2 a x_{1} x_{2}-2 x_{1} x_{3}+4 x_{2} x_{3}$

为正定二次型, 求 $a$.

33. 判定下列二次型的正定性;

(1) $f=-2 x_{1}^{2}-6 x_{2}^{2}-4 x_{3}^{2}+2 x_{1} x_{2}+2 x_{1} x_{3}$;

(2) $f=x_{1}^{2}+3 x_{2}^{2}+9 x_{3}^{2}-2 x_{1} x_{2}+4 x_{1} x_{3}$.

34. 证明对称阵 $A$ 为正定的充分必要条件是: 存在可逆矩阵 $U$, 使 $A=U^{\mathrm{T}} U$, 即 $A$ 与单 位阵 $\mathbf{E}$ 合同.

## *第六章 <br> 线性空间与线性变换

向量空间又称线性空间,是线性代数中一个最基本的概念. 在第四章中,我 们把有序数组叫做向量, 并介绍过向量空间的概念. 在这一章中, 我们要把这些 概念推广, 使向量及向量空间的概念更具一般性. 当然,推广后的向量概念也就 更加抽象化了.

## $\S 1$ 线性空间的定义与性质

定义 1 设 $V$ 是一个非空集合, 书为实数域. 如果对于任意两个元素 $\boldsymbol{\alpha}, \boldsymbol{\beta}$ $\in V$, 总有惟一的一个元素 $\gamma \in V$ 与之对应,称为 $\boldsymbol{\alpha}$ 与 $\boldsymbol{\beta}$ 的和, 记作 $\boldsymbol{\gamma}=\boldsymbol{\alpha}+\boldsymbol{\beta}$; 又对于任一数 $\lambda \in \mathbb{R}$ 与任一元素 $\alpha \in V$, 总有惟一的一个元素 $\delta \in V$ 与之对应, 称为 $\lambda$ 与 $\boldsymbol{\alpha}$ 的积, 记作 $\boldsymbol{\delta}=\lambda \boldsymbol{\alpha}$; 并且这两种运算满足以下八条运算规律 (设 $\boldsymbol{\alpha}$, $\boldsymbol{\beta}, \boldsymbol{\gamma} \in V ; \lambda, \mu \in \mathbb{R})$ :

(i) $\boldsymbol{\alpha}+\boldsymbol{\beta}=\boldsymbol{\beta}+\boldsymbol{\alpha}$;

(ii) $(\boldsymbol{\alpha}+\boldsymbol{\beta})+\boldsymbol{\gamma}=\boldsymbol{\alpha}+(\boldsymbol{\beta}+\boldsymbol{\gamma})$;

(iii) 在 $V$ 中存在零元素 0 ; 对任何 $\alpha \in V$,都有 $\alpha+0=\alpha$;

（iv）对任何 $\alpha \in V$,都有 $\alpha$ 的负元素 $\beta \in V$, 使 $\boldsymbol{\alpha}+\boldsymbol{\beta}=\mathbf{0}$;

(v) $1 \boldsymbol{\alpha}=\boldsymbol{\alpha}$;

(vi) $\lambda(\mu \boldsymbol{\alpha})=(\lambda \mu) \boldsymbol{\alpha}$;

(vii) $(\lambda+\mu) \boldsymbol{\alpha}=\lambda \boldsymbol{\alpha}+\mu \boldsymbol{\alpha}$;

(viii) $\lambda(\boldsymbol{\alpha}+\boldsymbol{\beta})=\lambda \boldsymbol{\alpha}+\lambda \boldsymbol{\beta}$.

那么, $V$ 就称为(实数域 $\mathbb{R}$ 上的) 向望空间 (或线性空间), $V$ 中的元素不论 其本来的性质如何,统称为(实)向量.

简言之, 凡满足上述八条规律的加法及乘数运算, 就称为线性运算; 凡定义 了线性运算的集合,就称向量空间.

在第四章中,我们把有序数组称为向量,并对它定义了加法和乘数运算,容易验 证这些运算满足上述八条规律. 最后，把对于运算为封闭的有序数组的集合称为向量 空间. 显然, 那些只是现在定义的特殊情形. 比较起来, 现在的定义有了很大的推广: 1. 向量不一定是有序数组;

2. 向量空间中的运算只要求满足上述八条运算规律, 当然也就不一定是有 序数组的加法及乘数运算.

下面举一些例子.

例 1 次数不超过 $n$ 的多项式的全体,记作 $P[x]_{n}$, 即

$$
P[x]_{n}=\left\{\boldsymbol{p}=a_{n} x^{n}+a_{n-1} x^{n-1}+\cdots+a_{1} x+a_{0} \mid a_{n}, \cdots, a_{1}, a_{0} \in \mathbb{R}\right\},
$$

对于通常的多项式加法、数乘多项式的乘法构成向量空间. 这是因为: 通常的多 项式加法、数乘多项式的乘法两种运算显然满足线性运算规律, 故只要验证 $P[x]_{n}$ 对运算封闭:

$$
\begin{aligned}
& \left(a_{n} x^{n}+\cdots+a_{1} x+a_{0}\right)+\left(b_{n} x^{n}+\cdots+b_{1} x+b_{0}\right) \\
= & \left(a_{n}+b_{n}\right) x^{n}+\cdots+\left(a_{1}+b_{1}\right) x+\left(a_{0}+b_{0}\right) \in P[x]_{n}, \\
& \lambda\left(a_{n} x^{n}+\cdots+a_{1} x+a_{0}\right) \\
= & \left(\lambda a_{n}\right) x^{n}+\cdots+\left(\lambda a_{1}\right) x+\left(\lambda a_{0}\right) \in P[x]_{n},
\end{aligned}
$$

所以 $P[x]_{n}$ 是一个向量空间.

例 $2 n$ 次多项式的全体

$$
Q[x]_{n}=\left\{\boldsymbol{p}=a_{n} x^{n}+\cdots+a_{1} x+a_{0} \mid a_{n}, \cdots, a_{1}, a_{0} \in \mathbb{R}, \text { 且 } a_{n} \neq 0\right\}
$$

对于通常的多项式加法和乘数运算不构成向量空间. 这是因为

$$
0 p=0 x^{n}+\cdots+0 x+0 \notin Q[x]_{n},
$$

即 $Q[x]_{n}$ 对运算不封闭.

例 3 正弦函数的集合

$$
S[x]=\{s=A \sin (x+B) \mid A, B \in \mathbb{R}\}
$$

对于通常的函数加法及数乘函数的乘法构成向量空间. 这是因为: 通常的函数加 法及乘数运算显然满足线性运算规律,故只要验证 $S[x]$ 对运算封闭:

$$
\begin{aligned}
& s_{1}+s_{2}=A_{1} \sin \left(x+B_{1}\right)+A_{2} \sin \left(x+B_{2}\right) \\
& =\left(a_{1} \cos x+b_{1} \sin x\right)+\left(a_{2} \cos x+b_{2} \sin x\right) \\
& =\left(a_{1}+a_{2}\right) \cos x+\left(b_{1}+b_{2}\right) \sin x \\
& =A \sin (x+B) \in S[x] \text {, } \\
& \lambda s_{1}=\lambda A_{1} \sin \left(x+B_{1}^{\prime}\right)=\left(\lambda A_{1}\right) \sin \left(x+B_{1}\right) \in S[x],
\end{aligned}
$$

所以 $S[x]$ 是一个向量空间.

检验一个集合是否构成向量空间, 当然不能只检验对运算的封闭性(如上面 二例). 若所定义的加法和乘数运算不是通常的实数间的加乘运算, 则就应仔细 检验是否满足八条线性运算规律.

例 $4 n$ 个有序实数组成的数组的全体

$$
S^{n}=\left\{\boldsymbol{x}=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} \mid x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

对于通常的有序数组的加法及如下定义的乘法

$$
\lambda \cdot\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}=(0, \cdots, 0)^{\mathrm{T}}
$$

不构成向空空间.

可以验证 $S^{n}$ 对运算封闭. 但因 $1 \cdot x=0$, 不满足运算规律 $\mathrm{v}$, 即所定义的运 算不是线性运算,所以 $S^{n}$ 不是向量空间.

比较 $S^{n}$ 与 $\mathbb{R}^{n}$,作为集合它们是一样的,但由于在其中所定义的运算不同, 以致 $\mathbb{R}^{n}$ 构成向空间而 $S^{n}$ 不是向量空间. 由此可见，向量空间的概念是集合与 运算二者的结合.一般的说, 同一个集合,若定义两种不同的线性运算,就构成不 同的向量空间; 若定义的运算不是线性运算,就不能构成向量空间.所以,所定义 的线性运算是向墨空间的本质, 而其中的元尞是什么倒并不重要. 由此可以说， 把向量空间叫做线性空间更为合适.

为了对线性运算的理解更具有一般性,请看下例.

例 5 正实数的全体,记作 $\mathbb{R}^{+}$, 在其中定义加法及乘数运算为

$$
\begin{gathered}
a \oplus b=a b\left(a, b \in \mathbb{R}^{+}\right), \\
\lambda \circ a=a^{\lambda}\left(\lambda \in \mathbb{R}, a \in \mathbb{R}^{+}\right),
\end{gathered}
$$

验证 $\mathbb{R}^{+}$对上述加法与乘数运算构成线性空间.

证实际上要验证十条:

对加法封闭: 对任意的 $a, b \in \mathbb{R}^{+}$, 有 $a \oplus b=a b \in \mathbb{R}^{+}$;

对乘数封闭: 对任意的 $\lambda \in \mathbb{R}, a \in \mathbb{R}^{+}$, 有 $\lambda \circ a=a^{\lambda} \in \mathbb{R}^{+}$;

(i) $a \oplus b=a b=b a=b \oplus a$;

(ii) $(a \oplus b) \oplus c=(a b) \oplus c=(a b) c=a(b c)=a \oplus(b \oplus c)$;

(iii) $\mathbb{R}^{+}$中存在零元素 1 , 对任何 $a \in \mathbb{R}^{+}$, 有 $a \oplus 1=a \cdot 1=a$;

(iv) 对任何 $a \in \mathbb{R}^{+}$, 有负元素 $a^{-1} \in \mathbb{R}^{+}$, 使 $a \oplus a^{-1}=a a^{-1}=1$;

(v) $1 \circ a=a^{1}=a$;

(vi) $\lambda \circ(\mu \circ a)=\lambda \circ a^{\mu}=\left(a^{\mu}\right)^{\lambda}=a^{\lambda \mu}=(\lambda \mu) \circ a$;

(vii) $(\lambda+\mu) \circ a=a^{\lambda+\mu}=a^{\lambda} a^{\mu}=a^{\lambda} \oplus a^{\mu}=\lambda \circ a \oplus \mu^{\circ} a$;

(viii) $\lambda \circ(a \oplus b)=\lambda \circ(a b)=(a b)^{\lambda}=a^{\lambda} b^{\lambda}=a^{\lambda} \oplus b^{\lambda}=\lambda \circ a \oplus \lambda \circ b$.

因此, $\mathbb{R}^{+}$对于所定义的运算构成线性空间.

下面讨论线性空间的性质.

1. 零元軞是惟一的

证 设 $0_{1}, \mathbf{0}_{2}$ 是线性空间 $V$ 中的两个零元素, 即对任何 $\alpha \in V$, 有 $\alpha+\mathbf{0}_{1}=$ $\boldsymbol{\alpha}, \boldsymbol{\alpha}+\boldsymbol{0}_{2}=\boldsymbol{\alpha}$. 于是特别有

所以

$$
\mathbf{0}_{2}+\mathbf{0}_{1}=\mathbf{0}_{2}, \mathbf{0}_{1}+\mathbf{0}_{2}=\mathbf{0}_{1} \text {, }
$$

$$
0_{1}=0_{1}+0_{2}=0_{2}+0_{1}=0_{2} \text {. }
$$ 

2. 任一元素的负元索是惟一的. $\boldsymbol{\alpha}$ 的负元素记作 $-\boldsymbol{\alpha}$.

证 设 $\alpha$ 有两个负元素 $\boldsymbol{\beta}, \boldsymbol{\gamma}$, 即 $\boldsymbol{\alpha}+\boldsymbol{\beta}=\mathbf{0}, \boldsymbol{\alpha}+\boldsymbol{\gamma}=\mathbf{0}$. 于是

$$
\beta=\beta+0=\beta+(\alpha+\gamma)=(\alpha+\beta)+\gamma=0+\gamma=\gamma \text {. }
$$

3. $0 \alpha=0 ;(-1) \alpha=-\alpha ; \lambda 0=0$.

证 $\alpha+0 \alpha=1 \alpha+0 \alpha=(1+0) \alpha=1 \alpha=\alpha$, 所以 $0 \alpha=0$,

$$
\alpha+(-1) \alpha=1 \alpha+(-1) \alpha=[1+(-1)] \alpha=0 \alpha=0,
$$

所以

$$
(-1) \boldsymbol{\alpha}=-\boldsymbol{\alpha}
$$

$$
\lambda \mathbf{0}=\lambda[\boldsymbol{\alpha}+(-1) \boldsymbol{\alpha}]=\lambda \boldsymbol{\alpha}+(-\lambda) \boldsymbol{\alpha}=[\lambda+(-\lambda)] \boldsymbol{\alpha}=\mathbf{0} \boldsymbol{\alpha}=\mathbf{0} .
$$

4. 如果 $\lambda \alpha=0$, 则 $\lambda=0$ 或 $\alpha=0$.

证 若 $\lambda \neq 0$, 在 $\lambda \alpha=0$ 两边乘 $\frac{1}{\lambda}$, 得

$$
\frac{1}{\lambda}(\lambda \boldsymbol{\alpha})=\frac{1}{\lambda} \boldsymbol{0}=\mathbf{0},
$$

而

$$
\frac{1}{\lambda}(\lambda \alpha)=\left(\frac{1}{\lambda} \lambda\right) \boldsymbol{\alpha}=1 \boldsymbol{\alpha}=\boldsymbol{\alpha},
$$

所以

$$
\boldsymbol{\alpha}=\mathbf{0} \text {. }
$$

## $\S 2$ 维数、基与坐标

在第四章中,我们用线性运算来讨论 $n$ 维数组向量之间的关系,介绍了一 些重要概念,如线性组合、线性相关与线性无关等等. 这些概念以及有关的性质 只涉及线性运算，因此，对于一般的线性空间中的元素仍然适用. 以后我们将直 接引用这些概念和性质.

在第四章中我们已经提出了基与维数的概念,这当然也适用于一般的线性 空间.这是线性空间的主要特性,特再叙述如下.

定义 2 在线性空间 $V$ 中, 如果存在 $n$ 个元素 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$, 满足:

(i) $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 线性无关;

（ii） $V$ 中任一元素 $\boldsymbol{\alpha}$ 总可由 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 线性表示,

那么, $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 就称为线性空间 $V$ 的一个基, $n$ 称为线性空间 $V$ 的 维数. 只含一个零元素的线性空间没有基,规定它的维数为 0 .

维数为 $n$ 的线性空间称为 $n$ 维线性空间, 记作 $V_{n}$.

这里要指出:线性空间的维数可以是无穷. 对于无穷维的线性空间,本书不 作讨论.

对于 $n$ 维线性空间 $V_{n}$, 若知 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 为 $V_{n}$ 的一个基,则 $V_{n}$ 可表示 为

$$
V_{n}=\left\{\boldsymbol{\alpha}=x_{1} \boldsymbol{\alpha}_{1}+x_{2} \boldsymbol{\alpha}_{2}+\cdots+x_{n} \boldsymbol{\alpha}_{n} \mid x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}\right\}
$$

即 $V_{n}$ 是基所生成的线性空间,这就较清楚地显示出线性空间 $V_{n}$ 的构造.

若 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 为 $V_{n}$ 的一个基, 则对任何 $\alpha \in V_{n}$, 都有倠一的一组有序 数 $x_{1}, x_{2}, \cdots, x_{n}$, 使

$$
\boldsymbol{\alpha}=x_{1} \boldsymbol{\alpha}_{1}+x_{2} \boldsymbol{\alpha}_{2}+\cdots+x_{n} \boldsymbol{\alpha}_{n} ;
$$

反之,任给一组有序数 $x_{1}, x_{2}, \cdots, x_{n}$, 总有惟一的元素

$$
\boldsymbol{\alpha}=x_{1} \boldsymbol{\alpha}_{1}+x_{2} \boldsymbol{\alpha}_{2}+\cdots+x_{n} \boldsymbol{\alpha}_{n} \in V_{n} .
$$

这样 $V_{n}$ 的元素 $\boldsymbol{\alpha}$ 与有序数组 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}}$ 之间存在着一种一一对应 的关系, 因此可以用这组有序数来表示元素 $\boldsymbol{\alpha}$.于是我们有

定义 3 设 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 是线性空间 $V_{n}$ 的一个基. 对于任一元素 $\alpha \in V_{n}$, 总有且仅有一组有序数 $x_{1}, x_{2}, \cdots, x_{n}$ 使

$$
\boldsymbol{\alpha}=x_{1} \boldsymbol{\alpha}_{1}+x_{2} \boldsymbol{\alpha}_{2}+\cdots+x_{n} \boldsymbol{\alpha}_{n},
$$

$x_{1}, x_{2}, \cdots, x_{n}$ 这组有序数就称为元素 $\boldsymbol{\alpha}$ 在 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 这个基下的坐标, 并记 作

$$
\alpha=\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}} .
$$

例 6 在线性空间 $P[x]_{4}$ 中, $p_{1}=1, p_{2}=x, p_{3}=x^{2}, p_{4}=x^{3}, p_{5}=x^{4}$ 就是 它的一个基.任一不超过 4 次的多项式

$$
p=a_{4} x^{4}+a_{3} x^{3}+a_{2} x^{2}+a_{1} x+a_{0}
$$

都可表示为

$$
\boldsymbol{p}=a_{0} \boldsymbol{p}_{1}+a_{1} \boldsymbol{p}_{2}+a_{2} \boldsymbol{p}_{3}+a_{3} \boldsymbol{p}_{4}+a_{4} \boldsymbol{p}_{5},
$$

因此 $p$ 在这个基下的坐标为 $\left(a_{0}, a_{1}, a_{2}, a_{3}, a_{4}\right)^{\mathrm{T}}$.

若另取一个基 $q_{1}=1, q_{2}=1+x, q_{3}=2 x^{2}, q_{4}=x^{3}, q_{5}=x^{4}$, 则

$$
\boldsymbol{p}=\left(a_{0}-a_{1}\right) \boldsymbol{q}_{1}+a_{1} \boldsymbol{q}_{2}+\frac{1}{2} a_{2} \boldsymbol{q}_{3}+a_{3} \boldsymbol{q}_{4}+a_{4} \boldsymbol{q}_{5},
$$

因此 $\boldsymbol{p}$ 在这个基下的坐标为 $\left(a_{0}-a_{1}, a_{1}, \frac{1}{2} a_{2}, a_{3}, a_{4}\right)^{\mathrm{T}}$.

建立了坐标以后, 就把抽象的向量 $\boldsymbol{\alpha}$ 与具体的数组向啙 $\left(x_{1}, x_{2}, \cdots, x_{n}\right)^{\mathrm{T}}$ 联系起来了. 并且还可把 $V_{n}$ 中抽象的线性运算与数组向量的线性运算联系起 来.

设 $\alpha, \beta \in V_{n}$, 有 $\alpha=x_{1} \alpha_{1}+\cdots+x_{n} \alpha_{n}, \boldsymbol{\beta}=y_{1} \alpha_{1}+\cdots+y_{n} \alpha_{n}$, 于是

$$
\begin{gathered}
\boldsymbol{\alpha}+\boldsymbol{\beta}=\left(x_{1}+y_{1}\right) \boldsymbol{\alpha}_{1}+\cdots+\left(x_{n}+y_{n}\right) \boldsymbol{\alpha}_{n}, \\
\lambda \boldsymbol{\alpha}=\left(\lambda x_{1}\right) \boldsymbol{\alpha}_{1}+\cdots+\left(\lambda x_{n}\right) \boldsymbol{\alpha}_{n},
\end{gathered}
$$

即 $\boldsymbol{\alpha}+\boldsymbol{\beta}$ 的坐标是 $\left(x_{1}+y_{1}, \cdots, x_{n}+y_{n}\right)^{\mathrm{T}}=\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}+\left(y_{1}, \cdots, y_{n}\right)^{\mathrm{T}}, \lambda \boldsymbol{\alpha}$ 的 坐标是 $\left(\lambda x_{1}, \cdots, \lambda x_{n}\right)^{\mathrm{T}}=\lambda\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}$. 总之, 设在 $n$ 维线性空间 $V_{n}$ 中取定一个基 $\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}$, 则 $V_{n}$ 中的向量 $\boldsymbol{\alpha}$ 与 $n$ 维数组向量空间 $\mathbb{R}^{n}$ 中的向量 $\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}$ 之间就有一个一一对应的关系, 且 这个对应关系具有下述性质:

设 $\boldsymbol{\alpha} \leftrightarrow\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}, \boldsymbol{\beta} \leftrightarrow\left(y_{1}, \cdots, y_{n}\right)^{\mathrm{T}}$, 则

(i) $\boldsymbol{\alpha}+\boldsymbol{\beta} \leftrightarrow\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}+\left(y_{1}, \cdots, y_{n}\right)^{\mathrm{T}}$;

(ii) $\lambda \alpha \leftrightarrow \lambda\left(x_{1}, \cdots, x_{n}\right)^{\mathrm{T}}$.

也就是说, 这个对应关系保持线性组合的对应. 因此, 我们可以说 $V_{n}$ 与 $\mathbb{R}^{n}$ 有相同的结构,我们称 $V_{n}$ 与 $\mathbb{R}^{n}$ 同构.

一般的,设 $V$ 与 $U$ 是两个线性空间, 如果在它们的元素之间有一一对应关 系,且这个对应关系保持线性组合的对应,那么就说线性空间 $V$ 与 $U$ 同构.

显然,任何 $n$ 维线性空间都与 $\mathbb{R}^{n}$ 同构,即维数相等的线性空间都同构. 从而 可知线性空间的结构完全被它的维数所决定.

同构的概念除元素一一对应外,主要是保持线性运算的对应关系. 因此, $V_{n}$ 中的抽象的线性运算就可转化为 $\mathbb{R}^{n}$ 中的线性运算,并且 $\mathbb{R}^{n}$ 中凡是只涉及线性运 算的性质就都适用于 $V_{n}$. 但 $\mathbb{R}^{n}$ 中超出线性运算的性质,在 $V_{n}$ 中就不一定具备, 例如 $\mathbb{R}^{n}$ 中的内积概念在 $V_{n}$ 中就不一定有意义.

## $\S 3$ 基变换与坐标变换

由例 6 可见, 同一元素在不同的基下有不同的坐标, 那么,不同的基与不同 的坐标之间有怎样的关系呢?

设 $\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}$ 及 $\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}$ 是线性空间 $V_{n}$ 中的两个基,

$$
\left\{\begin{array}{l}
\boldsymbol{\beta}_{1}=p_{11} \boldsymbol{\alpha}_{1}+p_{21} \boldsymbol{\alpha}_{2}+\cdots+p_{n 1} \boldsymbol{\alpha}_{n}, \\
\boldsymbol{\beta}_{2}=p_{12} \boldsymbol{\alpha}_{1}+p_{22} \boldsymbol{\alpha}_{2}+\cdots+p_{n 2} \boldsymbol{\alpha}_{n}, \\
\cdots \cdots \cdots \cdots \\
\boldsymbol{\beta}_{n}=p_{1 n} \boldsymbol{\alpha}_{1}+p_{2 n} \boldsymbol{\alpha}_{2}+\cdots+p_{n n} \boldsymbol{\alpha}_{n},
\end{array}\right.
$$

把 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 这 $n$ 个有序元素记作 $\left(\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}\right)$, 利用向量和矩阵的形 式,(1)式可表示为

$$
\left(\begin{array}{c}
\boldsymbol{\beta}_{1} \\
\boldsymbol{\beta}_{2} \\
\vdots \\
\boldsymbol{\beta}_{n}
\end{array}\right)=\left(\begin{array}{cccc}
p_{11} & p_{21} & \cdots & p_{n 1} \\
p_{12} & p_{22} & \cdots & p_{n 2} \\
\vdots & \vdots & & \vdots \\
p_{1 n} & p_{2 n} & \cdots & p_{n n}
\end{array}\right)\left(\begin{array}{c}
\boldsymbol{\alpha}_{1} \\
\boldsymbol{\alpha}_{2} \\
\vdots \\
\boldsymbol{\alpha}_{n}
\end{array}\right)=\boldsymbol{P}^{\mathrm{T}}\left(\begin{array}{c}
\boldsymbol{\alpha}_{1} \\
\boldsymbol{\alpha}_{2} \\
\vdots \\
\boldsymbol{\alpha}_{n}
\end{array}\right),
$$

或

$$
\left(\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}\right)=\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{P} .
$$

(1)或 (2) 称为基恋换公式,矩阵 $\boldsymbol{P}$ 称为由基 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 到基 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots$, $\boldsymbol{\beta}_{n}$ 的过渡矩阵. 由于 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}$ 线性无关,故过渡矩阵 $\boldsymbol{P}$ 可逆.

定理 1 设 $V_{n}$ 中的元素 $\boldsymbol{\alpha}$, 在基 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 下的坐标为 $\left(x_{1}, x_{2}, \cdots\right.$, $\left.x_{n}\right)^{\mathrm{T}}$, 在基 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}$ 下的坐标为 $\left(x^{\prime}{ }_{1}, x^{\prime}{ }_{2}, \cdots, x^{\prime}{ }_{n}\right)^{\mathrm{T}}$. 若两个基满足关系式 (2), 则有坐禁变换公式

$$
\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)=\mathbf{P}\left(\begin{array}{c}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
\vdots \\
x_{n}^{\prime}
\end{array}\right) \text {, 或 }\left(\begin{array}{c}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
\vdots \\
x_{n}^{\prime}
\end{array}\right)=\mathbf{P}^{-1}\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right) .
$$

证 因

$$
\begin{aligned}
\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)=\boldsymbol{\alpha} & =\left(\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}\right)\left(\begin{array}{c}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
\vdots \\
x^{\prime}{ }_{n}
\end{array}\right) \\
& =\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{P}\left(\begin{array}{c}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
\vdots \\
x^{\prime}{ }_{n}
\end{array}\right),
\end{aligned}
$$

由于 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 线性无关,故即有关系式(3).

这个定理的逆命题也成立. 即若任一元素的两种坐标满足坐标变换公式 (3),则两个基满足基变换公式(2).

例 7 在 $P[x]_{3}$ 中取两个基

$$
\begin{array}{ll}
\boldsymbol{\alpha}_{1}=x^{3}+2 x^{2}-x, & \boldsymbol{\alpha}_{2}=x^{3}-x^{2}+x+1, \\
\boldsymbol{\alpha}_{3}=-x^{3}+2 x^{2}+x+1, & \boldsymbol{\alpha}_{4}=-x^{3}-x^{2}+1 ;
\end{array}
$$

及 $\boldsymbol{\beta}_{1}=2 x^{3}+x^{2}+1$,

$$
\boldsymbol{\beta}_{2}=x^{2}+2 x+2 \text {, }
$$

$$
\boldsymbol{\beta}_{3}=-2 x^{3}+x^{2}+x+2, \quad \boldsymbol{\beta}_{4}=x^{3}+3 x^{2}+x+2 \text {. }
$$

求坐标变换公式.

解 将 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \boldsymbol{\beta}_{3}, \boldsymbol{\beta}_{4}$, 用 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}$ 表示. 由

$$
\begin{gathered}
\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}\right)=\left(x^{3}, x^{2}, x, 1\right) \boldsymbol{A}, \\
\left(\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \boldsymbol{\beta}_{3}, \boldsymbol{\beta}_{4}\right)=\left(x^{3}, x^{2}, x, 1\right) \boldsymbol{B},
\end{gathered}
$$

其中 $\quad \boldsymbol{A}=\left(\begin{array}{rrrr}1 & 1 & -1 & -1 \\ 2 & -1 & 2 & -1 \\ -1 & 1 & 1 & 0 \\ 0 & 1 & 1 & 1\end{array}\right), \boldsymbol{B}=\left(\begin{array}{rrrr}2 & 0 & -2 & 1 \\ 1 & 1 & 1 & 3 \\ 0 & 2 & 1 & 1 \\ 1 & 2 & 2 & 2\end{array}\right)$,

得 $\left(\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \boldsymbol{\beta}_{3}, \boldsymbol{\beta}_{4}\right)=\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \boldsymbol{\alpha}_{3}, \boldsymbol{\alpha}_{4}\right) \boldsymbol{A}^{-1} B$,

故坐标变换公式为

$$
\left(\begin{array}{l}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
x^{\prime}{ }_{3} \\
x^{\prime}{ }_{4}
\end{array}\right)=\boldsymbol{B}^{-1} \boldsymbol{A}\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right) \text {. }
$$

用矩阵的初等行变换求 $\boldsymbol{B}^{-1} \boldsymbol{A}$ : 把矩阵 $(\boldsymbol{B}, \boldsymbol{A})$ 中的 $\boldsymbol{B}$ 变成 $\boldsymbol{E}$, 则 $\boldsymbol{A}$ 即变成 $\boldsymbol{B}^{-1} \boldsymbol{A}$. 计算如下

$$
\begin{aligned}
& (\boldsymbol{B}, \boldsymbol{A})=\left(\begin{array}{rrrr:rrrr}
2 & 0 & -2 & 1 & 1 & 1 & -1 & -1 \\
1 & 1 & 1 & 3 & 2 & -1 & 2 & -1 \\
0 & 2 & 1 & 1 & -1 & 1 & 1 & 0 \\
1 & 2 & 2 & 2 & 0 & 1 & 1 & 1
\end{array}\right) \\
& \frac{r_{1}-2 r_{2}}{r_{4}-r_{2}}\left(\begin{array}{rrrr:rrrr}
0 & -2 & -4 & -5 & -3 & 3 & -5 & 1 \\
1 & 1 & 1 & 3 & 2 & -1 & 2 & -1 \\
0 & 2 & 1 & 1 & -1 & 1 & 1 & 0 \\
0 & 1 & 1 & -1 & -2 & 2 & -1 & 2
\end{array}\right) \\
& \begin{array}{r}
r_{1}+2 r_{4} \\
r_{2}-r_{4} \\
r_{3}-2 r_{4}
\end{array}\left(\begin{array}{rrrr:rrrr}
0 & 0 & -2 & -7 & -7 & 7 & -7 & 5 \\
1 & 0 & 0 & 4 & 4 & -3 & 3 & -3 \\
0 & 0 & -1 & 3 & 3 & -3 & 3 & -4 \\
0 & 1 & 1 & -1 & -2 & 2 & -1 & 2
\end{array}\right) \\
& \frac{r_{1}-2 r_{3}}{r_{4}+r_{3}}\left(\begin{array}{rrrr:rrrr}
0 & 0 & 0 & -13 & -13 & 13 & -13 & 13 \\
1 & 0 & 0 & 4 & 4 & -3 & 3 & -3 \\
0 & 0 & -1 & 3 & 3 & -3 & 3 & -4 \\
0 & 1 & 0 & 2 & 1 & -1 & 2 & -2
\end{array}\right)
\end{aligned}
$$

$$
\begin{aligned}
& \begin{array}{c}
r_{1} \div(-13) \\
r_{2}-4 r_{1} \\
r_{3}-3 r_{1} \\
r_{4}-2 r_{1}
\end{array}\left(\begin{array}{rrrr:rrrr}
0 & 0 & 0 & 1 & 1 & -1 & 1 & -1 \\
1 & 0 & 0 & 0 & 0 & 1 & -1 & 1 \\
0 & 0 & -1 & 0 & 0 & 0 & 0 & -1 \\
0 & 1 & 0 & 0 & -1 & 1 & 0 & 0
\end{array}\right) \\
& \underset{\frac{r_{1} \rightarrow r_{3} \div(-1)}{r_{2}-r_{4}}}{\frac{r_{4}}{4}}\left(\begin{array}{llll:rrrr}
1 & 0 & 0 & 0 & 0 & 1 & -1 & 1 \\
0 & 1 & 0 & 0 & -1 & 1 & 0 & 0 \\
0 & 0 & 1 & 0 & 0 & 0 & 0 & 1 \\
0 & 0 & 0 & 1 & 1 & -1 & 1 & -1
\end{array}\right) \text {, } \\
& \left(\begin{array}{l}
x^{\prime}{ }_{1} \\
x^{\prime}{ }_{2} \\
x^{\prime}{ }_{3} \\
x^{\prime}{ }_{4}
\end{array}\right)=\left(\begin{array}{rrrr}
0 & 1 & -1 & 1 \\
-1 & 1 & 0 & 0 \\
0 & 0 & 0 & 1 \\
1 & -1 & 1 & -1
\end{array}\right)\left(\begin{array}{l}
x_{1} \\
x_{2} \\
x_{3} \\
x_{4}
\end{array}\right) \text {. }
\end{aligned}
$$

## $\S 4$ 线 性 变 换

定义 4 设有两个非空集合 $A, B$, 如果对于 $A$ 中任一元素 $\alpha$, 按照一定的 规则, 总有 $B$ 中一个确定的元索 $\beta$ 和它对应, 那么, 这个对应规则称为丛集合 $A$ 烈焦合 $B$ 的映射. 我们常用字母表示一个映射, 暨如把上述映射记作 $T$, 并记

$$
\beta=T(\alpha) \text { 或 } \beta=T \alpha(\alpha \in A) .
$$

设 $\alpha_{1} \in A, T\left(\alpha_{1}\right)=\beta_{1}$, 就说映射 $T$ 把元素 $\alpha_{1}$ 变为 $\beta_{1}, \beta_{1}$ 称为 $\alpha_{1}$ 在映射 $T$ 下的像, $\alpha_{1}$ 称为 $\beta_{1}$ 在映射 $T$ 下的源. $A$ 称为映射 $T$ 的源焦. 像的全体所构成 的集合称为像焦, 记作 $T(A)$, 即

$$
\left.T(A)=|\beta=T(\alpha)|_{\alpha} \in A\right\},
$$

显然 $T(A) \subset B$.

映射的概念是函数概念的推广. 例如, 设二元函数 $z=f(x, y)$ 的定义域为 平面区域 $G$, 函数值域为 $Z$, 那么, 函数关系 $f$ 就是一个从定义域 $G$ 到实数域 $\mathbb{R}$ 的映射; 函数值 $f\left(x_{0}, y_{0}\right)=z_{0}$ 就是元素 $\left(x_{0}, y_{0}\right)$ 的像, $\left(x_{0}, y_{0}\right)$ 就是 $z_{0}$ 的源; $G$ 就是源集, $Z$ 就是像集.

定义 5 设 $V_{n}, U_{m}$ 分别是 $n$ 维和 $m$ 维线性空间, $T$ 是一个从 $V_{n}$ 到 $U_{m}$ 的 映射,如果映射 $T$ 满足:

(i) 任给 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2} \in V_{n}$ (从而 $\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2} \in V_{n}$ ), 有

$$
T\left(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}\right)=T\left(\boldsymbol{\alpha}_{1}\right)+T\left(\boldsymbol{\alpha}_{2}\right) ;
$$

(ii) 任给 $\boldsymbol{\alpha} \in V_{n}, \lambda \in \mathbb{R}$ (从而 $\lambda \boldsymbol{\alpha} \in V_{n}$ ), 有

$$
T(\lambda \boldsymbol{\alpha})=\lambda T(\boldsymbol{\alpha}),
$$

那么, $T$ 就称为从 $V_{n}$ 到 $U_{m}$ 的线性映射, 或称为线性变换.

简言之,线性映射就是保持线性组合的对应的映射.

例如, 关系式

$$
\left(\begin{array}{c}
y_{1} \\
y_{2} \\
\vdots \\
y_{m}
\end{array}\right)=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{m 1} & a_{m 2} & \cdots & a_{m n}
\end{array}\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)
$$

就确定了一个从 $\mathbb{R}^{n}$ 到 $\mathbb{R}^{m}$ 的映射,并且是个线性映射(参看后面的例 10).

特别, 在定义 5 中, 如果 $U_{m}=V_{n}$, 那么 $T$ 是一个从线性空间 $V_{n}$ 到其自身 的线性映射,称为线性空间 $V_{n}$ 中的线性变换.

下面我们只讨论线性空间 $V_{n}$ 中的线性变换.

例 8 在线性空间 $P[x]_{3}$ 中,

(1) 微分运算 D 是一个线性变换. 这是因为

任取 $p=a_{3} x^{3}+a_{2} x^{2}+a_{1} x+a_{0} \in P[x]_{3}$,

$$
\begin{aligned}
& \mathrm{D} p=3 a_{3} x^{2}+2 a_{2} x+a_{1}, \\
& q=b_{3} x^{3}+b_{2} x^{2}+b_{1} x+b_{0} \in P[x]_{3}, \\
& \mathrm{D} q=3 b_{3} x^{2}+2 b_{2} x+b_{1},
\end{aligned}
$$

有 $\mathrm{D}(\boldsymbol{p}+q)=\mathrm{D}\left[\left(a_{3}+b_{3}\right) x^{3}+\left(a_{2}+b_{2}\right) x^{2}+\left(a_{1}+b_{1}\right) x+\left(a_{0}+b_{0}\right)\right]$

$$
\begin{aligned}
& =3\left(a_{3}+b_{3}\right) x^{2}+2\left(a_{2}+b_{2}\right) x+\left(a_{1}+b_{1}\right) \\
& =\left(3 a_{3} x^{2}+2 a_{2} x+a_{1}\right)+\left(3 b_{3} x^{2}+2 b_{2} x+b_{1}\right) \\
& =\mathrm{D} p+\mathrm{D} \boldsymbol{q} ; \\
& \quad \mathrm{D}(\lambda \boldsymbol{p})=\mathrm{D}\left(\lambda a_{3} x^{3}+\lambda a_{2} x^{2}+\lambda a_{1} x+\lambda a_{0}\right) \\
& =\lambda\left(3 a_{3} x^{2}+2 a_{2} x+a_{1}\right)=\lambda \mathrm{D} p .
\end{aligned}
$$

(2) 如果 $T(\boldsymbol{p})=a_{0}$, 那么 $T$ 也是一个线性变换. 这是因为

$$
\begin{gathered}
T(\boldsymbol{p}+\boldsymbol{q})=a_{0}+b_{0}=T(\boldsymbol{p})+T(\boldsymbol{q}) ; \\
T(\lambda \boldsymbol{p})=\lambda a_{0}=\lambda T(\boldsymbol{p}) .
\end{gathered}
$$

(3) 如果 $T_{1}(\boldsymbol{p})=1$, 那么 $T_{1}$ 是个变换, 但不是线性变换. 这是因为 $T_{1}(\boldsymbol{p}$ $+q)=1$, 而 $T_{1}(p)+T_{1}(q)=1+1=2$, 故

$$
T_{1}(p+q) \neq T_{1}(p)+T_{1}(q) \text {. }
$$

例 9 由关系式

$$
T\left(\begin{array}{l}
x \\
y
\end{array}\right)=\left(\begin{array}{rr}
\cos \varphi & -\sin \varphi \\
\sin \varphi & \cos \varphi
\end{array}\right)\left(\begin{array}{l}
x \\
y
\end{array}\right)
$$

确定 $x O y$ 平面上的一个变换 $T$, 说明变换 $T$ 的几何意义(参看第二章图 2.3) ,

解 记 $\left\{\begin{array}{l}x=r \cos \theta, \\ y=r \sin \theta,\end{array}\right.$ 于是

$$
\begin{aligned}
T\left(\begin{array}{l}
x \\
y
\end{array}\right) & =\left(\begin{array}{l}
x \cos \varphi-y \sin \varphi \\
x \sin \varphi+y \cos \varphi
\end{array}\right)=\left(\begin{array}{l}
r \cos \theta \cos \varphi-r \sin \theta \sin \varphi \\
r \cos \theta \sin \varphi+r \sin \theta \cos \varphi
\end{array}\right) \\
& =\left(\begin{array}{l}
r \cos (\theta+\varphi) \\
r \sin (\theta+\varphi)
\end{array}\right),
\end{aligned}
$$

这表示变换 $T$ 把任一向量按逆时针方向旋转 $\varphi$ 角 (由例 10 可知这个变换是一 个线性变换).

线性变换具有下述基本性质:

(i) $T \mathbf{0}=\mathbf{0}, T(-\boldsymbol{\alpha})=-T \boldsymbol{\alpha}$;

(ii) 若 $\boldsymbol{\beta}=k_{1} \boldsymbol{\alpha}_{1}+k_{2} \boldsymbol{\alpha}_{2}+\cdots+k_{m} \boldsymbol{\alpha}_{m}$, 则

$$
T \boldsymbol{\beta}=k_{1} T \boldsymbol{\alpha}_{1}+k_{2} T \boldsymbol{\alpha}_{2}+\cdots+k_{m} T \boldsymbol{\alpha}_{m} ;
$$

（iii）若 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{m}$ 线性相关, 则 $T \alpha_{1}, T \alpha_{2}, \cdots, T \alpha_{m}$ 亦线性相关.

这些性质请读者证明之. 注意性质(iii) 的逆命题是不成立的, 即若 $\alpha_{1}, \alpha_{2}$, $\cdots, \boldsymbol{\alpha}_{m}$ 线性无关,则 $T \boldsymbol{\alpha}_{1}, T \boldsymbol{\alpha}_{2}, \cdots, T \boldsymbol{\alpha}_{m}$ 不一定线性无关.

(iv) 线性变换 $T$ 的像集 $T\left(V_{n}\right)$ 是一个线性空间，称为线性变换 $T$ 的像空 间.

证 设 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2} \in T\left(V_{n}\right)$, 则有 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2} \in V_{n}$, 使 $T \boldsymbol{\alpha}_{1}=\boldsymbol{\beta}_{1}, T \boldsymbol{\alpha}_{2}=\boldsymbol{\beta}_{2}$, 从而

$$
\begin{gathered}
\boldsymbol{\beta}_{1}+\boldsymbol{\beta}_{2}=T \boldsymbol{\alpha}_{1}+T \boldsymbol{\alpha}_{2}=T\left(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}\right) \in T\left(V_{n}\right)\left(\text { 因 } \boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2} \in V_{n}\right), \\
k \boldsymbol{\beta}_{1}=\lambda T \boldsymbol{\alpha}_{1}=T\left(\lambda \boldsymbol{\alpha}_{1}\right) \in T\left(V_{n}\right),\left(\text { 因 } \lambda \boldsymbol{\alpha}_{1} \in V_{n}\right),
\end{gathered}
$$

由上述证明知它对 $V_{n}$ 中的线性运算封闭,故它是一个线性空间.

(v) 使 $T \boldsymbol{\alpha}=0$ 的 $\boldsymbol{\alpha}$ 的全体

$$
S_{T}=\left\{\alpha \mid \alpha \in V_{n}, T \alpha=0\right\},
$$

也是一个线性空间. $S_{T}$ 称为线性变换 $T$ 的核.

证 $S_{T} \subset V_{n}$, 且

若 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2} \in S_{T}$, 即 $T \boldsymbol{\alpha}_{1}=\mathbf{0}, T \boldsymbol{\alpha}_{2}=\mathbf{0}$, 则 $T\left(\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2}\right)=T \boldsymbol{\alpha}_{1}+T \boldsymbol{\alpha}_{2}=\mathbf{0}$, 所以 $\boldsymbol{\alpha}_{1}+\boldsymbol{\alpha}_{2} \in S_{T}$;

若 $\boldsymbol{\alpha}_{1} \in S_{T}, \lambda \in \mathbb{R}$, 则 $T\left(\lambda \boldsymbol{\alpha}_{1}\right)=\lambda T \boldsymbol{\alpha}_{1}=\lambda \mathbf{0}=\mathbf{0}$, 所以 $\lambda \boldsymbol{\alpha}_{1} \in S_{T}$.

以上表明 $S_{T}$ 对线性运算封闭, 所以 $S_{T}$ 是一个线性空间.

例 10 设有 $n$ 阶矩阵

$$
\boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right)=\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right),
$$

其中

$$
\boldsymbol{\alpha}_{i}=\left(\begin{array}{c}
a_{1 i} \\
a_{2 i} \\
\vdots \\
a_{n i}
\end{array}\right),
$$

定义 $\mathbb{R}^{n}$ 中的变换 $\boldsymbol{y}=T(\boldsymbol{x})$ 为

$$
T(\boldsymbol{x})=\boldsymbol{A x}\left(\boldsymbol{x} \in \mathbb{R}^{n}\right),
$$

则 $T$ 为线性变换. 这是因为

设 $\boldsymbol{a}, \boldsymbol{b} \in \mathbb{R}^{n}$, 则

$$
\begin{gathered}
T(\boldsymbol{a}+\boldsymbol{b})=\boldsymbol{A}(\boldsymbol{a}+\boldsymbol{b})=\boldsymbol{A} \boldsymbol{a}+\boldsymbol{A} \boldsymbol{b}=T(\boldsymbol{a})+T(\boldsymbol{b}) ; \\
T(\lambda \boldsymbol{a})=\boldsymbol{A}(\lambda \boldsymbol{a})=\lambda \boldsymbol{A} \boldsymbol{a}=\lambda T(\boldsymbol{a}) .
\end{gathered}
$$

又, $T$ 的像空间就是由 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 所生成的向量空间

$$
T\left(\mathbb{R}^{n}\right)=\left\{y=x_{1} a_{1}+x_{2} a_{2}+\cdots+x_{n} a_{n} \mid x_{1}, x_{2}, \cdots, x_{n} \in \mathbb{R}\right\} ;
$$

$T$ 的核 $S_{T}$ 就是齐次线性方程组 $\boldsymbol{A x}=\mathbf{0}$ 的解空间.

## $\S 5$ 线性变换的矩阵表示式

上节例 10 中,关系式

$$
T(x)=A x \quad\left(x \in \mathbb{R}^{n}\right)
$$

简单明了地表示出 $\mathbb{R}^{n}$ 中的一个线性变换.我们自然希望 $\mathbb{R}^{n}$ 中任何一个线性变换 都能用这样的关系式来表示. 为此, 考虑到 $\alpha_{1}=A e_{1}, \cdots, \alpha_{n}=A e_{n}\left(e_{1}, \cdots, e_{n}\right.$ 为 单位坐标向量), 即

$$
\boldsymbol{\alpha}_{i}=T\left(\boldsymbol{e}_{i}\right) \quad(i=1,2, \cdots, n),
$$

可见如果线性变换 $T$ 有关系式 $T(\boldsymbol{x})=\boldsymbol{A} \boldsymbol{x}$, 那么矩阵 $\boldsymbol{A}$ 应以 $T\left(\boldsymbol{e}_{i}\right)$ 为列向量. 反之, 如果一个线性变换 $T$ 使 $T\left(\boldsymbol{e}_{i}\right)=\boldsymbol{\alpha}_{i}(i=1,2, \cdots, n)$, 那么 $T$ 必有关系式

$$
\begin{aligned}
T(\boldsymbol{x}) & =T\left[\left(e_{1}, \cdots, e_{n}\right) \boldsymbol{x}\right]=T\left(x_{1} e_{1}+x_{2} e_{2}+\cdots+x_{n} e_{n}\right) \\
& =x_{1} T\left(e_{1}\right)+x_{2} T\left(e_{2}\right)+\cdots+x_{n} T\left(e_{n}\right) \\
& =\left(T\left(e_{1}\right), \cdots, T\left(e_{n}\right)\right) x=\left(\alpha_{1}, \cdots, \boldsymbol{\alpha}_{n}\right) x=A x .
\end{aligned}
$$

总之, $\mathbb{R}^{n}$ 中任何线性变换 $T$,都能用关系式

$$
T(x)=A \boldsymbol{x} \quad\left(x \in \mathbb{R}^{n}\right)
$$

表示, 其中 $\boldsymbol{A}=\left(T\left(e_{1}\right), \cdots, T\left(e_{n}\right)\right)$.

把上面的讨论推广到一般的线性空间,我们有

定义 6 设 $T$ 是线性空间 $V_{n}$ 中的线性变换，在 $V_{n}$ 中取定一个基 $\boldsymbol{\alpha}_{1}$, $\boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$,如果这个基在变换 $T$ 下的像(用这个基线性表示)为

$$
\left\{\begin{array}{l}
T\left(\boldsymbol{\alpha}_{1}\right)=a_{11} \boldsymbol{\alpha}_{1}+a_{21} \boldsymbol{\alpha}_{2}+\cdots+a_{n 1} \boldsymbol{\alpha}_{n}, \\
T\left(\boldsymbol{\alpha}_{2}\right)=a_{12} \boldsymbol{\alpha}_{1}+a_{22} \boldsymbol{\alpha}_{2}+\cdots+a_{n 2} \boldsymbol{\alpha}_{n}, \\
\cdots \cdots \cdots \cdots \\
T\left(\boldsymbol{\alpha}_{n}\right)=a_{1 n} \boldsymbol{\alpha}_{1}+a_{2 n} \boldsymbol{\alpha}_{2}+\cdots+a_{n n} \boldsymbol{\alpha}_{n},
\end{array}\right.
$$

记 $T\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right)=\left(T\left(\boldsymbol{\alpha}_{1}\right), T\left(\boldsymbol{\alpha}_{2}\right), \cdots, T\left(\boldsymbol{\alpha}_{n}\right)\right)$, 上式可表示为

$$
T\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right)=\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{A}
$$

其中

$$
\boldsymbol{A}=\left(\begin{array}{cccc}
a_{11} & a_{12} & \cdots & a_{1 n} \\
a_{21} & a_{22} & \cdots & a_{2 n} \\
\vdots & \vdots & & \vdots \\
a_{n 1} & a_{n 2} & \cdots & a_{n n}
\end{array}\right),
$$

那么, $A$ 就称为线性变换 $T$ 在基 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 下的矩阵.

显然,矩阵 $\boldsymbol{A}$ 由基的像 $T\left(\boldsymbol{a}_{1}\right), \cdots, T\left(\boldsymbol{\alpha}_{n}\right)$ 惟一确定.

如果给出一个矩阵 $A$ 作为线性变换 $T$ 在基 $\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}$ 下的矩阵, 也就 是给出了这个基在变换 $T$ 下的像, 那么, 根据变换 $T$ 保持线性关系的特性, 我 们来推导变换 $T$ 必须满足的关系式

$V_{n}$ 中的任意元素记为 $\alpha=\sum_{i=1}^{n} x_{i} \boldsymbol{\alpha}_{i}$, 有

$$
\begin{aligned}
T\left(\sum_{i=1}^{n} x_{i} \boldsymbol{\alpha}_{i}\right) & =\sum_{i=1}^{n} x_{i} T\left(\boldsymbol{\alpha}_{i}\right) \\
& =\left(T\left(\alpha_{1}\right), T\left(\alpha_{2}\right), \cdots, T\left(\boldsymbol{\alpha}_{n}\right)\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right) \\
& =\left(\alpha_{1}, \alpha_{2}, \cdots, \alpha_{n}\right) A\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right),
\end{aligned}
$$

即

$$
T\left[\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right)\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right)\right]=\left(\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{A}\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right) .
$$

这个关系式惟一地确定一个变换 $T$, 可以验证所确定的变换 $T$ 是以 $\boldsymbol{A}$ 为矩 阵的线性变换. 总之, 以 $\boldsymbol{A}$ 为矩阵的线性变换 $T$ 由关系式(6)惟一确定. 定义 6 和上面一段讨论表明,在 $V_{n}$ 中取定一个基以后,由线性变换 $T$ 可 惟一地确定一个矩阵 $\boldsymbol{A}$, 由一个矩阵 $\boldsymbol{A}$ 也可惟一地确定一个线性变换 $\bar{T}$, 这样, 在线性变换与矩阵之间就有一一对应的关系.

由关系式(6), 可见 $\boldsymbol{\alpha}$ 与 $T(\boldsymbol{\alpha})$ 在基 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 下的坐标分别为

$$
\boldsymbol{\alpha}=\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right), T(\boldsymbol{\alpha})=\boldsymbol{A}\left(\begin{array}{c}
x_{1} \\
x_{2} \\
\vdots \\
x_{n}
\end{array}\right),
$$

即按坐标表示,有

$$
T(\boldsymbol{\alpha})=\boldsymbol{A \alpha} .
$$

例 11 在 $P[x]_{3}$ 中,取基

$$
p_{1}=x^{3}, p_{2}=x^{2}, p_{3}=x, p_{4}=1,
$$

求微分运算 $\mathrm{D}$ 的矩阵.

解

$$
\left\{\begin{array}{l}
\mathrm{D} p_{1}=3 x^{2}=0 p_{1}+3 p_{2}+0 p_{3}+0 p_{4}, \\
\mathrm{D} p_{2}=2 x=0 p_{1}+0 p_{2}+2 p_{3}+0 p_{4}, \\
\mathrm{D} p_{3}=1=0 p_{1}+0 p_{2}+0 p_{3}+1 p_{4}, \\
\mathrm{D} p_{4}=0=0 p_{1}+0 p_{2}+0 p_{3}+0 p_{4},
\end{array}\right.
$$

所以 $\mathrm{D}$ 在这组基下的矩阵为

$$
A=\left(\begin{array}{llll}
0 & 0 & 0 & 0 \\
3 & 0 & 0 & 0 \\
0 & 2 & 0 & 0 \\
0 & 0 & 1 & 0
\end{array}\right) .
$$

例 12 在 $\mathbb{R}^{3}$ 中, $T$ 表示将向量投影到 $x O y$ 平面的线性变换,即

$$
T(x i+y j+z k)=x i+y j,
$$

（1）取基为 $i, j, k$, 求 $T$ 的矩阵;

（2）取基为 $\alpha=i, \beta=j, \gamma=i+j+k$, 求 $T$ 的矩阵.

解 (1)

$$
\left\{\begin{array}{l}
T i=i \\
T j=j \\
T k=0
\end{array}\right.
$$

即

$$
T(\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k})=(\boldsymbol{i}, \boldsymbol{j}, \boldsymbol{k})\left(\begin{array}{lll}
1 & 0 & 0 \\
0 & 1 & 0 \\
0 & 0 & 0
\end{array}\right) \text {. }
$$

$$
\left\{\begin{array}{l}
T \boldsymbol{\alpha}=i=\alpha, \\
T \boldsymbol{\beta}=j=\boldsymbol{\beta}, \\
T \gamma=i+j=\alpha+\beta,
\end{array}\right.
$$

即

$$
T(\boldsymbol{\alpha}, \boldsymbol{\beta}, \boldsymbol{\gamma})=(\boldsymbol{\alpha}, \boldsymbol{\beta}, \boldsymbol{\gamma})\left(\begin{array}{lll}
1 & 0 & 1 \\
0 & 1 & 1 \\
0 & 0 & 0
\end{array}\right) .
$$

由上例可见,同一个线性变换在不同的基下有不同的矩阵.一般的,我们有 定理 2 设线性空间 $V_{n}$ 中取定两个基

$$
\begin{aligned}
& \boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n} ; \\
& \boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n},
\end{aligned}
$$

由基 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}, \cdots, \boldsymbol{\alpha}_{n}$ 到基 $\boldsymbol{\beta}_{1}, \boldsymbol{\beta}_{2}, \cdots, \boldsymbol{\beta}_{n}$ 的过渡矩阵为 $\boldsymbol{P}, V_{n}$ 中的线性变换 $T$ 在 这两个基下的矩阵依次为 $\boldsymbol{A}$ 和 $\boldsymbol{B}$, 那么 $\boldsymbol{B}=\boldsymbol{P}^{-1} \boldsymbol{A P}$.

证 按定理的假设,有

$$
\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right)=\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{P}, \boldsymbol{P} \text { 可逆; }
$$

及

$$
\begin{aligned}
& T\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right)=\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{A}, \\
& T\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right)=\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right) B,
\end{aligned}
$$

于是 $\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right) \boldsymbol{B}=T\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right)=T\left[\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{P}\right]$

$$
\begin{aligned}
& =\left[T\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right)\right] \boldsymbol{P}=\left(\boldsymbol{\alpha}_{1}, \cdots, \boldsymbol{\alpha}_{n}\right) \boldsymbol{A P} \\
& =\left(\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}\right) \boldsymbol{P}^{-1} \boldsymbol{A P},
\end{aligned}
$$

因为 $\boldsymbol{\beta}_{1}, \cdots, \boldsymbol{\beta}_{n}$ 线性无关, 所以

$$
B=P^{-1} A P .
$$

证毕

这定理表明 $\boldsymbol{B}$ 与 $\boldsymbol{A}$ 相似,且两个基之间的过渡矩阵 $\boldsymbol{P}$ 就是相似变换矩阵.

例 13 设 $V_{2}$ 中的线性变换 $T$ 在基 $\boldsymbol{\alpha}_{1}, \boldsymbol{\alpha}_{2}$ 下的矩阵为

$$
\boldsymbol{A}=\left(\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right),
$$

求 $T$ 在基 $\boldsymbol{\alpha}_{2}, \boldsymbol{\alpha}_{1}$ 下的矩阵.

解

$$
\left(\alpha_{2}, \alpha_{1}\right)=\left(\alpha_{1}, \alpha_{2}\right)\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)
$$

即

$$
P=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right) \text {, 求得 } P^{-1}=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right) \text {, }
$$

于是 $T$ 在基 $\left(\boldsymbol{\alpha}_{2}, \boldsymbol{\alpha}_{1}\right)$ 下的矩阵为

$$
\begin{aligned}
\boldsymbol{B} & =\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)\left(\begin{array}{ll}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{array}\right) \cdot\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right)=\left(\begin{array}{ll}
a_{21} & a_{22} \\
a_{11} & a_{12}
\end{array}\right)\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right) \\
& =\left(\begin{array}{ll}
a_{22} & a_{21} \\
a_{12} & a_{11}
\end{array}\right) .
\end{aligned}
$$

定义 7 线性变换 $T$ 的像空间 $T\left(V_{n}\right)$ 的维数,称为线性变换 $T$ 的秩. 显然,若 $\boldsymbol{A}$ 是 $T$ 的矩阵,则 $T$ 的秩就是 $R(\boldsymbol{A})$.

若 $T$ 的秩为 $r$, 则 $T$ 的核 $S_{T}$ 的维数为 $n-r$.

## 习 题 六

1. 验证:

(1) 2 阶矩阵的全体 $S_{1}$;

(2) 主对角线上的元素之和等于 0 的 2 阶矩阵的全体 $S_{2}$;

(3) 2 阶对称矩阵的全体 $S_{3}$,

对于矩阵的加法和乘数运算构成线性空间,并写出各个空间的一个基.

2. 验证: 与向里 $(0,0,1)^{\mathrm{T}}$ 不平行的全体 3 维数组向坦, 对于数组向然的加法和乘数运算 不构成线性空间.
3. 在 $\mathbb{R}^{3}$ 中求向舟 $\alpha=(7,3,1)^{\mathrm{T}}$ 在基

$$
\alpha_{1}=(1,3,5)^{\mathrm{T}}, \alpha_{2}=(6,3,2)^{\mathrm{T}}, \alpha_{3}=(3,1,0)^{\mathrm{T}}
$$

下的坐标.

4. 在 $\mathbb{R}^{3}$ 中, 取两个基

$$
\begin{aligned}
& \boldsymbol{\alpha}_{1}=(1,2,1)^{\mathrm{T}}, \boldsymbol{\alpha}_{2}=(2,3,3)^{\mathrm{T}}, \boldsymbol{\alpha}_{3}=(3,7,-2)^{\mathrm{T}} ; \\
& \boldsymbol{\beta}_{1}=(3,1,4)^{\mathrm{T}}, \boldsymbol{\beta}_{2}=(5,2,1)^{\mathrm{T}}, \boldsymbol{\beta}_{3}=(1,1,-6)^{\mathrm{T}},
\end{aligned}
$$

试求坐标变换公式.

5. 在 $\mathbb{R}^{4}$ 中取两个基

$$
\left\{\begin{array} { l } 
{ e _ { 1 } = ( 1 , 0 , 0 , 0 ) ^ { \mathrm { T } } , } \\
{ e _ { 2 } = ( 0 , 1 , 0 , 0 ) ^ { \mathrm { T } } , } \\
{ e _ { 3 } = ( 0 , 0 , 1 , 0 ) ^ { \mathrm { T } } , } \\
{ e _ { 4 } = ( 0 , 0 , 0 , 1 ) ^ { \mathrm { T } } , }
\end{array} \quad \left\{\begin{array}{l}
\boldsymbol{\alpha}_{1}=(2,1,-1,1)^{\mathrm{T}}, \\
\boldsymbol{\alpha}_{2}=(0,3,1,0)^{\mathrm{T}}, \\
\boldsymbol{\alpha}_{3}=(5,3,2,1)^{\mathrm{T}}, \\
\boldsymbol{\alpha}_{4}=(6,6,1,3)^{\mathrm{T}} .
\end{array}\right.\right.
$$

（1）求由前一个基到后一个基的过渡矩阵;

(2) 求向等 $\left(x_{1}, x_{2}, x_{3}, x_{4}\right)^{\mathrm{T}}$ 在后一个基下的坐标;

（3）求在两个基下有相同坐标的向贯.

6. 说明 $x O y$ 平面上变换 $T\left(\begin{array}{l}x \\ y\end{array}\right)=A\left(\begin{array}{l}x \\ y\end{array}\right)$ 的几何意义, 其中

(1) $A=\left(\begin{array}{rr}-1 & 0 \\ 0 & 1\end{array}\right)$;

(2) $A=\left(\begin{array}{ll}0 & 0 \\ 0 & 1\end{array}\right)$;

(3) $A=\left(\begin{array}{ll}0 & 1 \\ 1 & 0\end{array}\right)$;

(4) $A=\left(\begin{array}{rr}0 & 1 \\ -1 & 0\end{array}\right)$

7. $n$ 阶对称矩阵的全体 $V$ 对于矩阵的线性运算构成一个 $\frac{n(n+1)}{2}$ 维线性空间. 给出 $n$ 阶可逆矩阵 $\boldsymbol{P}$, 以 $\boldsymbol{A}$ 表示 $V$ 中的任一元家, 试证合同变换

$$
T(\boldsymbol{A})=\boldsymbol{P}^{\top} \boldsymbol{A P}
$$

是 $V$ 中的线性变换.

8. 函数集合

$$
V_{3}=\left\{\boldsymbol{\alpha}=\left(a_{2} x^{2}+a_{1} x+a_{0}\right) \mathrm{e}^{x} \mid a_{2}, a_{1}, a_{0} \in \mathbb{R}\right\}
$$

对于函数的线性运算构成 3 维线性空间. 在 $V_{3}$ 中取一个基

$$
\alpha_{1}=x^{2} \mathrm{e}^{x}, \alpha_{2}=x \mathrm{e}^{x}, \alpha_{3}=\mathrm{e}^{x},
$$

求微分运算 D 在这个基下的矩阵.

9. 2 阶对称矩阵的全体

$$
V_{3}=\left\{\boldsymbol{A}=\left(\begin{array}{ll}
x_{1} & x_{2} \\
x_{2} & x_{3}
\end{array}\right) \mid x_{1}, x_{2}, x_{3} \in \mathbb{R}\right\}
$$

对于矩阵的线性运算构成 3 维线性空间, 在 $V_{3}$ 中取一个基

$$
A_{1}=\left(\begin{array}{ll}
1 & 0 \\
0 & 0
\end{array}\right), A_{2}=\left(\begin{array}{ll}
0 & 1 \\
1 & 0
\end{array}\right), A_{3}=\left(\begin{array}{ll}
0 & 0 \\
0 & 1
\end{array}\right),
$$

在 $V_{3}$ 中定义合同变换

$$
T(\boldsymbol{A})=\left(\begin{array}{ll}
1 & 0 \\
1 & 1
\end{array}\right) A\left(\begin{array}{ll}
1 & 1 \\
0 & 1
\end{array}\right)
$$

求 $T$ 在基 $A_{1}, A_{2}, A_{3}$ 下的矩阵.

