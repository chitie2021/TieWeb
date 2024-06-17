流体力学
=====

.. _introduction:

流体力学概述
------------

流体力学是一门研究流体（包括液体和气体）运动规律及其与边界相互作用的科学。它在工程、自然科学和日常生活中具有广泛应用，如飞机设计、气象预报和管道输送等领域。流体力学的核心概念包括密度、粘度、压力和流速。主要的数学工具包括连续性方程、Navier-Stokes方程和能量方程，分别描述了流体的质量守恒、动量守恒和能量守恒。流体可以分为理想流体和粘性流体，以及可压缩和不可压缩流体，具体分类视情况而定。了解这些基本原理和方程能够帮助工程师和科学家设计更高效的系统和设备，从而提升现代科技的应用水平。

.. code-block:: console

   (.venv) $ pip install lumache

.. _fluidFunctions:

流体力学方程：
------------

在流体力学中，最基本的三个方程是连续性方程（描述质量守恒）、Navier-Stokes 方程（描述动量守恒）和能量方程（描述能量守恒）。以下是这三个方程的数学表达式及其 Python 代码表示。

1. 连续性方程（Continuity Equation）
~~~~~~~~~~~
连续性方程描述了流体的质量守恒。对于不可压缩流体，其形式为：

.. math::

    \\nabla \\cdot \\mathbf{u} = 0

对于可压缩流体，其形式为：

.. math::

    \\frac{\\partial \\rho}{\\partial t} + \\nabla \\cdot (\\rho \\mathbf{u}) = 0

2. Navier-Stokes 方程（Navier-Stokes Equations）
~~~~~~~~~~~~~
Navier-Stokes 方程描述了流体的动量守恒。其形式为：

.. math::

    \\rho \\left( \\frac{\\partial \\mathbf{u}}{\\partial t} + \\mathbf{u} \\cdot \\nabla \\mathbf{u} \\right) = -\\nabla p + \\mu \\nabla^2 \\mathbf{u} + \\mathbf{f}

3. 能量方程（Energy Equation）
~~~~~~~~~~~~~~
能量方程描述了流体的能量守恒。其形式为：

.. math::

    \\frac{\\partial}{\\partial t} \\left( \\frac{1}{2} \\rho |\\mathbf{u}|^2 + \\rho e \\right) + \\nabla \\cdot \\left( \\left( \\frac{1}{2} \\rho |\\mathbf{u}|^2 + \\rho e + p \\right) \\mathbf{u} \\right) = \\nabla \\cdot (k \\nabla T) + \\Phi

其中：
- \\(\\rho\\) 是流体密度
- \\(\\mathbf{u}\\) 是速度向量
- \\(p\\) 是压力
- \\(\\mu\\) 是动力粘度
- \\(\\mathbf{f}\\) 是体积力（如重力）
- \\(e\\) 是内能
- \\(k\\) 是热传导系数
- \\(T\\) 是温度
- \\(\\Phi\\) 是粘性耗散函数

以下是这三个方程在 Python 中的表示：

