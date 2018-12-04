import pygal

from die import Die

# 创建一个D6
die_1 = Die()
die_2 = Die(10)

# 掷几次骰子，并将结果存储在一个列表中
# results = []
# for _ in range(100000):
#     result = die_1.roll() + die_2.roll()
#     results.append(result)
results = [(die_1.roll() + die_2.roll()) for _ in range(10000)]

# 分析结果
max_result = die_1.num_sides + die_2.num_sides
# frequencies = []
# for value in range(2, max_result+1):
#     frequency = results.count(value)
#     frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_result+1)]

hist = pygal.Bar()
hist.title = "Results of rolling one D6 1000 times"
hist.x_labels = [i for i in range(2, max_result+1)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual.svg')
