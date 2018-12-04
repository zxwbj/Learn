from random import choice


class RandomWalk():
    """生成一个随机漫步类"""

    def __init__(self, num_points=5000):
        """初始化随机漫步的属性"""
        self.num_points = num_points

        # 所有随机漫步都始于(0, 0)点
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """计算随机漫步包含的点数"""

        # 不断随机漫步，直到列表达到指定的长度
        while len(self.x_values) < self.num_points:

            # 决定前进方向及沿着个方向前进的距离
            x_step = self.get_step()
            y_step = self.get_step()

            # 拒绝原地踏步
            if 0 == x_step and 0 == y_step:
                continue

            # 计算下一个点的 x 和 y 值
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        direction = choice([-1, 1])
        distance = choice([0, 1, 2, 3, 4, 5, 6, 7, 8])
        return direction * distance
