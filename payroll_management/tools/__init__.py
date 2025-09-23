# tools/__init__.py — export all interface tool lists
try:
    from tau_bench.envs.payroll_management.tools.interface_1 import ALL_TOOLS_INTERFACE_1
    from tau_bench.envs.payroll_management.tools.interface_2 import ALL_TOOLS_INTERFACE_2
    from tau_bench.envs.payroll_management.tools.interface_3 import ALL_TOOLS_INTERFACE_3
    from tau_bench.envs.payroll_management.tools.interface_4 import ALL_TOOLS_INTERFACE_4
    from tau_bench.envs.payroll_management.tools.interface_5 import ALL_TOOLS_INTERFACE_5
except ModuleNotFoundError:
    from .interface_1 import ALL_TOOLS_INTERFACE_1
    from .interface_2 import ALL_TOOLS_INTERFACE_2
    from .interface_3 import ALL_TOOLS_INTERFACE_3
    from .interface_4 import ALL_TOOLS_INTERFACE_4
    from .interface_5 import ALL_TOOLS_INTERFACE_5
