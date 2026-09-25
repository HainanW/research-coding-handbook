# %% E01-S0 案例说明与来源 / Example and source
"""MO-book 1.2: a basic production-planning LP, adapted for Spyder.

来源 / Source: Hands-On Mathematical Optimization with Python, sections 1.1-1.2.
https://mobook.github.io/MO-book/notebooks/01/02-production-planning-basic.html
Copyright (c) 2022 Jeffrey Kantor. MIT license: see LICENSE-MO-book.txt.

学习版改编 / Adapted 2026-09-25: bilingual numbered cells, explicit expressions,
editable inputs, inspectable tables, and feasibility checks; same original LP.
所有数据均为教材示例，不是公司数据。 / Textbook data, not company data.
这是单周LP，不是MILP或滚动计划。 / One-week LP, not MILP or rolling planning.
按编号顺序运行；修改参数后完整重跑。 / Run in order; rerun all after edits.
只在内存计算，不读写业务文件、不联网。 / In-memory only; no files or network.
"""

# %% E01-S1 导入工具 / Import tools
import pandas as pd  # 将结果整理成可查看的表格。 / Inspectable result tables.
import pyomo.environ as pyo  # 表达变量、约束和目标。 / Optimization modeling.

# %% E01-S2 已知参数：这一周有哪些条件？ / Given weekly inputs
# 单位按原教材保留；金额用货币单位，不指定美元。 / Original units; generic money.
price_u = 270.0  # U售价，货币单位/件。 / U selling price per unit.
price_v = 210.0  # V售价，货币单位/件。 / V selling price per unit.
material_cost = 10.0  # 原料单价，货币单位/克。 / Material price per gram.
labor_a_cost = 50.0  # A类人工单价，货币单位/小时。 / Labor A hourly cost.
labor_b_cost = 40.0  # B类人工单价，货币单位/小时。 / Labor B hourly cost.
labor_a_limit = 80.0  # A类人工每周最多可用小时。 / Weekly labor A limit.
labor_b_limit = 100.0  # B类人工每周最多可用小时。 / Weekly labor B limit.
u_market_limit = 40.0  # U最多可销售件数，不是必须完成的订单。 / Sales ceiling.
material_per_u = 10.0  # 每件U需要的原料克数。 / Material grams per U.
material_per_v = 9.0  # 每件V需要的原料克数。 / Material grams per V.
labor_a_per_u = 1.0  # 每件U需要的A类人工小时。 / Labor A hours per U.
labor_a_per_v = 1.0  # 每件V需要的A类人工小时。 / Labor A hours per V.
labor_b_per_u = 2.0  # 每件U需要的B类人工小时。 / Labor B hours per U.
labor_b_per_v = 1.0  # 每件V需要的B类人工小时。 / Labor B hours per V.

# %% E01-S3 创建模型与决策变量 / Create model and decision variables
model = pyo.ConcreteModel("MO-book 1.2 - weekly production LP")

# x_M是原料克数，x_A/x_B是人工小时；不是三种产品。 / Resource decisions.
model.x_M = pyo.Var(domain=pyo.NonNegativeReals)
model.x_A = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, labor_a_limit))
model.x_B = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, labor_b_limit))
# y_U/y_V是产量；原模型允许连续值，并未施加整数约束。 / Continuous output.
model.y_U = pyo.Var(domain=pyo.NonNegativeReals, bounds=(0, u_market_limit))
model.y_V = pyo.Var(domain=pyo.NonNegativeReals)

# 此时变量尚未求解，Value为None是正常的。 / Values are unknown before solving.
# model.pprint()  # 可取消注释查看完整模型。 / Optional model inspection.

# %% E01-S4 收入、成本与目标 / Revenue, cost, and objective
model.revenue = pyo.Expression(expr=price_u * model.y_U + price_v * model.y_V)
model.cost = pyo.Expression(
    expr=material_cost * model.x_M
    + labor_a_cost * model.x_A
    + labor_b_cost * model.x_B
)
# 最大化利润=收入-原料与人工成本。 / Maximize revenue minus resource costs.
model.profit = pyo.Objective(
    expr=model.revenue - model.cost, sense=pyo.maximize
)