.. code-block:: python

    import sympy as sp

    # 定义变量
    t = sp.symbols('t')
    x, y, z = sp.symbols('x y z')
    rho = sp.Function('rho')(x, y, z, t)
    u = sp.Function('u')(x, y, z, t)
    v = sp.Function('v')(x, y, z, t)
    w = sp.Function('w')(x, y, z, t)
    p = sp.Function('p')(x, y, z, t)
    mu = sp.symbols('mu')
    f_x, f_y, f_z = sp.symbols('f_x f_y f_z')
    e = sp.Function('e')(x, y, z, t)
    T = sp.Function('T')(x, y, z, t)
    k = sp.symbols('k')

    # 连续性方程（可压缩）
    continuity_eq = sp.Eq(sp.diff(rho, t) + sp.diff(rho*u, x) + sp.diff(rho*v, y) + sp.diff(rho*w, z), 0)

    # Navier-Stokes方程
    momentum_eq_x = sp.Eq(rho * (sp.diff(u, t) + u*sp.diff(u, x) + v*sp.diff(u, y) + w*sp.diff(u, z)), 
                          -sp.diff(p, x) + mu * (sp.diff(u, x, x) + sp.diff(u, y, y) + sp.diff(u, z, z)) + f_x)
    momentum_eq_y = sp.Eq(rho * (sp.diff(v, t) + u*sp.diff(v, x) + v*sp.diff(v, y) + w*sp.diff(v, z)), 
                          -sp.diff(p, y) + mu * (sp.diff(v, x, x) + sp.diff(v, y, y) + sp.diff(v, z, z)) + f_y)
    momentum_eq_z = sp.Eq(rho * (sp.diff(w, t) + u*sp.diff(w, x) + v*sp.diff(w, y) + w*sp.diff(w, z)), 
                          -sp.diff(p, z) + mu * (sp.diff(w, x, x) + sp.diff(w, y, y) + sp.diff(w, z, z)) + f_z)

    # 能量方程
    energy_eq = sp.Eq(sp.diff((0.5*rho*(u**2 + v**2 + w**2) + rho*e), t) + 
                      sp.diff(((0.5*rho*(u**2 + v**2 + w**2) + rho*e + p) * u), x) +
                      sp.diff(((0.5*rho*(u**2 + v**2 + w**2) + rho*e + p) * v), y) +
                      sp.diff(((0.5*rho*(u**2 + v**2 + w**2) + rho*e + p) * w), z),
                      sp.diff(k*sp.diff(T, x), x) + sp.diff(k*sp.diff(T, y), y) + sp.diff(k*sp.diff(T, z), z))

    # 输出方程
    continuity_eq, momentum_eq_x, momentum_eq_y, momentum_eq_z, energy_eq

这些方程在实际应用中会有很多简化和假设，以适应特定的问题和条件。理解并应用这些方程对于解决流体力学中的复杂问题至关重要。

.. _turbulence:

湍流
----------------

湍流是流体力学中的一个复杂且广泛存在的现象，指的是流体在高速度和高雷诺数（Reynolds number）条件下表现出的混乱和不规则的运动模式。与层流（laminar flow）相比，湍流具有更高的动量、能量和质量传输效率，但其行为更难以预测和建模。

湍流的特点
~~~~~~~~~~~~~~~~

1. **不规则性**：湍流具有高度的不规则性和随机性，表现为涡流和乱流结构的不断变化。
2. **能量级联**：湍流中能量在大尺度和小尺度之间传递，大尺度的能量通过非线性相互作用转移到较小尺度，直到被黏性耗散。
3. **尺度的广泛性**：湍流中存在多个尺度，从较大的主涡到较小的微涡，涵盖了广泛的频谱。
4. **高效的混合**：湍流能够显著增强动量、热量和质量的混合与传输，是许多工业过程和自然现象中的重要机制。

湍流的数学描述
~~~~~~~~~~~~~~~~~

尽管湍流的具体行为极其复杂，Navier-Stokes方程仍然是其基本描述工具。然而，由于湍流中的非线性和多尺度特性，直接求解Navier-Stokes方程在湍流条件下极为困难。因此，研究湍流通常依赖于以下方法：

1. **平均方法**：如Reynolds平均Navier-Stokes方程（RANS），通过对速度场进行时间或空间平均，引入雷诺应力来表征湍流的影响。
2. **大涡模拟**：大涡模拟（LES）通过直接模拟大尺度湍流结构，而将小尺度湍流的影响通过亚格子尺度模型来表示。
3. **直接数值模拟**：直接数值模拟（DNS）试图在所有尺度上精确求解Navier-Stokes方程，但由于计算成本极高，仅适用于低雷诺数或简化条件下的研究。

湍流模型
~~~~~~~~~~~~~~~~~

由于湍流的复杂性，许多湍流模型被提出用于工程和实际应用中的湍流预测。这些模型通常简化了湍流的某些特征，以便在计算上更加可行。常见的湍流模型包括：

1. **k-ε模型**：一种常用的RANS模型，通过引入湍动能（k）和湍流耗散率（ε）来描述湍流。
2. **k-ω模型**：另一种RANS模型，使用湍动能（k）和比耗散率（ω）来表征湍流行为。
3. **Spalart-Allmaras模型**：一种简化的湍流模型，主要用于航空和汽车工程中的附面层流动模拟。

湍流研究对于理解和预测各种流体现象具有重要意义，从大气和海洋中的自然湍流，到工业设备中的流动优化。通过不断的发展和改进湍流模型和数值方法，科学家和工程师能够更好地应对湍流带来的挑战，并利用其特性提高技术和工程系统的性能。

