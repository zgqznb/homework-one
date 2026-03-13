# CG-Lab

本项目为计算机图形学实验一作业，实现了基于 Taichi 的万有引力粒子群仿真，并采用 `src` 布局组织代码。

## 项目结构

```text
CG-Lab/
├─ .gitignore
├─ README.md
└─ src/
   └─ Work0/
      ├─ __init__.py
      ├─ config.py
      ├─ physics.py
      └─ main.py
在项目根目录下运行：python -m src.Work0.main
如果使用解释器绝对路径运行：E:\anaconda3\python.exe -m src.Work0.main

### config.py
负责系统参数配置，包括：

- 粒子数量
- 引力常数
- 时间步长
- 窗口大小
- 粒子渲染大小

### physics.py
实现粒子系统的核心物理计算：

- 粒子之间万有引力
- 鼠标作为引力源
- GPU并行计算
- 边界碰撞处理

### main.py
负责程序运行逻辑：

- 创建窗口
- 渲染粒子
- 处理鼠标交互
- 控制仿真循环

## 演示视频 [点击查看演示视频](./src/Experiment 0_ Taichi Gravity Swarm  193.876462 FPS 2026-03-13 18-01-02.mp4)



