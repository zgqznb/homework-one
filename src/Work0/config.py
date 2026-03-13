import taichi as ti

try:
    ti.init(arch=ti.gpu)
except Exception:
    ti.init(arch=ti.cpu)

# 粒子数量
N = 20000

# 时间步长
DT = 5e-5
# 粒子之间引力（弱一些）
G = 0.002

# 鼠标引力（强一些）
MOUSE_G = 50

# 粒子质量
MASS = 1.0

# 防止距离过小导致数值爆炸
EPS = 1e-4

# 阻尼，防止粒子越飞越快
DAMPING = 0.992

# 窗口设置
WINDOW_RES = (1000, 1000)
WINDOW_TITLE = "Experiment 0: Taichi Gravity Swarm"

# 这个版本里初始是全屏随机撒点，所以这个参数可留着但不使用
INIT_RADIUS = 0.12

# 粒子显示半径
PARTICLE_RADIUS = 0.001
