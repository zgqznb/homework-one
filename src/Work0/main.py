import taichi as ti
from .config import WINDOW_RES, WINDOW_TITLE, PARTICLE_RADIUS
from .physics import pos, init_particles, substep


def run():
    init_particles()

    window = ti.ui.Window(WINDOW_TITLE, WINDOW_RES)
    canvas = window.get_canvas()

    paused = False
    speed_levels = [1, 2, 4, 8]
    speed_idx = 0

    while window.running:
        if window.get_event(ti.ui.PRESS):
            if window.event.key == ti.ui.ESCAPE:
                break
            elif window.event.key == ti.ui.SPACE:
                paused = not paused
            elif window.event.key == "r":
                init_particles()
                speed_idx = 0
            elif window.event.key == ti.ui.UP:
                speed_idx = min(speed_idx + 1, len(speed_levels) - 1)
            elif window.event.key == ti.ui.DOWN:
                speed_idx = max(speed_idx - 1, 0)

        mouse = window.get_cursor_pos()
        mouse_x, mouse_y = mouse[0], mouse[1]

        if not paused:
            for _ in range(speed_levels[speed_idx]):
                substep(mouse_x, mouse_y)

        # 黑色背景
        canvas.set_background_color((0.0, 0.0, 0.0))

        # 小蓝点，更接近演示效果
        canvas.circles(
            pos,
            radius=PARTICLE_RADIUS,
            color=(0.2, 0.8, 1.0)
        )

        window.show()


if __name__ == "__main__":
    run()
