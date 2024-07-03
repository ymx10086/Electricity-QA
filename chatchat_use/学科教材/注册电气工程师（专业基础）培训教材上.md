
\section{1 电路的基本概念和基本定律}

\subsection{1 理想电路元件}

\section{1. 线性电阻}

定义: 线性电阻是一个理想电路元件, 在元件上电压 $u$ 与电流 $i$ 方向为关联关系时 (见图 1. 1-1), 将 $u$ 与 $i$ 的比值称为电阻, 即 $R=u / i$ 。单位为 $\Omega$ (欧姆)。电阻的倒数为电导 $G$, 单位 为 $\mathrm{S}$ (西门子)。

性质: (1)伏安关系符合欧姆定律 $u=R i($ 或 $U=R I)$ 。特性曲线见图 1.1-2。

(2)是无源性耗能元件。消耗的功率

$$
P=U I=I^{2} R=\frac{U^{2}}{R}
$$









单位为 W(瓦)。在 $t$ 时间内消耗的电能为

$$
W=U I t=I^{2} R t=\frac{U^{2}}{R} t
$$

单位为 $\mathrm{J}$ (焦耳)。

(3)无记忆性。

(4)双向性。

【例 1.1-1】某电阻上的电压 $U=10 \mathrm{~V} 、 I=5 \mathrm{~A}$ 。求该电阻值、电导值、消耗的电功率和在 1 分钟内消耗的电能。

$$
\begin{aligned}
\text { 解: } R=\frac{U}{I}=\frac{10}{5}=2 \Omega, & G=\frac{I}{U}=\frac{5}{10}=0.5 \mathrm{~S} \\
P=U I=10 \times 5=50 \mathrm{~W}, & W=U I t=10 \times 5 \times 60=3000 \mathrm{~J}
\end{aligned}
$$

\section{2. 独立电压源}

定义:是一个理想电路元件, 元件两端的电压与通过它的电流无关。

性质:(1)伏安约束关系为

$$
\left\{\begin{array}{l}
u=u_{\mathrm{S}} \\
i=\text { 任意值 }
\end{array}\right.
$$


(2)端电压为常数的电压源是直流电压源, 用 $U_{S}$ 表示; 随时间周期变化的电压源为交流电压源,用 $u_{\mathrm{S}}$ 表示。

(3)是电路中的激励源, 其电流 $I_{U \mathrm{~S}}$ 决定于与它相连接的外电路。

(4)电压源的功率计算式为 $P=U_{\mathrm{S}} I_{t \mathrm{~S}}$, 当 $U_{\mathrm{S}}$ 与 $I_{U \mathrm{~S}}$ 符合非关联方向 时, 两者乘积为正值, 电压源供出功率, 为负值时电压源吸收功率。


解: 依非关联方向设定电压源中的电流 $I_{u \mathrm{~S}}$, 得

$$
I_{U \mathrm{~S}}=\frac{U_{\mathrm{S}}}{2+\frac{4}{2}}=\frac{10}{4}=2.5 \mathrm{~A}
$$

最后得独立电压源供出的功率为

$$
P_{u s}=U_{\mathrm{s}} I_{u s}=10 \times 2.5=25 \mathrm{~W}
$$


\section{3. 独立电流源}

定义:是一个理想电路元件, 元件中的电流与它两端的电压无关。 性质: (1)伏安约束关系为

$$
\left\{\begin{array}{l}
i=i_{\mathrm{S}} \\
u=\text { 任意值 }
\end{array}\right.
$$


(2) 电流为常数的电流源是直流电流源, 用 $I_{\mathrm{s}}$ 表示; 随时间周期变化的电流源为交流电流 源,用 $i_{\mathrm{S}}$ 表示。

(3) 是电路中的激励源, 其端电压 $U_{I S}$ 决定于与它相连接的外电路。

(4)电流源的功率计算式为 $P_{I 5}=I_{\mathrm{S}} U_{I 5}$ 。当 $I_{\mathrm{S}}$ 与 $U_{I 5}$ 符合非关联方向时, 两者乘积为正值, 电 流源供出功率, 为负值时电流源吸收功率。



\section{4. 受控电压源}

定义:受电路中某处电压或电流控制的电压源称为受控电压源。其中, 受电压控制的电压 源称为电压控制的电压源 (VCVS); 受电流控制的电压源称为电流控制的电压源 (CCVS)。受控电压源两端的电压与通过它的电流无关。


性质: (1)VCVS 的端口约束关系为

$$
\left\{\begin{array}{l}
u_{2}=u_{\mathrm{CS}}=\mu u_{1} \\
i_{2}=\text { 任意值 }
\end{array}\right.
$$

CCVS 的端口约束关系为

$$
\left\{\begin{array}{l}
u_{2}=u_{\mathrm{CS}}=r i_{1} \\
i_{2}=\text { 任意值 }
\end{array}\right.
$$

受控电压源中的电流决定于与其相连接的外电路。两约束关系式中的 $\mu$ 和 $r$ 称为控制系数。 在 VCVS 中, $\mu=u_{2} / u_{1}$ 称为电压比, 为无量纲的常数。在 CCVS 中, $r=u_{2} / i_{1}$ 称为转移电阻, 单位 为 $\Omega$ 。

(2)不是电路中的激励源, 在电路中起参数耦合作用。

(3)受控电压源可以吸收功率, 也可以供出功率。功率的计算方法与独立电压源相同。

(4)当控制变量 $u_{1}$ 或 $i_{1}$ 消失时, 受控电压源随之消失, 即在去掉受控电压源后原处短路。当 控制变量存在时,受控电压源不允许短路。

\section{5. 受控电流源}

定义: 受控电路中某处电压或电流控制的电流源称为受控电流源。其中, 受电压控制的电 流源称为电压控制的电流源 (VCCS); 受电流控制的电流源称为电流控制的电流 源( CCCS)。受控电流源中的电流与它两端的电压无关。


性质: (1)VCCS 的端口约束关系为

$$
\left\{\begin{array}{l}
i_{2}=i_{\mathrm{CS}}=g u_{1} \\
u_{2}=\text { 任意值 }
\end{array}\right.
$$

$\operatorname{CCCS}$ 的端口约束关系为

$$
\left\{\begin{array}{l}
i_{2}=i_{\mathrm{CS}}=\beta i_{1} \\
u_{2}=\text { 任意值 }
\end{array}\right.
$$

受控电流源两端的电压决定于与其相连接的外电路。两约束关系式中的 $g$ 和 $\beta$ 称为控制系 数。在 VCCS 中, $g=i_{2} / u_{1}$ 称为转移电导, 单位为 $\mathrm{S}$ 。在 CCCS 中, $\beta=i_{2} / i_{1}$ 称为电流比, 为无量纲的常数。

(2)不是电路中的激励源, 在电路中起参数耦合作用。

(3)受控电流源可以吸收功率, 也可以供出功率。功率的计算方法与独立电流源相同。

(4)当控制变量 $u_{1}$ 或 $i_{1}$ 消失时, 受控电流源随之消失, 即在去掉受控电流源后原处开路。当 控制变量存在时,受控电流源不允许开路。


\section{6. 线性电容}

定义: 是一个理想电路元件, 见图 1.1-15, 在图中给出的电荷 $q$ 和电压 $u_{C}$ 的方向下, 将 $q$ 与 $u_{c}$ 之比定义为电容 $C$, 即 $C=q / u_{C}$, 单位为 $\mathrm{F}$ (法 拉)。

性质: (1)线性电容的特性曲线为在 $q-u_{C}$ 坐标系下过原点的斜直线。

(2)当两端电压 $u_{c}$ 和电流 $i_{c}$ 的参考方向符合图 1.1-15 中的关联方向时, 两变量的约束关系 为


$$
i_{c}=C \frac{\mathrm{d} u_{c}}{\mathrm{~d} t}
$$

(3)记忆元件。在任何时刻 $t$, 电容两端的电压 $u_{c}(t)$ 与初始电压 $u_{c}(0)$ 和从 0 时刻到 $t$ 所有电流值有关, 即

$$
u_{C}(t)=\frac{1}{C} \int_{-\infty}^{t} i_{C} \mathrm{~d} \tau=u_{C}(0)+\frac{1}{C} \int_{0}^{i} i_{C} \mathrm{~d} \tau
$$

(4)储能元件。在任何时刻 $t$ 电容储存的电场能量为

$$
W_{C}(t)=\frac{1}{2} C u_{C}^{2}(t)
$$

(5)隔直作用。电容在直流电压 $U_{c}$ 作用下无电流, 相当于开路。

\section{7. 线性电感}

定义: 是一个理想电路元件, 当磁链 $\psi$ 和电流 $i_{L}$ 的方向 符合右手定则时, 将 $\psi$ 与 $i_{L}$ 之比定义为电感 $L$, 即 $L=\psi / i_{L}$ 。 单位为 $\mathrm{H}$ (亨利)。


性质：(1)线性电感的特性曲线为在 $\psi-i_{L}$ 坐标系下过原点的斜直线。

(2) 当两端电压 $u_{L}$ 和电流 $i_{L}$ 的参考方向符合图 1.1-17 中的关联方向时, 两变量的约束关系 为

$$
u_{L}=L \frac{\mathrm{d} i_{L}}{\mathrm{~d} t}
$$

(3)记忆元件。在任何时刻 $t$, 电感中的电流 $i_{L}(t)$ 与初始电流 $i_{L}(0)$ 和从 0 时刻到 $t$ 所有电压值有关, 即

$$
i_{L}=\frac{1}{L} \int_{-\infty}^{t} u_{L} \mathrm{~d} \tau=i_{L}(0)+\frac{1}{L} \int_{0}^{t} u_{L} \mathrm{~d} \tau
$$

(4)储能元件。在任何时刻 $t$ 电感储存的磁场能量为

$$
W_{L}(t)=\frac{1}{2} L i_{L}^{2}(t)
$$

\section{8. 耦合电感}

定义:一对具有磁耦合关系电感的整体称为耦合电感。

所谓磁耦合关系, 是指由一个电感线圈中电流 $i_{L 1}$ 所产生的自感磁通 $\Phi_{11}$ 的一部分或全部 穿过另一个线圈的现象。穿过另一个线圈的磁通 $\Phi_{12}$ 称为互感磁通。





性质: (1)耦合系数 $k$ : 用来表示两线圈磁耦合关系紧密程度的参数。 $k=\sqrt{L_{1} / L_{2}} \leqslant 1$, 当 $k$ $=1$ 时称为全耦合。

(2)互感系数 $M$ : 穿过第二个线圈的磁链 $\psi_{12}=N_{2} \Phi_{12}$ 与产生此磁链的电 流 $i_{L 1}$ 的比为互感系数 $M_{2}$, 即 $M_{2}=\psi_{12} / i_{L 1}$; 同样可有 $M_{1}=\psi_{21} / i_{L 2}$ 。 可以证明 $M_{1}=M_{2}=M_{\text {。 }}$

(3)互感的标记端: 由于分析互感现象时直接与线圈的绕向有关,所以用“*”或“.”表示 两线圈的绕向关系;两标记端或两非标记端之间称为同名端,两线圈标记端与非标记端之间称 为异名端; 标记的原则是, 若两线圈都由同名端流进电流, 则此两电流产生的磁通是相互增强 的。

(4)互感电压: 由交变的互感磁通所产生的电压称为互感电压, 在图 1.1-20 中的, 由 $\Phi_{12}$ 产 生的互感电压为

$$
u_{M 12}=\frac{\mathrm{d} \psi_{12}}{\mathrm{~d} t}=M \frac{\mathrm{d} i_{L 1}}{\mathrm{~d} t}
$$

互感电压方向的判断方法是同名端一致原则。所谓同名端一致原则是,一个线圈上的互 感电压的方向与在另一个线圈中产生此互感电压的电流保持同名端一致。也就是说, 若产生 互感电压的电流由标记端流向非标记端, 则在另一个线圈中产生的互感电压也必然由标记端 指向非标记端。或电流由非标记端流人, 互感电压也必然由非标记端指向标记端。

\section{9. 理想变压器}

定义: 是由实际变压器经过理想化后的二端口器件, 即满足无损耗、全耦合且 自感和互感均无限大的理想耦合电感为理想变压器。 



性质: (1)理想变压器两线圈的匝数比 $n=N_{1} / N_{2}$ 称为变比;

(2)耦合系数 $k=1$;

(3) $u_{1} / u_{2}=N_{1} / N_{2}=n$;

(4) $i_{1} / i_{2}=-1 / n$ 。

\section{1.2 电流、电压的参考方向}

\section{1. 参考方向}

电流的实际方向为正电荷移动的方向。电压的实际方向为电位降的方向。在分析和计算 电路之前往往不知它们的实际方向, 但电路的定律都是依据电流、电压的实际方向而确定的, 这就需要在分析计算电路之前先假设一个电流、电压的实际方向。这个假设的实际方向称为电流、电压的参考方向。在设定电流、 电压的参考方向后, 分析计算结果为正值时,参考方向即为实际方向, 为负 值时,实际方向与参考方向相反。因此, 参考方向也称为正方向。在电路 理论中所标注的电流、电压的方向均为参考方向。

\section{2. 关联方向}

因为正电荷在电场力的作用下, 总是从高电位移向低电位, 即电流的实际方向指向电位降 的方向, 也就是说和电压的方向是一致的。按照这样的规律同时设定电流和电压的参考方向 时,电流和电压的方向关系称为关联方向。反之为非关联方向。


\section{1 .3 基尔霍夫定律}

\section{1. 基尔霍夫电流定律 ( $\mathrm{KCL}$ )}

在集中参数电路中, 对任何一个节点, 在任何时刻流人 (流出) 该节点的电流的代数和恒 等于零。其表达式为 $\sum i=0$ 或 $\sum i_{\text {人 }}=\sum i_{\text {出 }}$



\section{2. 基尔霍夫电压定律 ( KVL)}

在集总参数电路中, 对任何一个闭合回路, 在任何时刻沿该 回路循行时,所有支路电压的代数和恒等于零。其表达式为 $\sum u$ $=0$ 或 $\Sigma R i=\sum u_{\mathrm{s} \text { 升。 }}$

【例 1.1-9】在图 1.1-26 电路中, 已知 $R_{1}=R_{2}=1 \Omega, U_{\mathrm{SI}}=2$





$$
\mathrm{V}, U_{\mathrm{s} 2}=4 \mathrm{~V}, U_{\mathrm{s3}}=10 \mathrm{~V} \text { 。求开路电压 } U_{\mathrm{ab}} \text { 。 }
$$

解: 因为 $\mathrm{ab}$ 两端开路, 所以可以设回路中的电流 $I$ (见图 1.126)，根据 KVL 有

$$
\left(R_{1}+R_{2}\right) I+U_{\mathrm{S} 2}-U_{\mathrm{S} 1}=0
$$

可得

$$
I=\frac{U_{\mathrm{S} 1}-U_{\mathrm{S} 2}}{R_{1}+R_{2}}=\frac{2-4}{1+1}=-1 \mathrm{~A}
$$

由 KVL 得

$$
U_{\mathrm{ab}}=-U_{\mathrm{S} 3}+R_{2} I+U_{\mathrm{S} 2}=-10+1 \times(-1)+4=-7 \mathrm{~V}
$$

\section{2 电路的分析方法}

\subsection{1 常用的电路等效变换方法}

\section{1. 非理想独立电源间的等效变换}

由非理想独立电压源等效变换成非理想独立电流源的变换 关系为 (见图 1.2-1)

$$
I_{\mathrm{S}}=\frac{U_{\mathrm{S}}}{R_{\text {in }}}, G_{\text {in }}=\frac{1}{R_{\text {in }}}
$$

由非理想独立电流源等效变换成非理想独立电压源的变换



$$
U_{\mathrm{S}}=\frac{I_{\mathrm{S}}}{G_{\mathrm{in}}}, R_{\mathrm{in}}=\frac{1}{G_{\mathrm{in}}}
$$

当非理想独立电流源的并联电导用电阻表示时,两组变换关系式中等效变换前后该电阻 值不变。

【例 1.2-1】 将图 1.2-2(a)中的两个非理想电压源并联电路化简为一个非理想电压源。

解: (1)将图 (a) 中的两个非理想电压源等效变换成两个非理想电流源,如图 (b);

(2) 将图 (b) 中的两电阻并联为一个电阻, 两理想电流源合并为一个电流源, 如图 (c);

(3)将图 (c) 中的非理想电流源等效变换成非理想电压源,如图(d)。

\section{2. 非理想受控电源间的等效变换}

在 4 种受控电源中只有 VCVS $\Leftrightarrow$ VCCS 和 CCVS $\Leftrightarrow$ CCCS 两对受控电源之间能够进行等效 变换。两对受控电源之间的等效变换关系见图 1.2-3。 




在图 1.2-3 中, 当非理想受控电流源的并联电导用电阻表示时, 4 组变换关系式中等效变 换前后该电阻值不变。

【例 1.2-2】利用等效变换求图 1.2-4(a) 中的电流 $I$ 。



解: (1)利用等效变换关系将图 (a) 中的非理想独立电流源和非理想受控电流源变换成非 理想独立电压源和非理想受控电压源, 得图 (b);

(2)在图 (b) 电路中, 因为受控电压源受本身电流控制且符合关联方向, 则该受控电压源为 一个电阻, 此电阻即为控制系数, 即 $R=4 I / I=4 \Omega$, 见图(c), 最后得

$$
I=\frac{8}{2+2+4}=1 \mathrm{~A}
$$



\section{3. 星接 ( $Y$ 接) 和角接 ( $\Delta$ 接) 电阻间的等效变换}

由 $\Delta$ 接等效变换成 $Y$ 接时 (见图 1.2-5), $Y$ 接的各电阻为一分数, 分母为 $\Delta$ 接三电阻之 和, 分子为与所求 $Y$ 接电阻的外接节点相联的两个 $\Delta$ 接电阻之积, 即

$$
\begin{aligned}
& R_{1}=\frac{R_{12} R_{31}}{R_{12}+R_{23}+R_{31}} \\
& R_{2}=\frac{R_{12} R_{23}}{R_{12}+R_{23}+R_{31}} \\
& R_{3}=\frac{R_{23} R_{31}}{R_{12}+R_{23}+R_{31}}
\end{aligned}
$$

由 $\mathrm{Y}$ 接等效变换成 $\Delta$ 接时 (见图 1.2-5), $\Delta$ 接的各电阻为所求 $\Delta$ 接电阻的 两个外接节点相联的两 $Y$ 接电阻之和再加上此两电阻的乘积与另一电阻之比, 即

$$
\begin{aligned}
& R_{12}=R_{1}+R_{2}+\frac{R_{1} R_{2}}{R_{3}} \\
& R_{23}=R_{2}+R_{3}+\frac{R_{2} R_{3}}{R_{1}} \\
& R_{31}=R_{3}+R_{1}+\frac{R_{3} R_{1}}{R_{2}}
\end{aligned}
$$

在对称情况下,有 $R_{\mathrm{Y}}=R_{\Delta} / 3$ 或 $R_{\Delta}=3 R_{\mathrm{Y}}$ 。



\subsection{2 节点方程的列写方法及其求解电路}

\section{1. 节点方程的一般列写方法}

有效自导 $\times$ 本节点电压 - 有效互导 $\times$ 相邻节点电压 $=$ 流人本节点电源电流的代数和 有效自导指本节点与所有相邻节点支路中除电流源支路电导的所有电导之和。有效互导 指本节点与相邻节点之间的电导 (电流源支路电导为 0 )。

在含有电压源支路中, 流人本节点的电流为支路中的电压源与其所在支路中的等效电阻 之比。电压源正极性靠近本节点时取正, 负极性靠近本节点时取负。



【例 1.2-5】在图 1.2-8 电路中, $U_{\mathrm{S} 1 、} U_{\mathrm{S} 2} 、 I_{\mathrm{S}}$ 和 $R_{1} \sim R_{6}$ 均为 已知, 列写此电路的节点电压方程。

解: $\left\{\begin{array}{l}\left(\frac{1}{R_{1}}+\frac{1}{R_{3}}+\frac{1}{R_{5}}\right) U_{\mathrm{a}}-\frac{1}{R_{3}} U_{\mathrm{b}}-\frac{1}{R_{1}} U_{\mathrm{c}}=\frac{U_{\mathrm{S} 1}}{R_{1}} \\ \left(\frac{1}{R_{2}}+\frac{1}{R_{3}}+\frac{1}{R_{4}}\right) U_{\mathrm{b}}-\frac{1}{R_{3}} U_{\mathrm{a}}-\frac{1}{R_{4}} U_{\mathrm{c}}=\frac{U_{\mathrm{S} 2}}{R_{2}} \\ \left(\frac{1}{R_{1}}+\frac{1}{R_{4}}\right) U_{\mathrm{c}}-\frac{1}{R_{1}} U_{\mathrm{a}}-\frac{1}{R_{4}} U_{\mathrm{b}}=I_{S}-\frac{U_{\mathrm{S} 1}}{R_{1}}\end{array}\right.$

在此方程中没有出现 $1 / R_{6}$, 因为它在电流源支路是无效电 导。

\section{2. 含无伴电压源支路节点方程的列写方法}

所谓含无伴电压源支路, 是指在电路中某支路内只含独立电压源或只含受控电压源。对 这种电路在列写节点方程时, 优先选取独立电压源或受控电压源的负极性端为参考点。这样 可以减少方程的个数 (见下面的例 1.2-6)。如果电路中含有两个或两个以上无伴电压源支 路, 除优先选取独立电压源或受控电压源的负极性端为参考点外, 还应该相应地增加不与参考 点相连电压源中的电流为未知变量,并相应地增加补充方程。

【例 1.2-6】在图 1.2-9 电路中, 已知 $U_{\mathrm{S} 1}=3 \mathrm{~V}, U_{\mathrm{S} 2}=6 \mathrm{~V}, I_{\mathrm{S}}=1 \mathrm{~A}$, 各电阻 $R=3 \Omega$ 。求各 独立电源供出的功率。

解: 因为此电路只含一个无伴电压源 $U_{\mathrm{S} 1}$ 支路, 所以选取该电压源的负极性端为参考点。 这样, $U_{\mathrm{a}}=U_{\mathrm{st}}=3 \mathrm{~V}$ 为已知量, 无须对节点 a 列写方程。此电路的节点电压方程组为 

$$
\left\{\begin{array}{l}
\left(\frac{1}{R}+\frac{1}{R}+\frac{1}{R}\right) U_{\mathrm{b}}-\frac{1}{R}-U_{\mathrm{a}}-\frac{1}{R} U_{\mathrm{c}}=\frac{U_{\mathrm{S} 2}}{R} \\
\left(\frac{1}{R}+\frac{1}{R}\right) U_{\mathrm{c}}-\frac{1}{R} U_{\mathrm{b}}=I_{\mathrm{S}}
\end{array}\right.
$$

代人已知数据整理后的方程组为

$$
\left\{\begin{array}{l}
U_{\mathrm{b}}-\frac{1}{3} U_{\mathrm{c}}=3 \\
\frac{2}{3} U_{\mathrm{c}}-\frac{1}{3} U_{\mathrm{b}}=1
\end{array}\right.
$$



解得 $U_{\mathrm{b}}=4.2 \mathrm{~V}, U_{\mathrm{c}}=3.6 \mathrm{~V}$

为求各独立电源供出的功率, 设定两独立电压源中的电流和独立电流源两端的电压分别 为 $I_{U \mathrm{~S} 1} 、 I_{U \mathrm{~S} 2}$ 和 $U_{I \mathrm{~S}}$ (见图 1.2-9), 可得

$$
\begin{aligned}
& I_{U S 1}=\frac{U_{\mathrm{b}}}{R}+\frac{U_{\mathrm{c}}}{R}=\frac{4.2}{3}+\frac{3.6}{3}=2.6 \mathrm{~A} \\
& I_{U S 2}=\frac{U_{\mathrm{a}}-U_{\mathrm{b}}+U_{\mathrm{S} 2}}{R}=\frac{3-4.2+6}{3}=1.6 \mathrm{~A} \\
& U_{\mathrm{S}}=R I_{\mathrm{S}}+U_{\mathrm{c}}-U_{\mathrm{a}}=3 \times 1+3.6-3=3.6 \mathrm{~V}
\end{aligned}
$$

最后得各独立电源供出的功率分别为

$$
\begin{aligned}
& P_{U \mathrm{~S} 1}=U_{\mathrm{S} 1} I_{U \mathrm{~S} 1}=3 \times 2.6=7.8 \mathrm{~W} \\
& P_{U \mathrm{~S} 2}=U_{\mathrm{S} 2} I_{U \mathrm{~S} 2}=6 \times 1.6=9.6 \mathrm{~W} \\
& P_{\mathrm{IS}}=I_{\mathrm{S}} U_{I \mathrm{~S}}=1 \times 3.6=3.6 \mathrm{~W}
\end{aligned}
$$

\section{3. 含受控电源电路节点方程的列写方法}

在电路中含有受控电源时,列写节点方程应遵循以下两原则:

(1)将受控电源按独立电源对待;

(2)找出控制变量与末知变量的关系作为补充方程。

【例1.2-7】在图 1.2-10 电路中, 两独立电源 $U_{\mathrm{S}}$ 和 $I_{\mathrm{S}}$, 两受控电源的控制系数 $\mu$ 和 $\beta$ 以 及各电阻 $R_{1} \sim R_{4}$ 均为已知, 列写求解此电路的节点电压方程。

解: 解此电路同样可以优先选取受控电压源 $\mu U$ 的负极性端为参考点, 方程组为



$$
\left\{\begin{array}{l}
\frac{1}{R_{1}} U_{\mathrm{a}}-\frac{1}{R_{1}} U_{\mathrm{c}}=I_{\mathrm{S}}-\beta I \\
\left(\frac{1}{R_{2}}+\frac{1}{R_{3}}\right) U_{\mathrm{b}}-\frac{1}{R_{2}} U_{\mathrm{c}}=-\frac{U_{\mathrm{S}}}{R_{3}}-I_{\mathrm{S}} \\
U_{\mathrm{c}}=\mu U \\
U=U_{\mathrm{a}}-U_{\mathrm{c}} \\
I=\frac{U_{\mathrm{b}}-U_{\mathrm{c}}}{R_{2}}
\end{array}\right.
$$

在此方程组中, 前三个为节点方程, 后两个为补充方程。 

\section{4. 用节点电压法求解电路}

用节点电压法求解电路时可依照下述步骤计算:

(1)选好参考点,并将各独立节点命名;

(2)根据电路的不同结构,按方程的规律性列写节点方程和所需的补充方程;

(3) 解出所需的节点电压;

(4)设定所需求解其他变量的参考方向后,求得所需变量。 为熟悉以上步骤可参看前面的例 $1.2-6$ 。

\subsection{3回路方程的列写方法}

\section{1. 回路方程的一般列写方法}

自阻 $\times$ 本回路电流 $+\Sigma$ 共阻 $\times$ 相邻回路电流 $=$ 本回路电源电位升的代数和

应用上式时, 应以本独立回路电流的方向为循行方向。式中的“ $\Sigma$ 共阻 $\times$ 相邻回路电流” 是以在循行过程中, 相邻独立回路电流方向与循行方向一致时取正, 反之取负。等式右侧的 “本回路电源电位升的代数和” 为沿本回路独立电流方向循行时, 遇电位升取正, 反之取负。 当遇有电流源时, 必须设定其两端电压为未知变量, 并相应地增加补充方程。

\section{2. 网孔方程的列写方法}

当选择自然网孔为独立回路时, 并将各网孔电流的方向设成一致, 当沿网孔电流方向循行 时, 可直接按下列规律列写网孔电流方程。

\section{自阻 $\times$ 本网孔电流 - 共阻 $\times$ 相邻网孔电流 $=$ 本网孔电源电位升的代数和}

\section{3. 含电流源电路的回路方程}

对含有独立电流源和受控电流源的电路, 可优先选取包含电流源支路在内的回路为独立 回路, 其他的独立回路不再包含此支路。此独立回路电流即为已知, 不再对此回路列写回路电 流方程。

\section{4. 含受控电源电路的回路方程}

对含有受控电源的电路, 列写回路电流方程所遵循的原则, 仍然是将受控电源按独立电源 对待,并找出控制变量与未知变量的关系作为补充方程。

【例 1.2-8】 在图 1.2-11 电路中, 两独立电源 $U_{\mathrm{S}} 、 I_{\mathrm{S}}$, 受控电源的控制系数 $r$ 以及电阻 $R_{1}$ $\sim R_{4}$ 均为已知, 列写求解此电路的回路电流方程。

解: 选自然网孔为独立回路, 并将网孔电流皆按顺时针方向设定, 其中 $I_{\mathrm{a}}=I_{\mathrm{S}}$ 不必再对此 网孔列写方程, 只需列写两个网孔电流方程和一个补充方程。求解此电路的回路电流方程为



$$
\left\{\begin{array}{l}
\left(R_{2}+R_{3}\right) I_{\mathrm{b}}-R_{3} I_{\mathrm{S}}-R_{2} I_{\mathrm{c}}=r I-U_{\mathrm{S}} \\
\left(R_{1}+R_{2}+R_{4}\right) I_{\mathrm{c}}-R_{1} I_{\mathrm{S}}-R_{2} I_{\mathrm{b}}=0 \\
I=-I_{\mathrm{c}}
\end{array}\right.
$$

\subsection{4 叠加定理、戴维南定理和诺顿定理}

\section{1. 叠加定理}

定理内容:在多个激励源的线性电路中, 任何一处的电压、 电流响应为各激励源单独作用下, 在该处的电压、电流响应的代 数和。 在应用叠加定理时, 为实现某激励源单独作用, 需将其他不起作用的激励源置零, 即将其 中的独立电压源去掉后在原处短路; 将独立电流源去掉后在原处开路。


注意事项:

(1)叠加定理只适用于线性电路;

(2)受控电源不是激励源, 不能构成单独作用的分电路;

(3)各分电路中应包含原电路中的全部受控电源和控制变量;

(4)取代数和时, 应遵循以原电路中的电压、电流响应的参考方向为准的原则, 即分电路中 的电压、电流响应的参考方向与原电路一致者取正, 反之取负;

(5)叠加原理只适用于电压、电流响应,一般情况下不适用于功率响应。 

\section{2. 线性关系}

线性关系是齐次性原理和叠加定理综合表现形式, 即在线性电路中既满足齐次性原理又 满足叠加定理,两定理合称为线性关系。

线性关系特别适用于求解黑箱电路。线性关系有如下两种表达形式。

(1)对一个不含独立电源的图 1.2-13 黑箱电路 $N_{0}$, 某处电压响应 $u_{x}$ 、电流响应 $i_{x}$ 的线性关 系式为

$$
\begin{aligned}
\left.\begin{array}{c}
u_{x} \\
i_{x}
\end{array}\right\} & =K_{u 1} u_{\mathrm{S} 1}+K_{i 1} i_{\mathrm{S} 1}+K_{u 2} u_{\mathrm{S} 2}+K_{i 2} i_{\mathrm{S} 2}+\cdots+K_{u n} u_{\mathrm{Sn}}+K_{i n} i_{\mathrm{S} n} \\
& =\sum_{j=1}^{n}\left(K_{u j} u_{\mathrm{S} j}+K_{i j} i_{\mathrm{S} j}\right)
\end{aligned}
$$

式中, $K_{u 1}, K_{i 1}, K_{u 2}, K_{i 2}, \cdots, K_{u n}, K_{i n}$ 称为线性系数。





(2)对一个含有独立电源的图 1.2-14 黑箱电路 $N_{\mathrm{S}}$, 某处电压响应 $u_{x}$ 、电流响应 $i_{x}$ 的线性关 系式为

$$
\begin{aligned}
& \left.\begin{array}{l}
u_{x} \\
i_{x}
\end{array}\right\}=K_{u 1} u_{\mathrm{S} 1}+K_{i 1} i_{\mathrm{S} 1}+K_{u 2} u_{\mathrm{S} 2}+K_{i 2} i_{\mathrm{S} 2}+\cdots+K_{u n} u_{\mathrm{S} n}+K_{i n} i_{\mathrm{S} n}+C \\
& =\sum_{j=1}^{n}\left(K_{u j} u_{\mathrm{sj}}+K_{i j} i_{\mathrm{sj}}\right)+C
\end{aligned}
$$

式中: $\sum_{j=1}^{n}\left(K_{u j} u_{\mathrm{s} j}+K_{i j} i_{\mathrm{S} j}\right)$ 为黑箱电路中全部电源置零时, 电路中某处的电压、电流响应; 常数 $C$ 为黑箱电路外部所有独立电源置零后, 其内部全部独立电源共同作用下, 电路中某处的电压、 电流响应。

【例 1.2-10】在图 1.2-15 电路中, 黑箱电路 $N_{0}$ 为无独立电源的线性电路。当三个独立 电源共同作用时 $U=8 \mathrm{~V}$; 当 $4 \mathrm{~V}$ 电压源置零后 $U=4 \mathrm{~V}$; 当两个电压源同时置零后 $U=2 \mathrm{~V}$ 。求 当两个电压源同时反接后,三个电源共同作用下 $1 \Omega$ 电阻中消耗的功率。

解: 设 $1 \Omega$ 电阻的两端电压为 $U$, 根据线性关系有

$$
U=K_{1} U_{\mathrm{S1}}+K_{2} U_{\mathrm{S} 2}+K_{3} I_{\mathrm{S}}
$$

将已知数据代人此关系式有 

$$
\left\{\begin{array}{l}
4 K_{1}+2 K_{2}+2 K_{3}=8 \\
2 K_{2}+2 K_{3}=4 \\
2 K_{3}=2
\end{array}\right.
$$

解得线性系数

$$
K_{1}=K_{2}=K_{3}=1
$$

由此可得当两个电压源同时反接后, 三个电源共同作用下 1 $\Omega$ 电阻上的电压为

$$
U=-K_{1} U_{\mathrm{S} 1}-K_{2} U_{\mathrm{S} 2}+K_{3} I_{\mathrm{s}}=-4-2+2=-4 \mathrm{~V}
$$

最后得 $1 \Omega$ 电阻中消耗的功率为



$$
P=\frac{U^{2}}{R}=\frac{(-4)^{2}}{1}=16 \mathrm{~W}
$$

[例 1.2-11]在图 1.2-16 电路中, 黑箱电路 $N_{\mathrm{s}}$ 为含独立电源的线性电路。已知: 当 $U_{\mathrm{s}}=$ $4 \mathrm{~V}, I_{\mathrm{S}}=1 \mathrm{~A}$ 时, $I=4 \mathrm{~A}$; 当 $U_{\mathrm{s}}$ 置零后有 $I_{\mathrm{S}}$ 作用时, $I=2 \mathrm{~A}$; 当 $I_{\mathrm{S}}$ 置零后有 $U_{\mathrm{s}}$ 作用时, $I=1 \mathrm{~A}$ 。求 当 $N_{\mathrm{s}}$ 外部的两个独立电源同时增加一倍后共同作用下, 电压源 $U_{\mathrm{s}}$ 供出的功率。



解: 根据线性关系有

$$
I=K_{1} U_{\mathrm{S}}+K_{2} I_{\mathrm{S}}+C
$$

代人三个已知条件, 可有如下方程组:

$$
\left\{\begin{array}{l}
4 K_{1}+K_{2}+C=4 \\
K_{2}+C=2 \\
4 K_{1}+C=1
\end{array}\right.
$$

解得三个线性系数分别为

$$
K_{1}=0.5, K_{2}=3, C=-1
$$

将三个线性系数和所需求解的工作条件代人上述线性关系式得

$$
I=2 K_{1} U_{\mathrm{S}}+2 K_{2} I_{5}+C=2 \times 0.5 \times 4+2 \times 3 \times 1-1=9 \mathrm{~A}
$$

最后得电压源 $U_{\mathrm{s}}$ 供出的功率为

$$
P_{u \mathrm{~S}}=-2 U_{\mathrm{S}} I=-2 \times 4 \times 9=-72 \mathrm{~W}
$$

说明电压源 $U_{\mathrm{s}}$ 在所需求解的条件下吸收功率。

\section{3. 戴维南定理}

定理内容: 任何一个含有独立电源的线性一端口电阻电路, 对外电路而言可以用一个独立 电压源和一个线性电阻相串联的电路等效替代; 其独立电压源的电压为该含源一端口电路在 端口处的开路电压 $u_{\mathrm{oc}}$; 其串联电阻为该含源一端口电路中所有独立电源置零后, 端口处的人 端电阻 $R_{\text {in }}$ 。

人端电阻 $R_{\mathrm{in}}$ 的定义是: 对一个不含独立电压源的一端口电路, 在端口处的电压 $u_{\mathrm{in}}$ 和端口 处的电流 $i_{\text {in }}$ 在关联方向下的比值, 即

$$
R_{\text {in }}=\frac{u_{\text {in }}}{i_{\text {in }}}
$$

用戴维南定理等效后的电压源 $u_{\mathrm{oc}}$ 和电阻 $R_{\mathrm{in}}$ 串联电路称为原含源一端口电路的戴维南等 效电路。

戴维南定理可以用图 1.2-17 帮助理解和记忆。 



应用戴维南定理求解电路的解题步骤:

(1)选好开路端;

(2)求开路电压 $u_{0 C}$;

(3)求人端电阻 $R_{\text {in }}$ (可以有多种方法, 见例 1. 2-13。);

(4)画出原电路的等效电路;

(5)在等效电路中求所需响应。

使用戴维南定理的注意事项:

(1)将含独立电源的一端口电路用戴维南定 理等效是指对外电路等效;

(2)戴维南等效电路的独立电压源 $u_{\mathrm{OC}}$ 应与

所求得的开路电压方向保持一致;

(3)所求的开路电压 $u_{\mathrm{oc}}$ 和人端电阻 $R_{\mathrm{in}}$ 都有可能为负值。


【例 1.2-13】 在图 1.2-19(a) 电路中, 已知 $R_{1}=2 \Omega, R_{2}=5 \Omega, R_{\mathrm{L}}=2.5 \Omega, U_{\mathrm{S}}=10 \mathrm{~V}$, 控 制系数 $r=3 \Omega$ 。 求负载电阻 $R_{\mathrm{L}}$ 中的电流 $I_{R \mathrm{~L} \text { 。 }}$

解: 此题为求单一响应的电路,最适合用戴维南定理求解。现按戴维南定理的解题步骤求 解此电路。

(1)首先选取负载电阻 $R_{\mathrm{L}}$ 两端开路, 在 $R_{\mathrm{L}}$ 左侧形成一个含源一端口电路, 如图 $(\mathrm{b})$ 。

(2)求开路电压 $U_{\mathrm{oc}}$ 。根据 KVL 有

$$
U_{\mathrm{S}}+r I_{1}+\left(R_{1}+R_{2}\right) I_{1}=0
$$

则

得

$$
I_{1}=\frac{-U_{\mathrm{S}}}{R_{1}+R_{2}+r}=\frac{-10}{2+5+3}=-1 \mathrm{~A}
$$

$$
U_{\text {oc }}=-I_{1} R_{2}=-(-1) \times 5=5 \mathrm{~V}
$$

(3)求人端电阻 $R_{\mathrm{in}}$ 。将图 (b) 电路中的 独立电源去掉后在原处短路为图 (c)。下面 介绍 4 种求人端电阻 $R_{\text {in }}$ 的方法。

\section{方法 1 一比例法}

根据人端电阻的定义, 在图 (c) 电路的 端口处依关联方向设端口电压 $U_{\text {in }}$ 和端口电 流 $I_{\mathrm{in}}$, 并设电阻 $R_{2}$ 支路电流 $I_{2}$, 见图 $(\mathrm{d})$ 。 则有

$$
R_{1} I_{1}+r I_{1}=U_{\text {in }}
$$


方法 2一等效法

此方法的原理是利用等效变换关系, 求


$$
R_{\text {in }}=R_{\text {eq }}=\frac{(2+3) \times 5}{2+3+5}=2.5 \Omega
$$

方法 3- 一齐次法

根据齐次性原理, 可以在不含独立电源的一端口电路的端口处加一个 $1 \mathrm{~A}$ 电流源求其端 口处的电压响应, 此电压值即为人端电阻 $R_{\text {in }}$ 值; 也可以在端口处加一个 $1 \mathrm{~V}$ 电压源求其端口 处的电流响应, 此电流值的倒数即为人端电阻 $R_{\text {in }}$ 值。现将原电路图 (a) 中的独立电源置零后 的一端口电路的端口处加一个 $1 \mathrm{~A}$ 电流源, 见图 (f), 根据 KVL 有

$$
U_{\text {in }}=2 I_{1}+3 I_{1}
$$

得

$$
I_{1}=\frac{U_{\text {in }}}{5}
$$

又因为 $U_{\mathrm{in}}=5\left(1-I_{1}\right)=5\left(1-\frac{U_{\mathrm{in}}}{5}\right)$

解得 $U_{\text {in }}=2.5 \mathrm{~V}$

$$
\text { 即 } R_{\text {in }}=\frac{U_{\text {in }}}{1}=\frac{2.5}{1}=2.5 \Omega
$$

当端口处加 $1 \mathrm{~V}$ 电压源时的电路为图 $(\mathrm{g})$, 可有

$$
I_{2}=\frac{1}{5} \mathrm{~A}, 2 I_{1}+3 I_{1}=1
$$

即 $I_{1}=\frac{1}{5} \mathrm{~A}$

$$
I_{\text {in }}=I_{1}+I_{2}=\frac{1}{5}+\frac{1}{5}=\frac{2}{5} \mathrm{~A}
$$

得 $\quad R_{\text {in }}=\frac{1}{I_{\text {in }}}=\frac{5}{2}=2.5 \Omega$

在此方法中也可以根据替代定理, 将控制变量设定成 $1 \mathrm{~A}$, 如图 $(\mathrm{h})$, 求端口处的电压与电 流之比为人端电阻 $R_{\text {in }}$ 。由图 $(\mathrm{h})$ 可得

$$
U_{\text {in }}=2 \times 1+3 \times 1=5 \mathrm{~V}, I_{\text {in }}=1+\frac{5}{5}=2 \mathrm{~A}
$$

得 $\quad R_{\text {in }}=\frac{U_{\text {in }}}{I_{\text {in }}}=\frac{5}{2}=2.5 \Omega$

方法 4- 一开路短路法

此方法是根据戴维南定理, 若同时求出含源一端口的开路电压 $U_{\mathrm{oc}}$ 和短路电流 $I_{\mathrm{sc}}$ 后, 两者

有

$$
2 I_{1}+10+3 I_{1}=0
$$

由于 $5 \Omega$ 电阻被短路, 则 $I_{1}=-I_{\mathrm{sc}}$ 。根据 KVL 有

$$
-2 I_{\mathrm{sc}}+10-3 I_{\mathrm{sc}}=0
$$

解得 $I_{\mathrm{SC}}=\frac{10}{2+3}=2 \mathrm{~A}$ 可得 $R_{\mathrm{in}}=\frac{U_{\mathrm{OC}}}{I_{\mathrm{SC}}}=\frac{5}{2}=2.5 \Omega$

(4) 原电路的等效电路为图 $(\mathrm{j})$ 。

(5)所需求解的电流响应为

$$
I_{\mathrm{RL}}=\frac{U_{\mathrm{OC}}}{R_{\mathrm{in}}+R_{\mathrm{L}}}=\frac{5}{2.5+2.5}=1 \mathrm{~A}
$$

\section{4. 最大功率传输条件}

最大功率传输条件是,当负载电阻等于去掉负载电阻后的戴维南等效电路中的内阻 $R_{\mathrm{in}}$

载中获得的最大功率可用下式直接计算

$$
P_{\mathrm{L}, \max }=\frac{U_{\mathrm{oC}}^{2}}{4 R_{\mathrm{L}}}
$$

例如在上述例 1.2-13 中, 因为 $R_{\mathrm{L}}=R_{\mathrm{in}}=2.5 \Omega$, 所以负载电阻中所获得的最大功率为

$$
P_{\mathrm{L}, \text { max }}=\frac{U_{\mathrm{OC}}^{2}}{4 R_{\mathrm{L}}}=\frac{5^{2}}{4 \times 2.5}=2.5 \mathrm{~W}
$$

\section{5. 诺顿定理}

定理内容: 任何一个含有独立电源的线性一端口电阻电路, 对外电路而言可以用一个独立 电流源和一个线性电导相并联的电路等效替代; 其独立电流源的电流为该含源一端口电路在 端口处的短路电流 $i_{\mathrm{SC}}$; 其并联电导为该含源一端口电路中所有独立电源置零后, 端口处的人 端电导 $G_{\text {in。 }}$ 。

人端电阻 $R_{\mathrm{in}}$ 的倒数为人端电导 $G_{\mathrm{in}}$ 。其定义是: 对一个不含独立电源的一端口电路, 在端 口处的电流 $i_{\text {in }}$ 和端口处的电压 $u_{\text {in }}$ 在关联方向下的比值, 即

$$
G_{\text {in }}=\frac{1}{R_{\text {in }}}=\frac{i_{\text {in }}}{u_{\text {in }}}
$$

用诺顿定理等效后的电流源 $i_{\mathrm{SC}}$ 和电导 $G_{\mathrm{in}}$ 并联电路称为原含源一端口电路的诺顿等效电 路。

诺顿定理可以用图 1.2-20 帮助理解和记 忆。

对同一个线性一端口电阻电路的诺顿等 效电路与戴维南等效电路之间可进行等效变 换。

【例 1.2-14】用诺顿定理求解例 1.2-13 电路中的电流 $I_{R \mathrm{~L}}$ 。

解: 在例 1. 2-13 中已求得短路电流 $I_{\mathrm{SC}}=2$ $\mathrm{A}, R_{\mathrm{in}}=2.5 \Omega$, 可得

$$
G_{\text {in }}=\frac{1}{R_{\text {in }}}=\frac{1}{2.5}=0.4 \mathrm{~S}
$$


也可以直接从例 1.2-13 所得戴维南运用非理想电源间的等效变换关系得 

$$
J_{S C}=\frac{U_{\mathrm{oC}}}{R_{\mathrm{in}}}=\frac{5}{2.5}=2 \mathrm{~A}
$$



$$
G_{\text {in }}=\frac{1}{R_{\text {in }}}=\frac{1}{2.5}=0.4 \mathrm{~S}
$$

应用诺顿定理得此例题的等效电路为图 1.2-21, 最后得

$$
I_{R L}=I_{\mathrm{SC}} \frac{1 / G_{\text {in }}}{\left(1 / G_{\text {in }}\right)+R_{\mathrm{t} .}}=2 \times \frac{1 / 0.4}{1 / 0.4+2.5}=1 \mathrm{~A}
$$

\section{3 正弦电流电路}

\subsection{1 正弦量的三要素和有效值}

\section{1. 正弦量的三要素}

正弦量的幅值 (振幅、最大值)、频率(角频率) 和相位 (相角) 称为正弦量的三要素。正弦 电流、电压的表达式为

$$
\begin{aligned}
& i=I_{\mathrm{m}} \sin \left(\omega t+\psi_{i}\right) \\
& u=U_{\mathrm{m}} \sin \left(\omega t+\psi_{u}\right)
\end{aligned}
$$

式中: $I_{\mathrm{m}} 、 U_{\mathrm{m}}$ 为正弦电流、电压的最大值 (幅值); $\omega$ 为正弦电流、电压的角频率, 它与频率 $f$ 的关 系为

$$
\omega=2 \pi f
$$

因为正弦量的周期 $T=2 \pi$, 所以 $\omega 、 T$ 和 $f$ 三者有如下两关系式:

$$
f=\frac{1}{T}, \quad \omega=\frac{2 \pi}{T}
$$

$\left(\omega t+\psi_{i}\right)$ 和 $\left(\omega t+\psi_{u}\right)$ 分别称为电流和电压的相位。 $t=0$ 的相位称为初相位, 简称初相, 即 $\psi_{i}$ 和 $\psi_{u}$ 分别称为电流和电压的初相。

电压和电流的相位之差称为相位差, 用 $\varphi$ 表示, 即

$$
\varphi=\left(\omega t+\psi_{u}\right)-\left(\omega t+\psi_{i}\right)
$$

在同频率的情况下相位差称为初相差, 即

$$
\varphi=\psi_{u}-\psi_{i}
$$

\section{2. 有效值}

在正弦交流电中根据热等效原理, 定义电流和电压的有效值为其瞬时值在一个周期内的 方均根值,分别用 $I$ 和 $U$ 表示, 即

$$
I=\sqrt{\frac{1}{T} \int_{0}^{T} i^{2} \mathrm{~d} t}=\frac{I_{\mathrm{m}}}{\sqrt{2}}, \quad U=\sqrt{\frac{1}{T} \int_{0}^{T} u^{2} \mathrm{~d} t}=\frac{U_{\mathrm{m}}}{\sqrt{2}}
$$

【例 1.3-1】一个周期为 $50 \mathrm{~Hz}$, 有效值为 $380 \mathrm{~V}$ 的正弦电压, 其角频率 $\omega$ 和最大值 $U_{\mathrm{m}}$ 各 为多少?

解: $\omega=2 \pi f=2 \pi \times 50=314 \mathrm{rad} / \mathrm{s}$

$$
U_{\mathrm{m}}=\sqrt{2} U=380 \sqrt{2}=537 \mathrm{~V}
$$

【例 1.3-2】现有电压 $u=220 \sqrt{2} \sin 314 t(\mathrm{~V})$ 和电流 $i=2 \sqrt{2} \sin \left(314 t+\frac{\pi}{2}\right)(\mathrm{A})$ 的两正弦 量, 它们的相位差 $\varphi$ 为多少? 解: $\varphi=\psi_{u}-\psi_{i}=0-\frac{\pi}{2}=-\frac{\pi}{2}$

1.3 .2 电感、电容元件电流、电压关系的相量形式及基尔霍夫定律的相量形式

\section{1. 电感元件电流、电压关系的相量形式}

在图 1.3-1 的关联方向下电感电流相量 $i_{L}$ 和电感电压相量 $U_{L}$ 之间的关系为

$$
\begin{aligned}
& \dot{U}_{L}=\mathrm{j} X_{L} \dot{I}_{L} \\
& U_{L} \angle \psi_{u L}=X_{L} I_{L} \angle \psi_{i L}+\frac{\pi}{2} \\
& \dot{I}_{L}=-\mathrm{j} B_{L} U_{L} \\
& I_{L} \angle \psi_{i}=B_{L} U_{L} \angle \psi_{u L}-\frac{\pi}{2}
\end{aligned}
$$



式中的 $X_{L}=\omega L$ 称为电感的电抗, 简称感抗, 是电感元件的交流参数。它的定义是电感上的电 压有效值 (或最大值) 和电流有效值 (或最大值) 之比; $B_{L}=1 / \omega L$ 称为电感的电纳, 简称感纳, 也是电感元件的交流参数。它的定义是电感上的电流有效值(或最大值)和电压有效值 (或最 大值)之比, 即电感元件的交流参数有如下两个表达式:



$$
X_{L}=\frac{U_{L}}{I_{L}}=\frac{U_{L \mathrm{~m}}}{I_{L \mathrm{~m}}}, B_{L}=\frac{I_{L}}{U_{L}}=\frac{I_{L \mathrm{~m}}}{U_{L \mathrm{~m}}}
$$

电感元件上的相量图为图 1.3-2, 即电感两端电压相量超前于电流相量 $\pi / 2$ 。

\section{2. 电容元件电流、电压关系的相量形式}

在图 1.3-3 的关联方向下电容电流相量 $\dot{I}_{C}$ 和电感电压相量 $U_{C}$ 之间的关系为

$$
\begin{aligned}
& \dot{U}_{C}=-\mathrm{j} X_{C} \dot{I}_{C} \\
& U_{c} \angle \psi_{u C}=X_{C} I_{C} \angle \psi_{i c}-\frac{\pi}{2} \\
& \dot{I}_{C}=\mathrm{j} B_{C} U_{C} \\
& I_{C} \angle \psi_{i C}=B_{C} U_{C} \angle \psi_{u C}+\frac{\pi}{2}
\end{aligned}
$$



式中的 $X_{C}=1 / \omega C$ 称为电容的电抗, 简称容抗, 是电容元件的交流参数。它的定义是电容上的 电压有效值 (或最大值) 和电流有效值 (或最大值) 之比; $B_{C}=\omega C$ 称为电容的电纳, 简称容纳, 也是电容元件的交流参数。它的定义是电容上的电流有效值(或最大值)和电压有效值 (或最 大值)之比, 即电容元件的交流参数有如下两个表达式:



$$
X_{C}=\frac{U_{C}}{I_{C}}=\frac{U_{C_{\mathrm{m}}}}{I_{C \mathrm{~m}}}, B_{C}=\frac{I_{C}}{U_{C}}=\frac{I_{C \mathrm{~m}}}{U_{C \mathrm{~m}}}
$$

电容元件上的相量图为图 1.3-4, 即电容两端电流相量超前于电压相量 $\pi / 2$ 。

\section{3. 基尔霍夫的相量形式}

KCL 的相量形式为 $\sum \dot{I}=0$, 即在同频率的正弦电路中, 对任意节点, 在 任何时刻流人 (流出) 该节点的电流相量的代数和恒等于零。

$\mathrm{KVL}$ 的相量形式为 $\sum U=0$, 即在同频率的正弦电路中, 对任意闭合回路, 在任何时刻沿 回路循行时总的电压降相量的代数和恒等于零。 【例 1.3-3】在图 1. 3-5 电路中, 已知: $R=3 \Omega, X_{L}=8 \Omega, X_{C}=4 \Omega, I=1 \angle 0^{\circ} \mathrm{A}$, 求电阻电 压相量 $U_{R}$ 、电感电压相量 $U_{L}$ 、电容电压相量 $U_{C}$ 和电源电压相量 $U_{\mathrm{S}}$ 。



解 : 根据电阻、电感和电容元件电流、电压关系的相量形式得

$$
\begin{aligned}
& U_{R}=R \dot{I}=3 \times 1 \angle 0^{\circ}=3 \angle 0^{\circ} \mathrm{V} \\
& U_{L}=\mathrm{j} X_{L} \dot{I}=\mathrm{j} 8 \times 1 \angle 0^{\circ}=\mathrm{j} 8=8 \angle 90^{\circ} \mathrm{V} \\
& U_{C}=-\mathrm{j} X_{\mathrm{C}} \dot{I}=-\mathrm{j} 4 \times 1 \angle 0^{\circ}=-\mathrm{j} 4=4 \angle-90^{\circ} \mathrm{V}
\end{aligned}
$$

根据 KVL 的相量形式得

$$
U_{\mathrm{S}}=\dot{U}_{R}+\dot{U}_{L}+\dot{U}_{C}=3+\mathrm{j} 8-\mathrm{j} 4=3+\mathrm{j} 4=5 \angle 53.1^{\circ} \mathrm{V}
$$
量 $i$ 。

【例 1.3-4】在图 1.3-6 电路中, 已知: $U_{\mathrm{S}}=10 \angle 0^{\circ} \mathrm{V}, X_{L}=5 \Omega, X_{C}=10 \Omega$, 求电源电流相

解: 在电路中设电感和电容中的电流相量分别为 $i_{L}$ 和 $i_{C}$, 根据电 感和电容元件电流、电压关系的相量形式得

$$
\begin{aligned}
& i_{L}=\frac{U_{\mathrm{S}}}{\mathrm{j} X_{L}}=\frac{10 \angle 0^{\circ}}{5 \angle 90^{\circ}}=2 \angle-90^{\circ}=-\mathrm{j} 2 \mathrm{~A} \\
& \dot{I}_{C}=\frac{\dot{U}_{\mathrm{S}}}{-\mathrm{j} X_{C}}=\frac{10 \angle 0^{\circ}}{-\mathrm{j} 10}=1 \angle 90^{\circ}=\mathrm{j} 1 \mathrm{~A}
\end{aligned}
$$



根据 KCL 的相量形式得

$$
\dot{I}=\dot{I}_{L}+\dot{I}_{C}=-\mathrm{j} 2+\mathrm{j} 1=-\mathrm{j} 1=1 \angle-90^{\circ} \mathrm{A}
$$

\subsection{3 阻抗、导纳、有功功率、无功功率、视在功率和功率因数}

\section{1. 阻抗和导纳}

对图 1.3-7 (a) 不含独立电源的正弦交流一端口电路 $N_{0}$, 端口处的电压相量 $U\left(U_{\mathrm{m}}\right)$ 与电 流相量 $I\left(\dot{I}_{\mathrm{m}}\right)$ 在关联方向下之比为该电路的复阻抗 $Z$, 即

$$
Z=\frac{U}{I}=\frac{U_{\mathrm{m}}}{I_{\mathrm{m}}}=|Z| \angle \varphi_{Z}
$$

式中:复阻抗的模 $|Z|$ 称为电路的阻抗; 幅角 $\varphi_{z}$ 称为阻抗角。

若不含独立电源的正弦交流一端口电路 $N_{0}$ 为 $R 、 L 、 C$ 串联电路, 见 1.3-7(b), 则

$$
Z=R+\mathrm{j} X=R+\mathrm{j}\left(X_{L}-X_{C}\right)=R+\mathrm{j}\left(\omega L-\frac{1}{\omega C}\right)=|Z| \angle \psi_{Z}
$$

式中 $X=X_{L}-X_{C}$ 称为电路中的电抗。当 $X_{L}>X_{C}$ 时电路为感性, 当 $X_{C}>X_{L}$ 时电路为容性。电 路的阻抗 $|Z|$ 和阻抗角 $\varphi_{Z}$ 与串联电路中的参数关系为

$$
\begin{aligned}
& |Z|=\sqrt{R^{2}+X^{2}} \\
& \varphi_{Z}=\arctan \frac{X}{R}
\end{aligned}
$$

当 $\varphi_{Z}>0$ 时电路为感性, 当 $\varphi_{Z}<0$ 时电路为容性。

电阻 $R$ 、电抗 $X$ 、阻抗 $|Z|$ 和阻抗角 $\varphi_{Z}$ 构成阻抗三角形, 见图 1.3-7(c)。

对图 1.3-7 (a) 不含独立电源的正弦交流一端口电路 $N_{0}$, 端口处的电流相量 $\dot{I}\left(\dot{I}_{\mathrm{m}}\right)$ 与电压 相量 $U\left(U_{\mathrm{m}}\right)$ 在关联方向下之比为该电路的复导纳 $Y$, 即

$$
Y=\frac{i}{U}=\frac{i_{\mathrm{m}}}{U_{\mathrm{m}}}=|Y| \angle \varphi_{Y}
$$

式中:复导纳的模 $|Y|$ 称为电路的导纳; 幅角 $\varphi_{Y}$ 称为导纳角。

若不含独立电源的正弦交流一端口电路 $N_{0}$ 为 $R 、 L 、 C$ 并联电路 (见1.3-7 (d)), 则

$$
Y=G+\mathrm{j} B=G+\mathrm{j}\left(B_{C}-B_{L}\right)=|Y| \angle \varphi_{Y}
$$

式中: $B=B_{C}-B_{L}$ 称为电路中的电纳。当 $B_{C}>B_{L}$ 时电路为感性, 当 $B_{L}>B_{C}$ 时电路为容性。电 路的导纳 $|Y|$ 和阻抗角 $\varphi_{Y}$ 与并联电路中的参数关系为

$$
\begin{aligned}
& |Y|=\sqrt{G^{2}+B^{2}} \\
& \varphi_{Y}=\arctan \frac{B}{G}
\end{aligned}
$$

电导 $G$ 、电纳 $B$ 、导纳 $|Y|$ 和导纳角 $\varphi_{Y}$ 构成导纳三角形, 见图 1.3-7(e)。

对同一个不含独立电源的正弦交流一端口电路 $N_{0}$, 复阻抗 $Z$ 和复导纳 $Y$ 互为倒数; 导纳 角 $\varphi_{Y}$ 为阻抗角 $\varphi_{Z}$ 的负值, 即

$$
\begin{aligned}
& Y=\frac{1}{Z} \\
& Z=\frac{1}{Y} \\
& \varphi_{Y}=-\varphi_{Z}
\end{aligned}
$$

\section{2. 有功功率}

对一个正弦交流一端口电路 $N$ (见图 1.3-8), 它的瞬时功率 $p$ 为端口电压 的瞬时值 $u$ 与端口电流的瞬时值 $i$ 的乘积, 即

$$
p=u i
$$

设 $u=U_{\mathrm{m}} \sin \left(\omega t+\psi_{u}\right), i=I_{\mathrm{m}} \sin \left(\omega t+\psi_{i}\right)$, 则



$$
p=u i=U_{\mathrm{m}} \sin \left(\omega t+\psi_{u}\right) I_{\mathrm{m}} \sin \left(\omega t+\psi_{\mathrm{i}}\right)=U I \cos \left(\psi_{u}-\psi_{i}\right)-U I \cos \left(2 \omega t+\psi_{u}+\psi_{i}\right)
$$

有功功率定义: 瞬时功率 $p$ 在一个周期内的平均值为有功功率, 又称平均功率, 用大写 $P$ 表示,单位为 $W$ (瓦), 其数学表达式为

$$
P=\frac{1}{T} \int_{0}^{T} p \mathrm{~d} t=U I \cos \varphi
$$

式中 $\varphi=\psi_{u}-\psi_{i}$, 即为电路的阻抗角。

有功功率的物理意义是电路中消耗的功率。

\section{3. 无功功率}

无功功率的定义: 将图 1.3-8 正弦交流一端口电路中端口处的电压有效值 $U$ 、电流有效值 $I$ 和阻抗角的正弦值 $\sin \varphi$ 三者的乘积定义为交流电路的无功功率 $Q$, 单位为 $\operatorname{Var}$ (无功伏 安), 即

$$
Q=U I \sin \varphi
$$

无功功率的物理意义是电路 $N$ 与电源交换能量的最大速率。 

\section{4. 视在功率}

视在功率的定义: 将图 1.3-8 正弦交流一端口电路中端口处的电压有效值 $U$ 、电流有效值 $I$ 的乘积定义为交流电路的视在功率 $S$, 单位为 VA (伏安), 即

$$
S=U I
$$

视在功率的物理意义是电路 $N$ 所需占用电源的容量。

\section{5. 功率因数}

功率因数的定义是在图 1.3-8 的交流电路 $N$ 中阻抗角的余弦值,用 $\lambda$ 表示, 它的物理意义 是交流电路中的有功功率与视在功率的比值, 即



$$
\lambda=\cos \varphi=\frac{P}{S}
$$

有功功率、无功功率和视在功率三者的关系为

$$
S=\sqrt{P^{2}+Q^{2}}
$$

此关系可用图 1.3-9 所示的功率三角形帮助记忆交流电路中的各种功率的计算 式。

【例 1.3-5】图 1.3-10 (a) 为一个不含独立电源的交流一端口电路 $N_{0}$, 已知电源电压 $u_{\mathrm{S}}$ $=120 \sin 1000 t \mathrm{~V}$, 电流 $i=8 \sin \left(1000 t-53.1^{\circ}\right) \mathrm{A}$ 。试分别用两个元件的串联和并联电路等效该电路。

解: 由已知 $u 、 i$ 瞬时值表达式得知电压导前电流, 则 $N_{0}$ 为感性电路, 图 1.3-10(b) 的电阻 和电感串联电路与图 1.3-10 (c) 的电阻和电感并联电路为其等效电路。在图 1.3-10(b) 中有

$$
Z=\frac{U_{\mathrm{m}}}{I_{\mathrm{m}}}=\frac{120 \angle 0^{\circ}}{8 \angle-53.1^{\circ}}=15 \angle 53.1^{\circ}=9+\mathrm{j} 12 \Omega
$$

得

$$
R=9 \Omega, X_{L}=12 \Omega, L=\frac{X_{L}}{\omega}=\frac{12}{1000}=0.012 \mathrm{H}=12 \mathrm{mH}
$$

在图 1.3-10(c) 中有

$$
\begin{aligned}
& Y=\frac{1}{Z}=\frac{1}{15 \angle 53.1^{\circ}}=0.067 \angle-53.1^{\circ} \mathrm{S}=0.04-\mathrm{j} 0.053 \mathrm{~S}=G^{\prime}-\mathrm{j} B^{\prime} \\
& R^{\prime}=\frac{1}{G^{\prime}}=\frac{1}{0.04}=25 \Omega, X_{L}^{\prime}=\frac{1}{B^{\prime}}=\frac{1}{0.053}=18.9 \Omega \\
& L^{\prime}=\frac{X_{L}^{\prime}}{\omega}=\frac{18.9}{1000}=0.0189 \mathrm{H}=18.9 \mathrm{mH}
\end{aligned}
$$

【例 1.3-6】求图 1.3-11 电路的复阻抗 $Z$ 。 解: $Z=10+\frac{(10+\mathrm{j} 10)(-\mathrm{j} 20)}{10+\mathrm{j} 10-\mathrm{j} 20}=10+\frac{200-\mathrm{j} 200}{10-\mathrm{j} 10}=10+20=30 \Omega$





【例 1.3-7】 在图 1.3-12 电路中, $R_{1}=R_{2}=25 \Omega, X_{L}=X_{C}=33.3 \Omega$, 求电路的总复阻抗 $Z$ 。

解法 1: $Y_{1}=\frac{1}{R_{1}}-\mathrm{j} \frac{1}{X_{L}}=\frac{1}{25}-\mathrm{j} \frac{1}{33.3}=0.04-\mathrm{j} 0.03=0.05 \angle-36.9^{\circ} \mathrm{S}$

$$
\begin{aligned}
Y_{2} & =\frac{1}{R_{2}}+\mathrm{j} \frac{1}{X_{C}}=\frac{1}{25}+\mathrm{j} \frac{1}{33.3}=0.04+\mathrm{j} 0.03=0.05 \angle 36.9^{\circ} \mathrm{S} \\
Z & =Z_{1}+Z_{2}=\frac{1}{Y_{1}}+\frac{1}{Y_{2}}=\frac{1}{0.05 \angle-36.9^{\circ}}+\frac{1}{0.05 \angle 36.9^{\circ}}=20 \angle 36.9^{\circ}+20 \angle-36.9^{\circ} \\
& =16+\mathrm{j} 12+16-\mathrm{j} 12=32 \Omega
\end{aligned}
$$

解法 $2: Z=Z_{1}+Z_{2}=\frac{R_{1}\left(\mathrm{j} X_{L}\right)}{R_{1}+\mathrm{j} X_{L}}+\frac{R_{2}\left(-\mathrm{j} X_{C}\right)}{R_{2}-\mathrm{j} X_{C}}=\frac{25(\mathrm{j} 33.3)}{25+\mathrm{j} 33.3}+\frac{25(-\mathrm{j} 33.3)}{25-\mathrm{j} 33.3}$

$$
\begin{aligned}
& =\frac{832.5 \angle 90^{\circ}}{41.6 \angle 53.11^{\circ}}+\frac{832.5 \angle-90^{\circ}}{41.6 \angle-53.11^{\circ}}=20 \angle 36.9^{\circ}+20 \angle-36.9^{\circ} \\
& =16+\mathrm{j} 12+16-\mathrm{j} 12=32 \Omega
\end{aligned}
$$

【例 1.3-8】 在图 1.3-13 电路中, 已知: $U_{\mathrm{S}}=100 \angle 0^{\circ} \mathrm{V}, R=30 \Omega, X_{L}$ $=40 \Omega$ 。求电路中的视在功率、有功功率、无功功率。

解: $\dot{I}=\frac{U_{\mathrm{S}}}{R+\mathrm{j} X_{L}}=\frac{100 \angle 0^{\circ}}{30+\mathrm{j} 40}=\frac{100 \angle 0^{\circ}}{50 \angle 53.1^{\circ}}=2 \angle-53.1^{\circ} \mathrm{A}$

$$
\begin{aligned}
& S=U I=100 \times 2=200 \mathrm{VA}, P=U I \cos \varphi=100 \times 2 \cos 53.1^{\circ}=120 \mathrm{~W} \\
& Q=U I \sin \varphi=100 \times 2 \sin 53.1^{\circ}=160 \mathrm{Var}
\end{aligned}
$$



【例 1.3-9】在图 1.3-14(a) 电路中, 已知: $U_{\mathrm{s}}=100 \angle 0^{\circ} \mathrm{V}, R=16 \Omega, L=38.2 \mathrm{mH}$, 电源 频率 $f=50 \mathrm{~Hz}, C=90.5 \mu \mathrm{F}$ 。先求无并联电容时的电流 $I$ 和功率因数 $\lambda$; 再求并联电容后的电 流 $I^{\prime}$ 、功率因数 $\lambda^{\prime}$ 和电容支路中的电流 $I_{C}$, 并画出包括 $\dot{U}_{\mathrm{S}} 、 I^{\prime} I^{\prime}$ 和 $\dot{I}_{C}$ 的相量图。

\section{解: 无电容时电路的复阻抗为}

$$
Z=R+\mathrm{j} X_{L}=R+\mathrm{j} 2 \pi f L=16+\mathrm{j} 2 \pi \times 50 \times 38.2 \times 10^{-3}=16+\mathrm{j} 12 \Omega
$$


得

$$
\begin{aligned}
& I=\frac{U_{\mathrm{S}}}{Z}=\frac{100 \angle 0^{\circ}}{16+\mathrm{j} 12}=\frac{100 \angle 0^{\circ}}{20 \angle 36.9^{\circ}}=5 \angle-36.9^{\circ} \mathrm{A} \\
& I=5 \mathrm{~A}, \lambda=\cos \varphi=\cos \left(-36.9^{\circ}\right)=0.8
\end{aligned}
$$

并联电容后电容的容抗为


$$
X_{C}=\frac{1}{2 \pi f C}=\frac{1}{2 \pi \times 50 \times 90.5 \times 10^{-6}}=35.1 \Omega
$$

电路的复阻抗为

$$
\begin{aligned}
Z^{\prime} & =\frac{\left(R+\mathrm{j} X_{L}\right)\left(-\mathrm{j} X_{C}\right)}{R+\mathrm{j} X_{L}-\mathrm{j} X_{C}}=\frac{(16+\mathrm{j} 12)(-\mathrm{j} 35.1)}{16+\mathrm{j} 12-\mathrm{j} 35.1} \\
& =\frac{20\left[36.9^{\circ} \times 35.1 \angle-90^{\circ}\right.}{26-\mathrm{j} 23.1} \\
& =\frac{702 L-53.1^{\circ}}{34.8\left\lfloor-41.6^{\circ}\right.}=20.2\left\lfloor-11.5^{\circ} \Omega\right.
\end{aligned}
$$

并联电容后

$$
\begin{aligned}
& \dot{I}^{\prime}=\frac{U_{S}}{Z^{\prime}}=\frac{100 \angle 0^{\circ}}{20.2 \angle-11.5^{\circ}}=4.95 \angle 11.5^{\circ} \mathrm{A}, I^{\prime}=4.95 \mathrm{~A} \\
& \lambda^{\prime}=\cos 11.5^{\circ}=0.98 \approx 1 \\
& \dot{I}_{C}=\frac{U_{\mathrm{S}}}{-\mathrm{j} X_{C}}=\frac{100 \angle 0^{\circ}}{35.1 \angle-90^{\circ}}=28.4 \angle 90^{\circ} \mathrm{A}, I_{C}=2.84 \mathrm{~A}
\end{aligned}
$$

相量图见图 1.3-14(b)。

\subsection{4 正弦电流电路分析的相量方法}

\section{1. 相量计算方法}

在同频率的正弦电路中, 电路分析的相量计算法应遵循以下原则:

(1) 将电路中的变量用相量表示;

(2)将电路中的参数用复参数形式表示;

(3)画出电路的相量模型;

(4)选用系统分析法中的某种方法列出复数方程, 解方程求得所需变量的相量或所需求解 的复参数;

(5)应用电路的基本定理,求得所需变量的相量或所需求解的复参数;

(6) 将求得变量的相量形式变换成所需变量的交流变量值, 或由所得的复参数变成所需求 解的交流参数或元件参数。

【例 1.3-10】在图 1.3-15(a) 电路中, 已知: $u_{\mathrm{S}}=2 \sqrt{2} \sin \omega t \mathrm{~V}, i_{\mathrm{S}}=\sqrt{2} \sin \omega t \mathrm{~A}, \beta=1, R=2$ $\Omega, X_{L}=2 \Omega, X_{C}=2 \Omega$, 求电感中的电流 $i_{L}$ 和电容两端电压 $u_{C}$ 。






解: 图 1.3-15(a) 电路的相量模型为图 1.3-15(b)。选用网孔电流法, 在图 (b) 中设三个 网孔电流 $i_{1} 、 i_{2}$ 和 $i_{3}$, 则 $i_{3}=i_{\mathrm{S}}=1 \angle 0^{\circ} \mathrm{A}$, 只需列写如下两个方程:

$$
\left\{\begin{array}{l}
(2+\mathrm{j} 2) \dot{I}_{1}-\mathrm{j} 2 \dot{I}_{2}-2 \times 1 \angle 0^{\circ}=2 \angle 0^{\circ} \\
\dot{I}_{2}=\dot{I}=\dot{I}_{1}-1 \angle 0^{\circ}
\end{array}\right.
$$

将式(2)代人式(1)有

$$
(2+\mathrm{j} 2) \dot{I}_{1}-\mathrm{j} 2\left(\dot{I}_{1}-1 \angle 0^{\circ}\right)=2 \angle 0^{\circ}+2 \angle 0^{\circ}
$$

即

$$
(2+\mathrm{j} 2-\mathrm{j} 2) \dot{I}_{1}=4-\mathrm{j} 2
$$

得

$$
i_{1}=2-\mathrm{j} 1 \mathrm{~A}
$$

将此结果代人式(2)得

$$
i_{2}=2-\mathrm{j} 1-1=1-\mathrm{j} 1 \mathrm{~A}
$$

由图(b) 可得

$$
\begin{aligned}
& \dot{I}_{L}=\dot{I}_{1}-\dot{I}_{2}=2-\mathrm{j} 1-1+\mathrm{j} 1=1 \angle 0^{\circ} \mathrm{A} \\
& \dot{U}_{c}=\left(\dot{I}_{2}-\dot{I}_{3}\right) \times(-\mathrm{j} 2)=(1-\mathrm{j} 1-1) \times(-\mathrm{j} 2)=2 \angle 180^{\circ} \mathrm{A}
\end{aligned}
$$

最后得

$$
i_{L}=\sqrt{2} \sin \omega t \mathrm{~A}, u_{C}=2 \sqrt{2} \sin \left(\omega t+180^{\circ}\right) \mathrm{V}
$$

【例 1.3-11】在图 1.3-16(a) 电路中, 已知: $u_{\mathrm{S}}=\sqrt{2} \sin \omega t \mathrm{~V}, i_{\mathrm{S}}=\sqrt{2} \sin \omega t \mathrm{~A}, r=2 \Omega, R=1$ $\Omega, X_{\mathrm{C}}=3 \Omega$, 求 $X_{L}$ 为何值时流过它的电流有效值最大, 此电流为多少?


解: 电路的相量模型为图 1.3-16(b)。选用戴维南定理, 从电感两端开路, 开路后左侧电 路为图 1.3-16(c), 由节点电压法可有如下方程组:

$$
\left\{\begin{array}{l}
\left(\frac{1}{-\mathrm{j} 3}+1\right) U_{\mathrm{OC}}=\frac{1 \angle 0^{\circ}}{-\mathrm{j} 3}+\frac{2 \dot{I}_{1}}{1}+1 \\
I_{1}=\frac{1 \angle 0^{\circ}-U_{\mathrm{OC}}}{-\mathrm{j} 3}
\end{array}\right.
$$

将式(2)代人式(1)有

$$
\left(\frac{1}{-\mathrm{j} 3}+1\right) U_{\mathrm{oc}}=\mathrm{j} \frac{1}{3}+\mathrm{j} \frac{2}{3}-\mathrm{j} \frac{2}{3} U_{\mathrm{oc}}+1
$$

即

$$
\begin{aligned}
& \left(\mathrm{j} \frac{1}{3}+1+\mathrm{j} \frac{2}{3}\right) U_{O C}=\mathrm{j} 1+1 \\
& (1+\mathrm{j} 1) U_{O C}=\mathrm{j} 1+1
\end{aligned}
$$

得

$$
\dot{U}_{\mathrm{OC}}=1 \angle 0^{\circ} \mathrm{A}
$$

将图 1.3-16(c) 电路的独立电源置零后, 求人端复阻抗的电路为图 1.3-16(d), 在此电路 中按关联方向设端口电压 $U_{\text {in }}$ 端口电流 $i_{\text {in }}$ 和支路电流 $i_{2}$, 则有

$$
\begin{aligned}
& \dot{I}_{1}=-\frac{1}{-\mathrm{j} 3} \dot{U}_{\text {in }}=-\mathrm{j} \frac{1}{3} U_{\text {in }} \\
& \dot{I}_{2}=\frac{U_{\text {in }}-2 \dot{I}_{1}}{1}=U_{\text {in }}-2\left(-j \frac{1}{3} U_{\text {in }}\right)=U_{\text {in }}+\mathrm{j} \frac{2}{3} U_{\text {in }} \\
& \dot{I}_{\text {in }}=-I_{1}+\dot{I}_{2}=\mathrm{j} \frac{1}{3} U_{\text {in }}+U_{\text {in }}+\mathrm{j} \frac{2}{3} U_{\text {in }}=(1+\mathrm{j} 1) U_{\text {in }}
\end{aligned}
$$

得

$$
Z_{\text {in }}=\frac{U_{\text {in }}}{I_{\text {in }}}=\frac{U_{\text {in }}}{(1+\mathrm{j} 1) U_{\text {in }}}=\frac{1}{(1+\mathrm{j} 1)}=\frac{1}{\sqrt{2} \angle 45^{\circ}}=\frac{1}{\sqrt{2}} \angle-45^{\circ}=0.5-\mathrm{j} 0.5 \Omega
$$

原电路的等效电路为图 1.3-16(e), 由此电路可有下式:

$$
i_{L}=\frac{1 \angle 0^{\circ}}{0.5-\mathrm{j} 0.5+\mathrm{j} X_{L}}=\frac{1}{0.5+\mathrm{j}\left(-0.5+X_{L}\right)}
$$

由此式可知当分母的虚部为零时 $i_{L}$ 最大, 则此时可有

$$
-0.5+X_{L}=0
$$

可得当 $X_{L}=0.5 \Omega$ 时 $I_{L}$ 最大。

由此可得

$$
\dot{I}_{L \max }=\frac{1 \angle 0^{\circ}}{0.5}=2 \angle 0^{\circ} \mathrm{A}, I_{L \max }=2 \mathrm{~A}
$$

\section{2. 相量图解析法}

在同频率的正弦电路中, 可以借助相量图求得待求变量或待求参数, 其原则是:

(1)在所有已知变量的相量中选择一个参考相量;

(2)将相同性质的变量采用相同的比例, 由已知条件画出电路的相量图;

(3)根据电路的基本定律在相量图中找出待求变量的相量;

(4)利用相量图中的几何解析关系求出待求相量的数值;

(5)利用相量和参数的关系求出待求参数。

【例 1.3-12】在图 1.3-17(a) 中,两个电流表的读数皆为 $5 \mathrm{~A}$, 电压表的读数为 $70.7 \mathrm{~V}$,并 且已知电压 $u_{\mathrm{S}}$ 和电流 $i_{L}$ 同相。求电感上的电压有效值 $U_{L}$ 和电阻上的电压有效值 $U_{R}$ 以及电阻 $R$ 、感抗 $X_{L}$ 和容抗 $X_{C}$ 。

解: 选电阻中的电流相量 $\dot{I}_{R}$ 为参考相量, 见图 1.3-17(b), 即 $\dot{I}_{R}=5 \angle 0^{\circ} \mathrm{A}$, 画出相量 $\dot{I}_{R}$ 。 因为 $U_{R}$ 与 $\dot{I}_{R}$ 同相, $U_{R}$ 与 $U_{C}$ 为同一电压, $\dot{I}_{C}$ 导前于 $U_{C} 90^{\circ}, I_{C}=5 \mathrm{~A}$, 所以可以画出 $\dot{I}_{C}$ 相量, 即 $\dot{I}_{C}=5 \angle 90^{\circ} \mathrm{A}$ 。

根据 KCL, 有 $\dot{I}_{L}=\dot{I}_{R}+\dot{I}_{C}$, 可画出 $\dot{I}_{L}$ 相量, 即 $\dot{I}_{L}=5 \sqrt{2} \angle 45^{\circ}=7.07 \angle 45^{\circ} \mathrm{A}$ 。 


根据已知条件 $U_{\mathrm{s}}$ 与 $\dot{I}_{L}$ 同相, 且 $U_{\mathrm{s}}=70.7 \mathrm{~V}$, 可画出 $U_{\mathrm{s}}$ 相量, 即 $U_{\mathrm{s}}=70.7 \angle 45^{\circ} \mathrm{V}$ 。

因为 $\dot{U}_{R}$ 与 $\dot{I}_{R}$ 同相, $U_{L}$ 导前于 $i_{L} 90^{\circ}$, 则可知 $U_{R}$ 和 $U_{L}$ 的方位, 又根据 $U_{\mathrm{S}}=\dot{U}_{R}+U_{L}$, 可由 $U_{S}$ 相量的顶端做平行四边形, 见图 1.3-17(b), 由此得出 $U_{L}=U_{L} \angle 135^{\circ} \mathrm{V}, U_{R}=U_{R} \angle 0^{\circ} \mathrm{V}$ 。

由 $U_{R} 、 U_{L}$ 和 $U_{\mathrm{S}}$ 所构成的三角形为等腰三角形, 因为 $U_{\mathrm{S}}=70.7 \mathrm{~V}$, 所以可得

$$
\begin{aligned}
& U_{L}=U_{\mathrm{S}}=70.7 \mathrm{~V} \\
& U_{R}=2 U_{\mathrm{S}} \sin 45^{\circ}=2 \times 70.7 \sin 45^{\circ}=100 \mathrm{~V}
\end{aligned}
$$

由变量与参数的关系可得

$$
\begin{aligned}
& R=\frac{U_{R}}{I_{R}}=\frac{100}{5}=20 \Omega \\
& X_{L}=\frac{U_{L}}{I_{L}}=\frac{70.7}{7.077}=10 \Omega \\
& X_{C}=\frac{U_{C}}{I_{C}}=\frac{U_{R}}{I_{C}}=\frac{100}{5}=20 \Omega
\end{aligned}
$$

\section{3 .5 频率特性概念}

频率特性的定义:在正弦电路中, 交流参数与角频率的关系式和变量的有效值与频率的关 系式称为频率特性。表征这些关系式的曲线称为频率特性曲线。

例如,感抗 $X_{L}$ 、容抗 $X_{C}$ 、电抗 $X$ 、阻抗 $|Z|$ 和阻抗角 $\varphi_{Z}$ 与角频率的关系式为

$$
X_{L}=\omega L, X_{C}=\frac{1}{\omega C}, X=\omega L-\frac{1}{\omega C},|Z|=\sqrt{R^{2}+\left(\omega L-\frac{1}{\omega C}\right)^{2}}, \varphi_{Z}=\arctan \frac{\omega L-\frac{1}{\omega C}}{R}
$$

以上各式为交流参数的频率特性, 它们的频率特性曲线见图 1.3-18 (a) 和 (b)。


又如在电阻 $R$ 、电感 $L$ 和电容 $C$ 串联电路中, 各变量有效值的频率特性曲线为图 1.3-18 (c)。此特性曲线主要应用于研究电路中的谐振现象。 1.3. 6 三相电路中电源和负载的连接方式及相电压、相电流、线电压、线电流、三 相功率的概念和关系

\section{1. 三相电源和三相负载的连接方式}

在三相电路中, 三相电源和三相负载都有星形 $(Y)$ 和三角形 $(\Delta)$ 两种连接方式, 因此可构 成 $Y-Y 、 Y-\Delta 、 \Delta-Y$ 和 $\Delta-\Delta 4$ 种连接方式。这 4 种连接方式称为三相三线制。此外, 在低 压供电系统中, 将 $Y-Y$ 系统中的电源中点与负载中点用中线相连, 构成 $Y_{0}-Y_{0}$ 供电系统, 称 为三相四线制。因此,三相电路中可以有 5 种基本连接方式, 见图 1.3-19。

$\mathrm{Y}_{0}-\mathrm{Y}_{0}$


\section{2. 对称三相电路及其特点}

对称三相电路是指在三相电路中, 三相电源对称, 三相负载对称, 三个线路复阻抗相等的 三相电路。

对称三相电源是指构成三相电源的三个电压源复值相等, 频率相同, 相位互差 $120^{\circ}$ 。其 正序表达式为

$$
u_{\mathrm{A}}=U_{\mathrm{m}} \sin \omega t, u_{\mathrm{B}}=U_{\mathrm{m}} \sin \left(\omega t-120^{\circ}\right), u_{\mathrm{C}}=U_{\mathrm{m}} \sin \left(\omega t+120^{\circ}\right)
$$

其负序的表达式为

$$
u_{\mathrm{A}}=U_{\mathrm{m}} \sin \omega t, u_{\mathrm{B}}=U_{\mathrm{m}} \sin \left(\omega t+120^{\circ}\right), u_{\mathrm{C}}=U_{\mathrm{m}} \sin \left(\omega t-120^{\circ}\right)
$$

在电路理论中,如不特别指明,一般皆指正序。正序的电压(或电流)波形图见图 1.3-20, 相量图见图 1.3-21。


(1)在星形连接的三相电源或三相负载中, 线电流和相电流为同一电流; 线电压是相电压的 $\sqrt{3}$ 倍, 且线电压导前于相应的相电压 $30^{\circ}$, 即有

$$
\begin{array}{ll}
I_{l}=I_{\mathrm{p}}, \quad \dot{I}_{l}=I_{\mathrm{p}}, & U_{l}=\sqrt{3} U_{\mathrm{p}} \\
\dot{U}_{\mathrm{AB}}=\sqrt{3} U_{\mathrm{AN}} \angle 30^{\circ}, & U_{\mathrm{BC}}=\sqrt{3} U_{\mathrm{BN}} \angle 30^{\circ}, \quad U_{\mathrm{CA}}=\sqrt{3} U_{\mathrm{CN}} \angle 30^{\circ}
\end{array}
$$

(2)在三角形连接的三相电源或三相负载中,线电压和相电压为同一电压;线电流是相电流 的 $\sqrt{3}$ 倍, 且线电流滞后于相应的相电流 $30^{\circ}$, 即有

$$
\begin{aligned}
& U_{l}=U_{\mathrm{p}}, \quad U_{l}=\dot{U}_{\mathrm{p}}, \quad I_{l}=\sqrt{3} I_{\mathrm{p}} \\
& \dot{I}_{\mathrm{A}}=\sqrt{3} i_{\mathrm{AB}} \angle-30^{\circ}, \quad i_{\mathrm{B}}=\sqrt{3} i_{\mathrm{BC}} \angle-30^{\circ}, \quad \dot{I}_{\mathrm{C}}=\sqrt{3} i_{\mathrm{CA}} \angle-30^{\circ}
\end{aligned}
$$

(3)三个对称的电压或三个对称的电流的瞬时值或相量之和恒等于零, 即有

$$
\begin{array}{lr}
u_{\mathrm{A}}+u_{\mathrm{B}}+u_{\mathrm{C}}=0, & \dot{U}_{\mathrm{A}}+\dot{U}_{\mathrm{B}}+\dot{U}_{\mathrm{C}}=0 \\
i_{\mathrm{A}}+i_{\mathrm{B}}+i_{\mathrm{C}}=0, & \dot{I}_{\mathrm{A}}+\dot{I}_{\mathrm{B}}+\dot{I}_{\mathrm{C}}=0
\end{array}
$$

\section{3. 三相功率}

三相电路的有功功率为各相有功功率之和, 即

$$
P=P_{\mathrm{A}}+P_{\mathrm{B}}+P_{\mathrm{C}}
$$

在对称情况下为

$$
P=3 U_{\mathrm{p}} I_{\mathrm{p}} \cos \varphi, \quad P=\sqrt{3} U_{l} I_{l} \cos \varphi
$$

式中的 $\varphi$ 角为各相负载的阻抗角。

三相电路的无功功率为各相无功功率之和, 即

$$
Q=Q_{\mathrm{A}}+Q_{\mathrm{B}}+Q_{\mathrm{C}}
$$

在对称情况下为

$$
Q=3 U_{\mathrm{p}} I_{\mathrm{p}} \sin \varphi, \quad Q=\sqrt{3} U_{l} I_{l} \sin \varphi
$$

式中的 $\varphi$ 角为各相负载的阻抗角。

三相电路的视在功率与有功功率和无功功率的关系为

$$
S=\sqrt{P^{2}+Q^{2}}
$$

在对称情况下为

$$
S=3 U_{\mathrm{p}} I_{\mathrm{p}}, \quad S=\sqrt{3} U_{l} I_{l}
$$

三相电路的功率因数定义为有功功率与视在功率之比, 即

$$
\lambda=\cos \varphi=\frac{P}{S}
$$

式中的 $\varphi$ 角只有在对称情况才有实际意义,为各相负载的阻抗角。

三相电源或三相负载的瞬时功率为各相瞬时功率之和, 即

$$
p=p_{\mathrm{A}}+p_{\mathrm{B}}+p_{\mathrm{C}}
$$

在对称情况下, 三相电路的瞬时功率不随时间变化而为一定值, 此值为三相电路的有功功率 $P$, 即

$$
P=\sqrt{3} U_{l} I_{l} \cos \varphi=P
$$

此现象称为瞬时功率平衡, 可使三相旋转电机得到恒定转矩, 使其运行平稳。 



【例 1.3-13】在图 1.3-22 的对称三相电路中, 已知 $U_{A B}$ $=38010^{\circ} 、 \mathrm{~V}_{\text {。 }}$ 求相量 $U_{\mathrm{BC}} 、 U_{\mathrm{CA}} 、 U_{\mathrm{AN}^{\prime}} 、 U_{\mathrm{BN}^{\prime}} 、 U_{\mathrm{CN}^{\prime}} 、 I_{\mathrm{A}} 、 i_{\mathrm{B}} 、 I_{\mathrm{C}} 、 i_{\mathrm{AB}} 、$ $i_{\mathrm{BC}}$ 和 $i_{\mathrm{CA}}$, 并求电路中的有功功率 $P$ 、无功功率 $Q$ 、视在功率 $S$ 和功率因数 $\lambda$ 。

解: $\dot{U}_{\mathrm{BC}}=380 \angle-120^{\circ} \mathrm{V}$

$$
\begin{aligned}
& U_{\mathrm{CA}}=380 \angle 120^{\circ} \mathrm{V} \\
& U_{\mathrm{AN}}=\frac{U_{\mathrm{AB}}}{\sqrt{3}} \angle-30^{\circ}=\frac{380}{\sqrt{3}} \angle 0^{\circ}-30^{\circ}=220 \angle-30^{\circ} \mathrm{V}
\end{aligned}
$$

$U_{\mathrm{BN}^{\prime}}=\frac{U_{\mathrm{BC}}}{\sqrt{3}} \angle-30^{\circ}=\frac{380}{\sqrt{3}} \angle-120^{\circ}-30^{\circ}=220 \angle-150^{\circ} \mathrm{V}$

$U_{\mathrm{CN}^{\prime}}=U_{\mathrm{BN}^{\prime}} \angle-120^{\circ}=220 \angle-150^{\circ}-120^{\circ}=220 \angle-270^{\circ}=220 \angle 90^{\circ} \mathrm{V}$

$\dot{I}_{\mathrm{A}}=\frac{\dot{U}_{\mathrm{AN}^{\prime}}}{3+\mathrm{j} 4}=\frac{220 \angle-30^{\circ}}{5 \angle 53 \cdot 1^{\circ}}=44 \angle-83.1^{\circ} \mathrm{A}$

$\dot{I}_{\mathrm{B}}=\dot{I}_{\mathrm{A}} \angle-120^{\circ}=44 \angle-83.1^{\circ}-120^{\circ}=44 \angle-203.1^{\circ}=44 \angle 156.9^{\circ} \mathrm{A}$

$\dot{I}_{\mathrm{C}}=\dot{I}_{\mathrm{A}} \angle 120^{\circ}=44 \angle-83.1^{\circ}+120^{\circ}=44 \angle 36.9^{\circ} \mathrm{A}$

$i_{\mathrm{AB}}=\frac{\dot{I}_{\mathrm{A}}}{\sqrt{3}} \angle 30^{\circ}=\frac{44}{\sqrt{3}} \angle-83.1^{\circ}+30^{\circ}=25.4 \angle-53.1^{\circ} \mathrm{A}$

$\dot{I}_{\mathrm{BC}}=\dot{I}_{\mathrm{AB}} \angle-120^{\circ}=25.4 \angle-53.1^{\circ}-120^{\circ}=25.4 \angle-173.1^{\circ} \mathrm{A}$

$\dot{I}_{\mathrm{CA}}=\dot{I}_{\mathrm{AB}} \angle 120^{\circ}=25.4 \angle-53.1^{\circ}+120^{\circ}=25.4 \angle 66.9^{\circ} \mathrm{A}$

$P=\sqrt{3} U_{l} I_{l} \cos \varphi=\sqrt{3} \times 380 \times 44 \cos 53.1^{\circ}=17.39 \mathrm{~kW}$

$Q=\sqrt{3} U_{l} I_{l} \sin \varphi=\sqrt{3} \times 380 \times 44 \sin 53.1^{\circ}=23.16 \mathrm{kVar}$

$S=\sqrt{3} U_{l} I_{l}=\sqrt{3} \times 380 \times 44=28.96 \mathrm{kVA}$.

$\lambda=\cos \varphi=\cos 53.1^{\circ}=0.6$

\subsection{7 对称三相电路分析的相量方法}

\section{1. 简化为一相计算法}

原理: 因为在对称电路中, 各处的电压和电流都存在着对称关系, 所以只计算出一相电压 或电流响应后,其他两相的响应皆可按照对称关系得出。

在图 1.3-23 三相四线制电路中, 负载 $Z$ 、各线路阻抗 $Z_{1}$ 和中线复阻抗 $Z_{N}$ 均为已知, 求在给 定电源相电压相量下的各线电流相量。

根据节点电压法有

因为

$$
U_{\mathrm{NN}}=\frac{\left(U_{\mathrm{AN}}+U_{\mathrm{BN}}+U_{\mathrm{CN}}\right) \frac{1}{Z+Z_{l}}}{\frac{3}{Z+Z_{l}}+\frac{1}{Z_{\mathrm{N}}}}
$$

$$
U_{\mathrm{AN}}+U_{\mathrm{BN}}+U_{\mathrm{CN}}=0
$$

所以

$$
U_{N^{\prime} N}=0
$$



$$
\dot{I}_{\mathrm{A}}=\frac{U_{\mathrm{AN}}}{Z+Z_{l}}
$$

根据对称关系可得



$$
\dot{I}_{\mathrm{B}}=i_{\mathrm{A}} \angle-120^{\circ}, \quad \dot{I}_{\mathrm{C}}=i_{\mathrm{A}} \angle 120^{\circ}
$$

从以上分析可以看出, 对 $\mathrm{Y}_{0}-\mathrm{Y}_{0}$ 系统的三相电路, 根据三相电路的特点可以只计算图 1.3-24 所示的一相电路, 用此电路求得 $\mathrm{A}$ 线电流后, 其他两线电流的响应可由对称关系得出。 此外, 还可以用此电路计算出负载的相电压和线路阻抗上的电压以及一相功率等响应。这就 是简化为一相的计算法。

应用:对其他 4 种三相三线制电路,使用简化为一相计算法可遵循以下原则。

(1)在对称 $Y-Y$ 系统中, 因为电源的中点与负载的中点等电位, 可以用短路线相连后变成 $\mathrm{Y}_{0}-\mathrm{Y}_{0}$ 系统。

(2)在对称 $Y-\Delta$ 系统中, 将 $\Delta$ 接对称负载, 等效变换成 $Y$ 接对称负载, 构成 $Y-Y$ 系统后 再形成 $Y_{0}-Y_{0}$ 系统。

(3) 在对称 $\Delta-Y$ 系统中, 将 $\Delta$ 接对称电源, 利用对称关系变成对称 $Y$ 接电源, 构成 $Y-Y$ 系统后再形成 $Y_{0}-Y_{0}$ 系统。

(4) 在对称 $\Delta-\Delta$ 系统中, 将 $\Delta$ 接对称电源, 利用对称关系变成对称 $Y$ 接电源, 将 $\Delta$ 接对称 负载等效变换成 $Y$ 接对称负载,构成 $Y-Y$ 系统后再形成 $Y_{0}-Y_{0}$ 系统。

(5)对无线路阻抗的对称三相电路, 可直接利用负载与电源电压关系, 直接计算出一相响应 后,利用对称关系求得其他两相所需响应。

\section{2. 对称三相电路解题步骤}

(1)将已知的对称三相电路变成等效的 $\mathrm{Y}_{0}-\mathrm{Y}_{0}$ 系统;

(2)画出一相计算电路图;

(3)由已知条件确定一个参考相量;

(4)计算出一相所需的电路响应;

(5)根据对称关系计算其他所需的电路响应。

【例 1.3-14】电路如图 1.3-25(a), 电源为对称三相电源, 其线电压为 $380 \mathrm{~V}$, 对称三角 形连接的负载每相复阻抗 $Z_{\Delta}=45+\mathrm{j} 30 \Omega$, 线路复阻抗 $Z_{I}=1+\mathrm{j} 2 \Omega$ 。求负载端各线电压和各 相电流的有效值相量及负载中三相总有功功率。

解:将电源设成为星接,将 $\Delta$ 形负载复阻抗 $Z_{\Delta}$ 利用 $\Delta \Rightarrow \mathrm{Y}$ 关系变为等效的 $\mathrm{Y}$ 形负载 $Z_{\mathrm{Y}}$, 即

$$
Z_{Y}=\frac{1}{3} Z_{\Delta}=\frac{1}{3}(45+\mathrm{j} 30)=15+\mathrm{j} 10=18 \angle 33.7^{\circ} \Omega
$$

将电源中点与负载中点相连得图 1.3-25(b), 可得图 1.3-26一相计算电路。由已知条件得电 源相电压 $U_{A N}$ 为 $220 \mathrm{~V}$, 并以此电压的相量 $U_{A N}$ 为参考相量, 由此可得 $\mathrm{A}$ 线电流相量

$$
\dot{I}_{\mathrm{A}}=\frac{\dot{U}_{\mathrm{AN}}}{Z_{l}+Z_{\mathrm{Y}}}=\frac{220 \angle 0^{\circ}}{1+\mathrm{j} 2+15+\mathrm{j} 10}=\frac{220 \angle 0^{\circ}}{16+\mathrm{j} 12}=\frac{220 \angle 0^{\circ}}{20 \angle 36.9^{\circ}}=11 \angle-36.9^{\circ} \mathrm{A}
$$





等效 $\mathrm{Y}$ 形负载的 $\mathrm{A}$ 相电压相量为

$$
\begin{aligned}
\dot{U}_{\Lambda^{\prime} N^{\prime}} & =I_{A} Z_{\mathrm{Y}}=11 \angle-36.9^{\circ} \times 18 \angle 33.7^{\circ} \\
& =198 \angle-3.2^{\circ} \mathrm{V}
\end{aligned}
$$

根据对称关系得

$$
\begin{aligned}
& U_{\mathrm{B}^{\prime} \mathrm{N}^{\prime}}=U_{\mathrm{A}^{\prime} \mathrm{N}^{\prime}} \angle-120^{\circ}=198 \angle-3.2^{\circ}-120^{\circ}=198 \angle-123.2^{\circ} \mathrm{V} \\
& U_{\mathrm{C}^{\prime} \mathrm{N}^{\prime}}=U_{\mathrm{A}^{\prime} \mathrm{N}^{\prime}} \angle 120^{\circ}=198 \angle-3.2^{\circ}+120^{\circ}=198 \angle 116.8^{\circ} \mathrm{V}
\end{aligned}
$$

利用对称星形连接相、线电压的特点, 可得 $\mathrm{AB}$ 线电压相量为

$$
U_{A^{\prime} B^{\prime}}=\sqrt{3} U_{A^{\prime} N^{\prime}} \angle 30^{\circ}=\sqrt{3} \times 198 \angle-3.2^{\circ}+30^{\circ}=343 \angle 26.8^{\circ} \mathrm{V}
$$

根据对称关系得

$$
\begin{aligned}
& U_{\mathrm{B}^{\prime} \mathrm{C}^{\prime}}=U_{\mathrm{A}^{\prime} \mathrm{B}^{\prime}} \angle-120^{\circ}=343 \angle 26.8^{\circ}-120^{\circ}=343 \angle-93.2^{\circ} \mathrm{V} \\
& \dot{U}_{\mathrm{C}^{\prime} \mathrm{A}^{\prime}}=\dot{U}_{\mathrm{A}^{\prime} \mathrm{B}^{\prime}} \angle 120^{\circ}=343 \angle 26.8^{\circ}+120^{\circ}=343 \angle 146.8^{\circ} \mathrm{V}
\end{aligned}
$$

原电路中 $\mathrm{AB}$ 相负载中的电流相量为

$$
\dot{I}_{\Lambda^{\prime} B^{\prime}}=\frac{U_{A^{\prime} B^{\prime}}}{Z_{\Delta}}=\frac{343 \angle 26.8^{\circ}}{45+j 30}=\frac{343 \angle 26.8^{\circ}}{54 \angle 33.7^{\circ}}=6.35 \angle-6.9^{\circ} \mathrm{A}
$$

\section{根据对称关系得}

$$
\begin{aligned}
& \dot{I}_{\mathrm{B}^{\prime} \mathrm{C}^{\prime}}=\dot{I}_{\mathrm{A}^{\prime} \mathrm{B}^{\prime}} \angle-120^{\circ}=6.35 \angle-6.9^{\circ}-120^{\circ}=6.35 \angle-126.9^{\circ} \mathrm{A} \\
& \dot{I}_{\mathrm{C}^{\prime} \mathrm{A}^{\prime}}=\dot{I}_{\mathrm{A}^{\prime} \mathrm{B}^{\prime}} \angle 120^{\circ}=6.35 \angle-6.9^{\circ}+120^{\circ}=6.35 \angle 113.1^{\circ} \mathrm{A}
\end{aligned}
$$

负载的三相总有功功率为

$$
P=3 U_{\mathrm{p}} I_{\mathrm{p}} \cos \varphi=3 \times 343 \times 6.35 \times \cos 33.7^{\circ}=5.44 \mathrm{~kW}
$$

$$
\text { 或 } \quad P=\sqrt{3} U_{l} I_{l} \cos \varphi=\sqrt{3} \times 343 \times 11 \times \cos 33.7^{\circ}=5.44 \mathrm{~kW}
$$

【例 1.3-15】电路如图 1.3-27, 已知电源相电压为 $220 \mathrm{~V}, Z_{l}=1+\mathrm{j} 2 \Omega, Z_{1}=8+\mathrm{j} 6 \Omega, Z_{2}$ $=24+\mathrm{j} 18 \Omega, Z_{\mathrm{N}}=2+\mathrm{j} 1 \Omega$ 。求各线电流相量和电源供出的功率。

解: 将 $Z_{2}$ 的 $\Delta \Rightarrow Y$ 后, 画出图 1.3-28 的一相计算电路。选 A 相电源电压为参考相量, 可得 $A$ 线电流相量为




$$
=\frac{220 \angle 0^{\circ}}{1+\mathrm{j} 2+\frac{8+\mathrm{j} 6}{2}}=\frac{220 \angle 0^{\circ}}{5+\mathrm{j} 5}=\frac{220 \angle 0^{\circ}}{7.07 \angle 45^{\circ}}=31.1 \angle-45^{\circ} \mathrm{A}
$$





根据对称关系得

$$
\begin{aligned}
& \dot{I}_{\mathrm{B}}=\dot{I}_{\mathrm{A}} \angle-120^{\circ}=31.1 \angle-45^{\circ}-120^{\circ}=31.1 \angle-165^{\circ} \mathrm{A} \\
& \dot{I}_{\mathrm{C}}=\dot{I}_{\mathrm{A}} \angle 120^{\circ}=31.1 \angle-45^{\circ}+120^{\circ}=31.1 \angle 75^{\circ} \mathrm{A}
\end{aligned}
$$

电源供出的功率为

$$
P=\sqrt{3} U_{l} I_{l} \cos \varphi=\sqrt{3} \times 220 \sqrt{3} \times 31.1 \times \cos 45^{\circ}=14.5 \mathrm{~kW}
$$

【例 1.3-16】对称三相电路如图 1.3-29。电源线电压为 $380 \mathrm{~V}$, 负载阻抗 $Z=60+j 80 \Omega$ 。求负载中各相电流相量和各 线电流相量。

解: 以 $\mathrm{AB}$ 线电源电压为参考相量, 可得 $\mathrm{AB}$ 相负载电流相量 为

$$
\dot{I}_{\mathrm{AB}}=\frac{U_{\mathrm{AB}}}{Z}=\frac{380 \angle 0^{\circ}}{60+\mathrm{j} 80}=\frac{380 \angle 0^{\circ}}{100 \angle 53.1^{\circ}}=3.8 \angle-53.1^{\circ} \mathrm{A}
$$



根据对称关系得

$$
\begin{aligned}
& \dot{I}_{\mathrm{BC}}=\dot{I}_{\mathrm{AB}} \angle-120^{\circ}=3.8 \angle-53.1^{\circ}-120^{\circ}=3.8 \angle-173.1^{\circ} \mathrm{A} \\
& \dot{I}_{\mathrm{CA}}=\dot{I}_{\mathrm{AB}} \angle 120^{\circ}=3.8 \angle-53.1^{\circ}+120^{\circ}=3.8 \angle 66.9^{\circ} \mathrm{A}
\end{aligned}
$$

根据 $\Delta$ 形线电流和相电流的关系得

$$
i_{\mathrm{A}}=\sqrt{3} i_{\mathrm{AB}} \angle-30^{\circ}=3.8 \sqrt{3} \angle-53.1^{\circ}-30^{\circ}=6.58 \angle-83.1^{\circ} \mathrm{A}
$$

根据对称关系得

$$
\begin{aligned}
& \dot{I}_{\mathrm{B}}=\dot{I}_{\mathrm{A}} \angle-120^{\circ}=6.58 \angle-83.1^{\circ}-120^{\circ}=6.58 \angle-203.1^{\circ}=6.58 \angle 156.9^{\circ} \mathrm{A} \\
& \dot{I}_{\mathrm{C}}=\dot{I}_{\mathrm{A}} \angle 120^{\circ}=6.58 \angle-83.1^{\circ}+120^{\circ}=6.58 \angle 36.9^{\circ} \mathrm{A}
\end{aligned}
$$

\subsection{8 不对称三相电路的概念}

\section{1. 不对称三相电路}

在三相电路中, 若三相电源不对称, 或三相负载不对称, 或 3 条传输线上的复阻抗不相等, 都称为不对称三相电路。

在不对称三相电路中, 各相电流、线电流、相电压和线电压一般不存在对称关系。较常见 的不对称三相电路是电源对称, 3 条传输线上的复阻抗相等, 只有负载不对称。在这种情况 下,电源端的相、线电压仍保持对称关系, 并且满足对称三相电源的特点。

\section{2. 中点位移概念}

在图 1. 3-30 (a) 不对称 $\mathrm{Y}_{0}-\mathrm{Y}_{0}$ 系统中, 假设星形连接的电源对称; 3 条传输线上的复阻抗 $Z_{l}$ 相等; 各相复负载分别为 $Z_{\mathrm{A}} 、 Z_{\mathrm{B}}$ 和 $Z_{\mathrm{C}}$, 中线阻抗为 $Z_{\mathrm{N}}$, 欲求各线电流 $I_{\mathrm{A}} 、 I_{\mathrm{B}} 、 I_{\mathrm{C}}$ 和中线电流 $i_{\mathrm{N}}$ 。由节点电压法可得中线电压为

$$
U_{\mathrm{N}^{\prime} \mathrm{N}}=\frac{\frac{\dot{U}_{\mathrm{AN}^{\prime}}}{Z_{\mathrm{A}}+Z_{l}}+\frac{U_{\mathrm{BN}^{\prime}}}{Z_{\mathrm{B}}+Z_{l}}+\frac{\hat{U}_{\mathrm{CN}^{\prime}}}{Z_{\mathrm{C}}+Z_{l}}}{\frac{1}{Z_{\mathrm{A}}+Z_{l}}+\frac{1}{Z_{\mathrm{B}}+Z_{l}}+\frac{1}{Z_{\mathrm{C}}+Z_{l}}+\frac{1}{Z_{\mathrm{N}}}}
$$






一般情况下 $U_{N^{\prime} N} \neq 0$ 。

求得中线电压后可得各线电流为

$$
i_{\mathrm{A}}=\left(\frac{U_{\mathrm{AN}}-U_{\mathrm{N}^{\prime} \mathrm{N}}}{Z_{\mathrm{A}}+Z_{l}}\right), \dot{I}_{\mathrm{B}}=\left(\frac{U_{\mathrm{BN}}-U_{\mathrm{N}^{\prime} \mathrm{N}}}{Z_{\mathrm{B}}+Z_{l}}\right), \dot{I}_{\mathrm{C}}=\left(\frac{U_{\mathrm{CN}}-U_{\mathrm{N}^{\prime} \mathrm{N}}}{Z_{\mathrm{C}}+Z_{l}}\right)
$$

根据 KCL 可求得中线电流

$$
i_{\mathrm{N}}=\dot{I}_{\mathrm{A}}+\dot{I}_{\mathrm{B}}+\dot{I}_{\mathrm{C}} \neq 0
$$


引起中点位移的原因是负载不对称,负载不对称的程度越大中点位移越大。从相量图可 以看出,中点位移较大时的后果是, 某相负载电压过高导致该相负载设备损坏; 某相负载电压 过低使该相负载不能正常工作。在 $Y_{0}-Y_{0}$ 系统中, 由于中线阻抗很小, 中点位移较小, 即使负 载不对称, 仍然可保证各相负载电压接近电源的相电压, 只是有中线电流存在, 但各相负载仍 能够正常工作。如果断开中线, 形成 $Y-Y$ 系统的中点位移现象, 就会造成较大的不良后果。 因此, 在低压供电的 $Y_{0}-Y_{0}$ 系统中, 中线不允许安装开关和保险丝, 并且中线应该使用强度较 大的导线以防止中线断路。

\section{3. 不对称三相电路的计算}

就一般不对称三相电路的计算而言, 应按复杂交流电路对待, 选用系统分析方法或电路定 理进行分析计算。对 $\mathrm{Y}-\mathrm{Y}$ 和 $\mathrm{Y}_{0}-\mathrm{Y}_{0}$ 系统, 常选用节点电压法。对其他有三角形连接的电路 可视电路具体情况,用等效变换或回路电流法等方法进行分析计算。

有些不对称三相电路可以用较简便的方法计算。例如, 对无线路阻抗的 $Y_{0}-Y_{0}$ 系统和 $\Delta-\Delta$ 系统, 相当于各相负载直接与各相电源相接, 可以直接用欧姆定律、KCL 和 KVL 进行分 析计算。

总之, 对于不对称三相电路的计算, 应该根据电路的具体电路结构和参数的特点, 选择较 简便的方法进行分析计算。

【例 1.3-17】图 1.3-31 (a) 为相序指示器电路, 可以用来确定 3 条端线的相序。它是用 1 个电容和 2 个灯泡连成 $\mathrm{Y}$ 接电路, 并且使电容的容抗等于灯泡的电阻, 即 $1 / \omega C=R$ 。已知线 电压对称,求 2 个灯泡上的电压, 并以其亮度判断相序。






解:因为线电压对称, 所以图 1.3-31(a) 可看成图 1.3-31(b) 的对称电源向不对称负载供 电的 $\mathrm{Y}-\mathrm{Y}$ 系统不对称三相电路。设接电容者为 $\mathrm{A}$ 相, 且以 $U_{\mathrm{AN}}$ 为参考相量, 用节点电压法 有

$$
\begin{aligned}
U_{\mathrm{NN}} & =\frac{j \omega C U_{\mathrm{AN}}+\frac{1}{R} \dot{U}_{\mathrm{BN}}+\frac{1}{R} U_{\mathrm{CN}}}{\mathrm{j} \omega C+\frac{1}{R}+\frac{1}{R}}=\frac{\mathrm{j} U_{\mathrm{AN}} \angle 0^{\circ}+U_{\mathrm{AN}} \angle-120^{\circ}+U_{\mathrm{AN}} \angle 120^{\circ}}{\mathrm{j}+2} \\
& =(-0.2+\mathrm{j} 0.6) U_{\mathrm{AN}}
\end{aligned}
$$

$B$ 相灯泡的电压为

$$
\begin{aligned}
U_{\mathrm{BN}^{\prime}} & =U_{\mathrm{BN}}-U_{\mathrm{N}^{\prime} \mathrm{N}}=U_{\mathrm{AN}} \angle-120^{\circ}-(-0.2+\mathrm{j} 0.6) U_{\mathrm{AN}} \\
& =(-0.3-\mathrm{j} 1.466) U_{\mathrm{AN}}=1.496 \angle 258.4^{\circ} U_{\mathrm{AN}}
\end{aligned}
$$

$\mathrm{C}$ 相灯泡的电压为

$$
\begin{aligned}
U_{\mathrm{CN}^{\prime}} & =U_{\mathrm{CN}}-U_{\mathrm{N}^{\prime} \mathrm{N}}=U_{\mathrm{AN}} \angle 120^{\circ}-(-0.2+\mathrm{j} 0.6) U_{\mathrm{AN}} \\
& =(-0.3+\mathrm{j} 0.266) U_{\mathrm{AN}}=0.401 \angle 138.4^{\circ} U_{\mathrm{AN}} .
\end{aligned}
$$

即得 $B 、 C$ 两相电压的有效值分别为

$$
U_{\mathrm{BN}^{\prime}}=1.496 U_{\mathrm{AN}}, \quad U_{\mathrm{CN}^{\prime}}=0.401 U_{\mathrm{AN}}
$$

显然, $U_{\mathrm{BN}}>U_{\mathrm{CN}}$, 即两灯中较亮的为 $\mathrm{B}$ 相, 较暗的为 $\mathrm{C}$ 相。由此可以确定出各端线的相 序为: 接电容线 $\rightarrow$ 灯较亮线 $\rightarrow$ 灯较暗线。

\section{4 非正弦周期电流电路}

\subsection{1 非正弦周期量的傅里叶级数分解方法}

\section{1. 周期量的傅里叶级数分解}

一个周期函数 $f(t)$ 若满足狄里克雷收玫条件, 即在有限的时间间隔中, 仅有有限个极值 点和有限个第一类不连续点, 则可展开成收玫的傅里叶级数 (傅氏级数)。 



对图 1. 4-1 的非正弦函数 $f(t)$, 其周期为 $T$, 展开成傅氏级数 为

$$
\begin{aligned}
f(t)= & a_{0}+\left(a_{1} \cos \omega t+b_{1} \sin \omega t\right)+\left(a_{2} \cos 2 \omega t+b_{2} \sin 2 \omega t\right) \\
& +\cdots+\left(a_{k} \cos k \omega t+b_{k} \sin k \omega t\right)+\cdots \\
= & \left.a_{0}+\sum_{k=1}^{\infty}\left[a_{k} \cos k \omega t+b_{k} \sin k \omega t\right)\right]
\end{aligned}
$$

式中: $\omega=2 \pi / T, a_{0} 、 a_{k}$ 和 $b_{k}$ 为傅氏系数, 可按以下各式求得

$$
\begin{aligned}
& a_{0}=\frac{1}{T} \int_{0}^{T} f(t) \mathrm{d} t=\frac{1}{2 \pi} \int_{0}^{2 \pi} f(t) \mathrm{d}(\omega t) \\
& a_{k}=\frac{2}{T} \int_{0}^{T} f(t) \cos (k \omega t) \mathrm{d} t=\frac{1}{\pi} \int_{0}^{2 \pi} f(t) \cos (k \omega t) \mathrm{d}(\omega t) \\
& b_{k}=\frac{2}{T} \int_{0}^{T} f(t) \sin (k \omega t) \mathrm{d} t=\frac{1}{\pi} \int_{0}^{2 \pi} f(t) \sin (k \omega t) \mathrm{d}(\omega t)
\end{aligned}
$$

傅氏级数展开式的另一种形式为

$$
\begin{aligned}
f(t) & =A_{0}+A_{1 \mathrm{~m}} \sin \left(\omega t+\psi_{1}\right)+A_{2 \mathrm{~m}} \sin \left(2 \omega t+\psi_{2}\right)+\cdots+A_{k \mathrm{~m}} \sin \left(k \omega t+\psi_{k}\right)+\cdots \\
& =A_{0}+\sum_{k=1}^{\infty} A_{k \mathrm{~m}} \sin \left(k \omega t+\psi_{k}\right)
\end{aligned}
$$

式中, $A_{0}=a_{0}, A_{k \mathrm{~m}}=\sqrt{a_{k}^{2}+b_{k}^{2}}, \psi_{k}=\arctan \frac{a_{k}}{b_{k}}$ 。

\section{2. 非正弦周期电压、电流和非正弦电路}

在工程实际中, 会遇到许多非正弦电压、电流信号。在正弦激励下的非线性电路中会出现 非正弦电压、电流响应。交流发电机发出的电压严格地讲也不是理想的正弦。在图 1.4-2 中 给出了几种常见的非正弦周期电压和电流的波形。


工程中的非正弦周期电压、电流都满足狄里克雷收玫条件, 故可用傅里叶级数进行分解。 在电路理论中常用后一种傅氏级数展开式。非正弦周期电压 $u(t)$ 的傅氏级数展开式为

$$
\begin{aligned}
u(t) & =U_{0}+U_{1 \mathrm{~m}} \sin \left(\omega_{1} t+\psi_{u 1}\right)+U_{2 \mathrm{~m}} \sin \left(2 \omega_{1} t+\psi_{u 2}\right)+\cdots+U_{k \mathrm{~m}} \sin \left(k \omega_{1} t+\psi_{u k}\right)+\cdots \\
& =U_{0}+\sum_{k=1}^{\infty} U_{k \mathrm{~m}} \sin \left(k \omega_{1} t+\psi_{u k}\right)
\end{aligned}
$$

非正弦周期电流 $i(t)$ 的傅氏级数展开式为

$$
\begin{aligned}
i(t) & =I_{0}+I_{1 \mathrm{~m}} \sin \left(\omega_{1} t+\psi_{i 1}\right)+I_{2 \mathrm{~m}} \sin \left(2 \omega_{1} t+\psi_{i 2}\right)+\cdots+I_{k \mathrm{~m}} \sin \left(k \omega_{1} t+\psi_{i k}\right)+\cdots \\
& =I_{0}+\sum_{k=1}^{\infty} I_{k \mathrm{~m}} \sin \left(k \omega_{1} t+\psi_{i k}\right)
\end{aligned}
$$

由此看出, 一个非正弦周期电压、电流可以分解成一个直流分量和无限个频率与原非正弦 周期电压、电流的频率 $\omega_{1}$ 成整数倍的正弦电压、电流。其中: 和原非正弦周期电压、电流的频 率 $\omega_{1}$ 相同的电压、电流称为基波分量; 当 $k=2 、 k=3 、 k=4 \cdots \cdots$ 时,分别称为 2 次谐波、3 次 谐波、4 次谐波 …...等高次谐波。 $k$ 为奇数 $(k=1,3,5, \cdots)$ 时的谐波分量称为奇次谐波; $k$ 为偶 数 $(k=2,4,6, \cdots)$ 时的谐波分量称为偶次谐波。

在工程实际中,出现非正弦周期电压、电流的电路可有两种情况:一种情况为非正弦激励 下的线性电路; 另一种情况为正弦激励下的非线性电路。在电路理论中对非正弦电路分析计 算的重点在于第一种情况。

\section{4 .2 非正弦周期量的有效值、平均值和平均功率的定义和计算方法}

\section{1. 有效值、平均值和平均功率的定义}

有效值的定义为:直流分量的平方加上各次谐波平方之和的平方根, 即非正弦周期电压、 电流的有效值分别为

$$
\begin{aligned}
& U=\sqrt{U_{0}^{2}+\sum_{k=1}^{\infty} U_{k}^{2}}=\sqrt{U_{0}^{2}+U_{1}^{2}+U_{2}^{2}+U_{3}^{2}+\cdots} \\
& I=\sqrt{I_{0}^{2}+\sum_{k=1}^{\infty} I_{k}^{2}}=\sqrt{I_{0}^{2}+I_{1}^{2}+I_{2}^{2}+I_{3}^{2}+\cdots}
\end{aligned}
$$

平均值的定义为: 非正弦量的绝对值的平均值, 即非正弦周期电压、电流的平均值分别为

$$
U_{\text {平均 }}=\frac{1}{T} \int_{0}^{T}|u(t)| \mathrm{d} t, I_{\text {平均 }}=\frac{1}{T} \int_{0}^{T}|i(t)| \mathrm{d} t
$$

平均功率的定义为: 直流分量的功率与各次谐波的平均功率的代数和, 即

$$
\begin{aligned}
P & =P_{0}+\sum_{k=1}^{\infty} P_{k}=P_{0}+P_{1}+P_{2}+\cdots+P_{k}+\cdots \\
& =U_{0} I_{0}+U_{1} I_{1} \cos \varphi_{1}+U_{2} I_{2} \cos \varphi_{2}+\cdots+U_{k} I_{k} \cos \varphi_{k}+\cdots
\end{aligned}
$$

式中 $\varphi_{k}$ 为相同谐波次数的电压与电流的相位差, 即 $\varphi_{k}=\psi_{u k}-\psi_{i k}$ 。

\section{2. 有效值、平均值和平均功率的计算方法}

在非正弦电路中,计算有效值、平均值和平均功率时应注意以下几点。

(1)电压、电流的有效值应该为直流分量的平方与各次谐波的平方之和的开平方,而不是直 流分量与各次谐波的有效值之和, 即在非正弦电路中

$$
\begin{aligned}
& I \neq I_{0}+I_{1}+I_{2}+\cdots+I_{k}+\cdots \\
& U \neq U_{0}+U_{1}+U_{2}+\cdots+U_{k}+\cdots
\end{aligned}
$$

(2)工程上非正弦周期电压、电流的平均值与数学中的平均值不同, 在工程上是取绝对值的 平均值。

(3)在非正弦电路中, 不同谐波次数的电压、电流不构成平均功率。

(4)非正弦电流流过某电阻时的平均功率为

$$
P=I_{0}^{2} R+I_{1}^{2} R+I_{2}^{2} R+\cdots+I_{k}^{2} R+\cdots=I^{2} R
$$

【例 1. 4-1】 某非正弦电流 $i(t)=3+6 \sin \left(\omega t+30^{\circ}\right)+2 \sin 3 \omega t \mathrm{~A}$, 求该电流的有效值。

解: $I=\sqrt{I_{0}^{2}+I_{1}^{2}+I_{3}^{2}}=\sqrt{3^{2}+\left(\frac{6}{\sqrt{2}}\right)^{2}+\left(\frac{2}{\sqrt{2}}\right)^{2}}=5.39 \mathrm{~A}$

【例 1.4-2】 在图 1.4-3 非含源一端口 $N_{0}$ 的端口处加非正弦电压 $u(t)=50$ $N_{0} \begin{gathered}i(t) \\ i \\ u(t) \\ 0\end{gathered}$


$+40 \sqrt{2} \sin \left(\omega t+60^{\circ}\right)+10 \sqrt{2} \sin \left(5 \omega t-60^{\circ}\right) \mathrm{V}$, 得非正弦电流 $i(t)=10+$ $5 \sqrt{2} \sin \left(\omega t-30^{\circ}\right)+2 \sqrt{2} \sin \left(3 \omega t-60^{\circ}\right) \mathrm{A}$ 。求该电路的平均功率。

解: 因为不同次数谐波的电压和电流不构成功率, 则该电路的平均功率为

$$
P=P_{0}+P_{1}=U_{0} I_{0}+U_{i} I_{1} \cos \left(\varphi_{u I}-\varphi_{i 1}\right)
$$

$$
=50 \times 10+40 \times 5 \times \cos \left(60^{\circ}-\left(-30^{\circ}\right)\right)=500 \mathrm{~W}
$$

\subsection{3 非正弦周期电路的分析方法}

\section{1. 分析计算原理}

在工程中,对在非正弦电压、电流源激励下的线性电路进行分析计算的理论基础是傅氏级 数分解和叠加定理。即利用傅氏级数将非正弦激励源分解成傅氏级数, 并根据误差要求取其 有限项后, 分别计算电路在直流激励下和各次谐波单独激励下的所需响应。然后将直流激励 下的电压、电流响应和在各次谐波单独激励下所需电压、电流响应的瞬时值进行叠加, 并根据 定义求所需的有效值和平均功率。

\section{2. 解题步骤}

(1)用傅氏级数分解给定的非正弦激励。由于傅氏级数收玫较快,在工程实际中常取展开 式中的前 $3 \sim 5$ 项即可满足误差要求。常用的非正弦波形傅氏级数展开式都可从手册中查 到,不必进行积分运算。在电路理论中,对非正弦激励也常以展开式的形式给出。

(2)画出直流激励下的电路图,并求其所需响应。此时电感相当于短路, 电容相当于开路。

(3)按照激励源中存在的各次谐波的数目,分别画出各次谐波单独激励下的各正弦电路图, 同时在各分电路图中计算所需响应。此时对不同次数的正弦激励下的感抗和容抗应使用谐波 电抗,其计算式分别为

$$
X_{L}=k \omega L, X_{C}=\frac{1}{k \omega C}
$$

(4)将直流激励下求得的电压、电流所需响应和在各次谐波单独激励下求得的所需电压、电 流响应的瞬时值进行叠加,得所需电压、电流响应的瞬时值表达式。

(5)根据定义求所需响应的有效值和平均功率。

\section{3. 注意事项}

(1)当非正弦激励以展开式的形式给出时,第一步骤可以从略。

(2)在直流激励下的电路中, 电感相当于短路; 电容相当于开路。但电感中有电流; 电容上 有电压。

(3)在各次谐波激励下的正弦电路中,遇有 $L 、 C$ 串联或并联环节,在计算电路之前最好先 用谐波阻抗 $k \omega L=\frac{1}{k \omega C}$ 判断该环节是否谐振。如果发生谐振现象, $L 、 C$ 串联环节相当于短路; $L 、 C$ 并联环节相当于开路。

(4)在各次谐波激励下的正弦电路中, $L 、 C$ 串联环节谐振时,此环节相当于短路,但该处有 电流, 并用此电流求电感或电容上的电压; $L 、 C$ 并联环节谐振时, 此环节相当于开路, 但该处有 电压, 并用此电压求电感或电容中的电流。

(5)电路中的非正弦电压、电流响应只能是直流分量和各次谐波的瞬时值相叠加,切不可用 有效值叠加, 即

$$
U \neq U_{0}+U_{1}+U_{3}+\cdots+U_{k}+\cdots, I \neq I_{0}+I_{1}+I_{3}+\cdots+I_{k}+\cdots
$$

也不能用直流分量和各次谐波电路中所计算出的电压、电流相量叠加, 即

$$
U \neq U_{0}+U_{1}+U_{3}+\cdots+U_{k}+\cdots, i \neq I_{0}+i_{1}+\dot{I}_{3}+\cdots+\dot{I}_{k}+\cdots
$$

【例 1.4-3】 在图 1.4-4(a) 电路中, 已知: $u_{\mathrm{S}}(t)=10+141.4 \sin \omega t+70.7 \sin \left(3 \omega t+30^{\circ}\right)$ $V, \frac{1}{\omega C}=15 \Omega, \omega L=2 \Omega, R_{1}=5 \Omega, R_{2}=10 \Omega_{\text {。 }}$ 求各支路电流及 $R_{1}$ 支路电流的有效值和该支路 的平均功率。

解: 由于非正弦激励以展开式的形式给出, 则步骤(1)可以从略, 直接从步骤(2)开始计算。

直流分量单独作用下的电路为图 1.4-4(b), 此时电感 $L$ 相当于短路; 电容 $C$ 相当于开路。 各支路电流分别为










$$
I_{L(0)}=\frac{U_{S(0)}}{R_{1}}=\frac{10}{5}=2 \mathrm{~A}, I_{C(0)}=0, I_{(0)}=I_{L(0)}+I_{C(0)}=2+0=2 \mathrm{~A}
$$

基波分量单独作用下的电路为图 1.4-4(c), 用复数计算各支路电流相量得.

$$
\begin{aligned}
& i_{L(1)}=\frac{U_{S(1)}}{R_{1}+\mathrm{j} \omega L}=\frac{(141.4 / \sqrt{2}) \angle 0^{\circ}}{5+\mathrm{j} 2}=\frac{100 \angle 0^{\circ}}{5.385 \angle 21.8^{\circ}}=18.6 \angle-21.8^{\circ} \mathrm{A} \\
& \begin{aligned}
i_{C(1)} & =\frac{U_{S(1)}}{R_{2}-\mathrm{j} \frac{1}{\omega C}}=\frac{(141.4 / \sqrt{2}) \angle 0^{\circ}}{10-\mathrm{j} 15}=\frac{100<0^{\circ}}{18 \angle 56.3^{\circ}}=5.56 \angle 56.3^{\circ} \mathrm{A} \\
I_{(1)} & =I_{L(1)}+i_{C(1)}=18.6 \angle-21.8^{\circ}+5.56 \angle 56.3^{\circ} \\
& =17.27-\mathrm{j} 6.91+3.084+\mathrm{j} 4.626=20.35-\mathrm{j} 2.284=20.5 \angle-6.4^{\circ} \mathrm{A}
\end{aligned}
\end{aligned}
$$

三次谐波单独作用下的电路为图 1.4-4(d), 用复数计算各支路电流相量得

$$
\begin{aligned}
i_{L(3)} & =\frac{U_{S(3)}}{R_{1}+\mathrm{j} 3 \omega L}=\frac{(70.7 / \sqrt{2}) \angle 30^{\circ}}{5+\mathrm{j} 3 \times 2}=\frac{50 \angle 30^{\circ}}{7.81 \angle 50.2}=6.4 \angle-20.2^{\circ} \mathrm{A} \\
i_{C(3)} & =\frac{U_{S(3)}}{R_{2}-\mathrm{j} \frac{1}{3 \omega C}}=\frac{(70.7 / \sqrt{2}) \angle 30^{\circ}}{10-\mathrm{j} 15 / 3}=\frac{50 \angle 30^{\circ}}{11.18 \angle-26.6^{\circ}}=4.47 \angle 56.6^{\circ} \mathrm{A} \\
\dot{I}_{(3)} & =i_{L(3)}+i_{C(3)}=6.4 \angle-20.0^{\circ}+4.47 \angle 56.6^{\circ} \\
& =6.006-\mathrm{j} 2.21+2.461+\mathrm{j} 3.732=8.467+\mathrm{j} 1.522=8.6 \angle 10.2^{\circ} \mathrm{A}
\end{aligned}
$$

在直流激励下各支路电流与在各次谐波单独作用下求得的各支路电流的瞬时值进行叠加 得各支路电流的瞬时值表达式

$$
\begin{aligned}
& i_{L}=I_{L(0)}+i_{L(1)}+i_{L(3)}=2+18.6 \sqrt{2} \sin \left(\omega t-21.8^{\circ}\right)+6.4 \sqrt{2} \sin \left(3 \omega t-20.2^{\circ}\right) \mathrm{A} \\
& i_{C}=I_{C(0)}+i_{C(1)}+i_{C(3)}=5.56 \sqrt{2} \sin \left(\omega t+56.3^{\circ}\right)+4.47 \sqrt{2} \sin \left(3 \omega t+56.6^{\circ}\right) \mathrm{A} \\
& i=I_{(0)}+i_{(1)}+i_{(3)}=2+20.5 \sqrt{2} \sin \left(\omega t-6.4^{\circ}\right)+8.6 \sqrt{2} \sin \left(3 \omega t+10.2^{\circ}\right) \mathrm{A}
\end{aligned}
$$

$R_{1}$ 支路电流的有效值为

$R_{1}$ 支路的平均功率为

$$
I_{L}=\sqrt{I_{L(0)}^{2}+i_{L(1)}^{2}+i_{L(3)}^{2}}=\sqrt{2^{2}+18.6^{2}+6.4^{2}}=19.77 \mathrm{~A}
$$

$$
\begin{aligned}
P_{R 1}= & P_{R 1(0)}+P_{R 1(1)}+P_{R 1(3)} \\
= & U_{\mathrm{S}(0)} I_{(0)}+U_{\mathrm{S}(1)} I_{L(1)} \cos \left(\psi_{u S(1)}-\psi_{i L(1)}\right)+U_{\mathrm{S}(3)} I_{L(3)} \cos \left(\psi_{u S(3)}-\psi_{i L(3)}\right) \\
= & 10 \times 2+(141.4 / \sqrt{2}) \times 18.6 \times \cos \left(0-\left(-21.8^{\circ}\right)\right) \\
& +(70.7 / \sqrt{2}) \times 6.4 \times \cos \left(30^{\circ}-\left(-20.2^{\circ}\right)\right) \\
= & 20+1727+205=1952 \mathrm{~W}
\end{aligned}
$$

也可以用以下方法计算 $R_{1}$ 支路的平均功率为

$$
P_{R 1}=I_{L}^{2} R_{1}=19.77^{2} \times 5=1952 \mathrm{~W}
$$

【例 1.4-4】在图 1.4-5 (a) 电路中, 已知: $u_{\mathrm{S}}(t)=60+90 \sin \left(\omega t+150^{\circ}\right)$ $+40 \sin \left(2 \omega t+60^{\circ}\right) \mathrm{V}, \frac{1}{\omega C_{1}}=400 \Omega, \omega L_{1}=100 \Omega, \frac{1}{\omega C_{2}}=100 \Omega, \omega L_{2}=100 \Omega, R=60 \Omega$ 。求电 阻 $R$ 和电感 $L_{1}$ 中的电流 $i_{R}(t) 、 i_{L 1}(t)$ 。

解: 在图 1.4-5(a) 电路中, 在电源的直流分量作用下由于两电容对直流相当于断路, 其全 部电压作用于电阻 $R$ 上。对电源中的基波分量, 因为 $\omega L_{2}=\frac{1}{\omega C_{2}}=100 \Omega$, 所以 $L_{2} 、 C_{2}$ 串联环节 发生串联谐振, 相当于短路, 即基波电流不会流过电阻 $R$ 。对电源中的 2 次谐波分量, 因为 $2 \omega L_{1}=\frac{1}{2 \omega C_{1}}=200 \Omega$, 所以 $L_{1} 、 C_{1}$ 并联环节发生并联谐振, 相当于开路, 即 2 次谐波电流也不会 流过电阻 $R$ 。则电阻 $R$ 中只有电源中的直流分量所形成的电流, 见图 1.4-5 (b)。得电阻 $R$ 中的电流

$$
i_{R}=I_{R(0)}=\frac{U_{S(0)}}{R}=\frac{60}{60}=1 \mathrm{~A}
$$

对电感 $L_{1}$ 而言, 在电源的直流分量作用下, 流过它的电流与流过电阻 $R$ 的电流为同一电 流, 即

$$
I_{L(0)}=I_{R(0)}=\frac{U_{\mathrm{S}(0)}}{R}=\frac{60}{60}=1 \mathrm{~A}
$$

电感 $L_{1}$ 在电源的基波分量作用下的电路见图 1.4-5(c), 因为 $\omega L_{2}=\frac{1}{\omega C_{2}}=100 \Omega, L_{2} 、 C_{2}$ 串 联环节相当于短路电路, 即电阻 $R$ 不起作用, 电感 $L_{1}$ 中的基波分量电流最大值相量为


电感 $L_{1}$ 在电源的 2 次谐波分量作用下的电路见图 1.4-5(d), 此时 $2 \omega L_{1}=\frac{1}{2 \omega C_{1}}=200 \Omega$, 










$L_{1} 、 C_{1}$ 并联环节相当于开路, 即电源的电压全部作用于 $L_{1}$ 与 $C_{1}$ 相并联的环节上, 则电感 $L_{1}$ 中的 2 次谐波分量电流最大值相量为

$$
i_{L \mathrm{~m}(2)}=\frac{U_{\mathrm{Sm}(2)}}{\mathrm{j} 2 \omega L_{1}}=\frac{40 \angle 60^{\circ}}{\mathrm{j} 200}=0.2 \angle-30^{\circ} \mathrm{A}
$$

得电感 $L_{1}$ 中的电流

$$
i_{L 1}(t)=I_{L 1(0)}+i_{L 1 \mathrm{~m}(1)}+i_{L 1 \mathrm{~m}(2)}=1+0.9 \sin \left(\omega t+60^{\circ}\right)+0.2 \sin \left(2 \omega t-30^{\circ}\right) \mathrm{A}
$$

\section{5 简单动态电路的时域分析}

\section{5 .1 换路定则和电压、电流初始值的确定}

\section{1. 换路定则}

换路:引起电路工作状态变动的因素统称为换路。这些因素包括:开关的接通或断开、电 源的量值突然变化、元件参数的改变以及突发事故和干扰等因素。

换路定则: 在换路时刻 $(t=0)$, 电容电压 (电荷量) 和电感电流(磁链) 不能突变。用 $t\left(0_{+}\right)$表示换路后的初始时刻,用 $t\left(0_{-}\right)$表示换路前的终止时刻。换路定则的表达式为

$$
\begin{aligned}
& u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right), q_{C}\left(0_{+}\right)=q_{C}\left(0_{-}\right) \\
& i_{L}\left(0_{+}\right)=i_{L}\left(0_{-}\right), \psi_{L}\left(0_{+}\right)=\psi_{L}\left(0_{-}\right)
\end{aligned}
$$

在电路理论中, 换路符号为图 1.5-1。

\section{2. 电压和电流初始值的确定}

确定电压和电流初始值的方法是, 用换路前的电路求


电容电压和电感电流换路前的终止值 $u_{C}\left(0_{-}\right)$和 $i_{L}\left(0_{-}\right)$, 应用换路定则确定电容电压和电感 电流换路后的初始值 $u_{C}\left(0_{+}\right)$和 $i_{L}\left(0_{+}\right)$。然后, 在换路后的电路中根据 KCL、KVL 以及系统分 析方法等求解直流电路的方法, 求出 $u_{R}\left(0_{+}\right) 、 i_{R}\left(0_{+}\right) 、 u_{L}\left(0_{+}\right)$和 $i_{C}\left(0_{+}\right)$等其他电路变量的初 始值。在求其他变量初始值时, 电路中的电容电压可以用电压为 $u_{C}\left(0_{+}\right)$的电压源替代, 电路 中的电感电流可以用电流为 $i_{L}\left(0_{+}\right)$的电流源替代。 顺便指出, 电路中除电容电压 $u_{C}$ 和电感电流 $i_{L}$ 在换路前后不能突变外, 其他变量 $u_{R} 、 i_{R} 、 u_{L}$ 和 $i_{c}$ 等其他电路变量均可能突变。

【例 1.5-1】在图 1.5-2(a) 电路中, $S$ 闭合时电路已达稳态。求 $S$ 打开时刻各支路电流和 电感电压的初始值 $i_{1}\left(0_{+}\right) 、 i_{2}\left(0_{+}\right) 、 i_{3}\left(0_{+}\right)$和 $u_{L}\left(0_{+}\right)$。






解: 在图 1.5-2(a) 换路前的电路中, 求得电容电压 $u_{C}\left(0_{-}\right)$和电感电流 $i_{L}\left(0_{-}\right)$分别为

$$
u_{c}\left(0_{-}\right)=U_{\mathrm{S}}, \quad i_{L}\left(0_{-}\right)=i_{2}\left(0_{-}\right)=\frac{U_{\mathrm{S}}}{R_{2}}
$$

根据换路定律, 在图 1.5-2(b) 换路后的电路中有

$$
\begin{aligned}
& u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=U_{\mathrm{S}} \\
& i_{2}\left(0_{+}\right)=i_{L}\left(0_{+}\right)=i_{L}\left(0_{-}\right)=i_{2}\left(0_{-}\right)=\frac{U_{\mathrm{S}}}{R_{2}}
\end{aligned}
$$

因为 $R_{1} i_{1}\left(0_{+}\right)=u_{c}\left(0_{+}\right)$, 可得

$$
i_{1}\left(0_{+}\right)=\frac{u_{C}\left(0_{+}\right)}{R_{1}}=\frac{u_{C}\left(0_{-}\right)}{R_{1}}=\frac{U_{S}}{R_{1}}
$$

根据 KCL 有

$$
i_{3}\left(0_{+}\right)=-\left[i_{1}\left(0_{+}\right)+i_{2}\left(0_{+}\right)\right]=-\left[\frac{U_{\mathrm{S}}}{R_{1}}+\frac{U_{\mathrm{S}}}{R_{2}}\right]=-\frac{R_{1}+R_{2}}{R_{1} R_{2}} U_{\mathrm{S}}
$$

根据 KVL 有

可得

$$
u_{C}\left(0_{+}\right)=i_{2}\left(0_{+}\right) R_{2}+u_{L}\left(0_{+}\right)
$$

$$
u_{L}\left(0_{+}\right)=u_{C}\left(0_{+}\right)-i_{2}\left(0_{+}\right) R_{2}=U_{\mathrm{S}}-\frac{U_{\mathrm{S}}}{R_{2}} R_{2}=0
$$

\subsection{2一阶动态电路分析的基本方法}

\section{1. 一阶动态电路及其微分方程}

严格地讲, 对含有动态元件 (电感或电容) 电路, 所列写的微分方程为一阶微分方程时, 该 电路为一阶动态电路, 简称一阶电路。在一般情况下, 若电路中只有一个动态元件时, 即为一 阶电路。

所谓动态电路的微分方程是在电路中以时间 $t$ 为主变量, 根据电路的基本定律所列写的 微分方程式。以图 1.5-3 的 $R 、 C$ 串联电路为例, 设电路在开关 $\mathrm{S}$ 闭合前电容 $C$ 的原始电压为 $U_{0}$, 即 $u_{c}\left(0_{-}\right)=U_{0}$, 在 $t=0$ 时刻开关 $\mathrm{S}$ 闭合, 求开关 $\mathrm{S}$ 闭合后电容电压随时间的变化规律 $u_{C}(t)$ 。根据 $\mathrm{KVL}$ 和 $i(t)=C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}$, 电路的微分方程为 

$$
R C \frac{\mathrm{d} u_{c}(t)}{\mathrm{d} t}+u_{c}(t)=U_{\mathrm{S}}
$$

此微分方程为一阶常系数 (线性) 非齐次微分方程, 其解的形式 为

$$
u_{c}(t)=u_{c}^{\prime}(t)+u_{c}^{\prime \prime}(t)
$$

其中: $u_{c}^{\prime}(t)$ 称为稳态分量, 此分量与微分方程的非齐次项 $U_{\mathrm{s}}$ 相关,



对稳态分量 $u_{C}^{\prime}(t)$, 因为是微分方程的一个特解, 所以在电路理论中用换路后的稳态电路 的解, 即换路后 $t \rightarrow \infty$ 时的解为稳态解, 对图 1.5-3 则有

$$
u_{C}^{\prime}(t)=U_{\mathrm{S}}
$$

暂态分量 $u_{\mathrm{c}}^{\prime \prime}(t)$ 为非齐次微分方程所对应的齐次微分方程的通解, 其解的形式为

$$
u_{G}^{\prime \prime}(t)=A \mathrm{e}^{s t}
$$

其中: $A$ 为由初始条件确定的待定常数; $s$ 为齐次微分方程所对应的特征方程的特征根。则

$$
u_{c}(t)=u_{C}^{\prime}(t)+u_{C}^{\prime \prime}(t)=U_{\mathrm{S}}+A \mathrm{e}^{s t}
$$

在换路后的电路中, 根据换路定则, 当 $t=0_{+}$时有 $u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=U_{0}$, 即电容电压 $u_{c}(t)$ 的初始条件为 $U_{0}$, 则有

求得待定常数

$$
U_{\mathrm{s}}+A=U_{0}
$$

$$
A=U_{0}-U_{\mathrm{s}}
$$

齐次微分方程所对应的特征方程为

$$
R C s+1=0
$$

得特征根为

$$
s=-\frac{1}{R C}
$$

由以上求得的待定常数 $A$ 和特征根 $s$ 得暂态分量为

$$
u_{c}^{\prime \prime}(t)=\left(U_{0}-U_{\mathrm{S}}\right) \mathrm{e}^{-\frac{1}{R C} t}
$$

最后可得开关 $\mathrm{S}$ 闭合后电容电压随时间的变化规律为

$$
u_{c}(t)=u_{c}^{\prime}(t)+u_{c}^{\prime \prime}(t)=U_{\mathrm{S}}+A \mathrm{e}^{t}=U_{\mathrm{S}}+\left(U_{0}-U_{\mathrm{S}}\right) \mathrm{e}^{-\frac{1}{R C^{t}}}
$$

以上所述是用数学中的微分方程方法分析一阶电路的基本方法, 也称为经典法。

\section{2. 一阶电路的零输入响应}

零输人响应是指在一阶电路换路后的电路中无激励源的情况下, 在动态元件原始储能的 电压、电流激励下所形成的电路响应。

(1) $R C$ 电路的零输入响应

在图 1.5-4(a) 电路中, 换路前开关在 $\mathrm{a}$ 点处已达稳态, 电容电压 $u_{c}(t)=U_{0}$ 。在 $t=0$ 时 刻开关倒向 $\mathrm{b}$ 点, 即 $t \geqslant 0$ 时构成图 $1.5-4$ ( $\mathrm{b})$ 的 $R C$ 放电电路。分析 $t \geqslant 0$ 时电容电压 $u_{c}(t)$ 和 电流 $i_{c}(t)$ 等其他变量随时间的变化规律称为 $R C$ 电路的零输人响应。

对图 1.5-4 (b) 换路后的电路, 根据 $\mathrm{KVL}$ 和 $i_{C}(t)=C \frac{\mathrm{d} u_{c}(t)}{\mathrm{d} t}$ 有如下微分方程: 






$$
R C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}+u_{c}(t)=0
$$

此微分方程为齐次微分方程, 在其解中无稳态分量 $u_{c}^{\prime}(t)$, 即在零输人条件下, 无外加激励, 则无强制响应。 暂态分量解的形式为 $u_{C}^{\prime \prime}(t)=A \mathrm{e}^{s t}$ 。根据换路定 则, 当 $t=0_{+}$时有 $u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=U_{0}$ 。

由初始条件可知 $A=U_{0}$ 。由特征方程 $R C s+1=0$ 得特征根为

$$
s=-\frac{1}{R C}
$$

得电容电压 $u_{C}(t)$ 的零输人响应

$$
u_{C}(t)=u_{C}^{\prime \prime}(t)=A \mathrm{e}^{s t}=U_{0} \mathrm{e}^{-\frac{1}{R C} t} \quad(t \geqslant 0)
$$

电流 $i_{c}(t)$ 的零输人响应为

$$
i_{C}(t)=C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}=-\frac{U_{0}}{R} \mathrm{e}^{-\frac{1}{R C}}(t \geqslant 0)
$$

$R C$ 电路的零输人响应的电容电压 $u_{C}(t)$ 和电流 $i_{C}(t)$ 随时间的 变化曲线见图 1.5-5。

(2) $R L$ 电路的零输入响应

在图 1.5-6(a) 电路中, 换路前电路已达稳态, 电感电流 $i_{L}(t)=$ $I_{0}$ 。在 $t=0$ 时刻换路, 即 $t \geqslant 0$ 时构成图 1.5-6(b) 的 $R 、 L$ 放电电路。








对图 1.5-6(b) 换路后的电路, 根据 KVL 和 $u_{L}(t)=$ $L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}$ 有如下微分方程:

$$
L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}+R i_{L}(t)=0
$$

此微分方程为齐次微分方程, 在其解中无稳态分量 $i_{L}^{\prime}(t)$, 即在零输人条件下, 无外加激励, 则无强制响应。

暂态分量解的形式为 $i_{L}^{\prime \prime}(t)=A \mathrm{e}^{s t}$ 。根据换路定则, 当 $t=0_{+}$时有 $i_{L}\left(0_{+}\right)=i_{L}\left(0_{-}\right)=$ $I_{0}$ 。由初始条件可知 $A=I_{0}$ 。由特征方程 $L s+R=0$ 得特征根为

$$
s=-\frac{R}{L}
$$

得电感电流 $i_{L}(t)$ 的零输人响应

$$
i_{L}(t)=i_{L}^{\prime \prime}(t)=A \mathrm{e}^{s t}=I_{0} \mathrm{e}^{-\frac{R}{L^{t}}} \quad(t \geqslant 0)
$$

电压 $u_{L}(t)$ 的零输人响应

$$
u_{L}(t)=L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}=-I_{0} \operatorname{Re}^{-\frac{R}{L} t} \quad(t \geqslant 0)
$$

$R L$ 电路的零输入响应的电感电流 $i_{L}(t)$ 和电压 $u_{L}(t)$ 随时间的 变化曲线见图 1.5-7。



\section{3. 一阶电路的零状态响应}

零状态响应是指在一阶电路换路后的电路中, 动态元件的初始值为零的条件下, 在外加激 场源的作用时所形成的电路响应。

(1) $R C$ 电路在直流激励下的零状态响应

关 $S$ 闭合, 分析在直流电压源 $U_{\mathrm{S}}$ 激励下, $t \geqslant 0$ 时电容电压 $u_{C}(t)$ 和电流 $i_{c}(t)$ 等其他变量随时间的变化规律称为 $R C$ 电路在直流 激励下的零状态响应。

根据 KVL 和 $i_{C}(t)=C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}$ 有如下微分方程：

$$
R C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}+u_{C}(t)=U_{\mathrm{S}}
$$



取换路后 $t \rightarrow \infty$ 时的解为稳态解, 则有

$$
u_{c}^{\prime}(t)=U_{\mathrm{S}}
$$

暂态解的形式为

\section{微分方程的解为}

$$
u_{c}^{\prime \prime}(t)=A \mathrm{e}^{*}
$$

$$
u_{c}(t)=u_{c}^{\prime}(t)+u_{C}^{\prime \prime}(t)=U_{\mathrm{S}}+A \mathrm{e}^{s t}
$$

根据换路定则, 当 $t=0_{+}$时有 $u_{c}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=0$, 则有 $U_{\mathrm{S}}+A=0$, 可得 $A=-U_{\mathrm{S}}$ 。 特征方程为 $R C s+1=0$, 得

$$
s=-\frac{1}{R C}
$$

最后得电容电压和电流在直流激励下的零状态响应分别为

$$
u_{C}(t)=u_{C}^{\prime}(t)+u_{C}^{\prime \prime}(t)=U_{\mathrm{S}}-U_{\mathrm{S}} \mathrm{e}^{-\frac{1}{R c^{t}}}=U_{\mathrm{S}}\left(1-\mathrm{e}^{-\frac{1}{R C^{t}}}\right) \quad(t \geqslant 0)
$$



$$
i_{C}(t)=C \frac{\mathrm{d} u_{c}(t)}{\mathrm{d} t}=\frac{U_{\mathrm{S}}}{R} \mathrm{e}^{-\frac{1}{R C^{t}}} \quad(t \geqslant 0)
$$

$R C$ 电路的零状态响应的电容电压 $u_{C}(t)$ 和电流 $i_{C}(t)$ 随时间 的变化曲线见图 1.5-9。

\section{(2) $R L$ 电路在直流激励下的零状态响应}

在图 1.5-10 电路中, 开关 S 闭合前电路已达稳态, 电感电流 $i_{L}\left(0_{-}\right)=0_{\mathrm{o}}$ 在 $t=0$ 时刻开关 $\mathrm{S}$ 闭合, 分析在直流电压源 $U_{\mathrm{S}}$ 激励 下, $t \geqslant 0$ 时电感电流 $i_{L}(t)$ 和电压 $u_{L}(t)$ 的零状态响应。

根据 KVL 和 $u_{L}(t)=L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}$ 有如下微分方程:

$$
L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}+R i_{L}(t)=U_{\mathrm{S}}
$$

取换路后 $t \rightarrow \infty$ 时的解为稳态解, 则有

$$
i_{L}^{\prime}(t)=\frac{U_{\mathrm{S}}}{R}
$$



$$
i_{L}^{\prime \prime}(t)=A \mathrm{e}^{s t}
$$

微分方程的解为

$$
i_{L}(t)=i_{L}^{\prime}(t)+i_{L}^{\prime \prime}(t)=\frac{U_{\mathrm{S}}}{R}+A \mathrm{e}^{s t}
$$

根据换路定则, 当 $t=0_{+}$时有 $i_{L}\left(0_{+}\right)=i_{L}\left(0_{-}\right)=0$, 则有 $\frac{U_{\mathrm{S}}}{R}+A=0$, 可得 $A=-\frac{U_{\mathrm{S}}}{R}$ 。特 征方程为 $L s+R=0$, 得

$$
s=-\frac{R}{L}
$$

最后得电感电流和电压在直流激励下的零状态响应分别为

$$
i_{L}(t)=i_{L}^{\prime}(t)+i_{L}^{\prime \prime}(t)=\frac{U_{\mathrm{S}}}{R}-\frac{U_{\mathrm{S}}}{R} \mathrm{e}^{-\frac{R}{L} t}=\frac{U_{\mathrm{S}}}{R}\left(1-\mathrm{e}^{-\frac{R}{L^{t}}}\right) \quad(t \geqslant 0)
$$



$$
u_{L}(t)=L \frac{\mathrm{d} i_{L}(t)}{\mathrm{d} t}=U_{\mathrm{S}} \mathrm{e}^{-\frac{R}{L^{t}}} \quad(t \geqslant 0)
$$

$R L$ 电路的零状态响应的电容电流 $i_{L}(t)$ 和电压 $u_{L}(t)$ 随时 间的变化曲线见图 1.5-11。

\section{4. 一阶电路的全响应}

在一阶电路换路后有激励源存在, 且动态元件的初始值不为 零情况下, 电路中的响应为全响应。求解全响应的基本方法是微 分方程法, 即在本节开始处以图 1.5-3 的 $R 、 C$ 串联电路为例, 通 过列微分方程、求稳态解、写通解、定常数和求特征根等步骤, 可得所需的全响应。也可以根据 叠加定理将零输人响应与零状态响应相叠加得全响应。例如, 前面对 $R C$ 电路中, 电容电压 $u_{c}(t)$ 的零输人响应和零状态响应已分别求得

则全响应为

$$
u_{C}(t)_{\text {零输人 }}=U_{0} \mathrm{e}^{-\frac{1}{R C^{t}}}, u_{C}(t)_{\text {多状态 }}=U_{\mathrm{S}}\left(1-\mathrm{e}^{-\frac{1}{R C^{t}}}\right)
$$

$$
u_{C}(t)=u_{C}(t)_{\text {零输入 }}+u_{\mathrm{C}}(t)_{\text {雨状态 }}=U_{0} \mathrm{e}^{-\frac{1}{R C}}+U_{\mathrm{S}}\left(1-\mathrm{e}^{-\frac{1}{R C^{t}}}\right)=U_{\mathrm{S}}+\left(U_{0}-U_{\mathrm{S}}\right) \mathrm{e}^{-\frac{1}{R C^{t}}}
$$

此结果与在本节开始处以图 1.5-3 的 $R 、 C$ 串联电路为例, 用微分方程求得的结果相同。 为帮助记忆将此方法取名为叠加经典法。

顺便指出, 前面用微分方程所得到各种情况下的结果皆可作为公式直接使用。

\section{5. 求解一阶动态电路全响应的三要素法}

以 $R C$ 电路中电容电压 $u_{c}(t)$ 的全响应为例, 即

$$
u_{C}(t)=U_{\mathrm{S}}+\left(U_{0}-U_{\mathrm{S}}\right) \mathrm{e}^{-\frac{1}{R C}}
$$

其中: (1) $U_{\mathrm{S}}=u_{c}^{\prime}(t)$ 为换路后所求变量的稳态值, 即换路后 $t \rightarrow \infty$ 时的响应值, 可记为 $f(\infty)$;

(2) $U_{0}$ 为换路后所求变量的初始值, 可记为 $f\left(0_{+}\right)$;

(3) $R C$ 称为换路后电路的时间常数 $\tau$, 在 $R L$ 电路中 $\tau=L / R$ 。

由此可见, 当求解一阶动态电路全响应时, 只需求得所求变量的三个要素, 即换路后电路 的稳态值 $f(\infty)$ 、换路后的初始值 $f\left(0_{+}\right)$和电路的时间常数 $\tau$, 就可求得该变量的全响应。三 要素法的一般公式为 

$$
f(t)=f(\infty)+\left[f\left(0_{+}\right)-f(\infty)\right] \mathrm{e}^{-\frac{t}{\tau}}
$$

此公式适用于电路中的任何变量。

【例 1.5-2】在图 1.5-12 中, 已知 $R_{1}=8 \Omega, R_{2}=12 \Omega, L=$ $0.6 \mathrm{H}$, 直流电压源 $U_{\mathrm{S}}=220 \mathrm{~V}$ 。开关 $\mathrm{S}$ 打开时电路已达稳态, 在 $t$ $=0$ 时将开关 $\mathrm{S}$ 闭合。求 $\mathrm{S}$ 闭合后电路中的电流 $i(t)$ 。 定则有

解法 1 : 用叠加经典法。设 $U_{\mathrm{S}}=0$, 先求零输人响应。根据换路

$$
i\left(0_{+}\right)=i\left(0_{-}\right)=I_{0}=\frac{U_{\mathrm{S}}}{R_{1}+R_{2}}=\frac{220}{8+12}=11 \mathrm{~A}
$$



得 $S$ 闭合后电路中电流的零输人响应为

$$
i(t)_{\text {察䑳入 }}=I_{0} \mathrm{e}^{-\frac{R_{2}}{t^{t}}}=11 \mathrm{e}^{-\frac{12}{0.6^{t}}}=11 \mathrm{e}^{-20 t} \mathrm{~A}
$$

求零状态响应, 此时 $U_{\mathrm{S}}=220 \mathrm{~V}$, 并设初始电流 $I_{0}=0$, 可得

$$
i(t)_{\text {正状态 }}=\frac{U_{\mathrm{S}}}{R_{2}}\left(1-\mathrm{e}^{-\frac{R_{2}}{L}}\right)=\frac{220}{12}\left(1-\mathrm{e}^{-\frac{12}{0.6^{t}}}\right)=18.3\left(1-\mathrm{e}^{-20 t}\right) \mathrm{A}
$$

最后得 $\mathrm{S}$ 闭合后电路中的电流响应

$$
i(t)=i(t)_{\text {买辅人 }}+i(t)_{\text {米状态 }}=11 \mathrm{e}^{-20 t}+18.3\left(1-\mathrm{e}^{-20 t}\right)=18.3-7.3 \mathrm{e}^{-20 t} \mathrm{~A} \quad(t \geqslant 0)
$$

解法 2 : 用三要素法。

$$
\begin{aligned}
& i(\infty)=\frac{U_{\mathrm{S}}}{R_{2}}=\frac{220}{12}=18.3 \mathrm{~A} \\
& i\left(0_{+}\right)=i\left(0_{-}\right)=\frac{U_{\mathrm{S}}}{R_{1}+R_{2}}=\frac{220}{8+12}=11 \mathrm{~A} \\
& \tau=\frac{L}{R_{2}}=\frac{0.6}{12}=\frac{1}{20} \mathrm{~s}
\end{aligned}
$$



最后得 $\mathrm{S}$ 闭合后电路中的电流响应

$$
\begin{aligned}
i(t) & =i(\infty)+\left[i\left(0_{+}\right)-i(\infty)\right] \mathrm{e}^{-\frac{1}{t}} \\
& =18.3+(11-18.3) \mathrm{e}^{-20 t}=18.3-7.3 \mathrm{e}^{-20 t} \mathrm{~A} \quad(t \geqslant 0)
\end{aligned}
$$

此电流的变化曲线见图 1.5-13。

【例 1.5-3】 在图 1.5-14 中, 已知 $R_{1}=6 \Omega, R_{2}=3 \Omega, C=$ $0.5 \mu \mathrm{F}$, 直流电压源 $U_{\mathrm{S}}=24 \mathrm{~V}$ 。开关 $\mathrm{S}$ 打开时电路已达稳态, 在 $t$ $=0$ 时将开关 $\mathrm{S}$ 闭合。求 $\mathrm{S}$ 闭合后电容电压 $u_{\mathrm{C}}(t)$ 和电路中各支路电流 $i_{1}(t) 、 i_{2}(t)$ 及 $i_{c}(t)$ 。

解法 1 : 用三要素法, 首选 $u_{C}(t)$ 变量。

$$
\begin{aligned}
& u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=U_{\mathrm{S}}=24 \mathrm{~V} \\
& u_{C}(\infty)=\frac{U_{\mathrm{S}}}{R_{1}+R_{2}} R_{2}=\frac{24}{6+3} \times 3=8 \mathrm{~V} \\
& \tau=R C
\end{aligned}
$$

式中的电阻 $R$ 应为将电压源置零后, 从动态元件电容 $C$ 两



$$
R_{\text {in }}=\frac{R_{1} R_{2}}{R_{1}+R_{2}}=\frac{6 \times 3}{6+3}=2 \Omega
$$

得

$$
\tau=R_{\text {in }} C=2 \times 0.5 \times 10^{-6}=10^{-6} \mathrm{~s}
$$

得 $\mathrm{S}$ 闭合后电容电压

$$
u_{C}(t)=u_{C}(\infty)+\left[u_{C}\left(0_{+}\right)-u_{C}(\infty)\right] \mathrm{e}^{-\frac{1}{\tau} t}=8+(24-8) \mathrm{e}^{-10^{6} t}=8+16 \mathrm{e}^{-10 \sigma_{t}} \mathrm{~V} \quad(t \geqslant 0)
$$

电路中各支路电流分别为

$$
\begin{aligned}
& i_{C}(t)=C \frac{\mathrm{d} u_{\mathrm{C}}(t)}{\mathrm{d} t}=0.5 \times 10^{-6} \times 16 \times\left(-10^{6}\right) \mathrm{e}^{-10^{6} t}=-8 \mathrm{e}^{-10^{6} t} \mathrm{~A} \quad(t \geqslant 0) \\
& i_{2}(t)=\frac{u_{C}(t)}{R_{2}}=\frac{8+16 \mathrm{e}^{-10^{6} t}}{3}=2.67+5.33 \mathrm{e}^{-10^{6} t} \mathrm{~A} \quad(t \geqslant 0) \\
& i_{1}(t)=i_{C}(t)+i_{2}(t)=-8 \mathrm{e}^{-10^{6} t}+2.67+5.33 \mathrm{e}^{-10^{6} t}=2.67\left(1-\mathrm{e}^{-10^{6 t}}\right) \mathrm{A} \quad(t \geqslant 0)
\end{aligned}
$$

电容电压 $u_{C}(t)$ 和电路中各支路电流 $i_{1}(t) 、 i_{2}(t)$ 及 $i_{C}(t)$ 的变化曲线见图 1.5-15。


解法 2 : 用三要素法。首选 $i_{1}(t)$ 变量。

$$
\begin{aligned}
& i_{1}\left(0_{+}\right)=\frac{U_{\mathrm{S}}-u_{C}\left(0_{+}\right)}{R_{1}}=\frac{U_{\mathrm{S}}-u_{C}\left(0_{-}\right)}{R_{1}}=\frac{24-24}{6}=0 \\
& i_{1}(\infty)=\frac{U_{\mathrm{S}}}{R_{1}+R_{2}}=\frac{24}{3+6}=2.67 \mathrm{~A} \\
& \tau=R C
\end{aligned}
$$

式中的电阻 $R$ 应为将电压源置零后, 从动态元件电容 $C$ 两端看进去的人端电阻 $R_{\mathrm{in}}$, 即

$$
R_{\text {in }}=\frac{R_{1} R_{2}}{R_{1}+R_{2}}=\frac{6 \times 3}{6+3}=2 \Omega
$$

得

$$
\tau=R_{\mathrm{in}} C=2 \times 0.5 \times 10^{-6}=10^{-6} \mathrm{~s}
$$

得

$$
\begin{aligned}
& \begin{aligned}
i_{1}(t) & =i_{1}(\infty)+\left[i_{1}\left(0_{+}\right)-i_{1}(\infty)\right] \mathrm{e}^{-\frac{t}{\tau}}=2.67+[0-2.67] \mathrm{e}^{-\frac{t}{10-6}} \\
& =2.67\left(1-\mathrm{e}^{-10^{6}}\right) \mathrm{A} \quad(t \geqslant 0)
\end{aligned} \\
& \begin{aligned}
u_{\mathrm{C}}(t) & =-R_{1} i_{1}(t)+U_{\mathrm{S}}=-6 \times 2.67\left(1-\mathrm{e}^{-100_{t}}\right)+24=8+16 \mathrm{e}^{-10^{6 t}} \mathrm{~V} \quad(t \geqslant 0)
\end{aligned} \\
& i_{C}(t)=C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}=0.5 \times 10^{-6} \times 16 \times\left(-10^{6}\right) \mathrm{e}^{-10^{6} t}=-8 \mathrm{e}^{-10^{6} t} \mathrm{~A} \quad(t \geqslant 0) \\
& i_{2}(t)=\frac{U_{\mathrm{C}}(t)}{R_{2}}=\frac{8+16 \mathrm{e}^{-10^{6} t}}{3}=2.67+5.33 \mathrm{e}^{-10^{6 t}} \mathrm{~A} \quad(t \geqslant 0)
\end{aligned}
$$

解法 3 : 用叠加经典法。先求 $u_{C}(t)$ 的零输入响应。在换路后的电路中设 $U_{\mathrm{S}}=0$, 求得 $u_{c}\left(0_{+}\right)=U_{0}=24 \mathrm{~V}$ 。零输人响应的计算公式为 

$$
u_{C}(t)_{\text {霜揄入 }}=U_{0} \mathrm{e}^{-\frac{1}{R C}} \quad(t \geqslant 0)
$$

式中的电阻 $R$ 应为将电压源置零后, 从动态元件电容 $C$ 两端看进去的人端电阻 $R_{\mathrm{in}}$, 即

$$
R_{\text {in }}=\frac{R_{1} R_{2}}{R_{1}+R_{2}}=\frac{6 \times 3}{6+3}=2 \Omega
$$

得

$$
u_{C}(t)_{\text {棈人 }}=U_{0} \mathrm{e}^{-\frac{1}{R_{\mathrm{in}} t}}=24 \mathrm{e}^{-\frac{1}{2 \times 0.5 \times 10-0^{t}}}=24 \mathrm{e}^{-100_{t} t} \mathrm{~V} \quad(t \geqslant 0)
$$

再求 $u_{C}(t)$ 的零状态响应, 在换路后的电路中, 设 $u_{C}\left(0_{+}\right)=U_{0}=0$ 。零状态响应的计算公 式为

$$
u_{C}(t)_{\text {年状志 }}=U_{\mathrm{S}}^{\prime}\left(1-\mathrm{e}^{-\frac{1}{R c^{\prime}}}\right) \quad(t \geqslant 0)
$$

式中的电压源的电压 $U_{\mathrm{s}}^{+}$应为从动态元件电容 $C$ 两端开路后, 戴维南等效电路的开路电压 $U_{0 c}$, 即

$$
U_{\mathrm{S}}^{\prime}=U_{\mathrm{oC}}=\frac{U_{\mathrm{S}}}{R_{1}+R_{2}} R_{2}=\frac{24}{6+3} \times 3=8 \mathrm{~V}
$$

得

$$
u_{C}(t)_{\text {算状态 }}=U_{\mathrm{S}}^{\prime}\left(1-\mathrm{e}^{-\frac{1}{R_{\mathrm{in}} C^{t}}}\right)=8\left(1-\mathrm{e}^{-\frac{1}{2 \times 0.5 \times 10-6 t}}\right)=8\left(1-\mathrm{e}^{-106_{t} t}\right) \mathrm{V} \quad(t \geqslant 0)
$$

得 $\mathrm{S}$ 闭合后电容电压 $u_{c}(t)$ 的全响应

$$
u_{C}(t)=u_{C}(t)_{\text {年输入 }}+u_{C}(t)_{\text {军状态 }}=24 \mathrm{e}^{-106^{6}}+8\left(1-\mathrm{e}^{-106_{t}}\right)=8+16 \mathrm{e}^{-106_{t}} \mathrm{~V} \quad(t \geqslant 0)
$$

电路中各支路电流分别为

$$
\begin{aligned}
& i_{C}(t)=C \frac{\mathrm{d} u_{C}(t)}{\mathrm{d} t}=0.5 \times 10^{-6} \times 16 \times\left(-10^{6}\right) \mathrm{e}^{-10 \sigma_{t}}=-8 \mathrm{e}^{-106_{t}} \mathrm{~A} \quad(t \geqslant 0) \\
& i_{2}(t)=\frac{u_{C}(t)}{R_{2}}=\frac{8+16 \mathrm{e}^{-10 \sigma_{t} t}}{3}=2.67+5.33 \mathrm{e}^{-106_{t}} \mathrm{~A} \quad(t \geqslant 0) \\
& i_{1}(t)=i_{C}(t)+i_{2}(t)=-8 \mathrm{e}^{-106_{t} t}+2.67+5.33 \mathrm{e}^{-106_{t}}=2.67\left(1-\mathrm{e}^{-10 \sigma_{t}}\right) \mathrm{A} \quad(t \geqslant 0)
\end{aligned}
$$

\subsection{3 二阶电路分析的基本方法}

用二阶微分方程描述的动态电路为二阶电路。在时域中分析二阶电路的基本方法是微分 方程法。现以 $R L C$ 夰联电路的零状态响应为例简要介绍二阶电路分析的基本方法。

在图 1.5-16 中, 设电容 $C$ 在换路前的电压值 $U_{C}\left(0_{-}\right)=U_{0}$, 求开关闭合后的动态过程。

根据 KVL 列换路后电路的微分方程

$$
u_{L}+u_{R}+u_{C}=L \frac{\mathrm{d} i}{\mathrm{~d} t}+R i+u_{C}=0
$$

将 $i=C \frac{\mathrm{d} u_{C}}{\mathrm{~d} t}$ 代人上式得

$$
L C \frac{\mathrm{d}^{2} u_{C}}{\mathrm{~d} t^{2}}+R C \frac{\mathrm{d} u_{C}}{\mathrm{~d} t}+u_{C}=0
$$



此方程为齐次微分方程, 则无强制响应, 即 $u_{c}^{\prime}=0$ 。此微分方程的特征方程为

$$
L C s^{2}+R C s+1=0
$$

特征根为 

$$
s_{1,2}=-\frac{R}{2 L} \pm \sqrt{\frac{R^{2}}{4 L}-\frac{1}{L C}}=-\beta \pm \sqrt{\beta^{2}-\omega_{0}^{2}}
$$

式中: $\beta=R / 2 L, \omega_{0}=\sqrt{1 / L C}$ 。

对不同的电路参数 $R 、 L$ 和 $C$ 的情况下特征根有以下三种不同情况。

(1) 当 $\beta>\omega_{0}$ 时, $s_{1}$ 和 $s_{2}$ 为两个不等实根

\section{微分方程的解为}

$$
\begin{aligned}
& s_{1}=-\beta+\sqrt{\beta^{2}-\omega_{0}^{2}} \\
& s_{2}=-\beta-\sqrt{\beta^{2}-\omega_{0}^{2}}
\end{aligned}
$$

$$
u_{C}=u_{C}^{\prime \prime}=A_{1} \mathrm{e}^{s_{1} t}+A_{2} \mathrm{e}^{s_{2} t}
$$

待定常数 $A_{1}$ 和 $A_{2}$ 可由 $u_{C}$ 和 $\mathrm{d} u_{C} / \mathrm{d} t$ 的初值求得。根据换路定则有

可得

$$
\begin{aligned}
& u_{C}\left(0_{+}\right)=u_{C}\left(0_{-}\right)=U_{0} \\
& \left.\frac{\mathrm{d} u_{C}}{\mathrm{~d} t}\right|_{t=0_{+}}=\left.\frac{\mathrm{d} u_{C}}{\mathrm{~d} t}\right|_{t=0_{-}}=\frac{i\left(0_{+}\right)}{C}=\frac{i\left(0_{-}\right)}{C}=0
\end{aligned}
$$

$$
\begin{aligned}
& A_{1}+A_{2}=U_{0} \\
& A_{1} s_{1}+A_{2} s_{2}=0
\end{aligned}
$$

解得

$$
A_{1}=\frac{s_{2}}{s_{2}-s_{1}} U_{0}, A_{2}=\frac{s_{1}}{s_{1}-s_{2}} U_{0}
$$

最后可得电路中各变量的零输入响应分别为

$$
\begin{aligned}
& u_{C}=\frac{s_{2}}{s_{2}-s_{1}}\left(s_{2} \mathrm{e}^{s_{1} t}-s_{1} \mathrm{e}^{s_{2} t}\right) \quad(t \geqslant 0) \\
& i=C \frac{\mathrm{d} u_{C}}{\mathrm{~d} t}=\frac{U_{0}}{L\left(s_{2}-s_{1}\right)}\left(\mathrm{e}^{s_{1} t}-\mathrm{e}^{s_{2} t}\right) \quad(t \geqslant 0) \\
& u_{L}=L \frac{\mathrm{d} i}{\mathrm{~d} t}=\frac{U_{0}}{s_{2}-s_{1}}\left(s_{1} \mathrm{e}^{s_{1} t}-s_{2} \mathrm{e}^{s_{2} t}\right) \quad(t \geqslant 0) \\
& u_{R}=R i=\frac{R U_{0}}{L\left(s_{2}-s_{1}\right)}\left(\mathrm{e}^{s_{1} t}-\mathrm{e}^{s_{2} t}\right) \quad(t \geqslant 0)
\end{aligned}
$$



各变量随时间 $t$ 的变化曲线见图 1.5-17。

由以上各变量响应表达式和变化曲线可以看出, 因为 $s_{1}$ 和 $s_{2}$ 都小于零, 所以各变量都按指数规律衰减, 最后都趋向于零。因 为 $0>s_{1}>s_{2}$, 所以电流 $i$ 和电阻电压 $u_{R}$ 皆为负值, 电容连续放电。 但因有电感存在, 电流不能突变, 电流从零开始先反向增加, 到达 最大值后又趋向于零。当电流最大时其变化率为零, 此时电感电 压 $u_{L}$ 为零。在工程上将这种参数下的情况称为过阻尼非振荡过 程。

(2)当 $R<2 \sqrt{L / C}$ 时, 即 $R / 2 L<2 \sqrt{1 / L C}$, 即 $\beta<\omega_{0}$ 时, $s_{1}$ 和 $s_{2}$ 为一对共轭复根, 经进一步确 定待定常数 $A_{1}$ 和 $A_{2}$ (数学推导从略), 可得如下各变量的零状态响应。 

$$
\begin{aligned}
& u_{C}=U_{0} \frac{\omega_{0}}{\omega^{\prime}} \mathrm{e}^{-\beta t} \sin \left(\omega^{\prime} t+\arctan \frac{\omega^{\prime}}{\beta}\right) \quad(t \geqslant 0) \\
& i=-\frac{U_{0}}{\omega^{\prime} L} \mathrm{e}^{-\beta t} \sin \omega^{\prime} t \quad(t \geqslant 0) \\
& u_{L}=U_{0} \frac{\omega_{0}}{\omega^{\prime}} \mathrm{e}^{-\beta t} \sin \left(\omega^{\prime} t-\arctan \frac{\omega^{\prime}}{\beta}\right) \quad(t \geqslant 0)
\end{aligned}
$$

式中

$$
\omega^{\prime}=\sqrt{\omega_{0}^{2}-\beta^{2}}=\sqrt{\frac{1}{L C}-\frac{R^{2}}{4 L^{2}}}
$$

各变量随时间 $t$ 的变化曲线见图 1.5-18。

由以上各变量响应表达式和变化曲线可以看出, 各变量皆为幅值依指数规律衰减的正弦波。从 $t=0$ 时电流 $i$ 开始反向放电, 到达最大值即变化率为零时 电感电压 $u_{L}$ 与电容电压 $u_{C}$ 相等。经过多次反复衰减 振荡, 最后各变量皆趋向于零。在工程上将这种参数 下的情况称为欠阻尼振荡过程。若电路中无电阻或负 阻器补偿掉电路中的电阻, 可以构成等幅的正弦振荡



(3)当 $R=2 \sqrt{L / C}$ 时, 即 $R / 2 L=2 \sqrt{1 / L C}$, 即 $\beta=\omega_{0}$ 时, $s_{1}$ 和 $s_{2}$ 为一重根, 即

$$
s_{1}=s_{2}=-\beta
$$

各变量的零状态响应为

$$
\begin{aligned}
& u_{C}=U_{0}(1+\beta t) \mathrm{e}^{-\beta t} \quad(t \geqslant 0) \\
& i=-\frac{U_{0}}{L} t \mathrm{e}^{-\beta t} \quad(t \geqslant 0) \\
& u_{L}=U_{0}(1-\beta t) \mathrm{e}^{-\beta t} \quad(t \geqslant 0)
\end{aligned}
$$

各变量随时间 $t$ 的变化情况和变化曲线与非振荡过程相仿, 不再赘述。在工程上将这种 参数下的情况称为临界状态。

总之, 对二阶动态电路进行时域分析的基本方法是, 按照电路具体情况, 列写相应的二阶 微分方程, 根据微分方程和由电路参数决定的特征根特点, 解微分方程即可得到所需求解的变 量。

\section{6 静电场}

1.6 .1 电场强度、电位

\section{1. 电场强度}

定义: 正试验点电荷 $q_{0}$ 在电场中某点受力为 $\boldsymbol{F}$, 则电场强度为

$$
\boldsymbol{E}=\lim _{q_{0} \rightarrow 0} \frac{\boldsymbol{F}}{q_{0}}
$$

式中, $q_{0}$ 的单位为库仑 $(\mathrm{C}), \boldsymbol{F}$ 的单位为牛顿 $(\mathrm{N})$, 电场强度 $\boldsymbol{E}$ 的单位为伏特/米 $(\mathrm{V} / \mathrm{m})$ 。

电场强度 (简称场强) 是表示电场强弱的基本物理量, 是一个向量, 其大小反映该点场的 强弱, 其方向表示该点置一正试验点电荷受力的方向。静电场是由静止电荷产生的, 并且满足 无旋场特性, 即

$$
\oint_{1} \boldsymbol{E} \cdot \mathrm{d} \boldsymbol{l}=0 \text { 或 } \boldsymbol{\nabla} \times \boldsymbol{E}=\mathbf{0}
$$

在无限大均匀介质中, 点电荷 $q$ 产生的电场可以用下面公式计算:

$$
E=\frac{q}{4 \pi \varepsilon r^{2}} e_{r}
$$

式中, $r$ 表示源点 (电荷所在的点) 与场点(待计算场强的点)之间的距离, $\boldsymbol{e}_{r}$ 表示由源点指向场 点的单位向量。 $\varepsilon$ 表示介质的介电系数, 其单位为法拉 $/$ 米 $(\mathrm{F} / \mathrm{m})$, 在真空中, 通常用 $\varepsilon_{0}$ 表示 其介电系数,并且

$$
\varepsilon_{0}=\frac{1}{36 \pi} \times 10^{-9}=8.85 \times 10^{-12} \mathrm{~F} / \mathrm{m}
$$

关于点电荷在无限大均匀介质中计算公式的来历, 可以通过库仑定律直接获得。库仑定 律表示: 在无限大真空中, 两个距离为 $r$ 的点电荷 $q_{1}$ 和 $q_{2}$, 它们之间的作用力与 $r$ 的平方成反 比,与电荷的大小成正比,电荷间作用力的方向表现为同性相斥、异性相吸,其计算公式可以用 下式表示:

$$
\boldsymbol{f}=\frac{q_{1} q_{2}}{4 \pi \varepsilon_{0} r^{2}} e_{f}
$$

如果其中一个电荷可视作试验点电荷, 则由于 $\boldsymbol{E}=\boldsymbol{f} / q$, 则可得点电荷场强计算公式。将 $\varepsilon_{0}$ 写 成 $\varepsilon$,该计算式同样适用于无限大均匀介质。

除点电荷以外,工程上也常用所谓线电荷、面电荷和体电荷分布的概念。它们的定义分别 为

$$
\begin{aligned}
& \tau=\lim _{\Delta l \rightarrow 0} \frac{\Delta q}{\Delta l} \quad \mathrm{C} / \mathrm{m} \\
& \sigma=\lim _{\Delta S \rightarrow 0} \frac{\Delta q}{\Delta S} \mathrm{C} / \mathrm{m}^{2} \\
& \rho=\lim _{\Delta V \rightarrow 0} \frac{\Delta q}{\Delta V} \quad \mathrm{C} / \mathrm{m}^{3}
\end{aligned}
$$

如果在所研究的范围内, 电荷分布不是空间坐标的函数而是一个常量, 则称之为均匀分布电 荷。

多个点电荷或连续分布的电荷形成的电场均可以运用叠加定理计算, 但是由于 $\boldsymbol{E}$ 是向 量, 因此计算时应采用向量叠加,这一过程有时是很麻烦的。

对于无限大均匀介质中多个点电荷形成的电场, 其计算公式为

$$
\boldsymbol{E}=\frac{1}{4 \pi \varepsilon} \sum_{i=1}^{n} \frac{q_{i}}{r_{i}} \boldsymbol{e}_{i}
$$

式中, $q_{i} r_{i}$ 和 $e_{i}$ 分别表示第 $i$ 个点电荷单独作用时对应的电荷值、距离和单位向量。

对于无限大均匀介质中连续分布的电荷, 可以首先取一微分量, 并视作点电荷 $\mathrm{d} q$ 。针对 线元、面积元和体积元, 可以用以下各式分别求出 $\mathrm{d} q$ 值, 即

$$
\begin{aligned}
& \mathrm{d} q=\tau \mathrm{d} l^{\prime} \\
& \mathrm{d} q=\sigma \mathrm{d} S^{\prime}
\end{aligned}
$$



$$
\mathrm{d} q=\rho \mathrm{d} V^{\prime}
$$

上面各式加“'”的原因是只有电荷存在的区间各式才不为零, 因此最终形成的积分只在电荷分 布的源点区间进行,一般并不涉及整个空间的积分计算。由此可得

$$
\mathrm{d} \boldsymbol{E}=\frac{\mathrm{d} q}{4 \pi \varepsilon r^{2}} \boldsymbol{e}_{r}
$$

再通过积分或数值计算等手段求解, 但过程一般较繁, 有兴趣者可参考本科生电磁场教材。

【例 1.6-1】图 1.6-1 中, 点电荷 $q$ 位于 $\left(x^{\prime}, y^{\prime}, z^{\prime}\right)$ 位置, 试求任一场点 $p$ 处的电场强 度。

解: 由向量代数可知,图示各量可表示为

$$
\begin{aligned}
& \boldsymbol{r}^{\prime}=x^{\prime} \boldsymbol{e}_{x}+y^{\prime} \boldsymbol{e}_{y}+z^{\prime} \boldsymbol{e}_{z} \\
& \boldsymbol{r}=x \boldsymbol{e}_{x}+y \boldsymbol{e}_{y}+z \boldsymbol{e}_{z}
\end{aligned}
$$

两点之间的距离为

$$
\left|r-r^{\prime}\right|=\sqrt{\left(x-x^{\prime}\right)^{2}+\left(y-y^{\prime}\right)^{2}+\left(z-z^{\prime}\right)^{2}}
$$

由源点指向场点的单位向量为

$$
\frac{r-r^{\prime}}{\left|r-r^{\prime}\right|}=\frac{\left(x-x^{\prime}\right) e_{x}+\left(y-y^{\prime}\right) e_{y}+\left(z-z^{\prime}\right) e_{z}}{\sqrt{\left(x-x^{\prime}\right)^{2}+\left(y-y^{\prime}\right)^{2}+\left(z-z^{\prime}\right)^{2}}}
$$



故

$$
\boldsymbol{E}=\frac{q}{4 \pi \varepsilon_{0}\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|^{2}} \cdot \frac{\boldsymbol{r}-\boldsymbol{r}^{\prime}}{\left|\boldsymbol{r}-\boldsymbol{r}^{\prime}\right|}
$$

【例 1. 6-2】无限大真空中点电荷 $Q_{A}$ 位于直角坐标系坐标 $(-3,0,0)$ 处, 点电荷 $Q_{B}$ 位于 $(-3,-1,1)$ 处, 试求 $P$ 点 $(2,3,4)$ 处的电场强度。

解: $Q_{A}$ 与 $Q_{B}$ 单独作用产生的电场分别为

$$
\begin{aligned}
& \boldsymbol{E}_{A}=\frac{Q_{A}}{4 \pi \varepsilon_{0}} \cdot \frac{(2+3) \boldsymbol{e}_{x}+3 \boldsymbol{e}_{y}+4 \boldsymbol{e}_{z}}{\left[(2+3)^{2}+3^{2}+4^{2}\right]^{3 / 2}}=\frac{Q_{A}\left(5 \boldsymbol{e}_{x}+3 \boldsymbol{e}_{y}+4 \boldsymbol{e}_{z}\right)}{200 \sqrt{50} \pi \varepsilon_{0}} \\
& \boldsymbol{E}_{B}=\frac{Q_{B}}{4 \pi \varepsilon_{0}} \cdot \frac{(2+3) \boldsymbol{e}_{x}+(3+1) \boldsymbol{e}_{y}+(4-1) \boldsymbol{e}_{z}}{\left[(2+3)^{2}+(3+1)^{2}+(4-1)^{2}\right]^{3 / 2}}=\frac{Q_{B}\left(5 \boldsymbol{e}_{x}+4 \boldsymbol{e}_{y}+3 \boldsymbol{e}_{z}\right)}{200 \sqrt{50} \pi \varepsilon_{0}}
\end{aligned}
$$

合成后得所求电场

$$
\boldsymbol{E}=\boldsymbol{E}_{A}+\boldsymbol{E}_{B}=\frac{1}{200 \sqrt{50 \pi \varepsilon_{0}}}\left[Q_{A}\left(5 \boldsymbol{e}_{x}+3 \boldsymbol{e}_{y}+4 \boldsymbol{e}_{z}\right)+Q_{B}\left(5 \boldsymbol{e}_{x}+4 \boldsymbol{e}_{y}+3 \boldsymbol{e}_{z}\right)\right]
$$

\section{2. 电位}

由于静电场的无旋性, 可引人标量函数 $\varphi$, 有

$$
E=-\nabla_{\varphi}
$$

$\varphi$ 被称为标量电位函数, $\varphi$ 在空间某点的值称为该点的电位。电位的单位为伏特 $(V), \nabla_{\varphi}$ 表 示电位梯度,该定义中的负号表示场强的方向与 $\nabla_{\varphi}$ 的方向相反。

电位的另一种定义式可表示为

$$
\varphi_{P}=\int_{P}^{Q} E \cdot \mathrm{d} \boldsymbol{l}
$$

式中, $\varphi_{P}$ 表示 $P$ 点相对于 $Q$ 点的电位, $Q$ 点是电位的参考点。该式可解析为: $P$ 点的电位等于 在电场力的作用下, 把单位正电荷由 $P$ 点移到参考点 (此处为 $Q$ 点) 时电场力所做的功。此式 

\section{在计算中常被采用。}

两点间电压 $U_{A B}$ 可用电位计算, 即

$$
U_{A B}=\varphi_{A}-\varphi_{B}
$$

电位的参考点可以任意指定。参考点改变,电位的值也随之变化,但任意两点间电压的值 是不变的。静电场是无旋场,电位或电压的计算都与路径无关。参考点一般被取为无穷远处、 大地或金属外壳处。

在无限大均匀介质中, 若取无穷远处作为电位参考点, 则点电荷形成的电位为

$$
\varphi=\frac{q}{4 \pi \varepsilon r}
$$

由 $n$ 个点电荷在场点产生的电位为

$$
\varphi=\frac{1}{4 \pi \varepsilon} \sum_{i=1}^{n} \frac{q_{i}}{r_{i}}
$$

式中 $q_{i}$ 为负电荷时, 应取负值, 而 $r_{i}$ 表示电荷与场点的距离, 恒为正值。

静电场中的导体具有以下特点:

(1)导体内部电场强度为零;

(2)任一导体自身都是一个等位体;

(3)如果导体带电, 电荷只能分布在导体的表面, 而且导体表面处任一点电场强度的方向一 定与导体表面垂直。当导体表面带正电荷时, 电场强度方向向导体外指,否则相反。

【例 1.6-3】无限大真空中, 点电荷 $q_{A}=1 \mathrm{C} 、 q_{B}=2 \mathrm{C} 、 q_{C}=-3 \mathrm{C}$, 各电荷的直角坐标分别 为 $(0,1,1) 、(-1,1,1) 、(1,1,-2)$, 试求场点 $P(1,1,1)$ 位置的电位。

解: 各电荷距离场点的距离分别为

所以

$$
\begin{aligned}
& r_{A}=\sqrt{1^{2}+(1-1)^{2}+(1-1)^{2}}=1 \\
& r_{B}=\sqrt{(1+1)^{2}+(1-1)^{2}+(1-1)^{2}}=2 \\
& r_{C}=\sqrt{(1-1)^{2}+(1-1)^{2}+(1+2)^{2}}=3
\end{aligned}
$$

$$
\varphi_{P}=\frac{1}{4 \pi \varepsilon_{0}}\left(1+\frac{2}{2}+\frac{-3}{3}\right)=\frac{1}{4 \pi \varepsilon_{0}}
$$

【例 1.6-4】已知电位函数 $\varphi=4 x^{2}+3 x y z \mathrm{~V}$, 试求电场强度 $\boldsymbol{E}_{\text {。 }}$

解: 直角坐标系下展开 $\nabla \varphi$ 得

$$
\boldsymbol{E}=-\boldsymbol{\nabla}_{\varphi}=-\frac{\partial \varphi}{\partial x} \boldsymbol{e}_{x}-\frac{\partial \varphi}{\partial y} \boldsymbol{e}_{y}-\frac{\partial \varphi}{\partial z} \boldsymbol{e}_{z}=-(8 x+3 y z) \boldsymbol{e}_{x}-3 x z \boldsymbol{e}_{y}-3 x y \boldsymbol{e}_{z} \mathrm{~V} / \mathrm{m}
$$

若给出场点的具体坐标, 则代人相应的 $x 、 y$ 和 $z$ 值, 即可求出该点的场强。

\section{3. 静电场的基本方程和分界面条件}

掌握静电场的基本方程和分界面条件,是学好静电场的基础。现分别介绍如下。

(1) 基本方程

积分形式

$$
\left\{\begin{array}{l}
\oint_{l} \boldsymbol{E} \cdot \mathrm{d} \boldsymbol{l}=0 \\
\oint_{S} \boldsymbol{D} \cdot \mathrm{d} S=\int_{V} \rho \mathrm{d} V
\end{array}\right.
$$

微分形式

$$
\left\{\begin{array}{l}
\nabla \times E=0 \\
\nabla \cdot D=\rho
\end{array}\right.
$$

式中, $\rho$ 为自由电荷体密度; $\boldsymbol{D}$ 为电位移向量, 又称电通量密度, 单位为库仑 $/$ 米 $^{2}\left(\mathrm{C} / \mathrm{m}^{2}\right)$ 。

由于介质中存在束缚电荷, 在外电场作用下会产生所谓极化现象。电位移向量的一般表 达式为

$$
D=\varepsilon_{0} E+P
$$

式中 $\boldsymbol{P}$ 称极化强度, 与 $\boldsymbol{D}$ 的单位相同, 它反映介质极化的情况。一般而言, 当 $\boldsymbol{D} 、 \boldsymbol{E}$ 和 $\boldsymbol{P}$ 的方 向不相同时,称为各向异性介质,三者方向一致时称为各向同性介质。

对于各向同性介质, $\boldsymbol{D}$ 与 $\boldsymbol{E}$ 的关系可表示为

$$
D=\varepsilon E
$$

$\varepsilon$ 为介质的介电系数。 $\varepsilon$ 通常可表示为

$$
\varepsilon=\varepsilon_{\mathrm{r}} \varepsilon_{0}
$$

$\varepsilon_{\mathrm{r}}$ 称为相对介电系数, $\varepsilon_{0}$ 为真空中介质的介电系数。

当某空间中 $\varepsilon$ 不是电场强度的函数时,该介质称为线性介质。当空间中介电系数与坐标 无关时,称之为均匀介质。

本部分内容限定在讨论各向同性、线性均匀或非均匀媒质中的场。此处非均匀系指空间 存在多种介质,但在每一介质区域范围内, 介质又是均匀的情况。

基本方程表示静电场为无旋度源场,即无旋场,因而空间任一点的电位或任意两点间的电 压的计算将与路径无关。为此,适当地选择计算路径将会简化计算过程,通常选取沿场强方向 和垂直场强 (此时 $\boldsymbol{E} \cdot \mathrm{d} \boldsymbol{l}=0$ ) 的路线计算。静电场的散度不可能处处为零, 有电荷存在的位置 其散度不会是零, 电荷是产生静电场的原因。

任意无旋场都可以用标量电位函数表示, 对于静电场可引人标量电位 $\varphi$, 二者关系为

$$
\boldsymbol{E}=-\nabla \varphi
$$

电位 $\varphi$ 满足泊松方程, 即

$$
\nabla^{2} \varphi=-\rho / \varepsilon
$$

若研究区间无电荷存在, $\varphi$ 满足拉普拉斯方程, 即

$$
\nabla^{2} \varphi=0
$$

泊松方程和拉普拉斯方程都是偏微分方程,必须给出边界条件才可定解。三维方程求解 很繁, 即使二维方程的解析解也往往需要借助分离变量法或复变函数求解。但对一维情况, 其 求解过程一般还是比较方便的。

(2) 分界面条件

在两种介质的分界面处,场量一般要发生变化。假设分界面处取 法向如图 1.6-2 所示, 则由基本方程不难导得

$$
\left\{\begin{array}{l}
E_{1 t}=E_{2 t} \\
D_{2 n}-D_{1 n}=\sigma
\end{array}\right.
$$

式中表示分界面两侧相邻近点的电场强度的切向分量 $E_{1 t}$ 和 $E_{2 t}$ 相等,



用电位表示的分界面条件为

$$
\left\{\begin{array}{l}
\varphi_{1}=\varphi_{2} \\
-\varepsilon_{2} \frac{\partial \varphi_{2}}{\partial n}+\varepsilon_{1} \frac{\partial \varphi_{1}}{\partial n}=\sigma
\end{array}\right.
$$

各向同性介质中,若分界面处无面电荷分布, 则可导得所谓的折射定律, 即

$$
\frac{\tan \alpha_{1}}{\tan \alpha_{2}}=\frac{\varepsilon_{1}}{\varepsilon_{2}}
$$

如果用导体代替第一种介质, 则显然存在 $D_{2 n}=\sigma$, 导体表面的面电荷密度等于电位移 (只存在 法向分量)。反之, 存在 $D_{1 n}=-\sigma$ 。

分界面条件十分重要,它是分析场的分布特点的一条重要理论依据。

\section{(3) 常用术语}

电场线: 为了形象地描述电场, 引入电场线 (电力线) 概念, 电场线是有方向的曲线, 其方 向 (或曲线任一点的切线方向)表示该点场强的方向, 电场线的疏密表示其附近场强的大小。 值得指出的是, 电场线是按一定规则绘制的。

平行平面场:垂直于某一直线的各个平面上的场的分布都一样。

[7午平面场:场中存在一轴线,过轴线的任一半平面上的场的分布都是一样的场。

击穿强度: 介质能够承受的最大电场强度, 超过此值后介质将被击穿, 失去介质性质。

静电独立系统: 系统内的电场不受外部情况影响, 系统内电场也不影响系统外部, 这样的 系统中全部带电体所带有的电荷代数和为零。静电屏蔽可把空间分隔为不同的系统。

孤立带电导体: 有时会碰到孤立导体的电位和电容等提法, 这种提法实际必须考虑无穷远 处存在与之等量异号的电荷。“孤立体带电荷为 $q$, 求空间电场”, 该问题更严密的说法还应加 上在无穷远处存在总电量为 $-q$ 的电荷, 这样才满足静电独立系统。而孤立导体的电容实际 是该导体相对于无穷远处的电容。

\section{4. 常用数学知识}

无论是电场, 还是磁场, 它们都是向量场。电磁场理论涉及的数学知识较多, 掌握好这些 知识是学好电磁场的基础。下面将围绕常用的直角坐标系、圆柱坐标系和球面坐标系三种正 交坐标系做一简单介绍。



\section{(1) 直角坐标系}

直角坐标系中点与向量具有一一对应关系, 图 1.6-3 所示的点 $A$ 和点 $B$ 所对应的向量分别为

$$
\begin{aligned}
& \boldsymbol{R}^{\prime}=x^{\prime} \boldsymbol{e}_{x}+y^{\prime} \boldsymbol{e}_{y}+z^{\prime} \boldsymbol{e}_{z} \\
& \boldsymbol{R}=x \boldsymbol{e}_{x}+y \boldsymbol{e}_{y}+z \boldsymbol{e}_{z}
\end{aligned}
$$

而 $A$ 点与 $B$ 点连线对应的 $\boldsymbol{r}$ 向量为

$$
\boldsymbol{r}=\boldsymbol{R}-\boldsymbol{R}^{\prime}=\left(x-x^{\prime}\right) \boldsymbol{e}_{x}+\left(y-y^{\prime}\right) \boldsymbol{e}_{y}+\left(z-z^{\prime}\right) \boldsymbol{e}_{z}^{\prime}
$$

式中 $e_{x} 、 e_{y}$ 与 $e_{z}$ 分别表示 $x$ 方向 $y$ 方向和 $z$ 方向的单位向 量, 并且存在关系

及

$$
e_{x} \times e_{y}=e_{z}, e_{y} \times e_{z}=e_{x}, e_{z} \times e_{x}=e_{y}
$$



$$
\begin{aligned}
& e_{x} \cdot e_{x}=e_{y} \cdot e_{y}=e_{z} \cdot e_{z}=1 \\
& e_{x} \cdot e_{y}=e_{y} \cdot e_{z}=e_{z} \cdot e_{x}=0
\end{aligned}
$$

必须注意:工程上一般采用右旋坐标系统, 即右手四指由 $x$ 轴经 $90^{\circ}$ 绕至 $y$ 轴,拇指指向应 为 $z$ 轴方向。否则, 上述表达式不正确。

$$
r=|\boldsymbol{r}|=\sqrt{\left(x-x^{\prime}\right)^{2}+\left(y-y^{\prime}\right)^{2}+\left(z-z^{\prime}\right)^{2}}
$$

$r$ 向量的单位向量

$$
e_{r}=\frac{r}{|r|}=\frac{\left(x-x^{\prime}\right) e_{x}+\left(y-y^{\prime}\right) e_{y}+\left(z-z^{\prime}\right) e_{z}}{\sqrt{\left(x-x^{\prime}\right)^{2}+\left(y-y^{\prime}\right)^{2}+\left(z-z^{\prime}\right)^{2}}}
$$

对于任一标量函数 $g(x, y, z)$, 其梯度为

$$
\operatorname{grad} g(x, y, z)=\frac{\partial g}{\partial x} \boldsymbol{e}_{x}+\frac{\partial g}{\partial y} \boldsymbol{e}_{y}+\frac{\partial g}{\partial z} \boldsymbol{e}_{z}
$$

若引人那勃勒算子符号 $\boldsymbol{\nabla}$, 即

$$
\boldsymbol{\nabla}=\frac{\partial}{\partial x} \boldsymbol{e}_{x}+\frac{\partial}{\partial y} \boldsymbol{e}_{y}+\frac{\partial}{\partial z} \boldsymbol{e}_{z}
$$

则可得

$$
\operatorname{grad} g=\nabla g
$$

任一向量场 $\boldsymbol{A}(x, y, z)$ 的散度表示场的散度源, 其计算式为

$$
\operatorname{div} \boldsymbol{A}(x, y, z)=\frac{\partial A_{x}}{\partial x}+\frac{\partial A_{y}}{\partial y}+\frac{\partial A_{z}}{\partial z}
$$

或记为

$$
\operatorname{div} \boldsymbol{A}=\boldsymbol{\nabla} \cdot \boldsymbol{A}
$$

散度值为一标量。

任一向量场 $A(x, y, z)$ 的旋度表示场的旋度源, 其计算公式为

$$
\operatorname{curl} \boldsymbol{A}(x, y, z)=\left(\frac{\partial A_{z}}{\partial y}-\frac{\partial A_{y}}{\partial z}\right) \boldsymbol{e}_{x}+\left(\frac{\partial A_{x}}{\partial z}-\frac{\partial A_{z}}{\partial x}\right) \boldsymbol{e}_{y}+\left(\frac{\partial A_{y}}{\partial x}-\frac{\partial A_{x}}{\partial y}\right) \boldsymbol{e}_{z}
$$

或记为

$$
\operatorname{curl} A=\nabla \times A
$$

旋度值为一向量。

直角坐标系中拉普拉斯算子为

$$
\nabla^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}
$$

在梯度、散度和旋度的计算中,引人那勃勒算子后可使表达式简洁,并且它们遵从向量点 乘或叉乘的法则。

(2) 圆柱坐标系

将直角坐标系中 $x O y$ 平面的 $x$ 和 $y$ 坐标采用极坐标 $r$ 和 $\alpha$ 表示,则形成圆柱坐标系。其 中 $r$ 为与 $z$ 轴的距离, $\alpha$ 表示拇指指向 $z$ 轴时,四指由 $x$ 轴开始绕过的角度。

圆柱坐标系与直角坐标系不同,它的三个方向除 $z$ 轴方向固定不变外, $r$ 和 $\alpha$ 的方向均随 空间坐标位置的变化而变化,因此在向量叠加时将会遇到困难,其中尤以 $e_{\alpha}$ 方向最难表示。

考虑这是正交坐标系,则应用 

$$
e_{z} \times e_{r}=e_{\alpha}
$$

很容易将 $e_{\alpha}$ 用 $e_{z}$ 和 $e_{r}$ 表示, 而 $e_{r}$ 也可方便地用直角坐标表示, 即

$$
e_{r}=\cos \alpha e_{x}+\sin \alpha e_{y}
$$

这样在需要的时候, 都可以方便地转化为直角坐标系中的分量,叠加计算就十分方便了。

圆柱坐标系中的梯度计算公式为

$$
\nabla g(x, y, z)=\frac{\partial g}{\partial r} e_{r}+\frac{1 \partial g}{r \partial \alpha} e_{\alpha}+\frac{\partial g}{\partial z} e_{z}
$$

散度计算公式为

$$
\boldsymbol{\nabla} \cdot \boldsymbol{A}(x, y, z)=\frac{1 \partial}{r \partial r}(r A r)+\frac{1 \partial A_{\alpha}}{r \partial \alpha}+\frac{\partial A_{z}}{\partial z}
$$

旋度计算式为

$$
\boldsymbol{\nabla} \times \boldsymbol{A}=\left(\frac{1 \partial A_{z}}{r \partial \alpha}-\frac{\partial A_{\alpha}}{\partial z}\right) \boldsymbol{e}_{r}+\left(\frac{\partial A_{r}}{\partial z}-\frac{\partial A_{z}}{\partial r}\right) \boldsymbol{e}_{\alpha}+\frac{1}{r}\left[\frac{\partial}{\partial r}\left(r A_{\alpha}\right)-\frac{\partial A_{r}}{\partial \alpha}\right] \boldsymbol{e}_{z}
$$

$\nabla^{2} g(x, y, z)$ 的展开式为

$$
\nabla^{2} g(x, y, z)=\frac{1 \partial}{r \partial r}\left(r \frac{\partial g}{\partial r}\right)+\frac{1 \partial^{2} g}{r^{2} \partial \alpha^{2}}+\frac{\partial^{2} g}{\partial z^{2}}
$$

(3) 球面坐标系

球面坐标系坐标变量为 $r 、 \alpha$ 和 $\theta, r$ 为点到坐标原点的距离, $\alpha$ 为 $r$ 在 $x O y$ 平面上投影与 $x$ 轴间的夹角, $\theta$ 为 $r$ 与 $z$ 轴间的夹角。

球面坐标系适合辐射对称场的计算,例如点电荷或球面均匀分布电荷等在无限大均匀媒 质中形成的电场的计算。

球面坐标系中标量函数 $g(x, y, z)$ 的梯度计算公式为

$$
\nabla g(x, y, z)=\frac{\partial g}{\partial r} e_{r}+\frac{1 \partial g}{r \partial \theta} e_{\theta}+\frac{1}{r \sin \theta \partial \alpha} e_{\alpha}
$$

其散度和梯度公式较繁, 这里从略。

在实际计算中,常会遇到多个场源同时存在的情况,例如后面碰到的二线输电线等问题， 一开始就把问题放在一个统一的坐标系中进行计算,往往会造成式子十分庞大,而对不同场源 分别选取不同的坐标系表示往往步骤十分简单,如果需要的话,最后再用统一的坐标变量给 出,往往会有利于求解过程的简化。

值得指出的是: 本部分内容涉及的积分并不复杂, 大量问题涉及的仅是 $\frac{1}{r}$ 或 $\frac{1}{r^{2}}$ 的积分。更 复杂的积分是存在的,但由于过程十分复杂, 这里不再列举了。

1.6.2 用高斯定律计算具有对称性分布的静电场问题

高斯定律的一般形式为

$$
\oint_{S} D \cdot d S=\oint_{V} \rho \mathrm{d} V
$$

高斯定律是静电场的基本定律之一,该定律将场源即电荷与场量联系在一起。在任意闭 合曲面上,电位移向量的面积分恒等于该闭合曲面内所有自由电荷的代数和。该公式的计算 不需要考虑束缚电荷, 因此使用十分方便。

电位移向量在闭合面上的面积分与介质分布无关,这并不说明电位移的分布与介质无关。 例如空气介质圆柱电容器, 当内外导体所带电荷量为固定值时, 整个内导体单位长度所带电荷 也为定值, 此时在此电容器注人一定的液态电介质, 则导体所带电荷将重新分布, 同时电场会 变化。

在各向同性线性介质中,存在关系式

$$
D=\varepsilon E
$$

因此,通过高斯定律求得 $\boldsymbol{D}$, 则电场强度不难计算, 介电系数 $\varepsilon$ 通常都是已知的。

利用高斯定律可以方便地求得某些对称电场, 而判断电场的对称性则依赖于电荷与媒质 分布的特点。

\section{1. 辐射对称场}

辐射对称场表现为其场量仅是球面坐标系中 $r$ 的函数,其场源往往是点、球面、球壳或球 体等分布电荷, 周围介质分布也不会与球坐标系中的角度相关。

最简单的辐射对称场是由点电荷和带电金属球 (实心或空心) 在无限大均匀介质中产生 的电场。若金属球所带电量为 $q$, 金属球的半径为 $R$, 则金属球内的场强将为零, 金属球外的场 强

$$
\boldsymbol{E}=\frac{q}{4 \pi \varepsilon r^{2}} e_{r} \quad(r \geqslant R)
$$

若设无穷远处为电位参考点, 则

$$
\varphi=\int_{r}^{\infty} E \cdot \mathrm{d} r=\int_{r}^{\infty} \frac{q}{4 \pi \varepsilon r^{2}} e_{r} \cdot e_{r} \mathrm{~d} r=\frac{q}{4 \pi \varepsilon r} \quad(r \geqslant R)
$$

金属球的电位等于球面的电位, 为一定值, 即

$$
\varphi=\frac{q}{4 \pi \varepsilon R}
$$

下面是几个典型辐射对称场的计算实例。

【例 1. 6-5】 无限大真空中同心金属球壳的尺寸如图 1.6-4 所示, 它们分别带有电量 $q_{1}$ 和 $q_{2}$, 试求各点的电场强度和电位。

解: 由于介质分布的对称性, $q_{1}$ 将均匀分布在内导体球的外表面 处, 而半径为 $R_{2}$ 的球壳内表面将均匀分布有总电量为 $-q_{1}$ 的电荷, $q_{1}$ $+q_{2}$ 均匀分布在半径为 $R_{3}$ 的球壳外表面处。

以球心为半径的任一闭合球面上, 电位移的大小将相等,其方向与 e,方向一致。故高斯定律可表示为

$$
D \cdot 4 \pi r^{2}=\Sigma q
$$

再考虑 $\boldsymbol{D}=\varepsilon_{0} \boldsymbol{E}$, 则得解答



$$
\begin{aligned}
& E=0 \quad\left(r<R_{1} \text { 及 } R_{2}<r<R_{3}\right) \\
& \boldsymbol{E}=\frac{q_{1}}{4 \pi \varepsilon_{0} r^{2}} e_{r} \quad\left(R_{1} \leqslant r \leqslant R_{2}\right) \\
& \boldsymbol{E}=\frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} r^{2}} e_{r} \quad\left(r \geqslant R_{3}\right)
\end{aligned}
$$

若设无穷远处电位为零, 则 

$$
\begin{aligned}
& \varphi=\int_{l} \boldsymbol{E} \cdot \mathrm{d} \boldsymbol{l}=\int_{r}^{\infty} \frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} r^{2}} \mathrm{~d} r=\frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} r} \quad\left(r \geqslant R_{3}\right) \\
& \varphi=\int_{r}^{R_{2}} \frac{q_{1}}{4 \pi \varepsilon_{0} r^{2}} \mathrm{~d} r+\int_{R_{3}}^{\infty} \frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} r^{2}} \mathrm{~d} r=\frac{q_{1}}{4 \pi \varepsilon_{0}}\left(\frac{1}{r}-\frac{1}{R_{2}}\right)+\frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} R_{3}} \quad\left(R_{1} \leqslant r \leqslant R_{2}\right)
\end{aligned}
$$

外球壳的电位

$$
\varphi=\frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} R_{3}}
$$

内球体的电位

$$
\varphi=\frac{q_{1}}{4 \pi \varepsilon_{0}}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)+\frac{q_{1}+q_{2}}{4 \pi \varepsilon_{0} R_{3}}
$$

若此题 $q_{1}=-q_{2}$, 则 $r \geqslant R_{3}$ 处 $\boldsymbol{E}$ 将等于 0 , 而外球壳的电位也将变为 0 。



【例 1.6-6】图 1.6-5 为一双层介质的球形电容器, 若内外导 体间施加电压 $U_{0}$, 试求介质中的电场强度。

解:这是一个辐射对称场。设内导体所带电量为 $q$, 则由高斯 定律可求得

$$
\begin{aligned}
\boldsymbol{E}_{1} & =\frac{q}{4 \pi \varepsilon_{1} r^{2}} e_{r} \quad\left(R_{1}<r<R_{2}\right) \\
\boldsymbol{E}_{2} & =\frac{q}{4 \pi \varepsilon_{2} r^{2}} e_{r} \quad\left(R_{2}<r<R_{3}\right) \\
U_{0} & =\int_{R_{1}}^{R_{2}} \boldsymbol{E}_{1} \cdot \mathrm{d} \boldsymbol{r}+\int_{R_{2}}^{R_{3}} \boldsymbol{E}_{2} \cdot \mathrm{d} \boldsymbol{r} \\
& =\frac{q}{4 \pi \varepsilon_{1}}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)+\frac{q}{4 \pi \varepsilon_{2}}\left(\frac{1}{R_{2}}-\frac{1}{R_{3}}\right)
\end{aligned}
$$

由此可得

$$
\frac{q}{4 \pi}=\frac{U_{0}}{\frac{1}{\varepsilon_{1}}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)+\frac{1}{\varepsilon_{2}}\left(\frac{1}{R_{2}}-\frac{1}{R_{3}}\right)}
$$

将上式代人 $\boldsymbol{E}_{1}$ 和 $\boldsymbol{E}_{2}$ 二式,即为用 $U_{0}$ 表示的二介质中的场强。

【例 1. 6-7】介电系数为 $\varepsilon_{0}$ 的无限大均匀介质中,在半径 $r \leqslant R$ 的球形域中均匀分布着体 密度为 $\rho$ (常数) 的电荷, 试求空间任一点处的电场强度和电位。

解:介质与电荷分布均满足辐射对称,可用高斯定律求解。

当 $r \leqslant R$ 时

$$
\begin{aligned}
& D \cdot 4 \pi r^{2}=\int_{\rho}^{r} \rho 4 \pi r^{2} \mathrm{~d} r=\rho \frac{4}{3} \pi r^{3} \\
& \boldsymbol{E}=\frac{\boldsymbol{D}}{\varepsilon}=\frac{\rho r}{3 \varepsilon_{0}} e_{r}
\end{aligned}
$$

当 $r>R$ 时

$$
\begin{aligned}
& D \cdot 4 \pi r^{2}=\rho \frac{4}{3} \pi R^{3} \\
& \boldsymbol{E}=\frac{\rho R^{3}}{3 \varepsilon_{0} r^{2}} e_{r}
\end{aligned}
$$

设无穷远处电位为零, 则

$$
\begin{aligned}
& \varphi=\int_{,}^{\infty} \frac{\rho R^{3}}{3 \varepsilon_{0} r^{2}} \mathrm{~d} r=\frac{\rho R^{3}}{3 \varepsilon_{0} r} \quad(r>R) \\
& \varphi=\int_{,}^{R} \frac{\rho r}{3 \varepsilon_{0}} \mathrm{~d} r+\int_{R}^{\infty} \frac{\rho R^{3}}{3 \varepsilon_{0} r^{2}} \mathrm{~d} r=\frac{\rho}{6 \varepsilon_{0}}\left(R^{2}-r^{2}\right)+\frac{\rho R^{2}}{3 \varepsilon_{0}}=\frac{\rho R^{2}}{2 \varepsilon_{0}}-\frac{\rho r^{2}}{6 \varepsilon_{0}} \quad(r \leqslant R)
\end{aligned}
$$

\section{2. 平面辐射对称场}

在圆柱坐标系 $(r, \alpha, z)$ 中, 如果场量仅与 $r$ 相关, 即在半径为 $r$ 的圆柱面上, 场量的大小都 相等, 方向也仅是 $\boldsymbol{e}_{r}$ 方向, 这种场可称为平面辐射对称场。应用高斯定律时, 可做一同轴圆柱 面, 其上下二底面由于场量方向 $e_{r}$ 与面的外法向垂直而构不成通量, 它的侧表面上场量与表 面外法向一致而又大小相等, 因此高斯定律左端变成场量大小与侧表面面积的乘积, 从而可以 方便地求得场。这种场的场源一般表现为无限大均匀媒质或分层圆柱对称介质中的无限长均 匀分布的线电荷、圆柱面电荷或圆柱体电荷。

如果在无限大均匀介质中存在一无限长均匀分布的线密度为 $\tau$ 的线电荷, 则以线电荷所 在位置为 $z$ 轴, 任意半径 $r$ 处的电场强度值为

$$
E=\frac{\tau}{z \pi \varepsilon r} e_{r}
$$

必须注意: 这种电荷分布在求电位分布时, 不能将参考点取在无穷远处。

【例 1. 6-8】长为 $L$ 的圆柱形电容器, 内外导体的半径分别为 $R_{1}$ 和 $R_{2}$, 导体之间填充介 电系数为 $\varepsilon$ 的介质, 若在二导体间施加电压 $U_{0}$, 试求内导体上所带的电荷 (忽略边缘效应)。

解: 忽略边缘效应即表示该问题可以按无限长圆柱体计算。设内导体单位长所带电量为 $\tau$, 则 $R_{1} \leqslant r \leqslant R_{2}$ 区间存在

$$
E=\frac{\tau}{2 \pi \varepsilon r} e_{r}
$$

内外导体间电压

$$
U_{0}=\int_{R_{1}}^{R_{2}} \frac{\tau}{2 \pi \varepsilon r} \mathrm{~d} r=\frac{\tau}{2 \pi \varepsilon} \ln \frac{R_{2}}{R_{1}}
$$

内导体所带电荷量

$$
q=\tau \cdot L=\frac{2 U_{0} \pi \varepsilon L}{\ln \frac{R_{2}}{R_{1}}}
$$

【例 1. 6-9】无限长圆柱区间均匀分布电荷体密度为 $\rho$ 的电荷, 设周围介质的介电系数 为 $\varepsilon_{0}$, 试求空间任一点处的电场强度 (如图 1.6-6 所示)。

解:用高斯定律求解,分柱内与柱外两部分 (柱外包围电荷为定 值)。取单位长度圆柱面, 则 $0 \leqslant r \leqslant R$ 时, 有

$$
\begin{aligned}
& D \cdot 2 \pi r=\rho \cdot \pi r^{2} \\
& \boldsymbol{E}=\frac{\rho r}{2 \varepsilon_{0}} e_{r}
\end{aligned}
$$

$r>R$ 时, 有

$$
D \cdot 2 \pi r=\rho \cdot \pi R^{2}
$$



$$
\boldsymbol{E}=\frac{\rho R^{2}}{2 \varepsilon_{0} r} e_{r}
$$

【例 1. 6-10】双层介质的同轴电缆横断面如图 1.6-7 所示, 当内外导体间施加电压 $U_{0}$ 时, 试求电缆内的电位分布 (设导体外皮电位为 0 )。



解: 同轴电缆一般都可视为无限长, 故可用高斯定律求解。设内导 体单位长所带电荷为 $\tau$, 则

$$
\begin{aligned}
& \boldsymbol{E}=\frac{\tau}{2 \pi \varepsilon_{1} r} e_{r} \quad\left(R_{1}<r<R_{2}\right) \\
& \boldsymbol{E}=\frac{\tau}{2 \pi \varepsilon_{2} r} e_{r} \quad\left(R_{2}<r<R_{3}\right) \\
& U_{0}=\int_{R_{1}}^{R_{2}} \frac{\tau}{2 \pi \varepsilon_{1} r} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} \frac{\tau}{2 \pi \varepsilon_{2} r} \mathrm{~d} r=\frac{\tau}{2 \pi \varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{\tau}{2 \pi \varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}
\end{aligned}
$$

由此可解出

$$
\begin{aligned}
& \tau=\frac{U_{0}}{\frac{1}{2 \pi \varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{2 \pi \varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}} \\
& \varphi=\int_{r}^{R_{3}} \frac{\tau}{2 \pi \varepsilon_{2} r} \mathrm{~d} r=\frac{\tau}{2 \pi \varepsilon_{2}} \ln \frac{R_{3}}{r} \quad\left(R_{2} \leqslant r \leqslant R_{3}\right) \\
& \varphi=\int_{,}^{R_{2}} \frac{\tau}{2 \pi \varepsilon_{1} r} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} \frac{\tau}{2 \pi \varepsilon_{2} r} \mathrm{~d} r=\frac{\tau}{2 \pi \varepsilon_{1}} \ln \frac{R_{2}}{r}+\frac{\tau}{2 \pi \varepsilon_{2}} \ln \frac{R_{3}}{R_{2}} \quad\left(R_{1} \leqslant r \leqslant R_{2}\right)
\end{aligned}
$$

将 $\tau$ 值代人, 即可得到以 $U_{0}$ 表示的电位值。

\section{3. 面对称场}


$$
\begin{aligned}
& \boldsymbol{E}=\frac{\sigma}{2 \varepsilon} \boldsymbol{e}_{x} \quad(x>0) \\
& \boldsymbol{E}=-\frac{\sigma}{2 \varepsilon} \boldsymbol{e}_{x} \quad(x<0)
\end{aligned}
$$



面对称场通常处于无限大均匀媒质中, 其场强只与直角坐标系中一个变量相关。



【例 1. 6-11】 二无限大均匀带电面电荷空间位置如图1.6-9所示, 试求空间各点处的电场强度 (设介质的介电系数为 $\varepsilon_{0}$ )。

解: 利用静电场的叠加定理,让两个电荷各自单独作用,由于它们 带等量异号的电荷, 故

$$
\begin{aligned}
& \boldsymbol{E}=\frac{\sigma}{\varepsilon_{0}} \boldsymbol{e}_{x} \quad(-d<x<d) \\
& \boldsymbol{E}=0 \quad(|x|>d)
\end{aligned}
$$

【例 1. 6-12】在无限大真空中, $|z| \leqslant d$ 的空间分布有体密度为 $\rho$ 的均匀电荷, 试求空间 各点的电场强度。

解: 为分析方便, 作图 1. 6-10。 由面动得体可知,该体电荷可以看成无穷多个与 $z$ 轴垂直的 面电荷组成, 由对称性不难理解, $x O y$ 平面上的场强为零。在 $|z|>d$ 或 $|z| \leqslant d$ 的区间, 电场强度只具有 $z$ 方向值。

在 $x O y$ 平面上作一边长等于 $1 \mathrm{~m}$ 的正方形,取高为 $|z|$,构成 一立方体,则仅在 $z \neq 0$ 的平面上场强构成通量,由高斯定律可得 $-d \leqslant z \leqslant d$ 时

$$
\boldsymbol{E}=\frac{\rho z}{\varepsilon_{0}} \boldsymbol{e}_{z}
$$



$z>d$ 时

$$
E=\frac{\rho d}{\varepsilon_{0}} e_{z}
$$

$2<-d$ 时

$$
E=-\frac{\rho d}{\varepsilon_{0}} e_{z}
$$

类似此例题, 许多种体电荷组合也可以通过上述方法进行分析计算。即使 $\rho$ 不是常数, 只 要 $\rho$ 仅仅是 $z$ 的函数, 也可以仿照上述方法进行计算, 不过电荷的计算却要通过积分方可求 得。

必须指出, 以上计算都是在无限大均匀介质条件下进行的, 如果场中存在导体, 则分析将 困猚得多,甚至无法求出解析表达式。

\section{4. 场的叠加性}

线性媒质中, 电荷形成的场可用叠加方法进行计算。但必须注意, 电荷可以单独作用, 而 周围媒质却必须保持不变。



典型实例之一是计算二线输电线的电场。设导线半径等 于 $a$ 的两根平行架设的长直圆截面导线带有等量异号电荷, 如 图 1. 6-11 所示。假如二线间距离远大于导线半径, 即可用叠 加法计算。

导线很长, 可以视为平行平面场, 即忽略边缘效应, 这在工 程上是允许的。垂直输电线任取一平面坐标系如图 1. 6-11 所 示,由于导线截面积很小,因此忽略其对介质均匀性的破坏是 合理的。当 $\tau$ 与 $-\tau$ 单独作用时, 其各自形成的电场均以各自

中心对称, 故

$$
\boldsymbol{E}=\frac{\tau}{2 \pi \varepsilon_{0} r_{1}} e_{r 1}+\frac{-\tau}{2 \pi \varepsilon_{0} r_{2}} e_{r 2}
$$

如果一定要写成坐标统一的变量表示, 则可代人

$$
\begin{aligned}
& \frac{\boldsymbol{e}_{r 1}}{r_{1}}=\frac{\boldsymbol{r}_{1}}{r_{1}^{2}}=\frac{(x-b) \boldsymbol{e}_{x}+y \boldsymbol{e}_{y}}{(x-b)^{2}+y^{2}} \\
& \frac{\boldsymbol{e}_{r 2}}{r_{2}}=\frac{\boldsymbol{r}_{2}}{r_{2}^{2}}=\frac{(x+b) \boldsymbol{e}_{x}+y \boldsymbol{e}_{y}}{(x+b)^{2}+y^{2}}
\end{aligned}
$$

由于 $y O z$ 平面距二线距离相等, 而 $\tau$ 与 $-\tau$ 在该面上产生的电位合成后必为零, 故可设 $y$ 轴电位为参考电位, 通过推导, 不难得出此时任一场点的电位 

$$
\varphi=\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{r_{2}}{r_{1}}=\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{\sqrt{(x+b)^{2}+y^{2}}}{\sqrt{(x-b)^{2}+y^{2}}}
$$

最后应当指出的是: 导线中的电场应为 0 , 而两根导线的电位也各自为定值, 上述公式只 适合计算导线外部场, 导线电位可通过代人导体表面处任一点的坐标求得, 最方便的点是导线 与 $x$ 轴相交的点。

顺便指出,当空间具有多对平行架设的输电线时, 只要导线截面对介质均匀性的破坏可以 忽略, 即可利用上述公式一一叠加。要注意的是, 电场强度应按向量叠加, 而电位是标量叠加。

\subsection{3 静电场边值问题的镜像法和电轴法}

对于均匀介质, 静电场满足泊松方程

$$
\nabla^{2} \varphi=-\frac{\rho}{\varepsilon}
$$

如果研究的区间无电荷, 即 $\rho=0$,则满足拉普拉斯方程

$$
\nabla^{2} \varphi=0
$$

式中拉普拉斯算子 $\nabla^{2}$ 在直角坐标系中的展开式为

$$
\nabla^{2}=\frac{\partial^{2}}{\partial x^{2}}+\frac{\partial^{2}}{\partial y^{2}}+\frac{\partial^{2}}{\partial z^{2}}
$$

静电场中电位函数与时间无关, 其积分常数要依靠边界条件确定。可以证明, 满足边界条 件的泊松方程或拉普拉斯方程的解答是唯一的,这就是静电场问题中的解答唯一性定理。

静电场的边界条件主要分为三类:第一类是已知各导体的电位; 第二类是已知各导体表面 上的电荷面密度 $\sigma$, 由于 $\sigma=-\varepsilon \frac{\partial \varphi}{\partial n}$, 故也可以说已知各导体表面上电位的法向导数; 第三类 问题是由上述两类组合而成的所谓混合边界条件, 即已知某些导体的电位, 而另一些导体已知 的是电位在其表面处的法向导数。

最简单的边值问题计算是一维问题，此时泊松方程或拉普拉斯方程简化为常微分方程。 这一类问题的求解有时是十分方便的。



例如图 1. 6-12 所示的平板电容器, 中间介质为均匀介质, 其介电 系数为 $\varepsilon_{0}$, 二极板间分布有体密度为 $\rho$ 的均匀分布电荷, 极板间电压 为 $U_{00}$ 。欲求该电容器内部的场, 可以通过高斯定律求解, 但如此求解 需假设二极板上带有面电荷 $\sigma_{A}$ 和 $\sigma_{B}$, 且 $\sigma_{A}$ 不一定等于 $\sigma_{B}$, 显然这 样做并不方便。如果用泊松方程求解,则可以写出

$$
\frac{\mathrm{d}^{2} \varphi}{\mathrm{d} x^{2}}=-\rho / \varepsilon_{0}
$$

积分两次可得方程通解为

$$
\varphi=-\frac{\rho}{2 \varepsilon_{0}} x^{2}+C_{1} x+C_{2}
$$

$C_{1}$ 和 $C_{2}$ 为待定的积分常数。

假如设 $A$ 极板的电位为零 (参考点), 则边界条件为

$$
\begin{aligned}
& \left.\varphi\right|_{x=0}=0 \\
& \left.\varphi\right|_{x=d}=-U_{0}
\end{aligned}
$$

代人通解可得 $C_{1}$ 和 $C_{2}$ 分别为

$$
C_{2}=0, C_{1}=\frac{-U_{0}}{d}+\frac{\rho d}{2 \varepsilon_{0}}
$$

因此

$$
\varphi=-\frac{\rho}{2 \varepsilon_{0}} x^{2}+\left(\frac{-U_{0}}{d}+\frac{\rho d}{2 \varepsilon_{0}}\right) x
$$

电场强度可通过电位梯度求解, 即

$$
E=-\nabla_{\varphi}=-\frac{\mathrm{d} \varphi_{1}}{\mathrm{~d} x} \boldsymbol{e}_{x}=\left(\frac{\rho}{\varepsilon_{0}} x+\frac{U_{0}}{d}-\frac{\rho d}{2 \varepsilon_{0}}\right) \boldsymbol{e}_{x}
$$

由分界面条件可得极板上电荷面密度为

$$
\begin{aligned}
& \sigma_{A}=\left.D\right|_{x=0}=\left.\varepsilon_{0} E\right|_{x=0}=\frac{\varepsilon_{0} U_{0}}{d}-\frac{\rho d}{2} \\
& \sigma_{B}=-\left.D\right|_{x=d}=-\left.\varepsilon_{0} E\right|_{x=d}=-\frac{\varepsilon_{0} U_{0}}{d}-\frac{\rho d}{2}
\end{aligned}
$$

显然, 此时 $\sigma_{A} \neq-\sigma_{B}$ 。如果设极板面积为 $S$, 不难验证下式成立:

$$
\left(\sigma_{A}+\sigma_{B}\right) S+\rho S d=0
$$

\section{1. 镜像法}

镜像法是求解静电场边值问题解的一种间接方示, 其理论依据是静电场解答的唯一性定 理。

该方法的特点是在保持待求场域电荷分布、边界条件和媒质不变的条件下,把边界(或两 种介质分界面) 上复杂分布电荷的作用, 用待求场域外的简单分布电荷来代替, 从而变成无限 大均匀媒质中的无边界问题。

(1) 电荷对无限大导电平面的镜像

位于介质 $\varepsilon$ 中的点电荷 $q$ (如图 1.6-13(a)) 相对无 穷大导电平面的镜像电荷, 恰放置在相对平面对称的位 置,其计算模型如图 1.6-13(b) 所示,有效计算区为原 电荷所在的上半区间, 而 $-q$ 所在的下半区间原来对应 的是导体下方, 这里无电场, 不能用图示的模型计算。





由电荷形成场的叠加性, 多个点电荷、线电荷甚至任意分布的体电荷都可以根据上述方法 找到其相对于无限大导电平面的镜像。如果电荷分布比较复杂时, 就是找到镜像电荷也很难 计算。

【例 1. 6-13】无限大导电平面上方有一对与平面平行架设的二线输电线 (如图 1. 6-14 (a) 所示), 分别带有等量异号电荷 $\tau$ 与 $-\tau$, 试求任一场点 $P$ 处的电位。

解:利用镜像法, 可得图 1.6-14(b) 的计算模型, 由此形成两对输电线, 取 $y$ 轴为电位参考 点,则

$$
\varphi_{p}=\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{r_{2}}{r_{1}}+\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{r_{2}^{\prime}}{r_{1}^{\prime}}
$$

利用两点间距离公式,很容易求得 $r_{1} 、 r_{2} 、 r_{1}^{\prime}$ 和 $r_{2}^{\prime}$ 的坐标表达式, 这里从略。 






【例 1. 6-14】试给出利用镜像法计算图 1. 6-15(a) 和 (b) 两图形表示的无限大导电平面 构成的二面角内置以电荷的计算模型。






解: 除电荷所在位置外, 介质中电位满足

$$
\nabla^{2} \varphi=0
$$

可设导电平面电位为零, 由此可得图 1.6-16 的计算模型。






根据此例题, 如果无限大导电二面角的角度为 $\frac{\pi}{n}$, 则总可以找到合适的镜像, 而 $n$ 必须是 正整数。

无限大导电平面求得的所有镜像电荷的代数和,一般等于导电平面上分布的电荷总量。 （2）点电荷对导体球的镜像

如果导体球接地, 并且地面距导体球很远, 在导体球附近有一点电荷 $q$ (如图 1.6-17(a)), 由于导体球电位与无穷远等电位, 故可设为 0 , 此时只要在球内关于点电荷的反演点处设置适 当的电荷,即可满足边界条件(图 1.6-17(b)), 即

$$
q^{\prime}=\frac{R}{d} q
$$

而

$$
b \cdot d=R^{2}
$$






假如导体球不接地,导体球面应是一个等位面。此时计算球外的场时,必须在图 1. 6-17 (b) 的球心处置以正 $q^{\prime}$ 。如果导体球原来就带有电荷 $Q$, 则置于球心处的电荷应改为 $Q+q^{\prime}$ 。

当问题反过来思考, 即在接地的空心金属壳内置一点电荷时 (如图 1.6-18(a)), 显然这是 静电屏蔽问题, 球壳外电场强度为零。金属球壳的内表面将感应有与点电荷等量而异号的总 电荷, 此时的计算区域为球壳内, 其计算模型如图 1. 6-18(b) 所示, 由于 $b$ 和 $q^{\prime}$ 的位置意义不 同,此时将存在






$$
q^{\prime}=\frac{R}{d} q
$$

而

$$
b \cdot d=R^{2}
$$

如果金属球壳不接地, 而原来球壳又没带电荷, 则球壳内的电场强度仍如接地时一样计 算,但此时球壳外存在电场, 此电场是由金属壳外表面均匀分布的面电荷形成的, 电荷总量为 $q$, 而不是 $q^{\prime}$, 可用高斯定律直接计算

$$
E=\frac{q}{4 \pi \varepsilon_{0} r^{2}} e_{r} \quad(r \geqslant R)
$$

点电荷对金属球得到的镜像电荷, 只表示对有效计算区域代替边界上复杂分布电荷的作 用, 而不代表这些电荷的总量。例如在图 1.6-18 中, 由于 $R>d$, 显然 $\left|q^{\prime}\right|>|q|$, 而球壳内表面 的感应电荷总量却是 $-q$, 况且当 $d$ 变化而 $q$ 不变时, $q^{\prime}$ 变化而球壳内表面感应的电荷总量不 变。

【例 1. 6-15】如图 1.6-19 所示, 空气中一金属球接地 (地在很远处), 过球心一直线上有 等量异号两电荷位于球外,试求球外表面 $A$ 点的场强。





解: $b=\frac{R^{2}}{d}=\frac{1}{2} R$

$$
Q^{\prime}=\frac{R}{d} Q=\frac{1}{2} Q
$$

设 $A$ 点向右垂直金属球方向为 $\boldsymbol{e}_{x}$ 方向, 由图 1.6-20 可得

$$
\begin{aligned}
\boldsymbol{E}_{\text {A }} & =\left[\frac{-Q}{4 \pi \varepsilon_{0}(3 R)^{2}}+\frac{\frac{1}{2} Q}{4 \pi \varepsilon_{0}\left(\frac{3}{2} R\right)^{2}}+\frac{-\frac{1}{2} Q}{4 \pi \varepsilon_{0}\left(\frac{1}{2} R\right)^{2}}+\frac{-Q}{4 \pi \varepsilon_{0} R^{2}}\right] e_{x} \\
& =-\frac{26 Q}{36 \pi \varepsilon_{0} R^{2}} e_{x}=-\frac{13 Q}{18 \pi \varepsilon_{0} R^{2}} e_{x}
\end{aligned}
$$

(3) 电荷对无限大介质平面分界面的镜像

设两种介质的分界面是一无限大平面, 在 $\varepsilon_{1}$ 介质中置一点电荷 $q$, 位置如图 1.6-21(a) 所 示。该模型产生的场可通过图 (b) 和图 (c) 分别求得。图中








$$
\begin{aligned}
& q^{\prime}=\frac{\varepsilon_{1}-\varepsilon_{2}}{\varepsilon_{1}+\varepsilon_{2}} q \\
& q^{\prime \prime}=\frac{2 \varepsilon_{2}}{\varepsilon_{1}+\varepsilon_{2}} q
\end{aligned}
$$

如果用线密度为 $\tau$ 的线电荷代替图中 $q$, 则计算式中只是将 $q^{\prime}$ 和 $q^{\prime \prime}$ 换上 $\tau^{\prime}$ 和 $\tau^{\prime \prime}$ 即可。类 似地依据叠加特性,还可以建立其他的计算模型。

【例1.6-16】电场模型如图 1.6-22 所示, 试求点电荷与边界距离一半处的 $A$ 点及其对称 于分界面的 $B$ 点的电位。








解:利用镜像法分别得到图 1.6-23(a) 和 (b) 的计算模型。设无穷远处为电位参考点,则 由

$$
\begin{aligned}
& q^{\prime}=\frac{\varepsilon_{0}-4 \varepsilon_{0}}{\varepsilon_{0}+4 \varepsilon_{0}} q=\frac{-3}{5} \times 10^{-7} \mathrm{C} \\
& q^{\prime \prime}=\frac{2 \times 4 \varepsilon_{0}}{\varepsilon_{0}+4 \varepsilon_{0}} q=\frac{8}{5} \times 10^{-7} \mathrm{C}
\end{aligned}
$$

$A$ 点电位

$$
\begin{aligned}
\varphi_{A} & =\frac{q}{4 \pi \varepsilon_{0} \times 0.01}+\frac{q^{\prime}}{4 \pi \varepsilon_{0} \times 0.03}=\frac{10^{-7}}{4 \pi \times 8.85 \times 10^{-12} \times 0.01}+\frac{-0.6 \times 10^{-7}}{4 \pi \times 8.85 \times 10^{-12} \times 0.03} \\
& =71.9 \mathrm{kV}
\end{aligned}
$$

$B$ 点电位

$$
\varphi_{B}=\frac{q^{\prime \prime}}{4 \pi \times 4 \varepsilon_{0} \times 0.03}=\frac{1.6 \times 10^{-7}}{4 \pi \times 4 \times 8.85 \times 10^{-12} \times 0.03}=12.0 \mathrm{kV}
$$

(4) 特殊边界条件

镜像法也可求解一些复杂的边界条件,不可能一一举列。下面分析两个特例。





\section{2. 电轴法}

电轴法用于计算带等量异号电荷的两平行架设的长圆柱导体间的静电场。该方法的关键 



是确定等效电轴的位置,然后按二线输电线的计算公式进行计算。 等效电轴位置利用关于圆的反演公式很容易求得。

对于图 1.6-26(a) 所示的边值问题,可用图 1.6-26(b) 进行计 算。图中等效电轴的位置由下式确定:

$$
b=\sqrt{h^{2}-a^{2}}
$$

此例与二线输电线不同之处在于导体半径较大,因此在导体 表面上分布的电荷是不均匀的, 正负电荷相互吸引的结果造成等 效电轴位置偏移。显然, 若 $a \ll h$, 则 $b \approx h$, 就没必要再用电轴法 了。另外,图(b)的等效计算区域不包括导体所在的区域。







$$
\begin{aligned}
& \left(h_{1}+b\right)\left(h_{1}-b\right)=a_{1}^{2} \\
& \left(h_{2}+b\right)\left(h_{2}-b\right)=a_{2}^{2} \\
& h_{1}+h_{2}=d
\end{aligned}
$$






如果同轴电缆或圆柱电容器产生偏心,则二柱间的电场也可用电轴法求解。图 1.6-28 表 示了这一模型。这里有效计算区域为二圆柱间部分, 而三个待求量的计算也可以通过三个方 程联立求得,即

$$
\left(h_{1}+b\right)\left(h_{1}-b\right)=a_{1}^{2}
$$

$\left(h_{2}+b\right)\left(h_{2}-b\right)=a_{2}^{2}$

$h_{2}-h_{1}=d$






【例 1. 6-17】单位长度带电量为 $\tau$ 的长直圆柱导体与地面 平行架设, 其有关尺寸如图 1.6-29 所示, 试求圆柱导体的电位(设 大地电位为零)。

解: 利用镜像法, 在关于地面对称处得一带负电的导体圆柱, 二圆柱再用电轴法可得图 1.6-30 的计算模型图。其中





$$
b=\sqrt{h^{2}-a^{2}}
$$

显然, 导体上的电位以取 $\tau$ 和 $-\tau$ 连线与导体原位置的 交点 $A$ 计算最方便, 由二线输电线电位计算公式得

$$
\varphi=\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{b+(h-a)}{b-(h-a)}
$$

上式中, 对数中分子表示 $-\tau$ 电轴与 $A$ 点距离, 而分母表示 $\tau$ 电轴与 $A$ 点间的距离。

【例 1. 6-18】一均匀分布线电荷与一长直圆柱导体平 行,周围介质为空气, 如图 1.6-31 所示,试求圆柱导体表面 处的最大电场强度值。

解: 由于正负电荷的吸引作用, 最大场强在导体面处应发生在柱心与 $\tau$ 位置的连线与柱表 面的交点 $A$ 处, 如图 1.6-32 所示, 由电轴法中的反演关系得





$$
d(d-2 b)=a^{2}
$$

则

$$
b=\frac{1}{2}\left(d-\frac{a^{2}}{d}\right)
$$



$$
E_{A}=\frac{\tau}{2 \pi \varepsilon_{0}(d-a)}+\frac{\tau}{2 \pi \varepsilon_{0}(a-d+2 b)}
$$

\subsection{4 电场力及其计算}

\section{1. 用电场强度的定义计算}

$$
\boldsymbol{F}=q \boldsymbol{E}
$$

【例 1. 6-19】在直角坐标系中, 点电荷 $q_{1} 、 q_{2}$ 和 $q_{3}$ 分别位于 $\left(x_{1}, y_{1}, z_{1}\right) 、\left(x_{2}, y_{2}, z_{2}\right)$ 和 $\left(x_{3}, y_{3}, z_{3}\right)$ 处, 试求点电荷 $q_{3}$ 所受到的力。

解: $q_{1}$ 和 $q_{2}$ 在 $q_{3}$ 所在位置产生的电场强度

$$
\begin{aligned}
\boldsymbol{E}= & \frac{q_{1}\left[\left(x_{1}-x_{3}\right) \boldsymbol{e}_{x}+\left(y_{1}-y_{3}\right) \boldsymbol{e}_{y}+\left(z_{1}-z_{3}\right) \boldsymbol{e}_{z}\right]}{4 \pi \varepsilon_{0}\left[\left(x_{1}-x_{3}\right)^{2}+\left(y_{1}-y_{3}\right)^{2}+\left(z_{1}-z_{3}\right)^{2}\right]^{3 / 2}} \\
& +\frac{q_{2}\left[\left(x_{2}-x_{3}\right) \boldsymbol{e}_{x}+\left(y_{2}-y_{3}\right) \boldsymbol{e}_{y}+\left(z_{2}-z_{3}\right) \boldsymbol{e}_{z}\right]}{4 \pi \varepsilon_{0}\left[\left(x_{2}-x_{3}\right)^{2}+\left(y_{2}-y_{3}\right)^{2}+\left(z_{2}-z_{3}\right)^{2}\right]^{3 / 2}}
\end{aligned}
$$

故

$$
\boldsymbol{F}=q_{3} E
$$

【例 1. 6-20】与地面平行架设的一长直导线, 单位长度带电量为 $\tau$, 导线与地面的距离为 $h$,若 $h$ 远大于导线半径,试求该导线单位长度所承受地面作用力的大小和方向。

解: 用镜像法可以计算这种作用力。镜像电荷在导线处产生的场对导线产生作用力为.

$$
F=\frac{\tau^{2}}{2 \pi \varepsilon_{0} 2 h}=\frac{\tau^{2}}{4 \pi \varepsilon_{0} h} \text { (吸力, 垂直指向地面) }
$$

\section{2. 虚位移法}

电场力是向量, 直接利用定义积分计算相当复杂, 而虚位移法有时会方便得多。利用虚位 移法计算的公式为

$$
f_{\mathrm{g}}=\left.\frac{\partial W_{\mathrm{e}}}{\partial g}\right|_{\varphi_{k}=\text { 常量 }}=-\left.\frac{\partial W_{\mathrm{e}}}{\partial g}\right|_{q_{k}=\text { 常量 }}
$$

式中: $f_{\mathrm{g}}$ 为广义力, $g$ 为广义坐标, $W_{e}$ 为静电场能量, $\varphi_{k}$ 为导体电位, $q_{k}$ 为导体电荷。所谓广义 力与广义坐标概念可由下面关系理解: 广义力与广义坐标的乘积一定表示能量或功, 因此存 在:

广义坐标是位移一广义力是力;

广义坐标是角度一广义力是转矩;

广义坐标是体积一广义力是压强;

广义坐标是面积—广义力是表面张力。

静电场能量的普遍计算公式可利用静电场的能量体密度的体积分计算。设 $w_{\mathrm{e}}$ 表示静电 场能量体密度, 则

$$
w_{\mathrm{e}}=\frac{1}{2} E D=\frac{1}{2} \varepsilon E^{2}
$$

$w_{\mathrm{e}}$ 的单位是焦耳/米 ${ }^{3}\left(\mathrm{~J} / \mathrm{m}^{3}\right)$ 。而静电场能量为

$$
W_{\mathrm{e}}=\int_{V} w_{\mathrm{e}} \mathrm{d} V=\int_{V} \frac{1}{2} \varepsilon E^{2} \mathrm{~d} V
$$

对于多个导体组成的系统, 也可以通过各导体的电荷 $q_{k}$ 和各导体的电位 $\varphi_{k}$ 计算系统的 静电场总能量, 此时

$$
W_{e}=\sum_{k=1}^{n} \frac{1}{2} \varphi_{k} q_{k}
$$

【例 1. 6-21】平板电容器中间填充的介质的介电系数为 $\varepsilon$, 板的面积为 $S$, 二极板的距离 为 $d$, 试求在二极板施加恒定电压 $U_{0}$ 时,二极板间的吸力 ; 如果保持二极板上的电荷分布不 变,此时二极板间的吸力又为多大?

解: 平板电容器电容 $C=\varepsilon S / d$, 由

$$
\begin{aligned}
& W_{\mathrm{e}}=\frac{1}{2} C U_{0}^{2}=\frac{\varepsilon S}{2 d} U_{0}^{2} \\
& f=\left.\frac{\partial W_{\mathrm{e}}}{\partial d}\right|_{\varphi_{k}=\text { 学量 }}=-\frac{\varepsilon S}{2 d^{2}} U_{0}^{2} \\
& W_{\mathrm{e}}=\frac{1 q^{2}}{2 C}=\frac{d}{2 \varepsilon S} q^{2} \\
& f=-\left.\frac{\partial W_{\mathrm{e}}}{\partial d}\right|_{q_{k}=\text { 常量 }}=-\frac{1}{2 \varepsilon S} q^{2}
\end{aligned}
$$

$f$ 表达式皆为负值,表示力的方向与 $d$ 增大的方向相反。将 $q=C U_{0}$ 代人,会发现两次计算的 结果是相等的,因为位移是虚的,故只能是同一结果。

【例 1. 6-22】球形电容器的内外半径分别为 $R_{1}$ 和 $R_{2}$, 若已知该电容器储存的静电场能 量为

$$
W_{\mathrm{e}}=K \frac{R_{1} R_{2}}{R_{2}-R_{1}} U_{0}^{2}
$$

式中 $K$ 为一常数,试求球外壳单位面积受的力 (压强)。

解:利用广义力计算式

$$
f=\left.\frac{\partial W_{e}}{\partial V}\right|_{\varphi_{k}={ }^{*}{ }^{2}}
$$

球形体积 $V=\frac{4}{3} \pi R_{2}^{3}$, 则 $\partial V=4 \pi R_{2}^{2} \partial R_{2}$

$$
f=\left.\frac{1}{4 \pi R_{2}^{2} \partial W_{2}}\right|_{\varphi_{k}=\text { 荓量 }}=\frac{K R_{1}}{4 \pi R_{2}^{2}} \cdot \frac{-R_{1}}{\left(R_{2}-R_{1}\right)^{2}} U_{0}^{2}=\frac{-K R_{1}^{2}}{4 \pi R_{2}^{2}\left(R_{2}-R_{1}\right)^{2}} U_{0}^{2}
$$

式中负号表示此力是指向 $R_{2}$ 减小的方向。

\section{3. 法拉第的观点}

为了形象化描绘电场, 常使用所谓电场线 $(\boldsymbol{E}$ 线) 或电位移线 $(\boldsymbol{D}$ 线)绘制电场图形。绘制 场图一般要遵守下述二原则:一是线的疏密应代表场量的强弱,二是线的切线方向应代表场量 的方向。如果是平行平面场,则任意相邻两条曲线两点的连线沿纵向同样长度构成的曲面上 场量的通量应相等。由此,不难想像用 $\boldsymbol{D}$ 线描绘的场图可看作由许多电位移管组成。

法拉第认为: 静电场中每一段电位移管沿其轴向要受到纵张力,而垂直于轴向方向则要受 到侧压力, 并且纵张力和侧压力相等, 都是 $\frac{1}{2} D E\left(\mathrm{~N} / \mathrm{m}^{2}\right)$ 。电位移管沿轴线方向有收缩的趋 势,沿垂直轴线方向有扩张的倾向,由此可判断受力的方向。

【例 1. 6-23】 平板电容器二极板间距离为 $d$, 极板面积为 $S$, 中间填充的介质的介电系数 为 $\varepsilon$, 若在二极板间施加电压 $U_{0}$, 试求其极板上受的作用力。

解: $E=\frac{U_{0}}{d}$

由于导体内场量为零,故板面受到单位面积的力为

$$
f_{0}=\frac{1}{2} D E=\frac{1}{2} \varepsilon E^{2}=\frac{1}{2} \varepsilon \frac{U_{0}^{2}}{d^{2}}
$$

极板受的总力为

$$
f=f_{0} S=\frac{\varepsilon S U_{0}^{2}}{2 d^{2}}
$$

力的方向指向另一极板。该式与前面用虚位移法计算的结果相同。

【例 1. 6-24】试求图 1.6-33 所示平行板电容器介质分界面处每单位面



$$
\text { 解: }\left\{\begin{array}{l}
E_{1} d_{1}+E_{2} d_{2}=U_{0} \\
\varepsilon_{1} E_{1}=\varepsilon_{2} E_{2}
\end{array}\right.
$$

则

$$
E_{1}=\frac{\varepsilon_{2} U_{0}}{\varepsilon_{2} d_{1}+\varepsilon_{1} d_{2}}, \quad E_{2}=\frac{\varepsilon_{1} U_{0}}{\varepsilon_{2} d_{1}+\varepsilon_{1} d_{2}}
$$

取 $f_{1}$ 的方向为合力 $f$ 的方向, 则

$$
f=f_{1}-f_{2}=\frac{1}{2} \varepsilon_{1} E_{1}^{2}-\frac{1}{2} \varepsilon_{2} E_{2}^{2}=\frac{\varepsilon_{1} \varepsilon_{2}\left(\varepsilon_{2}-\varepsilon_{1}\right) U_{0}^{2}}{2\left(\varepsilon_{2} d_{1}+\varepsilon_{1} d_{2}\right)^{2}}
$$

\subsection{5 电容和部分电容, 简单形状电极结构电容的计算}

\section{1. 电容}

当空间只需考虑两个相互绝缘的导体时,两导体分别带有等量而异号的电荷,则电荷的量 值 $q$ 与两导体间电压 $U$ 之比, 称为两导体间的电容, 并以 $C$ 表示, 即

$$
C=\frac{q}{U}
$$

$C$ 恒取正值,单位是法拉 $(\mathrm{F})$ 。线性电容器的电容值仅与电极的几何形状、大小、中间填 充的介质以及两电极间相对位置有关, 而与其是否带电无关。但必须指出: 许多电容值的计算 却是通过电场计算获得。一般计算步骤为先假设极板上带等量异号电荷, 由电场分析计算出两极板间电压, 最后相比求得 $C$ 。

\section{(1) 平行板电容器}

平行板单介质的电容器为 $C=\frac{\varepsilon S}{d}$, 这里 $\varepsilon 、 S$ 和 $d$ 分别表示填充介质的介 电系数、极板面积和二导体之间的距离。显然, 电容 $C$ 的计算公式中无电荷 或电压。

【例 1. 6-25】试求图 1.6-34 所示双层介质的平板电容器的电容( 设极 板的面积为 $S$ )。

解: 假设两极板带等量异号电荷; 其面密度分别为 $\sigma$ 和 $-\sigma$ 。由导体和 介质分界面条件可知, 电位移 $D$ 将相等, 且满足二介质分界面条件。由此得



$$
\begin{aligned}
& \frac{D}{\varepsilon_{1}}=E_{1}, \quad \frac{D}{\varepsilon_{2}}=E_{2} \\
& U=E_{1} \cdot d_{1}+E_{2} d_{2}=\frac{\sigma}{\varepsilon_{1}} d_{1}+\frac{\sigma}{\varepsilon_{2}} d_{2} \\
& C=\frac{\sigma S}{U}=\frac{\varepsilon_{1} \varepsilon_{2} S}{d_{1} \varepsilon_{2}+d_{2} \varepsilon_{1}}
\end{aligned}
$$

【例 1. 6-26】图 1.6-35 所示为平行板电容器示意图, 若介电系数为 $\varepsilon_{1}$ 的介质对应的极板面积为 $S_{1}$, 单个极板的总面积为 $S$, 试求该电容器的电容。

解: 此例可看作两个平行板电容器并联, 故

$$
C=\frac{\varepsilon_{1} S_{1}+\varepsilon_{2}\left(S-S_{1}\right)}{d}
$$

(2) 圆柱形电容器

圆柱形电容器的电极是共轴的, 中间填充介质。当所填充的介质介电系 数为 $\varepsilon$, 而内外半径分别为 $R_{1}$ 和 $R_{2}$, 长度为 $L$ 时, 该电容器的电容

$$
C=\frac{2 \pi \varepsilon L}{\ln \left(R_{2} / R_{1}\right)}
$$



【例 1.6-27】长为 $L$, 横截面如图 1.6-36 所示的双层介质圆柱电容器, 试求其电容。



解: 设内导体单位长带电荷为 $\tau$, 则

$$
\begin{aligned}
& \boldsymbol{E}_{1}=\frac{\tau}{2 \pi \varepsilon_{1} r} e_{r} \quad\left(R_{1}<r<R_{2}\right) \\
& \boldsymbol{E}_{2}=\frac{\tau}{2 \pi \varepsilon_{2} r} e_{r} \quad\left(R_{2}<r<R_{3}\right) \\
& U=\int_{R_{1}}^{R_{2}} E_{1} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} E_{2} \mathrm{~d} r=\frac{\tau}{2 \pi}\left(\frac{1}{\varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}\right)
\end{aligned}
$$

单位长度电容为

总电容为

$$
C_{0}=\frac{\tau}{U}=\frac{2 \pi}{\frac{1}{\varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}}
$$

$$
C=C_{0} L=\frac{2 \pi L}{\frac{1}{\varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}}
$$

(3) 球形电容器

内外半径为 $R_{1}$ 和 $R_{2}\left(R_{2}>R_{1}\right)$ 的球形电容器, 中间填充介电系数为 $\varepsilon$ 的介质时, 其电容值 为

$$
C=\frac{4 \pi \varepsilon R_{1} R_{2}}{R_{2}-R_{1}}
$$

若中间填充的是两种介质, 介质分界面的半径为 $R_{2}$, 而外半径为 $R_{3}$, 介电系数分别用 $\varepsilon_{1}$ 和 $\varepsilon_{2}$ 表示,则由与例 1.6-27 相类似的计算过程不难得到 

$$
C=\frac{4 \pi R_{2}}{\frac{1}{\varepsilon_{1} R_{1}}\left(R_{2}-R_{1}\right)+\frac{1}{\varepsilon_{2} R_{3}}\left(R_{3}-R_{2}\right)}
$$

(4) 其他简单电容的计算

金属球与地、圆柱导体对地、二线输电线等之间的电容, 其结构都比较简单, 有些问题求解 也十分方便。另外, 通常提到的孤立导体的电容其实并不孤立, 而是另一导体被假设到了无穷 远处。



【例 1.6-28】与地面平行架设的长圆柱导体示意如图 1.637 所示,试求该导体单位长度对地的电容值。

解: 由镜像法加电轴法得图 1.6-38 所示的计算图形。若设地 平面为电位参考点, 则

$$
\varphi_{A}=\frac{\tau}{2 \pi \varepsilon_{0}} \ln \frac{b+h-a}{b-h+a}
$$

$$
b=\sqrt{h^{2}-a^{2}}
$$

$\varphi_{i}$ 即导体对大地的电压, 所求电容

$$
C_{0}=\frac{\tau}{\varphi_{A}}=\frac{2 \pi \varepsilon_{0}}{\ln \frac{b+h-a}{b-h+a}}
$$

当 $h \gg a$ 时, $b \approx h$, 则可得近似式

$$
C_{0} \approx \frac{2 \pi \varepsilon_{0}}{\ln \frac{2 h}{a}}
$$

如果求两平行架设的传输线之间的电容, 此时两导体之 间的电压应为两导体之间的电位差, 故相距为 $2 h$ 的等半径为



$$
C=\frac{\pi \varepsilon_{0}}{\ln \frac{b+h-a}{b-h+a}}
$$

\section{2. 部分电容}

系统中存在序号为 $0,1,2, \cdots, n$ 的 $n+1$ 个导体, 各导体所带电荷量用序号表示区别, 各导 体之间的电压用二者序号下标以示区别, 若存在关系式 $\sum_{i=0}^{n} q_{i}=0$, 则

$$
\begin{aligned}
& q_{1}=C_{10} U_{10}+C_{12} U_{12}+\cdots+C_{1 n} U_{1 n} \\
& q_{2}=C_{21} U_{21}+C_{20} U_{20}+\cdots+C_{2 n} U_{2 n} \\
& \cdots \cdots \\
& q_{n}=C_{n 1} U_{n 1}+C_{n 2} U_{n 2}+\cdots+C_{n 0} U_{n 0}
\end{aligned}
$$

式中各个系数称为多导体系统的部分电容。主对角线上的系数 (即 $C_{\mathrm{i} 0}$ ) 称为自部分电容。非 主对角线上的各系数称为互部分电容。对线性介质而言, 各个部分电容存在以下关系:

$$
\text { (1) } C_{i j}>0 \text {; }
$$

(2) $C_{i j}=C_{i i}$, 实际表示的是同一个电容。 因此, $n+1$ 个导体系统中, 部分电容的个数为 $\frac{1}{2} n(n+1)$ 。

部分电容只与各导体的形状、大小、周围介质的分布以及各导体间的相对位置有关。但 是,部分电容的求解必须通过电场分析计算,一般是比较复杂的。

【例 1.6-29]图 1.6-39 所示对称的三芯电缆, 各导体与铅皮之间的部分电容均为 $C_{0}$, 各 导体之间的部分电容均为 $C_{1}$, 试求: (1) 将三颗芯线连接后与铅皮之间的等效电容; (2) 在任 意两颗芯线间施加电压, 则此时电路的等效电容又为多少?





解:电缆的各部分电容表示为如图 1.6-40 所示, 其中 0 表示电缆的铅皮。

(1)芯线相联, $C_{1}$ 皆被短接, 故等效电容 $C_{\mathrm{e}}$ 为三个 $C_{0}$ 并联, 即

$$
C_{e}=3 C_{0}
$$

(2) 利用电容的星三角转换, 若把 $C_{1}$ 转换成星接, 则将变为 $3 C_{1}$, 再利用电容的串并联, 则 等效电容 $C_{\mathrm{D}}$ 为

$$
C_{\mathrm{D}}=\frac{1}{2}\left(3 C_{1}+C_{0}\right)
$$

此题也可以把星接 $C_{\mathrm{D}}$ 转变为角接, 则将变为 $\frac{1}{3} C_{0}$, 再利用电容串并联, 则仍有上面结论。

【例1.6-30】图1.6-41 中 1 和 2 表示与地面平行架设的二线输电线, 今测得 1 号导线对 地部分电容 $C_{10}=0.001 \mu \mathrm{F}$, 而 1 和 2 导体的等效电容为 $0.0025 \mu \mathrm{F}$, 试求部分电容 $C_{12}$ 和 $C_{200}$

解:由于对称关系

$$
C_{20}=C_{10}=0.001 \mu \mathrm{F}
$$

由虫并联关系

$$
C_{12}+\frac{1}{2} C_{10}=0.0025
$$

代人 $C_{10}$ 值, 即得



$$
C_{12}=0.0025-\frac{1}{2} \times 0.001=0.002 \mu \mathrm{F}
$$



\section{7 恒定电场}

\subsection{1 恒定电流、恒定电场和电流密度}

\section{1. 恒定电流}

导电媒质中电荷流动的大小和分布不是时间的函数的电流称为恒定电流, 它是由导电媒 质中的恒定电场产生的。

\section{2. 恒定电场}

由电荷在导电媒质中激发, 不随时间变化的电场称为恒定电场。

导体中存在电场, 必将产生电流, 恒定电场产生的电流也是恒定的。恒定电场与静电场的 重要区别在于: 静电场是由相对于观察者静止的电荷产生的; 而恒定电场是由相对于观察者做 宏观运动,但其空间分布不是时间函数的电荷所产生。

要维持恒定电场存在, 必须依赖于恒定电源 (恒定电源在电路中常称为直流电源)。电源 不是这里要关心的问题, 为简化分析过程, 在电源内部引入所谓局外力 $f_{\mathrm{e}}$ (非电场力) 和局外 场强 $\boldsymbol{E}_{\mathrm{e}}$ 的概念, 并且令

$$
E_{\mathrm{e}}=\frac{f_{\mathrm{e}}}{q}
$$

它表示在电源内部, 单位正电荷受到的局外力, 这里称局外场强完全是采用等效的概念。所谓 电源的电动势,一般可表示为

$$
\mathscr{E}=\int_{l} \boldsymbol{E}_{\mathrm{e}} \cdot \mathrm{d} \boldsymbol{l}
$$

积分路线 $l$ 是在电源内部由低电位电极到高电位电极。

导电媒质中存在恒定电场时, 导体不再是等位体, 除非由此引起的电位差很小而被忽略不 计。另外, 在导电媒质周围的介质中, 将存在与静电场相似的恒定电场, 它也是由恒定分布的 电荷产生的。

\section{3. 电流密度}

电荷的定向运动形成电流。衡量电流的大小采用电流强度 (简称电流) 的概念, 即 $I=$ $\mathrm{d} q / \mathrm{d} t$, 它表示单位时间通过某导线横截面上的电量。电流强度是一个积分量, 不可能描述场 中每一点处电荷的流动情况, 因此, 在电磁场理论中, 更多地使用电流密度这一物理量。

体密度为 $\rho$ 的分布电荷, 以速度 $v$ 运动时, 形成体分布的电流密度 $J$, 其表达式为

$$
J=\rho v
$$

电流密度也可以表述为: 当正电荷垂直通过某微小面积 $\Delta S$ 的电流强度为 $\Delta I$ 时, $\Delta I$ 与 $\Delta S$ 之比的极限, 即

$$
J=\lim _{\Delta S \rightarrow 0} \frac{\Delta I}{\Delta S}=\frac{\mathrm{d} I}{\mathrm{~d} S}
$$

正电荷运动的方向即为电流密度 $J$ 的方向。电流密度的单位为安培 $/$ 米 $^{2}\left(\mathrm{~A} / \mathrm{m}^{2}\right)$ 。

电流强度与电流密度的关系可以表示为

$$
I=\int_{S} \boldsymbol{J} \cdot \mathrm{d} S
$$

工程上会遇到电荷在一个很薄的面上流动的情况, 例如在一个薄金属板上流动。问题的 实质是,电流虽是体分布,但理想化成一个面电流分布对问题的分析计算更方便。理想化的结 果犹如一个面分布电荷 $\sigma$ 在面上流动, 由此引人 电流线密度向量 $J_{S}$, 且 $J_{S}=\sigma v_{\circ}$ 并可得到

$$
I=\int_{l} J_{S} \cdot e_{n} \mathrm{~d} l
$$

上式中 $e_{n}$ 为垂直于 $\mathrm{d} l$ 方向的单位向量。 $J_{S}$ 的单位为 $\mathrm{A} / \mathrm{m}$ 。

类似地分析, 如果电流通过的导线的横截面积非常小时,可以理想化地用一线电流表示。

【例 1.7-1】位于直角坐标系 $x O y$ 平面上的面电流可表示为

$$
J_{S}=4 e_{x}+3 e_{y} \quad \mathrm{~A} / \mathrm{m}
$$

武求通过点 $A(3,0)$ 和 $B(0,4)$ 之间线段上的电流。

解:由点的几何坐标, 通过图 1.7-1 不难判断出线段的垂线 方向的单位向量

$$
e_{n}=0.8 e_{x}+0.6 e_{y}
$$

由此

$$
I=\int_{l} J_{S} \cdot e_{n} \mathrm{~d} l=(4 \times 0.8+3 \times 0.6) \times \sqrt{3^{2}+4^{2}}=25 \mathrm{~A}
$$



1.7.2 欧姆定律和焦耳定律的微分形式,恒定电场的基本方程和分界面上的衔接条件

\section{1. 欧姆定律的微分形式}

$$
J=\gamma E
$$

式中 $\gamma$ 表示导电媒质的电导率, 单位为 $\mathrm{S} / \mathrm{m}$ 。

微分形式的欧姆定律表示导电媒质中电流密度 $J$ 的大小与电导率成正比,其方向与电场 强度的方向一致(各向同性媒质中)，它描述了媒质中任一点处电荷运动的情况。

【例 1.7-2】横截面积为 $3 \mathrm{~mm}^{2}$ 的导线, 通过它的电流为 $15 \mathrm{~A}$, 电流均匀分布于导线中, 若导线的电导率为 $5 \times 10^{7} \mathrm{~S} / \mathrm{m}$, 试求导线内部的电场强度。

解: 导线内的电流密度

$$
J=\frac{I}{S}=\frac{15}{3 \times 10^{-6}}=5 \times 10^{6} \mathrm{~A} / \mathrm{m}^{2}
$$

导线内的电场强度

$$
E=\frac{J}{\gamma}=\frac{5 \times 10^{6}}{5 \times 10^{7}}=0.1 \mathrm{~V} / \mathrm{m}
$$

\section{2. 焦耳定律的微分形式}

$$
p=J \cdot E \quad \text { 或 } p=\gamma E^{2}=\frac{J^{2}}{\gamma}
$$

式中 $p$ 表示导体内的功率损耗密度,即任一点处的单位体积所消耗的功率,其单位为瓦/米 ${ }^{3}$ $\left(\mathrm{W} / \mathrm{m}^{3}\right)$ 。

导电媒质中损耗的功率可通过下式计算:

$$
P=\int_{V} p \mathrm{~d} V=\int_{V} \boldsymbol{J E} \mathrm{d} V
$$

式中的 $P$ 与电路理论中的焦耳定律 $\left(P=I^{2} R\right)$ 的计算值相同。

【例 1.7-3】一球形电容器的内外半径分别为 $R_{1}$ 和 $R_{2}$, 中间填充介质的漏电电导率为 $\gamma$, 若已知漏电电流强度为 $I$, 试求电容器的功率损耗。 解: 由对称特点可知介质中的电流密度

$$
J=\frac{I}{4 \pi r^{2}} \quad\left(R_{1} \leqslant r \leqslant R_{2}\right)
$$

取球面 $4 \pi r^{2}$, 在 $4 \pi r^{2} \mathrm{~d} r$ 的体积内 $J$ 可视为常量, 故

$$
P=\int_{V} \frac{J^{2}}{\gamma} \mathrm{d} V=\int_{R_{1}}^{R_{2}} \frac{I^{2}}{16 \pi^{2} \gamma r^{4}} 4 \pi r^{2} \mathrm{~d} r=\frac{I^{2}}{4 \pi \gamma}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)
$$

\section{3. 基本方程}

恒定电场的基本方程为

$$
\left\{\begin{array}{l}
\oint_{l} \boldsymbol{E} \cdot \mathrm{d} \boldsymbol{l}=0 \\
\oint_{S} \boldsymbol{J} \cdot \mathrm{d} \boldsymbol{S}=0
\end{array}\right.
$$

以上二式研究的区间不包含电源内部, 但恒定电场的存在必定存在电源, 这样处理只是对 电源内部另做处理的一种分离。

恒定电场的环路积分恒等于零, 说明恒定电场是位场, 可以引人电位概念, 即令

$$
E=-\nabla \varphi
$$

恒定电流密度在任一闭合面上的积分恒等于零, 这一表达式又被称为电流连续性方程。 流人某闭合曲面电流必定等于流出该闭合曲面的电流,这一结论是电路中直流电路基尔霍夫 电流定律的理论依据。

微分形式恒定电场的基本方程为

$$
\left\{\begin{array}{l}
\nabla \times E=0 \\
\nabla \cdot J=0
\end{array}\right.
$$

恒定电场是一个无散度源的场，电流线必是无头无尾的闭合曲线。

引人标量电位后, 对于均匀媒质不难得到

$$
\nabla^{2} \varphi=0
$$

即电位满足拉普拉斯方程。



\section{4. 分界面上的衔接条件}

两种电导率不同的媒质,在分界面处场量会发生变化,其衔 接条件为

$$
\left\{\begin{array}{l}
E_{1 t}=E_{2 t} \\
J_{1 n}=J_{2 n}
\end{array}\right.
$$

即分界面处的电场强度切向分量连续,而电流密度的法向分量 连续。

对于各向同性的导电媒质,存在所谓的恒定电场的折射定 律, 如图 1. 7-2 所示, 则

$$
\frac{\tan \theta_{1}}{\tan \theta_{2}}=\frac{\gamma_{1}}{\gamma_{2}}
$$

当 $\gamma_{1} \gg \gamma_{2}$ 时, 只要 $\theta_{1}$ 不接近于 $90^{\circ}$, 则 $\theta_{2}$ 总可以认为近似为 $0^{\circ}$ 。由此不难得到: 当电流从良 导体流人不良导体时,其电场强度或电流密度在不良导体中的方向总是近似垂直于分界面的。 

\section{5. 恒定电场的计算}

恒定电场的计算类似于静电场。当电流密度的分布可以依据场域或边界条件判断时, 可 以通过简单的函数进行计算,也可以由拉普拉斯方程和边界条件定解。

由于无电荷区域的静电场和电源外部的恒定电场所满足的数学表达式相似, 恒定电场还 可以通过静电比拟求解。静电场与恒定电场的对应量为: $\boldsymbol{E} \sim \boldsymbol{E} 、 \varphi \sim \varphi 、 D \sim J 、 q \sim I 、 \varepsilon \sim \gamma$ 。所 谓静电比拟, 意义之一可理解为: 如果静电场中的场源、边界条件和介质分布被对应的恒定电 场物理量所置换, 则静电场解答式中的物理量用恒定电场对应量代替后,该解答即为恒定电场 的解答。媒质置换时应当注意保证满足条件

$$
\frac{\gamma_{1}}{\gamma_{2}}=\frac{\varepsilon_{1}}{\varepsilon_{2}}
$$

利用静电比拟, 可以推得分界面为无限大平面时, 两种导电媒质中的镜像法, 图 1. 7-3 中 表示了这一过程。图中

$$
\begin{aligned}
& I^{\prime}=\frac{\gamma_{1}-\gamma_{2}}{\gamma_{1}+\gamma_{2}} I \\
& I^{\prime \prime}=\frac{2 \gamma_{2}}{\gamma_{1}+\gamma_{2}} I
\end{aligned}
$$

若 $\gamma_{2}=0$, 则

$$
\begin{aligned}
& I^{\prime}=I \\
& I^{\prime \prime}=0
\end{aligned}
$$

例如土壤中 $\left(\gamma_{2}\right)$ 埋一电极, 上部为空气 $\left(\gamma_{1}\right)$ 即属于这种情况。








利用静电比拟关系,还可以把工程上难以测量的静电场问题比拟成恒定 电场问题, 而恒定电场可以通过直流测试仪表进行测量, 这种模拟实验在实 际中被广泛应用。

在恒定电场计算中, 常用到所谓“电极”一词,这里的电极是指它由优良 的导体制作, 可以视为一等位体。因此, 电极处必是一个等电位的边界条件。

【例 1.7-4】一平行板电容器横截面如图 1.7-4 所示, 若二介质中的漏 电电导率分别为 $\gamma_{1}$ 和 $\gamma_{2}$, 试给出在外施电压 $U_{0}$ 作用下, 介质分界面处的电 位和面电荷密度。

解: 由于介质漏电, 在暂态过程中分界面处可能积累有自由电荷。在恒 定状态下,用电流密度计算比较方便。由于 $J_{1 n}=J_{2 n}$, 可得



$$
\begin{aligned}
& \gamma_{1} E_{1}=\gamma_{2} E_{2} \\
& U_{0}=E_{1} \frac{d}{2}+E_{2} \frac{d}{2}=\frac{1}{2} E_{2} d+\frac{1 \gamma_{2}}{2 \gamma_{1}} E_{2} d
\end{aligned}
$$

即可得

$$
E_{2}=\frac{2 \gamma_{1} U_{0}}{\left(\gamma_{1}+\gamma_{2}\right) d}
$$

若取 $\varepsilon_{2}$ 一侧极板接电源负极, 并取为电位参考点, 则分界面处电位为

$$
\varphi=E_{2} d / 2=\frac{\gamma_{1} U_{0}}{\gamma_{1}+\gamma_{2}}
$$

而分界面处的面电荷 $\sigma$ 可由分界面条件获得

$$
\sigma=D_{2 n}-D_{1 n}
$$

由 $D=\varepsilon E$ 和 $J=\gamma E$ 可得

$$
\sigma=\varepsilon_{2} E_{2}-\varepsilon_{1} E_{1}=\frac{\varepsilon_{2}}{\gamma_{2}} J_{2}-\frac{\varepsilon_{1}}{\gamma_{1}} J_{1}=\left(\frac{\varepsilon_{2}}{\gamma_{2}}-\frac{\varepsilon_{1}}{\gamma_{1}}\right) J
$$

代人 $J=\gamma_{2} E_{2}=\frac{2 \gamma_{1} \gamma_{2} U_{0}}{\left(\gamma_{1}+\gamma_{2}\right) d}$

可得 $\quad \sigma=\frac{2\left(\gamma_{1} \varepsilon_{2}-\gamma_{2} \varepsilon_{1}\right)}{\left(\gamma_{1}+\gamma_{2}\right) d} U_{0}$

由此例可见, 当

$$
\frac{\varepsilon_{2}}{\gamma_{2}}-\frac{\varepsilon_{1}}{\gamma_{1}} \neq 0 \text { 或 } \frac{\varepsilon_{2}}{\varepsilon_{1}} \neq \frac{\gamma_{2}}{\gamma_{1}}
$$

时, 二媒质分界面处会积累有电荷。



【例 1.7-5】双层介质长直圆柱导体, 其横截面如图 1. 7-5 所示, 二介质漏电电导率分别为 $\gamma_{1}$ 和 $\gamma_{2}$, 如在二导体 间施加电压 $U_{0}$, 而各导体均可视为等位体, 试求二圆柱间单 位长度的漏电流。

解: 由于对称关系, 在半径为 $R_{1} \leqslant r \leqslant R_{3}$ 的区间, 电流密 度仅是 $r$ 的函数。假设从内导体单位长流出的电流为 $I$, 则

$$
J=\frac{I}{2 \pi r} e,
$$

\section{二介质中的场强分别为}

$$
\boldsymbol{E}_{1}=\frac{I}{2 \pi \gamma_{1} r} e_{r}
$$

\section{二导体间电压}

$$
\boldsymbol{E}_{2}=\frac{\boldsymbol{I}}{2 \pi \gamma_{2}{ }^{r}} \boldsymbol{e}_{r}
$$

$$
U_{0}=\int_{R_{1}}^{R_{2}} \frac{I}{2 \pi \gamma_{1} r} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} \frac{I}{2 \pi \gamma_{2} r} \mathrm{~d} r=\frac{I}{2 \pi}\left(\frac{1}{\gamma_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\gamma_{2}} \ln \frac{R_{3}}{R_{2}}\right)
$$

由此可解得 

$$
I=\frac{2 \pi U_{0}}{\frac{1}{\gamma_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\gamma_{2}} \ln \frac{R_{3}}{R_{2}}}
$$

由静电比拟也可计算本题。若设内导体单位长带有电荷 $\tau$, 则

$$
U_{0}=\frac{\tau}{2 \pi}\left(\frac{1}{\varepsilon_{1}} \ln \frac{R_{2}}{R_{1}}+\frac{1}{\varepsilon_{2}} \ln \frac{R_{3}}{R_{2}}\right)
$$

利用 $I$ 代替 $\tau, \gamma_{1}$ 和 $\gamma_{2}$ 分别代替 $\varepsilon_{1}$ 和 $\varepsilon_{2}$ 可得 $I$ 。

\section{7 .3 电导和接地电阻}

1. 电导

$$
G=\frac{I}{U}
$$

式中 $I$ 为两电极间流过的电流, $U$ 为两电极间的电压。

对于形状较规则的导体, 可先假设一电流再计算出电流密度 $\boldsymbol{J}$, 通过 $\boldsymbol{E}=\boldsymbol{J} / \gamma$ 计算出 $\boldsymbol{E}$, 再 积分求得 $U=\int_{I} \boldsymbol{E} \cdot \mathrm{d} l$, 可计算出 $G=I / U$, 或二电极间的电阻 $R=U / I$ 。 另外, 也可以通过两导 体间电压, 计算出电流 $I$, 但这一过程并不多用。电导的计算, 还可以通过 拉普拉斯方程求解。

【例 1.7-6】一平行板电容器, 极板面积为 $S$, 二极板间填充介质的漏 电电导率为 $\gamma$, 如图 1.7-6 所示, 若二极板间距离为 $d$, 试求该电容器的漏电 电阻。

解: 假设极板间流动的电流为 $I$, 则

$$
\begin{aligned}
& J=\frac{I}{S}, E=\frac{I}{\gamma S} \\
& U=\int_{0}^{d} \frac{I}{\gamma S} \mathrm{~d} x=\frac{I}{\gamma S} d
\end{aligned}
$$



故有 $R=\frac{U}{I}=\frac{d}{\gamma S}$

【例 1.7-7】图 1.7-7 所示为一双层介质的电容器示意图, 若极板面积



解: 设极板间电流为 $I$, 则此问题由分界面条件可判断, $J_{1}=J_{2}$, 即为均匀 分布电流, 故有

$$
R=\frac{U}{I}=\frac{d-d_{1}}{\gamma_{1} S}+\frac{d_{1}}{\gamma_{2} S}
$$

$$
\begin{aligned}
& J=\frac{I}{S} \\
& E_{1}=\frac{J}{\gamma_{1}}=\frac{I}{\gamma_{1} S}, E_{2}=\frac{J}{\gamma_{2}}=\frac{I}{\gamma_{2} S} \\
& U=\int_{l 1} E_{1} \mathrm{~d} l_{1}+\int_{n} E_{2} \mathrm{~d} l_{2}=\int_{0}^{d-d_{1}} \frac{I}{\gamma_{1} S} \mathrm{~d} l_{1}+\int_{0}^{d_{1}} \frac{I}{\gamma_{2} S} \mathrm{~d} l_{2}
\end{aligned}
$$

$$
=\frac{I}{\gamma_{1} S}\left(d-d_{1}\right)+\frac{I}{\gamma_{2} S} d_{1}
$$

此题也可视为二段电阻串联,利用例 1.7-6 的结论直接计算。即使有多层介质, 只要其中 电流是均匀分布的, 这种方法也同样适用。

【例 1.7-8】一圆柱形电容器, 内外导体半径分别为 $R_{1}$ 和 $R_{2}$, 中间填充的介质漏电, 漏电 电导率为 $\gamma$, 若圆柱导体长度为 $L$, 试求该电容器的漏电电阻。

解: 设内导体流出的电流为 $I$, 则电流密度

漏电电阻

$$
\begin{aligned}
& J=\frac{I}{2 \pi r L}, E=\frac{J}{\gamma}=\frac{I}{2 \pi \gamma L r} \\
& U=\int_{R_{1}}^{R_{2}} E d r=\int_{R_{1}}^{R_{2}} \frac{I}{2 \pi \gamma L r} \mathrm{~d} r=\frac{I}{2 \pi \gamma L} \ln \frac{R_{2}}{R_{1}}
\end{aligned}
$$

$$
R=\frac{U}{I}=\frac{1}{2 \pi \gamma L} \ln \frac{R_{2}}{R_{1}}
$$

若此题改为双层介质或多层介质, 只要电流在 $r$ 处大小相等, 方向又都只存在径向分量, 计算过程仅仅注意到不同媒质中 $\gamma$ 不同,因而 $E$ 不同,分段积分就可得到计算结果。具体过 程可以参照例 1.7-5。

【例 1.7-9】一球形电容器, 内外半径分别为 $R_{1}$ 和 $R_{3}$, 中间填充两种介质, 介质分界面的 半径为 $R_{2}$, 若内外两层介质的漏电电导率分别为 $\gamma_{1}$ 和 $\gamma_{2}$ (如图 1.7-8), 求此电容器的漏电导。

解: 设内导体流出的电流为 $I$, 由对称可得电容器内



$$
\begin{aligned}
J & =\frac{I}{4 \pi r^{2}} \\
E_{1} & =\frac{J}{\gamma_{1}}=\frac{I}{4 \pi \gamma_{1} r^{2}} \quad\left(R_{1}<r<R_{2}\right) \\
E_{2} & =\frac{J}{\gamma_{2}}=\frac{I}{4 \pi \gamma_{2} r^{2}} \quad\left(R_{2}<r<R_{3}\right) \\
U & =\int_{R_{1}}^{R_{2}} E_{1} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} E_{2} \mathrm{~d} r \\
& =\int_{R_{1}}^{R_{2}} \frac{I}{4 \pi \gamma_{1} r^{2}} \mathrm{~d} r+\int_{R_{2}}^{R_{3}} \frac{I}{4 \pi \gamma_{2} r^{2}} \mathrm{~d} r \\
& =\frac{I}{4 \pi}\left[\frac{1}{\gamma_{1}}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)+\frac{1}{\gamma_{2}}\left(\frac{1}{R_{2}}-\frac{1}{R_{3}}\right)\right]
\end{aligned}
$$

$$
G=\frac{I}{U}=\frac{4 \pi \gamma_{1} \gamma_{2}}{\gamma_{2}\left(\frac{1}{R_{1}}-\frac{1}{R_{2}}\right)+\gamma_{1}\left(\frac{1}{R_{2}}-\frac{1}{R_{3}}\right)}
$$

【例 1.7-10】图 1.7-9 所示厚为 $d$ 的一块导电板, 导电材料的电导率为 $\gamma$, 试求:

(1) 沿厚度方向的电阻;

(2) 两圆弧面间的电阻;

(3) 两个侧表面间的电阻。

解: 此题为一典型题目, 它说明电阻与施加电极的位置有关。换言之, 电阻与电流的分布 有关, 即不仅是与材料、大小和几何形状相关,也是场分布的函数。

(1)沿厚度方向的电阻, 相当于在其两面各加一等面积的电极, 这样二电极间的电流必是均 匀分布, 可用所谓的电阻定律直接给出 $R$ 值, 即 

$$
R=\frac{L}{S \gamma}=\frac{2 d}{\gamma \theta\left(R_{2}^{2}-R_{1}^{2}\right)}
$$

(电阻定律: 电流均匀流过一段均匀导体时, 其电阻的大小与电导 率 $\gamma$ 成反比,与导体的横截面积成反比, 而与导体的长度成正比。)

若以电场计算, 可设电流为 $I$, 则

$$
\begin{aligned}
& J=\frac{I}{S}=\frac{2 I}{\theta\left(R_{2}^{2}-R_{1}^{2}\right)} \\
& E=\frac{J}{\gamma} \\
& U=E d=\frac{2 I d}{\gamma \theta\left(R_{2}^{2}-R_{1}^{2}\right)}
\end{aligned}
$$



用 $U / I$ 同样可得上面结果。

(2)由于形状特点,电流 $I$ 由内弧面流向外弧面时,面积随 $r$ 的增大而增大,但在同一 $r$ 的面 上,电流密度应为同值,故有

$$
\begin{aligned}
& J=\frac{I}{S}=\frac{I}{\theta r d} \\
& E=\frac{J}{\gamma} \\
& U=\int_{R_{1}}^{R_{2}} E \mathrm{~d} r=\int_{R_{1}}^{R_{2}} \frac{I}{\gamma \theta r d} \mathrm{~d} r=\frac{I}{\gamma \theta d} \ln \frac{R_{2}}{R_{1}} \\
& R=\frac{U}{I}=\frac{1}{\gamma \theta d} \ln \frac{R_{2}}{R_{1}}
\end{aligned}
$$

(3)电极加在两侧, 由特定的几何形状可判断出: 对应于扇形的角度方向任一截面上, 电场 强度必定垂直于该面, 而该面上的场强将与 $r$ 有关。若设两侧面施加电压 $U$, 则

$$
\begin{aligned}
& E=\frac{U}{\theta r} \\
& J=\gamma E \\
& I=\int_{S} J \mathrm{~d} s=\int_{R_{1}}^{R_{2}} \frac{\gamma U}{\theta r} d \mathrm{~d} r=\frac{\gamma U d}{\theta} \ln \frac{R_{2}}{R_{1}} \\
& R=\frac{U}{I}=\frac{\theta}{d \gamma \ln \frac{R_{2}}{R_{1}}}
\end{aligned}
$$

该电阻的计算通过拉普拉斯方程计算也很方便,但必须掌握圆柱坐标系拉普拉斯方程和 梯度公式,下面给出这一计算过程。

电位仅是 $\alpha$ 的函数,故可建立定解问题为

$$
\left\{\begin{array}{l}
\frac{1}{r^{2}} \frac{\partial^{2} \varphi}{\partial \alpha^{2}}=0 \\
\left.\varphi\right|_{\alpha=0}=0 \\
\left.\varphi\right|_{\alpha=\theta}=U
\end{array}\right.
$$

解得

$$
\varphi=C_{1} \alpha+C_{2}
$$

代人边界条件后可得

$$
\begin{aligned}
& C_{2}=0, \quad C_{1}=\frac{U}{\theta} \\
& \varphi=\frac{U}{\theta} \alpha \\
& \boldsymbol{E}=-\nabla_{\varphi}=-\frac{\partial \varphi}{r \partial \alpha} \boldsymbol{e}_{\alpha}=-\frac{U}{r \theta} \boldsymbol{e}_{\alpha} \\
& \boldsymbol{J}=\boldsymbol{\gamma} \boldsymbol{E}=-\frac{\gamma U}{r \theta} \boldsymbol{e}_{\alpha} \\
& I=\int_{S} \boldsymbol{J} \cdot \mathrm{d} S=-\int_{R_{2}}^{R_{1}} \frac{\gamma U}{r \theta} d \mathrm{~d} r=\frac{\gamma d U}{\theta} \ln \frac{R_{2}}{R_{1}}
\end{aligned}
$$

故有

$$
R=\frac{U}{I}=\frac{\theta}{d \gamma \ln \frac{R_{2}}{R_{1}}}
$$

用拉普拉斯方程求解,虽然过程较繁,但对此题分析过程却要简便一些。

【例 1.7-11】厚为 $h$ 的无限大导电平板, 其电导率为 $\gamma$, 今在板上挖有两个圆孔, 圆孔的 半径均为 $a$, 两圆孔的中心距离为 $d$, 现在圆孔中镶嵌以等半径的电极, 设电极的电导率远大于 平板的电导率, 试求二电极间的电阻。

解: 由于二线输电线单位长度的电容为

$$
C_{0}=\frac{\pi \varepsilon_{0}}{\ln \frac{b+h-a}{b-h+a}}
$$

式中 $h=\frac{1}{2} d$, 而 $b=\sqrt{h^{2}-a^{2}}$, 采用静电比拟后, 无限长二圆柱电极对应的单位长度电导应为

$$
G_{0}=\frac{\pi \gamma}{\ln \frac{\frac{d}{2}+\sqrt{(d / 2)^{2}-a^{2}}-a}{-\frac{d}{2}+\sqrt{(d / 2)^{2}-a^{2}}+a}}
$$

厚为 $h$ 的平极电极间电导应为

$$
G=G_{0} h
$$

其对应的电阻为 $G$ 的倒数, 因此

$$
R=\ln \frac{\frac{d}{2}+\sqrt{\frac{1}{4} d^{2}-a^{2}}-a}{-\frac{d}{2}+\sqrt{\frac{1}{4} d^{2}-a^{2}}+a} /(\pi \gamma h)
$$

\section{2. 接地电阻}

电气设备通过引线与埋人地中导体相连接称为接地。一个接地装置的接地电阻主要由接 地的导体 (接地体) 电流流散时, 通过土壤形成。对于引线电阻、接地体自身电阻以及接地体 与大地之间的接触电阻,由于其值相对较小,除非特殊申明,一般不予考虑。

接地电阻的计算与一般电阻的计算完全一样,只是其周围媒质离不开土壤。下面将列举 几种典型接地电极系统的接地电阻的计算。

【例1.7-12】 半径为 $R_{0}$ 的半球接地体, 流出的电流为 $I$, 设土壤的电导率为 $\gamma$, 试求:

(1) 该接地体的接地电阻;

(2) 距球心 $l \mathrm{~m}$ 处向球心行进一步 (步长为 $b \mathrm{~m}$ ) 时的跨步电压;

(3) 若人体的跨步电压允许值为 $U_{\mathrm{ml}}$, 试确定该接地体危险区的半径 (设 $\left.l \gg b\right)$ 。

解: (1) 如图 1.7-10 所示, 由镜像法可知,该半球电流 I 流出的电流是对称的,且

$$
J=\frac{I}{2 \pi r^{2}}, E=\frac{I}{2 \pi \gamma r^{2}}
$$

半球到无穷远处的电压

$$
U=\int_{R_{0}}^{\infty} \frac{I}{2 \pi \gamma r^{2}} \mathrm{~d} r=\frac{I}{2 \pi \gamma R_{0}}
$$



接地体的电阻

$$
R=\frac{U}{I}=\frac{1}{2 \pi \gamma R_{0}}
$$

(2) 设跨步电压为 $U_{l}$, 则

$$
U_{l}=\int_{l-b}^{l} \frac{I}{2 \pi \gamma r^{2}} \mathrm{~d} r=\frac{I}{2 \pi \gamma}\left(\frac{1}{l-b}-\frac{1}{l}\right)
$$

(3) 若 $l \gg b$, 则

$$
\frac{1}{l-b}-\frac{1}{l}=\frac{b}{l(l-b)} \approx \frac{b}{l^{2}}
$$

故有

$$
U_{\mathrm{ml}}=\frac{I b}{2 \pi \gamma l^{2}}
$$

危险区半径

$$
l=\sqrt{\frac{I b}{2 \pi \gamma U_{\mathrm{ml}}}}
$$

一般情况下, 步长 $b$ 及 $U_{\mathrm{m} \mid}$ 均有规定值, 故此危险区半径 $l$ 取决于接地体流出的电流值 $I$ 。

【例 1.7-13】一半径为 $R_{0}$ 的球形接地导体, 深埋土壤中, 若土壤的电导率为 $\gamma$, 试求该接 地体的接地电阻。

解: 此题可视为金属球体在均匀导电媒质中向无穷远处电流流散, 故若设流出的电流为 $I$, 则

$$
\begin{aligned}
& J=\frac{I}{4 \pi r^{2}} e_{r}, E=\frac{J}{\gamma} \\
& U=\int_{R_{0}}^{\infty} \frac{I}{4 \pi \gamma r^{2}} \mathrm{~d} r=\frac{I}{4 \pi \gamma R_{0}}
\end{aligned}
$$

接地电阻为

$$
R=\frac{U}{I}=\frac{1}{4 \pi \gamma R_{0}}
$$

【例 1.7-14】位于悬崖一侧有一半球接地体,如图 1.7-11



解: 由于存在条件 $h \gg R_{0}$, 故本例仍可用例 1.7-12 的方法计 算,即接地电阻

$$
R \approx \frac{1}{2 \pi \gamma R_{0}}
$$

【例 1.7-15】圆柱形接地体如图 1.7-12(a) 所示, 试求其 接地电阻。






解: 这是一种常见的接地体,其计算公式为

$$
R=\frac{1}{2 \pi \gamma L} \ln \frac{4 L}{d}
$$

该公式的推导过程较繁,且为近似计算,现推证如下。

首先利用镜像法可得到一长为 $2 L$ 的模型, 若原模型流出的电流为 $I$, 则新模型在无限大均 匀媒质中流出的电流为 $2 I$ 。由静电比拟可得到图 1.7-12(b), 现假设导体单位长度带电量为 一常数值 $\tau$, 且对外形成的场可视为等于电荷集中在几何轴线上。若以无穷远处为电位参考 点,则在 $z=0$ 的平面上存在

$$
\begin{aligned}
& \mathrm{d} \varphi=\frac{\tau \mathrm{d} z}{4 \pi \varepsilon r^{\prime}}, r^{\prime}=\sqrt{z^{2}+r^{2}} \\
& \varphi=\frac{\tau}{4 \pi \varepsilon} \int_{-L}^{L} \frac{\mathrm{d} z}{\sqrt{z^{2}+r^{2}}}=\frac{\tau}{4 \pi \varepsilon} \ln \frac{L+\sqrt{L^{2}+r^{2}}}{-L+\sqrt{L^{2}+r^{2}}}=\frac{\tau}{4 \pi \varepsilon} \ln \frac{\left(L+\sqrt{L^{2}+r^{2}}\right)^{2}}{r^{2}}
\end{aligned}
$$

当 $r=\frac{d}{2}$ 时,求圆柱表面在 $z=0$ 处的电位。此时再考虑一般情况下存在 $L \gg d$, 则

$$
\varphi=\frac{\tau}{4 \pi \varepsilon} \ln \left(\frac{2 L}{d / 2}\right)^{2}=\frac{\tau}{2 \pi \varepsilon} \ln \frac{4 L}{d}
$$

遵照上述计算方法, 得到的仅是 $z=0$ 处导体表面电位, 但电荷集中在几何轴线上, 以此模 型计算得到的导体表面其他位置的电位并不等于该值。基于工程考虑, 导体应是一个等位体, 当 $L \gg d$ 时,一般取 $z=0$ 处的电位值代表导体电位。显然, 这将是一个近似值, 但一般满足工 程上的需要。

长为 $2 L$ 的导体所带的电荷 $q=\tau 2 L$, 故得孤立导体的电容为

$$
C=\frac{q}{\varphi}=\frac{\tau 2 L}{\frac{\tau}{2 \pi \varepsilon} \ln \frac{4 L}{d}}=\frac{4 \pi \varepsilon L}{\ln \frac{4 L}{d}}
$$

由静电比拟, 长为 $2 L$ 的圆柱导体, 在无限大均匀媒质中产生的电导为

$$
G^{\prime}=\frac{4 \pi \gamma L}{\ln \frac{4 L}{d}}
$$

由于实际的接地体流出电流仅是总电流的一半, 故接地体的电导为

$$
G=\frac{2 \pi \gamma L}{\ln \frac{4 L}{d}}
$$

而接地电阻

$$
R=\frac{1}{G}=\frac{1}{2 \pi \gamma L} \ln \frac{4 L}{d}
$$

$G$ 为 $G^{\prime}$ 的一半, 还可以视为对应于两个电导 $G$ 并联的结果。另外, 流散同样的电流, 接地 体通过的导电媒质仅为无限大均匀媒质的一半, 故电导减半, 而电阻则加倍。

\section{8 恒定磁场}

\section{8 .1 磁感应强度、磁场强度及磁化强度}

\section{1. 磁感应强度}

磁感应强度 $(\boldsymbol{B})$ 是表示磁场强弱的基本物理量。其定义一般用洛仑兹力公式给出,即

$$
f=q(v \times B)
$$

它表示当点电荷 $q$ 以速度 $v$ 运动时, 磁场对运动电荷产生的力大小不仅与电荷运动的速度和 酷感应强度的大小成正比, 而且与速度 $v$ 的方向与磁感应强度的方向之间夹角的正弦值成正 比; 而力的方向符合右手螺旋法则, 即四指由 $\boldsymbol{v}$ 绕到 $\boldsymbol{B}$, 而拇指表示受力方向。

由此不难理解: 当单位正电荷以单位速度垂直磁场运动时, 该电荷受力的大小即表示该点 的磁感应强度的大小。显然, 电荷受力愈大, 表示该点磁场愈强。 $B$ 的单位为特斯拉 $(\mathrm{T})$ 。

静止电荷 $v=0$, 因此不会受到磁场力, 但会受到电场力, 这是区别电场和磁场的重要性质 之一。另外, 力 $f$ 的方向恒与电荷运动的方向相垂直, 故洛仑兹力只能改变运动电荷速度的方 向,而不能改变速度的量值; 换言之, 洛仑兹力不能做功。

(1) 安培力公式

载流导线受到的磁场力, 可通过安培力公式计算。通有电流 $I$ 的导线段 $\mathrm{d} l(\mathrm{~d} l$ 的方向系指 电流密度的方向), 其安培力为

其积分形式为

$$
\mathrm{d} \boldsymbol{f}=I(\mathrm{~d} \boldsymbol{l} \times \boldsymbol{B})
$$

$$
f=I \int \mathrm{d} l \times \boldsymbol{B}
$$

若在均匀磁场中有长为 $l$ 的一段直导线, 则 

$$
\boldsymbol{f}=I(\boldsymbol{l} \times \boldsymbol{B})
$$

当 $l$ 与 $B$ 垂直时,其受力的大小变为

$$
f=I l B
$$

(2) 毕奥-萨伐尔定律

在真空中, 电流 $I$ 所产生的磁场为

$$
\boldsymbol{B}=\frac{\mu_{0}}{4 \pi} \oint_{l} \frac{I \mathrm{~d} l \times \boldsymbol{e}_{r}}{r^{2}}
$$

上式称为毕奥-萨伐尔定律,式中 $\mu_{0}$ 为真空中的磁导率, $\mu_{0}=4 \pi \times 10^{-7}$ 亨利 $/$ 米 $(\mathrm{H} / \mathrm{m})$ 。

上式表示的定律运用于线电流产生的磁场的计算,但若是面电流或体分布电流,其计算式 往往涉及面积分或体积分,一般计算较繁。即

$$
\begin{aligned}
& \boldsymbol{B}=\frac{\mu_{0}}{4 \pi} \oint_{S} \frac{\boldsymbol{K} \times \boldsymbol{e}_{r}}{r^{2}} \mathrm{~d} S \\
& \boldsymbol{B}=\frac{\mu_{0}}{4 \pi} \oint_{V^{\prime}} \frac{\boldsymbol{J} \times \boldsymbol{e}_{r}}{r^{2}} \mathrm{~d} V^{\prime}
\end{aligned}
$$

毕奥-萨伐尔定律运用于无限大真空条件。如果媒质是无限大均匀媒质, 其磁导率为 $\mu$, 则上面各公式中只需将 $\mu_{0}$ 换成 $\mu$ 就成立。但必须指出,毕奥-萨伐尔定律不能计算非均匀媒 质中的磁场。

【例 1.8-1】边长为 $2 a$ 的正方形载流导线如图 1.8-1 所示, 试求该正方形几何中心处的 磁感应强度 $\boldsymbol{B}$ ( 设其周围媒质为真空)。



解: 取电流段 $I \mathrm{~d} l$, 如图所示, 源点坐标为 $\left(a, y^{\prime}, 0\right)$, 而场 点坐标为 $(0,0,0)$, 故有

$$
\begin{aligned}
& r=\sqrt{a^{2}+y^{\prime 2}} \\
& \boldsymbol{e}_{r}=\frac{-a \boldsymbol{e}_{x}-y^{\prime} \boldsymbol{e}_{y}}{\sqrt{a^{2}+y^{\prime 2}}} \\
& \mathrm{~d} \boldsymbol{l}=\mathrm{d} y^{\prime} \boldsymbol{e}_{y} \\
& \mathrm{~d} \boldsymbol{l} \times \boldsymbol{e}_{r}=\frac{a \boldsymbol{e}_{z}}{\sqrt{a^{2}+y^{\prime 2}}} \mathrm{~d} y^{\prime}
\end{aligned}
$$

$A B$ 段电流产生的磁场

$$
\boldsymbol{B}_{1}=\frac{\mu_{0} I}{4 \pi} \int_{l_{A B}} \frac{\mathrm{d} \boldsymbol{l} \times \boldsymbol{e}_{r}}{r^{2}}=\frac{\mu_{0} I}{4 \pi} \int_{-a}^{a} \frac{a \boldsymbol{e}_{z}}{\left(a^{2}+y^{\prime 2}\right)^{3 / 2}} \mathrm{~d} y^{\prime}=\left.\frac{\mu_{0} a I \quad y^{\prime} \boldsymbol{e}_{z}}{4 \pi a^{2} \sqrt{a^{2}+y^{\prime 2}}}\right|_{-a} ^{a}=\frac{\mu_{0} I}{2 \sqrt{2} a \pi} \boldsymbol{e}_{z}
$$

由于对称, 其他三段电流在该点产生的磁场和 $A B$ 电流产生的磁场完成相同, 故得

$$
\boldsymbol{B}=4 \boldsymbol{B}_{1}=\frac{\sqrt{2} \mu_{0} I}{a \pi} e_{z}
$$

本例题采用比较规范的向量运算过程,省去了判别磁场方向由投影关系判断的麻烦,步骤 比较清晰。不难看出,直接用毕奥-萨伐尔定律计算磁场是不容易的。

【例 1.8-2】真空中有一半径为 $R$ 的圆形电流, 如图 1.8-2 所示, 若该电流值为 $I$, 试求其 轴线上任一点处的磁感应强度。

解: 由于对称, $I \mathrm{~d} l$ 在场点产生的 $\mathrm{d} B$ 在垂直 $z$ 轴的平面上必然抵消, 而在 $z$ 轴方向的分量 却互相增强,故由

而 $\mathrm{d} B_{2}=\mathrm{d} B \sin \theta$

代人 $r^{2}=R^{2}+z^{2}, \mathrm{~d} l=R \mathrm{~d} \alpha$ 及 $\sin \theta=\frac{R}{\sqrt{R^{2}+z^{2}}}$

则积分为

$$
\mathrm{d} B=\frac{\mu_{0} I}{4 \pi r^{2}}\left(\mathrm{~d} l \times e_{r}\right)
$$



\section{2. 磁化强度}

$$
B_{z}=\int_{0}^{2 \pi} \frac{\mu_{0} I R}{4 \pi\left(R^{2}+z^{2}\right)^{3 / 2}} R \mathrm{~d} \alpha e_{z}=\frac{\mu_{0} I R^{2}}{2\left(R^{2}+z^{2}\right)^{3 / 2}} e_{z}
$$

磁化强度是描述媒质磁化状态的物理量, 并用 $M$ 表示。它 表示媒质中每单位体积内所有分子磁矩的向量和, 即

$$
M=\lim _{\Delta V \rightarrow 0} \frac{\sum m_{i}}{\Delta V}
$$

式中 $m$ 为分子的磁矩, $m=I S, I$ 表示分子的等效电流强度, $S$ 为分子电流包围的面积, $S$ 的方 向与电流绕向间服从右手螺旋法则。 $\boldsymbol{m}$ 的单位为安 $\cdot$ 米 $^{2}\left(\mathrm{~A} \cdot \mathrm{m}^{2}\right)$, 而 $\boldsymbol{M}$ 的单位为安/米 (A) m) 0

磁化电流强度 $I_{M}$ 表示穿过 $S$ 面上的总磁化电流, 并且

$$
I_{M}=\oint_{l} M \cdot \mathrm{d} l
$$

选化电流密度 $J_{m}$ 满足

$$
J_{m}=\nabla \times M
$$

化电流的面密度 $\boldsymbol{K}_{m}$ 满足

$$
\boldsymbol{K}_{m}=\left(\boldsymbol{M}_{1}-\boldsymbol{M}_{2}\right) \times \boldsymbol{e}_{n}
$$

式中 $e_{n}$ 表示媒质分界面处由第一种媒质指向第二种媒质的单位法向向量。当媒质二中 $\boldsymbol{M}_{2}=$ 0 (例如真空) 时, 则

$$
\boldsymbol{K}_{m}=\boldsymbol{M}_{\mathrm{I}} \times \boldsymbol{e}_{\mathrm{n}}
$$

由分子电流形成的磁化电流和通常意义上的电流 (又称自由电流, 源于自由电荷流动) 一 样, 都可以产生磁场, 只是未被磁化的媒质中, 分子磁矩排列杂乱无章, 对外不显示磁性。在计 算含有媒质区域的磁场时, 只要把磁化电流和自由电流一起考虑进去, 则整个空间可以按照真 穴计算。

\section{3. 磁场强度}

磁化电流计算是比较麻烦的, 工程上一般引人磁场强度这一概念, 再利用描述媒质导磁性 质的一个系数,即磁导率来计算磁场。一般情况下,磁场强度 $\boldsymbol{H}$ 表达式为

$$
\boldsymbol{H}=\frac{\boldsymbol{B}}{\mu_{0}}-\boldsymbol{M}
$$

对于各向同性线性媒质,存在

$$
\boldsymbol{M}=\chi_{m} \boldsymbol{H}
$$

$\chi_{n}$ 称为媒质的磁化率, 是一个纯数, 由此可得 

$$
\boldsymbol{B}=\mu_{0}(\boldsymbol{H}+\boldsymbol{M})=\mu_{0}\left(1+\chi_{m}\right) \boldsymbol{H}=\mu_{0} \mu_{r} \boldsymbol{H}=\mu \boldsymbol{H}
$$

媒质磁导率 $\mu=\mu_{\mathrm{r}} \mu_{0}$, 相对磁导率 $\mu_{\mathrm{r}}=1+\chi_{m}$, 且 $\mu_{\mathrm{r}}=\mu / \mu_{0}$ 。

磁场强度的单位为安/米 $(\mathrm{A} / \mathrm{m})$ 。

【例 1. 8-3】均匀磁化的媒质中磁感应强度为 $B_{0}$, 媒质的相对磁导率为 $\mu_{\mathrm{r}}$, 试求媒质中的 磁化强度。

解: $H=\frac{1}{\mu} B_{0}=\frac{B_{0}}{\mu_{\mathrm{r}} \mu_{0}}$

$$
M=\frac{B_{0}}{\mu_{0}}-H=\frac{B_{0}}{\mu_{0}}-\frac{B_{0}}{\mu_{\mathrm{r}} \mu_{0}}=\frac{B_{0}}{\mu_{0}}\left(1-\frac{1}{\mu_{\mathrm{r}}}\right)=\frac{B_{0}\left(\mu_{\mathrm{r}}-1\right)}{\mu_{\mathrm{r}} \mu_{0}}
$$

\subsection{2 恒定磁场的基本方程和分界面上的衔接条件}

\section{1. 恒定磁场中的基本方程}

\section{积分形式为}

$$
\left\{\begin{array}{l}
\oint_{\boldsymbol{I}} \boldsymbol{H} \cdot \mathrm{d} \boldsymbol{l}=\boldsymbol{\Sigma} I \\
\oint_{S} \boldsymbol{B} \cdot \mathrm{d} S=0
\end{array}\right.
$$

\section{上面二式分别被称为安培环路定律和磁通连续性定理。}

安培环路定律说明磁场强度 $\boldsymbol{H}$ 沿任意闭合回路的线积分恒等于该回路所包围的全部自 由电流, 当 $I$ 与 $\mathrm{d} l$ 的绕向符合右手螺旋法则时取正值, 否则取负值。使用该定理时注意电流 $I$ 必须是回路,不能是一段电流。

磁通连续性定理说明磁场线 (又称磁感应线) 必定是无头无尾的闭合曲线。

恒定磁场基本方程的微分形式为

$$
\left\{\begin{array}{l}
\boldsymbol{\nabla} \times \boldsymbol{H}=\boldsymbol{J}_{S} \\
\boldsymbol{\nabla} \cdot \boldsymbol{B}=0
\end{array}\right.
$$

式中 $J_{\mathrm{S}}$ 表示自由面电流线密度。恒定磁场是有旋场,但是一个无散度源的无散场。

联系二场量的关系式为

$$
\boldsymbol{B}=\mu_{0}(\boldsymbol{H}+\boldsymbol{M})
$$

在各向同性媒质中有

$$
\boldsymbol{B}=\mu \boldsymbol{H}
$$

\section{2. 分界面上的衔接条件}

$$
\left\{\begin{array}{l}
H_{1 t}-H_{2 t}=J_{S} \\
B_{1 n}=B_{2 n}
\end{array}\right.
$$

下标 $t$ 和 $n$ 分别表示切向和法向。面电流线密度 $J_{S}$ 与 $\boldsymbol{H}_{1}$ 绕至 $\boldsymbol{H}_{2}$ 时符合右手螺旋法则时取 正,否则应取负值。用向量形式表示上述关系则存在

$$
\left\{\begin{array}{l}
\left(H_{1}-H_{2}\right) \times e_{n}=J_{S} \\
\left(B_{1}-B_{2}\right) \cdot e_{n}=0
\end{array}\right.
$$

对于各向同性媒质,若分界面处 $\boldsymbol{J}_{S}=0$, 则存在所谓的折射定律 (参照图 1.8-3)

$$
\frac{\tan \alpha_{1}}{\tan \alpha_{2}}=\frac{\mu_{1}}{\mu_{2}}
$$

当 $\mu_{1} \gg \mu_{2}$ 时 (例如铁磁材料相对非铁磁材料), 只要 $\alpha_{1} \neq 90^{\circ}$, 则可近似认为 $\alpha_{2}=0$, 即 $\mu_{2}$ 中的磁场是垂直于分界面的。例如 $\mu_{1}=$ $3000 \mu_{0}, \mu_{2}=\mu_{0}$, 当 $\alpha_{1}=88^{\circ}$ 时, 可由折射定律求得 $\alpha_{2}=33^{\prime}$ 。这一结 论在实用中十分有用。

\section{3. 安培环路定律的应用}

在电流与媒质分布具有对称特性时, 依据安培环路定律和分界 面上的衔接条件, 可以方便地求得某些磁场。

【例 1.8-4】半径为 $a$ 的长直导线通有电流 $I$, 周围是磁导率为 $\mu$ 的均匀媒质, 试求媒质中的 $H 、 B$ 和 $M$ 。



解: 长直导线可认为电流在远处闭合, 故可应用安培环路定律计算。设导线轴线为柱坐标 的 $z$ 轴, 取 $z$ 轴方向与 $I$ 参考方向一致, 则

$$
\begin{aligned}
& \oint_{I} \boldsymbol{H} \cdot \mathrm{d} \boldsymbol{l}=H \cdot 2 \pi r=I \\
& H=\frac{I}{2 \pi r} \\
& B=\mu H=\frac{\mu I}{2 \pi r} \\
& M=\frac{B}{\mu_{0}}-H=\frac{\mu-\mu_{0}}{\mu_{0}} \cdot \frac{I}{2 \pi r}
\end{aligned}
$$

若以长直导线中电流 $I$ 的方向为 $z$ 轴, 则相应的 $B$ 可写为向量形式

$$
B=\frac{\mu I}{2 \pi r} e_{\alpha}
$$

$e_{a}$ 为圆柱坐标系中 $\alpha$ 方向的单位向量。显然, $B$ 与 $Z$ 坐标无关, 是一个平行平面场。

【例 1.8-5】真空中位于 $y O z$ 平面上均匀分布着面电流 $J_{S}=J_{S} \boldsymbol{e}_{z}$, 试求其周围的磁场。



解 : 该电流可以看作由无限多的 $J_{S} \mathrm{~d} y$ 电流组成, 而 $J_{s} \mathrm{~d} y$ 相 当于一细线电流(如图 1.8-4), 它产生的磁场为

$$
\mathrm{d} \boldsymbol{B}=\frac{\mu_{0} J_{S} \mathrm{~d} y}{2 \pi_{T}} \boldsymbol{e}_{\alpha}
$$

由于对称,距离 $y O z$ 平面为 $x$ 位置处的磁感应强度在 $x$ 方 向上的分量将抵消,而 $y$ 方向的分量为 $\mathrm{d} B \cos \theta$, 故当 $x>0$ 时

$$
\begin{aligned}
\boldsymbol{B} & =\frac{\mu_{0} J_{S}}{2 \pi} \int_{-\infty}^{\infty} \frac{\cos \theta}{\sqrt{x^{2}+y^{2}}} \mathrm{~d} y \boldsymbol{e}_{y}=\int_{-\infty}^{\infty} \frac{\mu_{0} J_{S} x}{2 \pi\left(x^{2}+y^{2}\right)} \mathrm{d} y \boldsymbol{e}_{y} \\
& =\left.\frac{\mu_{0} J_{S}}{2 \pi} \arctan \frac{y}{x}\right|_{-\infty} ^{\infty} \boldsymbol{e}_{y}=\frac{\mu_{0} J_{S}}{2} \boldsymbol{e}_{y}
\end{aligned}
$$

当 $x<0$ 时,存在

$$
\boldsymbol{B}=-\frac{\mu_{0} J_{S}}{2} \boldsymbol{e}_{y}
$$

从计算结果可以看出, 无限大面电流形成的磁场到处量值相等,而两侧的 $\boldsymbol{B}$ 反向。

【例 1.8-6】 真空中距离为 $d$ 的两个无限大平面如图1.8-5所示, $A 、 B$ 二平面上分别存在 均面电流 $J_{A}=3 e_{z}, J_{B}=-3 e_{z}$, 试求空间各点的磁感应强度。 



可得 $R_{1}<r<R_{2}$ 时

$$
\begin{aligned}
& H 2 \pi r=\frac{I \pi\left(r^{2}-R_{1}^{2}\right)}{\pi\left(R_{2}^{2}-R_{1}^{2}\right)} \\
& H=\frac{I\left(r^{2}-R_{1}^{2}\right)}{2 \pi\left(R_{2}^{2}-R_{1}^{2}\right) r} \\
& B=\frac{\mu I\left(r^{2}-R_{1}^{2}\right)}{2 \pi\left(R_{2}^{2}-R_{1}^{2}\right) r} e_{\alpha}
\end{aligned}
$$

解:两个平面上的电流分别单独作用, 然后合成得

$$
\begin{aligned}
& \boldsymbol{B}=2 \times \frac{\mu_{0} J_{A}}{2} e_{y}=\mu_{0} J_{A} e_{y}=3 \mu_{0} e_{y} \quad(0<x<d) \\
& B=0 \quad(x<0 \text { 和 } x>d)
\end{aligned}
$$

显然, $A$ 与 $B$ 二平面之间为一均匀磁场, 而二平面之外区间 无磁场。

【例 1.8-7】磁导率为 $\mu$ 的长直管形导体, 通有电流 $I$, 管外 为空气,试求空间各点的磁感应强度。

解:该导体的横断面如图 1.8-6 所示,这是一个满足轴对称 的平行平面场。以轴心 $O$ 为圆心, 任意半径为 $r$ 的圆上 $H$ 相等, 方向与 $e_{\alpha}$ 一致,故由



当 $r>R_{2}$ 时

$$
\boldsymbol{B}=\frac{\mu_{0} I}{2 \pi r} e_{\alpha}
$$

当 $r<R_{1}$ 时

$$
\boldsymbol{B}=0
$$



【例 1. 8-8】磁导率为 $\mu$ 的无穷大导磁平板, 厚度为 $2 a$, 如图 1.8-7 所示。板内有均匀分布的体电流密度 $J=J_{0} e_{z}$, 试求 空间各点的 $B 、 H$ 和 $M$ 。

解: 由于对称, 可判断出 $x O z$ 平面上存在 $\boldsymbol{B}=0 、 \boldsymbol{H}=0 、 \boldsymbol{M}=$ 0 。板内体电流可以视为无穷多的薄片面电流组成, 因此可判 断出 $\boldsymbol{B}$ 将只具有 $x$ 方向分量。在 $x$ 轴上取单位长度,在 $x O y$ 平 面做矩形回路,则 $y$ 方向的两边 $\mathrm{d} \boldsymbol{l}$ 的方向与 $\boldsymbol{B}$ 的方向垂直点 乘为零, 此时安培环路定律仅存在于高为 $y$ 的边上, $\boldsymbol{H}$ 与 $\mathrm{d} \boldsymbol{l}$ 方

向一致,故有

$0<y<a$ 时

$$
\begin{aligned}
& \boldsymbol{H}=-J_{0} y \boldsymbol{e}_{x} \\
& \boldsymbol{B}=-\mu_{0} J_{0} y \boldsymbol{e}_{x} \\
& \boldsymbol{M}=\frac{\boldsymbol{B}}{\mu_{0}}-\boldsymbol{H}=-\frac{\mu-\mu_{0}}{\mu_{0}} J_{0} y \boldsymbol{e}_{x}
\end{aligned}
$$



$$
\begin{aligned}
& \boldsymbol{H}=-J_{0} a \boldsymbol{e}_{x} \\
& \boldsymbol{B}=-\mu_{0} J_{0} a \boldsymbol{e}_{x} \\
& \boldsymbol{M}=0
\end{aligned}
$$

在 $y<0$ 的空间, 其值应取相异符号, 即

$-a<y<0$ 时

$$
\begin{aligned}
& \boldsymbol{H}=J_{0} y \boldsymbol{e}_{x} \\
& \boldsymbol{B}=\mu J_{0} y \boldsymbol{e}_{x} \\
& \boldsymbol{M}=\frac{\mu-\mu_{0}}{\mu_{0}} J_{0} y \boldsymbol{e}_{x}
\end{aligned}
$$

$y<-a$ 时

$$
\begin{aligned}
& \boldsymbol{H}=J_{0} a \boldsymbol{e}_{x} \\
& \boldsymbol{B}=\mu_{0} J_{0} a \boldsymbol{e}_{x} \\
& \boldsymbol{M}=0
\end{aligned}
$$

利用叠加性质, 许多类似此题的多种情况组合均可方便求解。

【例 1.8-9】在真空中, 半径为 $R_{1}$ 的无限长直圆柱内, 除半 径为 $R_{2}$ 的无限长直圆柱外, 均有均匀电流, 其体密度为 $J_{0} e_{s}$, 试 求空洞内任一点的磁感应强度 $\boldsymbol{B}$ 。

解: 由图 1. 8-8 所示, 如果令半径为 $R_{1}$ 圆柱内通有电流 $J_{0} e_{t}$, 而让半径为 $R_{2}$ 圆柱内通有电流 $-J_{0} e_{z}$, 二者叠加即为本题 解。考虑柱对称磁场的方向均为 $e_{\alpha}$ 方向, 分别取二柱中心轴为 2轴,则由安培环路定律可以得到

$$
\boldsymbol{B}=\frac{\mu_{0} J_{0} \pi r_{1}^{2}}{2 \pi r_{1}} \boldsymbol{e}_{\alpha 1}+\frac{-\mu_{0} J_{0} \pi r_{2}^{2}}{2 \pi r_{2}} \boldsymbol{e}_{\alpha 2}=\frac{\mu_{0} J_{0}}{2}\left(r_{1} \boldsymbol{e}_{\alpha 1}-r_{2} \boldsymbol{e}_{\alpha 2}\right)
$$



圆柱坐标系为正交坐标系,存在关系式

$$
e_{\alpha}=e_{z} \times e_{r}
$$

则

$$
\begin{aligned}
\boldsymbol{B} & =\frac{\mu_{0} J_{0}}{2}\left[r_{1}\left(\boldsymbol{e}_{z} \times \boldsymbol{e}_{r 1}\right)-r_{2}\left(\boldsymbol{e}_{z} \times \boldsymbol{e}_{r 2}\right)\right]=\frac{\mu_{0} J_{0}}{2}\left[\boldsymbol{e}_{z} \times\left(\boldsymbol{r}_{1}-\boldsymbol{r}_{2}\right)\right] \\
& =\frac{\mu_{0} J_{0}}{2}\left(\boldsymbol{e}_{z} \times d \boldsymbol{e}_{x}\right)=\frac{\mu_{0} J_{0} d}{2} \boldsymbol{e}_{y}
\end{aligned}
$$


可见空洞内的磁场为一均匀磁场。 上任一点处的磁感应强度。

【例 1.8-10】空气中二平行架设的无限长直导线 (导线材料的 磁导率为 $\mu_{0}$ ) 通有电流 $I$, 如图 1.8-9 所示, 试求过二导线轴线的平面

解: 由所定义的坐标系不难看出, 该平面上 $\boldsymbol{B}$ 只有 $z$ 方向分量。 利用叠加定理, 当左导线单独作用时, 在左导体内部:


$$
\boldsymbol{B}_{1}=\frac{\mu_{0} I \pi\left(x+\frac{d}{2}\right)^{2}}{2 \pi\left(x+\frac{d}{2}\right) \pi R^{2}} \boldsymbol{e}_{z}=\frac{\mu_{0} I\left(x+\frac{d}{2}\right)}{2 \pi R^{2}} \boldsymbol{e}_{z}
$$

在左导线外部:

$$
\boldsymbol{B}_{2}=\frac{\mu_{0} I}{2 \pi\left(x+\frac{d}{2}\right)} \boldsymbol{e}_{z}
$$

当右导线单独作用时,在右导线内部:

在右导线外部:

$$
\boldsymbol{B}_{3}=\frac{-\mu_{0} I \pi\left(x-\frac{d}{2}\right)^{2}}{2 \pi\left(x-\frac{d}{2}\right) \pi R^{2}} \boldsymbol{e}_{z}=\frac{-\mu_{0} I\left(x-\frac{d}{2}\right)}{2 \pi R^{2}} \boldsymbol{e}_{z}
$$

$$
\boldsymbol{B}_{4}=\frac{-\mu_{0} I}{2 \pi\left(x-\frac{d}{2}\right)} e_{z}
$$

由叠加可得在左导线内部:

$$
\boldsymbol{B}=\boldsymbol{B}_{1}+\boldsymbol{B}_{4}=\left[\frac{\mu_{0} I\left(x+\frac{d}{2}\right)}{2 \pi R^{2}}-\frac{\mu_{0} I}{2 \pi\left(x-\frac{d}{2}\right)}\right] \boldsymbol{e}_{z}
$$

在右导线内部:

$$
\boldsymbol{B}=\boldsymbol{B}_{2}+\boldsymbol{B}_{3}=\left[\frac{\mu_{0} I}{2 \pi\left(x+\frac{d}{2}\right)}-\frac{\mu_{0} I\left(x-\frac{d}{2}\right)}{2 \pi R^{2}}\right] \boldsymbol{e}_{;}
$$

在二导线外部:

$$
\boldsymbol{B}=\boldsymbol{B}_{2}+\boldsymbol{B}_{4}=\left[\frac{\mu_{0} I}{2 \pi\left(x+\frac{d}{2}\right)}-\frac{\mu_{0} I}{2 \pi\left(x-\frac{d}{2}\right)}\right] \boldsymbol{e}_{z}
$$

注意: 置于坐标系中, 本题 $x$ 有正有负。



【例 1.8-11】二平行架设的长直输电线通有电流 $I$, 如图 1. 8-10 所示。试求二线连线中垂面上任一点的磁感应强度。 解: 由安培环路定律和叠加定理可得

$$
\begin{aligned}
\boldsymbol{B} & =\boldsymbol{B}_{1}+\boldsymbol{B}_{2}=\frac{\mu_{0} I}{2 \pi r} \cos \theta \boldsymbol{e}_{y}+\frac{\mu_{0} I}{2 \pi r} \cos \theta \boldsymbol{e}_{y} \\
& =\frac{\mu_{0} I \frac{d}{2}}{\pi r r} \boldsymbol{e}_{y}=\frac{\mu_{0} d I}{2 \pi\left(\frac{1}{4} d^{2}+y^{2}\right)} e_{y}
\end{aligned}
$$

【例 1.8-12】一空心圆环如图 1.8-11 所示, 圆环的磁导率为 $\mu$, 且 $\mu$ $>\mu_{0}$, 圆环上均匀密绕有 $N$ 匝线圈, 若线圈中通有电流 $I$, 试求圆环的平均 半径处的磁感应强度和圆环内的平均磁感应强度。

解:平均半径

$$
R=\frac{R_{1}+R_{2}}{2}
$$

在该位置处, 由安培环路定律得



$$
B_{0}=\frac{\mu N I}{2 \pi R}=\frac{\mu N I}{\pi\left(R_{1}+R_{2}\right)}
$$

设环内任一半径处半径为 $r$, 则

$$
B=\frac{\mu N I}{2 \pi r}
$$

其平均值

$$
B_{\mathrm{av}}=\frac{1}{R_{2}-R_{1}} \int_{R_{1}}^{R_{2}} \frac{\mu N I}{2 \pi r} \mathrm{~d} r=\frac{\mu N I}{2 \pi\left(R_{2}-R_{1}\right)} \ln \frac{R_{2}}{R_{1}}
$$

【例 1.8-13】一长直螺线管, 单位长度绕有 $N$ 匝线圈, 若线圈通有电流 $I$, 螺线管内的磁 导率为 $\mu_{0}$, 试求螺线管内的磁感应强度 $B$ 。

解: 此问题的严格计算并不简单, 螺线管内无论沿轴向还是沿径向, 其磁感应强度 $B$ 的大 小都有差异。但如果螺线管很长, 而螺线管的横截面积又相对较小, 则在螺线管中绝大部分区 域可近似认为其磁场是均匀的,并存在

$$
B=\mu_{0} N I
$$

该式的推导方法之一是利用分界面条件,即

$$
H_{1 t}-H_{2 t}=J_{S}
$$

嫘线管内的磁场只具切向分量, 并且远大于管外的磁场, 而分界面处的 $N$ 匝电流等效为单位 长度上的面电流, 故有管内磁场强度

$$
H=N I
$$

而

$$
B=\mu_{0} H=\mu_{0} N I
$$

显然, 这个结果是近似值。



【例 1. 8-14】两种媒质以 $y O z$ 平面为分界面, 如图 1.8-12 所示, 若媒质 $\mu_{1}$ 中的磁场强度 $H_{1}=3 e_{x}+4 e_{y}+5 e_{z} \mathrm{~A} / \mathrm{m}$, 分界面上存在面电 流线密度 $J_{S}=e_{z} \mathrm{~A} / \mathrm{m}$, 求媒质 $\mu_{2}$ 中分界面处的磁场强度。

解: $H_{1}$ 中 $y$ 方向和 $z$ 方向分量构成分界面处的切向分量。由

$$
H_{1}-H_{2 t}=J_{S}
$$

可得

$$
H_{1 z}=H_{2 z}=5
$$

$$
\text { .. } H_{1 y}-H_{2 y}=-J_{S}
$$

$$
H_{2 y}=H_{1 y}+J_{S}=4+1=5
$$

$H_{1}$ 的 $x$ 方向分量是分界面的法线方向, 故由 $B_{1 n}=B_{2 n}$ 可得 合成后存在

$$
\begin{aligned}
& \mu_{1} H_{1 x}=\mu_{2} H_{2 x} \\
& H_{2 x}=\frac{\mu_{1}}{\mu_{2}} H_{1 x}=3 \frac{\mu_{1}}{\mu_{z}}
\end{aligned}
$$

$$
\boldsymbol{H}_{2}=3 \frac{\mu_{1}}{\mu_{2}} \boldsymbol{e}_{x}+5 \boldsymbol{e}_{y}+5 \boldsymbol{e}_{z} \mathrm{~A} / \mathrm{m}
$$

\section{8 .3 自感与互感}

电感可分为自感与互感两种概念, 自感又可分为内自感和外自感两种不同的计算方法。 研究电感离不开磁通和磁链。所谓磁通即表示某面积上磁感应强度的通量, 即

$$
\phi=\int_{S} \boldsymbol{B} \cdot \mathrm{d} \boldsymbol{S}
$$

磁通是一个标量, 在设定的参考方向下, 有正负之分, 类似于电流强度。磁通的单位为韦伯 $(\mathrm{Wb})$ 。

磁链与磁通相交链的电流相关, 一个通有电流 $I$ 的 $n$ 匝线圈, 其磁链

$$
\Psi=\phi_{1}+\phi_{2}+\cdots+\phi_{n}
$$

式中 $\phi_{i}$ 为每一匝线圈通过的磁通。如果每匝线圈通过的磁通都为 $\phi$, 则

$$
\Psi=n \phi
$$

对于磁通包围的电流不足一匝的情况, 必须引人分数匝概念, 此时将存在关系式

$$
\mathrm{d} \Psi=\frac{I^{\prime}}{I} \mathrm{~d} \phi
$$

\section{1. 自感}

(1)内自感

内自感由导体内部磁链产生, 此时磁通包围的电流为分数匝, 典型计算如下。



设半径为 $R$ 的长直导线通有均匀分布的电流 $I$, 如图 1.8-13 所示。该导线内部的磁感应强度

$$
B=\frac{\mu_{0} I \pi r^{2}}{2 \pi r \pi R^{2}}=\frac{\mu_{0} I r}{2 \pi R^{2}}
$$

取轴向长度为 $l$ 、宽为 $\mathrm{d} r$ 的矩形面积元, $\mathrm{d} r$ 是微分量, 故在该面积 元上 $B$ 可视为常量,因此

$$
\mathrm{d} \phi_{i}=B \mathrm{~d} S=\frac{\mu_{0} I r}{2 \pi R^{2}} l \mathrm{~d} r
$$

由 $\mathrm{d} \phi_{i}$ 包围的电流不是 $I$, 而是导线中全部电流的一部分, 相当于

一匝电流的比例为

$$
\frac{I^{\prime}}{I}=\frac{I \pi r^{2}}{I \pi R^{2}}=\frac{r^{2}}{R^{2}}
$$

由此得内磁链微分量为

$$
\mathrm{d} \Psi_{i}=\frac{I^{\prime}}{I} \mathrm{~d} \phi_{i}=\frac{\mu_{0} I l r^{3}}{2 \pi R^{4}} \mathrm{~d} r
$$

内磁链 

$$
\Psi_{i}=\int_{S} \mathrm{~d} \Psi_{i}=\int_{0}^{R} \frac{\mu_{0} I l r^{3}}{2 \pi R^{4}} \mathrm{~d} r=\frac{\mu_{0} I l}{8 \pi}
$$

内自感

$$
L_{i}=\frac{\Psi_{i}}{I}=\frac{\mu_{0} l}{8 \pi}
$$

单位长度的内自感为一常数, 即

$$
L_{i 0}=\frac{L_{i}}{l}=\frac{\mu_{0}}{8 \pi}
$$

显然, 长直圆导线的内自感与导线半径 $R$ 无关, 而单位长直圆导线的内自感为一定值, 这 一结论十分重要。如果导线的磁导率不是 $\mu_{0}$, 而换上其相应的磁导率 $\mu$ 时, 这一结论仍然正 确。二线输电线往返有两颗导线, 只要是实心导体, 则其单位长度的内自感应为 $2 \frac{\mu_{0}}{8 \pi}=\frac{\mu_{0}}{4 \pi}$ 。 上述结论具有普遍的应用意义。

(2)外自感

外自感不涉及分数匝概念,其一般计算公式为

$$
L_{0}=\frac{\Psi_{0}}{I}
$$

【例1.8-15】导线半径为 $R$ 的二线输电线,轴线间距离为 $d$,周围 为空气,试求其单位长度的自感。

解: 其计算模型如图 1.8-14 所示。设导线中流动的电流为 $I$, 则二 导线轴线所在平面上,左导线单独作用时

$$
B_{1}=\frac{\mu_{0} I}{2 \pi r}
$$

二导线间单位长度上,由 $B_{1}$ 形成的磁通

$$
\phi_{1}=\int_{S} \boldsymbol{B}_{1} \cdot \mathrm{d} S=\int_{R}^{\mathrm{d}-R} \frac{\mu_{0} I}{2 \pi r} \mathrm{~d} r=\frac{\mu_{0} I}{2 \pi} \ln \frac{d-R}{R}
$$



由于对称,右导线在二导线间形成的磁通与 $\phi_{1}$ 大小相等,方向相同。故二导线形成的外 酳通(单回路磁通即外磁链)

$$
\phi_{0}=2 \phi_{1}=\frac{\mu_{0} I}{\pi} \ln \frac{d-R}{R}
$$

外自感

$$
L_{0}=\frac{\phi_{0}}{I}=\frac{\mu_{0}}{\pi} \ln \frac{d-R}{R}
$$

二线输电线单位长度的内自感为 $\frac{\mu_{0}}{4 \pi}$, 故单位长度的自感为

$$
L=L_{0}+L_{i}=\frac{\mu_{0}}{\pi} \ln \frac{d-R}{R}+\frac{\mu_{0}}{4 \pi}
$$

如果 $R \ll d$, 则上式变为

$$
L=\frac{\mu_{0}}{\pi} \ln \frac{d}{R}+\frac{\mu_{0}}{4 \pi}
$$





【例 1.8-16】试求图 1.8-15 所示同轴电缆单位长度的自感。 解: 设内外导体流动的电流为 $I$, 由安培环路定律不难得到

$$
\begin{aligned}
& B_{1}=\frac{\mu_{0} I r}{2 \pi R_{1}^{2}} \quad\left(r \leqslant R_{1}\right) \\
& B_{2}=\frac{\mu_{0} I}{2 \pi r} \quad\left(R_{1} \leqslant r \leqslant R_{2}\right) \\
& B_{3}=\frac{\mu_{0}\left[I-\frac{I \pi\left(r^{2}-R_{2}^{2}\right)}{\pi\left(R_{3}^{2}-R_{2}^{2}\right)}\right]}{2 \pi r}=\frac{\mu_{0} I\left(R_{3}^{2}-r^{2}\right)}{2 \pi r\left(R_{3}^{2}-R_{2}^{2}\right)} \quad\left(R_{2} \leqslant r \leqslant R_{3}\right)
\end{aligned}
$$

内导体为实心圆导线,故内自感为

$$
L_{1}=\frac{\mu_{0}}{8 \pi}
$$

外导体的磁链

$$
\begin{aligned}
\Psi_{3} & =\int_{R_{2}}^{R_{3}} \frac{I^{\prime}}{I} B_{3} \mathrm{~d} r=\int_{R_{2}}^{R_{3}} \frac{I-\frac{I \pi\left(r^{2}-R_{2}^{2}\right)}{\pi\left(R_{3}^{2}-R_{2}^{2}\right)}}{I} B_{3} \mathrm{~d} r=\int_{R_{2}}^{R_{3}} \frac{\mu_{0} I\left(R_{3}^{2}-r^{2}\right)^{2}}{I r\left(R_{3}^{2}-R_{2}^{2}\right)^{2}} \mathrm{~d} r \\
& =\frac{\mu_{0} I R_{3}^{4}}{2 \pi\left(R_{3}^{2}-R_{2}^{2}\right)^{2}} \ln \frac{R_{3}}{R_{2}}-\frac{\mu_{0} I R_{3}^{2}}{2 \pi\left(R_{3}^{2}-R_{2}^{2}\right)}+\frac{\mu_{0} I\left(R_{3}^{2}+R_{2}^{2}\right)}{8 \pi\left(R_{3}^{2}-R_{2}^{2}\right)}
\end{aligned}
$$

外导体的内自感

$$
L_{3}=\frac{\Psi_{3}}{I}=\frac{\mu_{0} R_{3}^{4}}{2 \pi\left(R_{3}^{2}-R_{2}^{2}\right)^{2}} \ln \frac{R_{3}}{R_{2}}-\frac{\mu_{0} R_{3}^{2}}{2 \pi\left(R_{3}^{2}-R_{2}^{2}\right)}+\frac{\mu_{0}\left(R_{3}^{2}+R_{2}^{2}\right)}{8 \pi\left(R_{3}^{2}-R_{2}^{2}\right)}
$$

内外导体间单位长度的外自感

$$
L_{2}=\frac{\phi_{2}}{I}=\int_{R_{1}}^{R_{2}} \frac{\mu_{0}}{2 \pi r} \mathrm{~d} r=\frac{\mu_{0}}{2 \pi} \ln \frac{R_{2}}{R_{1}}
$$

同轴电缆单位长度的总自感

$$
L=L_{1}+L_{2}+L_{3}
$$

本例题计算量较大, 但 $L_{1} 、 L_{2}$ 和 $L_{3}$ 任何一个值都可以单独进行计算, 只有 $L_{3}$ 计算积分比 较麻烦。同轴电缆的外导体的内自感不能使用 $\frac{\mu_{0}}{8 \pi}$, 原因是它不是实心圆导线。

【例 1.8-17】内外半径分别为 $R_{1}$ 和 $R_{2}$ 的长直圆管形导体, 磁导率为 $\mu_{0}$, 其单位长度的 内自感为多大?

解: 设圆管中通有电流 $I$, 则

$$
\begin{aligned}
& B=\frac{\mu_{0} I\left(r^{2}-R_{1}{ }^{2}\right)}{2 \pi r\left(R_{2}{ }^{2}-R_{1}^{2}\right)} \\
& \mathrm{d} \Psi_{i}=\frac{I^{\prime}}{I} \mathrm{~d} \varphi_{i}=\frac{\mu_{0} I\left(r^{2}-R_{1}{ }^{2}\right)^{2}}{2 \pi r\left(R_{2}{ }^{2}-R_{1}{ }^{2}\right)^{2}} \mathrm{~d} r
\end{aligned}
$$

显然, 这一个结果与上题中 $\Psi_{3}$ 中的被积函数形式完全相似, 只是 $R_{3}$ 和 $R_{2}$ 的值被 $R_{2}$ 和 $R_{1}$ 所 代替,因此本题的解答为

$$
L=\frac{\mu_{0} R_{2}{ }^{4}}{2 \pi\left(R_{2}{ }^{2}-R_{1}{ }^{2}\right)} \ln \frac{R_{2}}{R_{1}}-\frac{\mu_{0} R_{2}{ }^{2}}{2 \pi\left(R_{2}{ }^{2}-R_{1}{ }^{2}\right)}+\frac{\mu_{0}\left(R_{2}{ }^{2}+R_{1}{ }^{2}\right)}{8 \pi\left(R_{2}{ }^{2}-R_{1}{ }^{2}\right)}
$$

【例 1.8-18】横截面为长方形的铁磁镯环, 高为 $a$, 镯环内外半径分别为 $R_{1}$ 和 $R_{2}$, 铁磁 材料的磁导率为 $\mu$, 镯环上均匀密绕有 $N$ 匝导线 (如图 1.8-16 所示), 试求镯环的自感。

解: 设导线中流过电流为 $I$, 则

$$
\begin{aligned}
& B=\frac{\mu I N}{2 \pi r} \\
& \phi=\int_{S} B \cdot \mathrm{d} S=\int_{R_{1}}^{R_{2}} \frac{\mu I N}{2 \pi r} a \mathrm{~d} r=\frac{\mu I a N}{2 \pi} \ln \frac{R_{2}}{R_{1}}
\end{aligned}
$$

钽环为铁磁材料, 可认为 $\Psi=N \phi$, 故

$$
L=\frac{\Psi}{I}=\frac{\mu a N^{2}}{2 \pi} \ln \frac{R_{2}}{R_{1}}
$$

\section{2. 互感}

由线圈 1 的电流 $I_{1}$ 所产生的磁场, 在线圈 2 中产生的磁链为



$$
M_{21}=\frac{\Psi_{21}}{I_{1}}
$$

同理,线圈 2 对线圈 1 的互感定义为

$$
M_{12}=\frac{\Psi_{12}}{I_{2}}
$$

在各向同性线性媒质中,存在关系式

$$
M_{21}=M_{12}
$$

互感与线圈的几何形状、大小、二线圈的相对位置和周围的媒质有关。为了计算互感,通常也 需要在一个线圈中通以电流, 求出另一线圈所在回路的磁链, 然后得出 $M$ 值。

两线形回路的互感存在计算公式

$$
M_{12}=M_{21}=\frac{\mu_{0}}{4 \pi} \oint_{l 1} \oint_{12} \frac{\mathrm{d} l_{1} \cdot \mathrm{d} l_{2}}{r}
$$

上式称为聂以曼公式,有时也用来计算线圈的外自感。但是,上式中两个闭合回路的线积分计 算比较麻烦,因此只有典型的几个特例才可求得其解析解。



【例 1.8-19】两对平行架设的传输线 $A B$ 与 $C D$ 如图 1.8-17 所 示,试求它们之间单位长度的互感。

解 : 设 $A B$ 对传输线通有电流 $I$ 。 $A$ 导线单独作用时,在 $C D$ 连线 并沿轴向取单位长构成的面积上产生的磁通,可由下式计算：

$$
\phi_{A}=\int_{R_{A C}}^{R_{A D}} \frac{\mu_{0} I}{2 \pi r} \mathrm{~d} r=\frac{\mu_{0} I}{2 \pi} \ln \frac{R_{A D}}{R_{A C}}
$$

式中积分限取 $R_{A C}$ 和 $R_{A D}$ 的原因是: 磁场中穿过 $C D$ 所在的平面与穿 过由 $R_{A C}$ 和 $R_{A D}$ 界定的区域是相同的。

同理, $B$ 导线单独作用在该面上产生的磁通

$\phi_{B}=\frac{\mu_{0} I}{2 \pi} \ln \frac{R_{B C}}{R_{B D}}$ 

$$
\begin{aligned}
& \phi=\phi_{A}+\phi_{B}=\frac{\mu_{0} I}{2 \pi} \ln \frac{R_{A D} R_{B C}}{R_{A C} R_{B D}} \\
& M=\frac{\phi}{I}=\frac{\mu_{0}}{2 \pi} \ln \frac{R_{A D} R_{B C}}{R_{A C} R_{B D}}
\end{aligned}
$$

如果二对输电线的中垂线 (断面图中)一致, 则 $R_{A C}=R_{B D}, R_{A D}=R_{B C}$, 上式变为

$$
M=\frac{\mu_{0}}{\pi} \ln \frac{R_{A D}}{R_{A C}}
$$

如果 $C D$ 位于 $A B$ 连线的中垂线上, 则存在 $R_{A C}=R_{B C}, R_{A D}=R_{B D}$, 此时 $M=0$ 。显然, 此时二 对输电线间无电磁千扰。



【例 1.8-20】矩形单匝线圈与二平行架设的输电线位于同 一平面上,相互位置及有关尺寸如图 1.8-18 所示, 试求二线圈之 间的互感 $M$ 。

解: 设二线输电线中通有电流 $I$, 并设穿人纸面的磁通为正, 则

$$
B=\frac{\mu_{0} I}{2 \pi r_{1}}-\frac{\mu_{0} I}{2 \pi r_{2}}
$$

式中 $r_{1}$ 和 $r_{2}$ 分别为导线右侧处平面上任一点距离右侧导线和左 侧导线的距离。

$$
\begin{aligned}
& \phi=\int_{S} \boldsymbol{B} \cdot \mathrm{d} \boldsymbol{S}=\int_{d+a}^{d+a+b}-\frac{\mu_{0} I}{2 \pi r_{2}} c \mathrm{~d} r_{2}+\int_{a}^{a+b} \frac{\mu_{0} I}{2 \pi r_{1}} c \mathrm{~d} r_{1}=\frac{\mu_{0} I c}{2 \pi} \ln \frac{(a+b)(d+a)}{a(d+a+b)} \\
& M=\frac{\phi}{I}=\frac{\mu_{0} c}{2 \pi} \ln \frac{(a+b)(d+a)}{a(d+a+b)}
\end{aligned}
$$

【例 1.8-21】在 $x O y$ 平面上有一三角形单匝回路, $y$ 轴上 有一无限长直导线, 周围为空气, 试求它们之间的互感。（相 互间位置如图 1.8-19 所示)

解: 设 $y$ 轴上的导线流过电流为 $I$, 则

$$
B=\frac{\mu_{0} I}{2 \pi x}
$$

三角形斜边的表达式为



$$
y=\frac{c}{b-a}(x-a)
$$

由于 $B$ 仅为 $x$ 的函数,故在 $y \mathrm{~d} x$ 的微小面积上 $B$ 可视为常量。磁通

$$
\begin{aligned}
& \phi=\int_{S} \boldsymbol{B} \cdot \mathrm{d} S=\int_{a}^{b} \frac{\mu_{0} I}{2 \pi x} \cdot \frac{c}{b-a}(x-a) \mathrm{d} x=\frac{\mu_{0} I c}{2 \pi(b-a)}\left[(b-a)-a \ln \frac{b}{a}\right] \\
& M=\frac{\phi}{I}=\frac{\mu_{0} c}{2 \pi}-\frac{\mu_{0} a c}{2 \pi(b-a)} \ln \frac{b}{a}
\end{aligned}
$$

无限长直导线本身可以视为无限大半径的回路, 在有限区间则表示为一直线, 故本题的实 质仍是二回路之间的互感。

【例 1.8-22】铁磁材料制成的圆环上绕有线圈 1, 线圈的匝数为 $N_{1}$, 今已测得该线圈的 自感为 $L_{1}$, 若磁通全部通过圆环内部, 试问在圆环上另一线圈 (匝数为 $N_{2}$ ) 与线圈 1 之间的互 感。

解: 设线圈 1 通有电流 $I_{1}$, 则

$$
L_{1}=\frac{\Psi_{1}}{I_{1}}=\frac{N_{1} \phi}{I_{1}}
$$

线圈 2 穿过的磁通仍为 $\phi$, 故有

$$
M=\frac{\Psi_{21}}{I_{1}}=\frac{N_{2} \phi}{I_{1}}
$$

解得

$$
M=\frac{N_{2}}{N_{1}} L_{1}
$$

1.8.4 磁场能量和磁场力

\section{1. 磁场能量}

磁场能量的体密度 $w_{m}$ : 表示单位体积中的磁场能量, 其计算公式为

$$
w_{m}=\frac{1}{2} \boldsymbol{H} \cdot \boldsymbol{B}
$$

对于各向同性线性媒质存在

$$
w_{m}=\frac{1}{2} \mu H^{2}=\frac{1}{2 \mu} B^{2}
$$

体积 $V$ 内的磁场能量

$$
W_{m}=\int_{V} \frac{1}{2} \mu H^{2} \mathrm{~d} V=\int_{V} \frac{1}{2 \mu} B^{2} \mathrm{~d} V
$$

(1) 单回路场源系统

$$
W_{m}=\frac{1}{2} L I^{2}=\frac{1}{2} I \Psi
$$

这是回路电流的自有能。

(2) 具有 $N$ 个电流回路场源的磁场

$$
W_{m}=\frac{1}{2} \sum_{i=1}^{N} L_{i} I_{i}^{2}+\left.\frac{1}{2} \sum_{i=1}^{N} \sum_{j=1}^{N} M_{i j} I_{i} I_{j}\right|_{i \neq j}
$$

或

$$
W_{m}=\frac{1}{2} \sum_{i=1}^{N} I_{k} \Psi_{k}
$$

式中与 $L_{i}$ 相关的能量称为系统的自有能; 与 $M_{i j}$ 相关的能量称为系统的互有能, 它表示各电流 回路之间的相互作用能。

\section{2. 磁场力}

(1) 洛仑兹力公式

磁场对运动点电荷 $q$ 的作用力

$$
f=q(\boldsymbol{v} \times \boldsymbol{B})
$$

(2) 安培力公式

磁场对载流导线的作用力 

$$
f=\int_{l} I \mathrm{~d} l \times B
$$

(3) 虚位移法


(4) 用毕奥-萨伐尔定律计算磁场力

$$
f_{21}=\frac{\mu_{0}}{4 \pi} \oint_{l_{1}} \oint_{h_{2}} \frac{I_{2} \mathrm{~d} l_{2} \times\left(I_{1} \mathrm{~d} l_{1} \times e_{r}\right)}{r^{2}}
$$

显然, 这一表达式比较复杂, 计算也很繁, 但它是与库仑定律相对应的磁场实验定律, 具有重要 的理论价值。至于公式中各符号和方向的意义, 可参阅本科生相关教材, 此处不再一一介绍。

(5) 法拉第观点

法拉第认为: 由磁感应强度线 (磁场线) 构成的磁感应管沿其轴向受到纵张力, 同时在其 垂直方向上受到侧压力, 此二力量值相等, 其单位面积受到的力均等于该处磁场能量的体密 度。

另外, 在两种媒质的分界面上, 不论磁场的方向如何, 分界面受到的力总是与分界面垂直, 并且力的方向总是由磁导率较大的媒质指向磁导率较小的媒质。当分界面处无面电流时, $H_{\mathrm{it}}$ $=H_{21}, B_{1 n}=B_{2 n}$, 若 $\mu_{2}>\mu_{1}$, 则单位面积上的力

$$
f_{0}=\frac{1}{2}\left(\frac{B_{1 n}^{2}}{\mu_{1}}-\frac{B_{2 n}^{2}}{\mu_{2}}\right)+\frac{1}{2}\left(\mu_{2} H_{2 t}^{2}-\mu_{1} H_{1 t}^{2}\right)=\frac{\mu_{2}-\mu_{1}}{2 \mu_{1} \mu_{2}}\left(B_{1 n}^{2}+\mu_{1} \mu_{2} H_{1 t}^{2}\right)
$$

利用法拉第的观点, 有时可以十分方便地求得磁场力。

【例 1.8-23】内导体半径为 $R_{1}$, 外导体半径为 $R_{2}$ 的同轴电缆, 通有电流 $I$, 中间媒质的磁 导率为 $\mu_{0}$, 试求该电缆单位长度内外导体间储存的磁场能量。

解: 由安培环路定律

$$
H=\frac{I}{2 \pi r} \quad\left(R_{1}<r<R_{2}\right)
$$

可求得

$$
W_{m}=\int_{v} \frac{1}{2} \mu_{0} H^{2} \cdot \mathrm{d} V=\int_{R_{2}}^{R_{1}} \frac{1 \quad \mu_{0} I^{2}}{2(2 \pi r)^{2}} 2 \pi r \mathrm{~d} r=\int_{R_{1}}^{R_{2}} \frac{\mu_{0} I^{2}}{4 \pi r} \mathrm{~d} r=\frac{\mu_{0} I^{2}}{4 \pi} \ln \frac{R_{2}}{R_{1}}
$$

由同轴电缆单位长度的外自感



$$
L_{0}=\frac{\mu_{0}}{2 \pi} \ln \frac{R_{2}}{R_{1}}
$$

利用公式 $W_{m}=\frac{1}{2} L_{0} I^{2}$, 同样可求得 $W_{m}$ 值。

【例 1.8-24】二线输电线与一矩形单匝线圈位于同一平面内, 有关 尺寸如图 1.8-20 所示, 若在矩形线圈中通有电流 $I_{2}$, 试求:

(1) 在二线输电线回路中产生的磁通 $\phi$;

(2) 若线圈为刚性线圈, 今在二线输电线中通有电流 $I_{1}\left(I_{1}\right.$ 方向为左 导线向上,右导线向下), 则线圈所受的力为多大?

解: (1) 单匝回路中, 由

$$
M_{12}=\frac{\phi_{12}}{I_{2}}, M_{21}=\frac{\phi_{21}}{I_{1}}, M_{12}=M_{21}
$$

可得

$$
\frac{\phi_{12}}{I_{2}}=\frac{\phi_{21}}{I_{1}}
$$

令 $I_{1}=I_{2}$, 则可得 $\phi_{12}=\phi_{21}$, 故若二线输电线通以电流 $I_{2}$, 则线圈区间存在

$$
B=\frac{\mu_{0} I_{2}}{2 \pi r_{1}}+\frac{\mu_{0} I_{2}}{2 \pi r_{2}}
$$

$r_{1}$ 与 $r_{2}$ 分别为距离左右二导线距离。故有

$$
\phi=\int_{S} \boldsymbol{B} \cdot \mathrm{d} S=\int_{a}^{a+b} \frac{\mu_{0} I_{2} c}{2 \pi r_{1}} \mathrm{~d} r_{1}+\int_{d-a-b}^{d-a} \frac{\mu_{0} I_{2} c}{2 \pi r_{2}} \mathrm{~d} r_{2}=\frac{\mu_{0} I_{2} c}{2 \pi} \ln \frac{(a+b)(\mathrm{d}-a)}{a(\mathrm{~d}-a-b)}
$$

(2) 由 (1) 知, 二回路间互感

$$
M=\frac{\phi}{I_{2}}
$$

故当二回路各通有 $I_{1}$ 和 $I_{2}$ 时, 其互有能

$$
W_{m}=M I_{1} I_{2}=\frac{\mu_{0} I_{1} I_{2} c}{2 \pi} \ln \frac{(a+b)(\mathrm{d}-a)}{a(d-a-b)}
$$

对于刚性线圈,假设 $a$ 移动,而 $b$ 和 $c$ 不变,其所受的力

$$
f=\left.\frac{\partial W_{m}}{\partial a}\right|_{I_{k}=\text { 每数 }}=\frac{\mu_{0} I_{1} I_{2} c}{2 \pi}\left(\frac{1}{a+b}-\frac{1}{\mathrm{~d}-a}-\frac{1}{a}+\frac{1}{\mathrm{~d}-a-b}\right)
$$

力 $f$ 的方向为使 $a$ 增大的方向。

此题也可以通过安培力公式,计算由 $I_{1}$ 产生的磁场对 $I_{2}$ 产生作用力。计算过程如下:

$$
B_{1}=\frac{\mu_{0} I_{1}}{2 \pi r_{1}}+\frac{\mu_{0} I_{1}}{2 \pi r_{2}}
$$

由于是直导线, 根据公式

$$
f=I_{2} \oint_{l}(\mathrm{~d} l \times B)
$$

此时矩形上下边受的力大小相等, 方向相反而抵消, 左右两边受力可用左手定则给出方向。若 假设力的方向向右为正, 则

$$
f=-\left.I_{2} c B_{1}\right|_{\substack{r_{1}=a \\ r_{2}=d-a}}+\left.I_{2} c B_{1}\right|_{\substack{r_{1}=a+b \\ r_{2}=d-a-b}}
$$

代人后结果与虚位移法计算的结果相同。若引人坐标系,该计算过程用向量计算也很方便。

【例 1.8-25】一匝数为 $N$ 的环形细线圈位于均匀磁场中, 如图 1.8-21 所示, 外磁场的磁 感应强度为 $B_{0}$, 线圈的法向与磁场间夹角为 $\alpha$, 线圈所围成的面积为 $S$, 并通有电流 $I$, 试求线 圈所受的力矩 $T_{\text {。 }}$

解: $\Psi=N \int_{S} \boldsymbol{B} \cdot \mathrm{d} \boldsymbol{S}=N B_{0} S \cos \alpha$ 互有能

$$
W_{m}=I \Psi=N B_{0} I S \cos \alpha
$$

著广义力为力矩, 广义几何坐标对应的是角度, 故

$$
T=\left.\frac{\partial W_{m}}{\partial \alpha}\right|_{l=\text { 常数 }}=-N I B_{0} S \sin \alpha
$$



【例 1.8-26】在某分界面处, 磁感应强度 $\boldsymbol{B}$ 垂直于铁磁材料进人空气中, $B=0.1 \mathrm{~T}$, 若铁 磁材料的磁导率 $\mu=1000 \mu_{0}$, 试求分界面处铁磁材料单位面积受到的力。

解: 此题可直接应用法拉第的观点, 用能量体密度计算, 力的方向由铁磁材料指向空气。 由于 $B_{1 n}=B_{2 n}$, 分界面处二媒质中 $B$ 相同, 故

$$
f_{0}=\frac{1 B^{2}}{2 \mu_{0}}-\frac{1 B^{2}}{2 \mu}=\frac{B^{2}}{2 \mu_{0}}\left(1-\frac{1}{1000}\right) \approx \frac{B^{2}}{2 \mu_{0}}=\frac{0.1^{2}}{2 \times 4 \pi \times 10^{-7}}=3.98 \times 10^{3} \mathrm{~N} / \mathrm{m}^{2}
$$



【例 1.8-27】一电磁铁如图 1.8-22 所示, 设电磁铁的横截 面积为 $S$, 空气隙 $l$ 很小, 计算时可忽略边缘效应, 若保持电磁铁 中的磁通 $\phi$ 不变, 试求该电磁铁的吸力。

解: 空气中的磁场能量由两侧组成, 空气隙中的磁场可认为 是一均匀磁场,因此

磁场力

$$
W_{m}=w_{m} V=\frac{B^{2}}{2 \mu_{0}} 2 s l=\frac{\phi^{2}}{2 \mu_{0} s^{2}} 2 s l=\frac{\phi^{2} l}{\mu_{0} s}
$$

$$
f=-\left.\frac{\partial W_{m}}{\partial l}\right|_{\phi=\text { 娄数 }}=\frac{-\phi^{2}}{\mu_{0} S}
$$

式中负号表示该力是吸力,即使 $l$ 减小的方向。

\section{9 均匀传输线}

\subsection{1 均匀传输线的基本方程和正弦稳态分析方法}

\section{1. 均匀传输线的基本方程}

均匀传输线的定义:沿传输线路的电阻、电感、电导和电容是均匀分布的传输线。

假设均匀传输线的传输方向为 $x$ 方向, 传输线的始端 (电源端) 为 $x=0$, 则均匀传输线沿 线路各处的电流和电压将表现为距离 $x$ 和时间 $t$ 的函数。

任何电路的参数分布都是沿线分布的,构成特定的 均匀传输线求解问题还必须认识到: 由于电磁能量以有 限速度向空间传播, 当所研究的线路长度与电磁波波长 的长度可比时, 此时应该采用分布参数电路的特定求解 方法, 而不能再用集总参数电路的求解方法。

在图 1.9-1(a) 所示的均匀传输线中, 其微分段 $\mathrm{d} x$ 的等效电路如图 1.9-1 (b) 所示。由 KCL 和 KVL 并稍加 推导, 可以得到均匀传输线方程

$$
\left\{\begin{array}{l}
-\frac{\partial u}{\partial x}=R_{0} i+L_{0} \frac{\partial i}{\partial t} \\
-\frac{\partial i}{\partial x}=G_{0} u+C_{0} \frac{\partial u}{\partial t}
\end{array}\right.
$$





式中各参数的意义分别为:

$R_{0}$ 一单位长度 (一去一回两条线) 导线的电阻; $L_{0}$ - 单位长度的电感;

$G_{0}$ 一一单位长度线间的漏电电导;

$C_{0}$ 一单位长度线间的电容。

对于 $R_{0}=0, G_{0}=0$ 的传输线, 称为无损耗的传输线, 又称无损线。无损耗的均匀传输线方 程为

$$
\left\{\begin{array}{l}
-\frac{\partial u}{\partial x}=L_{0} \frac{\partial i}{\partial t} \\
-\frac{\partial i}{\partial x}=C_{0} \frac{\partial u}{\partial t}
\end{array}\right.
$$

\section{2. 均匀传输线的正弦稳态解}

对于正弦稳态电路,均匀传输线方程对应的相量表达式为

$$
\left\{\begin{array}{l}
-\frac{\mathrm{d} U}{\mathrm{~d} x}=R_{0} I+j \omega L_{0} I=Z_{0} I \\
-\frac{\mathrm{d} \dot{I}}{\mathrm{~d} x}=G_{0} U+j \omega C_{0} U=Y_{0} U
\end{array}\right.
$$

式中 $Z_{0}=R_{0}+j \omega L_{0}$ 为单位长度的复阻抗, $Y_{0}=G_{0}+j \omega C_{0}$ 为单位长度的复导纳。

上面二式各对 $x$ 求二阶导数,并相互代人可得

$$
\left\{\begin{array}{l}
\frac{\mathrm{d}^{2} U}{\mathrm{~d} x^{2}}=\gamma^{2} \dot{U} \\
\frac{\mathrm{d}^{2} \dot{I}}{\mathrm{~d} x^{2}}=\gamma^{2} \dot{I}
\end{array}\right.
$$

式中 $\gamma=\sqrt{\left(R_{0}+j \omega L_{0}\right)\left(G_{0}+j \omega C_{0}\right)}$,称为传播常数。将 $\gamma$ 的实部和虚部分离可得

$$
\gamma=\alpha+\mathrm{j} \beta
$$

式中 $\alpha$ 称为衰减常数, $\beta$ 称为相位常数。

求解二阶常微分方程, 可得到通解为

$$
\left\{\begin{array}{l}
\dot{U}=A_{1} \mathrm{e}^{-\gamma x}+A_{2} \mathrm{e}^{\gamma x} \\
\dot{I}=\frac{A_{1}}{Z_{\mathrm{C}}} \mathrm{e}^{-\gamma x}-\frac{A_{2}}{Z_{\mathrm{C}}} \mathrm{e}^{\gamma x}
\end{array}\right.
$$

上式中 $A_{1}$ 和 $A_{2}$ 为依靠边界条件确定的积分常数, $Z_{\mathrm{C}}$ 称为特性阻抗或波阻抗。波阻抗

$$
Z_{\mathrm{C}}=\sqrt{\frac{R_{0}+\mathrm{j} \omega L_{0}}{G_{0}+\mathrm{j} \omega C_{0}}}=\sqrt{\frac{Z_{0}}{Y_{0}}}
$$

将边界处 ( $x=0$ 处或 $x=l$ 处) 的电压和电流代人通解中, 可确定 $A_{1}$ 和 $A_{2}$, 具体解答如下。

(1) 由始端 ( $x=0$ 处) 的电压 $U_{1}$ 和电流 $I_{1}$ 边界条件所确定的解答形式

$$
\left\{\begin{array}{l}
U=\frac{1}{2}\left(U_{1}+Z_{\mathrm{C}} \dot{I}_{1}\right) \mathrm{e}^{-\gamma x}+\frac{1}{2}\left(U-Z_{\mathrm{C}} \dot{I}_{1}\right) \mathrm{e}^{\gamma x} \\
I=\frac{1}{2}\left(\frac{U_{1}}{Z_{\mathrm{C}}}+I_{1}\right) \mathrm{e}^{-\gamma x}-\frac{1}{2}\left(\frac{U_{1}}{Z_{\mathrm{C}}}-\dot{I}_{1}\right) \mathrm{e}^{\gamma x}
\end{array}\right.
$$

或写成

$$
\begin{aligned}
& U=U^{+}+U^{-} \\
& I=I^{+}-i^{-}
\end{aligned}
$$

式中

$$
\begin{aligned}
& U^{+}=\frac{1}{2}\left(U_{1}+Z_{\mathrm{c}} \dot{I}_{1}\right) \mathrm{e}^{-\gamma x} \\
& U^{-}=\frac{1}{2}\left(U_{1}-Z_{\mathrm{c}} \dot{I}_{1}\right) \mathrm{e}^{\gamma x} \\
& \dot{I}^{+}=\frac{1}{2}\left(\frac{U_{1}}{Z_{\mathrm{c}}}+\dot{I}_{1}\right) \mathrm{e}^{-\gamma x} \\
& \dot{I}^{-}=\frac{1}{2}\left(\frac{U_{1}}{Z_{\mathrm{c}}}-\dot{I}_{1}\right) \mathrm{e}^{\gamma x}
\end{aligned}
$$

$U^{+}$和 $\dot{I}^{+}$表示人射波 (又称正向行波) 电压和电流, $U^{-}$和 $\dot{I}^{-}$表示反射波 ( 又称反向行波) 电压和电流。显然,该解答形式对于分析无反射波存在的线路十分方便。

运用双曲函数

$$
\begin{aligned}
& \sinh \gamma x=\frac{1}{2}\left(\mathrm{e}^{\gamma x}-\mathrm{e}^{-\gamma x}\right) \\
& \cosh \gamma x=\frac{1}{2}\left(\mathrm{e}^{\gamma x}+\mathrm{e}^{-\gamma x}\right)
\end{aligned}
$$

上面解答形式可改写为

$$
\left\{\begin{array}{l}
\dot{U}=\dot{U}_{1} \cosh \gamma x-\dot{I}_{1} Z_{\mathrm{c}} \sinh \gamma x \\
\dot{I}=\dot{I}_{1} \cosh \gamma x-\frac{\dot{U}_{1}}{Z_{\mathrm{c}}} \sinh \gamma x
\end{array}\right.
$$

(2) 由终端 ( $x=l$ 处) 的边界条件 $U_{2}$ 和 $\dot{I}_{2}$ 所确定的解答形式

设 $x^{\prime}=l-x$, 则可得到

$$
\left\{\begin{array}{l}
U=\frac{1}{2}\left(\dot{U}_{2}+\dot{I}_{2} Z_{\mathrm{C}}\right) \mathrm{e}^{\gamma x^{\prime}}+\frac{1}{2}\left(\dot{U}_{2}-\dot{I}_{2} Z_{\mathrm{C}}\right) \mathrm{e}^{-\gamma x^{\prime}} \\
\dot{I}=\frac{1}{2}\left(\frac{U_{2}}{Z_{\mathrm{C}}}+\dot{I}_{2} Z_{\mathrm{C}}\right) \mathrm{e}^{\gamma x^{\prime}}-\frac{1}{2}\left(\frac{U_{2}}{Z_{\mathrm{C}}}-\dot{I}_{2}\right) \mathrm{e}^{-\gamma x^{\prime}}
\end{array}\right.
$$

或写作

$$
\left\{\begin{array}{l}
U=\dot{U}_{2} \cosh \gamma x^{\prime}+\dot{I}_{2} Z_{\mathrm{c}} \sinh \gamma x^{\prime} \\
\dot{I}=\dot{I}_{2} \cosh \gamma x^{\prime}+\frac{U_{2}}{Z_{\mathrm{C}}} \sinh \gamma x^{\prime}
\end{array}\right.
$$

\section{3. 无损耗均匀传输线的正弦稳态解}

$$
\begin{aligned}
& \gamma=\mathrm{j} \omega \sqrt{L_{0} C_{0}}, \alpha=0, \beta=\omega \sqrt{L_{0} C_{0}} \\
& Z_{\mathrm{C}}=\sqrt{\frac{L_{0}}{C_{0}}}
\end{aligned}
$$

此时, 对应双曲函数解答式蜕变为三角函数式, 即

$$
\left\{\begin{array}{l}
U=\dot{U}_{1} \cos \beta x-\mathrm{j} \dot{I}_{1} Z_{\mathrm{C}} \sin \beta x \\
\dot{I}=\dot{I}_{1} \cos \beta x-\mathrm{j} \frac{\dot{U}_{1}}{Z_{\mathrm{C}}} \sin \beta x
\end{array}\right.
$$

或 

$$
\left\{\begin{array}{l}
U=U_{2} \cos \beta x^{\prime}+\mathrm{j}_{2} Z_{\mathrm{c}} \sin \beta x^{\prime} \\
I=I_{2} \cos \beta x^{\prime}+\mathrm{j} \frac{U_{2}}{Z_{\mathrm{c}}} \sin \beta x^{\prime}
\end{array}\right.
$$

上面两个表达式,依据边界条件的不同,适当选择可以简化计算过程。

在均匀传输线中, $R_{0} 、 L_{0} 、 G_{0}$ 和 $C_{0}$ 被称为均匀传输线的原参数, 而传播常数 $\gamma$ 和特性阻抗 $Z_{\mathrm{c}}$ 被称为副参数。副参数一般都是频率的函数。当传输信号的波长 $\lambda$ 为已知时,无损耗均匀 传输线的传播常数 $\gamma$ 的虚部 $\beta$ 可通过下式计算:

$$
\beta=\frac{2 \pi}{\lambda}
$$

波长 $\lambda$ 与波速 $v$ 和频率 $f$ 有关, 并且存在 $\lambda=v / f$ 。

\section{4. 均匀传输线的输入阻抗}

当均匀传输线终端接负载 $Z_{\mathrm{L}}$ 时, 如图 1.9-2 所示, 从始 湍观察的输人阻抗

$$
Z_{\text {in }}=\left.\frac{U_{1}}{I_{1}}\right|_{x=1}=\frac{U_{2} \cosh \gamma l+\dot{I}_{2} Z_{C} \sinh \gamma l}{i_{2} \cosh \gamma l+\frac{U_{2}}{Z_{\mathrm{C}}} \sinh \gamma l}
$$

由于 $U_{2} / i_{2}=Z_{\mathrm{L}}$, 上式分子分母同除以 $i_{2}$ 可以得到



$$
Z_{\text {in }}=\frac{Z_{\mathrm{L}} \cosh \gamma l+\sinh \gamma l}{\cosh \gamma l+\frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}} \sinh \gamma l}
$$

该式计算比较麻烦,但当 $Z_{\mathrm{L}}=0$ (短路状态) 或 $Z_{\mathrm{L}}=\infty$ (开路状态) 时, 上式变得简单。 $Z_{\text {in }}$ 的计算虽然麻烦, 但在复杂的传输线路中运算是不可避免的。为了简单又便于计算, 下面分析 无损耗的均匀传输线的输人阻抗, 此时

$$
Z_{\text {in }}=\frac{U_{2} \cos \beta l+\mathrm{j} I_{2} Z_{\mathrm{c}} \sin \beta l}{I_{2} \cos \beta l+\mathrm{j} \frac{U_{2}}{Z_{\mathrm{C}}} \sin \beta l}=\frac{Z_{\mathrm{L}} \cos \beta l+\mathrm{j} Z_{\mathrm{C}} \sin \beta l}{\cos \beta l+\mathrm{j} \frac{Z_{\mathrm{L}}}{Z_{\mathrm{C}}} \sin \beta l}
$$

(1) 终端开路状态 $\left(Z_{\mathrm{L}}=\infty\right)$

此时 $\dot{I}_{2}=0$, 故

$$
Z_{\text {in }}=\frac{U_{2} \cos \beta l}{\mathrm{j} \frac{U_{2}}{Z_{\mathrm{C}}} \sin \beta l}=-\mathrm{j} Z_{\mathrm{c}} \cot \beta l
$$

$Z_{\text {in }}$ 相当于一个纯电抗。当 $l<\frac{1}{4} \lambda$ 时, 相当于一个电容; 当 $\frac{1}{4} \lambda<l<\frac{1}{2} \lambda$ 时, 相当于一个电 感依次可类推。

(2) 终端短路状态 $\left(Z_{\mathrm{L}}=0\right)$

此时 $U_{2}=0$, 故

$$
Z_{\text {in }}=\frac{\mathrm{j}_{2} Z_{\mathrm{c}} \sin \beta l}{I_{2} \cos \beta l}=j Z_{\mathrm{c}} \tan \beta l
$$


一个电容。

通过上面分析不难看到, 无论是终端短路还是开路, 都不能认为是始端 $Z_{\text {in }}$ 等于零或无穷 大, 这是分布参数特点。在终端开路时, 若 $l=\frac{1}{4} \lambda$, 则 $Z_{\mathrm{in}}=0$, 反而造成始端短路; 而在终端短 路时, 若 $l=\frac{1}{4} \lambda$, 则 $Z_{\mathrm{in}}=\infty$, 反而使始端相当于开路。

【例 1.9-1】无损耗均匀传输线的长度 $l=100 \mathrm{~m}$, 特性阻抗 $Z_{\mathrm{C}}=300 \Omega$, 波长 $\lambda=1200 \mathrm{~m}$ 的正弦波电压在其终端开路时终端电压 $U_{2}=10 \mathrm{~V}$, 试求其始端电压和电流的有效值。

解: 设 $U_{2}=1010^{\circ} \mathrm{V}$, 由于终端开路, 故 $\dot{I}_{2}=0$, 考虑

代人公式

$$
\beta l=\frac{2 \pi}{\lambda} l=\frac{2 \pi}{1200} \times 100=\frac{\pi}{6}=30^{\circ}
$$

$$
\begin{aligned}
& U=\dot{U}_{2} \cos \beta x^{\prime}+\mathrm{j} \dot{I}_{2} Z_{\mathrm{c}} \sin \beta x^{\prime} \\
& \dot{I}=\dot{I}_{2} \cos \beta x^{\prime}+\mathrm{j} \frac{U_{2}}{Z_{\mathrm{C}}} \sin \beta x^{\prime}
\end{aligned}
$$

可得始端电压和电流为

$$
\begin{aligned}
& \dot{U}_{1}=10 \cos 30^{\circ}=8.66 \mathrm{~V} \\
& \dot{I}_{1}=\mathrm{j} \frac{10}{300^{\circ}} \sin 30^{\circ}=\mathrm{j} 16.7 \mathrm{~mA}
\end{aligned}
$$

始端电压 $U_{1}=8.66 \mathrm{~V}$, 电流 $I_{1}=16.7 \mathrm{~mA}^{\circ}$

【例 1.9-2】长度为传输信号波长 $\frac{1}{6}$ 的一段均匀传输线, 波阻抗为 $400 \Omega$, 已知终端短路 时的始端电压 $U_{1}=5 \mathrm{~V}$, 试求传输线的始端电流和终端电流的有效值。

解: 由已知始端边界电压的表达式

$$
U=U_{1} \cos \beta x-\mathrm{j} I_{1} Z_{C} \sin \beta x
$$

在终端处, 由于 $U_{2}=0$, 故

$$
i_{1}=\frac{U_{1} \cos \beta x}{\mathrm{j} Z_{\mathrm{c}} \sin \beta x}
$$

代人 $\beta x=\frac{2 \pi}{\lambda} \cdot \frac{\lambda}{6}=\frac{\pi}{3}$, 并设 $U_{1}=5 \not 0^{\circ} \mathrm{V}$, 则

$$
\begin{aligned}
& i_{1}=\frac{5 \cos 60^{\circ}}{\mathrm{j} 400 \sin 60^{\circ}}=-\mathrm{j} 7.22 \mathrm{~mA} \\
& i_{2}=i_{1} \cos 60^{\circ}-\mathrm{j} \frac{5}{400} \sin 60^{\circ}=-\mathrm{j} 7.22 \times 0.5-\mathrm{j} 12.5 \times 0.866=-\mathrm{j} 14.4 \mathrm{~mA}
\end{aligned}
$$

始端和终端电流的有效值分别为: $I_{1}=7.22 \mathrm{~mA}, I_{2}=14.4 \mathrm{~mA}$ 。

【例 1.9-3】一波阻抗为 $Z_{\mathrm{c}}$ 的短路线可视为无损耗的均匀传输线, 若线路长度为传输信 号波长的 $\frac{1}{8}$, 则由始端观察该线路的等效阻抗为多大?

解: 由 $\beta l=\frac{2 \pi}{\lambda} \cdot \frac{\lambda}{8}=\frac{\pi}{4}$, 得

$$
Z_{\mathrm{e}}=\mathrm{j} Z_{\mathrm{c}} \tan \beta l=\mathrm{j} Z_{\mathrm{c}} \tan \frac{\pi}{4}=\mathrm{j} Z_{\mathrm{c}}
$$

眀等效阻抗为 $\mathrm{j} Z_{\mathrm{c}}$ 。

【例 1.9-4] 某高压输电线长 $l=200 \mathrm{~km}$, 波阻抗 $Z_{\mathrm{c}}=400 \Omega$, 线路终端电压 $U_{2}=110 \times$ $10^{3} 0^{\circ} \mathrm{V}$,终端负载 $Z_{\mathrm{L}}=22030^{\circ} \Omega$, 如图 1.9-3 所示。若该传输线可近似用无损耗线计算, 试估算其始端的电压和电流。

解: $\dot{I}_{2}=\frac{U_{2}}{Z_{\mathrm{L}}}=\frac{110 \times 10^{3} \angle 0^{\circ}}{220 \underline{30^{\circ}}}=500 \angle-30^{\circ} \mathrm{A}$

$$
\begin{aligned}
\beta l & =\frac{2 \pi}{\lambda} l=\frac{2 \pi}{6000} \times 200=\frac{\pi}{15}=12^{\circ} \\
U_{1} & =U_{2} \cos \beta l+\mathrm{j} I_{2} Z_{\mathrm{C}} \sin \beta l \\
& =110 \times 10^{3} \times \cos 12^{\circ}+\mathrm{j} 500 \angle-30^{\circ} \times 400 \sin 12^{\circ} \\
& =107.6 \times 10^{3}+\mathrm{j} 41.6 \times 10^{3} \angle 60^{\circ} \\
& =128.4 \times 10^{3}+\mathrm{j} 36.0 \times 10^{3}=133 \times 10^{3} \not 15.7^{\circ} \mathrm{V}
\end{aligned}
$$



$$
\begin{aligned}
\dot{I}_{1} & =\dot{I}_{2} \cos \beta l+\mathrm{j} \frac{\dot{U}_{2}}{Z_{\mathrm{c}}} \sin \beta l=500 \angle-30^{\circ} \\
& =424-\mathrm{j} 246+\mathrm{j} 57.2=464 \angle-24^{\circ} \mathrm{A}
\end{aligned}
$$

【例 1.9-5】长度 $l=60 \mathrm{~m}$ 的架空线路, 工作频率为 $1 \mathrm{MHz}$, 其波阻抗 $Z_{\mathrm{c}}=150 \Omega$, 当其终 端开路时, 试求其输人端的等效阻抗 $Z_{\mathrm{e}}$ 。

解:架空线路的波速为 $3 \times 10^{8} \mathrm{~m} / \mathrm{s}$, 故波长

$$
\begin{aligned}
& \lambda=\frac{v}{f}=\frac{3 \times 10^{8}}{10^{6}}=300 \mathrm{~m} \\
& \beta l=\frac{2 \pi}{\lambda} l=\frac{2 \pi}{300} \times 60=\frac{2}{5} \pi=72^{\circ}
\end{aligned}
$$

终耑开路的等效阻抗

$$
Z_{\mathrm{e}}=-\mathrm{j} Z_{\mathrm{C}} \cot \beta l=\mathrm{j} 150 \cot 72^{\circ}=-\mathrm{j} 48.7 \Omega
$$

$Z_{\mathrm{e}}$ 的值相当于某一电容的纯容抗值。如果改变线路长度, $Z_{\mathrm{e}}$ 值将变化, 当然也可以相当 干纯电感的感抗值。

【例 1.9-6】一均匀传输线无反射波存在, 若已知该线路的传播常数 $\gamma=\alpha+\mathrm{j} \beta$, 波阻抗为 $Z_{c}$, 始端电压 $U_{1}=U_{0} / 0^{\circ} \mathrm{V}$, 试求该传输线沿线 ( $x$ 方向) 的电压和电流的瞬时值。

解:由于无反射波,故存在

$$
U=A_{1} \mathrm{e}^{-\gamma x}
$$

代人边界条件: $x=0$ 时, $U=U_{1}$, 得到

$$
U_{0}=A_{1}
$$

敬有

$$
\begin{aligned}
& U=U_{0} \mathrm{e}^{-\gamma x}=U_{0} \mathrm{e}^{-\alpha x} \mathrm{e}^{-i \beta x} \\
& \dot{I}=\frac{A_{1}}{Z_{\mathrm{c}}} \mathrm{e}^{-\gamma x}=\frac{U_{0}}{Z_{\mathrm{c}}} \mathrm{e}^{-\alpha x} \mathrm{e}^{-i \beta x}
\end{aligned}
$$

由此可对应写出电压和电流的僢时值表达式

$$
\begin{aligned}
& u(t, x)=\sqrt{2} U_{0} \mathrm{e}^{-\alpha x} \sin (\omega t-\beta x) \\
& i(t, x)=\sqrt{2} \frac{U_{0}}{Z_{\mathrm{C}}} \mathrm{e}^{-\alpha x} \sin (\omega t-\beta x)
\end{aligned}
$$

由此不难看出, 衰减常数表示电压或电流幅值的衰减, 波行进 $x=\frac{1}{\alpha} \mathrm{m}$, 其幅度衰减到 $\frac{1}{\mathrm{e}}$, 即变为原值 $36.8 \%$ 。而相位常数 $\beta$ 表示波行进单位长度正弦波电压或电流相位的改变量。 1.9 .2 均匀传输线的特性阻抗和阻抗匹配

\section{1. 均匀传输线的特性阻抗}

$$
Z_{\mathrm{c}}=\sqrt{\frac{R_{0}+\mathrm{j} \omega L_{0}}{G_{0}+\mathrm{j} \omega C_{0}}}=\sqrt{\frac{Z_{0}}{Y_{0}}}=\left|Z_{\mathrm{c}}\right| \mathrm{e}^{\mathrm{j} \theta}
$$

对于无损耗均匀传输线, 则

$$
Z_{\mathrm{c}}=\sqrt{\frac{L_{0}}{C_{0}}}
$$

在直流工作状态下, 存在

$$
Z_{\mathrm{C}}=\sqrt{\frac{R_{0}}{G_{0}}}
$$

可见, 一般情况下, $Z_{\mathrm{c}}$ 为一复数, 它表示人射波 (或反射波) 电压与电流相量之比, 其 $\theta$ 值 表示特定的参考方向下(指电流由始端流向终端的方向为入射波电流方向, 而反射波电流取 其相反的方向) 电压超前电流的相位。对于无损线或直流状态, 波阻抗为一正实数。

\section{2. 阻抗匹配}

终端接人的负载 $Z_{\mathrm{L}}$ 等于均匀传输线的特性阻抗 $Z_{\mathrm{C}}$ 时,称传输线工作在匹配状态。

工作在匹配状态下的均匀传输线, 具有以下特点。

(1)电压或电流均无反射波, 线路上电压和电流的有效值都是按指数规律从始端到终端逐 渐衰减的, 即

$$
U=U_{1} \mathrm{e}^{-\gamma x}, \dot{I}=\dot{I}_{1} \mathrm{e}^{-\gamma x}
$$

(2)在线路任一位置处电压和电流的相量比都相等,都等于线路的波阻抗, 即

$$
\frac{\vec{U}}{\dot{I}}=Z_{\mathrm{c}}
$$

(3)自然功率: 在无反射条件下, 线路能够传输到终端的功率称为自然功率。显然在匹配状 态下, 自然功率即终端功率 $P_{2}$, 即

$$
P_{2}=U_{2} I_{2} \cos \theta=\frac{U_{2}^{2}}{\left|Z_{\mathrm{C}}\right|} \cos \theta
$$

(4)传输效率: 由于匹配状态下无反射波存在, 此时传输线的传输效率比较高, 但这一值并 不一定是最大传输效率。传输线始端功率为

由传输效率

$$
P_{1}=U_{1} I_{1} \cos \theta
$$

$$
\eta=\frac{P_{2}}{P_{1}}=\frac{U_{2} I_{2} \cos \theta}{U_{1} I_{1} \cos \theta}=\frac{U_{2} I_{2}}{U_{1} I_{1}}
$$

当传输线的长度为 $l$ 时, 存在

因此

$$
\begin{aligned}
& U_{2}=U_{1} \mathrm{e}^{-\gamma l}=U_{1} \mathrm{e}^{-\alpha l} \mathrm{e}^{-i \beta l} \\
& \dot{I}_{2}=\dot{I}_{1} \mathrm{e}^{-\gamma l}=I_{1} \mathrm{e}^{-\alpha l} \mathrm{e}^{-j \beta l}
\end{aligned}
$$



$$
U_{2}=U_{1} \mathrm{e}^{-\alpha t}, I_{2}=I_{1} \mathrm{e}^{-\alpha l}
$$

数有

$$
\eta=\mathrm{e}^{-2 \alpha t}
$$

该结果显示, 匹配状态下的传输线效率只与线路的长度 $l$ 和衰减系数 $\alpha$ 相关。

如果线路是无损耗的,线路终端又接以匹配负载,此时将存在

$$
U=U_{1} \mathrm{e}^{-\mathrm{i} \beta x}, \dot{I}=\dot{I}_{1} \mathrm{e}^{-\mathrm{i} \beta x}
$$

沿线路各处的电压和电流的有效值将不再变化, 仅仅相位随 $x$ 而变化。由于特性阻抗是实数, 沿线路任一位置电压和电流都将是同相位的。此时衰减系数 $\alpha=0$, 效率 $\eta=100 \%$, 达到最大 值。

【例 1.9-7】一电缆参数为 $R_{0}=0.00184 \Omega / \mathrm{m}, L_{0}=0.07 \times 10^{-6} \mathrm{H} / \mathrm{m}, G_{0}=0.5 \times 10^{-9}$ $\mathrm{S} / \mathrm{m}, C_{0}=0.031 \times 10^{-9} \mathrm{~F} / \mathrm{m}$, 工作频率 $f=800 \mathrm{~Hz}$, 试求该线路的特性阻抗。

解: $Z_{0}=R_{0}+\mathrm{j} \omega L_{0}=0.00184+\mathrm{j} 2 \pi \times 800 \times 0.07 \times 10^{-6}$

$$
\begin{aligned}
& =0.00184+\mathrm{j} 0.000352=1.87 \times 10^{-3} 10.8^{\circ} \Omega \\
Y_{0} & =G_{0}+\mathrm{j} \omega C_{0}=0.5 \times 10^{-9}+\mathrm{j} 2 \pi \times 800 \times 0.031 \times 10^{-9} \\
& =(0.0005+\mathrm{j} 0.156) \times 10^{-6}=0.156 \times 10^{-6} \angle-89.8^{\circ} \mathrm{S}
\end{aligned}
$$

$$
Z_{\mathrm{C}}=\sqrt{\frac{Z_{0}}{Y_{0}}}=\sqrt{\frac{1.87 \times 10^{-3} / 10.8^{\circ}}{0.156 \times 10^{-6} / 89.8^{\circ}}}=109 L-39.5^{\circ} \Omega
$$

【例 1.9-8】 某电力传输线, 当终端接特性阻抗负载时, 终端电压 $U_{2}=10 \mathrm{kV}$, 传输线长度 $l=100 \mathrm{~km}$, 若已知线路的衰减系数 $\alpha=1.4 \times 10^{-6} 1 / \mathrm{m}$, 试求该传输线始端电压的有效值 $U_{10}$

解: 由

$$
U=U_{1} \mathrm{e}^{-\gamma x}
$$

可得

$$
U_{2}=U_{1} \mathrm{e}^{-\alpha l}
$$

即有

$$
U_{1}=U_{2} \mathrm{e}^{\alpha l}=10^{4} \times \mathrm{e}^{1.4 \times 10^{-6} \times 10^{5}}=11.5 \mathrm{kV}
$$

【例 1.9-9】无损耗均匀传输线的原参数为 $L_{0}=1.3 \times 10^{-3} \mathrm{H} / \mathrm{km}, C_{0}=8.6 \times 10^{-9} \mathrm{~F} / \mathrm{km}$, 攽使该线路工作在匹配状态, 则终端应接多大的负载?

解: $Z_{\mathrm{C}}=\sqrt{\frac{L_{0}}{C_{0}}}=\sqrt{\frac{1.3 \times 10^{-3}}{8.6 \times 10^{-9}}}=389 \Omega$

故终端应接负载

$$
Z_{\mathrm{L}}=389 \Omega
$$

【1.9-10】某高压输电线的波阻抗 $Z_{\mathrm{C}}=380\left\lfloor-6^{\circ} \Omega\right.$, 现测得在终端匹配的情况下始端电 压 $U_{1}=147 \mathrm{kV}$, 终端电压 $U_{2}=127 \mathrm{kV}$, 试求该传输线传输的自然功率和传输效率。

解: 自然功率

$$
P_{2}=U_{2} I_{2} \cos \theta=\frac{U_{2}^{2}}{\left|Z_{C}\right|} \cos \theta=\frac{\left(127 \times 10^{3}\right)^{2}}{380} \cos 6^{\circ}=42.2 \mathrm{MW}
$$

始端功率 

$$
P_{1}=\frac{U_{1}^{2}}{\left|Z_{\mathrm{c}}\right|} \cos \theta=\frac{\left(147 \times 10^{3}\right)^{2}}{380} \cos 6^{\circ}=56.6 \mathrm{MW}
$$

传输效率

$$
\eta=\frac{P_{2}}{P_{1}}=\frac{42.2}{56.6}=74.6 \%
$$

【例 1.9-11】图 1.9-4 所示电路中, 若 $l_{1}=\frac{1}{4} \lambda, l_{2}=\frac{1}{4} \lambda, l_{3}=\frac{1}{8} \lambda, Z_{\mathrm{Cl}}=100 \Omega, Z_{\mathrm{C} 2}=300$ $\Omega, Z_{\mathrm{c} 3}=200 \Omega, R_{1}=600 \Omega, R_{2}=300 \Omega, R_{3}=200 \Omega$, 试求 $1-1^{\prime}$ 端的输人阻抗。





解: 由于两段分传输线路终端接的负载分别等于各自的波阻抗, 因此从 $2-2^{\prime}$ 端观察它们 的输人阻抗分别等于 $R_{2}$ 和 $R_{3}$ 。在 2-2'端, 三个电阻并联如图 1. 9-5 所示, 2-2 $2^{\prime}$ 端的等效电 阻 $R_{\mathrm{e}}$ 为

$$
R_{\mathrm{e}}=\frac{1}{1 / R_{1}+1 / R_{2}+1 / R_{3}}=\frac{1}{1 / 600+1 / 300+1 / 200}=100 \Omega
$$

$R_{\mathrm{e}}$ 与 $Z_{\mathrm{C}, 1}$ 相等, 满足匹配条件, 因此 $1-1^{\prime}$ 端的输人阻抗

$$
Z_{1-1},=Z_{\mathrm{CI}}=100 \Omega
$$



\section{复习内容}

\section{1 半导体及二极管}

2.1.1 PN 结的形成及单向导电性

1. 载流子,扩散,漂移

(1) 载流子

半导体中空穴和电子两种载流子共同参与导电。

本征半导体中, 电子和空穴总是成对出现的, 电子一空穴对的数量受温度影响。空穴与电 子所带电量相同, 极性相反, 因此本征半导体整体是电中性的。

$\mathrm{P}$ 型半导体和 $\mathrm{N}$ 型半导体是两种基本的杂质半导体。

$\mathrm{P}$ 型半导体: 空穴数量远大于电子数量, 以空穴导电为主, 空穴为多数载流子, 电子为少数 载流子。

$\mathrm{N}$ 型半导体: 电子数量远大于空穴数量, 以电子导电为主, 电子为多数载流子, 空穴为少数 载流子。 (2) 载流子的扩散与漂移运动

载流子的扩散运动: 由于浓度差, 载流子从高浓度向低浓度方向产生的运动称为载流子的 拱散运动。

漂移运动: 在电场力的作用下, 载流子沿电场力方向产生的定向运动称为载流子的漂移运 敞。

\section{PN 结的形成及单向导电性}

(1) PN 结的形成

用半导体工艺将 $\mathrm{P}$ 型半导体和 $\mathrm{N}$ 型半导体结合在一起, 在其交界面处载流子由于浓度差 $\rightarrow$ 产生多子扩散 $\rightarrow$ 形成内电场 $\rightarrow$ 产生少子漂移, 当扩散运动与漂移运动达到动态平衡时, 在交 界面处形成一层只有不能移动的离子而没有载流子的区域, 称该区域为空间电荷区或耗尽层, 即PN结。PN 结又称势垒区或阻挡层。

(2) PN 结的单向导电性

在 PN 结上没有外加电压时, 通过 PN 结的扩散电流和漂移电流达到动态平衡, 通过 PN 结 的总电流为零。当有外加电压时, 平衡状态被打破。

外加正向电压 $\rightarrow$ 耗尽层变窄, 内电场减弱 $\rightarrow$ 扩散大于漂移 $\rightarrow$ 扩散电流形成的正向电流大, 受外加电压影响显著 $\rightarrow$ 正向 PN 结呈现低电阻特征。

外加反向电压 $\rightarrow$ 耗尽层变宽, 内电场增强 $\rightarrow$ 漂移大于扩散 $\rightarrow$ 漂移电流形成很小的反向电 流,且不随外加电压变化 $\rightarrow$ 反向 PN 结呈现高电阻特征。

PN 结的电路特征表现为正向电阻很小, 反向电阻很大, 这就是 PN 结的单向导电性。

\section{1 .2 二极管和稳压管特性、参数}

\section{1. 半导体二极管}

(1) 二极管的伏一安特性

二极管的伏一安特性如图 2.1-1(a) 所示, 分为三个区段: $A$ 段一一正向特性, $B$ 段一一反 向特性, $C$ 段一一向击穿特性。图 2.1-1 (b) 为理想二极管的伏一安特性, 正向压降 $U_{\mathrm{D}}=$ $0 \mathrm{~V}$,门坎电压 $U_{\mathrm{th}}=0 \mathrm{~V}$ 。






(2) 二极管的伏一安特性方程

二极管的正向特性和反向特性也可以用二极管的伏一安特性方程来描述。

$i_{0}=I_{\mathrm{S}}\left(\mathrm{e}^{u_{\mathrm{D}} / U_{\mathrm{T}}}-1\right)$, 当 $T=300 \mathrm{~K}$ 时, $U_{\mathrm{T}}=26 \mathrm{mV}_{\text {。 }}$ 正向特性: 当二极管的外加电压 $u_{\mathrm{D}}$ 为正, 且 $u_{\mathrm{D}} \gg U_{\mathrm{T}}$ 时, $i_{\mathrm{D}} \approx I_{\mathrm{S}}\left(\mathrm{e}^{u_{\mathrm{D}} / U_{\mathrm{T}}}\right)$ 。

反向特性: 当二极管的外加电压 $u_{\mathrm{D}}$ 为负, 且 $\left|u_{\mathrm{D}}\right| \gg U_{\mathrm{T}}$ 时, $i_{\mathrm{D}} \approx-I_{\mathrm{S}}$ 。

但反向击穿特性不能用伏一安特性方程来描述。

硅二极管门坎电压 $U_{\mathrm{th}} \approx 0.5 \mathrm{~V}$, 正向压降 $U_{\mathrm{D}} \approx 0.7 \mathrm{~V}$ 。

锗二极管门坎电压 $U_{\mathrm{th}} \approx 0.1 \mathrm{~V}$, 正向压降 $U_{\mathrm{D}} \approx 0.3 \mathrm{~V}$ 。

(3) 二极管的主要参数

最大整流电流 $I_{\mathrm{F}}$ : 长期运行时,允许通过的最大正向平均电流。

最大反向工作电压 $U_{\mathrm{R}}$ : 允许承受的最大反向电压, 其值约为击穿电压 $U_{\mathrm{BR}}$ 的一半。

反向电流 $I_{\mathrm{R}}$ : 外加反向电压尚未击穿时, 流过管子的电流。

最高工作频率 $f_{\mathrm{m}}$ : 主要由极间电容的大小决定。当工作频率高于此值时, 二极管的单向导 电性将变差, 甚至消失。

【例 2.1-1】 二极管电路如图 2.1-2 所示, 试问图中各二极管是导通还是截止, $U_{\mathrm{o}}$ 多少伏? 设二极管是理想的。

解: 解这种类型题, 关键是正确判断二极管是导通还是截止, 而后再计算 $U_{\mathrm{o}}$ 。判断二极管 状态的方法: 假定将二极管与电路断开, 分别计算阳极和阴极对参考点的电位 (本题参考点为 “地”), 并将二者比较。对理想二极管, 当阳极电位大于阴极电位时, 二极管正偏, 导通; 反之, 反偏,截止。










【例 2.1-2】电路如图 2.1-3 所示, 试判断图 中各二极管是导通还是截止,并计算电压 $U_{\mathrm{o}}$ 的值。 设二极管的导通压降 $U_{\mathrm{D}}=0.7 \mathrm{~V}$ 。

解: 本题电路中有两个二极管。若两个二极 管均为正偏, 则正向电压较大者优先导通, 以此再 判断另一个二极管的状态。

将 $\mathrm{D}_{1}$ 和 $\mathrm{D}_{2}$ 从“ “ $x$ ”处断开, 得: 图 (a) 中 $\mathrm{D}_{1}$ 的 $U_{\text {ak1 } 1}=12 \mathrm{~V}, \mathrm{D}_{2}$ 的 $U_{\mathrm{ak} 2}=6 \mathrm{~V}, U_{\mathrm{ak1}}>U_{\mathrm{ak2}}, \mathrm{D}_{1}$ 优先导 通。

在 $\mathrm{D}_{1}$ 导通后, $U_{\mathrm{o}}=-0.7 \mathrm{~V}$ 。在此状态下, 再判断 $\mathrm{D}_{2}$ 是导通还是截止。于是, $\mathrm{D}_{2}$ 的 $U_{\mathrm{ak2}}=$ $-6-(-0.7)=-5.3 \mathrm{~V}$, 故 $\mathrm{D}_{2}$ 反偏而截止。所以 $U_{\mathrm{o}}=-0.7 \mathrm{~V}$ 。

由图(b)用同样的方法, 可得: $\mathrm{D}_{1}$ 的 $U_{\mathrm{ak} 1}=12 \mathrm{~V}, \mathrm{D}_{2}$ 的 $U_{\mathrm{ak} 2}=18 \mathrm{~V}, U_{\mathrm{ak} 2}>U_{\mathrm{ak} 1}, \mathrm{D}_{2}$ 优先导通, $U_{0}=-5.3 \mathrm{~V}$, 此时 $\mathrm{D}_{1}$ 的 $U_{\mathrm{ak} 1}=-5.3 \mathrm{~V}$, 反偏而截止。所以 $U_{\mathrm{o}}=-5.3 \mathrm{~V}$ 。

【例2.1-3】限幅电路如图 2.1-4 所示, D 的导通压降 $U_{\mathrm{D}}=0.7 \mathrm{~V}, U_{\mathrm{REF}}=4 \mathrm{~V}$, 当输人电压 $u_{i}=10 \sin \omega t \mathrm{~V}$ 时,对应画出 $u_{\mathrm{o}}$ 的波形。

解: 在 $u_{\mathrm{i}}$ 的正半周, 当 $u_{\mathrm{i}}<U_{\mathrm{REF}}+U_{\mathrm{D}}=4.7 \mathrm{~V}$ 时, $\mathrm{D}$ 反偏, 截止, $U_{\mathrm{o}}=u_{\mathrm{i}}$ 。当 $u_{\mathrm{i}} \geqslant U_{\mathrm{REF}}+U_{\mathrm{D}}$ $=4.7 \mathrm{~V}$ 时, D 正偏, 导通, $U_{0}=4.7 \mathrm{~V}$ 。

在 $u_{\mathrm{i}}$ 的负半周, D 反偏,截止, $U_{\mathrm{o}}=u_{\mathrm{i}}$ 。输出波形如图 (b) 中的“粗线”所示。







\section{2. 稳压管}

（1）稳压管的伏一安特性

稳压管的伏一安特性曲线也分为正向特性、反向特性和反向击穿特性三个区域, 见图 2.1.5。

稳压管工作在反向击穿状态, 动态电阻 $r_{\mathrm{z}}=\Delta u_{\mathrm{z}} / \Delta i_{\mathrm{z}}$ 越小, 稳压性能越好。

(2) 稳压管的参数

稳定电压 $U_{z}$ : 即稳压管的击穿电压。

稳定电流 $I_{z}$ :工作电压等于稳定电压时的工作电流。工作电流低于该值时, 稳压效果不 好。

耗散功率 $P_{\mathrm{M}}$ : 允许的最大功率损耗 $P_{\mathrm{M}}=U_{\mathrm{Z}} I_{\mathrm{ZM}}$, 其中 $I_{\mathrm{ZM}}$ 为最大稳定电流。

稳定电压的温度系数: 管子的工作电流等于稳定电流 $I_{\mathrm{Z}}$ 时, 环境温度改变 $1^{\circ} \mathrm{C}$ 时, 稳定电 压变化量称为温度系数。

动态电阻 $r_{\mathrm{Z}}$ : 在稳压范围内, 稳压管两端电压变化量与工作电流变化量的比值。

【例 2.1-4】电路如图 2.1-6 所示, 设稳压管 $\mathrm{D}_{\mathrm{z} 1}$ 和 $\mathrm{D}_{\mathrm{Z} 2}$ 的稳定电压分别为 $6 \mathrm{~V}$ 和 $8 \mathrm{~V}$, 求 图中各电路的输出电压 $U_{\text {。。 }}$ 。知稳压管的正向压降为 $0.7 \mathrm{~V}$ 。

解:图(a) $U_{0}=14 \mathrm{~V}$; 图(b) $U_{0}=1.4 \mathrm{~V}$; 图(c) $U_{0}=6 \mathrm{~V}$; 图(d) $U_{0}=0.7 \mathrm{~V}$ 。









\section{2 放大电路基础}

\subsection{1 基本放大电路}

半导体三极管简称晶体管或三极管。因多子和少子都参与导电, 又称双极结型晶体管 (BJT)。三极管的主要特点是具有电流放大作用, 是构成放大电路的核心器件。

\section{1. 放大电路的组成原则}

(1) 具有放大功能

(1)三极管工作在放大状态, 即电源极性设置须使发射结正向偏置、集电结反向偏置; (2) 被 放大的信号能输人,放大后的信号能取出。

(2) 不失真

设置合适的工作点。

\section{2. 三种基本放大电路}

基本放大电路有三种基本接法或组态, 它们是共射极放大电路、共集电极放大电路和共基 极放大电路, 分别如图 2.2-1(a)、(b),(c) 所示。








\section{3. 放大电路的两种工作状态}

\section{(1) 静态}

当输人交流信号 $u_{\mathrm{i}}=0$ 时, 放大电路的工作状态称为直流工作状态, 简称静态。电路中的 电压、电流均为不变的直流量。

\section{(2) 动态}

当输人交流信号 $u_{\mathrm{i}} \neq 0$ 时, 电路处于放大状态, 简称动态。电路中的电压、电流均随 $u_{\mathrm{i}}$ 的 变化而变化。

\section{4. 直流通路和交流通路}

(1) 直流通路的画法

将电路中的电容开路, 所得电路为直流通路, 用于静态分析。

(2) 交流通路的画法

将电路中的电容和电源短路, 所得电路为交流通路, 用于动态分析。

【例 2.2-1】电路如图 2.2-2 所示, 试判断各电路是否具有放大作用。

解: 图(d) 具有放大功能。











置。图(c) 中交流输人信号被电容 $C_{2}$ 短路, 加不到发射结。图 (b) 中电源 $U_{\mathrm{cc}}$ 的极性错误, 不 能保证发射结正向偏置,集电结反向偏置。

\section{5. 静态工作点 $Q$ 及其稳定问题}

(1) 静态工作点 $Q$

放大电路处于静态时, 三极管极间电压 $U_{\mathrm{CE}} 、 U_{\mathrm{BE}}$ 和电流 $I_{\mathrm{C}} 、 I_{\mathrm{B}}$ 的数值称为静态工作点。 $U_{\mathrm{BE}}$ 对于硅管为 $0.7 \mathrm{~V}$, 锗管为 $0.3 \mathrm{~V}$, 作为已知值。

(2) $Q$ 点的稳定问题

影响静态工作点稳定的主要因素是温度, 温度上升使 $\beta \uparrow 、 I_{\mathrm{CBO}} \uparrow 、 U_{\mathrm{BE}} \downarrow$, 其结果是使 $I_{\mathrm{C}} \uparrow$; 温度下降, 使 $I_{\mathrm{C}} \downarrow$ 。严重时可能导致 $Q$ 点进人三极管的饱和区或截止区。

(3) 能稳定 $Q$ 点的电路——射极偏置电路








\section{2 .2 放大电路的基本分析方法}

基本分析方法有近似估算法、图解法和微变等效电路法。

\section{1. 近似估算法}

用于近似计算静态工作点 $Q$ 。估算静态工作点应使用直流通路。

(1) 固定偏置电路

求解思路: $I_{\mathrm{B} Q} \rightarrow I_{\mathrm{C} Q} \rightarrow U_{\mathrm{CE} Q}$ 。


$$
I_{\mathrm{B} Q}=\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}}, I_{\mathrm{C} Q}=\beta I_{\mathrm{B} Q}, U_{\mathrm{CE} Q}=U_{\mathrm{cC}}-I_{\mathrm{C} Q} R_{\mathrm{c}}
$$

(2) 射极偏置电路

求解思路: $U_{\mathrm{B}} \rightarrow U_{\mathrm{E}} \rightarrow I_{\mathrm{EQ} Q} \rightarrow U_{\mathrm{CE} Q}$ 。

射极偏置电路 (图 2.2-3) 的直流通路如图 2.2-5 所示。

$$
\begin{aligned}
& U_{\mathrm{B}} \approx \frac{R_{\mathrm{b} 2}}{R_{\mathrm{b} 1}+R_{\mathrm{b} 2}} U_{\mathrm{CC}}, I_{\mathrm{C} Q} \approx I_{\mathrm{E} Q}=\frac{U_{\mathrm{B}}-U_{\mathrm{BE}}}{R_{\mathrm{e}}} \\
& U_{\mathrm{CE} Q} \approx U_{\mathrm{CC}}-I_{\mathrm{CQ}}\left(R_{\mathrm{c}}+R_{\mathrm{e}}\right), I_{\mathrm{B} Q}=\frac{I_{\mathrm{C} Q}}{\beta}
\end{aligned}
$$

【例 2. 2-2】近似计算图 2.2-6(a) 所示放大电路的静态工作点 $Q$ 。 解: 图 2.2-6(b) 为放大电路的直流通路。从图可知基极电流

$$
\begin{aligned}
I_{\mathrm{B} Q} & =\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}+(1+\beta)\left(R_{\mathrm{e} 1}+R_{\mathrm{e} 2}\right)}=\frac{12-0.7}{250+51 \times 0.5}=41 \mu \mathrm{A} \\
I_{\mathrm{CQ}} & =\beta I_{\mathrm{B} Q}=50 \times 41 \times 10^{-6} \approx 2.1 \mathrm{~mA} \\
U_{\mathrm{CEQ}} & =U_{\mathrm{CC}}-\left[I_{\mathrm{CQ}} R_{\mathrm{c}}+I_{\mathrm{E} Q}\left(R_{\mathrm{e} 1}+R_{\mathrm{e} 2}\right)\right] \approx U_{\mathrm{CC}}-I_{\mathrm{CQ}}\left(R_{\mathrm{c}}+R_{\mathrm{el}}+R_{\mathrm{e} 2}\right) \\
& =12-2.1 \times(3+0.5)=4.65 \mathrm{~V}
\end{aligned}
$$

静态工作点为: $I_{\mathrm{B} Q}=41 \mu \mathrm{A}, I_{\mathrm{C} Q}=2.1 \mathrm{~mA}, U_{\mathrm{CE} Q}=4.65 \mathrm{~V}$ 。






【例 2. 2-3】图 2. $2-3$ 中, $U_{\mathrm{cC}}=12 \mathrm{~V}, R_{\mathrm{b} 1}=15 \mathrm{k} \Omega, R_{\mathrm{b} 2}=5 \mathrm{k} \Omega, R_{\mathrm{c}}=5 \mathrm{k} \Omega, R_{\mathrm{e}}=2.3 \mathrm{k} \Omega$; 三 极管的 $U_{\mathrm{BE}}=0.7, \beta=50$ 。试确定静态工作点 $Q$ 。

解: $U_{\mathrm{B}} \approx \frac{R_{\mathrm{b} 2}}{R_{\mathrm{b} 1}+R_{\mathrm{b} 2}}-U_{\mathrm{cC}}=\frac{5}{5+15} \times 12=3 \mathrm{~V}, U_{\mathrm{E}}=U_{\mathrm{B}}-U_{\mathrm{BE}}=3-0.7=2.3 \mathrm{~V}$

$$
\begin{aligned}
& I_{\mathrm{E} Q}=\frac{U_{\mathrm{E}}}{R_{\mathrm{c}}}=\frac{2.3}{2.3}=1 \mathrm{~mA}, I_{\mathrm{B} Q}=\frac{I_{\mathrm{E} Q}}{1+\beta}=\frac{1}{51} \approx 19.6 \mu \mathrm{A} \\
& I_{\mathrm{C} Q}=\beta I_{\mathrm{B} Q}=0.98 \mathrm{~mA} \\
& U_{\mathrm{CE} Q} \approx U_{\mathrm{CC}}-I_{\mathrm{C} Q}\left(R_{\mathrm{c}}+R_{\mathrm{e}}\right)=4.85 \mathrm{~V}
\end{aligned}
$$

静态工作点为 $I_{\mathrm{B} Q}=19.6 \mu \mathrm{A}, I_{\mathrm{C} Q} \approx I_{\mathrm{E} Q}=1 \mathrm{~mA}, U_{\mathrm{CE} Q}=4.85 \mathrm{~V}$ 。

\section{2. 图解法}

主要用于确定合适的静态工作点和求出最大不失真输出电压峰值。 (1) 直流负载线

(1) 直流负载线的画法。画直流负载线要用直流通路, 图 2.2-7(a) 是典型固定偏置放大电 路,其直流通路如图 2.2-7(c) 所示。依图可得直流负载线方程









$$
u_{\mathrm{ce}}=U_{\mathrm{CC}}-i_{\mathrm{c}} R_{\mathrm{c}}
$$

令 $i_{\mathrm{c}}=0$, 则 $u_{\mathrm{ce}}=U_{\mathrm{CC}}=12 \mathrm{~V}$, 得横轴上一点 $M_{\mathrm{o}}$ 令 $u_{\mathrm{ce}}=0$, 则 $i_{\mathrm{c}}=U_{\mathrm{CC}} / R_{\mathrm{c}}=12 / 3=4 \mathrm{~mA}$, 得纵 朝上一点 $N$ 。在三极管的输出特性曲线 (图 2.2-7(b)) 上画出 $M 、 N$ 点连线, 直线 $M N$ 即为直 流负载线, 其斜率为 $-1 / R_{\mathrm{o}}$ 。

(2) 确定 $Q$ 点。

$$
I_{\mathrm{B} Q}=\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}}=\frac{12-0.7}{380} \approx 30 \mu \mathrm{A}
$$

$I_{\mathrm{BQ}}=30 \mu \mathrm{A}$ 的输出特性曲线与直流负载线的交点, 为静态工作点 $Q$ 。从 $Q$ 点得

$$
I_{\mathrm{CQ}}=1.5 \mathrm{~mA}, U_{\mathrm{CEQ}}=7.5 \mathrm{~V}
$$

(2) 交流负载线

(1) 交流负载线的画法。交流负载线用于动态分析, 画交流负载线依据放大电路的交流通 路, 如图 2.2-7(d) 所示。交流负载电阻 $R_{\mathrm{L}}^{\prime}=R_{\mathrm{c}} / / R_{\mathrm{L} .}$ 。通过 $Q$ 点, 画斜率为 $-1 / R_{\mathrm{L}}^{\prime}$ 的直线, 就 是交流负载线,如图 2.2-7(b) $A B$ 直线所示。或者用 $U_{\mathrm{CEQ}}+I_{\mathrm{C} Q} R_{\mathrm{L}}^{\prime}$ 得交流负载线在横轴上一 点,用该点通过 $Q$ 点做直线即为交流负载线(见图 2.2-8)。


从图 2.2-8 可知: 最大不截止失真输出电压幅度为 $I_{\mathrm{C} Q} R_{\mathrm{L}}^{\prime}$, 最大不饱和失真输出电压幅度 为 $U_{\mathrm{CE} Q}-U_{\mathrm{CES}}$ 。

最大不失真输出电压峰值为

$$
U_{\mathrm{om}}=\min \left[U_{\mathrm{CEQ}}-U_{\mathrm{CES}}, I_{\mathrm{CQ}} R_{\mathrm{L}}^{\prime}\right]
$$

要得到最大的 $U_{\mathrm{om}}$ 应把 $Q$ 点选在交流负载线的中点, 即满足 $U_{\mathrm{CE} Q}-U_{\mathrm{CES}}=I_{\mathrm{C} Q} R_{\mathrm{L}}^{\prime}$ 。

【例 2.2-4】电路图及其直流负载线和交流负载线分别如图 2. 2-9(a) 和 (b) 所示, 设 $U_{\mathrm{BE}}$ $=0 \mathrm{~V}$ 。试求:

(1) $U_{\mathrm{CC}} 、 I_{\mathrm{B} Q} 、 I_{\mathrm{C} Q} 、 U_{\mathrm{CE} Q}$ 的值;

(2) 电阻 $R_{\mathrm{b}} 、 R_{\mathrm{c}} 、 R_{\mathrm{L}}$ 的值;

(3) 最大不失真输出电压的峰值;

(4) 当 $u_{i}$ 的幅度足够大时,将首先产生何种失真? 如何消除?






解: (1) $U_{\mathrm{CC}}=12 \mathrm{~V}, I_{\mathrm{BQ}}=30 \mu \mathrm{A}, I_{\mathrm{CQ}}=1.8 \mathrm{~mA}, U_{\mathrm{CEQ}}=7.1 \mathrm{~V}$

(2) $R_{\mathrm{b}}=\left(U_{\mathrm{CC}}-U_{\mathrm{BE}}\right) / I_{\mathrm{BQ}}=12 / 30=400 \mathrm{k} \Omega$

$R_{\mathrm{c}}=\left(U_{\mathrm{CC}}-U_{\mathrm{CE} Q}\right) / I_{\mathrm{CQ}}=(12-7.1) / 1.8 \approx 2.7 \mathrm{k} \Omega$

$R_{\mathrm{L}}^{\prime}=(10-7.1) / I_{\mathrm{CQ}}=2.9 / 1.8 \approx 1.61 \mathrm{k} \Omega$

$R_{\mathrm{L}}=\left(R_{\mathrm{c}} R_{\mathrm{L}}^{\prime}\right) /\left(R_{\mathrm{c}}-R_{\mathrm{L}}^{\prime}\right)=(2.7 \times 1.61) /(2.7-1.61) \approx 4.0 \mathrm{k} \Omega$, 取 $R_{\mathrm{L}}=3.9 \mathrm{k} \Omega$

(3) 最大不失真输出电压峰值

$$
U_{\text {om }}=I_{\mathrm{CQ}} R_{\mathrm{L}}^{\prime}=10-7.1=2.9 \mathrm{~V}
$$

(4) 首先出现截止失真, 减少 $R_{\mathrm{b}}$ 可消除失真。

(3) 静态工作点与波形失真

以 NPN 管组成的基本放大电路为例:

(1) $Q$ 点太高一产生饱和失真, 如图 2.2-10 (a) 所示。 $Q$ 点太高, 当输人信号足够大时, 在正半周,三极管进人饱和区, $u_{\mathrm{ce}}$ 的负半周被削平。

(2) $Q$ 点太低一一产生截止失真, 如图 2.2-10 (b) 所示。 $Q$ 点太低, 当输人信号足够大时, 在负半周,三极管进人截止区, $u_{\mathrm{ce}}$ 的正半周被削平。

若是 PNP 管, 则正好相反: 图 2.2-10(a) 是截止失真; 图 2.2-10(b) 是饱和失真。

【例 2. 2-5】图 2.2-1(a) 所示放大电路, 其输人、输出波形示于图 2.2-11, 为使输出波形 





为正弦波,试问应使
(A) $R_{\mathrm{c}} \uparrow$
(B) $R_{\mathrm{b}} \uparrow$
(C) $C_{\mathrm{b} 1} \uparrow$
(D) $R_{\mathrm{b}} \downarrow$

解: 输出波形是饱和失真, 所以应选 $(\mathrm{B})$ 。

\section{3. 微变等效电路分析法}

(1) 简化的 $H$ 参数微变等效电路

在工作点附近的微小范围内, 将三极管的非线 性做局部线性化, 从而可用一个线性电路来代替非 线性的三极管, 图 2. 2-12 所示。

受控源 $\beta i_{\mathrm{b}}$ 反映了三极管的电流控制作用, 其 方向与 $i_{\mathrm{b}}$ 相关联。按图中规定的电压和电流方向,


(2) 确定 $r_{\text {be }}$

$$
r_{\mathrm{be}}=R_{\mathrm{bb}^{\prime}}+(1+\beta) \frac{U_{\mathrm{T}}(\mathrm{mV})}{I_{\mathrm{E}}(\mathrm{mA})} \approx 200 \Omega+(1+\beta) \frac{26(\mathrm{mV})}{I_{\mathrm{E}}(\mathrm{mA})}
$$

$R_{\mathrm{b} \mathrm{b}^{\prime}}$ 在 $50 \sim 300 \Omega$ 之间，一般取 $200 \Omega$ 。

微变等效电路只能用于交流分析, 不能用来求静态工作点 $Q$ 。但参数必须在工作点上求 得, 式中的 $I_{\mathrm{E}}$ 即为工作点值 $I_{\mathrm{E} Q} \circ \beta$ 值实测得到, 在试题中给出。

(3) 放大电路微变等效电路的画法

(1) 用 $H$ 参数等效电路代替放大电路中的三极管。

(2) 凡恒定的电压源都视为短路; 凡电容都视为短路。

(3) 其他元件都按原位置画。

(4) 电压和电流用相量表示。

\section{4. 用 $H$ 参数等效电路分析基本放大电路}

(1) 共射极基本放大电路

(1) 画等效电路。如图 2.2-13 (b) 所示。

(2) 电压放大倍数

$$
A_{u}=\frac{U_{\mathrm{o}}}{\dot{U}_{\mathrm{i}}}=-\frac{\beta \dot{I}_{\mathrm{b}} R_{\mathrm{L}}^{\prime}}{\dot{I}_{\mathrm{b}} r_{\mathrm{be}}}=-\frac{\beta R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}}
$$

负号表示 $U_{\mathrm{o}}$ 与 $U_{\mathrm{i}}$ 相位相反。

(3) 输人电阻 $R_{\mathrm{i}}$ 。在输人端将信号源 $U_{\mathrm{s}}$ 及其电阻 $R_{\mathrm{s}}$ 拿掉, 外加一个测试电压 $U_{\mathrm{T}}$; 输出端的 






$R_{\mathrm{L}}$ 仍然保留, 就得到求输入电阻 $R_{\mathrm{i}}$ 的等效电路图 2.2-14。从图得

$$
R_{\mathrm{i}}=\frac{\dot{U}_{\mathrm{T}}}{\dot{I}_{\mathrm{T}}}=R_{\mathrm{b}} / / r_{\mathrm{be}}
$$





(4) 输出电阻 $R_{\mathrm{o}}$ 。在输人端将信号源 $U_{\mathrm{s}}$ 短路, 但保留其电阻 $R_{\mathrm{s}}$; 输出端把 $R_{\mathrm{L}}$ 拿掉, 外加一 个测试电压 $U_{\mathrm{T}}$, 就得到求输出电阻 $R_{\mathrm{o}}$ 的等效电路图 2.2-15。因为 $U_{\mathrm{s}}=0 \Rightarrow i_{\mathrm{b}}=0 \Rightarrow \beta I_{\mathrm{b}}=0$, 所 以 $R_{\mathrm{o}}=\frac{\dot{U}_{\mathrm{T}}}{\dot{I}_{\mathrm{T}}}=R_{\mathrm{c}}$ 。

(5) 源电压放大倍数

$$
A_{u s}=\frac{\dot{U}_{\mathrm{o}}}{\dot{U}_{\mathrm{s}}}=\frac{\dot{U}_{\mathrm{o}}}{\dot{U}_{\mathrm{i}}} \times \frac{\dot{U}_{\mathrm{i}}}{U_{\mathrm{s}}}=A_{u} \times \frac{R_{\mathrm{i}}}{R_{\mathrm{s}}+R_{\mathrm{i}}}
$$

【例 2.2-6】电路如图 2.2-16(a) 所示, 设 $C_{\mathrm{b} 1} 、 C_{\mathrm{b} 2} 、 C_{\mathrm{b} 3}$ 对交流可视为短路。要求:










（1）画出直流通路,写出 $I_{\mathrm{CQ}}$ 和 $U_{\mathrm{CE} Q}$ 的表达式; (2) 画出交流通路及简化的 $H$ 参数微变等效电路;

(3) 写出 $A_{u}=U_{\mathrm{o}} / \dot{U}_{\mathrm{i}}, R_{\mathrm{i}}$ 和 $R_{\mathrm{o}}$ 的表达式。

解: (1) 直流通路如图 2.2-16(b) 所示。

$$
I_{\mathrm{B} Q}=\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}}, I_{\mathrm{C} Q}=\beta I_{\mathrm{B} Q}, U_{\mathrm{CE} Q}=U_{\mathrm{CC}}-I_{\mathrm{C} Q}\left(R_{\mathrm{c} 1}+R_{\mathrm{c} 2}\right)
$$

(2) 交流通路及简化的 $H$ 参数微变等效电路如图 2.2-16 (c)、(d) 所示。

(3) $A_{u}=-\frac{\beta R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}}, R_{\mathrm{L}}^{\prime}=R_{\mathrm{cl}} / / R_{\mathrm{L}}, R_{\mathrm{i}}=R_{\mathrm{b}} / / r_{\mathrm{be}}, R_{\mathrm{o}}=R_{\mathrm{cl} 1}$ 。

(2) 共集电极放大电路一一射极输出器、射极跟随器

(1) 求 $Q$ 点。根据直流通路图 2.2-17(b), 可以得到

$$
U_{\mathrm{CC}}=I_{\mathrm{B} Q} R_{\mathrm{b}}+U_{\mathrm{BE}}+I_{\mathrm{E} Q} R_{\mathrm{e}}, I_{\mathrm{B} Q}=\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}+(1+\beta)^{\bullet} R_{\mathrm{e}}}, I_{\mathrm{C} Q}=\beta I_{\mathrm{B} Q}, U_{\mathrm{CE} Q} \approx U_{\mathrm{CC}}-I_{\mathrm{C} Q} R_{\mathrm{e}}
$$

(2) 电压放大倍数

$$
A_{u}=\frac{U_{\mathrm{o}}}{U_{\mathrm{i}}}=\frac{(1+\beta) R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}+(1+\beta) R_{\mathrm{L}}^{\prime}} \approx \frac{B R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}+\beta R_{\mathrm{L}}^{\prime}} \approx 1 \text { (因为一般 } r_{\mathrm{be}} \ll \beta R_{\mathrm{L}}^{\prime} \text { ) }
$$

式中 $R_{\mathrm{L}}^{\prime}=R_{\mathrm{e}} / / R_{\mathrm{L} \text { 。 }}$

由于 $\dot{U}_{\mathrm{o}}$ 与 $U_{\mathrm{i}}$ 相位相同, 又 $A_{u} \approx 1$, 所以又称射极跟随器。

(3) 输人电阻 $R_{\mathrm{i}}$ 。因

$$
\begin{aligned}
& R_{\mathrm{i}}^{\prime}=\frac{U_{\mathrm{i}}}{\dot{I}_{\mathrm{b}}}=\frac{r_{\mathrm{be}} \dot{\mathrm{b}}_{\mathrm{b}}+(1+\beta) \dot{I}_{\mathrm{b}} R_{\mathrm{L}}^{\prime}}{\dot{I}_{\mathrm{b}}}=r_{\mathrm{be}}+(1+\beta) R_{\mathrm{L}}^{\prime} \\
& R_{\mathrm{i}}=R_{\mathrm{b}} / / R_{\mathrm{i}}^{\prime}=R_{\mathrm{b}} / /\left[r_{\mathrm{be}}+(1+\beta) R_{\mathrm{L}}^{\prime}\right]
\end{aligned}
$$

(4) 输出电阻

$$
R_{\mathrm{o}}=R_{\mathrm{e}} / / \frac{R_{\mathrm{s}}^{\prime}+r_{\mathrm{be}}}{1+\beta} \approx \frac{R_{\mathrm{s}}^{\prime}+r_{\mathrm{be}}}{1+\beta}, R_{\mathrm{s}}^{\prime}=R_{\mathrm{s}} / / R_{\mathrm{b}}
$$

【例 2.2-7】图 2.2-17(a) 所示, 已知 $U_{\mathrm{CC}}=12 \mathrm{~V}, R_{\mathrm{b}}=470 \mathrm{k} \Omega, R_{\mathrm{e}}=R_{\mathrm{L}}=5 \mathrm{k} \Omega, R_{\mathrm{s}}=100$ $n$, 晶体管的 $\beta=100, U_{\mathrm{BE}}=0.7 \mathrm{~V}$ 。求: (1) 电压放大倍数 $A_{u}$; (2) 输人电阻 $R_{\mathrm{i}}$; (3) 输出电阻










解: 首先求出 $r_{\mathrm{be}}$ 。 

$$
\begin{aligned}
& I_{\mathrm{B} Q}=\frac{U_{\mathrm{CC}}-U_{\mathrm{BE}}}{R_{\mathrm{b}}+(1+\beta) R_{\mathrm{e}}}=\frac{12-0.7}{470+101 \times 5} \approx 11.64 \mu \mathrm{A} \\
& I_{\mathrm{CQ}}=\beta I_{\mathrm{BQ}}=100 \times 11.6=1.16 \mathrm{~mA} \\
& r_{\mathrm{be}}=200(1+\beta) \frac{26}{I_{\mathrm{E}}} \approx 200+101 \times \frac{26}{1.16}=2.46 \mathrm{k} \Omega
\end{aligned}
$$

(1) 电压放大倍数 $A_{u}$ : 画输出 $H$ 参数微变等效电路, 如图 2.2-17(c) 所示。

$$
A_{u}=\frac{U_{\mathrm{o}}}{U_{\mathrm{i}}}=\frac{(\beta+1) R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}+(1+\beta) R_{\mathrm{L}}^{\prime}}=\frac{101 \times(5 / / 5)}{2.46+101 \times(5 / / 5)}=\frac{252.5}{255} \approx 0.99
$$

(2) 输人电阻 $R_{\mathrm{i}}$ 。

$$
\begin{aligned}
& R_{e}^{\prime}=R_{e} / / R_{\mathrm{L}}=5 / / 5=2.5 \mathrm{k} \Omega \\
& R_{\mathrm{i}}=R_{\mathrm{b}} / /\left[r_{\mathrm{be}}+(1+\beta) R_{c}^{\prime}\right]=470 / /(2.46+101 \times 2.5)=470 / / 255 \approx 165 \mathrm{k} \Omega
\end{aligned}
$$

(3) 求 $R_{\mathrm{o}}$ 的等效电路如图 2.2-17(d) 所示。有

$$
R_{\mathrm{o}} \approx \frac{R_{\mathrm{s}} / / R_{\mathrm{b}}+r_{\mathrm{be}}}{1+\beta} \approx \frac{R_{\mathrm{s}}+r_{\mathrm{be}}}{1+\beta}=\frac{0.1+2.46}{101} \approx 25 \Omega
$$

（3）共基极基本放大电路









(1) 求 $Q$ 点, 与射极偏置电路相同。

(2) 电压放大倍数

$U_{\mathrm{o}}$ 与 $\dot{U}_{\mathrm{i}}$ 相位相同。

$$
A_{u}=\frac{\dot{U}_{\mathrm{o}}}{\dot{U}_{\mathrm{i}}}=\frac{-\dot{I}_{\mathrm{c}} R_{\mathrm{L}}^{\prime}}{-\dot{I}_{\mathrm{b}} r_{\mathrm{be}}}=\frac{\beta R_{\mathrm{L}}^{\prime}}{r_{\mathrm{be}}}, R_{\mathrm{L}}^{\prime}=R_{\mathrm{c}} / / R_{\mathrm{L}}
$$

(3) 输人电阻 $R_{\mathrm{i}}$ 。由

$$
\begin{aligned}
& r_{\mathrm{eb}}=\frac{U_{\mathrm{i}}}{-\dot{I}_{\mathrm{e}}}=\frac{-\dot{I}_{\mathrm{b}} r_{\mathrm{be}}}{-(1+\beta) \dot{I}_{\mathrm{b}}}=\frac{r_{\mathrm{be}}}{1+\beta} \\
& R_{\mathrm{i}}=R_{\mathrm{e}} / / r_{\mathrm{eb}} \approx r_{\mathrm{eb}}=\frac{r_{\mathrm{be}}}{1+\beta}
\end{aligned}
$$

(4). 输出电阻 $R_{\text {o }}$

$$
R_{\mathrm{o}}=r_{\mathrm{cb}} / / R_{\mathrm{c}} \approx R_{\mathrm{c}}
$$

\section{5. 三种基本放大电路的特点}

在三种基本放大电路中, 以共射极电路和共集电极电路为重点。 (1) 共射极电路

(1) 输出信号与输入信号相位相反;

(2) 电压、电流、功率放大倍数都较大, 输人电阻和输出电阻适中;

(3) 主要用于多级放大器的中间级。

(2) 共集电极电路一一射极输出器、射极跟随器

(1) 输出信号与输人信号相位相同;

(2) 电压放大倍数接近于 1 , 而小于 1 ;

(3) 输人电阻高, 输出电阻低, 带负载能力强;

(4) 主要用于输人级、输出级或缓冲级。

(3) 共基极电路

(1) 输出信号与输人信号相位相同;

(2) 电压放大倍数与共射极电路一样, 但电流放大倍数小于 1 ;

(3) 输人电阻很低, 输出电阻适中;

(4) 主要用于高频和恒流源电路。

【例 2. 2-8】 从共射、共集、共基放大电路的三种基本组态中,选择正确答案填空。

(1)要求电压放大倍数高, 且输人与输出同相位, 应选用

(2)要求带负载能力强,应选用

(3) 要求从信号源吸取的电流小, 应选用

(4)要求对电压和电流都能放大, 应选用

解：(1)共基极电路; (2)共集电极电路; (3)共集电极电路; (4)共射极电路。

\section{2 .3 放大电路的频率特性}

\section{1. 频率特性}

由于放大电路中存在耦合电容、旁路电容和晶体管的极间电容这些电抗元件, 致使电路的 由压放大倍数对于不同频率的正弦信号不再恒定,而是频率的函数。

放大电路对不同频率正弦信号的稳态响应称为频率特性,即

$$
A_{u}=A_{u}(f) \angle \varphi(f)
$$

撸率特性包括幅频特性 $A_{u}(f)$ 和相频特性 $\varphi(f)$ 两部分。

通常, 将频率特性分成三部分: 低频段、中频段和高频段。下限频率由堁合电容和旁路电 渱定,上限频率由管子的极间电容决定。单级 $R C$ 耦合放大电路的对数频率特性(波特图) 如图 2.2-19 所示。

\section{2. 通频带}

当放大倍数 $A_{u}=\left|A_{u}\right|$ 下降到中频放大倍数 $\left|A_{u \mathrm{M}}\right|$ 的 $\frac{1}{\sqrt{2}}(=0.707)$ 时, 所对应的低频频率 和高频频率分别称为下限频率 $f_{\mathrm{L}}$ 和上限频率 $f_{\mathrm{H}}$ 。

通频带 (带宽) 为

$$
f_{\mathrm{BW}}=f_{\mathrm{H}}-f_{\mathrm{L}} \approx f_{\mathrm{H}}
$$

\section{3. 波特图}

幅频特性的横坐标 $f$ 用对数刻度 (即用 $\lg f$ ), 纵坐标用 $20 \lg \left|A_{u}\right|$ (单位为分贝, $\mathrm{dB}$ ) 表 



示; 相频特性的纵坐标为 $\varphi$, 这样绘制的对数频率特性称为波特图(图 2.2-19)。

用折线组成的波特图与实际曲线的误差是: 幅频特性的最大误差为 $3 \mathrm{~dB}$, 在 $f_{\mathrm{L}}$ 和 $f_{\mathrm{H}}$ 处。相 频特性的最大误差为 $\pm 5.71^{\circ}$, 分别在 $0.1 f_{\mathrm{L}}$ 和 $10 f_{\mathrm{L}}$ 及 $0.1 f_{\mathrm{H}}$ 和 $10 f_{\mathrm{H}}$ 处。

\section{4. 增益带宽积}

中频电压放大倍数与通频带的乘积叫做增益带宽积 $\left|A_{\mu \mathrm{M}} f_{\mathrm{H}}\right|$ 。当电路参数和管子选定后, $\left|A_{u M} f_{\mathrm{H}}\right|$ 基本上是个常数, 放大倍数提高多少倍, 频带就变窄多少倍。

【例 2.2-9】电路如图 2.2-13 所示, 写出其下限频率表达式。

解: $C_{\mathrm{b} 1}$ 和 $C_{\mathrm{b} 2}$ 对频率特性的影响可以分开计算。

$$
f_{\mathrm{L} 1}=\frac{1}{2 \pi C_{\mathrm{b} 1}\left(R_{\mathrm{s}}+R_{\mathrm{b}} / / r_{\mathrm{be}}\right)}, f_{12}=\frac{1}{2 \pi C_{\mathrm{b} 2}\left(R_{\mathrm{c}}+R_{\mathrm{L}}\right)}
$$

若 $f_{\mathrm{L}}$ 与 $f_{\mathrm{L} 2}$ 二者相差 4 倍以上, 取数值较大者为放大电路的下限频率 $f_{\mathrm{L}}$ 。

【例 2.2-10】某放大电路的波特图如图 2.2-20 所示, 则



(1) 中频放大倍数为
(A) 20
(B) 40
(C) 100
(D) 120
(2) 上限频率
(B) $=100 \mathrm{kHz}$
(C) $>100 \mathrm{kHz}$
(D) $=10 \mathrm{kHz}$
(3) 下限频率 ;
(A) $<100 \mathrm{~Hz}$
(B) $=100 \mathrm{~Hz}$
(C) $>100 \mathrm{~Hz}$
(D) $=1 \mathrm{KHz}$

(4) 当 $f=f_{\mathrm{L}}$ 或 $f=f_{\mathrm{H}}$ 时, 电路的放大倍数为
(A) $40 \mathrm{~dB}$
(B) $37 \mathrm{~dB}$
(C) $3 \mathrm{~dB}$
(D) $28.28 \mathrm{~dB}$ 解: (1) ( C), (2) (B), (3) (B), (4) (B)。

2.2 .4 反馈的概念、类型及极性; 电压串联负反馈的分析计算

\section{1. 反馈的概念}

(1) 反馈

将放大电路的输出电压或电流的一部分或全部通过反馈网络回送到放大电路的输人端, 与外加信号共同参与控制作用的过程称为反馈。判断有无反馈就是看从输出回路到输人回路 之间有无通路或支路, 有, 则有反馈; 无, 则无反馈。反馈网络可由无源元件或有源器件组成。

(2) 反馈极性: 正反馈和负反馈

正反馈: 反馈量使净输人信号增强的为正反馈, 正反馈使放大倍数增大。

负反馈: 反馈量使净输人信号削弱的为负反馈,负反馈使放大倍数减小。

(3) 直流反馈和交流反馈

直流反馈: 反馈信号中只有直流成分的为直流反馈。直流反馈的作用是稳定静态工作点, 不影响放大电路的动态性能。

交流反馈: 反馈信号中只有交流成分的为交流反馈。交流反馈的作用是改善放大电路的 动态性能。

\section{2. 反馈的四种类型 (或组态)}

通常,反馈的四种类型是对交流负反馈划分的。

(1) 四种反馈类型

按照反馈量取的是输出电压还是输出电流以及在输人端反馈信号与输人信号、净输人信 号是以电压形式相加减还是以电流形式相加减, 把反馈分为电压串联负反馈、电压并联负反 贵、电流串联负反馈和电流并联负反馈。

(2) 四种反馈类型及反馈极性的判别方法

(1) 正、负反馈的判别方法一一瞬时极性法。假定输人信号的瞬时极性 $\rightarrow$ 逐步推断电路中 各相关点的相应极性 $\rightarrow$ 确定输人端反馈信号的瞬时极性 $\rightarrow$ 判断净输人信号是增强了还是削弱 了,增强的是正反馈, 削弱的是负反馈。用 $\oplus$ 表示信号上升, $\ominus$ 表示信号下降。

(2) 电压反馈和电流反馈判别方法。反馈信号与电压成比例的, 称为电压反馈。反馈信号 与电流成比例的, 称为电流反馈。也可用输出电压短路法判别: 假定将输出端对地短路, 若反 信号消失, 则为电压反馈; 若反馈信号依然存在, 则为电流反馈。

(3)串联反馈和并联反馈判别法。串联反馈: 反馈信号与输人信号分别加在两个输人端上, 眼在输人回路以电压形式叠加, 为串联反馈。并联反馈: 反馈信号与输人信号都加在同一个输 人端上, 即以电流形式叠加, 为并联反馈。

【例 2.2-11】四种反馈类型举例。

例 1 : 电压串联负反馈。


(1) 根据瞬时极性法在图中标出瞬时极性, 可知净输人电压 $u_{\mathrm{id}}=u_{\mathrm{i}}-u_{\mathrm{r}}$ 比无反馈时减小, 所以是负反馈。

(2) 利用输出电压短路法将 $R_{\mathrm{I}}$ 短路, 则 $R_{\mathrm{f}}$ 的右端接地, 反馈消失, 所以是电压反馈。

(3) 输人电压和反馈电压分别加在运放器的两个输人端, 净输人信号 $u_{\mathrm{id}}=u_{\mathrm{i}}-u_{\mathrm{f}}$, 在输人 端是电压相减,所以是串联反馈。

综上, 该电路是电压串联负反馈。

电压串联负反馈的特点是: 能稳定输出电压, 提高输人电阻, 降低输出电阻。信号源内阻 $R_{\mathrm{s}}$ 越小, 反馈效果越好。





例 2 : 电压并联负反馈。



并联反馈是电流形式相叠加, 信号源内阻 $R_{\mathrm{s}}$ 越大, 反馈效果越好。

例 3 : 电流串联负反馈。






反馈极性和串、并联反馈的判断方法与例 1 和例 2 相同。该电路当输出端对地交流短路 后, 三极管的工作状态没有改变, $\dot{I}_{\mathrm{o}}$ 依然存在, 反馈信号 $U_{\mathrm{f}}$ 也依然存在, 所以是电流反馈。

电流反馈能稳定输出电流, 提高输出电阻。

例 4 : 电流并联负反馈。


【例 2.2-12】判别图 2.2-25 分别从 $u_{01}$ 输出和从 $u_{02}$ 输出时的反馈类型和极性。 解: 反馈元件是 $R_{\mathrm{e}}$, 为串联负反馈。从 $u_{\mathrm{ol}}$ 输出时, 将输出端对 蛇短路, $I_{\mathrm{e}}$ 电流仍然存在, 反馈信号 $u_{\mathrm{f}}$ 也依然存在, 所以是电流串联 负反馈。

从 $u_{02}$ 输出时, 若将输出端对地短路, 则反馈信号消失, 所以为电 压电联负反馈。

3. 电压串联负反馈的分析计算

电压串联负反馈的闭环电压放大倍数

$$
A_{u f}=\frac{U_{o}}{U_{\mathrm{i}}}=\frac{A_{u}}{1+A_{u} F_{u}}
$$



其中反馈系数 $F_{u}=\frac{\dot{U}_{\mathrm{f}}}{\dot{U}_{\mathrm{o}}}$, 开环放大倍数 $A_{u}=\frac{\dot{U}_{\mathrm{o}}}{\dot{U}_{\mathrm{id}}}, U_{\mathrm{id}}$ 为净输人信号。 $\left|1+\dot{A}_{u} F_{u}\right|$ 为反馈深度, 满 足条件 $\left|1+A_{u} F_{u}\right| \gg 1$, 即 $\left|A_{u} F_{u}\right| \gg 1$ 的反馈称为深度负反馈。

深度负反馈下的闭环电压放大倍数

$$
A_{u f}=\frac{\dot{U}_{o}}{\dot{U}_{\mathrm{i}}}=\frac{A_{u}}{1+A_{u} F_{u}} \approx \frac{1}{F_{u}}
$$

【例 2.2-13】电路如图 2.2-26 所示, 已知 $R_{\mathrm{b} 11}=100 \mathrm{k} \Omega, R_{\mathrm{b} 12}=22 \mathrm{k} \Omega, R_{\mathrm{c} 1}=2.7 \mathrm{k} \Omega, R_{\mathrm{el}}=$ $22 \Omega, R_{\mathrm{b} 21}=24 \mathrm{k} \Omega, R_{\mathrm{b} 22}=4.7 \Omega, R_{\mathrm{c} 2}=2.7 \mathrm{k} \Omega, R_{\mathrm{e} 2}=750 \Omega, R_{\mathrm{f}}=2.4 \mathrm{k} \Omega, R_{\mathrm{s}}=600 \Omega, R_{\mathrm{L}}=1.6$ $\mathrm{t} \Omega, \beta_{1}=\beta_{2}=80$ 。该电路满足深度负反馈条件, 试近似计算闭环电压放大倍数。

解: 深度负反馈条件下, 近似计算闭环电压放大倍数。

反馈系数

$$
F_{u}=\frac{\dot{U}_{\mathrm{f}}}{U_{\mathrm{o}}} \approx \frac{R_{\mathrm{el}}}{R_{\mathrm{f}}+R_{\mathrm{el}}}=\frac{0.022}{2.4+0.022}=0.00908
$$

闭环电压放大倍数

$$
A_{u f} \approx \frac{1}{F_{u}}=\frac{1}{0.00908} \approx 110
$$



\section{2.5 正负反馈的特点, 不同反馈类型对性能的影响}

\section{1. 正、负反馈的特点}

(1) 正反馈的特点

适当引人正反馈, 可提高放大倍数和输人电阻。但使用不当,易造成工作不稳定。

(2) 负反馈的特点

负反馈使放大倍数降低,但能改善放大电路的性能。

\section{2. 不同反馈类型对性能的影响}

\section{(1) 电压负反馈}

电压负反馈能稳定输出电压, 降低输出电阻, 带负载能力强。

(2) 电流负反馈

电流负反馈能稳定输出电流, 提高输出电阻。

(3) 串联负反馈 显。

串联负反馈能提高输人电阻, 减少从信号源汲取的电流, 信号源内阻越小, 反馈作用越明

(4) 并联负反馈

并联负反馈能降低输人电阻, 信号源内阻越大, 反馈作用越明显。

2.2.6 自激的原因及条件, 消除自激的方法, 去耦电路

\section{1. 自激的原因及条件}

产生自激的原因是负反馈在某一频率上变成了正反馈。产生自激的条件是: $\dot{A F}=-1$ 或 $|\overrightarrow{A F}|=1$ —一自激的幅值条件; $\varphi=\varphi_{A}+\varphi_{F}= \pm(2 n+1) \pi$ 一自激的相位条件。

判断能否自激的方法是利用波特图, 对应 $\varphi=\varphi_{A}+\varphi_{F}=180^{\circ}$ 的 $|\dot{A F}| \geqslant 1$ 时, 就会产生自激 振荡。

【例 2.2-14】选择题。

(1) 负反馈放大电路产生自激振荡的条件是
(A) $\dot{A F}=0$
(B) $\dot{A} \dot{F}=1$
(C) $\dot{A F}=-1$
(D) $\dot{A} \dot{F}=\infty$

(2) 共射极基本放大电路,如果通过电阻引进负反馈
(A) 一定会产生高频自激振荡
(B) 一定满足自激振荡的相位条件
(C) 一定不会产生高频自激振荡
(D) 不能确定

解: (1) (C), (2) (C)。

\section{2. 消除自激的方法, 去耦电路}

\section{(1) 消除自激的方法}

消除自激的方法有(1)减小反馈系数 $F$; (2)接人校正网络。实际常用的校正网络如图 2.227 所示。

\section{(2) 去耦电路}

在多级放大电路中, 由于共用的直流电源存在内阻, 各级的交流电流经过该内阻相互影 响。在内阻上产生的交流电压, 对电路的某一级可能形成正反馈, 使放大电路自激。在图 2. 2-28中对第一级形成正反馈。消除自激的有效办法是接人去耦电路, 图中 $R_{\phi}$ 和 $C_{\phi}$ 组成去耦 电路。在电源内阻上产生的交流电压经 $R_{\phi}$ 与 $C_{\phi}$ 分压后, 再加于 $R_{\mathrm{bl}}$ 上, 只要满足 $R_{\phi} \gg$ $\frac{1}{\omega_{1} C_{\phi}}$, 就可大大削弱对第一级的正反馈, 使电路保持正常工作, $\omega_{\mathrm{L}}$ 是电路的下限角频率。




\section{3 线性集成运算放大器和运算电路}

\subsection{1 差动放大电路}

\section{1. 差动放大电路的工作原理}


(1) 静态

假定电路为完全对称的理想状态, 即 $\mathrm{T}_{1}$ 和 $\mathrm{T}_{2}$ 的特性完全一样, $R_{\mathrm{c} 1}=R_{\mathrm{c} 2}$ 。当输人信号 $u_{\mathrm{i} 1}$ $=u_{\mathrm{i} 2}=0$ 时, $i_{\mathrm{c} 1}=i_{\mathrm{c} 2}, R_{\mathrm{c} 1} i_{\mathrm{c} 1}=R_{\mathrm{c} 2} i_{\mathrm{c} 2}$, 输出电压 $u_{\mathrm{o}}=u_{\mathrm{c} 1}-u_{\mathrm{c} 2}=0$ 。

(2) 动态

若 $u_{\mathrm{i} 1}$ 和 $u_{\mathrm{i} 2}$ 不等于零, 而且大小相等, 极性相反, 即 $u_{\mathrm{i} 1}=-u_{\mathrm{i} 2}$, 将使 $i_{\mathrm{c1}}$ 增加, $i_{c 2}$ 等量减少, 则 $u_{\mathrm{a}}=u_{\mathrm{ci}}-u_{\mathrm{c} 2} \neq 0$, 有放大输出。

若 $u_{\mathrm{i} 1}$ 和 $u_{\mathrm{i} 2}$ 不等于零, 但大小相等, 极性相同, 即 $u_{\mathrm{i} 1}=u_{\mathrm{i} 2}$, 则 $i_{\mathrm{c} 1}$ 和 $i_{\mathrm{c} 2}$ 将作相同的变化, $u_{\mathrm{o}}=$ $u_{\mathrm{c}}-u_{\mathrm{c} 2}=0$, 放大器没有输出。

\section{2. 差模、共模、零漂的概念}

(1) 差模

大小相等, 极性相反, 即 $u_{\mathrm{i1}}=-u_{\mathrm{i} 2}$ 的两个输人信号称为差模信号。

(2) 共模

大小相等, 极性相同, 即 $u_{\mathrm{i} 1}=u_{\mathrm{i} 2}$ 的两个输人信号称为共模信号。

(3) 零漂 (零点漂移的简称)

当放大电路的输人端短路时, 输出端仍有不规则缓慢变化的输出电压产生, 致使放大电路 侮离零点。产生零漂的主要原因是晶体管参数 $U_{\mathrm{BE}} \beta 、 I_{\mathrm{CBO}}$ 随温度的变化而变化。

$\Delta U_{\mathrm{i}}=\Delta U_{\mathrm{o}} /\left(A_{u} \Delta T\right)$ 是衡量零漂的指标, 即把温度变化 $1^{\circ} \mathrm{C}$ 时输出电压漂移量除以电压放 大倍数折合成输入电压作为漂移参数值。

\section{3. 差动放大电路的四种接法}

差动放大电路的四种接法是: (1)双端输人一双端输出, 见图 2.3-1; (2)双端输人一单端输 出, 见图 2.3-2; (3)单端输人一双端输出, 见图 2.3-3; (4)单端输人一单端输出, 见图 2.3-4。 









\section{4. 静态及动态的分析计算}

\section{(1) 静态分析}

静态分析就是求静态工作点。对长尾电路 (如图 2.3-1 有 $R_{\mathrm{e}}$ 的电路) 和恒流源电路 ( $R_{\mathrm{e}}$ 由 恒流源代替),均可认为三极管基极对地的电位 $U_{\mathrm{B}} \approx 0$ 。 可得

$$
\begin{aligned}
& I_{\mathrm{Cl}}=I_{\mathrm{C} 2}=\approx \frac{I_{\mathrm{E}}}{2} \approx \frac{U_{\mathrm{EE}}-U_{\mathrm{BE}}}{2 R_{\mathrm{e}}}\left(I_{\mathrm{E}} \text { 为流过 } R_{\mathrm{e}} \text { 的电流 }\right) \\
& I_{\mathrm{B} 1}=I_{\mathrm{B} 2}=\frac{I_{\mathrm{C} 1}}{\beta}, U_{\mathrm{CE} 1}=U_{\mathrm{CE} 2}=U_{\mathrm{CB} 1}+U_{\mathrm{BE} 1} \\
& U_{\mathrm{CB} 1}=U_{\mathrm{CC}}-I_{\mathrm{C} 1} R_{\mathrm{c} 1}-U_{\mathrm{B}} \approx U_{\mathrm{CC}}-I_{\mathrm{C} 1} R_{\mathrm{c} 1}
\end{aligned}
$$

所以

$$
U_{\mathrm{CE} 1}=U_{\mathrm{CE} 2}=U_{\mathrm{CC}}-I_{\mathrm{C} 1} R_{\mathrm{cl}}+U_{\mathrm{BE} 1}
$$

(2) 动态指标计算

在单端输人时,一般 $R_{\mathrm{e}}$ 足够大, 所以结果与双端输人一样。

(1) 差模电压放大倍数。 双端输出:

$$
A_{u \mathrm{~d}}=\frac{u_{\mathrm{ol}}-u_{\mathrm{o} 2}}{u_{\mathrm{i} 1}-u_{\mathrm{i} 2}}=\frac{2 u_{\mathrm{o} 1}}{2 u_{\mathrm{i} 1}}=\frac{-\beta R_{\mathrm{L}}^{\prime}}{R_{\mathrm{s}}+r_{\mathrm{be}}}, R_{\mathrm{L} .}^{\prime}=R_{\mathrm{c}} / / \frac{1}{2} R_{\mathrm{L}}
$$

单端输出: 从 $T_{1}$ 的集电极输出

$$
A_{u \mathrm{dl}}=\frac{u_{\mathrm{o} 1}}{u_{\mathrm{i} 1}-u_{\mathrm{i} 2}}=\frac{u_{\mathrm{ol}}}{2 u_{\mathrm{i} 1}}=-\frac{1 \beta R_{\mathrm{L}}^{\prime}}{2 R_{\mathrm{s}}+r_{\mathrm{be}}}
$$

$M \mathrm{~T}_{2}$ 的集电极输出

$$
\begin{aligned}
& A_{u \mathrm{~d} 2}=\frac{u_{\mathrm{o} 2}}{u_{\mathrm{i} 1}-u_{\mathrm{i} 2}}=\frac{u_{\mathrm{o} 2}}{2 u_{\mathrm{i} 1}}=+\frac{1 \beta R_{\mathrm{L}}^{\prime}}{2 R_{\mathrm{s}}+r_{\mathrm{be}}} \\
& R_{\mathrm{L} .}^{\prime}=R_{\mathrm{c}} / / R_{\mathrm{L}}
\end{aligned}
$$

(2) 共模电压放大倍数。

双端输出时

$$
A_{u \mathrm{c}}=\frac{u_{\mathrm{ol}}-u_{\mathrm{o} 2}}{u_{\mathrm{ic}}} \approx 0
$$

单端输出时

$$
A_{u \mathrm{c}} \approx-\frac{R_{\mathrm{L}}^{\prime}}{2 R_{\mathrm{e}}}, R_{\mathrm{L}}^{\prime}=R_{\mathrm{c}} / / R_{\mathrm{L}}
$$

(3) 共模抑制比。

双端输出时

$$
K_{\mathrm{CMR}}\left|\frac{A_{u \mathrm{~d}}}{A_{u c}}\right| \approx \infty
$$

单端输出时

$$
K_{\text {CMR }}=\left|\frac{A_{u d l}}{A_{u c l}}\right| \approx \frac{\beta R_{\mathrm{e}}}{R_{\mathrm{s}}+r_{\text {be }}}
$$

(4) 差模输人电阻: 双端与单端差模输人电阻一样, 为 $R_{\mathrm{id}} \approx 2\left(R_{\mathrm{s}}+r_{\mathrm{be}}\right)$ 。

(5) 差模输出电阻: 双端输出 $R_{\mathrm{od}} \approx 2 R_{\mathrm{c}}$, 单端输出 $R_{\mathrm{od}} \approx R_{\mathrm{c}}$ 。

(3) 输入信号的分解

如果两个输人信号的大小、极性都是任意的, 可分解成差模信号 $u_{\text {id }}$ 和共模信号 $u_{\text {ic。 }}$ 。

$$
u_{\mathrm{id}}=u_{\mathrm{i} 1}-u_{\mathrm{i} 2}, u_{\mathrm{ic}}=\frac{1}{2}\left(u_{\mathrm{i} 1}+u_{\mathrm{i} 2}\right)
$$

输出电压

$$
u_{\mathrm{o}}=A_{u \mathrm{~d}} u_{\mathrm{id}}+A_{u \mathrm{c}} u_{\mathrm{ic}}
$$

【例 2.3-1】图 2.3-1 所示差动放大电路, 已知 $U_{\mathrm{CC}}=U_{\mathrm{EE}}=12 \mathrm{~V}, R_{\mathrm{s}}=1 \mathrm{k} \Omega, R_{\mathrm{c}}=R_{\mathrm{cl}}=R_{\mathrm{c} 2}$ $=10 \mathrm{k} \Omega, R_{\mathrm{e}}=10 \mathrm{k} \Omega, R_{\mathrm{t}}=12 \mathrm{k} \Omega$, 两晶体管参数相同 $\beta=60, r_{\mathrm{be}}=1.5 \mathrm{k} \Omega, U_{\mathrm{BE}}=0.6 \mathrm{~V}$ 。试 求:

(1) 静态工作点 $I_{\mathrm{B}}, I_{\mathrm{C}}, U_{\mathrm{CE}}$;

(2) 当 $u_{\mathrm{i} 1}=10 \mathrm{mV}, u_{\mathrm{i} 2}=-2 \mathrm{mV}$ 时, (1)双端输出电压 $u_{\mathrm{o}}$, (2)负载电阻 $R_{\mathrm{L}}$ 接在 $C_{1}$ 与地之间 时, 单端输出电压 $u_{\mathrm{ol}}$;

(3) 差模输人电阻 $R_{\text {id }}$ 、单端输出电阻 $R_{\mathrm{od}}$ 。

解: (1) 静态工作点: $I_{\mathrm{C}} \approx I_{\mathrm{E}}=\frac{U_{\mathrm{EE}}-U_{\mathrm{BE}}}{2 R_{\mathrm{e}}}=\frac{12-0.6}{2 \times 10}=0.57 \mathrm{~mA}, I_{\mathrm{B}}=\frac{I_{\mathrm{C}}}{\beta}=\frac{0.57}{60}=9.5 \mu \mathrm{A}$, $U_{\mathrm{CE}}=U_{\mathrm{CC}}-I_{\mathrm{C}} R_{\mathrm{e}}+U_{\mathrm{BE}}=12-0.57 \times 10+0.6=6.9 \mathrm{~V}$ 。

(2) 首先将信号分解成差模信号和共模信号, 差模信号 $u_{\mathrm{id}}=u_{\mathrm{i} 1}-u_{\mathrm{i} 2}=10-(-2)=12$ $\mathrm{mV}$, 共模信号 $u_{\mathrm{ic}}=\left(u_{\mathrm{i} 1}+u_{\mathrm{i} 2}\right) / 2=(10-2) / 2=4 \mathrm{mV}$ 。

(1)求双端输出电压 $u_{0}$ 。 

$$
R_{\mathrm{L} .}^{\prime}=R_{\mathrm{c}} / /\left(R_{\mathrm{L}} / 2\right)=10 / / 6=3.75 \mathrm{k} \Omega
$$

差模电压放大倍数

$$
\begin{aligned}
& A_{u \mathrm{~d}}=-\frac{\beta R_{\mathrm{L}}^{\prime}}{R_{\mathrm{s}}+r_{\mathrm{be}}}=-\frac{\beta \times\left(R_{\mathrm{c}} / / \frac{R_{\mathrm{L}}}{2}\right)}{R_{\mathrm{s}}+r_{\mathrm{be}}}=\frac{60 \times(10 / / 6)}{1+1.5}=-90 \\
& u_{\mathrm{o}}=A_{u \mathrm{~d}} u_{\mathrm{id}}=-90 \times 12=-1080 \mathrm{mV}=1.08 \mathrm{~V}
\end{aligned}
$$

(2)求单端输出电压 $u_{\mathrm{ol}}$ 。

$$
R_{\mathrm{L}}^{\prime}=R_{\mathrm{c}} / / R_{\mathrm{L}}^{\prime}=10 / / 12=5.45 \mathrm{k} \Omega
$$

差模电压放大倍数

$$
A_{u \mathrm{~d} l}=\frac{1 \beta R_{\mathrm{L}}^{\prime}}{2 R_{\mathrm{s}}+r_{\mathrm{be}}}=\frac{1}{2} \times \frac{60 \times 5.45}{1+1.5}=-65.4
$$

共模电压放大倍数

$$
\begin{aligned}
& A_{u \mathrm{c}} \approx-\frac{R_{\mathrm{t}}^{\prime}}{2 R_{\mathrm{e}}}=-\frac{5.45}{2 \times 10} \approx-0.27 \\
& u_{\mathrm{o}}=A_{u \mathrm{dl}} u_{\mathrm{id}}+A_{u \mathrm{c}} u_{\mathrm{ic}}=-65.4 \times 12-0.27 \times 4 \approx-786 \mathrm{mV}
\end{aligned}
$$

(3) $R_{\mathrm{id}}=2\left(R_{\mathrm{s}}+r_{\mathrm{be}}\right)=2 \times(1+1.5)=5 \mathrm{k} \Omega$

$$
R_{\text {od }}=R_{\mathrm{c}}=10 \mathrm{k} \Omega
$$

\section{5. 输入输出相位关系}

根据输出电压与输人电压的相位关系, 输人端分为同相输人端和反相输人端。在图 2. 3-1 中, 当输出为 $u_{o}$ 或 $u_{\mathrm{ol}}\left(C_{1}\right.$ 点) 时, $u_{\mathrm{i} 1}$ 与 $u_{\mathrm{o}}$ (或 $u_{\mathrm{ol}}$ ) 的相位相反, $u_{\mathrm{i} 1}$ 称为反相输人端; $u_{\mathrm{i} 2}$ 与 $u_{\mathrm{o}}$ 或 $u_{\mathrm{o} 1}$ 的相位相同, $u_{\mathrm{i} 2}$ 称为同相输人端。当从 $C_{2}\left(u_{\mathrm{o} 2}\right)$ 点单端输出时, $u_{\mathrm{i} 1}$ 则为同相输人端, $u_{\mathrm{i} 2}$ 则为 反相输人端。输出与输人同相位, 则放大倍数是正的, 输出与输人反相位, 则放大倍数是负的。

\section{6. 零漂抑制原理}

零点漂移主要是温度的影响, 由于温度对放大电路的影响是一致的, 所以是个共模信号。 差动放大电路抑制零漂的原理主要是利用 $\mathrm{T}_{1} 、 \mathrm{~T}_{2}$ 的对称性和通过 $R_{\mathrm{e}}$ 引进共模负反馈。 $R_{\mathrm{e}}$ 越 大, 抑制效果越显著。但由于电源的限制和集成电路中不能制造大电阻, 为此采用恒流源代替 $R_{\mathrm{e}}$ 。恒流源的交流电阻很大, 从而比 $R_{\mathrm{e}}$ 抑制共模信号的作用更强。

【例 2.3-2】选择正确的答案。

(1) 共模抑制比 $K_{\mathrm{CMR}}$ 是___ 之比。

(A) 差模信号与共模信号之比

(B) 输人量中差模成分与共模成分之比

(C) 差模电压放大倍数绝对值与共模电压放大倍数绝对值之比

(D) 交流放大倍数绝对值与直流放大倍数绝对值之比

(2) $K_{\mathrm{CMR}}$ 越大, 表明电路

(A) 放大倍数越稳定

(B)交流放大倍数越大

(C) 抑制温漂能力越强

(D) 输人信号中差模成分越大

解: (1) (C), (2) (C)。 2.3.2 集成运放的特点及组成, 复合管的正确接法及等效参数的计算, 恒流源作 有源负载和偏置电路

\section{1. 集成运放的特点及组成}

(1) 特点

集成运放是高增益的直接耦合多级放大电路。

(2) 组成

集成运放通常由四部分组成(图 2.3-5)。



(1) 差动输人级: 是提高性能指标的关键, 均采用差动放大电路。

(2) 电压放大级: 主要用来提高电压放大倍数,通常采用恒流源负载。

(3) 输出级:一般采用由复合管组成的甲乙类互补推挽功率放大电路。

(4) 偏置电路: 为整个电路提供稳定和合适的偏置电流, 一般由恒流源构成。

\section{2. 复合管的正确接法及等效参数的计算}

(1) 相同极性三极管组成的复合管

(1)正确接法如图 2.3-6。(2)等效参数为: $\beta \approx \beta_{1} \beta_{2}, r_{\mathrm{be}} \approx r_{\mathrm{bel}}+\beta_{1} r_{\mathrm{b} 22}$ 。(3)等效三极管的极性, 与原来的极性相同。(4)各电极名称不变。


(2) 不同极性三极管组成的复合管

(1)正确接法如图 2.3-7。(2)等效参数为: $\beta \approx \beta_{1} \beta_{2}, r_{\mathrm{be}} \approx r_{\mathrm{bel}}$ 。(3)等效三极管的极性, 与最前 面的(第一个管) 极性相同。(4)各电极名称, 由最前面的(第一个管) 电极名称决定。



两管发射极电流方向一致, 就正确; 否则就错误。

【例 2.3-3】复合管电路如图 2.3-8 所示, 设 $T_{1} 、 T_{2}$ 的电流放大系数分别为 $\beta_{1} 、 \beta_{2}$, 输人电 阻分别为 $r_{\text {bel }} 、 r_{\text {be } 2}$ 。要求:

(1) 分别画出等效晶体管符号 (电极名称);

(2) 写出等效晶体管的 $\beta$ 与 $\beta_{1} 、 \beta_{2}$ 的关系式;

(3) 写出各复合管的输人电阻表达式。











解: (1) 图 (a)、(d) 为 PNP 管, 图 (b)、(c) 为 NPN 管。等效晶体管符号如图 2.3-9 所示。

(2) 图 (a)、(b)、(c)、(d) 均为 $\beta \approx \beta_{1} \beta_{2}$ 。

(3) 图 (a)、 (b) 由同类型管子组成, 输人电阻包括两个发射结, 所以 $r_{\mathrm{be}}=r_{\mathrm{bel}}+\left(1+\beta_{1}\right) r_{\mathrm{be}}$; 图 (c)、(d) 由不同类型管子组成, 输人电阻只包括一个发射结, 所以 $r_{\text {be }}=r_{\text {bel }}$ 。

【例 2. 3-4】判断图 2.3-10 中各复合管连接是否正确。如正确, 各分别等效为何种极性 的晶体管,管脚 $1 、 2 、 3$ 分别对应什么电极。

解: 图 ( a ) 连接正确, 等效晶体管为 PNP 型, 管脚 $1-\mathrm{e}$ 极, 管脚 $2-\mathrm{b}$ 极, 管脚 $3-\mathrm{c}$ 极。图 (b) 连接不正确,因为 $\mathrm{T}_{1}$ 和 $\mathrm{T}_{2}$ 发射极电流方向不一致。








\section{3. 恒流源作有源负载和偏置电路}

\section{（1）镜像电流源}


\section{(2) 有源负载}


(3) 偏置电路

恒流源作为偏置电路, 可为放大器提供稳定的偏置电流。图 2.3-13 中 $\mathrm{T}_{3} 、 \mathrm{~T}_{4} 、 R$ 组成的恒 流源为 $\mathrm{T}_{1} 、 \mathrm{~T}_{2}$ 提供偏置电流。又由于恒流源的交流电阻很大, 相当于长尾电路中的 $R_{\mathrm{e}}$ 很大, 使 共模抑制能力很强。

【例 2. 3-5】图 2.3-14 中, $U_{\mathrm{CC}}=6.5 \mathrm{~V},-U_{\mathrm{EE}}=-6.5 \mathrm{~V}, R_{2}=12.4 \mathrm{k} \Omega, \mathrm{T}_{1} \sim \mathrm{T}_{7}$ 的 $\beta=100$, $\left|U_{\mathrm{BE}}\right|=0.6 \mathrm{~V} ; r_{\mathrm{bel}}=r_{\mathrm{be} 2}=5.3 \mathrm{k} \Omega$, 试问:

(1) 各三极管分别组成何种功能的电路?

(2) 求静态电流 $I_{\mathrm{c} 1}$ 和 $I_{\mathrm{c} 2}$ 。

解: (1) $\mathrm{T}_{1} 、 \mathrm{~T}_{2}$ 组成差动放大电路。 $\mathrm{T}_{3} 、 \mathrm{~T}_{4}$ 组成镜像恒流源, 作为差动放大电路的有源负载。 $\mathrm{T}_{3} 、 \mathrm{~T}_{6}$ 组成镜像恒流源, 作为差动放大电路的偏置电路。 $\mathrm{T}_{7}$ 组成共射极放大电路。

(2) 首先求出 $\mathrm{T}_{5} 、 \mathrm{~T}_{6}$ 组成的镜像恒流源的输出电流 $I_{\mathrm{e} 5}$ 。

$$
\begin{aligned}
& I_{\mathrm{C} 5} \approx I_{\mathrm{REF}}=\frac{U_{\mathrm{CC}}-\left(-U_{\mathrm{EE}}\right)-U_{\mathrm{BE}}}{R_{2}}=\frac{13-0.6}{12.4}=1 \mathrm{~mA} \\
& I_{\mathrm{Cl}}=I_{\mathrm{C} 2}=\frac{1}{2} I_{\mathrm{C} 5}=0.5 \mathrm{~mA}
\end{aligned}
$$





\section{4. 集成运算放大器参数的含义}

(1)开环差模电压放大倍数 $A_{u 0}$ : 无反馈情况下的直流差模电压增益。

(2)输人失调电压 $U_{\mathrm{io}}$ : 为使输出电压为零, 在输人端所需加人的补偿电压。它反映了电路 的对称程度的好坏。数值越大, 说明对称程度越差。

(3)输人失调电流 $I_{\mathrm{i} 0}$ : 当输出电压为零时, 流人放大器两输人端的静态基极电流之差。

(4)输人偏置电流 $I_{\mathrm{iB}}$ : 输出电压为零时, 两个输人端静态电流的平均值。

(5)温漂: 由输人失调电压和输人失调电流随温度的漂移所引起的。其中输人失调电压温 漂 $\Delta U_{\mathrm{in}_{0}} / \Delta T$ 为在规定工作范围内 $U_{\text {io }}$ 的温度系数。输人失调电流温漂 $\Delta I_{\mathrm{io}} / \Delta T$ 为在规定工作 范围内 $I_{\mathrm{ie}}$ 的温度系数。

(6)共模抑制比 $K_{\mathrm{CMR}}$ : 差模电压放大倍数与共模电压放大倍数之比的绝对值。

(7)差模输人电阻 $r_{\text {id }}$ : 两个输人端之间的等效动态电阻。 (8)输出电阻 $r_{\mathrm{o}}$ : 从输出端和地之间看进去的动态电阻。

(9)最大差模输人电压 $U_{\text {idmax }}$ : 反相和同相输人端所能承受的最大电压值。

(10最大共模输人电压 $U_{\text {icmax }}$ : 所能承受的最大共模输入电压值。

(11)最大输出电流 $I_{\text {omax }}$ : 所能输出的正向或反向峰值电流。

(12)开环带宽 $B W\left(f_{\mathrm{H}}\right)$ : 开环差模电压增益下降 $3 \mathrm{~dB}$ 时对应的上限频率 $f_{\mathrm{H}}$ 。

(13)转换速率 $S_{\mathrm{R}}$ : 放大电路在闭环状态下, 输人为大信号时, 输出电压对时间的最大变化率。

2.3.3 多级放大电路的耦合方式及频率响应

\section{1. 耦合方式}

(1) 阻容耦合

各级之间静态工作点相互独立,零点漂移可忽略。不能放大缓慢变化的信号。

(2) 直接耦合

各级之间静态工作点相互影响, 存在零点漂移。能放大缓慢变化的信号。由于在集成电 路中还不能制作大容量电容, 所以集成运算放大器为直接耦合多级放大电路。

(3) 变压器耦合

各级之间静态工作点相互独立,利用变比的不同可以提高放大作用和输出功率。

\section{2. 频率响应}

将几级放大电路串接起来, 放大倍数提高, 但频带变窄, 即 $f_{\mathrm{L}}$ 增大, $f_{\mathrm{H}}$ 减小。

【例 2.3-6】选择正确的答案填空。

(1) 多级放大电路的通频带与各级通频带之间的关系

(A) 比通频带最窄的还要窄

(B) 比通频带最宽的还要宽

(C) 各级通频带的平均值

(D) 各级通频带的乘积

(2) 具有相同参数的两级放大电路, 在各级的截止频率处, 电压增益的幅值下降
(A) $3 \mathrm{~dB}$
(B) $6 \mathrm{~dB}$
(C) $20 \mathrm{~dB}$
(D) $9 \mathrm{~dB}$

解: (1) (A), (2) (B)。

\subsection{4 基本运算电路}

\section{1. 理想运放的虚短、虚地、虚断概念及其分析方法}

(1) 理想运放的模型

满足以下理想化参数的运放称为理想运放。

(1) 开环差模电压放大倍数 $A_{u \mathrm{o}}=\infty$;

(2) 差模输人电阻 $r_{\text {id }}=\infty$;

(3) 输出电阻 $r_{\mathrm{o}}=0$;

(4) 输人失调电压 $U_{\mathrm{io}}=0$;

(5) 输人失调电流 $I_{\mathrm{io}}=0$;

(6) 输人偏置电流 $I_{\mathrm{iB}}=0$;

(7) 输人失调电压温漂 $\Delta U_{\mathrm{io}} / \Delta T=0$;

(8) 输人失调电流温漂 $\Delta I_{\mathrm{io}} / \Delta T=0$;

(9) 共模抑制比 $K_{\mathrm{CMR}}=\infty$;

(10) 开环带宽 $B W\left(f_{\mathrm{H}}\right)=\infty$; (11) 转换速率 $S_{\mathrm{R}}=\infty$ 。

(2) 虚短、虚地、虚断概念

虚短和虚断是线性工作状态下理想集成运放的两个重要特点。

虚短: 由于 $A_{u \mathrm{~d}} \rightarrow \infty, u_{\mathrm{id}}=u_{\mathrm{N}}-u_{\mathrm{P}}=0$, 即同相输人端与反相输人端的电位相等, 二者之间接 近于短路, 而又不是真正的短路, 所以称为虚短。

虚断: 由于 $r_{\mathrm{id}} \rightarrow \infty$, 两个输人端的电流 $i_{\mathrm{N}}=i_{\mathrm{P}}=0$, 即输人端好似断路, 而又并非真的断路, 所以称为虚断。

虚地: 当同相端直接或通过电阻接地时, 因为存在虚短, 则反相端虚地。可见虚地只有在 同相输人端是地电位的条件下才存在。

(3) 理想运放的分析方法

(1) 首先判断运放器是否具有深度负反馈。存在深度负反馈, 则运放器工作在线性区。只 有工作在线性状态, 虚短、虚地才成立。若运放器处于开环状态或有正反馈, 则运放器工作在 非线性状态, 虚短、虚地不成立。

(2) 利用虚短、虚地、虚断的特点,求输出和输人的运算关系。当有多个输人信号时, 利用 叠加原理求解。

(3) 工作在线性区, 一般都具有深度电压负反馈, 各级输出电阻近似为零。因此, 对于多级 运算电路,不必考虑前后级之间的影响。

(4) 求解较复杂的电路时, 首先确定每个运放器的功能, 写出其输人、输出函数关系, 最后 得到整个电路的运算关系。

\section{2. 比例、加减运算电路及其电压传输特性}

(1) 反相比例运算电路






(2) 同相比例运算电路


$$
u_{\mathrm{o}}=\frac{R_{1}+R_{\mathrm{f}}}{R_{1}} u_{\mathrm{s}}=\left(1+\frac{R_{\mathrm{f}}}{R_{1}}\right) u_{\mathrm{s}}
$$

因为 $u_{\mathrm{N}}=u_{\mathrm{p}} \neq 0$, 有共模输人电压, 所以同相输人不存在虚地。同相比例运算电路是个深 度电压串联负反馈电路 (3) 反相加法运算电路






(4) 同相加法运算电路


$$
u_{\mathrm{o}}=\left(1+\frac{R_{\mathrm{f}}}{R_{3}}\right)\left(\frac{R_{2}}{R_{1}+R_{2}} u_{\mathrm{s} 1}+\frac{R_{1}}{R_{1}+R_{2}} u_{\mathrm{s} 2}\right)
$$

当 $R_{1}=R_{2}=R_{3}=R_{\mathrm{f}}$ 时, $u_{\mathrm{o}}=u_{\mathrm{s} 1}+u_{\mathrm{s} 2}$ 。

(5) 差动输入减法运算电路


$$
, u_{\mathrm{o}}=\left(\frac{R_{1}+R_{\mathrm{f}}}{R_{\mathrm{1}}}\right)\left(\frac{R_{3}}{R_{2}+R_{3}}\right) u_{\mathrm{s} 2}-\frac{R_{\mathrm{f}}}{R_{1}} u_{\mathrm{s} 1}
$$

若满足 $R_{\mathrm{f}} / R_{1}=R_{3} / R_{2}$, 则 $u_{\mathrm{o}}=\frac{R_{\mathrm{f}}}{R_{1}}\left(u_{\mathrm{s} 2}-u_{\mathrm{s} 1}\right)$ 。





(6) 电压跟随器


【例 2.3-7】在图 2.3-21 中, 运放器为理想的。写出各输出电压的数值。 


解: $u_{\mathrm{oa}}=\left(1+\frac{60}{120}\right) \times 0.2=1.5 \times 0.2=0.3 \mathrm{~V}, u_{\mathrm{ob}}=-\frac{60}{120} \times 0.2=-0.1 \mathrm{~V}$

$u_{\mathrm{oc}}=3 \mathrm{~V}$ (该电路是电压跟随器), $u_{\mathrm{od}}=-\frac{30}{15} \times 1+\left(1+\frac{30}{15}\right) \times 3=-2+9=7 \mathrm{~V}$

(7) 比例及加减运算电路的电压传输特性

运算电路的输出电压 $u_{\mathrm{o}}$ 与输人电压 $u_{\mathrm{i}}$ 的关系曲线称为电压传输特性。

【例 2.3-8】电路如图 2.3-22 所示, 设运放器为理想的, 要求画出其电压传输特性。

解: 该电路是一个反相比例运算电路, 其输出端有稳压管限幅, 最大输出电压为 $\pm 8 \mathrm{~V} 。 u_{0}$ $=-\frac{120}{12} u_{\mathrm{i}}=-10 u_{\mathrm{i}}$ 。当 $u_{\mathrm{o}}=8 \mathrm{~V}$ 时, $u_{\mathrm{i}}=-\frac{8}{10}=-0.8 \mathrm{~V}$ 。同样, 当 $u_{\mathrm{o}}=-8 \mathrm{~V}$ 时, $u_{\mathrm{i}}=0.8 \mathrm{~V}$ 。 电压传输特性如图 2.3-23 所示。







【例 2.3-9】图 2.3-24 为某运算电路的电压传输特性, 试问:

(1) 输人与输出电压之间的运算关系;

(2) 电压放大倍数为多少?

(3) 若输人电压为正弦信号时,最大不失真输出电压的有效值为多少?

解: (1) 从图可知 $u_{\mathrm{i}}>0, u_{\mathrm{o}}>0$ 。同样 $u_{\mathrm{i}}<0, u_{\mathrm{o}}<0$ 。可见输出与输人同相位, 所以是同相 比例运算电路。 （2）在线性范围内有 $\Delta u_{\mathrm{o}} / \Delta u_{\mathrm{i}}=1$, 所以电压放大倍数 $A_{u}=\Delta u_{\mathrm{o}} / \Delta u_{\mathrm{i}}=1$ 。

(3) 最大不失真输出电压的有效值为 $\frac{5.6}{\sqrt{2}} \approx 3.96 \mathrm{~V}$ 。

\section{3. 积分、微分电路的工作原理}

\section{(1) 积分电路}


$$
u_{\mathrm{o}}=-\frac{1}{C} \int i_{C} \mathrm{~d} t+U_{\infty}=-\frac{1}{R C} \int u_{\mathrm{s}} \mathrm{d} t+U_{\infty}
$$

若电容 $C$ 的初始电压 $U_{\omega 0}=0$, 则

$$
u_{\mathrm{o}}=-\frac{1}{C} \int i_{C} \mathrm{~d} t=-\frac{1}{R C} \int u_{\mathrm{s}} \mathrm{d} t
$$





当 $u_{\mathrm{s}}$ 为阶跃电压时, $u_{\mathrm{o}}=-\frac{U_{\mathrm{s}}}{R C} t, u_{\mathrm{o}}$ 与时间 $t$ 成线性关系, 如图 2.3-26 所示。 $U_{\mathrm{o}}$ 增长到 $U_{\mathrm{om}}$ 时, 积分停止。此时运放进人饱和状态, $U_{\mathrm{om}}$ 为运放器的最大输出电压。

【例 2. 3-10】电路如图 2.3-25 所示, 运放是理想的。已知电容 $C$ 的初始电压 $U_{\infty}=0, R$ $=100 \mathrm{k} \Omega, C=4 \mu \mathrm{F}$ 。在 $t=0$ 时加上 $1 \mathrm{~V}$ 的直流电压, 试求 2 秒钟后的 $u_{\mathrm{o}}$ 值。

解: $u_{\mathrm{o}}=-\frac{1}{R C} \int u_{\mathrm{s}} \mathrm{d} t=-\frac{1}{R C} U_{\mathrm{s}} t=-\frac{1}{100 \times 10^{3} \times 4 \times 10^{-6}} \times 1 \times 2=-5 \mathrm{~V}$

(2) 微分电路






【例 2.3-11】图 2.3-27 所示的微分电路, 运放是理想的。已知 $R=10 \mathrm{k} \Omega, C=100 \mu \mathrm{F}, u_{\mathrm{s}}$ 的波形如图 2.3-29 所示,试画出 $u_{0}$ 的波形,并标出有关数值。





解: $u_{\mathrm{o}}=-R C \frac{\mathrm{d} u_{\mathrm{s}}}{\mathrm{d} t}=-\frac{\mathrm{d} u_{\mathrm{s}}}{\mathrm{d} t}$

(1) $0 \sim 10$ 秒段: $u_{\mathrm{ol}}=-\frac{\mathrm{d} u_{\mathrm{s}}}{\mathrm{d} t}=\frac{-1}{10} \mathrm{~V}=-0.1 \mathrm{~V}$ 。

(2) $10 \sim 30$ 秒段: $u_{\mathrm{o} 2}=\frac{\mathrm{d} u_{\mathrm{s}}}{\mathrm{d} t}=0 \mathrm{~V}$ 。

(3) $30 \sim 40$ 秒段: $u_{\mathrm{o}}=-\frac{\mathrm{d} u_{\mathrm{s}}}{\mathrm{d} t}=\frac{1}{10}=0.1 \mathrm{~V}$ 。

$u_{0}$ 的波形如图 2.3-30 所示。

\subsection{5 实际运算放大器运算电路的分析}

\section{1. 只考虑 $A_{u 0} \neq \infty$ 的情况}


由于 $A_{u o} \neq \infty$, 所以虚短不成立, $u_{\mathrm{N}} \neq 0$, 即 $u_{\mathrm{N}}=$ $-\frac{u_{\mathrm{o}}}{A_{u 0}}$ 。因为仍有 $r_{\mathrm{id}}=\infty$, 所以 $i_{\mathrm{i}}=0$, 于是 $\frac{u_{\mathrm{s}}-u_{\mathrm{N}}}{R_{1}}=$ $\frac{u_{\mathrm{N}}-u_{\mathrm{o}}}{R_{\mathrm{f}}}$, 将 $u_{\mathrm{N}}=-\frac{u_{\mathrm{o}}}{A_{u_{\mathrm{o}}}}$ 代人得

$$
A_{u f}^{\prime}=\frac{u_{\mathrm{o}}}{u_{\mathrm{s}}}=-\frac{R_{\mathrm{f}}}{R_{\mathrm{t}}} \times \frac{A_{u 0}}{A_{u \mathrm{o}}+\left(1+\frac{R_{\mathrm{f}}}{R_{1}}\right)}
$$



【例 2.3-12】反相比例运算电路如图 2.3-31 所示, 已知 $A_{u o}=1000, R_{1}=100 \mathrm{k} \Omega, R_{\mathrm{f}}=$ $1 \mathrm{M} \Omega$ 。求运算的相对误差 $\delta$ 。

解: $A_{u 0}=1000$, 将已知数据代人表达式,得

$$
A_{u f}^{\prime}=\frac{u_{\mathrm{o}}}{u_{\mathrm{s}}}=-\frac{R_{\mathrm{f}}}{R_{\mathrm{l}}} \times \frac{A_{u \mathrm{o}}}{A_{u \mathrm{o}}+\left(1+\frac{R_{\mathrm{f}}}{R_{1}}\right)}=-\frac{1000}{100} \times \frac{1000}{1000+\left(1+\frac{1000}{100}\right)}=-9.89
$$

若 $A_{u 0}=\infty$, 则 $A_{u f}=-10$ 。所以 

$$
\delta=\frac{A_{u f}-A_{u f}^{\prime}}{A_{u f}^{\prime}}=\frac{10-9.89}{9.89} \approx 0.11 \%
$$

\section{2. 只考虑失调电压 $U_{\mathrm{io}} \neq 0$ 时产生的误差输出电压}

若放大器的失调电压不为零, 要想使输出电压等于零, 必须在其输人端施加一个与 $U_{\mathrm{io}}$ 大 小相等、极性相反的补偿电压。所以等效电路如图 2.3-32 所示。





$$
U_{\mathrm{A}}=U_{\text {io }}=\frac{R_{1}}{R_{1}+R_{\mathrm{f}}} u_{\mathrm{o}}
$$

所以由 $U_{\mathrm{io}}$ 引起的误差输出电压

$$
U_{\mathrm{or}}=U_{\mathrm{io}} \frac{R_{1}+R_{\mathrm{f}}}{R_{1}},
$$

\section{3. 只考虑输入偏置电流 $I_{\mathrm{iB}} \neq 0$ 和输入失调电流 $I_{\mathrm{i} 0} \neq 0$ 时产生的误差输出电压}

$I_{\mathrm{B}}=\left(I_{\mathrm{BN}}+I_{\mathrm{BP}}\right) / 2$, 当 $I_{\mathrm{BN}} \neq I_{\mathrm{BP}}$ 时, 使 $I_{\mathrm{io}}=\left|I_{\mathrm{BN}}-I_{\mathrm{BP}}\right| \neq 0$, 就产生了失调电流。 利用叠加原理求解:

(1)设反相输人端的 $I_{\mathrm{iB}} \neq 0$, 同相输入端的 $I_{\mathrm{iB}}=0 、 I_{\mathrm{io}}=0$ 。产生的误差输出电压

$$
U_{\text {orN }}=I_{\mathrm{iB}} R_{\mathrm{f}} \text { (因为 } U_{\mathrm{N}}=U_{\mathrm{P}}=0 \text { ) }
$$

(2)设同相输人端的 $I_{\mathrm{iB}} \neq 0 、 I_{\mathrm{io}} \neq 0$, 反相输人端的 $I_{\mathrm{iB}}=0$ 。产生的误差输出电压

$$
U_{\text {orP }}=\frac{R_{1}+R_{\mathrm{f}}}{R_{1}}\left(-I_{\mathrm{iB}}+I_{\mathrm{io}}\right) R_{2}
$$

(3)总的误差输出电压

$$
U_{\text {or }}=U_{\text {orN }}+U_{\text {orP }}=-I_{\text {iB }}\left(\frac{R_{1}+R_{\mathrm{f}}}{R_{1}} R_{2}-R_{\mathrm{f}}\right)+I_{\mathrm{io}} \frac{R_{1}+R_{\mathrm{f}}}{R_{1}} R_{2}
$$

为使两输人端的外接电阻平衡, 取 $R_{2}=R_{1} / / R_{\mathrm{f}}$, 则 $\frac{R_{1}+R_{f}}{R_{1}} R_{2}-R_{\mathrm{f}}=0$, 可以消除偏置电流 $I_{\mathrm{B}}$ 对输出电压的影响。

【例 2.3-13】电路如图 2.3-34(a) 所示, 运放器的型号为 $\mu \mathrm{A} 741$, 已知 $I_{\mathrm{iB}}=100 \mathrm{nA}, I_{\mathrm{io}}=$ $20 \mathrm{nA}, U_{\mathrm{io}}=5 \mathrm{mV}$ 。试求由 $I_{\mathrm{iB}} 、 I_{\mathrm{io}} 、 U_{\mathrm{io}}$ 产生的误差输出电压 $U_{\mathrm{or}}$ 。

解: 因为求的是误差输出电压 $U_{\mathrm{or}}$, 所以令输人电压 $u_{\mathrm{i}}=0$, 如图 (b) 所示。又 $R_{2}=R_{\mathrm{1}} / / R_{\mathrm{f}}$, 故

$$
U_{\mathrm{or}}=U_{\mathrm{io}} \frac{R_{1}+R_{\mathrm{f}}}{R_{\mathrm{1}}}+I_{\mathrm{io}} \frac{R_{1}+R_{\mathrm{f}}}{R_{\mathrm{f}}} R_{2}=\frac{R_{1}+R_{\mathrm{f}}}{R_{\mathrm{f}}} U_{\mathrm{io}}+I_{\mathrm{io}} R_{\mathrm{f}}
$$








$$
=\frac{100+1000}{100}\left(5 \times 10^{-3}\right)+20 \times 10^{-9} \times 1000 \times 10^{3}=75 \mathrm{mV}
$$

2.3.6 对数和指数运算电路工作原理, 输入输出关系

\section{1. 对数运算电路}


$$
i_{\mathrm{c}} \approx i_{\mathrm{c}} \approx I_{\mathrm{ES}} \mathrm{e}^{\frac{u_{\mathrm{BE}}}{U_{\mathrm{T}}}}, i_{\mathrm{c}}=i=u_{\mathrm{s}} / R, u_{\mathrm{o}}=-u_{\mathrm{BE}}
$$

得到输人、输出关系式为

$$
u_{\mathrm{o}}=-U_{\mathrm{T}} \ln \frac{u_{\mathrm{s}}}{R}+U_{\mathrm{T}} \ln I_{\mathrm{ES}}
$$

从图 2.3-35 可知, $\left|u_{0}\right|<0.7 \mathrm{~V}$ 。





\section{2. 指数 (反对数) 运算电路}

将对数运算电路中的三极管与 $R$ 对调就得到如图 2.3-36 所示的反对数运算电路。输人、 输出关系式为

$$
u_{\mathrm{o}}=-I_{\mathrm{ES}} R_{\mathrm{r}} \mathrm{e}^{u_{\mathrm{s}} / U_{\mathrm{T}}}
$$

\subsection{7 乘法器的应用(平方、均方根、除法)}

\section{1. 模拟乘法器工作原理}

利用对数和反对数运算电路可实现乘法运算, 其数学原理是:

$$
u_{\mathrm{o}}=\ln ^{-1}\left(\ln u_{x}+\ln u_{y}\right)=u_{x} u_{y}
$$

根据此式可得乘法器框图(图 2.3-37)。 







\section{2. 乘法器的应用}

\section{(1) 乘法运算}

乘法器能实现乘法运算。符号如图 2.3-38 所示, 输出 $u_{0}$ 与输人 $u_{x}$ 和 $u_{y}$ 的乘积成正比, 即 $u_{\mathrm{o}}=k u_{x} u_{y}$ 。

\section{(2) 平方运算}

当 $u_{x}=u_{y}=u_{\mathrm{i}}$ 时, $u_{\mathrm{o}}=k u_{\mathrm{i}}{ }^{2}$, 如图 2.3-39 所示。

(3) 除法运算


该电路要求 $u_{x}>0 \mathrm{~V}$, 以保证运放器处于负反馈工作状态。

(4) 开平方运算

电路如图 2.3-41 所示。依虚地概念有 $\frac{u_{\mathrm{s}}}{R}+\frac{u_{1}}{R}=0, u_{1}=-u_{\mathrm{s}}$, 又 $u_{1}=k u_{\mathrm{o}}^{2}$, 所以 $u_{\mathrm{o}}=$ $\sqrt{-\frac{u_{\mathrm{s}}}{k}}$ 。





该电路要求 $u_{s}$ 必须是负值。否则, 运放器通过乘法器引人的负反馈将变成正反馈。

(5) 均方根运算


$$
\begin{aligned}
& u_{\mathrm{o} 1}=k u_{\mathrm{i} 1}^{2}, u_{\mathrm{o} 2}=k u_{\mathrm{i} 2}^{2}, u_{\mathrm{o} 3}=-k\left(u_{\mathrm{i} 1}^{2}+u_{\mathrm{i} 2}^{2}\right) \\
& u_{\mathrm{o}}=\sqrt{-\frac{R_{2}}{R_{1} k}(-k)\left(u_{\mathrm{i} 1}^{2}+u_{\mathrm{i} 2}^{2}\right)}=\sqrt{\frac{R_{2}}{R_{1}}\left(u_{\mathrm{i} 1}^{2}+u_{\mathrm{i} 2}^{2}\right)}
\end{aligned}
$$





\section{4 信号处理电路}

\subsection{1 滤波器}

\section{1. 滤波器的概念、种类及幅频特性}

滤波器是一种选频电路, 其功能是使有用频率的信号通过,而将其余频率的信号加以抑制 或衰减。

滤波器分类:按信号通过的频率分为低通滤波器、高通滤波器、带通滤波器、带阻滤波器和 全通滤波器。它们的理想幅频特性如图 2.4-1 所示, $|A|$ 为传输函数的模, $A_{u p}$ 为通带电压放大 倍数。


低通滤波器


高通滤波器


带通滤波器


带阻澞波器


全通滤波器


通带截止频率: 能够通过的信号频率范围称为通带, 被衰减的信号频率范围称为阻带。通 带和阻带的界限频率称为通带截止频率, 如图 2. 4-1 中的 $\omega_{\mathrm{I}}$ 和 $\omega_{\mathrm{H}}$ 。

低通滤波器 (LPF) : 其功能是 $0 \sim \omega_{\mathrm{H}}$ 的低频信号通过, 而频率高于 $\omega_{\mathrm{H}}$ 的信号则被衰减。

高通滤波器 $(\mathrm{HPF})$ : 频率大于 $\omega_{\mathrm{L}}$ 的高频信号通过,而频率低于 $\omega_{\mathrm{L}}$ 的信号被抑制。

带通滤波器 $(\mathrm{BPF})$ : 只允许频率在 $\omega_{\mathrm{L}}<\omega<\omega_{\mathrm{H}}$ 范围内的信号通过。 $\omega_{\mathrm{L}}$ 和 $\omega_{\mathrm{H}}$ 的中点频率称 为中心角频率 $\omega_{0}$ 。主要用于从众多信号中提取有用信号。

带阻滤波器 $(\mathrm{BEF})$ : 阻止频率在 $\omega_{\mathrm{H}}<\omega<\omega_{\mathrm{L}}$ 范围内的信号通过。 $\omega_{\mathrm{L}}$ 和 $\omega_{\mathrm{H}}$ 的中点频率称为 中心角频率 $\omega_{0}$ 。主要用于抑制 $\omega_{\mathrm{H}}<\omega<\omega_{\mathrm{L}}$ 范围内的干扰信号。

全通滤波器: 又称移相滤波器, 能通过所有频率的信号, 通带放大倍数为常数, 仅相位是频 率的函数。

当前广泛使用的是由运算放大器和 $R C$ 滤波网络组成的有源滤波器。

\section{2. 低通有源滤波电路 (LPF)}

(1) 一阶低通有源滤波电路

(1)电路组成。在图 2.4-2 中, $R 、 C$ 为无源低通滤波环节, 其后接一个同相比例放大电路。 (2)通带电压放大倍数 $A_{\text {up }} \circ \omega=0$ (或 $f=0$ ) 时, $u_{\mathrm{o}}$ 与 $u_{\mathrm{i}}$ 的比值, $A_{\text {up }}=1+\frac{R_{\mathrm{f}}}{R_{1}}$ 。

(3)传递函数。利用虚短和虚断, 该电路的传递函数为 $A(s)=\frac{U_{\mathrm{o}}(s)}{U_{\mathrm{i}}(s)}=\frac{A_{\text {up }}}{1+s R C}$, 其中分母为 $s$ 的一次幂,所以称为一阶低通有源滤波电路。

(4)通带截止频率。将传递函数中的 $s$ 用实际频率 $\mathrm{j} \omega$ 代替,则得频率特性为

$$
A(\mathrm{j} \omega)=\frac{U_{\mathrm{o}}(\mathrm{j} \omega)}{U_{\mathrm{i}}(\mathrm{j} \omega)}=\frac{A_{u \mathrm{p}}}{1+\mathrm{j}\left(\frac{\omega}{\omega_{n}}\right)}=\frac{A_{u \mathrm{p}}}{1+\mathrm{j}\left(\frac{f}{f_{n}}\right)}
$$

其中 $\omega_{n}=1 /(R C)$ 称为特征角频率, $f_{n}=1 /(2 \pi R C)$ 称为特征频率, 二者与 $R 、 C$ 的参数有关。 当 $\omega=\omega_{\mathrm{H}}=\omega_{n}$ 时, $|A|=\frac{A_{\text {up }}}{\sqrt{2}}=0.707 A_{\text {up }}$, 因此通带截止角频率 $\omega_{\mathrm{H}}=1 /(R C)$, 通带截止频率 $f_{\mathrm{H}}$ $=1 /(2 \pi R C)$ 。







(5)主要性能。对数频率特性如图 2. 4-3 所示。当 $\omega>\omega_{\mathrm{n}}$ 时, 仅以 $-20 \mathrm{~dB} /$ 十倍频程衰减, 与理想情况相 差较大。

(2) 二阶低通有源滤波电路

在图 2.4-2 的基础上再加一级 $R C$ 低通滤波电路 就得到二阶低通有源滤波电路, 如图 2.4-4 所示。图 中第一级的 $C$ 没有直接接地, 而是接到输出端, 引进适 度的正反馈, 以使频率特性更接近理想特性。

(1) 通带电压放大倍数 $A_{u \mathrm{p}}=1+\left(R_{\mathrm{f}} / R_{1}\right)$ 。

(2)传递函数 $A(s)=\frac{U_{\mathrm{o}}(s)}{U_{\mathrm{i}}(s)}=\frac{A_{u p}}{1-\left(3-A_{u \mathrm{p}}\right) s C R+(s C R)^{2}}=\frac{A_{u p} \omega_{n}^{2}}{s^{2}+\frac{\omega_{n}}{Q} s+\omega_{n}^{2}}$

传递函数的分母中有 $s^{2}$ 项, 可见该电路是一个二阶低通滤波电路。

(3)通带截止频率 $f_{\mathrm{H}}=f_{n}=1 /(2 \pi R C)$ 。特征频率 $\omega_{n}=1 /(R C)$ 。

(4) 性能。当 $\omega>\omega_{n}$ 时, 以 $-40 \mathrm{~dB} /$ 十倍频程衰减, 较一阶电路加快一倍。品质因数 $Q=$ $1 /\left(3-A_{u \mathrm{p}}\right)$, 表明该电路只有 $A_{u \mathrm{p}}=1+\left(R_{\mathrm{f}} / R_{\mathrm{f}}\right)<3$ 时, 才能稳定工作。当 $A_{u \mathrm{p}}=1+\left(R_{\mathrm{f}} / R_{\mathrm{f}}\right)=$ 3 时, $Q \rightarrow \infty$, 电路产生自激振荡。 

\section{3. 高通与低通滤波电路的对偶关系、特性及带通滤波电路的组成}

(1) 一阶高通、低通滤波电路的对偶关系


(1)电路结构的对偶性: 将低通滤波电路中的 $R 、 C$ 位置对换, 就组成了高通滤波电路。

(2)传递函数的对偶性: 将低通滤波电路传递函数分母中的 $s R C$ 换成 $\frac{1}{s R C}$, 就可得到高通滤 波电路的传递函数 $A(s)_{\mathrm{H}}=\frac{U_{\mathrm{o}}(s)}{U_{\mathrm{i}}(s)}=\frac{A_{u \mathrm{p}} 1}{1+\frac{1}{s R C}}=\frac{s R C}{1+s R C} A_{\text {up }}$

(3)频率特性的对偶性:二者成“镜像”关系。


(2) 二阶高通、低通滤波电路的对偶关系

将二阶低通滤波电路中的 $R 、 C$ 互换就组成二阶高通滤波电路,如图 2.4-6 所示。






\section{(3) 带通滤波电路的组成}

低通与高通滤波电路相串联可组成带通滤波电路 (BPF), 如图 2.4-7 所示。条件是低通 的截止角频率 $\omega_{\mathrm{H}}$ 大于高通的截止角频率 $\omega_{\mathrm{L}}$, 通频带为 $\omega_{\mathrm{H}}-\omega_{\mathrm{L}}$ 。

按该方法将二阶低通滤波电路的其中一级接成高通滤波电路, 就组成了二阶带通滤波电 路,如图 2. 4-8 所示。其中 $R_{3}$ 引进适度正反馈,仍然为改善频率特性。

\section{【例 2.4-1】选择正确的滤波器类型填空。}

(1) 有用信号频率为 $7 \mathrm{~Hz}$

(2) 有用信号频率低于 $500 \mathrm{~Hz}$

(3) 希望抑制 $50 \mathrm{~Hz}$ 交流电源的干扰

(4) 希望抑制 $1 \mathrm{kHz}$ 以下的信号
(A) 低通
(B) 高通
(C) 带通
(D) 带阻 




解: (1) (C), (2) (A), (3) (D), (4) (B)。

【例 2.4-2】电路如图 2.4-9 所示, 已知 $R=10 \mathrm{k} \Omega, C=0.001 \mu \mathrm{F}, R_{\mathrm{f}}=20 \mathrm{k} \Omega$ 。设运放器 是理想的。试问:

(1) 是什么类型的滤波器;

(2) 写出推导传递函数;

(3) 求通带截止频率。

解: (1) 有源低通滤波电路。

(2) 传递函数

$$
A(s)=\frac{U_{0}(s)}{U_{\mathrm{i}}(s)}=\frac{1}{1+s R C}
$$



(3) 通带截止频率

$$
f_{\mathrm{H}}=\frac{1}{2 \pi R C} \approx 15.9 \mathrm{kHz}
$$

\subsection{2 比较器}

\section{1. 单门限电压比较器}

（1）基本电路

比较器是用来比较输人电压 $u_{\mathrm{i}}$ 与参考电压 $U_{\mathrm{REF}}$ 大小的电路。运放器工作在非线性区, 其 输出电压只有两个值:一个为正饱和值 $U_{\mathrm{oH}}$ (或正最大值 $+U_{\mathrm{om}}$ ), 一个为负饱和值 $U_{\mathrm{oL}}$ (或负最 大值 $-U_{\mathrm{om}}$ )。当 $u_{\mathrm{i}}$ 经过 $U_{\mathrm{REF}}$ 时, 输出电压就从一个饱和值跳到另一个饱和值。


若 $U_{\mathrm{REF}}=0$, 则称为过零比较器。

(2) 阈值

输出电压 $u_{\mathrm{o}}$ 从一个极性的饱和值跳到另一个极性的饱和值所对应的输人电压 $u_{\mathrm{i}}$ 的大小 称为门限电压或阈值电压 $U_{\text {tho }}$ 。

【例 2. 4-3】电路如图 2. 4-12 所示, 运放器为理想的, $U_{\mathrm{oH}}=12 \mathrm{~V}, U_{\mathrm{oL}}=-12 \mathrm{~V}$, 输人电压 $u_{\mathrm{i}}=2 \sin \omega t \mathrm{~V}$ 。试对应画出 $u_{0}$ 的波形。 



解: 本电路是一个反相输人的过零比较器, $u_{\mathrm{o}}$ 的波形如图 2.4-13 所示。





\section{2. 迟滞比较器}


$$
U_{\mathrm{th}+}=\frac{R_{3}}{R_{2}+R_{3}} U_{\mathrm{REF}}+\frac{R_{2}}{R_{2}+R_{3}} U_{\mathrm{oH}}, U_{\mathrm{th}-}=\frac{R_{3}}{R_{2}+R_{3}} U_{\mathrm{REF}}+\frac{R_{2}}{R_{2}+R_{3}} U_{\mathrm{oL}}
$$






传输特性如图 2.4-14(b) 所示。

2.4.3 检波器和采样保持电路的工作原理

\section{1. 检波器工作原理}

检波器又称为线性整流电路, 可有效地克服二极管的门坎电压和非线性对检波性能的影 响。






\section{2. 采样保持电路的工作原理}

采样保持电路由模拟开关、存储电容和缓冲放大器三部分组成, 模拟开关采用场效应管, 缓冲放大器使用集成运放器, 电路如图 2.4-17 所示。工作过程分为采样和保持两个周期, 由 CTRL 端的控制信号控制。当控制信号为低电平时, $T$ 导通, 开始采样, $C$ 上的电压跟踪输人信 号, 经由缓冲放大器 (电压跟随器) 到 $u_{\mathrm{o}}$ 。所以输出信号跟踪输人信号的变化, 这是采样周期。 当控制信号为高电平时, $\mathrm{T}$ 截止, 存储电容 $C$ 将 $\mathrm{T}$ 截止时刻的输人信号保存下来, 并送到 $u_{0}$, 为 保持周期,直到下一个采样开始。

【例 2. 4-4】电路图和输出波形、控制信号分别如图 2. 4-17 和图 2.4-18 所示, 试画出 $u_{0}$ 的波形。

解: $\mathrm{S}$ 表示采样周期, $\mathrm{H}$ 表示保持周期。输出波形如图中“粗线”所示。





\section{5 信号发生电路}

2.5.1 产生正弦波自激振荡的条件

\section{1. 相位平衡条件}

$\varphi_{A}+\varphi_{F}=2 n \pi(n=0,1,2, \cdots)$, 相位平衡条件就是保证正反馈。

\section{2. 振幅平衡条件}

$|\dot{A} \vec{F}|=1$, 就是保证维持振荡。在满足相位平衡条件下, $|\dot{A F}|>1$ 是起振条件, $|\dot{A} \dot{F}|=1$ 是 等幅振荡。 

\subsection{2 $R C$ 文氏电桥正弦波振荡电路}

\section{1. 组成}

$R C$ 文氏电桥正弦波振荡电路由 $R C$ 串并联选频网络和电压放大电路两部分组成 (图 2.51)。 $R C$ 串并联网络既是选频网络, 又是正反馈网络。 $R_{\mathrm{f}}$ 和 $R_{\mathrm{t}}$ 构成负反馈, 用来改善输出波形 和稳定振荡幅度。





\section{2. $R C$ 串并联网络的选频特性}

$R C$ 串并联选频网络如图 2.5-2 所示,其选频特性为

$$
F_{u}=\frac{U_{\mathrm{f}}}{U_{\mathrm{o}}}=\frac{R / / \frac{1}{\mathrm{j} \omega C}}{R+\frac{1}{\mathrm{j} \omega C}+R / / \frac{1}{\mathrm{j} \omega C}}=\frac{1}{3+\mathrm{j}\left(\frac{\omega}{\omega_{0}}-\frac{\omega_{0}}{\omega}\right)}
$$

式中 $\omega_{0}=1 / R C$, 为选频网络的谐振角频率。当 $\omega=\omega_{0}=\frac{1}{R C}$ 或 $f=f_{0}=\frac{1}{2 \pi R C}$ 谐振时, $F_{u}$ 的最大 愊值 $\left|F_{u \max }\right|=\frac{1}{3}, F_{u}$ 的相角 $\varphi_{F}=0^{\circ}$ 。

\section{3. 振荡频率}

振荡频率 $f_{0}=1 /(2 \pi R C)$

\section{4. 相位和振幅平衡条件}

\section{(1) 相位条件}

放大器为同相放大电路, 相移 $\varphi_{A}=0^{\circ}$; 在振荡频率 $f_{0}=1 /(2 \pi R C)$ 时, 选频网络的相移 $\varphi_{F}$ $=0^{\circ}$, 满足相位条件。

\section{(2) 振幅条件}

为能起振, 应满足起振条件 $F_{u \max } A_{u \mathrm{f}}>1$, 即 $A_{u \mathrm{f}}>3$ 又 $A_{u \mathrm{f}} \approx 1+\left(R_{\mathrm{f}} / R_{1}\right)$, 所以起振条件应满 足 $R_{\mathrm{f}}>2 R_{1}$ 。

等幅振荡条件: $F_{u \max } A_{u \mathrm{f}}=1, A_{\mathrm{uf}}=3, R_{\mathrm{f}}=2 R_{1}$ 。

\section{5. 稳幅措施}

稳定输出电压幅度就是维持 $F_{u \max } A_{u \mathrm{f}}=1$ 。若起振后仍是 $F_{u \max } A_{u \mathrm{f}}>1$, 输出波形将产生失 真。稳幅的措施是在负反馈回路中采用非线性元件, 如用一个负温度系数的热敏电阻代替 $R_{\mathrm{i}}$, 或用正温度系数的热敏电阻代替 $R_{1}$ 。随着输出电压幅度的加大, 反馈量也随之加大, 使 $F_{\text {max }} A_{u f}$ 接近于 1 , 维持稳定的正弦输出。 



【例 2.5-1】电路如图 2.5-3 所示, 运放器为理想的, $R=1$ $\mathrm{k} \Omega, C=0.01 \mu \mathrm{F}$, 试求:

(1) 振荡频率 $f_{0}$;

(2) 若 $R_{1}=2 \mathrm{k} \Omega, R_{\mathrm{f}}$ 的最小值。

解: (1) 振荡频率

$$
f_{0}=\frac{1}{2 \pi R C}=\frac{1}{6.28 \times 1 \times 10^{3} \times 0.01 \times 10^{-6}} \approx 15.9 \mathrm{kHz}
$$

(2) $R_{\mathrm{f}} \geqslant 2 R_{1} \geqslant 2 \times 2 \mathrm{k} \Omega$, 取 $R_{\mathrm{f} \text { in }}=4.3 \mathrm{k} \Omega$ 。

\subsection{3 $L C$ 正弦波振荡器}

\section{1. 变压器反馈式}

电路如图 2.5-4 所示, $L_{1} C_{1}$ 并联电路为选频网络, 反馈由变压器绕组 $L_{2}$ 实现。

判断相位平衡条件: $L_{2}$ 一端接地, 另一端接输人 (基极) 为反馈元件。谐振时 $L_{1} C_{1}$ 并联回 路为纯电阻性质, 用瞬时极性法判断可知 $L_{2}$ 引人的是正反馈, 满足相位平衡条件。







\section{2. 电感三点式 (电感反馈式)}

电路如图 2. 5-5 所示, $L_{2}$ 接在基极和发射极之间 (交流通路),所以是反馈元件。 $L C$ 并联 谐振回路谐振时近似为纯电阻, 用瞬时极性法判断可知是正反馈, 满足相位平衡条件。

\section{3. 电容三点式 (电容反馈式)}

电路如图 2.5-6 所示, $C_{1} 、 C_{2}$ 和 $L$ 组成谐振回路, 反馈元件是 $C_{2}$, 引人的是正反馈。

【例 2.5-2】 用相位平衡条件判断图 2.5-7 中哪个可能产生正弦波振荡。

解: 图 (a) 满足相位平衡条件, 可能振荡, 为电容三点式电路。图 (b) 不满足相位平衡条 件, 不可能振荡。图 (c) 满足相位平衡条件, 可能振荡, 为电感三点式电路。

\subsection{4 石英晶体振荡电路}

\section{1. 石英晶体的等效电路与电抗特性}


串联谐振频率 $f_{\mathrm{s}}=\frac{1}{2 \pi \sqrt{L C}}$ 








并联谐振频率 $f_{\mathrm{p}}=\frac{1}{2 \pi \sqrt{L \frac{C C_{0}}{C+C_{0}}}}=f_{\mathrm{s}} \sqrt{1+\frac{C}{C_{0}}}$







因为 $C_{0} \gg C$, 所以 $f_{\mathrm{s}}$ 与 $f_{\mathrm{p}}$ 很接近。

\section{2. 石英晶体振荡电路}

(1) 并联型振荡电路 (图 2.5-9)

石英晶体谐振频率 $f_{\mathrm{s}}<f_{0}<f_{\mathrm{p}}$, 石英晶体为大电感, 组成电容三点式振荡电路。

(2) 串联型振荡电路 (图 2.5-10)

石英晶体工作在 $f=f_{\mathrm{s}}$ 处, 振荡频率 $f_{0}=f_{\mathrm{s}}$ 时, 晶体阻抗最小, 并且为纯电阻性质, 相移为 零, 此时电路的正反馈最强。







【例 2.5-3】图 2.5-11 是一个正弦波振荡器,试问石英晶体 的工作频率为
(A) $f$ s
(B) $f_{\mathrm{p}}$
(C) $<f_{\mathrm{s}}$
(D) $>f_{\mathrm{p}}$

解: 答案为 $(A)$ 。晶体串联谐振时, 呈纯电阻性, 并且阻值极 低, 没有相移, 所以正反馈最强。故石英晶体的工作频率应为串 联谐振频率 $f_{\mathrm{s}}$ 。

\subsection{5 各种正弦波振荡器的使用场合}

各种正弦波振荡器的使用场合主要根据工作频率范围、波形

好坏和稳定性选择。

\begin{tabular}{c|c|c|c|c}
\hline 振荡电路类型 & 频率范围 & 频率稳定度 & 波形质量 & 频率调节 \\
\hline$R C$ 文氏电桥 & 几 $\mathrm{Hz} \sim$ 几百 $\mathrm{kHz}$ & $10^{-2} \sim 10^{-4}$ & 好 & 方便,范围宽 \\
\hline 变压器反馈式 & 几百 $\mathrm{kHz} \sim$ 几 MHz & $10^{-2} \sim 10^{-4}$ & 差 & 方便, 范围宽 \\
\hline 电感三点式 & 几百 $\mathrm{kHz} \sim$ 十几 MHz & $10^{-2} \sim 10^{-4}$ & 差 & 方便,范围宽 \\
\hline 电容三点式 & 几 $\mathrm{MHz} \sim$ 几十 $\mathrm{MHz}$ & $10^{-2} \sim 10^{-4}$ & 较好 & 不方便, 范围套 \\
\hline 石英晶体 & 几 $\mathrm{kHz} \sim$ 十几 $\mathrm{MHz}$ & $10^{-5} \sim 10^{-8}$ & 好 & 微调 \\
\hline
\end{tabular}

\section{5 .6 方波、三角波、锯齿波发生电路}

\section{1. 方波发生器}

方波发生器如图 2.5-12(a) 所示, 由迟滞比较器和 $R C$ 积分电路组成。阈值为






$$
U_{\mathrm{th}+}=+\frac{R_{2}}{R_{1}+R_{2}} U_{\mathrm{z}}, U_{\mathrm{th}-}=-\frac{R_{2}}{R_{1}+R_{2}} U_{\mathrm{z}}
$$

当 $C$ 充电到 $U_{\mathrm{th}+}$ 时, 输出跳变为 $-U_{\mathrm{z}}$ 。而后 $C$ 反向充电, 到 $U_{\mathrm{th}-}$ 时, 输出又跳变为 $+U_{\mathrm{z}}$ 。 如此反复输出电压 $u_{\mathrm{o}}$ 为方波 (图 (b))。 $u_{C}$ 为 $C$ 的充放电波形。

振荡周期

$$
T=2 R_{\mathrm{f}} C \ln \left(1+\frac{2 R_{2}}{R_{1}}\right)
$$

【例 2.5-4】在图 2.5-12(a)中,已知 $R_{\mathrm{f}}=51 \mathrm{k} \Omega, R_{1}=500 \mathrm{k} \Omega, R_{2}=1 \mathrm{M} \Omega, C=0.01 \mu \mathrm{F}, U_{\mathrm{z}}$ $=6 \mathrm{~V}$ 。设运算放大器为理想的, 试求:

(1) 画出 $u_{\mathrm{o}}$ 和 $u_{C}$ 的波形;

(2) 方波的周期 $T_{\text {。 }}$

解: (1) $u_{\mathrm{o}}$ 和 $u_{C}$ 的波形如图 2. 5-13 所示。

(2) 方波的周期

$$
T=2 R_{\mathrm{f}} C \ln \left(1+\frac{2 R_{2}}{R_{1}}\right)=1.02 \times 10^{-3} \ln 5=1.64 \mathrm{~ms}
$$

\section{2. 三角波发生器}




振荡周期

$$
T=\frac{4 R C R_{2}}{R_{1}}
$$






\section{3. 锯齿波发生器}







迟滞比较器的阈值

$$
U_{\mathrm{T}+}=\left(R_{1} / R_{2}\right) U_{\mathrm{Z}}, U_{\mathrm{T}-}=-\left(R_{1} / R_{2}\right) U_{\mathrm{Z}}
$$

振荡周期 

$$
T=T_{1}+T_{2}=\frac{2 R_{1} R_{6} C\left(R_{6}+2 R_{5}\right)}{R_{2}\left(R_{5}+R_{6}\right)}
$$

\subsection{7 压控振荡器}

振荡频率受外加电压控制的振荡器称为压控振荡器。

\section{1. 输入、输出关系}

\begin{tabular}{c|c}
\hline 控制电压类型 & 输出电压类型 \\
\hline 直流电压 & 频率可调的信号源 \\
\hline 正弦电压 & 调频振荡器,输出调频波 \\
\hline 方波 & 双频振落器,能交替输出两种频率的波形 \\
\hline 锯毕波 & 当频振荡器,输出扫频波 \\
\hline
\end{tabular}

\section{2. 电路组成及工作原理}


$\mathrm{A}_{3}$ 与 $\mathrm{A}_{4}$ 电路结构相同, 又相互串联, 所以 $u_{03}$ 和 $u_{\mathrm{o} 4}$ 大小相等, 方向相反。迟滞比较器 $\mathrm{A}_{2}$ 的上、下门限也是大小相等, 方向相反。 $u_{\mathrm{o} 1}$ 为三角波, $u_{\mathrm{o} 2}$ 为方波。



\section{3. 振荡频率}

$$
f_{0}=\frac{R_{1} U_{\mathrm{i}}}{4 R C R_{2} U_{\mathrm{z}}}
$$

\section{6 功率放大电路}

2.6. 1 功率放大电路的特点及互补推挽功率放大电路

\section{1. 特点}

(1)输出功率尽可能大。

(2)效率要高。 (3)尽可能减小非线性失真。

(4)要考虑散热和过载保护。

\section{2. 乙类双电源互补推挽功率放大电路}


\section{(1) 工作原理}

(1)静态。 $u_{\mathrm{i}}=0$ 时, 两个管子均不导通, $R_{\mathrm{t}}$ 上无电流, $u_{\mathrm{o}}=0$, 电路无 静态功耗。

(2)动态。在正弦信号 $u_{\mathrm{i}}$ 的正半周, $\mathrm{T}_{1}$ 导通, $\mathrm{T}_{2}$ 截止, $\mathrm{T}_{1}$ 和 $R_{\mathrm{L}}$ 工作在



(2) 计算公式

(1) 输出功率 $P_{0}$ : 输出功率 $P_{\mathrm{o}}=$ 输出电压有效值 $U_{\mathrm{o}} \times$ 输出电流有效值 $I_{\mathrm{o}}$ 。

$$
P_{\mathrm{o}}=U_{\mathrm{o}} I_{\mathrm{o}}=\frac{U_{\mathrm{om}}}{\sqrt{2}} \times \frac{U_{\mathrm{om}}}{\sqrt{2} R_{\mathrm{L}}}=\frac{1}{2} \times \frac{U_{\mathrm{om}}^{2}}{R_{\mathrm{L}}}\left(U_{\mathrm{om}} \text { 为输出电压峰值 }\right)
$$

最大输出功率 $P_{\mathrm{om}}$ : 当 $u_{\mathrm{i}}$ 足够大时, $U_{\mathrm{om}}=U_{\mathrm{cc}}-U_{\mathrm{cES}} \approx U_{\mathrm{cC}}$, 则

$$
P_{\mathrm{om}}=\frac{1}{2} \times \frac{\left(U_{\mathrm{CC}}-U_{\mathrm{CES}}\right)^{2}}{R_{\mathrm{L}}} \approx \frac{1}{2} \times \frac{U_{\mathrm{CC}}^{2}}{R_{\mathrm{L}}}
$$

(2) 两管总管耗

$$
P_{\mathrm{T}}=P_{\mathrm{T} 1}+P_{\mathrm{T} 2}=\frac{2}{R_{\mathrm{L}}}\left(\frac{U_{\mathrm{cC}} U_{\mathrm{om}}}{\pi}-\frac{U_{\mathrm{om}}^{2}}{4}\right)
$$

每管管耗

$$
P_{\mathrm{T} 1}=P_{\mathrm{T} 2}=\frac{1}{R_{\mathrm{L}}}\left(\frac{U_{\mathrm{CC}} U_{\mathrm{om}}}{\pi}-\frac{U_{\mathrm{om}}^{2}}{4}\right)
$$

当 $U_{\mathrm{om}}=\frac{2}{\pi} U_{\mathrm{CC}}$ 时,管耗最大。最大管耗

$$
P_{\mathrm{Tlm}}=P_{\mathrm{T} 2 \mathrm{~m}}=\frac{1}{\pi^{2}} \times \frac{U_{\mathrm{CC}}^{2}}{R_{\mathrm{L}}}
$$

(3) 单管最大管耗 $P_{\mathrm{Tl} \mathrm{m}}$ 与最大输出功率 $P_{\mathrm{om}}$ 之间的关系:

$$
P_{\mathrm{T} 1 \mathrm{~m}} \approx 0.2 P_{\mathrm{om}}
$$

(4) 直流电源供给的功率

$$
P_{U}=P_{\mathrm{o}}+P_{\mathrm{T}}=\frac{2}{\pi} \times \frac{U_{\mathrm{CC}} U_{\mathrm{om}}}{R_{\mathrm{L}}}
$$

电源供给的最大功率

$$
P_{U \mathrm{~m}}=\frac{2}{\pi} \times \frac{U_{\mathrm{CC}}^{2}}{R_{\mathrm{L}}}
$$

(5) 能量转换效率

$$
\eta=\frac{P_{\mathrm{o}}}{P_{U}}=\frac{\pi}{4} \times \frac{U_{\mathrm{om}}}{U_{\mathrm{cc}}}
$$

最大效率

$$
\eta_{\mathrm{m}}=\frac{\pi}{4} \times \frac{U_{\mathrm{CC}}}{U_{\mathrm{CC}}}=\frac{\pi}{4} \approx 78.5 \%
$$

注意:

(1) 以上计算公式对所有互补推挽功率放大电路均适用。当单电源供电时, 只将公式中 $U_{\mathrm{cC}}$ 换成 $\frac{1}{2} U_{\mathrm{cc}}$ 即可。

(2) $P_{\mathrm{o}}$ 与 $P_{\mathrm{om}}, P_{\mathrm{T}}$ 与 $P_{\mathrm{Tl} \mathrm{m}}, P_{U}$ 与 $P_{U \mathrm{~m}}, \eta$ 与 $\eta_{\mathrm{m}}$ 之间的差别是: 前者用的输出电压的幅值 $U_{\mathrm{om}}<$ $U_{\mathrm{cC}}$, 后者用的是最大不失真的输出电压幅值 $U_{\mathrm{om}}=U_{\mathrm{CC}}-U_{\mathrm{eEs}} \approx U_{\mathrm{cC}}$ 。

【例 2.6-1】如图 2.6-1 所示的互补推挽功率放大电路中, 输人为正弦信号, 功放管的饱 和压降忽略不计,在输出不失真情况下,最大管耗在 出现。
(A) 输出功率约为最大不失真输出功率的 0.4 倍时
(B) 输出功率为最大时
(C) 效率最大时
(D) 输出幅度为 $U_{\mathrm{CC}}$ 时

解:答案为 $(\mathrm{A})$ 。

因为 $P_{\mathrm{o}}=\frac{U_{\mathrm{om}}^{2}}{2 R_{\mathrm{L}}}, P_{\mathrm{om}}=\frac{U_{\mathrm{CC}}^{2}}{2 R_{\mathrm{L}}}$, 又当 $U_{\mathrm{om}}=\frac{2 U_{\mathrm{CC}}}{\pi}$ 时, 管耗最大。所以

$$
\frac{P_{\mathrm{o}}}{P_{\mathrm{om}}}=\frac{U_{\mathrm{om}}^{2}}{U_{\mathrm{CC}}^{2}}=\frac{\left(\frac{2}{\pi} U_{\mathrm{CC}}\right)^{2}}{U_{\mathrm{CC}}^{2}}=\left(\frac{2}{\pi}\right)^{2} \approx 0.4
$$

\section{3. 甲乙类互补推挽功率放大电路}

(1) 双电源供电

对于图 2. 6-1 所示的乙类互补推挽功率放大电路, 由于晶体管输人特性的非线性, 有门坎 电压 $U_{\mathrm{th}} \approx 0.6 \mathrm{~V}$ (硅管) 或 $0.2 \mathrm{~V}$ (锗管)。当 $u_{\mathrm{i}}<U_{\mathrm{th}}$ 时, 晶体管不导通。实际输出波形如图 2. 6-2 所示, 在输人波形穿越零点附近产生了失真, 这种失真称为交越失真。解决的办法是给 两个功放管加上偏压, 使它们处于微导通状态, 即使功放管处于甲乙类工作状态。






单电源供电的互补对称电路又称为 OTL( Output Transformerless, 无输出变压器) 电路。图 2.6-4 只有 $+U_{\mathrm{CC}}$ 供电, 为单电源供电方式。输出端的电容 $C$ 起着 $-U_{\mathrm{Cc}}$ 的作用, 静态时, 其上 电压 $U_{C}=\frac{1}{2} U_{\mathrm{cC}}$ 。所以单电源电路的输出端必须接人大电容 $C$,其后再接负载。

单电源供电的电路, 功放管的工作电压不是 $U_{\mathrm{CC}}$ 而是 $U_{\mathrm{CC}} / 2$, 输出电压的最大值 $U_{\mathrm{om}}$ 也只能 是 $U_{\mathrm{Cc}} / 2$, 所以在乙类双电源电路中 $P_{\mathrm{o}} 、 P_{\mathrm{T}} 、 P_{U} 、 \eta$ 等, 只要用 $U_{\mathrm{cc}} / 2$ 替换公式中的 $U_{\mathrm{cc}}$ 即可用于 单电源供电的电路。





【例 2.6-2】如图 2.6-5 所示单电源甲乙类互补推挽功率放大电路。已知 $U_{\mathrm{CC}}=24 \mathrm{~V}, R_{\mathrm{L}}$. $=16 \Omega, C_{2}$ 足够大。试问:

(1) 静态时 $C_{2}$ 上的电压应为多少? 调整哪个电阻能满足此要求?

(2) 如果输出出现交越失真, 应调整哪个电阻,如何调整?

(3) 设功放管的饱和压降 $U_{\mathrm{CES}}=1 \mathrm{~V}$, 求负载 $R_{\mathrm{L}}$ 上得到的最大功率 $P_{\mathrm{om}}$ 。

解: 该电路是一个单电源互补推挽功率放大电路, 计算公式中, 要将双电源电路公式中的 $U_{\mathrm{cC}}$ 用 $U_{\mathrm{CC}} / 2$ 代人。

(1) $C_{2}$ 上的电压应等于 $12 \mathrm{~V}$ 。调整 $R_{\mathrm{b} 1}$ 或 $R_{\mathrm{b} 2}$ 即可达到此数值。

(2) 增大电阻 $R$ 。

(3) $P_{\mathrm{om}}=\frac{1}{2} \times \frac{\left(\frac{U_{\mathrm{CC}}}{2}-U_{\mathrm{CES}}\right)^{2}}{R_{\mathrm{L}}}=\frac{1}{2} \times \frac{121}{16} \approx 3.78 \mathrm{~W}$

2.6.2 集成功率放大电路的内部组成


\section{1. 主要组成部分}

(1) 差动输入级

由 $\mathrm{T}_{1} 、 \mathrm{~T}_{2}$ 组成长尾式 (即带 $R_{\mathrm{e}}$ 的) 差动放大电路, 1 端为同相输人端, 2 端为反相输人端, 3 端为输出端。

(2) 中间电压放大级

由 $\mathrm{T}_{4} 、 \mathrm{~T}_{5}$ 组成。 $\mathrm{T}_{4}$ 的射极和基极分别接在 $\mathrm{T}_{1} 、 \mathrm{~T}_{2}$ 的集电极, 使差动放大电路双端输出, 比 



单端输出的电压放大倍数增加一倍。 $\mathrm{T}_{4}$ 又把差动放大电路的双端输出转换成单端输出, 从集 电极送给 $\mathrm{T}_{5}$ 。 $\mathrm{T}_{5}$ 是输出级的前置放大级, 驱动推挽输出级。 $\mathrm{T}_{3}$ 接成二极管, 为 $\mathrm{T}_{4}$ 提供偏置电 压。若无 $T_{3}$, 因为静态时 $T_{1} 、 T_{2}$ 的集电极电位相等, $U_{\mathrm{BE} 4}=0, T_{4}$ 不能正常工作。

(3) 互补推挽功率放大输出级

由 $T_{9} \sim T_{13}$ 组成。 $T_{9} 、 T_{10}$ 组成的复合管等效为 NPN 管, $T_{11} \sim T_{13}$ 组成的复合管等效为 PNP 管。 $T_{6} 、 T_{7} 、 T_{8}$ 三个发射结的电压供给 $T_{9} 、 T_{10} 、 T_{11}$ 三个发射结的偏置电压, 使它们处于微导通状 态,用来克服交越失真。

\section{2. 稳定静态工作点的措施}

从 $\mathrm{K}$ 点通过 $R_{6}$ 到 $\mathrm{T}_{2}$ 的基极引人电压负反馈, 以稳定静态工作点。调整 $R_{6}$ 可使 $\mathrm{K}$ 点电位 $U_{\mathrm{K}}=\frac{1}{2} U_{\mathrm{cc}}$ 。

\subsection{3 自举电路及功率放大管}

\section{1. 自举电路一一提高正向输出电压幅度}


加人 $R_{2} 、 C_{2}$ 自举环节后, 静态时, $C_{2}$ 上的电压被充电到 $U_{C}=U_{\mathrm{cC}} / 2$ 。由于 $C_{2}$ 数值较大, 动 态时可认为 $U_{C}=U_{\mathrm{CC}} / 2$ 不变, 所以 $\mathrm{A}$ 点电位 $U_{\mathrm{A}}$ 始终比 $\mathrm{K}$ 点高。这样, 在 $u_{\mathrm{i}}$ 为负时, $\mathrm{T}_{1}$ 导通, $U_{\mathrm{K}}$ 在 $U_{\mathrm{cC}} / 2$ 的基础上升高。于是 $U_{\mathrm{A}}>U_{\mathrm{cC}}$, 保证 $\mathrm{T}_{1}$ 能达到饱和状态, 提高正向输出电压幅度, 也 即提高了最大不失真输出电压的幅度。

\section{2. 功率放大管}

\section{(1) 工作状态}

(1)甲类。如图 2.6-8 所示, 静态工作点 $Q_{1}$ 位于负载线中间附近。功放管在一个周期内均 有电流流过。优点是不失真, 缺点是静态损耗大, 效率低。主要用于电压放大。 





(2)甲乙类。静态工作点 $Q_{2}$ 靠近横轴。 $\pi<$ 功放管导通角度 $<2 \pi$ 。

(3)乙类。静态工作点 $Q_{3}$ 在横轴上。功放管只在半个周期导电, $0^{\circ}<$ 功放管导通角度 $<\pi 。$ 甲乙类和乙类工作状态用于功率放大电路。静态损耗小, 效率高, 但失真严重。

甲类、乙类、甲乙类功率放大电路就是根据功率放大管的工作状态划分的。

(2) 功率放大管的选择

(1) 最大允许管耗 $P_{\mathrm{CM}}>P_{\mathrm{T} 1 \mathrm{~m}} \approx 0.2 P_{\mathrm{om}}$ 。

(2) 集电极最大允许电流 $I_{\mathrm{CM}}>U_{\mathrm{CC}} / R_{\mathrm{L}}$ 。

(3) 反向击穿电压 $U_{(\mathrm{BR}) \mathrm{CEO}}>2 U_{\mathrm{CC}}$ (双电源) 或 $U_{(\mathrm{BR}) \mathrm{CEO}}>U_{\mathrm{CC}}$ (单电源)。

【例 2.6-3】电路如图 2. 6-1 所示, 已知输人电压 $u_{\mathrm{i}}$ 为正弦信号, $U_{\mathrm{CC}}=20 \mathrm{~V}, R_{\mathrm{L}}=8 \Omega$, 忽 略功放管的饱和压降 $U_{\mathrm{CES}}$, 要求最大输出功率 $P_{\mathrm{om}}=25 \mathrm{~W}$ 。试计算所选功放管的集电极最大 允许功率损耗 $P_{\mathrm{CM}}$ 、集电极最大允许电流 $I_{\mathrm{CM}}$ 和反向击穿电压 $U_{(\mathrm{BR}) \mathrm{CEO} O}$ 的最小值。

解: 每个管子的集电极最大允许功率损耗

$$
P_{\mathrm{CM}} \geqslant 0.2 P_{\mathrm{om}}=0.2 \times 25=5 \mathrm{~W}
$$

集电极最大允许电流

$$
I_{\mathrm{CM}} \geqslant U_{\mathrm{CC}} / R_{\mathrm{L}}=20 / 8=2.5 \mathrm{~A} \text {. }
$$

反向击穿电压

$$
U_{(\mathrm{BR}) \mathrm{CEO}} \geqslant 2 U_{\mathrm{CC}} \geqslant 40 \mathrm{~V}
$$

(3) 功率放大管的发热

功率放大管在把直流电源的功率转换为负载上的输出功率过程中, 管压降和流过集电极 的电流会造成集电极的功率损耗,使管子的结温升高。当达到结温后,会使管子损坏。为达到 最大允许管耗 $P_{\mathrm{CM}}$, 应该加装手册上推荐尺寸的散热器。如功放管 $3 \mathrm{AD} 6$, 加上 $120 \mathrm{~mm} \times 120$ $\mathrm{mm} \times 4 \mathrm{~mm}$ 的散热片后, 允许的 $P_{\mathrm{CM}}=10 \mathrm{~W}$; 而不加散热装置时, $P_{\mathrm{CM}}$ 仅为 $1 \mathrm{~W}$ 。手册上给出的 $P_{C M}$ 是在环境温度为 $25^{\circ} \mathrm{C}$, 并加装规定尺寸的散热器后测得的。 

\section{7 直流稳压电源}

\subsection{1 桥式整流及滤波电路}

\section{1. 桥式整流电路}

(1) 工作原理




$u_{2}$ 的正半周, $\mathrm{D}_{2} 、 \mathrm{D}_{4}$ 截止, $\mathrm{D}_{1} 、 \mathrm{D}_{3}$ 导通。 $u_{2}$ 的负半周, $\mathrm{D}_{1} 、 \mathrm{D}_{3}$ 截止, $\mathrm{D}_{2} 、 \mathrm{D}_{4}$ 导通。

正、负半周流过 $R_{\mathrm{L}}$ 的电流均为图中 $i_{\mathrm{o}}$ 的方向,在负载 上得到了方向不变的脉动电流和电压。该电流和电压含

有直流分量和较大的交流分量。

(2) 参数计算

(1) 输出直流电压 $U_{\mathrm{o}}=0.9 U_{2}, U_{2}$ 为变压器次级电压有效值。

(2) 输出直流电流 $I_{\mathrm{o}}=\left(0.9 U_{2}\right) / R_{\mathrm{L}}$ 。

(3) 脉动系数 $S \approx 0.67$ 。

(4.)二极管的平均电流 $I_{\mathrm{D}}=\frac{I_{\mathrm{o}}}{2}=\frac{0.9 U_{2}}{2 R_{\mathrm{L}}}=\frac{0.45 U_{2}}{R_{\mathrm{L}}}$ 。

(5) 二极管承受的最大反压 $U_{\mathrm{RM}}=\sqrt{2} U_{2}$ 。

(6) 变压器副边电流有效值 $I_{2}=1.11 I_{\mathrm{o}}$ 。

\section{2. 电容滤波电路 (图 2.7-2)}

(1) 参数计算

(1) 滤波电容的容量 $R_{\mathrm{L}} C \geqslant(3 \sim 5) \frac{T}{2}, T$ 为 $u_{2}$ 的周期。

(2) $U_{\mathrm{o}} \approx 1.2 U_{2}$ (在满足上式所选电容容量下)。

(3) 输出直流电流 $I_{\mathrm{o}}=\frac{U_{\mathrm{o}}}{R_{\mathrm{L}}}=1.2 \frac{U_{2}}{R_{\mathrm{L}}}$ 。



时, 峰值增大, 故整流二极管工作电流取无电容滤波时的 $2 \sim 3$ 倍。

(5) 二极管承受的最大反压 $U_{\mathrm{RM}}=\sqrt{2} U_{2}$ 。

(6) 变压器副边电流有效值 $I_{2}=(1.5 \sim 2) I_{\circ}$ 。

(2) 外特性

输出电压与输出电流的关系曲线称为电容滤波电路的外特性。图 2.7-3 中的曲线 2 为无 电容滤波时的外特性。曲线 1 为有电容滤波时的外特性。从图可见, 空载时 (即 $R_{\mathrm{L}}=\infty$ ), $U_{\text {。 }}$ $=\sqrt{2} U_{2} \approx 1.4 U_{2}$, 但随着 $I_{0}$ 的增加, 下降很快, 所以电容滤波电路适用于负载电流变化不大的 场合。 





【例 2.7-1】电路如图 2.7-4 所示, $u_{1}$ 的频率 $f=50 \mathrm{~Hz}, U_{\mathrm{o}}=30 \mathrm{~V}, R_{\mathrm{T}}=200 \Omega$ 。试求: (1) 变压器副边电压 $u_{2}$ 的有效值 $U_{2}$; (2) 滤波电容 $C$ 的容量及承受的最高反向电压 $U_{\text {CM }}$; (3) 流过二极管的平均电流 $I_{\mathrm{D}}$ 和承受的最高反向电压 $U_{\mathrm{RM}}$ 。

解: (1) 变压器副边电压有效值

$$
U_{2}=\frac{U_{\mathrm{o}}}{1.2}=\frac{30}{1.2}=25 \mathrm{~V}
$$

(2) $R_{\mathrm{L}} C \geqslant(3 \sim 5) \frac{T}{2}=4 \frac{T}{2}=2 T=2 \times \frac{1}{50}=0.04 \mathrm{~s}$

$$
C=\frac{0.04}{R_{L}}=\frac{0.04}{200}=200 \mu \mathrm{F}
$$

$C$ 承受的最高反向电压

$$
U_{\mathrm{CM}}=\sqrt{2} U_{2} \approx 35 \mathrm{~V}
$$

(3) 二极管的平均电流

$$
I_{\mathrm{D}}=\frac{1}{2} \times \frac{U_{\mathrm{o}}}{R_{\mathrm{L}}}=\frac{30}{2 \times 200}=0.075 \mathrm{~A}=75 \mathrm{~mA}
$$

承受的最高反向电压

$$
U_{\mathrm{RM}}=\sqrt{2} U_{2}=\sqrt{2} \times 25 \approx 35 \mathrm{~V}
$$

\subsection{2 串联型稳压电路}

\section{1. 工作原理}




\section{2. 电压调节范围}

该电路引人了深度负反馈, $\mathrm{T}$ 是射极跟随器接法。根据虚短有

$$
U_{\mathrm{N}}=U_{\mathrm{P}}=U_{\mathrm{REF}} \text {, 又 } U_{\mathrm{N}}=\frac{R_{2}^{\prime}}{R_{1}^{\prime}+R_{2}^{\prime}} U_{\mathrm{o}}
$$



$$
U_{\mathrm{o}}=\left(\frac{R_{1}^{\prime}+R_{2}^{\prime}}{R_{2}^{\prime}}\right) U_{\mathrm{REF}}
$$

当 $R_{\mathrm{p}}$ 的滑动头调至最上端时, 输出电压最小: $U_{\mathrm{omin}}=U_{\mathrm{REF}}\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{\mathrm{p}}+R_{2}}\right)$ 。 当 $R_{\mathrm{p}}$ 的滑动头调至最下端时, 输出电压最大: $U_{\mathrm{o} \text { max }}=U_{\mathrm{REF}}\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{2}}\right)$ 。 电压调节范围为: $U_{\mathrm{REF}}\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{\mathrm{p}}+R_{2}}\right)<U_{\mathrm{o}}<U_{\mathrm{REF}}\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{2}}\right)$ 。

\section{3. 参数选择}

用例题说明参数的选择。

【例 2.7-2】电路如图 2.7-6 所示, 已知运放器是理想的, 其最大输出电流为 $1 \mathrm{~mA} ; U_{\mathrm{REF}}$ $=6 \mathrm{~V}, R_{1}=R_{2}=R_{\mathrm{p}}=2 \mathrm{k} \Omega, \beta_{1}=20, \beta_{2}=50$ 。试求:

(1) 最大输出电流 $I_{\mathrm{omax}}$;

(2) 当 $U_{\mathrm{i}}=24 \mathrm{~V}$ 时, $\mathrm{T}_{1}$ 的最大集电极功耗 $P_{\mathrm{C}_{\text {max }}}$;

(3) 若 $\mathrm{T}_{1}$ 的 $U_{\mathrm{CE1}} \geqslant 3 \mathrm{~V}, U_{\mathrm{i}}$ 应至少多大?



解: 应首先求出 $U_{0}$ 的调节范围。

$U_{\text {omax }}=\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{2}}\right) \times U_{\mathrm{REF}}=\left(\frac{2+2+2}{2}\right) \times 6=18 \mathrm{~V}$

$U_{\text {omin }}=\left(\frac{R_{1}+R_{\mathrm{p}}+R_{2}}{R_{2}+R_{\mathrm{p}}}\right) \times U_{\mathrm{REF}}=\left(\frac{2+2+2}{2+2}\right) \times 6=9 \mathrm{~V}$

(1) $I_{\text {omax }}=1 \times \beta_{1} \beta_{2}=1 \times 20 \times 50=1 \mathrm{~A}$

(2) $P_{\text {Cmax }}=\left(U_{\mathrm{i}}-U_{\text {omin }}\right) I_{\text {omax }}=(24-9) \times 1=15 \mathrm{~W}$

(3) $U_{\mathrm{i}} \geqslant U_{\text {omax }}+U_{\mathrm{CE} 1 \min }=18+3=21 \mathrm{~V}$

2.7 .3 三端集成稳压器

\section{1. 输出电压固定的三端集成稳压器}

（1）电路结构及工作原理




\section{(2) 应用电路}

常用的固定电压输出式三端集成稳压器或三端稳压块有 W78 $\times \times$ (正电压输出) 和 W79 $x \times$ (负电压输出) 两个系列。额定输出电压有 $5 \mathrm{~V} 、 6 \mathrm{~V} 、 9 \mathrm{~V} 、 12 \mathrm{~V} 、 15 \mathrm{~V} 、 18 \mathrm{~V}$ 和 $24 \mathrm{~V}$ 七个等 级。型号中后两位数字表示额定输出电压值,如 7805 表示输出电压为 $+5 \mathrm{~V}$ 。

(1) 基本应用电路, 如图 2.7-8 和图 2.7-9 所示。要求 $U_{i}-U_{o} \geqslant 3 \mathrm{~V}, C_{1}$ 的作用是抑制自激 撽, $C_{2}$ 用来消弱高频噪声。





(2) 提高输出电压的电路。图 2.7-10 是提高输出电压的电路。 $U_{\mathrm{ow}}$ 是稳压块的额定输出 电压, $I_{\mathrm{W}}$ 是稳压块的静态电流。 $I_{R 1}=U_{\mathrm{oW}} / R_{1}, I_{R 1} \gg I_{\mathrm{W}}$, 所以有

$$
U_{\mathrm{o}}=I_{R 1} R_{1}+\left(I_{\mathrm{W}}+I_{R 1}\right) R_{2}=\left(1+\frac{R_{2}}{R_{1}}\right) U_{\mathrm{oW}}+I_{\mathrm{W}} R_{2} \approx\left(1+\frac{R_{2}}{R_{1}}\right) U_{\mathrm{oW}}
$$

可见,改变 $R_{1}$ 和 $R_{2}$ 的数值, 可以提高输出电压。





【例 2. 7-3】 电路如图 2.7-10 所示, 静态电流 $I_{\mathrm{W}}=10 \mathrm{~mA}, R_{1}=150 \Omega, R_{2}=90 \Omega$, 求 $U_{\mathrm{o}}$ 为 多少?

解: $U_{\mathrm{o}}=\left(1+\frac{R_{2}}{R_{1}}\right) U_{\mathrm{oW}}+I_{\mathrm{W}} R_{2}=\left(1+\frac{90}{150}\right) \times 5+10 \times 0.090=1.6 \times 5+0.9=8.9 \mathrm{~V}$

(3) 扩展输出电流的电路。图 2.7-11 是扩展输出电流的电路, 图中 $I_{\mathrm{oW}}$ 是稳压块的输出电 流。从图可直接得到

$$
U_{\mathrm{o}}=U_{\mathrm{oW}}+U_{\mathrm{D}}-U_{\mathrm{BE}}
$$

若 $U_{\mathrm{D}}=U_{\mathrm{BE}}$, 则 $U_{\mathrm{o}}=U_{\mathrm{oW}}$, 使输出电压仍为三端稳压器的输出电压值。输出电流

$$
I_{\mathrm{o}}=(1+\beta) I_{\mathrm{B}}=(1+\beta)\left(I_{\mathrm{oW}}-\frac{U_{\mathrm{oW}}}{R}\right)
$$



【例 2.7-4】电路如图 2.7-12 所示, $R=24 \Omega, I_{\mathrm{W}}=10$ $\mathrm{mA}$, 运算放大器是理想的。试问 $I_{\mathrm{o}}$ 为多少?

解: W7812 的额定输出电压 $U_{\mathrm{oW}}=12 \mathrm{~V}$, 利用运算放大器 的虚短概念, 则 $R$ 两端的电压为 $12 \mathrm{~V}$ 。所以

$$
I_{\mathrm{o}}=12 / 24=0.5 \mathrm{~A}
$$

\section{2. 输出电压可调的三端集成稳压器}

正电压输出的有 W117、W217、W317 系列,负电压输出的 有 W137、W237、W337 系列, $V_{\mathrm{REF}}=1.25 \mathrm{~V}$, 输出电压调节范围

为 $1.25 \sim 37 \mathrm{~V}$ 。


$\mathrm{D}_{1}$ : 当输人短路时, 为 $C_{4}$ 放电提供通路, 防止 $C_{4}$ 上存储的电荷放电反向流人稳压器, 使之损坏。输人电压较高, 电容量较大时, 必 须接此二极管加以保护。

$\mathrm{D}_{2}$ : 当输出短路时, 为 $C_{2}$ 提供放电通路, 防止 $C_{2}$ 通过调整端 $\mathrm{ADJ}$ 放电, 损坏稳压器。



输出电压 $U_{\mathrm{o}}=U_{\mathrm{REF}}\left(1+\frac{R_{\mathrm{p}}}{R}\right)+I_{\mathrm{ADJ}} R_{\mathrm{p}} \approx$

$1.25 \times\left(1+\frac{R_{\mathrm{p}}}{R}\right)$, 调节 $R_{\mathrm{p}}$ 即可改变输出电压。

为保证稳压器空载时也能正常工作, 一般 $R$ 取 $120 \sim 240 \Omega$ 。 可调范围。

【例 2.7-5】图 2.7-13 中, 已知 $R=120 \Omega, R_{\mathrm{p}}=2.2 \mathrm{k} \Omega, I_{\mathrm{ADJ}}=50 \mu \mathrm{A}_{\text {。 }}$, 求输出电压 $U_{\mathrm{o}}$ 的

解: $U_{\mathrm{o}}=U_{\mathrm{REF}}\left(1+\frac{R_{\mathrm{p}}}{R}\right)+I_{\mathrm{ADJ}} R_{\mathrm{p}}$ 。当 $R_{\mathrm{p}}=0$ 时, $U_{\mathrm{o}}=U_{\mathrm{REF}}=1.25 \mathrm{~V}$; 当 $R_{\mathrm{p}}=2.2 \mathrm{k} \Omega$ 时, $U_{\mathrm{o}}=$ 1. $25 \times(1+2200 / 120)+50 \times 10^{-6} \times 2200=24.3 \mathrm{~V}$ 。

输出电压 $U_{\mathrm{o}}$ 的可调范围为 $1.25 \mathrm{~V} \sim 24.3 \mathrm{~V}$ 。

2.7.4 硅稳压管稳压电路中限流电阻的计算及倍压整流电路工作原理

\section{1. 稳压管稳压电路中限流电阻的计算}

在图 2. 7-14 中, 限流电阻 $R$ 的选择应满足: (1) $R_{\min }$ 应满足: 流过稳压管的最大电流 $I_{Z_{\max }}<$ 稳压管的最大允许工作电流 $I_{\mathrm{ZM}}$, 使功耗不超过其最大耗散功率 $P_{\mathrm{M}}\left(P_{\mathrm{M}}=U_{\mathrm{Z}} I_{\mathrm{ZM}}\right)$, 保证稳压管 不被烧坏。(2) $R_{\max }$ 应满足: 流过稳压管的最小电流 $I_{\mathrm{Z} \min }>$ 稳压管的稳定电流 $I_{\mathrm{Z}}$, 保证稳压管具 有稳压功能。 当输人电压最大, 同时负载电流最小 ( $R_{\mathrm{L}}$ 最大) 时, 流过稳压管的电流最大, 其值应小于 $I_{2 u}$, 即

$$
\begin{aligned}
& I_{Z \mathrm{M}}>\frac{U_{\mathrm{imax}}-U_{\mathrm{o}}}{R_{\min }}-I_{\mathrm{omin}} \\
& R_{\min }>\frac{U_{\mathrm{imax}}-U_{\mathrm{o}}}{I_{\mathrm{ZM}}+I_{\mathrm{o} \min }}
\end{aligned}
$$

当输人电压最小, 同时负载电流最大 $\left(R_{\mathrm{L}}\right.$ 最小) 时, 流过稳压管的电流最小, 其值应大于 $l_{2}$, 即

$$
\begin{aligned}
& I_{\mathrm{Z}}<\frac{U_{\mathrm{i} \min }-U_{\mathrm{o}}}{R_{\max }}-I_{\mathrm{o} \max } \\
& R_{\max }<\frac{U_{\mathrm{imin}}-U_{\mathrm{o}}}{I_{\mathrm{Z}}+I_{\mathrm{o} \max }}
\end{aligned}
$$

$R$ 的选择范围是:

$$
\begin{aligned}
& \frac{U_{\mathrm{i} \text { max }}-U_{\mathrm{o}}}{I_{\mathrm{ZM}}+I_{\mathrm{o} \text { min }}}<R<\frac{U_{\mathrm{i} \text { min }}-U_{\mathrm{o}}}{I_{\mathrm{Z}}+I_{\mathrm{o} \max }} \\
& U_{\mathrm{o}}=U_{\mathrm{Z}} \text { (稳压管的稳定电压) }
\end{aligned}
$$

【例 2.7-6】电路如图 2.7-14 所示, 已知稳压管 $\mathrm{D}_{2}$ 的稳定电压 $U_{\mathrm{Z}}=6 \mathrm{~V}$, 稳定电流 $I_{\mathrm{Z}}=5 \mathrm{~mA}$, 最大电流 $I_{D M}=40 \mathrm{~mA}$; 输出电流 $I_{0}$ 的变化范围为 $0 \sim 20 \mathrm{~mA}, U_{\mathrm{i}}$ $=18 \mathrm{~V}$ 。当电网电压 $u_{1}$ 波动范围为 $\pm 10 \%$ 时, 求限流 电阻 $R$ 的取值范围?



$$
\text { 解: } \begin{aligned}
R & >\frac{U_{\mathrm{i} \max }-U_{\mathrm{o}}}{I_{\mathrm{ZM}}+I_{\mathrm{o} \text { min }}}=\frac{1.1 \times 18-6}{(40+0) \times 10^{-3}}=\frac{13.8}{40 \times 10^{-3}}=345 \Omega \\
R & <\frac{U_{\mathrm{i} \text { min }}-U_{\mathrm{o}}}{I_{\mathrm{Z}}+I_{\mathrm{o} \text { max }}}=\frac{0.9 \times 18-6}{(5+20) \times 10^{-3}}=\frac{10.2}{25 \times 10^{-3}}=408 \Omega
\end{aligned}
$$

所以 $345 \Omega<R<408 \Omega$

\section{2. 倍压整流电路的工作原理}

倍压整流电路适用于负载电流小并且基本维持不变的场合。

(1) 二倍压整流电路


每个二极管承受的最大反向电压为 $2 \sqrt{2} U_{2}, C_{1}$ 所承受的最大反向电压为 $\sqrt{2} U_{2}, C_{2}$ 所承受 的最大反向电压为 $2 \sqrt{2} U_{2}$ 。

(2) $n$ 倍压整流电路








\section{复习内容}

\section{1 数字电路基础知识}

\section{1 .1 数字电路的基本概念}

\section{1. 数字电路}

用来产生、传输、处理不连续变化的离散信号的电路称为数字电路。数字电路的特点是电 路中的半导体器件多数工作在开关状态, 即工作在饱和区或截止区, 而放大区只是过渡状态。

\section{2. 数字电路的分类}

按其组成的结构可分为分立元件电路和集成电路两大类。其中集成电路根据集成度又可 分为小规模集成电路、中规模集成电路、大规模集成电路、超大规模集成电路。

按电路所用器件不同分为双极型电路和单极型电路。其中双极型电路有 DTL、TTL、ECL 等, 单极型电路有 JFET、NMOS、PMOS、CMOS 等。

按电路的逻辑功能特点分为组合逻辑电路和时序逻辑电路。

\section{1 .2 数制和码制}

\section{1. 数制}

人们常用数字量表示事物的多少, 在多位数码中, 每一位的构成方法以及从低位向高位进 位的规则称为计数进位制, 简称数制。常用的数制有十进制数、二进制数、八进制数、十六进制 数等。 

\section{(1) 十进制数}

十进制数中的每一位用 $0 、 1 、 2 、 3 、 4 、 5 、 6 、 7 、 8 、 9$ 十个符号表示数码, 其基数为 10 ,进位关 系是“逢十进一”。

十进制数中,数码所在的位置不同,其“权”值的大小不同,所表示的数值就不同。如十进 制数 435.76 可按“权”展开如下:

435. $76=4 \times 10^{2}+3 \times 10^{1}+5 \times 10^{0}+7 \times 10^{-1}+6 \times 10^{-2}$

(2) 二进制数

二进制数中的每一位用 $0 、 1$ 两个符号表示数码, 其基数为 2 , 进位关系是“逢二进一”。

任何一个二进制数同样可以按权展开。如

$(101.11)_{2}=1 \times 2^{2}+0 \times 2^{1}+1 \times 2^{0}+1 \times 2^{-1}+1 \times 2^{-2}=(5.75)_{10}$

(3) 八进制数和十六进制数

“逢八进一”。

任何一个八进制数可以按权展开。如

$(234)_{8}=2 \times 8^{2}+3 \times 8^{1}+4 \times 8^{0}=(156)_{10}$

十六制数中的每一位用 $0 \sim 9 、 A 、 B 、 C 、 D 、 E 、 F$ 十六个符号表示数码,其基数为 16 ,进位关 系是“逢十六进一”。

任何一个十六进制数可以按权展开。如

$$
(2 \mathrm{~A} .7 \mathrm{~F})_{16}=2 \times 16^{1}+10 \times 16^{0}+7 \times 16^{-1}+15 \times 16^{-2}=(42.4960)_{10}
$$

\section{2. 数制的转换}

(1) $2^{n}$ 进制数转换成十进制数

二进制数、八进制数、十六进制数可将它们按权位展开后, 求得各位数之和, 即可得到对应 的十进制数。

【例 3.1-1】将 $(1011.01)_{2} 、(25.46)_{8} 、(B 2)_{16}$ 数转换成十进制数。

解: $\left(\begin{array}{lll}1 & 011.01\end{array}\right)_{2}=\left(1 \times 2^{3}+0 \times 2^{2}+1 \times 2^{1}+1 \times 2^{0}+0 \times 2^{-1}+1 \times 2^{-2}\right)_{10}$

$$
\begin{aligned}
& =(8+2+1+0.25)_{10} \\
& =(11.25)_{10}
\end{aligned}
$$

$(25.46)_{8}=\left(2 \times 8^{1}+5 \times 8^{0}+4 \times 8^{-1}+6 \times 8^{-2}\right)_{10}$

$=(16+5+0.5+0.09375)_{10}$

$=(21.59375)_{10}$

$(\mathrm{B} 2)_{16}=\left(11 \times 16^{1}+2 \times 16^{0}\right)_{10}=(178)_{10}$

(2) 十进制数转换成 $2^{n}$ 进制数

十进制数转换成 $2^{n}$ 进制数时, 可将其分为整数和小数两部分分别转换, 然后将其合并起 来,即可得出转换的结果。

(1) 整数部分的转换:采用除基取余法。即用目的数制的基数去除十进制整数,第一次所 得的余数为目的数的最低位, 把所得的商再除以该基数,所得的余数为目的数的次低位, 依此 类推, 直至商为 0 , 所得的余数为目的数的最高位。

【例 3.1-2】把 (28) ${ }_{10}$ 转换成二进制数、八进制数、十六进制数。 解:

$$
\begin{aligned}
& (28)_{10}=(11100)_{2} \\
& (28)_{10}=(34)_{8} \\
& (28)_{10}=(1 C)_{16}
\end{aligned}
$$

(2)小数部分的转换: 采用乘基取整法。即用该小数去乘目的数制的基数, 第一次乘得的结 果整数部分为目的数的最高位, 将乘得结果的小数部分再乘基数, 所得结果的整数部分作为目 的数的第二位, 依此类推, 直到小数部分为零或达到要求的精度 (要求的小数位数) 为止。

【例 3.1-3】把 $(0.765)_{10}$ 转换成二进制数、八进制数、十六进制数 (要求精确到小数后四 位)。

解:
$0.765 \times 2=1.530 \quad 1$
$0.765 \times 8=6.12$
6
$0.765 \times 16=12.24$
C
$0.530 \times 2=1.06 \quad 1$
$0.12 \times 8=0.96 \quad 0$
$0.24 \times 16=3.84 \quad 3$
$0.06 \times 2=0.12$
$0.96 \times 8=7.68$
$0.84 \times 16=13.44$
D
$0.12 \times 2=0.24$
$0.68 \times 8=5.44$
$0.44 \times 16=7.04$
7
$0.24 \times 2=0.48$
$0.44 \times 8=3.52$
$0.04 \times 16=0.64$
0
$(0.765)_{10}=(0.1100)_{2}$
$(0.765)_{10}=(0.6075)_{8}$
$(0.765)_{10}=(0 . \mathrm{C} 3 \mathrm{D} 7)_{16}$

在将十进制小数转换成其他进制时, 一般保留 4 位小数,第 5 位数在二进制时采用“零舍 一人”的原则,在八进制时采用“三舍四人”, 在十六进制时采用“七舍八人”。

\section{(3) $2^{n}$ 进制数之间的转换}

八进制的基数为 $8=2^{3}$, 十六进制的基数为 $16=2^{4}$, 所以 3 位二进制数构成 1 位八进制数, 4 位二进制数构成 1 位十六进制数。若将二进制数转换成八进制数或十六进制数, 整数部分 只要从低位到高位每 3 位或 4 位分成一组并代之以等值的八进制数或十六进制数, 小数部分 则要从高位到低位同理转换, 即可得到相应的八进制数或十六进制数。

将八进制数或十六进制数转换成二进制数时, 只要写出每位数码对应的二进制数, 依次排 好即可。

【例 3.14 】将二进制数(1 101101100.110111011$)_{2}$ 转换成八进制数。


$\begin{array}{llllllll}1 & 5 & 5 & 4 & 6 & 7 & 3\end{array}$

$(1101101100.110111011)_{2}=(1554.673)_{8}$

【例 3.1-5】将二进制数( 1101101100.110111011$)_{2}$ 转换成十六进制数。

解: $0011 \quad 0110 \quad 1100 \quad \cdot 1101 \quad 1101 \quad 1000$


【例 3.1-6】将八进制数 $(1234.56)_{8}$ 换成二进制数。

解: $\quad \begin{array}{ccccccc}1 & 2 & 3 & 4 & . & 5 & 6\end{array}$

$\begin{array}{lllllll}001 & 010 & 011 & 100 & \cdot & 101 & 110\end{array}$


\section{3. 码制}

用一定位数的二进制数来代表某一特定的事物、文字、符号等, 称为编码。采用不同的编 码形式,称为码制。常用的有如下几种。 

\section{(1) BCD 码}

用四位二进制数组成一组代码, 表示 $0 \sim 9$ 十个数字, 这种代码称为二一十进制代码 (Binary Coded Decimal), 简称 BCD 码。其常用的编码形式有 8421 码、2421 码、余三码等,如表 3 . 1-1 所示。

(1) 8421 码: 该码四位二进制数的权值从高位到低位分别为 $8 、 4 、 2 、 1$,故称 8421 码。它属 于有权码。如

$(84)_{10}=(10000100)_{8421 \mathrm{BCD}}$

(2)2421 码: 它也是有权码, 其权值从高位到低位分别为 $2 、 4 、 2 、 1$ 。

(3)余三码: 它属于无权码。它的数值要比它所表示的十进制数码多 3 。

表 3.1-1 常用的 BCD 码

\begin{tabular}{c|c|c|c}
\hline 十进制数 & 8421 码 & 2421 码 & 余三码 \\
\hline 0 & 0000 & 0000 & 0011 \\
\hline 1 & 0001 & 0001 & 0100 \\
\hline 2 & 0010 & 0010 & 0101 \\
\hline 3 & 0011 & 0011 & 0110 \\
\hline 4 & 0100 & 0100 & 0111 \\
\hline 5 & 0101 & 1011 & 1000 \\
\hline 6 & 0110 & 1100 & 1001 \\
\hline 7 & 0111 & 1101 & 1010 \\
\hline 8 & 1000 & 1110 & 1011 \\
\hline 9 & 1001 & 1111 & 1100 \\
\hline
\end{tabular}

(2) 格雷 (Gray) 码

它属于无权码。其特点是任意两个相邻的码之间只有一位数码不同, 另外, 由于首、尾相 接后也仅一位不同,故通常又称循环码。如表 3.1-2 所示。

表 3.1-2 格雷码的编码表

\begin{tabular}{c|c||c|c}
\hline 十进制数 & 格雷码 & 十进制数 & 格雷码 \\
\hline 0 & 0000 & 8 & 1100 \\
\hline 1 & 0001 & 9 & 1101 \\
\hline 2 & 0011 & 10 & 1111 \\
\hline 3 & 0010 & 11 & 1110 \\
\hline 4 & 0110 & 12 & 1010 \\
\hline 5 & 0111 & 13 & 1011 \\
\hline 6 & 0101 & 14 & 1001 \\
\hline 7 & 0100 & 15 & 1000 \\
\hline
\end{tabular}

(3) 奇偶校验码

奇偶校验码是将 1 位二进制代码配置到每一组二进制代码的最后一位, 表示每一组代码 中“1”的个数为奇数或偶数, 如表 3.1-3 所示为带奇偶校验位的 8421 码。

表 3.1-3 带奇偶校验位的 8421 码

\begin{tabular}{c|c|c|c}
\hline 十进制数 & 8421 码 & 奇校验码 & 偶校验码 \\
\hline 0 & 0000 & 00001 & 00000 \\
\hline 1 & 0001 & 00010 & 00011 \\
\hline 2 & 0010 & 00100 & 00101 \\
\hline 3 & 0011 & 00111 & 00110 \\
\hline 4 & 0100 & 01000 & 01001 \\
\hline 5 & 0101 & 01011 & 01010 \\
\hline 6 & 0110 & 01101 & 01100 \\
\hline 7 & 0111 & 01110 & 01111 \\
\hline 8 & 1000 & 10000 & 10001 \\
\hline 9 & 1001 & 10011 & 10010 \\
\hline
\end{tabular}

【例 3.1-7】试用 $8421 \mathrm{BCD}$ 码和余三码表示十进制数 (751) 10 。

解: (751) 10 用 $8421 \mathrm{BCD}$ 码表示时, 是用四位二进制数表示一位十进制数, 即可得 (0111 $01010001)_{8421 \mathrm{BCD}}$ 。

用余三码表示时,应在 8421BCD 码上加 3, 则可得(1010 10000100 ) xs3。

【例 3.1-8】已知二进制码为 $(01011001)_{2}$, 试求它所对应的格雷码。

解: 二进制码转换成格雷码的方法是从低位开始每两位相异或, 即可得出转换后所对应的 格雷码为 $(01011001)_{8421 \mathrm{BCD}}=(01110101)_{\text {Gray }}$ 。

\section{1 .3 半导体器件的开关特性}

\section{1. 理想开关特性}

在图 3.1-1 所示的电路中, 如果 $\mathrm{S}$ 是一个理想的开关, 则:

(1) 开关 $\mathrm{S}$ 断开时, 在开关两端 $\mathrm{A} 、 \mathrm{~B}$ 间的电压 $U_{\mathrm{AB}}=E$, 通过开关的电流 $I=0$, 开关等效电 阻 $R=\infty$;

(2)开关 $\mathrm{S}$ 闭合时, 在开关两端 $\mathrm{A} 、 \mathrm{~B}$ 间的电压 $U_{\mathrm{AB}}=0$, 通过开关的电流 $I=E / R$, 开关等效 电阻 $R=0$;

(3)开关 $\mathrm{S}$ 的开闭动作瞬时完成。

\section{2. 二极管开关特性}

二极管具有单向导电性。若二极管两端加上正向电压且超过死区电压时, 二极管导通, 且 钳位于 $U_{\mathrm{D}}=0.7 \mathrm{~V}$ (硅管) 或 $U_{\mathrm{D}}=0.2 \mathrm{~V}$ (锗管), 此时相当于开关闭合, 如图 3.1-2(a) 所示; 若 二极管两端加上反向电压或正向电压小于死区电压时, 二极管截止, 相当于开关断开, 如图 3.1-2(b) 所示。

\section{3. 三极管开关特性}

三极管可工作在截止、放大、饱和三种工作状态。通常在数字电路中, 三极管作为开关元 









件, 主要工作在饱和状态 (“开”态) 或截止状态(“关”态)。三极管的开关等效电路如图 3.1-3 所示。









三极管的三种工作状态的条件和特点可由表 3.1-4 表示。

表 3.1-4 NPN 硅三极管共发射极电路三种状态条件和特点

\begin{tabular}{|c|c|c|c|c|}
\hline \multicolumn{2}{|r|}{ 工作状态 } & 截止 & 放大 & 饱和 \\
\hline \multicolumn{2}{|r|}{ 条 件 } & $i_{\mathrm{b}} \approx 0$ & $0<i_{\mathrm{b}}<I_{\mathrm{CS}} / \beta$ & $i_{\mathrm{b}}>I_{\mathrm{CS}} / \beta$ \\
\hline \multirow{4}{*}{$\begin{array}{l}\text { I } \text { 隹 } \\
\text { 等 }\end{array}$} & 偏置情况 & 发射结和集电结均为反偏 & 发射结正偏, 集电结反偏 & 发射结和集电结均为正偏 \\
\hline & 集电极电流 & $i_{\mathrm{c}} \approx 0$ & $i_{c}=\beta i_{\mathrm{b}}$ & $i_{\mathrm{c}}=I \mathrm{es} \approx U \mathrm{cc} / R_{\mathrm{c}}$ \\
\hline & 管压降 & $U_{\text {CEO }} \approx U c \mathrm{c}$ & $U_{\mathrm{CE}}=U \mathrm{cc}-i_{\mathrm{c}} R_{c}$ & $U_{\text {CES }} \approx 0.3 \mathrm{~V}$ \\
\hline & $\mathrm{C} 、 \mathrm{E}$ 间等效电阻 & 很大, 相当于开路 & 可变 & 很小,相当于开关闭合 \\
\hline
\end{tabular}

【例 3.1-9】分析图 3.1-4 所示三个电路的工作状态。

解: 分析三极管的工作状态时, 要根据三极管的三个工作区的不同特点进行分析 (以 NPN 硅管为例)。

(1) 图 3.1-4(a) 所示电路状态分析。因为该电路中 $U_{\mathrm{BE}}>0.7 \mathrm{~V}$, 三极管导通, 有 $i_{\mathrm{B}}=\frac{U_{\mathrm{i}}-0.7}{R}=\frac{6-0.7}{50}=0.1 \mathrm{~mA}$

而

$$
I_{\mathrm{CS}}=\frac{E_{\mathrm{C}}-U_{\mathrm{CES}}}{R_{\mathrm{C}}}=\frac{12-0.3}{1 \times 10^{3}}=11.7 \mathrm{~mA}
$$










有

$$
i_{\mathrm{c}}=\beta i_{\mathrm{b}}=50 \times 0.1=5 \mathrm{~mA}<I_{\mathrm{cS}}
$$

所以,图 3.1-4(a) 所示电路中三级管工作在放大区。

(2) 图 3.1-4(b) 所示电路状态分析。因为

$$
U_{\mathrm{BE}}=\frac{U_{\mathrm{i}} R_{1}-E_{\mathrm{B}} R_{2}}{R_{1}+R_{2}}=-\frac{E_{\mathrm{B}} R_{2}}{R_{1}+R_{2}}=-\frac{6 \times 10}{30}=-2 \mathrm{~V}<0 \mathrm{~V}
$$

电路不满足三极管的导通条件, 图 3.1-4 (b) 电路中三极管工作在截止区。

(3) 图3.1-4 (c) 所示电路状态分析。利用戴维南定理,可求出基极电位

$$
\begin{aligned}
& U_{\mathrm{B}}=\frac{U_{i} R_{1}-E_{\mathrm{B}} R_{2}}{R_{1}+R_{2}}=\frac{6 \times 20-6 \times 10}{30}=2 \mathrm{~V} \\
& i_{\mathrm{b}}=i_{1}-i_{2}=\frac{U_{\mathrm{i}}-0.7}{R_{2}}-\frac{0.7+E_{\mathrm{B}}}{R_{1}}=(0.53-0.33)=0.2 \mathrm{~mA} \\
& I_{\mathrm{BS}}=\frac{I_{\mathrm{CS}}}{\beta}=\frac{E_{\mathrm{C}}-U_{\mathrm{CES}}}{\beta R_{\mathrm{C}}}=\frac{10-0.3}{2 \times 50}=0.12 \mathrm{~mA}
\end{aligned}
$$

满足 $i_{\mathrm{b}}>I_{\mathrm{BS}}$ 条件,图 3.1-4(c) 所示电路中三极管工作在饱和区。

\section{MOS 管开关特性}


\section{1 .4 三种基本逻辑关系及其表达方式}

基本逻辑关系有与逻辑、或逻辑和非 (反) 逻辑。实现这些逻辑关系的电路称为与门、或 门和非门。用这三种基本门电路还可以组成多种复合门电路。

\section{1. 与逻辑}

与逻辑: 输人逻辑变量 $A$ 与 $B$ 同时为 “ 1 ” 时, 输出逻辑变量 $F$ 才为 “ 1 ”, 否则 $F$ 为“ 0 ”。其 表达方式可用如下三种形式。 








(1)真值表

\begin{tabular}{|c|c|c|}
\hline$A$ & $B$ & $F$ \\
\hline 0 & 0 & 0 \\
\hline 0 & 1 & 0 \\
\hline 1 & 0 & 0 \\
\hline 1 & 1 & 1 \\
\hline
\end{tabular}

(2)逻辑表达式

$$
F=A \cdot B
$$

(3)逻辑符号,如图 3.1-6 所示。









\section{2. 或逻辑}

或逻辑: 输人逻辑变量 $A$ 与 $B$ 只要有一个为 “ 1 ” 时,输出逻辑变量 $F$ 才为 “ 1 ”, 否则 $F$ 为 “ 0 ”。其表达方式可用如下三种形式。

(1)真值表

\begin{tabular}{|c|c|c|}
\hline$A$ & $B$ & $F$ \\
\hline 0 & 0 & 0 \\
\hline 0 & 1 & 1 \\
\hline 1 & 0 & 1 \\
\hline 1 & 1 & 1 \\
\hline
\end{tabular}

(2)逻辑表达式

$$
F=A+B
$$

(3)逻辑符号, 如图 3.1-7 所示。









\section{3. 非 (反) 逻辑}

非 (反) 逻辑: 输人逻辑变量只有一个, 当输人逻辑变量 $A$ 为 “ 1 ” 时, 输出逻辑变量 $F$ 为 “ 0 ”; 当输人逻辑变量 $A$ 为 “ 0 ” 时, 输出逻辑变量 $F$ 为“ 1 ”, 两者状态相反。其表达方式可用如 下三种形式。

(1)真值表

\begin{tabular}{|l|l|}
\hline$A$ & $F$ \\
\hline 0 & 1 \\
\hline 1 & 0 \\
\hline
\end{tabular}

(2)逻辑表达式

$$
F=\bar{A}
$$

(3)逻辑符号, 如图 3.1-8 所示。









【例 3.1-10】由门电路组成的电路如图 3.1-9 所示。试写出输出 $F$ 的逻辑表达式; 并求 出当 $A=1 、 B=0$ 时, 输出 $F$ 的值。

解: 根据图 3.1-9 的电路, 可写出逻辑函数表达式:

$$
\begin{aligned}
& P=A B \\
& Q=\overline{\bar{A} \bar{B}} \\
& F=A B+\overline{\bar{A} \bar{B}}
\end{aligned}
$$

将 $A=1 、 B=0$ 代人上式, 可得

$$
F=1
$$

\section{2 集成逻辑门电路}

\subsubsection{TTL 集成逻辑门电路}



\section{TTL 与非门电路}

（1）电路结构




转移的角度, $\mathrm{T}_{1}$ 的作用相当于多个二极管作在 一个芯片上,几个二极管并联,构成一个多发 射极晶体管。 $\mathrm{T}_{1} 、 R_{1}$ 为输人级, 完成与的逻辑 功能。 $\mathrm{T}_{2} 、 R_{2} 、 R_{3}$ 为中间级, 完成倒相的功能, 获得两个相位相反的信号。 $\mathrm{T}_{3} 、 \mathrm{~T}_{4} 、 \mathrm{~T}_{5}$ 和 $R_{5}$ 构 成推拉式输出级 (又称图腾柱输出电路), 以 提高带负载的能力。

(2) 工作原理

输人全为高电平 $(3.6 \mathrm{~V})$ 时的工作情况 如下。

三极管 $\mathrm{T}_{1}: U_{A}=U_{B}=U_{C}=3.6 \mathrm{~V}, U_{\mathrm{B} 1}=$ $U_{\mathrm{BC} 1}+U_{\mathrm{BE} 2}+U_{\mathrm{BES}}=2.1 \mathrm{~V}, U_{\mathrm{C} 1}=1.4 \mathrm{~V}_{\circ} A 、 B 、 C$ 三个发射结都反偏, 集电结正偏, 此时, $\mathrm{T}_{1}$ 工作 于“倒置” 的状态, 即发射结起集电结的作用, 集电结起发射结的作用。

三极管 $\mathrm{T}_{2}$ : 因为 $I_{\mathrm{B} 2}=I_{\mathrm{CI}}$, 该电流很大, 可使 $\mathrm{T}_{2}$ 饱和。因此, $U_{\mathrm{CE} 2}=0.3 \mathrm{~V}$ 。

三极管 $\mathrm{T}_{5}$ : 因为 $U_{\mathrm{BS}}=U_{\mathrm{E} 2}=0.7 \mathrm{~V}$, 深饱和, 可允许很大的灌电流负载, $U_{\mathrm{ol}}=U_{\mathrm{CPS}}=0.3 \mathrm{~V}$ 。 三极管 $\mathrm{T}_{3} 、 \mathrm{~T}_{4}$ : 因为 $U_{\mathrm{C} 2}=U_{\mathrm{BE} 5}+U_{\mathrm{CE} 2}=0.7+0.3=1 \mathrm{~V}$, 所以, $\mathrm{T}_{3}$ 处于微导通, $\mathrm{T}_{4}$ 处于截止状 态。

输人有低电平 $(0.3 \mathrm{~V})$ 时的工作情况如下。

三极管 $\mathrm{T}_{1}$ : 设 $U_{A}=0.3 \mathrm{~V}, U_{B}=U_{C}=3.6 \mathrm{~V}$, 则 $U_{\mathrm{B} 1}=U_{A}+U_{\mathrm{BE} 1}=0.3+0.7=1 \mathrm{~V}$ 。此电位不 足以使 $\mathrm{T}_{1}$ 的集电结及 $\mathrm{T}_{2} 、 \mathrm{~T}_{5}$ 的发射结正偏, 故 $\mathrm{T}_{2} 、 \mathrm{~T}_{5}$ 截止。

三极管 $\mathrm{T}_{3} 、 \mathrm{~T}_{4}$ : 由于电源 $E_{\mathrm{c}}$ 通过 $R_{2}$ 向 $\mathrm{T}_{3}$ 提供基极电流, 因为 $\mathrm{T}_{5}$ 截止, 所以 $\mathrm{T}_{3} 、 \mathrm{~T}_{4}$ 处于导通 状态。

通过上述分析可以得出该电路的逻辑关系是: 输人全 1 , 输出为 0 ; 输人有 0 , 输出为 1 。

(3) 电压传输特性

TTL 与非门的电压传输特性如图 3.2-2 所示。 图中曲线大体分为四段,即 $A B$ 段、 $B C$ 段、 $C D$ 段和 $D E$ 段。

$A B$ 段: $U_{1}<0.6 \mathrm{~V}$ 。输人低电平, $\mathrm{T}_{1}$ 深饱和, $\mathrm{T}_{2}$ 、 $\mathrm{T}_{5}$ 截止, $\mathrm{T}_{3}$ 微导通, $\mathrm{T}_{4}$ 导通, 输出 $U_{\mathrm{o}}=U_{\mathrm{oH}}=3.6 \mathrm{~V}$, 属于“关门”状态。

$B C$ 段: $U_{\mathrm{i}}=0.6 \sim 1.4 \mathrm{~V}$ 。随着 $U_{\mathrm{i}}$ 的增高 $\mathrm{T}_{2}$ 开 始导通, $U_{\mathrm{C} 2}$ 随 $U_{\mathrm{Cl}}$ 的上升而下降, 而经 $\mathrm{T}_{3} 、 \mathrm{~T}_{4}$ 使 $U_{\mathrm{o}}$ 随 $U_{\mathrm{C} 2}$ 的下降而下降,出现了 $B C$ 段。



$C D$ 段: $U_{\mathrm{i}} \approx 1.4 \mathrm{~V}$ 。当 $U_{\mathrm{i}} \approx 1.4 \mathrm{~V}$ 时, $T_{2}$ 导通电流较大。以至 $U_{\mathrm{B} 5}$ 达到 $0.7 \mathrm{~V}$ 左右, 使 $\mathrm{T}_{5}$ 很 快由导通变为饱和, 使输出幅度明显下降。

$D E$ 段: $U_{\mathrm{i}}>1.4 \mathrm{~V}_{0}$ 。 $\mathrm{T}_{5}$ 饱和导通, $\mathrm{T}_{4}$ 截止。输人增加对输出电压影响不大。此时 $U_{\mathrm{o}}=U_{\mathrm{ol}}$. $=0.35 \mathrm{~V}$, 属于与非门的“开门”状态。

从电压传输特性曲线可以得出:

低电平噪声容限 高电平噪声容限

$$
U_{\mathrm{NL}}=U_{\mathrm{OFF}}-U_{\mathrm{iL}}=0.8-0.1=0.70 \mathrm{~V}
$$

$$
U_{\mathrm{NH}}=U_{\mathrm{iH}}-U_{\mathrm{ON}}=3.0-1.4=1.6 \mathrm{~V}
$$

2. 特殊 TTL 门电路

(1) 集电极开路与非门 (OC门)

为了使门电路的输出能够并联使用, 采用的方法就是把输出级改为集电极开路的三极管 结构, 称为集电极开路的门电路 (OC门), 电路结构和逻辑符号如图 3.2-3 所示。



(常用)



OC 门工作时, 输出端需要外接负载电阻和电源。

【例 3.2-1】试分析图 3.2-4 所示电路的逻辑功能。



解: $Y=Y_{1} \cdot Y_{2}=\overline{A B} \cdot \overline{C D}=\overline{A B+C D}$

(2) 三态与非门(TS门)

普通的 TTL 门有两个状态, 即输出逻辑 “ 0 ” 和逻辑 “ 1 ”, 这两个状态都是低阻输出。三态 输出门是在普通门电路的基础上附加控制电路而构成的, 它的特点是多了一种高阻状态, 电路 结构和逻辑符号如图 3.2-5 所示。

在电路中 $E N$ 为控制端 (使能端), 当 $E N=1$ 时, 对 $\mathrm{T}_{1}$ 管无影响, 二极管 $\mathrm{D}$ 截止, 电路处于 与非门工作状态; $Y=\overline{A B}$; 当 $E N=0$ 时, $\mathrm{T}_{1}$ 导通, $U_{\mathrm{b}} \approx 1 \mathrm{~V}, \mathrm{~T}_{2} 、 \mathrm{~T}_{3}$ 管截止, 由于 $\mathrm{D}$ 导通, 使 $\mathrm{T}_{4}$ 管也 


截止, 故输出端呈高阻状态。这样输出端就有三种状态, 即高电平、低电平、高阻状态。由于电 路在 $E N=1$ 时为正常的与非工作状态, 所以称为高电平有效三态门。若在使能端加人一个非 门, 此时, 电路在 $\overline{E N}=0$ 时才处于正常的与非门工作状态, 故称为低电平有效三态门。

\section{3. 其他逻辑功能 TTL 逻辑门}

TTL 逻辑门电路除上述的与非门电路外, 还可构成具有其他逻辑功能的集成逻辑门电路。

(1) 或非门

【例 3.2-2】试分析图 3.2-6 所示电路的逻辑功能。



解: 该电路为或非门电路, 即

$$
Y=\overline{A+B}
$$

(2) 与或非门

【例 3.2-3】试分析图 3.2-7 所示电路的逻辑功能。

解: 该电路为与或非门电路, 即

$$
Y=\overline{A B+C D}
$$

(3) 异或门

【例 3.2-4】试分析图 3.2-8 所示电路的逻辑功能。

解: 该电路为异或门电路, 即 





$$
Y=A \bar{B}+\bar{A} B=A \oplus B
$$

\subsubsection{MOS 集成逻辑门电路}

MOS 集成电路按照所用的管子类型不同分为三种。

(1)PMOS 电路, 是由 PMOS 管构成的集成电路。其制造工艺简单, 但工作速度较低。

(2)NMOS 电路, 是由 NMOS 管构成的集成电路。其工作速度优于 PMOS, 但制造工艺较为 复杂。

(3)CMOS 电路, 是由 PMOS 管和 NMOS 管构成的互补 MOS 集成电路。具有静态功耗低、 抗干扰能力强、工作稳定性好、开关速度高等优点。

\section{NMOS 反相器及逻辑门}

(1) NMOS 反相器


一般 NMOS 电源电压 $E_{\mathrm{D}} \leqslant 15 \mathrm{~V}$, 典型数据为 $12 \mathrm{~V}, \mathrm{NMOS}$ 增强型管的开启电压 $U_{\mathrm{TN}}=3 \sim 5$ $\mathrm{V}, U_{\mathrm{TN}}$ 一般取 $4 \mathrm{~V}$ 进行分析。

工作原理:

当 $U_{\mathrm{i}}$ 为低电平 $(1 \mathrm{~V})$ 时, 由于 $U_{\mathrm{i}}<U_{\mathrm{T} 1}(4 \mathrm{~V})$, 因 此 $\mathrm{T}_{1}$ 截止; 而 $\mathrm{T}_{2}$ 管因 $U_{\mathrm{G} 2}=U_{\mathrm{D} 2}=E_{\mathrm{D}}=12 \mathrm{~V}$, 因此 $U_{\mathrm{GS} 2}$ $>U_{\mathrm{T} 2}(4 \mathrm{~V})$, 开启导通。输出电压 $U_{\mathrm{o}}=E_{\mathrm{D}}-U_{\mathrm{T} 2}=12$ $-4=8 \mathrm{~V}$, 为输出高电平。

当 $U_{i}$ 为高电平 $(8 \mathrm{~V})$ 时, 由于 $U_{i}>U_{T 1}(4 \mathrm{~V})$, 因 此 $\mathrm{T}_{1}$ 开通; 而 $\mathrm{T}_{2}$ 管因 $U_{\mathrm{GS}}$ 也大于 $U_{\mathrm{T} 2}(4 \mathrm{~V}), \mathrm{T}_{2}$ 也开启 导通。则输出电压

$$
U_{\mathrm{o}}=\frac{E_{\mathrm{D}}}{r_{\mathrm{DS} 1}+r_{\mathrm{DS} 2}} \times r_{\mathrm{DS} 1}
$$



由于 $\mathrm{T}_{1}$ 和 $\mathrm{T}_{2}$ 的跨导不同, 其中 $g_{m 1} \gg g_{m 2}$, 所以 $\mathrm{T}_{1}$ 和 $\mathrm{T}_{2}$ 导通后, 漏源电阻 $r_{\mathrm{DS} 1}<<r_{\mathrm{DS} 2}$, 输出 电压 $U_{\mathrm{o}}=U_{\mathrm{oL}} \approx 1 \mathrm{~V}$ 。


电压传输特性和性能分析:

典型 NMOS 增强型负载管反向器的电压 传输特性如图 3.2-10 所示。输出高电平 $U_{\mathrm{oH}}=$

线 $U_{\mathrm{i}} \geqslant 4 \mathrm{~V}$ 后转折。

由电压传输特性曲线可得其关门电平 $U_{\mathrm{OFF}}$ 为 $4.5 \mathrm{~V}$; 开门电平 $U_{\mathrm{ON}}$ 为 $5 \mathrm{~V}$, 则可求出此反相 器的噪声容限。低电平噪声容限为

$$
U_{\mathrm{NL}}=U_{\mathrm{OFF}}-U_{\mathrm{iL}}=4.5-1=3.5 \mathrm{~V}
$$

高电平噪声容限为

$$
U_{\mathrm{NH}}=U_{\mathrm{iH}}-U_{\mathrm{ON}}=8-3=3 \mathrm{~V}
$$

可见 MOS 电路抗干扰能力较强。

(2) NMOS门电路

NMOS 与非门和或非门电路分别如图 3.2-11(a)、(b) 所示。







其中,图 3.2-11 (a) 所示电路输出为

$$
L=\overline{A \cdot B}
$$


$$
L=\overline{A+B}
$$

NMOS 与或非门和或与非门电路分别如图 3.2-12(a)、(b) 所示。

其中, 图 3.2-12(a) 所示电路输出为

$$
L=\overline{A B+C}
$$


$$
L=\overline{(A+B)(C+D)}
$$

【例 3. 2-5】 NMOS 逻辑门电路如图 3.2-13 所示, 试写出输出逻辑表达式。

解: $Y_{1}=\overline{\overline{A(B+C)+A D}}=A B+A C+A D$

【例 3. 2-6】MOS 逻辑门电路如图 3.2-14 所示, 试写出输出逻辑表达式。 











解: $Y_{2}=\overline{\overline{A(B+C)}} \overline{\overline{B+B C+D}}=A B+A C+B C+D$ 

\section{PMOS 反相器及逻辑门}

(1) PMOS 反相器

在 PMOS 集成电路中,一般取负逻辑, 规定: 高电平为“ 0 ”, 低电平为“ 1 ”。由图 3. 2-15 可 以看出, 当输人 $U_{\mathrm{i}}$ 为 $-1 \mathrm{~V}$ 时 (高电平“ 0 ”), 输出 $U_{o}$ 为 $-8 \mathrm{~V}$ (低电平 “ 1 ”) ; 输人 $U_{i}$ 为 $-8 \mathrm{~V}$ (低 电平“ 1 ”) 时, 输出 $U_{\mathrm{o}}$ 为 $-1 \mathrm{~V}$ (高电平 “ 0 ”)。



(2) PMOS 门电路

PMOS 与非门、或非门、与或非门电路分别如图 3.2-16(a)、(b)、(c) 所示。

其中, 图 3.2-16 (a) 所示电路输出为

$$
L=\overline{A B}
$$


$$
L=\overline{A+B}
$$


$$
L=\overline{A B+C}
$$






$\frac{1}{(\mathrm{c})}$



\section{CMOS 反相器及逻辑门}

\section{(1) CMOS 反相器}

CMOS 反相器是由一个 NMOS 管和一个 PMOS 管构成的互补 MOS 反相电路, 如图 3. 2-17 所示。工作管 $T_{1}$ 是增强型 NMOS 管, 它的衬 底 $B_{1}$ 与 $S_{1}$ 相接, 并接地 (最低电平) ; 负载管 $\mathrm{T}_{2}$ 是一个增强型 PMOS 管, 它的衬底 $B_{2}$ 与 $S_{2}$ 相接, 并接电源 $E_{\mathrm{D}}$ (最高电平)。栅极连接在 一起作为反向器的输人端, 漏极也连接在一 起作为反向器的输出端。

电源电压 $E_{\mathrm{D}}>\left|U_{\mathrm{TP}}\right|+U_{\mathrm{TN}}$ 。( $U_{\mathrm{TP}} 、 U_{\mathrm{TN}}$ 分 别为 $\mathrm{T}_{2}$ 管和 $\mathrm{T}_{1}$ 管的开启电压), 一般取 $U_{\mathrm{TP}}=$ $-3 \mathrm{~V} ; U_{\mathrm{TN}}=3 \mathrm{~V}$, 电源电压 $E_{\mathrm{D}}$ 为 $+10 \mathrm{~V}$ 。

工作原理:



当 $U_{\mathrm{i}}$ 为低电平 $(\approx 0 \mathrm{~V})$ 时, 工作管 $\mathrm{T}_{1}$ 截止, 负载管 $\mathrm{T}_{2}$ 导通, 电源电压主要降在 $\mathrm{T}_{1}$ 管上, 输 出电压 $U_{\mathrm{o}}=E_{\mathrm{D}}(10 \mathrm{~V})$, 为高电平。

当 $U_{\mathrm{i}}$ 为高电平 $(10 \mathrm{~V})$ 时, 工作管 $\mathrm{T}_{1}$ 导通, 负载管 $\mathrm{T}_{2}$ 截止, 电源电压主要降在 $\mathrm{T}_{2}$ 管上, 输出 电压 $U_{\mathrm{o}}=0 \mathrm{~V}$, 为低电平。

由上述分析可见, CMOS 反相器有倒相的功能; 两管中一个导通, 另一个截止, 因此静态功 耗极小; 两个互补管的跨导都比较大, 因此在两个不同的输出状态下, 都为负载电容提供了一 个低阻抗的快速放电回路,使其工作速度较高。

(2) CMOS门电路

【例 3. 2-7】试分析图 3.2-18(a)、(b)、(c) 所示的 CMOS 逻辑门电路的逻辑功能。









解: 图 3.2-18(a) $: L=\overline{A B}$, 为与非门。



(3) CMOS 传输门

CMOS 传输门电路与符号如图 3.2-19 所示。它是由一个 PMOS 管 $\mathrm{T}_{\mathrm{P}}$ 和一个 NMOS 管 $\mathrm{T}_{\mathrm{N}}$ 并联而成, 两管源极接在一起, 作为输人端 $U_{\mathrm{i}}$ 。两管漏极接在一起作为输出端 $U_{\mathrm{o}}$, 两管相极作 




为控制端 (如加一对 $C P$ 和 $\overline{C P}$ (互为反相) 的控制 电压)。由于 MOS 管结构对称, 源极和漏极可以 互换, 电流可两个方向流动, 所以 $U_{\mathrm{i}}$ 和 $U_{\mathrm{o}}$ 可以互 换,因此,传输门称双向开关。

工作原理:

当 $C P=$ “ 1 " $(10 \mathrm{~V}), \overline{C P}=$ “ 0 ” ( $0 \mathrm{~V})$ 时, 输人 在 $0 \sim 10 \mathrm{~V}$ 范围内连续变化, 传输门 $\mathrm{TG}$ 开通。为 分析方便起见, 设 $T_{P}$ 和 $T_{N}$ 的开启电压均为 $3 \mathrm{~V}$ 。 $U_{\mathrm{i}}$ 在 $0 \sim 7 \mathrm{~V}$ 范围内变化时, $\mathrm{T}_{\mathrm{N}}$ 导通; $U_{\mathrm{i}}$ 在 $3 \sim 10 \mathrm{~V}$ 范围内变化时, $\mathrm{T}_{\mathrm{p}}$ 导通。因此, $U_{\mathrm{i}}$ 在 $0 \sim 10 \mathrm{~V}$ 范围 内变化时, $\mathrm{T}_{\mathrm{p}} 、 \mathrm{~T}_{\mathrm{N}}$ 管中至少有一个管子导通, 即相

当于开关接通,输出 $U_{\mathrm{o}}=U_{\mathrm{i}}$ 。

当 $C P=$ “ 0 " $(0 \mathrm{~V}), \overline{C P}=$ “ 1 ” (10 V) 时, 无论输人为在 $0 \sim 10 \mathrm{~V}$ 范围内的任何值, $\mathrm{T}_{\mathrm{P}} 、 \mathrm{~T}_{\mathrm{N}}$ 均 不能导通,因此, 相当于开关断开。

【例 3.2-8】 MOS 逻辑门电路如图 3.2-20 所示, 试写出输 出逻辑表达式。

解: $Y=A \bar{B}+\bar{A} B=A \oplus B$

【例 3.2-9】在 CMOS 电路中, 有时采用如图 3.2-21 所示 的电路扩展它的逻辑功能, 试分析各图的逻辑功能, 写出 $Y_{1} \sim$ $Y_{4}$ 的逻辑式。

解:图( a)

$$
Y_{1}=\overline{A B C D E}
$$












$$
Y_{2}=\overline{A+B+C+D+E}
$$


$$
Y_{3}=\overline{A B C} \cdot \overline{D E F}=\overline{A B C+D E F}
$$


$$
Y_{4}=\overline{A+B+C} \cdot \overline{D+E+F}
$$

\section{3 逻辑代数及逻辑函数化简}

\subsection{1 逻辑代数的基本运算}

逻辑代数中,基本逻辑运算有“与”逻辑、“或”逻辑、“非”逻辑三种运算。

\section{1. “与”逻辑运算}

“与”逻辑运算简称“与”运算, 又称逻辑乘, 通常用符号 “ . ”表示。两个变量的 “与”运算 的逻辑表达式为

$$
F=A \cdot B
$$

对于 $n$ 个变量的“与”运算逻辑表达式为

$$
F=A_{1} \cdot A_{2} \cdot A_{3} \cdot \cdots \cdot A_{n}
$$

\section{2. “或”逻辑运算}

“或”逻辑运算简称 “或”运算, 又称逻辑加, 通常用符号“ + ”表示。两个变量的“或”运算 的逻辑表达式为

$$
F=A+B
$$

对于 $n$ 个变量的“或”运算逻辑表达式为

$$
F=A_{1}+A_{2}+A_{3}+\cdots+A_{n}
$$

\section{3. “非”逻辑运算}

“非”逻辑运算简称“非”运算, 又称反相运算。其逻辑表达式为

$$
F=\bar{A}
$$

实际应用中会出现一些复杂的逻辑函数式, 它们都是由一些基本运算组合而成。几种常 用的逻辑运算逻辑符号及表达式如图 3.3-1 所示。

\subsection{2 逻辑代数的基本定律和基本定理}

\section{1. 逻辑代数的基本定律}

(1)自等律

$$
\begin{aligned}
& A+0=A \\
& A \cdot 1=A
\end{aligned}
$$

(2)互补律

$$
\begin{aligned}
& A+\bar{A}=1 \\
& A \cdot \bar{A}=0
\end{aligned}
$$

(3) 交换律

$$
\begin{aligned}
& A+B=B+A \\
& A \cdot B=B \cdot A
\end{aligned}
$$




(4) 结合律

$$
\begin{aligned}
& (A+B)+C=A+(B+C) \\
& (A \cdot B) \cdot C=A \cdot(B \cdot C)
\end{aligned}
$$

(5) $0-1$ 律

$$
\begin{aligned}
& 1+A=1 \\
& 0 \cdot A=0
\end{aligned}
$$

(6)重叠律

$$
\begin{aligned}
& A+A=A \\
& A \cdot A=A
\end{aligned}
$$

(7)分配律

$$
\begin{aligned}
& A \cdot(B+C)=A \cdot B+A \cdot C \\
& A+B \cdot C=(A+B) \cdot(A+C)
\end{aligned}
$$

(8)狄 - 摩根定律 (De Morgan)

$$
\begin{aligned}
& \overline{A \cdot B \cdot C}=\bar{A}+\bar{B}+\bar{C} \\
& \overline{A+B+C}=\bar{A} \cdot \bar{B} \cdot \bar{C}
\end{aligned}
$$

(9)二次求反律

\section{2. 几个常用的公式}

$$
\begin{aligned}
& A+A B=A \\
& A+\bar{A} B=A+B \\
& A B+A \bar{B}=A \\
& A(A+B)=A \\
& A B+C D=(A+C)(A+D)(B+C)(B+D) \\
& A B+\bar{A} C+B C=A B+\bar{A} C
\end{aligned}
$$



\section{3. 逻辑代数的基本定理}

\section{(1) 代入定理}

在任何逻辑代数等式中, 如果等式两边所有出现某一变量的位置都代以一个逻辑函数, 则 等式仍然成立。这就是代人定理。

\section{(2) 反演定理}

求原函数的反函数的过程称为反演。对于任意一个逻辑函数 $Y$, 若将其中的 “.”换成

得出的结果即为原函数的反函数 $\bar{Y}_{\text {。 }}$ 这个规律称为反演定理。

使用反演定理时应注意两个原则: “先括号后乘、加” 的运算原则; 不属于单个变量的反号 应保留下来。

【例 3. 3-1】若 $Y=\overline{B+C D+\overline{C+E}}+A B$, 求 $\bar{Y}_{\text {。 }}$

解: 用反演定理可以直接写出:

$$
\bar{Y}=\overline{\bar{B}(\bar{C}+\bar{D}) \cdot \overline{\bar{C}} \bar{E}} \cdot(\bar{A}+\bar{B})
$$

\section{(3) 对偶定理}

对于任意一个逻辑函数 $Y$, 若将其中的“ . ”换成“ + ”, “+”换成 “.”, “ 0 ”换成“ 1 ”, “ 1 ” 换成 “ 0 ”, 变量不变, 则得出的函数式为原函数式的对偶式 $Y^{\prime}$ 。

【例 3.3-2】若 $Y=A(\bar{B}+C)+C D$ 求 $Y^{\prime}$ 。

解: 用对偶定理可直接写出:

$$
Y^{\prime}=(A+\bar{B} C)(C+D)
$$

\subsection{3 逻辑函数的建立和表达方法}

对于任何一个二值的逻辑问题, 常常可以设定此问题产生的条件为输入逻辑变量, 设定此 问题产生的结果为输出逻辑变量, 从而用逻辑函数来描述它。

下面以一个实例来说明逻辑函数的建立和它的描述方法。如有三个变量 $A 、 B 、 C$ 。当三 个输人变量中有两个或两个以上为 “ 1 ” 时输出为 “ 1 ”, 否则, 输出为“ 0 ”。其逻辑关系的真值表 列于表 3. 3-1 中。

\section{表 3. 3-1 真值表}

\begin{tabular}{l|l|l|l||l|l|l|l}
\hline$A$ & $B$ & $C$ & $Y$ & $A$ & $B$ & $C$ & $Y$ \\
\hline 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
\hline 0 & 0 & 1 & 0 & 1 & 0 & 1 & 1 \\
\hline 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 \\
\hline 0 & 1 & 1 & 1 & 1 & 1 & 1 & 1 \\
\hline
\end{tabular}

根据真值表可写出逻辑函数表达式并化简:

$$
\begin{aligned}
Y & =\bar{A} B C+A \bar{B} C+A B \bar{C}+A B C=\bar{A} B C+A \bar{B} C+A B(\bar{C}+C) \\
& =\bar{A} B C+A(\bar{B} C+B)=\bar{A} B C+A B+A C=B(\bar{A} C+A)+A C \\
& =A B+A C+B C
\end{aligned}
$$

根据逻辑函数表达式, 可以画出相应的逻辑电路图, 如图 3.3-2 所示。 



卡诺图是描述逻辑函数的另一种方法,如图 3.3-3 所 示。它是用几何图形来简化逻辑函数表达式的有用工具。

综上所述, 逻辑函数真值表、逻辑函数表达式、逻辑电 路图和卡诺图是描述逻辑问题的四种不同形式。这四种 形式是可以相互转换的。

【例 3.3-3】 已知一个三变量逻辑函数的卡诺图如图 3.3-4 所示。试用真值表、逻辑函数表达式和逻辑图来表 示该逻辑函数。





解:用真值表表示该逻辑函数如下。

\begin{tabular}{l|l|l|l||l|l|l|l}
\hline$A$ & $B$ & $C$ & $Y$ & $A$ & $B$ & $C$ & $Y$ \\
\hline 0 & 0 & 0 & 0 & 1 & 0 & 0 & 0 \\
\hline 0 & 0 & 1 & 0 & 1 & 0 & 1 & 1 \\
\hline 0 & 1 & 0 & 0 & 1 & 1 & 0 & 1 \\
\hline 0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
\hline
\end{tabular}

用逻辑函数表示为

$$
Y=A \bar{B} C+A B \bar{C}+A B C=A \bar{B} C+A B(\bar{C}+C)=A B+A C
$$

用逻辑图表示,如图 3. 3-5 所示。



\subsection{4 逻辑函数的标准表达形式}

一个逻辑函数可以有多种等效的表达式,但其标准形式是唯一的。逻辑函数有两种标准 形式, 即标准与或式(最小项表达式) 和标准或与式(最大项表达式)。

\section{1. 标准与或式(最小项表达式)}

在 $n$ 个变量的逻辑函数中,若 $m$ 是由 $n$ 个变量组成的乘积项, 在每一个乘积项中, 这 $n$ 个 变量均以原变量或反变量出现,且仅出现一次,则该乘积项 $m$ 即为最小项。例如, $A 、 B 、 C$ 三个 变量的逻辑函数共有 $\bar{A} \bar{B} \bar{C} 、 \bar{A} \bar{B} C 、 \bar{A} B \bar{C} 、 \bar{A} B C 、 A \bar{B} \bar{C} 、 A \bar{B} C 、 A B \bar{C} 、 A B C$ 八个最小项。为了叙述和 书写方便,通常用 $m_{i}$ 表示最小项。下标 $i$ 按下面规则规定: 把最小项的取值看做一个二进制 数,那么它所表示的十进制数即为该最小项的编号。如最小项 $A \bar{B} C$ 记作 $m_{5}$ 。

$n$ 变量构成的逻辑函数共有 $2^{n}$ 个最小项。

任何一个逻辑函数都可以表示成若干最小项之和,该表达式称为最小项标准与或表达式。

【例 3.3-4】写出 $Y=A B+A C+B C$ 的最小项标准与或表达式。

解: $Y=A B+A C+B C$

$$
\begin{aligned}
& =A B(C+\bar{C})+A C(B+\bar{B})+B C(A+\bar{A}) \\
& =A B C+A B \bar{C}+A B C+A \bar{B} C+A B C+\bar{A} B C \\
& =\bar{A} B C+A \bar{B} C+A B \bar{C}+A B C \\
& =m_{3}+m_{5}+m_{6}+m_{7}=\sum m(3,5,6,7)
\end{aligned}
$$

\section{2. 标准或与式 (最大项表达式)}

在 $n$ 个变量的逻辑函数中, 若 $M$ 是由 $n$ 个变量组成的和项, 在每一个和项中, 这 $n$ 个变量 均以原变量或反变量出现, 且仅出现一次, 则和项 $M$ 即为最大项。例如 $A 、 B 、 C$ 三个变量的逻 辑函数共有 $(\bar{A}+\bar{B}+\bar{C}) 、(\bar{A}+\bar{B}+C) 、 \cdots \cdots,(A+B+C)$ 八个最大项。为了叙述和书写方便, 通 常用 $M_{j}$ 表示最大项。下标 $j$ 按下面规则规定: 最大项的取值看做一个二进制数,然后取反,那 么它所表示的十进制数即为该最大项的编号。如最大项 $(A+\bar{B}+C)$ 记作 $M_{2}$ 。

$n$ 变量构成的逻辑函数共有 $2^{n}$ 个最大项。

任何一个逻辑函数, 都可以表示成若干最大项之积, 该表达式称为最大项标准或与表达 式。

【例 3. 3-5】写出 $Y=A B+A C+B C$ 的最大项标准或与表达式。

解: $Y=A B+A C+B C$

$$
\begin{aligned}
& =(A B+A C+B)(A B+A C+C)=(B+A C)(C+A B) \\
& =(B+A)(B+C)(A+C)(B+C)=(A+B)(A+C)(B+C) \\
& =(A+B+C \bar{C})(A+B \bar{B}+C)(A \bar{A}+B+C) \\
& =(A+B+C)(A+B+\bar{C})(A+B+C)(A+\bar{B}+C)(A+B+C)(\bar{A}+B+C) \\
& =(A+B+C)(A+B+\bar{C})(A+\bar{B}+C)(\bar{A}+B+C) \\
& =M_{0} M_{1} M_{2} M_{4}=\prod M(0,1,2,4)
\end{aligned}
$$

3. 最小项与最大项的关系

对于一个逻辑函数的最小项表达式 $Y=\sum m_{i}$, 其最大项表达式就是它的反函数 $\bar{Y}$, 即

$$
Y=\overline{\bar{Y}}=\overline{\sum_{k \neq i} m_{k}}=\prod_{k \neq i} \overline{m_{k}}=\prod_{k \neq i} M_{k}
$$

\subsection{5 逻辑函数的化简}

\section{1. 逻辑函数的公式化简法}

公式法就是灵活运用逻辑代数的基本定律、定理和常用公式进行简化。现将经常使用的 方法归纳如下。

(1) 并项法

利用互补律 $A+\bar{A}=1$, 将两个乘积项合并为一项, 并消去一个变量。例如:

$$
Y=A B C+A B \bar{C}=A B(C+\bar{C})=A B
$$

(2) 吸收法

利用公式 $A+A B=A$, 吸收多余的乘积项, 例如:

$$
Y=A \bar{C}+A \bar{B} \bar{C}+B C=A \bar{C}(1+\bar{B})+B C=A \bar{C}+B C
$$

(3) 消去法

利用公式 $A+\bar{A} B=A+B$, 消去多余的变量。例如:

$$
Y=A B+\bar{A} C+\bar{B} C=A B+(\bar{A}+\bar{B}) C=A B+\overline{A B} C=A B+C
$$

(4) 配项法

利用互补律 $B(A+\bar{A})=B$, 将某一项配成两项, 以便消去更多的乘积项。例如:

$$
\begin{aligned}
Y & =A B+\bar{A} \bar{B}+B C+\bar{B} \bar{C}=A B+\bar{A} \bar{B}(C+\bar{C})+B C(A+\bar{A})+\bar{B} \bar{C} \\
& =A B+\bar{A} \bar{B} C+\bar{A} \bar{B} \bar{C}+A B C+\bar{A} B C+\bar{B} \bar{C} \\
& =A B+\bar{B} \bar{C}+\bar{A} C
\end{aligned}
$$

用代数法化简逻辑函数的优点是简单方便, 变量数没有限制。缺点是要熟练掌握逻辑代 数的基本定律和公式以及灵活运用的技巧; 化简后的函数有时难以判断是否为最简式。

【例 3.3-6】用代数法化简逻辑函数

$$
Y=\overline{\bar{A}(B+\bar{C})}(A+\bar{B}+C)(\overline{\bar{A} \bar{B} \bar{C}})
$$

解: $Y=\overline{\bar{A}(B+\bar{C})}(A+\bar{B}+C)(\overline{\bar{A} \bar{B} \bar{C}})$

$$
\begin{aligned}
& =[A+\overline{(B+\bar{C})}](A+\bar{B}+C)(A+B+C) \\
& =[A+\bar{B} C](A+\bar{B}+C)(A+B+C) \\
& =A+\bar{B} C
\end{aligned}
$$

【例 3. 3-7】用代数法化简逻辑函数

$$
Y=A B+A \bar{C}+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D}+A D E(F+G)
$$

解: $Y=A B+A \bar{C}+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D}+A D E(F+G)$

$$
\begin{aligned}
& =A(B+\bar{C})+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D}+A D E(F+G) \\
& =A \bar{B} C+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D}+A D E(F+G) \\
& =A+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D}+A D E(F+G) \\
& =A+\bar{B} C+B \bar{C}+\bar{B} D+B \bar{D} \\
& =A+\bar{B} C(D+\bar{D})+B \bar{C}+B \bar{D}+B \bar{D}(C+\bar{C}) \\
& =A+\bar{B} C D+\bar{B} C \bar{D}+B \bar{C}+\bar{B} D+B C \bar{D}+B \bar{C} \bar{D} \\
& =A+\bar{B} D+C \bar{D}+B \bar{C}
\end{aligned}
$$

\section{2. 逻辑函数的卡诺图化简法}

(1) 卡诺图的构成

卡诺图实质上是将代表逻辑函数的最小项用小方格表示, 并将这些小方格按相邻原则排 列而成的方块图。图3.3-6 中分别画出二到四变量的卡诺图。

(2) 用卡诺图表示逻辑函数

任何一个逻辑函数都可以用最小项之和的形式来表示, 因此, 也就可以用卡诺图来表示任 意一个逻辑函数。其方法是: 首先将逻辑函数转换成最小项之和的形式, 然后在卡诺图上与这 些最小项对应的位置上填人 1 , 其余位置上填人 0 (或不填), 这就得到了表示该逻辑函数的卡 诺图。 









(3) 用卡诺图化简逻辑函数为最简与或式

由于卡诺图具有相邻性, 当相邻的两个方格为 1 时, 即可消去两个方格中不同的那个变 量。其具体化简步骤如下。

第一步,根据给定的逻辑函数,画出该逻辑函数的卡诺图。

第二步,合并最小项。即将卡诺图中相邻方格中的“ 1 ” 圈起来。画包围圈原则如下:

(1)包围圈中所包围的最小项的个数必须为 $2^{n}$ 个 $(n=1,2,3, \cdots)$;

(2)包围圈要尽量大,以便消去更多的变量因子;

(3)避免重复包围。包围圈中必须有新的变量。否则,该包围圈将是多余的。

第三步,按包围圈写出每个包围圈的函数式,然后将 这些函数式相加, 即得出简化后的逻辑函数式。

【例 3. 3-8】用卡诺图化简逻辑函数

$$
Y=\overline{A B C} D+\overline{A B} C D+\overline{A B} D+\bar{A} B \bar{D}+A C D+A \bar{B}
$$

解: 先将逻辑函数变换成最小项表达式,即

$$
\begin{aligned}
Y & =\overline{A B C} D+\overline{A B} C D+\overline{A B} D+\bar{A} B \bar{D}+A C D+A \bar{B} \\
& =\sum m(1,3,4,6,8,9,10,11,15)
\end{aligned}
$$

画出该逻辑函数的卡诺图,如图 3.3-7 所示。

画包围圈合并最小项,写出最简与或表达式为

$$
Y=A \bar{B}+\bar{A} B \bar{D}+\bar{B} D+A C D
$$



(4) 具有无关项的逻辑函数的化简

在实际逻辑电路中, 经常会遇到某些最小项的取值可以是任意的,或者这些最小项在电路 中根本不会出现, 例如 BCD 码, 用四位二进制数组成的 16 个最小项中的 10 个编码, 其余 6 个 呪余项是不会出现, 这样的最小项称为无关项。在卡诺图和真值表中用 $\phi$ 表示这些无关项。 在无关项的取值可以为 1 或 0 , 在用卡诺图化简时, 其取值应有利于得到更为简化的逻辑函数 式。

【例 3.3-9】用卡诺图化简如下逻辑函数为最简与或表达式。

$$
\begin{aligned}
& Y(A, B, C, D) \\
& =\sum m(4,6,7,8,12,13)+\sum \phi(5,9,15)
\end{aligned}
$$




解:画出卡诺图,如图 3.3-8 所示。

利用无关项进行化简,可得最简与或表达式为 $Y=\bar{A} C+B C$

画包围圈时应避免重复包围,否则将产生多余项, 图 3.3-8 中虚线所示的包围圈即为多余项。

\section{4 集成组合逻辑电路}

\subsection{1 组合逻辑电路概述}

组合逻辑电路在结构上的特点是:

(1)它单纯由各类逻辑门组成, 逻辑电路中不含存 储元件;

(2)逻辑电路的输人和输出之间没有反馈通路。

由此可以看出, 组合逻辑电路在任何时刻, 电路的输出状态仅取决于该时刻的输人状态, 而与电路前一时刻的状态无关。这样的逻辑电路称为组合逻辑电路, 简称组合电路。

\section{4 .2 组合逻辑电路的分析和设计}

\section{1. 组合逻辑电路的分析}

对一个给定的组合逻辑电路进行分析, 就是对电路进行逻辑解析, 从而确定它的逻辑功 能。其步骤如下:

(1)由给定的逻辑电路逐级写出各输出端的逻辑函数表达式, 最后得到表示输出与输人关 系的逻辑表达式;

(2)化简和变换逻辑表达式为最小项表达式;

(3)根据最小项表达式,列出真值表;

(4)由真值表分析其执行的逻辑功能;

(5)评价原设计电路,改进设计,寻找最佳设计方案。

在实际进行电路分析时, 由于电路的形式各种各样, 所以不必拘泥上述步骤, 可以略去或 颠倒其中某些步骤。

【例 3. 4-1】组合逻辑电路如图 3.4-1 所示, 试分析该电路的逻辑功能。



解: (1) 列出输出逻辑函数表达式。

$$
Y=C(A \oplus B)+A \cdot \bar{B}+C+\overline{A+B+C}
$$

(2)化简和变换逻辑表达式为最小项表达式。

$$
\begin{aligned}
Y & =C(A \oplus B)+A \cdot \bar{B}+C+\overline{A+B+C} \\
& =C(A \bar{B}+\bar{A} B)+A B \bar{C}+\bar{A} \bar{B} \bar{C} \\
& =A \bar{B} C+\bar{A} B C+A B \bar{C}+\bar{A} \bar{B} \bar{C} \\
& =\sum m(0,3,5,6)
\end{aligned}
$$

(3) 根据最小项表达式,列出真值表,如表 3.4-1 所示。

(4) 分析电路的逻辑功能: 从真值表中可以看出, 当 $A 、 B 、 C$ 三个输人变量组合中出现偶数个 “ 1 ” 时, 输出函数 $Y$ 为 “ 1 ”, 否则 为“ 0 ”, 因此该组合电路是三输人偶校验电路。

(5)评价原设计电路: 上述电路用异或门或异或非门实现,电 路比较简单。因为

$$
\begin{aligned}
Y & =A \bar{B} C+\bar{A} B C+A B \bar{C}+\bar{A} \bar{B} \bar{C} \\
& =C(A \bar{B}+\bar{A} B)+\bar{C}(A B+\bar{A} \bar{B}) \\
& =C(A \oplus B)+\bar{C} \overline{(A \oplus B)} \\
& =\overline{A \oplus B \oplus C}
\end{aligned}
$$

\section{2. 组合逻辑电路的设计}

组合逻辑电路设计是根据给出的实际逻辑问题, 经过逻辑抽象, 找出用最少的逻辑门实现 给定的逻辑功能的方案, 并画出逻辑电路图。其设计步骤如下:

(1)根据给定的逻辑问题, 对逻辑问题进行抽象, 确定因果关系, 做出输人、输出变量规定, 建立真值表;

\begin{tabular}{|c|c|c|c|}
\hline \multicolumn{3}{|c|}{ 输人变量 } & \multirow{2}{*}{$\frac{\text { 输出变量 }}{Y}$} \\
\hline A & $B$ & C & \\
\hline 0 & 0 & 0 & 0 \\
\hline 0 & 0 & 1 & 0 \\
\hline 0 & 1 & 0 & 0 \\
\hline 0 & 1 & 1 & 0 \\
\hline 1 & 0 & 0 & 0 \\
\hline 1 & 0 & 1 & 1 \\
\hline 1 & 1 & 0 & 1 \\
\hline 1 & 1 & 1 & 1 \\
\hline
\end{tabular}

(2)根据真值表写出逻辑表达式;

(3)化简或变换逻辑函数表达式;

(4)根据逻辑函数表达式画出逻辑电路图。

【例 3.4-2】试用与非门设计一个组合电路, 实现如下逻

表 3.4-2 例 3.4-2 真值表 辑功能:

只有当三个裁判(包括裁判长), 或一个裁判长和另一个裁 判确认的情况下, 才认为成功, 按下按键, 使灯亮, 否则, 表示失 败。

解: (1) 对逻辑问题进行抽象。设 $A 、 B 、 C$ 三个逻辑变量代 表三个裁判, 其中 $A$ 为裁判长。设逻辑 “ 1 ” 表示按下按键, 逻辑 “ 0 ”表示未按按键; $Y=1$ 表示成功, $Y=0$ 表示失败。

(2)列出真值表,如表 3.4-2 所示。

(3) 根据真值表写出逻辑表达式。

$$
Y=A B \bar{C}+A \bar{B} C+A B C
$$

(4) 化简或变换逻辑函数表达式。

$$
\begin{aligned}
Y & =A B \bar{C}+A \bar{B} C+A B C \\
& =A B(\bar{C}+C)+A C(\bar{B}+B) \\
& =A B+A C
\end{aligned}
$$

$$
=\overline{A B} \cdot \overline{A C}
$$

(5) 画出逻辑电路图, 如图 3. 4-2 所示。

\section{4 .3 编码器}

将二进制码按一定的规律进行编排, 使每一组代码具有 一定的含义 (如代表某一个数或符号), 这一过程称为编码。 实现编码的电路称为编码器。

\section{1. 二一十进制编码器}

二一十进制编码器的功能是将十进制的十个数字 $(0 \sim 9)$ 分别编成四位 BCD 码。以 $8421 \mathrm{BCD}$ 码为例, 该编码器有十个输人端 $\left(I_{0} \sim I_{9}\right)$ 代表十进制的十个数字, 有四个输出端 $(A$ 、 $B 、 C 、 D)$ 为二进制数, 代表四位 $\mathrm{BCD}$ 码, 其中 $A$ 为最高位, $D$ 为最低位, 如图 3.4-3 所示。



由于编码的惟一性, 即某一时刻只能对一个输人进行编码, 所以十个输人信号 $\left(I_{0} \sim I_{9}\right)$ 中, 某一时刻只能有一个输人信号为低电平 (设低电平为有效状态), 其余均为高电平。根据 逻辑电路可写出逻辑函数表达式为

$$
\begin{aligned}
& A=\overline{I_{8}}+\overline{I_{9}}=\overline{I_{8} I_{9}} \\
& B=\overline{I_{4}}+\overline{I_{5}}+\overline{I_{6}}+\overline{I_{7}}=\overline{I_{4} I_{5} I_{6} I_{7}} \\
& C=\overline{I_{2}}+\overline{I_{3}}+\overline{I_{6}}+\overline{I_{7}}=\overline{I_{2} I_{3} I_{6} I_{7}} \\
& D=\overline{I_{1}}+\overline{I_{3}}+\overline{I_{5}}+\overline{I_{7}}+\overline{I_{9}}=\overline{I_{1} I_{3} I_{5} I_{7} I_{9}}
\end{aligned}
$$

\begin{tabular}{|c|c|c|c|c|c|c|c|c|c|c|c|c|c|c|}
\hline \multirow{2}{*}{ 十进制数 } & \multicolumn{10}{|c|}{ 输 人 } & \multicolumn{4}{|c|}{ 输 出 } \\
\hline & $I_{9}$ & $I_{8}$ & $I_{7}$ & $I_{6}$ & $I_{5}$ & $I_{4}$ & $I_{3}$ & $I_{2}$ & $I_{1}$ & $I_{0}$ & $A$ & $B$ & C & $D$ \\
\hline 0 & 1 & 1 & 1 & 1 & I & 1 & 1 & 1 & 1 & 0 & 0 & 0 & 0 & 0 \\
\hline 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 0 & 0 & 0 & 1 \\
\hline 2 & 1 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 0 & 0 & 1 & 0 \\
\hline 3 & 1 & 1 & 1 & 1 & 1 & 1 & 0 & 1 & 1 & 1 & 0 & 0 & 1 & 1 \\
\hline
\end{tabular}

根据逻辑函数式, 可列出 8421 BCD 编码器的逻辑功能表, 如表 3.4-3 所示。

表 3. 4-3 8421 BCD 编码器的逻辑功能表 续表


\section{2. 二进制编码器}

【例 3.4-3】试分析如图 3.4-4 所示逻辑电路的 逻辑功能。

解: (1) 根据逻辑电路, 写出输出逻辑函数表达

$$
\begin{aligned}
& Y_{0}=\overline{\overline{I_{1}}} \cdot \overline{I_{3}} \cdot \overline{I_{5}} \cdot \overline{I_{7}} \\
& Y_{1}=\overline{\overline{I_{2}} \cdot \overline{I_{3}} \cdot \overline{I_{6}} \cdot \overline{I_{7}}} \\
& Y_{2}=\overline{\overline{I_{4}}} \cdot \overline{I_{5}} \cdot \overline{I_{6}} \cdot \overline{I_{7}}
\end{aligned}
$$

(2) 根据逻辑函数式列出逻辑功能表, 如表 3.4-4



表 3.4-4 例 3.4-3 逻辑功能表


(3) 分析逻辑功能: 从逻辑功能表可以看出, 该逻辑电路为输人低电平有效的 8-3 二进制 编码器。 

\section{4 .4 译码器和显示器}

\section{1. 译码器}

译码是编码的逆过程, 它的逻辑功能是将每一组代码的含义“翻译”出来, 即将每一组代 码译为一个特定的输出信号, 表示它原来所代表的信息。能完成译码功能的逻辑电路称为译 码器。

\section{(1) 二进制译码器}

二进制译码器原理电路如图 3.4-5 所示。

二进制译码器有 $n$ 位二进制代码输人端, $2^{n}$ 个译码输出端, 还可以有一个或多个输人使能 端。当输人使能端为有效电平时, 对应每一组的代码输人, 仅有一个与该代码相对应的输出端 为有效电平, 其他 $2^{n}-1$ 个输出端均为无效电平。










当使能端为有效电平, 即 $S_{1}=1, \overline{S_{2}}=\overline{S_{3}}=0$ 时, 根据逻辑电路可写出输出逻辑函数表达 式:

$$
\begin{aligned}
& \overline{Y_{0}}=\overline{\bar{A}_{2} \bar{A}_{1} \bar{A}_{0}}=\overline{m_{0}} ; \quad \overline{Y_{4}}=\overline{A_{2} \bar{A}_{1} \bar{A}_{0}}=\overline{m_{4}} \\
& \overline{Y_{1}}=\overline{\bar{A}_{2} \bar{A}_{1} \bar{A}_{0}}=\overline{m_{1}} ; \quad \overline{Y_{5}}=\overline{A_{2} \overline{A_{1}} A_{0}}=\overline{m_{5}} \\
& \overline{Y_{2}}=\overline{\overline{A_{2}} A_{1} \overline{A_{0}}}=\overline{m_{2}} ; \quad \overline{Y_{6}}=\overline{A_{2} A_{1} \overline{A_{0}}}=\overline{m_{6}} \\
& \overline{Y_{3}}=\overline{\overline{A_{2}} A_{1} A_{0}}=\overline{m_{3}} ; \quad \overline{Y_{7}}=\overline{A_{2} A_{1} A_{0}}=\overline{m_{7}}
\end{aligned}
$$

(2) 二一十进制译码器

二一十进制译码器的逻辑功能是将四位 BCD 码的十组代码翻译成十组高、低电平输出信 号,代表十进制数码。


根据图 3.4-7 写出译码器输出逻辑函数的逻辑表达式:

$$
\begin{aligned}
& \overline{Y_{0}}=\overline{\bar{A}_{3} \bar{A}_{2} \bar{A}_{1} \bar{A}_{0}}, \quad \overline{Y_{5}}=\overline{\overline{A_{3}} A_{2} \overline{A_{1}} A_{1}} \\
& \overline{Y_{1}}=\overline{\bar{A}_{3} \bar{A}_{2} \overline{A_{1} A_{0}}}, \quad \overline{Y_{6}}=\overline{\overline{A_{3}} A_{2} A_{1} \overline{A_{0}}}
\end{aligned}
$$





$$
\begin{array}{ll}
\overline{Y_{2}}=\overline{\bar{A}_{3} \bar{A}_{2} \bar{A}_{1} A_{0}}, & \overline{Y_{7}}=\overline{\overline{A_{3}} A_{2} A_{1} A_{0}} \\
\overline{Y_{3}}=\overline{\bar{A}_{3} \bar{A}_{2} A_{1} A_{0},} & \overline{Y_{8}}=\overline{A_{3} \bar{A}_{2} \bar{A}_{1} A_{0}} \\
\overline{Y_{4}}=\overline{\bar{A}_{3} A_{2} \bar{A}_{1} \bar{A}_{0}}, & \overline{Y_{9}}=\overline{A_{3} \bar{A}_{2} \bar{A}_{1} A_{0}}
\end{array}
$$

\section{2. 译码显示驱动器}




该电路中数码管为七段共阴极数码管,当某一段为高电平时,该端发光二极管亮。集成电 路74LS48 为七段译码驱动器, 输人 $A_{3} \sim A_{0}$ 为四位二进制代码, 译码器输出 $Y_{\mathrm{a}} \sim Y_{\mathrm{g}}$ 用来驱动发 光二极管。例如: 当输人二进制代码 $A_{3} \sim A_{0}=0011$ 时, 译码器的输出 $Y_{\mathrm{a}} \sim Y_{\mathrm{g}}=1111001$, 即 七段显示器 $a 、 b 、 c 、 d 、 g$ 段被点亮, 此时显示数字“ 3 ”。

【例 3.4-4】试用两片 3-8 译码器 74LS138 接成 4-16 译码器。

解: 由于 3 线-8 线译码器 74LS138 只有 3 个代码输人端, 而 4 线-16 线译码器应有 4 个代 码输人端, 所以,可选用控制端作为第四个代码输人端。

取片 (1) 和片 (2) 的 $S_{1}$ 作为第四个代码输人端 $A_{3}$,片 (1) 和片 (2) 的 3 个代码输人端 $A_{2}$ 、 $A_{1} 、 A_{0}$ 接在一起作为 4-16 译码器的 3 个代码输人端 $A_{2} 、 A_{1} 、 A_{0}$ 。同时, 使两片的 $\overline{S_{2}}=\overline{S_{3}}=0$, 如图 3. 4-9 所示。

电路的工作原理如下。

当 $A_{3}=0$ 时,片 (1) 工作, 而片 (2) 禁止, 将 $A_{3} A_{2} A_{1} A_{0}=0000 \sim 0111$ 这八个输人代码译成 $\overline{Y_{0}} \sim \overline{Y_{7}}$ 八个低电平信号。当 $A_{3}=1$ 时, 片 (1) 禁止, 而片 (2) 工作, 将 $A_{3} A_{2} A_{1} A_{0}=0111 \sim 1111$ 



这八个输人代码译成 $\overline{Y_{8}} \sim \overline{Y_{15}}$ 八个低电平信号。这样即实现了用两个 $3-8$ 译码器扩展成一个 4 16 译码器。

\section{4 .5 加法器}

能够完成两个数码相加的逻辑电路称为加法器。

\section{1. 半加器}

半加是实现两个一位二进制数相加的运算电路, 称为半加器。

假定两个一位二进制数 $A_{i}$ 和 $B_{i}$ 进行半加运算, 半加和为 $S_{i}$, 向高位进位用 $C_{i}$ 表示。按二 进制的加法运算规则可得到半加器的真值表, 如表 3.4-5 所示。

表 3.4-5 半加器真值表

\begin{tabular}{c|c|c|c||c|c|c|c}
\hline \multicolumn{2}{c|}{ 输 } & \multicolumn{3}{c||}{ 输 出 } & \multicolumn{2}{c|}{ 输 人 } & \multicolumn{2}{c}{ 输出 } \\
\hline$A_{i}$ & $B_{i}$ & $S_{i}$ & $C_{i}$ & $A_{i}$ & $B_{i}$ & $S_{i}$ & $C_{i}$ \\
\hline 0 & 0 & 0 & 0 & 1 & 0 & 1 & 0 \\
\hline 0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 \\
\hline
\end{tabular}

由表 3. 4-5 可写出半加器的输出逻辑表达式:

$$
\begin{aligned}
& S_{i}=A_{i} \overline{B_{i}}+\overline{A_{i}} B_{i}=A_{i} \oplus B_{i} \\
& C_{i}=A_{i} B_{i}
\end{aligned}
$$

由输出逻辑表达式可以画出半加器的逻辑电路图, 如图 3.4-10 所示。

\section{2. 全加器}

全加是指两个一位二进制数相加时, 还要考虑到来自低位的进位数的运算。实现全加运 算的逻辑电路称为全加器。

假定来自低位的进位用 $C_{\mathrm{i}-1}$ 表示, 两个一位二进制数 $A_{\mathrm{i}}$ 和 $B_{\mathrm{i}}$ 进行全加运算, 按二进制的 加法运算规则可得到全加器的真值表, 如表 3.4-6 所示。

由表 3.4-6 可写出全加器的输出逻辑函数表达式:

$$
\begin{aligned}
& S_{i}=\bar{A}_{i} \bar{B}_{i} C_{i-1}+\bar{A}_{i} B_{i} \bar{C}_{i-1}+A_{i} \bar{B}_{i} \bar{C}_{i-1} \\
& C_{i}=\bar{A}_{i} B_{i} C_{i-1}+A_{i} \bar{B}_{i} C_{i-1}+A_{i} B_{i} \bar{C}_{i-1}+A_{i} B_{i} \bar{C}_{i-1}
\end{aligned}
$$











若用半加器和门电路组成全加器的逻辑电路, 则可将上式变换为

表 3.4-6 全加器真值表

\begin{tabular}{c|c|c|c|c||c|c|c|c|c}
\hline \multicolumn{3}{|c|}{ 输 } & \multicolumn{3}{c||}{ 输 出 } & \multicolumn{3}{c|}{ 输 人 } & \multicolumn{2}{c}{ 输 出 } \\
\hline$A_{i}$ & $B_{i}$ & $C_{i-1}$ & $S_{i}$ & $C_{i}$ & $A_{i}$ & $B_{i}$ & $C_{i-1}$ & $S_{i}$ & $C_{i}$ \\
\hline 0 & 0 & 0 & 0 & 0 & 1 & 0 & 0 & 1 & 0 \\
\hline 0 & 0 & 1 & 1 & 0 & 1 & 0 & 1 & 0 & 1 \\
\hline 0 & 1 & 0 & 1 & 0 & 1 & 1 & 0 & 0 & 1 \\
\hline 0 & 1 & 1 & 0 & 1 & 1 & 1 & 1 & 1 & 1 \\
\hline
\end{tabular}

$S_{i}=A_{i} \oplus B_{i} \oplus C_{i-1}$

$C_{i}=\left(A_{i} \oplus B_{i}\right) C_{i-1}+A_{i} B_{i}$

由此逻辑函数式画出的逻辑电路图,如图 3.4-11 所示。






\section{3. 多位加法器}

由四个全加器构成的四位二进制串行进位加法器如图 3.4-12 所示。其中 $A_{3} \sim A_{0}$ 为被加 数, $B_{3} \sim B_{0}$ 为加数, $S_{3} \sim S_{0}$ 为和数, $C_{3}$ 为进位数。

\section{4 .6 数码比较器}

能完成两数进行比较的数字逻辑电路称为数码比较器。用来比较的两个数, 可以是二进 制数, 也可以是其他进制数。

\section{1. 一位数码比较器}

$A$ 和 $B$ 为一位二进制数, 进行数值比较, 比较结果有三种情况: 


(1) $A>B$, 应使比较器的输出 $Y_{(A>B)}=1$;

(2) $A=B$, 应使比较器的输出 $Y_{(A=B)}=1$;

(3) $A<B$, 应使比较器的输出 $Y_{(A<B)}=1$ 。

根据上述三种情况, 可以列出一位数码比较器的真值表, 如表 3.4-7 所示。

表 3.4-7 一位数码比较器真值表

\begin{tabular}{c|c|c|c|c}
\hline \multicolumn{2}{c|}{ 输 } & \multicolumn{3}{|c}{ 输 出 } \\
\hline$A$ & $B$ & $Y_{(A>B)}$ & $Y_{(A=B)}$ & $Y_{(A<B)}$ \\
\hline 0 & 0 & 0 & 1 & 0 \\
0 & 1 & 0 & 0 & 1 \\
1 & 0 & 1 & 0 & 0 \\
1 & 1 & 0 & 1 & 0 \\
\hline
\end{tabular}

由表 3. 4-7 可得到输出逻辑函数表达式:

$$
\begin{aligned}
& Y_{(A>B)}=A \bar{B} \\
& Y_{(A=B)}=\bar{A} \bar{B}+A B=\bar{A} B+A \bar{B} \\
& Y_{(A<B)}=\bar{A} B
\end{aligned}
$$

根据逻辑函数表达式, 可画出一位数码比较器的逻辑电路图, 如图 3.4-13 所示。





\section{2. 多位数码比较器}

常用的集成数码比较器是四位数码比较器, 如 74LS85 芯片, 其逻辑符号如图 3.4-14 所 示。该四位数码比较器是输人的四位数 $A_{3} \sim A_{0}$ 与 $B_{3} \sim B_{0}$ 进行比较, 三个输出端为 $Y_{(A>B)}$ 、 $Y_{(A=B)} 、 Y_{(A<B)}$ 。为了使比较器的功能更加完善, 使用灵活, 又增加了从低位来的比较结果的三 个输入端 $I_{(A>B)} 、 I_{(A=B)} 、 I_{(A<B)}$ 。

【例 3.4-5】 将两片四位数码比较器 74LS85 扩展成八位二进制数码比较器。

解: 对两个八位二进制数, 若高四位相等, 则它们的大小应由低四位的比较结果来确定。

$\left.Y_{L(A<B)}\right)$ 应分别连接到高四位的进位输人端 $\left(I_{(A>B)} 、 I_{(A=B)} 、 I_{(A<B)}\right)$ 。如图 3.4-15 所示。



\section{4 .7 数据选择器}

在数据传输过程中, 经常遇到需要把多路信号中的某一路信号挑选出来,能完成这一功能 的部件, 称为数据选择器 (或多路开关)。它是一种多路输人,单路输出的逻辑部件,究竟选择 耶一路输人信号,则由地址控制端决定。

八选一数据选择器74LS151 的逻辑电路图和逻辑符号如图 3.4-16 所示。由图中可以看 出, 该数据选择器有 $Y$ 和 $\bar{Y}$ 两个互补输出端, $I_{7} \sim I_{0}$ 为 8 路数据输人端, $A_{2} \sim A_{0}$ 为 3 路通道选择 政, 还有一个使能输人端 $\vec{S}$ 。







当 $\bar{S}=0$ 时, 电路处于工作状态, 选择器工作, 此时可列出它的输出逻辑表达式:

$$
Y=\bar{A}_{2} \bar{A}_{1} \bar{A}_{0} I_{0}+\bar{A}_{2} \bar{A}_{1} A_{0} I_{1}+\bar{A}_{2} A_{1} \overline{A_{0}} I_{2}+\overline{A_{2}} A_{1} A_{0} I_{3}+A_{2} \bar{A}_{1} \bar{A}_{0} I_{4}+A_{2} \overline{A_{1}} A_{0} I_{5}
$$



$$
+A_{2} A_{1} \overline{A_{0}} I_{6}+A_{2} A_{1} A_{0} I_{7}
$$

【例 3.4-6】 试用 8 选 1 数据选择器 74LS151 实现逻辑函数

$$
F(A, B, C)=\bar{A} \bar{B} \bar{C}+A \bar{C}+A B C
$$

解: (1) 将函数表达式展成最小项表达式。

$$
F(A, B, C)=\bar{A} \bar{B} \bar{C}+A \bar{C}(B+\bar{B})+A B C=m_{0}+m_{4}+m_{6}+m_{7}
$$

(2) 写出八选一数据选择器的输出逻辑函数式, 并与上述函数式进行比较, 求出对应关 系。令

$$
\begin{aligned}
& I_{0}=I_{4}=I_{6}=I_{7}=1 \\
& I_{1}=I_{2}=I_{3}=I_{5}=0
\end{aligned}
$$

根据上述逻辑函数式, 可画出逻辑电路图, 如图 3. 4-17 所示。



\section{4 .8 数据分配器}

在数据传输过程中, 完成将一路输人数据分配到多路输出端的电路称为数据分配器。它 是一种单路输人, 多路输出的逻辑部件, 究竟从哪一路输出, 则由地址控制端决定。


由逻辑图可写出数据分配器的输出逻辑函数逻辑 表达式:

$$
\begin{aligned}
& F_{0}=\overline{E \bar{A}_{1} \overline{A_{0} \bar{D}}}, F_{1}=\overline{E \overline{A_{1}} A_{0} \bar{D}} \\
& F_{2}=\overline{E A_{1} \bar{A}_{0} \bar{D}}, F_{3}=\overline{E A_{1} A_{0} \bar{D}}
\end{aligned}
$$

如当 $E=1, A_{1} A_{0}=10$ 时, $F_{2}=D$, 其他输出为 1 。其 余可以依此类推。

\section{4 .9 半导体存储器}

\section{1. 存储器分类}

半导体存储器的种类很多, 根据用户能对存储器进 行的操作分为只读存储器 (ROM) 和随机读写存储器




\section{2. 存储器的结构}

存储器电路包括地址译码器、存储矩阵和读/写控制电路。RAM 和 ROM 的结构基本一 致。地址译码器实现地址编码到字选信号的变换, 通常分为行译码和列译码。存储矩阵将存 储单元按矩阵排列, 来自译码器输出的行选信号和列选信号选通存储矩阵中的某一存储单元, 一个存储单元存放一位二进制数。读/写电路完成读出和写人的方向选择。如图 3.4-19 所示 为一个 256 字 $\times 4$ 位的存储器电路结构。




【例 3.4-7】在图 3.4-20 所示的 ROM 电路中适当的位置加画 NMOS 管, 分别实现下面组 合逻辑函数,并用三态门输出。

$$
D_{3}=\overline{A \cdot B}, D_{2}=\overline{A+B}, D_{1}=A \oplus B, D_{0}=\overline{A \oplus B}
$$

解: 这是一个用 NMOS 管反相器为基本存储单元构成的 ROM 电路, 其中, 地址信号 $A 、 B$ 作为函数输人信号, 位线信号 $S$ 控制三态门输出。 



列出实现逻辑函数的真值表, 如表 3. 4-9 所示。

表 3.4-9 例 3.4-7 真值表

\begin{tabular}{c|c|c|c|c|c}
\hline \multirow{2}{*}{$\quad B \quad$} & $D_{3}$ & $D_{2}$ & $D_{1}$ & $D_{0}$ \\
\cline { 2 - 5 } & $\overline{A B}$ & $\overline{A+B}$ & $A \oplus B$ & $\overline{A \oplus B}$ \\
\hline 0 & 0 & 1 & 1 & 0 & 1 \\
\hline 0 & 1 & 1 & 0 & 1 & 0 \\
\hline $1 \quad 0$ & 1 & 0 & 1 & 0 \\
\hline $1 \quad 1$ & 0 & 0 & 0 & 1 \\
\hline
\end{tabular}

按电路分析的要求,在适当的位线和字线交叉点的位置上加 MOS 管即可。为了方便,通 常用加黑点代替管子, 如图 3. 4-20 所示。

\subsubsection{0 可编程逻辑阵列}

可编程逻辑阵列 (Programmable Logic Array) 是由可编程逻辑与阵列和可编程逻辑或阵列 组成, 如图 3.4-21 所示。


$$
\begin{aligned}
& F_{3}=B_{1} B_{0} A_{1} A_{0} \\
& F_{2}=B_{1} \overline{B_{0}} A_{1}+B_{1} A_{1} \overline{A_{0}} \\
& F_{1}=B_{1} \overline{A_{1}} A_{0}+B_{1} \overline{B_{0}} A_{0}+\overline{B_{1}} B_{0} A_{1}+B_{0} A_{1} \overline{A_{0}} \\
& F_{0}=B_{0} A_{0}
\end{aligned}
$$

【例 3.4-8】试用 PLA 实现表 3. 4-10 所示一组多输出组合逻辑函数 $F_{1} 、 F_{2} 、 F_{3}$ 和 $F_{4}$ 。 



表 3.4-10 例 3.4-8 题表


解: 由于 PLA 的与逻辑阵列和或逻辑阵列都是可以编程的, 因此, 可先对表 3.4-10 给出的 一组逻辑函数进行化简, 然后画出 PLA 的阵列图形。

根据表 3.4-10 给出的真值表, 利用卡诺图化简可得

$$
\begin{aligned}
& F_{1}=\bar{B} D+B C+\bar{A} \bar{B} \bar{C} \\
& F_{2}=B C+\bar{A} \bar{B} \bar{C}+A B \\
& F_{3}=\bar{B} D+B C+\bar{A} \bar{B} \bar{C} \\
& F_{4}=\bar{A} \bar{C}+A C+\bar{B} \bar{C}
\end{aligned}
$$

根据逻辑表达式,画出 PLA 阵列图,如图 3. 4-22 所示。图中“.”表示存储 1 。 



\section{5 触发器}

\subsubsection{RS 触发器}

\section{1. 基本 RS 触发器}

(1) 电路组成

由与非门组成的基本 RS 触发器是由两个与非门交叉耦合而成,如图 3.5-1 (a) 所示。它 有两个输出端 $Q$ 和 $\bar{Q}$, 它们互为反变量; 两个输人端, $\overline{S_{\mathrm{D}}}$ (称为置位端或置 1 端), $\overline{R_{\mathrm{D}}}$ (称为复位 端或置 0 端)。逻辑符号如图 3.5-1 (b) 所示。







(2) 工作原理

当 $\overline{S_{\mathrm{D}}}=0, \overline{R_{\mathrm{D}}}=1$ 时, $Q^{n+1}=1, \overline{Q^{n+1}}=0$, 电路处于 1 状态。

当 $\overline{S_{\mathrm{D}}}=1, \overline{R_{\mathrm{D}}}=0$ 时, $Q^{n+1}=0, \overline{Q^{n+1}}=1$, 电路处于 0 状态。

当 $\overline{S_{\mathrm{D}}}=1, \overline{R_{\mathrm{D}}}=1$ 时,电路保持原状态不变。

当 $\overline{S_{\mathrm{D}}}=0, \overline{R_{\mathrm{D}}}=0$ 时, 电路的输出状态是无法确定的。因此, 这种情况是不允许出现的, 即 约束条件为: $\overline{R_{\mathrm{D}}}+\overline{S_{\mathrm{D}}}=1$ 。

(3) 逻辑功能的描述

根据上述工作过程可列出功能表 (特性表) 来表示逻辑功能, 其功能表如表 3.5-1 所示。 表 3.5-1 用与非门组成的基本 RS 触发器的功能表



根据功能表可画出基本 RS 触发器 $Q^{n+1}$ 的卡诺图, 如图 3.5-2 所示。 化简后可得出该触发器的逻辑功能函数表达式(特征方程):

$$
\left\{\begin{array}{l}
Q^{n+1}=S_{\mathrm{D}}+\overline{R_{\mathrm{D}}} Q^{\mathrm{n}} \\
\overline{S_{\mathrm{D}}}+\overline{R_{\mathrm{D}}}=1
\end{array}\right.
$$





根据状态表或特征方程可以画出状态转 资图,如图 3. 5-3 所示。

根据状态表或特征方程还可以画出基本 RS 触发器在输人信号作用下, 输出信号随时 间变化的时序波形图(简称时序图), 如图 3.54 所示。

\section{2. 同步 RS 触发器}

\section{(1) 电路组成}

该电路由两部分组成: 与非门 $G_{1}, G_{2}$ 组成 基本 RS 触发器; 与非门 $G_{3} 、 G_{4}$ 组成输人控制 电路, 如图 3.5-5 (a) 所示。逻辑符号如图 3.5-



\section{(2) 工作原理}

当 $C P=0$ 时, $\mathrm{G}_{3} 、 \mathrm{G}_{4}$ 截止,输人信号 $R 、 S$ 不会影响输出状态,故触发器保持原状态不变。 






当 $C P=1$ 时, $R 、 S$ 信号通过 $G_{3} 、 G_{4}$ 反相加到由 $G_{1} 、 G_{2}$ 组成的基本 $R S$ 触发器上, 使 $Q$ 和 $\bar{Q}$ 的状态随输人状态而改变。它的功能表如表 3.5-2 所示。

表 3.5-2 同步 RS 触发器的功能表


从功能表可以看出, 只有当 $C P=1$ 时触发器输出的状态才受输人信号控制, 而且在 $C P=$ 1 时的功能与基本 RS 触发器相同, 其约束条件为 $R 、 S$ 不能同时为 1 , 即 $S R=0$ 。

(3) 逻辑功能的描述 来描述。

同步 RS 触发器的功能除用上述的功能表描述外, 还可用特征方程、状态转换图、时序图

根据功能表可写出逻辑函数式并化简,即可得出特征方程:

$$
\left\{\begin{array}{l}
Q^{n+1}=S+\bar{R} Q^{n} \\
S R=0 \quad \text { (约束条件). }
\end{array}\right.
$$

根据状态表或特征方程可以画出状态转换图,如图 3.5-6 所示。

在 $C P 、 S 、 R$ 输人信号作用下输出的时序波形图如图 3.5-7 所示。 





\section{3. 主从 RS 触发器}

(1) 电路组成

主从 RS 触发器是由两个同步 RS 触发器组成, 如图 3.5-8(a) 所示。与非门 $G_{1} \sim G_{4}$ 组成 的同步 RS 触发器称主触发器; 与非门 $G_{5} \sim G_{8}$ 组成的同步 RS 触发器称从触发器, 非门 $G_{9}$ 使主 从触发器的时钟脉冲互相反相。输出端为 $Q$ 和 $\bar{Q}$, 输人端为 $S 、 R$ 。逻辑符号如图 3.5-8(b) 所 示。






(2) 工作原理

$C P=1$ 时为接收阶段, 与非门 $\mathrm{G}_{1} 、 \mathrm{G}_{2}$ 开通, $\mathrm{G}_{5} 、 \mathrm{G}_{6}$ 被封锁, 故主触发器的输出状态由 $S 、 R$ 来确定, 从触发器的输出状态不变。

$C P$ 下降沿来到后, $C P=0$, 与非门 $G_{1} 、 G_{2}$ 封锁, $\mathrm{G}_{5} 、 \mathrm{G}_{6}$ 开通, 故主触发器的输出状态不变, 从触发器的输出状态由主触发器的输出 $S_{1} 、 R_{1}$ 来确定。

(3) 逻辑功能的描述

主从 RS 触发器的逻辑功能与同步 RS 触发器相同, 但要注意它输出状态是在时钟脉冲的 下降沿改变。

【例 3.5-1】试画出主从 RS 触发器在输人如图 3.5-9 所示的 $S 、 R$ 信号作用下, 输出端 $Q$ 



\section{的波形 (设触发器的初态为 0 )。}

解: 在 $C P=1$ 时,与非门 $\mathrm{G}_{1} 、 \mathrm{G}_{2}$ 开通,将输人的 $S 、 R$ 信号保存在主触发器的 $Q_{m}$ 和 $\overline{Q_{m}}$ 中, 由于 $\mathrm{G}_{5}$ 、 $\mathrm{G}_{6}$ 被封锁, 故从触发器的输出状态不变; 在 $C P=0$ 时, $G_{1} 、 G_{2}$ 封锁, $G_{5} 、 G_{6}$ 开通, 将主触发器的 $Q_{m}$ 和 $\overline{Q_{m}}$ 状态传送到从触发器。其输出波形如图 3. 5-9 所示。

\section{5 .2 D 触发器}

\section{1. 同步 D 触发器}

(1) 电路组成

在同步 RS 触发器的输人 $S$ 和 $R$ 之间接一非门, 输人信号只从 $S$ 端输人, 并改称 $S$ 端为 $D$ 端, 这种触发器又称为 D 锁存器, 如图 3.5-10(a) 所示。它的逻辑符号如图 3.5-10(b) 所示。






\section{(2) 工作原理}

当 $C P=0$ 时, 由于控制门被封锁, 触发器的状态保持不变。

当 $C P=1$ 时, 控制门被打开, 若 $D=1$, 则 $S=1, R=0$, 故 $Q^{n+1}=1$; 若 $D=0$, 则 $S=0, R=1$, 故 $Q^{n+1}=0$ 。

(3) 逻辑功能的描述

根据上述工作状况可列出功能表, 如表 3.5-3 所示。

表 3.5-3 D 触发器功能表

\begin{tabular}{c|c|c|c|c}
\hline$C P$ & $D$ & $Q^{n}$ & $Q^{n+1}$ & 功能 \\
\hline 0 & 0 & 0 & 0 & \multirow{2}{*}{ 不变 } \\
\hline 0 & 1 & 1 & 1 & \multirow{2}{*}{ 同 $D$ 端 } \\
\hline 1 & 0 & 0 & 0 & 1 \\
\hline
\end{tabular}

特性方程:

$$
Q^{n+1}=D
$$

状态转换图如图 3.5-11 所示。





【例 3.5-2】试画出同步 D 触发器在输人如图 3.5-12 所示的 $D$ 信号作用下, 输出端 $Q$ 和 $\bar{Q}$ 的波形 (设触发器的初态为 0 )。

解: 根据 $\mathrm{D}$ 触发器的逻辑功能和输人信号, 可画出其输出 $Q$ 和 $\bar{Q}$ 的波形, 如图 3.5-12 所 示。

\section{2. 维持阻塞 D 触发器}

(1) 电路组成

它是由六个与非门组成的正边沿触发器, 如图 3.5-13 所示。



\section{(2) 工作原理}

$C P=0$ 时,输人信号被 $G_{3} 、 G_{4}$ 封锁,输出状态保持不变。这时 $G_{1} 、 G_{2}$ 根据输人的 $D$ 信号 做好准备。

$C P$ 的上升沿来到时, 触发器的状态即根据准备好的信号发生翻转。

维持阻塞 D 触发器的逻辑功能与同步 D 触发器相同。

【例 3.5-3】已知维持阻塞 D 触发器输人 $C P$ 和 $D$ 信号的波形, 如图 3.5-14 所示, 设触发 器的初态为 0 , 试画出输出端 $Q$ 的波形。

解: 维持阻塞 D 触发器的输出只决定于 $C P$ 上升沿到来前瞬间 $D$ 的状态变化, 而与原 来状态无关。其输出波形如图 3. 5-14 所示。



\section{5 .3 主从 JK 触发器}

\section{1. 电路组成}

在主从 RS 触发器的基础上加上两条反馈线, 得到如图 3.5-15(a) 所示的主从 JK 触发器。 逻辑符号如图 3.5-15(b) 所示。







利用 $Q$ 和 $Q$ 不能同时为 “ 1 ” 的特点, 将它们交叉反馈到输人门 $G_{1} 、 G_{2}$, 从而避免 $C P=1$ 时, 触发器输出状态可能出现不定的现象, 这样对输人信号 $S 、 R$ 无约束条件。为了与主从 RS 触发器相区别, 将输人 $S$ 端改用 $J$ 表示, 输人 $R$ 端改用 $K$ 表示, 故称主从 $J K$ 触发器。

\section{2. 工作原理}

若 $J=1, K=0, Q^{n}=0$, 则 $C P=1$ 时主触发器置 $1, C P$ 下降沿来到后, $C P=0$, 从触发器随之 置 1 , 即 $Q^{n+1}=1$; 若 $J=1, K=0, Q^{n}=1$, 则 $C P=1$ 时主触发器保持不变, $C P$ 下降沿来到后, $C P$ $=0$, 从触发器输出保持不变, 即 $Q^{n+1}=1$ 。

若 $J=0, K=1, Q^{n}=0$, 则 $C P=1$ 时主触发器保持不变。 $C P$ 下降沿来到后, $C P=0$, 从触发 器输出保持不变, 即 $Q^{n+1}=0$; 若 $J=0, K=1, Q^{n}=1$, 则 $C P=1$ 时主触发器置 $0, C P$ 下降沿来到 后, $C P=0$, 从触发器随之置 0 , 即 $Q^{n+1}=0$ 。

若 $J=0, K=0$, 与非门 $\mathrm{G}_{1} 、 \mathrm{G}_{2}$ 被封锁, 则 $C P=1$ 时主触发器保持不变。 $C P$ 下降沿来到后, $C P=0$, 从触发器输出保持不变, 即 $Q^{n+1}=Q^{n}$ 。

若 $J=1, K=1, Q^{n}=0$, 则 $C P=1$ 时主触发器置 $1, C P$ 下降沿来到后, $C P=0$, 从触发器随之 置 1 , 即 $Q^{n+1}=1$; 若 $J=1, K=1, Q^{n}=1$, 则 $C P=1$ 时主触发器置 $0, C P$ 下降沿来到后, $C P=0$, 从触发器随之置 0 , 即 $Q^{n+1}=0$, 因此, 可表示为: $Q^{n+1}=\overline{Q^{n}}$ 。在这种情况下触发器将翻转为与 原态相反的状态。该特点称为触发器的计数翻转功能。

\section{3. 逻辑功能的描述}

根据上述分析可列出其功能表如表 3.5-4 所示。 表 3.5-4 JK 触发器功能表


根据功能表可写出状态方程 (特征方程):

$$
Q^{n+1}=J \overline{Q^{n}}+\bar{K} Q^{n}
$$

状态转换图如图 3.5-16 所示。





【例 3.5-4】主从 JK 触发器的输人 $C P 、 J 、 K$ 波形如图 3.5-17 所示, 试画出输出 $Q$ 和 $\bar{Q}$ 的 波形。设触发器的初始状态为“ 0 ”态。

解: 输出 $Q$ 和 $\bar{Q}$ 的波形如图 3.5-17 所示。

\subsubsection{T 触发器}

$\mathrm{T}$ 触发器是受控计数型触发器, 它是逻辑设计中使用较多的一种触发器, 但一般不生产这 样的产品, 它多由 JK 触发器或 D 触发器转换得到。

其逻辑功能如表 3.5-5 所示。

表 3.5-5 T 触发器功能表

\begin{tabular}{c|c|c|c}
\hline$T$ & $Q^{n}$ & $Q^{n+1}$ & 说明 \\
\hline 0 & 0 & 0 & $Q^{n+1}=Q^{n}$ 保持 \\
0 & 1 & 1 & $Q^{n+1}=\overline{Q^{n}}$ 翻转 \\
\hline 1 & 0 & 1 & 0 \\
\hline
\end{tabular}

根据功能表可写出 $\mathrm{T}$ 触发器的特征方程:

$$
Q^{n+1}=\bar{T} Q^{n}+T \overline{Q^{n}}
$$

【例 3.5-5】由 $\mathrm{D}$ 触发器组成的 $\mathrm{T}$ 触发器如图 3.5-18 所示, 试画出在 $T 、 C P$ 信号作用下, 输出 $Q$ 端的波形。设触发器的初始状态为“ 0 ”态。





解: 根据 $\mathrm{T}$ 触发器的特性方程, 可画出波形如图 3.5-19 所示。

\section{5 .5 触发器时钟脉冲的触发方式}

对于不同电路结构的触发器, 可以实现相同的逻辑功能, 但其动态特点是不同的, 反应到 逻辑符号上,时钟的触发方式是不同的。即逻辑符号的 $C P$ 脉冲输人端上不带小三角的为电 平触发, 带小三角的为脉冲边沿触发, 不带小圈的为时钟脉冲的高电平或上升沿触发, 带小圈 的为时钟脉冲的低电平或下降沿触发。因此, 在画时序图时应注意时钟脉冲的触发方式。

现以 JK 触发器为例, 画出各种触发方式的逻辑符号, 如图 3.5-20 所示。










【例 3.5-6】 试分别画出图 3.5-20(c)、(d) 触发器在图 3.5-21 所示 $J 、 K$ 信号作用下, $Q$ 端的输出波形 (设动态为“ “ 0 ”。

解: 根据 JK 触发器的逻辑功能和输入的信号, 并考虑到图 (c) 为上升沿触发, 图 (d) 为下 降沿触发, 可画出 $Q$ 端的输出波形如图 3.5-21 所示。





\subsection{6 触发器逻辑功能的转换}

\section{D 触发器转换为 $T$ 触发器}

$\mathrm{T}$ 触发器的特征方程为

$$
Q^{n+1}=\bar{T} Q^{n}+T \overline{Q^{n}}
$$

$\mathrm{D}$ 触发器的特征方程为

$$
Q^{n+1}=D
$$

将两个方程相比,可得

$$
D=\bar{T} Q^{n}+T \overline{Q^{n}}
$$

根据此式可画出逻辑电路图, 如图 3.5-22 所示。

\section{JK 触发器转换为 $\mathrm{D}$ 触发器}

$J \mathrm{~K}$ 触发器的特征方程为

$$
Q^{n+1}=J \overline{Q^{n}}+\bar{K} Q^{n}
$$

$\mathrm{D}$ 触发器的特征方程为

$$
Q^{n+1}=D
$$

转换时, 可将 D 触发器的特征方程变换成 JK 触发器特征方程相似的形式, 即

$$
Q^{n+1}=D=D\left(\overline{Q^{n}}+Q^{n}\right)=D \overline{Q^{n}}+D Q^{n}=J \overline{Q^{n}}+\bar{K} Q^{n}
$$

可见, 若取 $J=D, K=\bar{D}$, 则可画出逻辑电路图, 如图 3.5-23 所示。



D 触发器的逻辑图



【例 3.5-7】试画出由 D 触发器转换成 JK 触发器的逻辑电路图。

解:已知 $\mathrm{D}$ 触发器的特征方程为

$$
Q^{n+1}=D
$$

$\mathrm{JK}$ 触发器的特征方程为

$$
Q^{n+1}=J \overline{Q^{n}}+\bar{K} Q^{n}
$$

则可得

$$
D=J \bar{Q}^{n}+\bar{K} Q^{n}
$$

根据此式可画出逻辑电路图如图 3.5-24 所示。

\subsubsection{CMOS 触发器}

CMOS 触发器具有功耗低、集成度高、抗干扰能力强和成本低等优点。这类触发器一般都 是主从结构, 产品有 D 和 JK 两种类型。

\section{CMOS D 触发器}

CMOS D 触发器如图 3.5-25 所示。它是由主触发器和从触发器两部分构成的主从结构。 


主能发器
从能发器






当 $C P=0, \overline{C P}=1$ 时, 传输门 $\mathrm{TG}_{1}$ 开通, $\mathrm{TG}_{2}$ 关闭, 主触发器开通, 但因 $\mathrm{TG}_{2}$ 关闭而失去自 锁作用, $G_{1} 、 G_{2}$ 变成两个串连的非门, 输人 $D$ 信号即经过两次反相后存在主触发器中, 此时, $D$ 信号若发生变化, 主触发的输出状态也发生相应变化, 因此, 它不存在一次变化现象。同时, 传 输门 $\mathrm{TG}_{3}$ 关闭、 $\mathrm{TG}_{4}$ 开通, 使从触发器和主触发器之间断开, 故从触发器自锁, 保持原来状态不 变。

当 $C P$ 上升沿到来时, 传输门 $\mathrm{TG}_{1}$ 关闭, $\mathrm{TG}_{2}$ 开通, 使主触发器建立自锁, 保持 $C P$ 上升沿 到来之前的 $D$ 信号。同时, $\mathrm{TG}_{3}$ 开通, $\mathrm{TG}_{4}$ 关闭, 从触发器失去自锁作用, 使从触发器的输出状 态随主触发器的输出状态而变化。即电路的输出状态在 $C P$ 上升沿到来时 $Q^{n+1}=D$ 。

\section{CMOS JK 触发器}

CMOS JK 触发器是在 CMOS D 触发器的输入端增加一个组合电路, $J 、 K$ 输人端信号经组 合电路送到 D 触发器, 如图 3.5-26 所示。







根据电路可写出:

$$
Q^{n+1}=D=\overline{J+Q}+\overline{K Q}=(J+Q) \overline{K Q}=(J+Q)(\bar{K}+\bar{Q})=J \bar{Q}+\bar{K} Q
$$

从而得出该电路实现 JK 触发器的逻辑功能。 

\section{6 时序逻辑电路}

\subsection{1 时序逻辑电路的特点及组成}

\section{1. 时序逻辑电路的特点}

时序逻辑电路任何时刻的输出不仅取决于该时刻的输入, 还与电路原来的状态有关, 这是 由时序电路的结构决定的。

\section{2. 时序逻辑电路的组成}

时序逻辑电路是由组合逻辑电路和存储电路两部 分组成, 如图 3.6-1 所示。


$$
\begin{array}{ll}
Z=F_{1}\left(X, Q^{n}\right) & \text { 输出方程 } \\
Y=F_{2}\left(X, Q^{n}\right) & \text { 驱动方程 } \\
Q^{n+1}=F_{3}\left(Y, Q^{n}\right) & \text { 状态方程 }
\end{array}
$$



\section{3. 时序逻辑电路逻辑功能的描述}

描述时序逻辑电路逻辑功能的方法有驱动方程、状态方程和输出方程。但从这一组方程 式还不能获得电路逻辑功能的完整印象, 因此, 描述时序电路转换全过程的方法还有状态转换 表、状态转换图和时序图。

\subsection{2 时序逻辑电路的分析方法}

时序逻辑电路的分析是根据给定的逻辑电路图, 通过分析, 找到电路输出状态 $Q$ 端的变 化规律及外部输出 $Z$ 的变化规律。

由于时序逻辑电路有同步和异步之分, 因此, 其分析也分为同步电路分析和异步电路分 析。时序逻辑电路一般分析步骤如下:

(1)分析电路的组成;

(2) 确定输出方程和驱动方程;

(3)写出存储器的状态方程 (分析异步时序电路时应考虑时钟脉冲的作用)；

(4)列出状态转换真值表和状态表;

(5)画出状态转换图;

(6)电路逻辑功能的描述。

【例 3.6-1】 分析图 3.6-2 所示时序逻辑电路的逻辑功能。

解: (1) 分析电路的组成。该电路的组合电路是一个与门, 存储电路是两级 $\mathrm{T}$ 触发器, 每 个触发器的 $C P$ 端都接在一起,共同接受输人时钟,所以是一个同步时序逻辑电路。

(2) 确定输出方程和驱动方程。分别为

$$
\begin{aligned}
& T_{1}=X \\
& T_{2}=X Q_{1}
\end{aligned}
$$





$$
Z=X Q_{1} Q_{2}
$$

(3) 写出存储器的状态方程。

$$
\begin{aligned}
& Q_{1}^{n+1}=X \overline{Q_{1}^{n}}+\bar{X} Q_{1}^{n}=X \oplus Q_{1}^{n} \\
& Q_{2}^{n+1}=X Q_{1}^{n} \overline{Q_{2}^{n}}+\overline{X Q_{1}^{n}} Q_{2}^{n}=X Q_{1}^{n} \oplus Q_{2}^{n}
\end{aligned}
$$

(4)列出状态转换真值表和状态表。设定外部输人和初态, 求出次态, 列出真值表, 如表 3. 6-1 所示。

表 3. 6-1 例 3. 6-1 状态转换真值表

\begin{tabular}{|c|c|c|c|c|c|}
\hline \multirow{3}{*}{$Q_{\mathrm{i}}^{\pi}$} & \multirow{3}{*}{$Q_{2}^{n}$} & \multirow{2}{*}{\multicolumn{4}{|c|}{$\frac{Q_{2}^{n+1} Q_{1}^{n+1} / Z}{X}$}} \\
\hline & & & & & \\
\hline & & & 0 & & 1 \\
\hline 0 & 0 & 0 & $0 / 0$ & 0 & $1 / 0$ \\
\hline 0 & 1 & 0 & $1 / 0$ & 1 & $0 / 0$ \\
\hline 1 & 0 & 1 & $0 / 0$ & 1 & $1 / 0$ \\
\hline 1 & 1 & 1 & $1 / 0$ & 0 & $0 / 1$ \\
\hline
\end{tabular}

\begin{tabular}{c|c|c|c|c|c|c|c}
\hline$X$ & $Q_{2}^{n}$ & $Q_{1}^{n}$ & $T_{2}$ & $T_{1}$ & $Q_{2}^{n+1}$ & $Q_{1}^{n+1}$ & $Z$ \\
\hline 0 & 0 & 0 & 0 & 0 & 0 & 0 & 0 \\
\hline 0 & 0 & 1 & 0 & 0 & 0 & 1 & 0 \\
\hline 0 & 1 & 0 & 0 & 0 & 1 & 0 & 0 \\
\hline 0 & 1 & 1 & 0 & 0 & 1 & 1 & 0 \\
\hline 1 & 0 & 0 & 0 & 1 & 0 & 1 & 0 \\
\hline 1 & 0 & 1 & 1 & 1 & 1 & 0 & 0 \\
\hline 1 & 1 & 0 & 0 & 1 & 1 & 1 & 0 \\
\hline 1 & 1 & 1 & 1 & 1 & 0 & 0 & 1 \\
\hline
\end{tabular}

表 3.6-2 例 3.6-1 状态转换表

由表 3.6-1 可以列出更为简单和直观的状态转换表,如表 3.6-2 所示。



(5) 画出状态转换图。状态表虽然可以描述电路的状 态转换和逻辑功能, 但不直观, 所以, 通常采用状态图来更 直观地描述逻辑功能。假设电路现态 $Q_{2} Q_{1}$ 为 $00,01,10$ 和 11 , 分别用 $S_{0}, S_{1}, S_{3}$ 和 $S_{4}$ 表示, 可以画出状态转换图 3.63 。

(6) 电路逻辑功能的描述。从状态转换图可以看出: 当 $X=0$ 时, 状态维持不变; 当 $X=1$ 时, 状态发生转换。假如, $X$ 固定取值为 1 , 并预置电路在 $S_{0}$ 状态, 那么, 随着 $C P$ 的作 用, 状态将按照 $S_{0} \rightarrow S_{1} \rightarrow S_{2} \rightarrow S_{3} \rightarrow$ 循环转换, 并且每输人

四个脉冲作用后输出一个进位脉冲, 故此电路逻辑功能是可控模 4 加法计数器。

【例 3.6-2】分析图 3.6-4 所示时序逻辑电路的逻辑功能。

解: (1) 分析电路的组成。该电路是由三个 $\mathrm{JK}$ 触发器组成的时序电路, 且 $C P$ 端都接在一 



起,共同接受输人时钟, $C P$ 端带有小圈,故是下降沿触发的同步时序逻辑电路。

(2) 确定驱动方程。

$$
\begin{aligned}
& J_{1}=\overline{Q_{3}^{n}}, K_{1}=1 \\
& J_{2}=K_{2}=Q_{1}^{n} \\
& J_{3}=Q_{1}^{n} Q_{2}^{n}, K_{3}=1
\end{aligned}
$$

(3) 写出存储器的状态方程。

$$
\begin{aligned}
& Q_{1}^{n+1}=J_{1} \overline{Q_{1}^{n}}+\overline{K_{11}} Q_{1}^{n}=\overline{Q_{3}^{n}} \cdot \overline{Q_{1}^{n}} \\
& Q_{2}^{n+1}=J_{2} \overline{Q_{2}^{n}}+\overline{K_{21}} Q_{2}^{n}=Q_{1}^{n} \overline{Q_{2}^{n}}+\overline{Q_{1}^{n}} Q_{2}^{n} \\
& Q_{3}^{n+1}=J_{3} \overline{Q_{3}^{n}}+\overline{K_{31}} Q_{3}^{n}=Q_{1}^{n} Q_{2}^{n} \overline{Q_{3}^{n}}
\end{aligned}
$$

(4) 列出状态转换真值表。设定初态,求出次态,列出真值表,如表 3.6-3 所示。

(5) 画出状态转换图。根据状态转换表, 可以画出状态转换图, 如图 3.6-5 所示。

表 3.6-3 例 3.6-2 状态转换表



$Q_{3}$


\begin{tabular}{c|c|c|c}
\hline$C P$ 脉种序列 & $Q_{3}$ & $Q_{2}$ & $Q_{1}$ \\
\hline 0 & 0 & 0 & 0 \\
\hline 1 & 0 & 0 & 1 \\
\hline 2 & 0 & 1 & 0 \\
\hline 3 & 0 & 1 & 1 \\
\hline 4 & 1 & 0 & 0 \\
\hline 5 & 0 & 0 & 0 \\
\hline
\end{tabular}

(6) 电路逻辑功能的描述。从状态转换图的分 析可以看出, 它具有 5 个状态构成一个闭合的环形, 即每经过 5 个时钟脉冲电路循环变化一次, 而且变 化的规律是 $000 、 001 、 010 、 011 、 100 、 000$ 依次循环, 所以该电路是一个同步五进制加法计数器。

(7) 时序波形图。图3.6-6 画出了在 $C P$ 脉冲作 用下的 $Q_{3} Q_{2} Q_{1}$ 的输出波形。 

\section{6 .3 计数器}

\section{1. 计数器的基本概念}

所谓 “计数”, 就是计算时钟脉冲的个数。计数器的应用十分广泛, 不仅用来计数, 也可用 做分频、定时等。

\section{2. 计数器的分类}

计数器可从以下几个方面进行分类。

(1) 按计数脉冲引入方式

按计数脉冲引人方式分为同步计数器和异步计数器。

(2) 按计数器中数码的变化规律

按计数器中数码的变化规律分为加法计数器、减法计数器和可逆计数器。

(3) 按计数体制

按计数体制分为二进制计数器、十进制计数器和任意进制 (也称 $N$ 进制, 即除二进制、十 进制之外的其他进制) 计数器。

\section{3. 异步二进制计数器分析}

【例 3.6-3】由 JK 触发器组成的时序逻辑电路如图 3.6-7 所示, 试分析该电路的逻辑功 能。



解: (1) 分析电路的组成。该电路是由四个下降沿触发的 JK 触发器组成的电路。每个触 发器的 $J 、 K$ 端都悬空, 即相当接高电平 “ 1 ”, 所以, 它构成计数型触发器; 且输人 $C P$ 脉冲是加 到第一级触发器计数脉冲输人端, 第一级的 $Q$ 端输出作为第二级的计数脉冲输人, 依此类推, 所以该电路是异步时序逻辑电路。

(2) 确定电路的状态方程。由于该电路是异步时序电路, 各触发器的时钟脉冲不是同时 到达, 故在列出状态方程时应将时钟脉冲作为变量考虑进去。状态方程为



$Q_{1} \square \cdot \square \square \square$


$Q_{3}$


$$
\begin{aligned}
& Q_{0}^{n+1}=\overline{Q_{0}^{n}} C P_{0} \downarrow=\overline{Q_{0}^{n}} C P \downarrow \\
& Q_{1}^{n+1}=\overline{Q_{1}^{n}} C P_{1} \downarrow=\overline{Q_{1}^{n}} Q_{0}^{n} \downarrow \\
& Q_{2}^{n+2}=\overline{Q_{2}^{n}} C P_{2} \downarrow=\overline{Q_{2}^{n}} Q_{1}^{n} \downarrow \\
& Q_{3}^{n+1}=\overline{Q_{3}^{n}} C P_{3} \downarrow=\overline{Q_{3}^{n}} Q_{2}^{n} \downarrow
\end{aligned}
$$

(3) 根据状态方程可以画出时序波形图, 如图 3.68 所示。

(4) 逻辑功能描述。该电路是一个异步四位二进 制加法计数器。

【例 3.6-4】 由 D 触发器组成的时序逻辑电路如图 3.6-9 所示, 试分析该电路的逻辑功 



解: (1) 分析电路的组成。该电路是由四个上升沿触发的 D 触发器组成的电路, 其中每个 D触发器都接成计数型触发器。

(2) 确定状态方程。

$$
\begin{aligned}
& Q_{0}^{n+1}=D_{0}=\overline{Q_{0}^{n}} C P_{0} \downarrow=\overline{Q_{0}^{n}} C P \uparrow \\
& Q_{1}^{n+1}=D_{1}=\overline{Q_{1}^{n}} C P_{1} \uparrow=\overline{Q_{1}^{n}} Q_{0}^{n} \uparrow \\
& Q_{2}^{n+1}=D_{2}=\overline{Q_{2}^{n}} C P_{2} \uparrow=\overline{Q_{2}^{n}} Q_{1}^{n} \uparrow \\
& Q_{3}^{n+1}=D_{3}=\overline{Q_{3}^{n}} C P_{3} \uparrow=\overline{Q_{3}^{n}} Q_{2}^{n} \uparrow
\end{aligned}
$$

$Q_{1}$

(3) 根据状态方程可以画出时序波形图, 如图 3.610 所示。

(4) 逻辑功能描述。该电路是一个异步四位二进 制减法计数器。

$Q_{3}$


\section{4. 同步二进制计数器分析}

【例 3.6-5】 由 JK 触发器组成的同步时序逻辑电路如图 3.6-11 所示, 试分析该电路的逻 踶功能。



解: (1) 分析电路的组成: 该 电路由于 $C P$ 端接在一起, 同时接 受时钟脉冲, 所以它是一个同步 时序逻辑电路。

(2) 确定驱动方程:

$$
\begin{aligned}
& J_{3}=K_{3}=Q_{2}^{n} Q_{1}^{n} Q_{0}^{n} \\
& J_{2}=K_{2}=Q_{1}^{n} Q_{0}^{n} \\
& J_{1}=K_{1}=Q_{0}^{n} \\
& J_{0}=K_{0}=1
\end{aligned}
$$

(3) 写出存储器的状态方程:

$$
\begin{aligned}
& Q_{3}^{n+1}=Q_{2}^{n} Q_{1}^{n} Q_{0}^{n} \overline{Q_{3}^{n}}+\overline{Q_{2}^{n} Q_{1}^{n} Q_{0}^{n}} Q_{3}^{n} \\
& Q_{2}^{n+1}=Q_{1}^{n} Q_{0}^{n} \overline{Q_{2}^{n}}+\overline{Q_{1}^{n} Q_{0}^{n} Q_{2}^{n}} \\
& Q_{1}^{n+1}=\overline{Q_{0}^{n}} \overline{Q_{1}^{n}}+\overline{Q_{0}^{n}} Q_{1}^{n} \\
& Q_{0}^{n+1}=\overline{Q_{0}^{n}} \\
& C=Q_{3}^{n} Q_{2}^{n} Q_{1}^{n} Q_{0}^{n}
\end{aligned}
$$

(4)列出状态转换真值表: 设定初态,求出次态,列出真值表,如表 3.6-4 所示。 表 3.6-4 例 3.6-5 状态转换表


(5)画出状态转换图: 如图 3.6-12 所示。



(6) 电路逻辑功能的描述: 从状态转换表或状态转换图可以看出该电路是一个四位二进 制加法计数器。 $C$ 为进位信号。

(7) 时序波形图: 如图 3.6-13 所示。

\section{6 .4 寄存器}

能够存放二值代码的部件叫寄存器。

构成寄存器的核心器件是触发器。 


一个触发器只能存储一位二值代码, 所以, $n$ 位寄存器实际上就是受同一时钟脉冲控制的 $n$ 个触发器。

寄存器又分为数码寄存器和移位寄存器。移位寄存器又分为左移移位寄存器、右移移位 奇存器和双向移位寄存器。

\section{1. 数码寄存器}

由 $\mathrm{D}$ 触发器构成的四位数码寄存器如图 3.6-14 所示。D 触发器的逻辑功能是: 在 $C P=1$ 时, $Q$ 端的状态随 $D$ 端的信号变化。 $D_{3} \sim D_{0}$ 为数据输人端, 在 $C P=1$ 时, $Q_{3} \sim Q_{0}$ 的状态即随 $D_{3} \sim D_{0}$ 输人的数据而改变, $C P$ 变为低电平时, $Q$ 端的状态保持不变, 即将数码寄存起来。



为增加使用的灵活性,有些寄存器还增加一些控制电路, 如图 3.6-15 所示。该电路是采 用负边沿触发的 $\mathrm{D}$ 触发器, 且具有清零端输人。当 $\bar{R}_{\mathrm{D}}=0$ 时, 四个触发器被清零; 在 $\bar{R}_{\mathrm{D}}=1$, $C P$ 的上升沿来到时, 经反相器加到触发器的 $C P$ 端, 使触发器的输出 $Q$ 端发生相应的变化, 即 将数码寄存起来。



\section{2. 移位寄存器}

移位寄存器除了具有存储代码的功能外, 还具有移位的功能。所谓移位, 是指寄存器里存 储的代码能在移位脉冲的作用下依次左移或右移。因此, 移位寄存器不仅可以用于寄存代码, 还可以实现数据的串行一并行转换数值的运算和数据的处理等。






其工作过程如下。设输入四位数码 $A_{3} A_{2} A_{1} A_{0}$, 数码是从 $D_{0}$ 端串行输人, 先将 $A_{3}$ 送到 $D_{0}$ 端, 在第一个 $C P$ 脉冲的下降沿到来 后, $Q_{0}=A_{3}$; 再将 $A_{2}$ 送到 $D_{0}$ 端，在第二个 $C P$ 脉冲的下降沿到来 后, $Q_{0}=A_{2}, Q_{1}=A_{3}$; 然后将数码 $A_{1}$ 送到 $D_{0}$ 端, 在第三个 $C P$ 脉冲 的下降沿到来后, $Q_{0}=A_{1}, Q_{1}=A_{2}, Q_{2}=A_{3}$; 最后将数码 $A_{0}$ 送到 $D_{0}$ 端, 在第四个 $C P$ 脉冲的下降沿到来后, $Q_{0}=A_{0}, Q_{1}=A_{1}, Q_{2}=$ $A_{2}, Q_{3}=A_{3}$ 。图3.6-17 画出了在 $A_{3} A_{2} A_{1} A_{0}=1011$ 时, 各输出 $Q$ 端的波形。

从波形图中可以看出,数据从 $D_{0}$ 端输人, 从 $Q_{3}$ 端输出, 此时 是串行输出, 它是一个左移的移位寄存器。亦可同时由 $Q_{3} Q_{2} Q_{1}$ $Q_{0}$ 同时输出,即并行输出。

\subsection{5 序列信号发生器}

产生二进制序列信号的逻辑电路称为序列信号发生器。它的功能是产生一组或多组二进 制序列信号。序列信号发生器在雷达、通信、遥控和遥测、测量以及无线电仪表等领域中得到 广泛的应用。例如, 在通信设备中要产生一组规则码, 用来调试或检修设备; 又如通信系统中 的同步就需要产生一组特定的二进制序列信号来表示一组信息的开始或终止。

序列信号发生器通常可以在寄存器或计数器的基础上构成, 前者通常只产生一组序列信 号,后者可以产生一组或多组序列信号。

\section{1. 寄存器型序列信号发生器}

寄存器型序列信号发生器的框图如图 3.6-18 所示。反馈电路的作用是检测移位寄存器 的现态, 产生 0 或 1 的输出, 输至移位寄存器以便得到相应状态, 使电路输出给定的序列信号。

【例 3.6-6】寄存器型序列信号发生器如图 3.6-19 所示, 试分析该电路的逻辑功能。

解: (1) 该电路是由三个 D 触发器构成的移位寄存器和由门电路组成的反馈电路组成的 序列脉冲产生电路。

(2) 电路的驱动方程和状态方程为

$$
D_{3}=Q_{2}^{n}=Q_{3}^{n+1}
$$





信号发生器框图



$$
\begin{aligned}
& D_{2}=Q_{1}^{n}=Q_{2}^{n+1} \\
& D_{1}=\bar{Q}_{2}^{n} \bar{Q}_{3}^{n}+\overline{Q_{3}^{n}} Q_{1}^{n}+\overline{Q_{1}^{n}} Q_{2}^{n} Q_{3}^{n}=Q_{1}^{n+1}
\end{aligned}
$$

(3)列出状态转换表, 如表 3.6-5 所示。

表 3. 6-5 例 3.6-6 状态转换表

\begin{tabular}{c|c|c|c|c|c|c}
\hline$Q_{3}^{n}$ & $Q_{2}^{n}$ & $Q_{1}^{n}$ & $Q_{3}^{n+1}$ & $Q_{2}^{n+1}$ & $Q_{1}^{n+1}$ & $D_{1}$ \\
\hline 0 & 0 & 0 & 0 & 0 & 1 & 1 \\
\hline 0 & 0 & 1 & 0 & 1 & 1 & 1 \\
\hline 0 & 1 & 1 & 1 & 1 & 1 & 1 \\
\hline 1 & 1 & 1 & 1 & 1 & 0 & 0 \\
\hline 1 & 1 & 0 & 1 & 0 & 0 & 1 \\
\hline 1 & 0 & 1 & 0 & 1 & 0 & 0 \\
\hline 0 & 1 & 0 & 1 & 0 & 0 & 0 \\
\hline
\end{tabular}

(4) 从状态转换表可以看出, 该电路无论从 $Q_{1}$ 输出, 还是从 $Q_{2} 、 Q_{3}$ 输出, 都可产生一序列 脉冲,其脉冲序列为 00011101 , 所以它的逻辑功能是一个 00011101 序列信号发生器。

(5)画出它的状态转换图,如图 3.6-20 所示。





\section{2. 计数器型序列信号发生器}

计数器构成的序列信号发生器的框图如图 3.6-21 所示。它是由周期为 $M$ 的计数器和组 合电路组成。组合电路的输出可以是周期为 $M$ 的一组, 也可以是周期为 $M$ 的多组序列信号。 【例 3.6-7】计数器型序列信号发生器如图 3.6-22 所示, 试分析该电路的逻辑功能。



解: (1) 该电路是由四位二进制计数器 74LS193 构成的模为 11 的加法计数器和门电路构 成的组合电路组成的计数器型序列信号发生器。

(2) 输出逻辑函数表达式为

$$
F=\overline{Q_{A}} Q_{B}+Q_{B} Q_{C}+\overline{Q_{A}} Q_{D}
$$

(3) 由于计数器是先预置数为 0100 , 故计数为从 $0100 \sim 1111$ 进行加计数。可列出状态转 换表,如表 3.6-6 所示。

表 3.6-6 例 3. 6-7 状态转换表

\begin{tabular}{c|c|c|c|c|c}
\hline$C P$ & $Q_{0}$ & $Q_{C}$ & $Q_{B}$ & $Q_{A}$ & $F$ \\
\hline 0 & 0 & 1 & 0 & 0 & 0 \\
\hline 1 & 0 & 1 & 0 & 1 & 0 \\
\hline 2 & 0 & 1 & 1 & 0 & 1 \\
\hline 3 & 0 & 1 & 1 & 1 & 1 \\
\hline 4 & 1 & 0 & 0 & 0 & 1 \\
\hline 5 & 1 & 0 & 0 & 1 & 0 \\
\hline 6 & 1 & 0 & 1 & 0 & 1 \\
\hline 7 & 1 & 0 & 1 & 1 & 0 \\
\hline 8 & 1 & 1 & 0 & 0 & 1 \\
\hline 9 & 1 & 1 & 0 & 1 & 1 \\
\hline 10 & 1 & 1 & 1 & 0 & 1 \\
\hline 11 & 1 & 1 & 1 & 1 & 0 \\
\hline
\end{tabular}

(4) 从状态真值表可以看出, 在 $C P$ 脉冲的作用下, 输出端 $F$ 依次输出一系列脉冲 001110101011 , 所以该电路为序列脉冲发生器。

\section{7 脉冲波形的产生}

\subsection{1 多谐振荡器}

多谐振荡器是一种自激振荡器, 它没有稳定的状态, 不需要外加信号, 只要接通电源, 就能 产生矩形脉冲信号。由于矩形波有丰富的谐波分量, 故常称这种振荡器为多谐振荡器。它主 要作为信号源来应用。

\section{1. 环形多谐振荡器}

它是利用闭合回路中的正反馈作用产生自激振荡的。由于门电路存在传输延迟时间, 将 奇数个门首尾相接,即可构成环形多谐振荡器。其原理图如图 3.7-1(a)所示。







若 $u_{\mathrm{o}}$ 为高电平, 经三级门倒相后, $u_{\mathrm{o}}$ 跳转为低电平。若门电路的平均传输延迟时间为 $t_{\mathrm{pd}}$,


用这种方法构成的振荡器很简单, 但不实用。因为门电路的传输延迟时间极短, 输出信号 的频率很高, 而且不能调节。为此, 通常采用外加 $R C$ 延迟电路来改进环形多谐振荡器。

\section{2. $R C$ 环形多谐振荡器}

(1) 电路组成

它是由三个非门 $G_{1} 、 G_{2} 、 G_{3}$ 、两个电阻 $\left(R_{1} 、 R\right)$ 和一个电容 $C$ 组成, 如图 3.7-2 所示。电阻 $R_{1}$ 是非门 $G_{3}$ 的限流保护电阻,一般在 $100 \Omega$ 左右; $R 、 C$ 为定时器件, $R$ 的值要小于门的关门电 阻,一般在 $700 \Omega$ 以下, 否则电路无法工作。由于 $R C$ 的值足够大, 传输时间增大, 门延迟时间 $t_{\mathrm{pd}}$ 可以忽略不计。



(2) 工作原理

设初始时 $\mathrm{A}$ 点电位为低电平, $\mathrm{G}_{1}$ 关闭, 输出 $u_{\mathrm{o} 1}$ 为高电平。它一方面使 $\mathrm{G}_{2}$ 开通, 输出 $u_{\mathrm{o} 2}$ 为 低电平; 另一方面通过电容 $C$ 的耦合使 B 点和 $\mathrm{D}$ 点的电位 $u_{\mathrm{B}} 、 u_{\mathrm{D}}$ 均为高电平, 导致 $\mathrm{G}_{3}$ 开通, 输 出 $u_{03}$ 为低电平。由于 $u_{03}$ 的低电平通过反馈线反馈到 $G_{1}$ 的输入端, 稳定在低电平, 所以能保持 一段时间不变。

但它是一个暂稳态, 因为 $u_{02}$ 为低电平, $u_{01}$ 通过 $R$ 对电容 $C$ 充电, 使 $\mathrm{B}$ 点电位 $u_{\mathrm{B}}$ 逐渐下降, $u_{\mathrm{D}}$ 也随之下降。当 $u_{\mathrm{D}}$ 降到 $\mathrm{G}_{3}$ 的关门电平时, $\mathrm{G}_{3}$ 关闭, 输出 $u_{03}$ 为高电平。电路转入另一个暂稳 态, 这是因为 $u_{03}$ 为高电平后, 由反馈线使 $\mathrm{G}_{1}$ 门开通, 输出 $u_{01}$ 转为低电平, $\mathrm{G}_{2}$ 关闭, 输出 $u_{\mathrm{o} 2}$ 为高 电平, 电容 $C$ 被反向充电, 使 $u_{\mathrm{B}}$ 逐渐上升, 当 $u_{\mathrm{B}}$ 达到 $\mathrm{G}_{3}$ 的开门电平时, $\mathrm{G}_{3}$ 开通, 电路恢复到第 一暂稳态, 如此周而复始, 反复翻转, 便形成了多谐振荡, 输出矩形波。

\section{(3) 输出脉冲周期}

输出脉冲的周期 $T$ 由电容 $C$ 的充电 $\left(t_{\mathrm{W} 1}\right)$ 和放电 $\left(t_{\mathrm{W} 2}\right)$ 两部分组成, 其中

$$
\begin{aligned}
& t_{\mathrm{w}_{1}} \approx 1.1 R C \\
& t_{\mathrm{w}_{2}} \approx 1.2 R C
\end{aligned}
$$

振荡周期

$$
T=t_{\mathrm{W} 1}+t_{\mathrm{w} 2} \approx 2.3 R C
$$

【例 3.7-1】用奇数个与非门组成的环形多谐振荡器如图 3.7-3 所示。

(1) 设每个门的平均传输时间为 $t_{\mathrm{pd}}$, 试求振荡频率的计算公式。

(2) 若每级门的平均传输时间为 $\iota_{\mathrm{pd}}=20 \mathrm{~ns}$, 要想获得频率 $f=5 \mathrm{MHz}$ 的振荡波形, 试问需 多少个门?



解: (1) 每级门的传输时间为 $t_{\mathrm{pd}}, n$ 级门的传输时间为 $n t_{\mathrm{pd}}$, 则可得振荡周期为 振荡频率为

$$
T=2 n t_{\mathrm{pd}}
$$

$$
f=\frac{1}{2 n t_{\mathrm{pd}}}
$$

(2) 根据 $f=\frac{1}{2 n t_{\mathrm{pdt}}}$, 可求出

$$
n=\frac{1}{2 f t_{\mathrm{pd}}}=\frac{1}{2 \times 5 \times 10^{6} \times 20 \times 10^{-9}}=5
$$

【例 3.7-2】 $R C$ 环形多谐振荡器电路如图 3.7-2 所示。

若电路中 $R=510 \Omega, C=0.01 \mu \mathrm{F}$, 试求振荡频率。

解: 根据 $R C$ 环形多谐振荡器的振荡周期 $T \approx 2.3 R C$, 可得出

$$
f=\frac{1}{T}=\frac{1}{2.3 R C}=\frac{1}{2.3 \times 510 \times 0.01 \times 10^{-6}}=85 \mathrm{kHz}
$$

\section{7 .2 单稳态触发器}

单稳态触发器具有稳态和暂稳态两个不同的工作状态, 在外界触发信号作用下, 能从稳态 副转到暂稳态,维持一段时间以后,再自动返回到稳态,暂稳态维持时间的长短取决于电路的 参数, 而与外界触发信号的宽度和幅度无关。

这种电路被广泛应用于脉冲整形、延时以及定时电路中。

\section{1. 微分型单稳态触发器}

微分型单稳态触发器如图 3.7-4 (a) 所示。其中, $G_{1}$ 和 $G_{2}$ 为两级正反馈连接的与非门, $R$ 和 $C$ 组成延时电路, 它们按微分电路的连接方式接在 $G_{1}$ 门的输出端和 $\mathrm{G}_{2}$ 门的输人端之间。 $C_{\mathrm{i}}$ 和 $R_{i}$ 组成触发输人电路,把触发信号微分成尖脉冲,如图 3.7-4(b) 所示。

电路的工作过程如下。





（a）电路图（b) 波形图

\section{(1) $0 \sim t_{1}$ 稳定状态}

门 $G_{1}$ 和 $G_{2}$ 的输人端都接有一个电阻, 其值的选择可决定 $G_{1}$ 和 $G_{2}$ 的输出, 所以, 选择 $R<$ $R_{\mathrm{off}}$, 使 $u_{R}$ 约为 $0.5 \mathrm{~V}$,门 $\mathrm{G}_{2}$ 输出为高电平, 它反馈到 $\mathrm{G}_{1}$ 门的输人, 若选 $R_{\mathrm{i}}>R_{\mathrm{on}}, u_{\mathrm{r}}$ 被钳位在 1.4 $V$, 门 $G_{1}$ 输出为低电平, 触发器为稳定状态, 此时, $u_{\mathrm{o} 1}=$ “ 0 ”, $u_{\mathrm{o} 2}=$ “ 1 ”, 电容 $C$ 上的电压约为 -0.2

\section{(2) $t_{1} \sim t_{2}$ 暂稳态}

当 $u_{i}$ 出现下降沿时, 经 $R_{i} 、 C_{i}$ 微分电路得到负尖脉冲, 使 $u_{\text {ol }}$ 上跳至高电平, 由于电容 $C$ 电 压不能突变, 故 $u_{R}$ 也变为高电平, 使 $u_{\mathrm{o} 2}$ 变为低电平, 电路发生翻转, 从而进人暂稳态。随着电 容器 $C$ 的充电, $u_{R}$ 也逐渐降低, 当达到 $\mathrm{G}_{2}$ 门的关门电平时, $\mathrm{G}_{2}$ 门关闭, $u_{\mathrm{o} 2}$ 变为高电平, $u_{\mathrm{o} 1}$ 变为 低电平, 电路自动返回到初始稳定状态。暂稳态的持续时间决定于定时电路 $R C$ 的充电速度。 (3) $t>t_{2}$ 恢复期

电路自动翻转后, 电容两端的电压要恢复到初始状态时需要一定的时间, 一般取

$$
t_{\mathrm{R}}=(3 \sim 5) \tau_{\mathrm{d}}=(3 \sim 5) R C
$$

(4) 参数计算

该单稳态触发器可产生一定宽度的负脉冲, 其输出脉冲宽度为

$$
t_{\mathrm{w}} \approx 0.7 R C
$$

一般采用改变电容的大小实现脉冲宽度的粗调,用改变电阻的大小来实现脉冲宽度的微 调。

电路的最高工作频率为

$$
f_{\max }=\frac{1}{t_{\mathrm{w}}+t_{\mathrm{R}}}
$$

【例 3.7-3】微分型单稳态触发器如图 3.7-4(a) 所示。电路参数如图中标出的数值, 试 求: 电路的输出脉冲宽度; 电路的最高工作频率。

解: 输出脉冲宽度为

$t_{\mathrm{w}}=0.7 R C=0.7 \times 390 \times 0.01 \times 10^{-6}=2.73 \mu \mathrm{s}$

最高工作频率的计算

$$
\begin{aligned}
& t_{\mathrm{R}}=(3 \sim 5) \tau_{\mathrm{d}}=(3 \sim 5) R C=4 R C=4 \times 390 \times 0.01 \times 10^{-6}=15.6 \mu \mathrm{s} \\
& f_{\max }=\frac{1}{t_{\mathrm{W}}+t_{\mathrm{R}}}=\frac{1}{2.73+15.6}=0.05 \mathrm{MHz}
\end{aligned}
$$

\section{2. 积分型单稳态触发器}

积分型单稳态触发器如图 3.7-5 (a) 所示。图中 $R C$ 为积分定时电路。

其工作波形如图 3.7-5(b) 所示。电路工作过程如下。




在正触发脉冲作用之前, $u_{\mathrm{i}}$ 为低电平, 门 $\mathrm{G}_{1}$ 和 $\mathrm{G}_{2}$ 均处于关闭状态, 它们的输出 $u_{\mathrm{o} 1}$ 和 $u_{\mathrm{o} 2}$ 均 为高电平, 电路处于稳定状态。此时 $R$ 上无电流流过, 电容 $C$ 上充有恒定电压 $\left(u_{C}=3.6 \mathrm{~V}\right)$ 。 在 $t=t_{1}$ 瞬间, $u_{i}$ 正跳变, 由于电容 $C$ 两端电压不能突变, $u_{C}$ 仍为高电平, 因而, 门 $\mathrm{G}_{1}$ 和 $\mathrm{G}_{2}$ 同 时开通, $u_{\mathrm{o} 1}$ 和 $u_{\mathrm{o} 2}$ 立即由高电平跳变到低电平, 电路发生翻转, 进人到暂稳态。

当 $u_{\mathrm{o} 1}$ 由高电平变为低电平后, 已充电的电容 $C$ 就要通过 $R$ 和 $G_{1}$ 门进行放电, 使 $u_{C}$ 按指数 䡇律下降。当 $t=t_{2}, u_{C}$ 下降到 $G_{2}$ 门的关门电平时, $G_{2}$ 门关闭, $u_{o 2}$ 由低电平变为高电平, 暂稳态 结束。但此时电容 $C$ 仍继续放电。

新充电, 充电时间常数 $\tau_{C}=\left(R_{0}+R\right) C_{\text {。 }}$ 经过 $(3 \sim 5) \tau_{C}$ 时间后, 电路才返回到初始稳态。

输出脉冲宽度为

$$
t_{\mathrm{W}}=R C \ln \left(\frac{U_{\mathrm{OH}}}{U_{\mathrm{T}}}\right)
$$

式中: $U_{\mathrm{oH}}$ 为 TTL 门的输出高电平值; $U_{\mathrm{T}}$ 为 TTL门的阈值电压。

由上面分析可以看出, 这种单稳态触发器要求正触发脉冲的宽度 $\iota_{W_{i}}$ 必须大于输出脉冲宽 度 $t_{W}$, 否则, 电路将不能正常工作。

【例 3.7-4】 积分型单稳态触发器如图 3.7-5 (a) 所示。电路参数如图中标出的数值, 门 $G_{1} 、 G_{2}$ 的阈值电压 $U_{\mathrm{T}}=1.4 \mathrm{~V}$, 输出高电平 $U_{\mathrm{oH}}=3.6 \mathrm{~V}$ 。

试求: 电路的输出脉冲宽度; 输人触发脉冲宽度 $\iota_{\mathrm{wi}}=0.5 \mu \mathrm{s}$ 时电路是否能正常工作?

解: 输出脉冲宽度为

$$
t_{\mathrm{W}}=R C \ln \left(\frac{U_{\mathrm{oH}}}{U_{\mathrm{T}}}\right)=200 \times 5000 \times 10^{-12} \ln \frac{3.6}{1.4}=0.94 \mu \mathrm{s}
$$

当输入触发脉冲的宽度 $t_{\mathrm{Wi}}=0.5 \mu \mathrm{s}$ 时, 由于 $t_{\mathrm{Wi}}<t_{\mathrm{w}}$, 所以, 电路不能正常工作。

\section{7 .3 施密特触发器}

施密特触发器是脉冲波形变换经常使用的一种电路。输出有两个稳定状态。该电路有两 个重要特点:一是输出状态依赖于电路输人信号的电平; 二是能改善输出波形, 使输出电压波 形的边沿变得很陡。

\section{1. 电路图}




\section{2. 工作原理}

设输人 $u_{i}$ 为三角波, 如图 3.7-7 (a) 所示。设 $G_{1} 、 G_{2} 、 G_{3}$ 的门坎电平为 $U_{\mathrm{T}}$ 。

当 $u_{\mathrm{i}}$ 高于 $U_{\mathrm{T}}$ 时, $\mathrm{G}_{3}$ 开通, 使 $\overline{R_{\mathrm{D}}}=0, \mathrm{D}$ 截止, 则 $\overline{S_{\mathrm{D}}}=1, u_{\mathrm{ol}}=1, u_{\mathrm{o} 2}=0$, 电路处于第一稳态, $Q$ $=0$ 。

只有当 $u_{\mathrm{i}}$ 下降到 $u_{\mathrm{i}}=U^{-}=U_{\mathrm{T}}-U_{\mathrm{D}}$ 时, $\overline{R_{\mathrm{D}}}=1, \mathrm{D}$ 导通, $\overline{S_{\mathrm{D}}}=0$, 电路才发生翻转到第二稳 态, $Q=1$ 。

当 $u_{\mathrm{i}}$ 再升高时, 只有当升高到 $u_{\mathrm{i}}=U^{*}=U_{T}$ 时, $\mathrm{G}_{3}$ 开通, D 截止, $\overline{R_{\mathrm{D}}}=0, \overline{S_{\mathrm{D}}}=1, u_{\mathrm{ol}}=1, u_{\mathrm{o} 2}$ $=0$, 电路又返回到第一稳态。图 3.7-7 (b)、(c) 给出了相应的 $u_{\mathrm{o} 1}$ 与 $u_{\mathrm{o} 2}$ 波形。










\section{3. 回差特性}

通过上述分析可以看出, 在输人电压下降过程中, 电路由第一稳态翻转到第二稳态所要求 的输人电压 $u_{i}=U^{-}$, 与输人电压上升过程中电路从第二稳态回到第一稳态所要求的输入电压 $u_{i}=U^{+}$是不同的。这种现象称为回差现象, 如图 3.7-8 所示。 $U^{+}$称为正向阈值电压, $U^{-}$称为 负向阈值电压, 电路的回差电压 $\Delta U=U^{+}-U^{-}$。

\section{4. 施密特触发器的应用}

(1)用于波形变换;

(2)用于脉冲整形;

(3)用于脉冲的幅度鉴别。



【例 3.7-5】图 3.7-9 所示的施密特电路中, 与非门 $\mathrm{G}_{1} 、 \mathrm{G}_{2}$ 的阈值电压 $U_{\mathrm{T}}=1.1 \mathrm{~V}$, 二极管的导通压降 $U_{\mathrm{D}}=0.7$ $\mathrm{V}, R_{\mathrm{t}}=1 \mathrm{k} \Omega, R_{2}=2 \mathrm{k} \Omega$, 试计算正向阈值电压 $U^{+}$、负向國 值电压 $U^{-}$和电路的回差电压 $\Delta U$ 。

解: 当输人电压 $u_{\mathrm{i}}=0$ 时, $\mathrm{G}_{1}$ 门关闭, $\mathrm{G}_{2}$ 门开通, 输出 $u_{\mathrm{o}}$ 为低电平。

当输人电压 $u_{\mathrm{i}}$ 升高, 达到 $\mathrm{G}_{1}$ 门的开门电平时, $\mathrm{G}_{1}$ 门开通, 欲使 $\mathrm{G}_{1}$ 门开通则要求:

$$
\frac{u_{\mathrm{i}}-0.7-u_{\mathrm{o}}}{R_{1}+R_{2}} \times R_{2}+u_{\mathrm{o}}=U_{\mathrm{T}}
$$

将给定数值代人, 即

$$
\frac{u_{\mathrm{i}}-0.7-0.3}{1+2} \times 2+0.3=1.1 \mathrm{~V}
$$

可求出正向阈值电压

$$
u_{\mathrm{i}}=U^{+}=2.2 \mathrm{~V}
$$

负向國值电压

$$
U^{-}=1.1 \mathrm{~V}
$$

电路的回差电压

$$
\Delta U=2.2-1.1=1.1 \mathrm{~V}
$$

\section{8 数模 $(\mathrm{D} / \mathrm{A})$ 和模数 $(\mathrm{A} / \mathrm{D})$ 转换}

\section{8 .1 数模转换器 ( D/A 转换器)}




$D_{3} \sim D_{0}$ 表示四位二进制数字输人信号, $D_{3}$ 为高位, $D_{0}$ 为低位。 $\mathrm{S}_{3} \sim \mathrm{S}_{0}$ 是四个电子模拟开 关, 当某一位数 $D_{i}=1$, 即表示 $\mathrm{S}_{i}$ 接 1 , 这时相应的电流 $I_{i}$ 流向 $I_{01}$, 当 $D_{i}=0$, 即表示 $\mathrm{S}_{i}$ 接 0 , 则 流过相应电阻的电流 $I_{i}$ 流向 $I_{02}$ 到地。因此, 运算放大器的输人电流 $I_{01}$ 由下式决定:

$$
\begin{aligned}
I_{01} & =I_{3} D_{3}+I_{2} D_{2}+I_{1} D_{1}+I_{0} D_{0} \\
& =\frac{U_{\mathrm{REF}}}{2 R} D_{3}+\frac{1 U_{\mathrm{REF}}}{2 R} D_{2}+\frac{1 U_{\mathrm{REF}}}{2^{2} 2 R} D_{1}+\frac{1 U_{\mathrm{REF}}}{2^{3} 2 R} D_{0} \\
& =\frac{U_{\mathrm{REF}}}{2^{4} R}\left(D_{3} 2^{3}+D_{2} 2^{2}+D_{1} 2^{1}+D_{0} 2^{0}\right)
\end{aligned}
$$


$$
U_{\mathrm{o}}=-I_{01} R_{\mathrm{f}}=-\frac{U_{\mathrm{REF}} R_{\mathrm{f}}}{2^{4} R}\left(D_{3} 2^{3}+D_{2} 2^{2}+D_{1} 2^{1}+D^{0} 2^{0}\right)
$$

即输出的模拟电压与输人的数字信号 $D_{3} \sim D_{0}$ 的状态以及位权成正比。

若取电阻 $R_{\mathrm{f}}=R$, 且电阻网络由 $N$ 级组成, 则 $\mathrm{D} / \mathrm{A}$ 转换后的输出电压表示为

$$
U=-\frac{U_{\text {REF }}}{2^{n}}\left(D_{n-1} 2^{n-1}+D_{n-2} 2^{n-2}+\cdots+D_{1} 2^{1}+D_{0} 2^{0}\right)
$$

数模 $(\mathrm{D} / \mathrm{A})$ 转换器的主要参数如下。

\section{(1) 分辨率}

分辨率是指对输出最小电压的分辩能力。它用输人数妈只有最低有效位为 1 时的输出电 压与输人数码全为 1 时输出满量程电压之比表示, 即

分辦率 $=\frac{1}{2^{n}-1}$

(2) 绝对误差 (绝对精度)

绝对误差是指当输人数码为全 1 时, 所对应实际输出电压与电路理论值之差。

(3) 转换速度

转换速度是指从送人数字信号起, 到输出电流或电压达到稳态值所需要的时间。

【例 3.8-1】四位 $R-2 R$ 的 $\mathrm{T}$ 形网络 $\mathrm{D} / \mathrm{A}$ 转换器, 如图 3.8-1 所示电路, 试求: 参考电压 $U_{\mathrm{REF}}=8 \mathrm{~V}$, 数字量输人 $D_{3} D_{2} D_{1} D_{0}=1001$ 时的输出电压。

解: $U_{\mathrm{o}}=-I_{01} R_{\mathrm{f}}=-\frac{U_{\mathrm{REF}}}{2^{4}}\left(D_{3} 2^{3}+D_{2} 2^{2}+D_{1} 2^{1}+D_{0} 2^{0}\right)$

$$
=-\frac{8}{2^{4}}\left(1 \times 2^{3}+0 \times 2^{2}+0 \times 2^{1}+1 \times 2^{0}\right)=-4.5 \mathrm{~V}
$$

【例 3.8-2】某 8 位 $\mathrm{D} / \mathrm{A}$ 转换器, 满度输出电压为 $8 \mathrm{~V}$, 那么, 它的 $1 \mathrm{LSB}$ 对应电压值是多 少?

解: $\frac{8}{2^{8}-1}=0.031 \mathrm{~V}$

\section{8 .2 模数转换器 ( $\mathrm{A} / \mathrm{D}$ 转换器)}

\section{1. 逐次逼近式模数转换器}

逐次逼近式模数转换器是由比较器、D/A 转换器、数码寄存器和控制逻辑电路等组成, 如 图 3. 8-2 所示。



转换开始前, 先将数码寄存器清零, 所以, 给 $\mathrm{D} / \mathrm{A}$ 转换器 DAC 的数字量也全是零。当发 出转换控制信号后, 通过逻辑控制电路, 首先使寄存器的输出最高位置 1 , 这个数字量被送到 $\mathrm{D} / \mathrm{A}$ 转换器, 转换成相应的模拟电压 $U_{i}$, 并送到比较器与输人信号 $U_{i}$ 进行比较, 如果 $U_{i}>U_{i}$, 说明数字过大, 去掉这个 “ 1 ”; 如果 $U_{\mathrm{f}}<U_{\mathrm{i}}$, 说明数字不够大, 保留这个 “ 1 ”。接着, 寄存器的次 高位置“1”,按上述方法确定这个“ 1 ”是否保留,逐位比较下去,直到最低位比较完为止。这时 寄存器所存的数码就是所求的数字量。

【例 3.8-3】一个 8 位二进制输出的逐次逼近型 $\mathrm{A} / \mathrm{D}$ 转换器中, 若 $U_{\mathrm{REF}}=5 \mathrm{~V}, U_{\mathrm{i}}=4.22$ $\mathrm{V}$, 试问输出是多少? 若其他条件不变, 仅将 $\mathrm{A} / \mathrm{D}$ 转换器换成 10 位, 那么输出是多少?

解: 输人 $U_{\mathrm{i}}=4.22 \mathrm{~V}$ 时, 对应的输出数字量为 11010111 。

若将 $A / D$ 转换器换成 10 位, 则输出数字量为 1101011111 。

\section{2. 双积分型模数转换器}

双积分 A/D 转换器原理电路如图 3. 8-3 所示。它是由积分器、比较器、计数器、控制逻辑 电路和时钟信号源等几部分组成。



其工作过程分三个阶段进行。

(1) 初始准备

转换控制信号 $U_{\mathrm{L}}=0$, 计数器清零, 开关 $\mathrm{S}$ 闭合, 使电容 $C$ 完全放电。

(2) 第一次积分 (采样阶段)

转换控制信号 $U_{\mathrm{L}}=1$, 通过控制逻辑电路使 $\mathrm{S}$ 断开, 开关 $\mathrm{S}_{1}$ 接到模拟输人 $U_{\mathrm{i}}$ 上, 积分器开 始对 $U_{i}$ 积分。当积分到 $T_{1}$ 时刻, 采样阶段结束, 此时, 积分器的输出电压为

$$
U_{\mathrm{o}}=-\frac{1}{R C} \int_{0}^{T_{1}} u_{\mathrm{i}} \mathrm{d} t=-\frac{T_{1}}{R C} U_{\mathrm{i}}
$$

式中: $T_{1}$ 为采样时间, $T_{1}=N T_{C P} ; N$ 为脉冲数; $T_{C P}$ 为时钟脉冲的周期。

此时, 控制逻辑输出使 $\mathrm{S}_{1}$ 开关置于 $-U_{\mathrm{REF}}$, 电路进人比较阶段。 

\section{(3) 第二次积分 (比较阶段)}

此时积分器反向积分, 当积分器输出电压上升到零时, 积分过程结束, 设这段时间为 $T_{2}$, 则积分输出电压为

$$
\begin{aligned}
& U_{\mathrm{o}}=\frac{1}{C} \int_{0}^{T_{2}} \frac{U_{\mathrm{REF}}}{R} \mathrm{~d} t-\frac{T_{1}}{R C} U_{\mathrm{i}}=0 \\
& \frac{T_{2}}{R C} U_{\text {REF }}=\frac{T_{1}}{R C} U_{\mathrm{i}}
\end{aligned}
$$

所以

$$
T_{2}=\frac{T_{1}}{U_{\text {REF }}} U_{\mathrm{i}}
$$

从而可以看出, 反向积分到 $U_{\mathrm{o}}=0$ 的这段时间 $T_{2}$ 与输人信号 $U_{\mathrm{i}}$ 成正比, 被转换电压 $U_{\mathrm{i}}$ 越大, $U_{\mathrm{o}}$ 数值越大, $T_{2}$ 时间越长。令计数器在 $T_{2}$ 时间里对固定频率为 $f_{C P}\left(f_{C P}=\frac{1}{T_{C P}}\right)$ 的时钟脉 冲计数为 $D$, 则

取 $T_{1}=N T_{C P}$, 则

$$
D=\frac{T_{2}}{T_{C P}}=\frac{T_{1}}{T_{C P} U_{\mathrm{REF}}} U_{\mathrm{i}}
$$

$$
D=\frac{U_{\mathrm{i}}}{U_{\mathrm{REF}}} N
$$

被转换电压 $U_{i}$ 的大小转换为计数脉冲值 $D$, 即数字量大小。而 $N$ 为采样积分的时钟脉冲数, 它是一个常数。其工作波形如图 3.8-4 所示。



【例 3.8-4】一个双积分 $A / D$ 转换器的计数器为四位十进制计数器, 设最大容量为 (3000) $)_{10}$, 计数器的时钟频率 $f_{\text {cp }}=400 \mathrm{kHz}$, 求:

(1) 若参考电压 $U_{\mathrm{REF}}=15 \mathrm{~V}$, 当输出为 $(1000)_{10}$ 时, 输人模拟电压是多少?

(2) 转换器的最小工作周期是多少?

解: (1) 输人模拟量

$$
U_{i}=\frac{1000}{3000} \times 15=5 \mathrm{~V}
$$

(2) 采样时间

$$
T_{1}=N T_{C P}=3000 \times \frac{1}{400 \times 10^{3}}=7.5 \mathrm{~ms}
$$

比较时间

$$
T_{2}=\frac{T_{1}}{U_{\text {REF }}} \times U_{i}=\frac{7.5}{15} \times 5=2.5 \mathrm{~ms}
$$

最小工作周期

$$
T=T_{1}+T_{2}=7.5+2.5=10 \mathrm{~ms}
$$

3.8 .3 典型集成数模和模数转换器

\section{1. 集成数模转换器}

集成 D/A 芯片通常是将 $\mathrm{T}$ 形 (倒 $\mathrm{T}$ 形) 电阻网络、模拟开关等集成到一块芯片上, 它并不 包括运算放大器。构成 $\mathrm{D} / \mathrm{A}$ 转换器时需外接运算放大器, 有时还要外接反馈电阻。常用的 D/A芯片有 8 位、10 位、12 位、16 位等。

下面以 8 位 D/A 芯片 DAC0832 为例, 说明它的结构。




(1) 锁存器 (寄存器)

具有两个锁存器, 即输人锁存器和 DAC 锁存器, 可以进行两次缓冲操作, 使操作灵活、多 样。

(2) 控制电路

由 $G_{1} 、 G_{2} 、 G_{3}$ 等门电路组成, 实现锁存器的多种控制。

(3) D/A 转换电路

8 位 $\mathrm{D} / \mathrm{A}$ 转换电路, 主要由倒 $\mathrm{T}$ 形电阻网络组成。 

\section{2. 集成模数转换器}




它主要由三部分电路组成。

(1)模拟多路器。ADC0809 可以处理 8 个不同信号源的模拟信号, 它通过 8 位模拟开关和 地址锁存译码器来完成。

(2) D/A 转换器。该芯片是 8 位逐次比较式 A/D 转换。

(3)控制器。实现对 8 路模拟输人量的选择和 A/D 转换的控制。

\section{8 .4 采样保持电路}

把随时间连续变化的模拟信号变化成对应的离散数字信号, 首先要按一定时间间隔取出 模拟信号的值,这一过程叫采样。由于 A/D 转换需要一定的时间, 在这段时间内所采集的模 拟信号应保持不变, 完成这种功能的电路称为采样保持电路。

采样保持电路的原理电路如图 3-8-7(a) 所示。


采样就是对模拟信号周期性地抽取样值, 使模拟信号变成时间上离散的脉冲串, 其幅值取 决于采样时间内输人模拟信号的大小。

采样频率 $f_{\mathrm{S}}(1 / T)$ 越高, 采样越密, 采样值就越多, 采样信号 $u_{\mathrm{s}}$ 的包络线就越接近输人信 号波形。采样定理指出: 只有当采样频率大于模拟信号最高频率分量的 2 倍时, 即 $f_{\mathrm{S}} \geqslant 2 f_{\text {imax }}$ 时,所采集的信号才能不失真地反映原来模拟信号的变化规律。

对于变化较快的模拟信号, 其采样值 $u_{\mathrm{s}}$ 在脉冲持续时间内会有明显的变化, 顶部不平, 故 不能得到一个采样值。为此, 利用电容 $C$ 的电荷存储作用, 使 $u_{\mathrm{o}}$ 保持采样结束时 $u_{\mathrm{i}}$ 的瞬时值, 形成幅度固定的采样值。 $u_{\mathrm{o}}$ 形状如图 3.8-7(e) 所示。

【例 3.8-5 若 A D D 转换器的输人模拟信号 电压最高频率为 $20 \mathrm{kHz}$, 则采样频率的下限是 多少?

解: 根据采样定理有

$$
f_{\mathrm{S}} \geqslant 2 f_{\text {imax }}
$$

则可采样频率的下限为 $40 \mathrm{kHz}$ 。


\section{复习内容}

\section{1 电力系统基本知识}

\subsection{1 电力系统运行特点和基本要求}

\section{1. 电力系统运行的特点}

(1)电能不能大量存储。电能的生产、输送、分配和消费实际上是同时进行的, 任何时刻发 电机所发出的功率等于用电设备所消耗的功率与输送和分配环节中功率损耗之和。

(2)电力系统的暂态过程非常短促。从一种运行状态到另一种运行状态的过渡极为迅速, 以毫秒甚至微秒计。

(3)与国民经济和人民生活密切相关。供电的突然中断会造成很大的损失以致严重的后 果。

\section{2. 对电力系统运行的基本要求}

(1)保证安全可靠供电。对负荷按照不同级别分别采取适当的技术措施来满足它们对供电 可靠性的要求。

(2)保证电能的质量(电压、频率和谐波)。

(3)要有良好的经济性(降低网损、降低煤耗等)。

(4)电能生产要符合环境保护标准 (限制二氧化碳、二氧化硫等污染物的排放量)。

\subsection{2 电能质量各项指标}

(1)电压幅值。对于 $35 \mathrm{kV}$ 及以上电压级允许变化范围为额定值的 $\pm 5 \%, 10 \mathrm{kV}$ 及以下电 压级允许变化范围为 $\pm 7 \%$ 。

(2)频率。我国电力系统的额定频率为 $50 \mathrm{~Hz}$, 正常运行时允许的偏移为 $\pm 0.2 \sim \pm 0.5 \mathrm{~Hz}$ 。

(3)谐波。为保证电压质量, 要求电压为正弦波形, 但由于某种原因总会产生一些谐波, 会 造成电压波形的畸变。为此, 对电压正弦波形畸变率也有限制 (波形畸变率是指各次谐波有 效值平方和的方根对基波有效值的百分比), 对于 $6 \sim 10 \mathrm{kV}$ 供电电压不超过 $4 \%, 0.38 \mathrm{kV}$ 电 压不超过 $5 \%$ 。

\subsection{3 电力系统中各种接线方式及特点}

电力系统的接线包括发电厂、变电所的主接线和电力网的接线。电力网的接线通常按可 靠性分为无备用和有备用两类。

(1)无备用接线,是指每一个负荷只能靠一条线路取得电能。优点是设备费用小, 缺点是可 靠性差。无备用接线主要有三种方式,即放射式、干线式、树状网络,如图 4.1-1 所示。

(2) 有备用接线, 是指负荷可以从两条及以上线路取得电能。优点是可靠性高, 缺点是设备 费用高。主要有三种方式,即双回线、环网、两端供电, 如图 4.1-2 所示。

\subsection{4 我国电力系统的额定电压}

以下所说的额定电压均指额定线电压。

\section{1. 网络的额定电压}

网络的额定电压等于用户设备的额定电压, 也等于母线的额定电压, 也等于线路的额定电 压, 也就是通常所说的额定电压。具体数值见表 4.1-1 的第一列。