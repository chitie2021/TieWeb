.. _fluidFunctions:

流体力学基本方程
==============

在流体力学中，最基本的三个方程是连续性方程（描述质量守恒）、Navier-Stokes 方程（描述动量守恒）和能量方程（描述能量守恒）。以下是这三个方程的数学表达式及其 Python 代码表示。

1. 连续性方程（Continuity Equation）
--------------------
连续性方程描述了流体的质量守恒。对于不可压缩流体，其形式为：

.. math::

   \nabla \cdot \mathbf{u} = 0


对于可压缩流体，其形式为：

.. math::

   \frac{\partial \rho}{\partial t} + \nabla \cdot (\rho \mathbf{u}) = 0

2. Navier-Stokes 方程（Navier-Stokes Equations）
--------------------
Navier-Stokes 方程描述了流体的动量守恒。其形式为：

.. math::

   \rho \left( \frac{\partial \mathbf{u}}{\partial t} + \mathbf{u} \cdot \nabla \mathbf{u} \right) = -\nabla p + \mu \nabla^2 \mathbf{u} + \mathbf{f}

3. 能量方程（Energy Equation）
-------------------
能量方程描述了流体的能量守恒。其形式为：

.. math::

   \frac{\partial}{\partial t} \left( \frac{1}{2} \rho |\mathbf{u}|^2 + \rho e \right) + \nabla \cdot \left( \left( \frac{1}{2} \rho |\mathbf{u}|^2 + \rho e + p \right) \mathbf{u} \right) = \nabla \cdot (k \nabla T) + \Phi

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


