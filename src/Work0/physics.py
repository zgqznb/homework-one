import taichi as ti
from .config import N, DT, G, MOUSE_G, MASS, EPS, DAMPING

pos = ti.Vector.field(2, dtype=ti.f32, shape=N)
vel = ti.Vector.field(2, dtype=ti.f32, shape=N)
acc = ti.Vector.field(2, dtype=ti.f32, shape=N)


@ti.kernel
def init_particles():
    for i in range(N):
        # 全屏随机撒点，更接近演示效果
        pos[i] = ti.Vector([
            ti.random(dtype=ti.f32),
            ti.random(dtype=ti.f32)
        ])
        vel[i] = ti.Vector([0.0, 0.0])
        acc[i] = ti.Vector([0.0, 0.0])


@ti.kernel
def substep(mouse_x: ti.f32, mouse_y: ti.f32):
    mouse_pos = ti.Vector([mouse_x, mouse_y])

    # 计算受力
    for i in range(N):
        force = ti.Vector([0.0, 0.0])

        # 粒子之间的弱引力
        for j in range(N):
            if i != j:
                r = pos[j] - pos[i]
                dist_sqr = r.dot(r) + EPS
                inv_dist = 1.0 / ti.sqrt(dist_sqr)
                inv_dist3 = inv_dist * inv_dist * inv_dist
                force += G * MASS * MASS * r * inv_dist3

        # 鼠标作为主要引力源
        r_mouse = mouse_pos - pos[i]
        dist_mouse_sqr = r_mouse.dot(r_mouse) + EPS
        inv_mouse_dist = 1.0 / ti.sqrt(dist_mouse_sqr)
        inv_mouse_dist3 = inv_mouse_dist * inv_mouse_dist * inv_mouse_dist
        force += MOUSE_G * MASS * MASS * r_mouse * inv_mouse_dist3

        acc[i] = force / MASS

    # 更新速度和位置
    for i in range(N):
        vel[i] += acc[i] * DT

        # 阻尼
        vel[i] *= DAMPING

        pos[i] += vel[i] * DT

        # 边界墙：撞墙反弹
        if pos[i].x < 0.0:
            pos[i].x = 0.0
            vel[i].x *= -0.5
        elif pos[i].x > 1.0:
            pos[i].x = 1.0
            vel[i].x *= -0.5

        if pos[i].y < 0.0:
            pos[i].y = 0.0
            vel[i].y *= -0.5
        elif pos[i].y > 1.0:
            pos[i].y = 1.0
            vel[i].y *= -0.5
