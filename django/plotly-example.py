import math
import plotly
import plotly.graph_objs as go

x = [x/10 for x in range(100)]
y = [math.sin(v) for v in x]

# print(f'x={x}')
# print(f'y={y}')

# # build the graph
# fig = go.Scatter(x=x, y=y)
# # plot it
# plotly.offline.plot({"data": [fig]})

# fig = go.Pie(labels=['a', 'b', 'c'], values=[0.4, 0.5, 0.1])
# graph_div = plotly.offline.plot({"data": [fig]}, auto_open=False, output_type='div')
# print(graph_div)