# %% E01-S5 资源约束 / Resource constraints
# 生产所需资源不能超过购买/安排的资源。 / Consumption <= allocated resources.
model.raw_materials = pyo.Constraint(
    expr=material_per_u * model.y_U + material_per_v * model.y_V <= model.x_M
)
model.labor_A = pyo.Constraint(
    expr=labor_a_per_u * model.y_U + labor_a_per_v * model.y_V <= model.x_A
)
model.labor_B = pyo.Constraint(
    expr=labor_b_per_u * model.y_U + labor_b_per_v * model.y_V <= model.x_B
)

# %% E01-S6 调用HiGHS求解 / Solve locally with HiGHS
solver = pyo.SolverFactory("appsi_highs")
if not solver.available(exception_flag=False):
    raise RuntimeError("HiGHS unavailable. Use the Jushi_scheduler environment.")

# 先检查求解状态，再读取结果，避免使用失败求解的变量值。 / Check before loading.
results = solver.solve(model, tee=False, load_solutions=False)
termination = str(results.solver.termination_condition)
if results.solver.termination_condition != pyo.TerminationCondition.optimal:
    raise RuntimeError(f"No proven optimal solution: {termination}")
model.solutions.load_from(results)

# %% E01-S7 提取普通数值与表格 / Extract values for Spyder Variable Explorer
u_units = pyo.value(model.y_U)  # U最优产量，件/周。 / U units per week.
v_units = pyo.value(model.y_V)  # V最优产量，件/周。 / V units per week.
material_grams = pyo.value(model.x_M)  # 原料，克/周。 / Material grams per week.
labor_a_hours = pyo.value(model.x_A)  # A类人工，小时/周。 / Labor A hours.
labor_b_hours = pyo.value(model.x_B)  # B类人工，小时/周。 / Labor B hours.
revenue_value = pyo.value(model.revenue)
cost_value = pyo.value(model.cost)
profit_value = pyo.value(model.profit)

# 双击这些表格，比直接展开Pyomo对象更适合初学。 / Open these tables in Spyder.
production = pd.DataFrame({
    "product": ["U", "V"],
    "quantity_units_per_week": [u_units, v_units],
})
resources = pd.DataFrame({
    "resource": ["Material M", "Labor A", "Labor B"],
    "allocated": [material_grams, labor_a_hours, labor_b_hours],
    "limit": [None, labor_a_limit, labor_b_limit],
    "unit": ["g/week", "hours/week", "hours/week"],
})
financials = pd.Series({
    "revenue": revenue_value, "cost": cost_value, "profit": profit_value,
}, name="monetary_units_per_week")

# %% E01-S8 独立复算与显示 / Recheck feasibility and display results
# 容差处理浮点误差；不把教材最优值写死，以便修改参数练习。 / Numerical tolerance.
tolerance = 1e-6
checks = pd.Series({
    "nonnegative": min(u_units, v_units, material_grams,
                       labor_a_hours, labor_b_hours) >= -tolerance,
    "u_market_limit": u_units <= u_market_limit + tolerance,
    "labor_a_limit": labor_a_hours <= labor_a_limit + tolerance,
    "labor_b_limit": labor_b_hours <= labor_b_limit + tolerance,
    "material_balance": (
        material_per_u * u_units + material_per_v * v_units
        <= material_grams + tolerance
    ),
    "labor_a_balance": (
        labor_a_per_u * u_units + labor_a_per_v * v_units
        <= labor_a_hours + tolerance
    ),
    "labor_b_balance": (
        labor_b_per_u * u_units + labor_b_per_v * v_units
        <= labor_b_hours + tolerance
    ),
    "profit_balance": abs(profit_value - (revenue_value - cost_value)) <= tolerance,
}, name="passed")
if not checks.all():
    raise RuntimeError("Independent solution checks failed; inspect checks.")

print("MO-book 1.2 | Textbook example only | LP, not MILP or rolling planning")
print(f"Solver termination: {termination}")
print(production.to_string(index=False))
print(resources.to_string(index=False))
print(financials.to_string())
print(f"Independent checks passed: {bool(checks.all())}")
