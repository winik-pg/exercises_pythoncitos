import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import numpy as np


########### Define your variables
beers=['uno', 'dos', 'tres', 'Cuatro']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Añadir graficas'
tabtitle='weed!'
myheading='Irina'
label1='IBU'
label2='ABV'
githublink='https://github.com/Aeelen-Miranda/flying-dog-beers'
sourceurl='https://plotly.com/python/histograms/'

########### Set up the chart
bitterness = go.Bar(
    x=beers,
    y=ibu_values,
    name=label1,
    marker={'color':color1}
)
alcohol = go.Bar(
    x=beers,
    y=abv_values,
    name=label2,
    marker={'color':color2}
)

beer_data = [bitterness, alcohol]
beer_layout = go.Layout(
    barmode='group',
    title = mytitle
)

beer_fig = go.Figure(data=beer_data, layout=beer_layout)

####################dos
histograma = go.Figure(data=[go.Scatter(x=[1, 2, 3], y=[4, 1, 2])])
dcc.Graph(
        id='example-graph-2',
        figure=histograma
    )
#######################tres

x = ['1970-01-01', '1970-01-01', '1970-02-01', '1970-04-01', '1970-01-02',
     '1972-01-31', '1970-02-13', '1971-04-19']

fig = make_subplots(rows=3, cols=2)

trace0 = go.Histogram(x=x, nbinsx=4)
trace1 = go.Histogram(x=x, nbinsx = 8)
trace2 = go.Histogram(x=x, nbinsx=10)
trace3 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size='M18'), # M18 stands for 18 months
                      autobinx=False
                     )
trace4 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size='M4'), # 4 months bin size
                      autobinx=False
                      )
trace5 = go.Histogram(x=x,
                      xbins=dict(
                      start='1969-11-15',
                      end='1972-03-31',
                      size= 'M2'), # 2 months
                      autobinx = False
                      )

fig.append_trace(trace0, 1, 1)
fig.append_trace(trace1, 1, 2)
fig.append_trace(trace2, 2, 1)
fig.append_trace(trace3, 2, 2)
fig.append_trace(trace4, 3, 1)
fig.append_trace(trace5, 3, 2)

#fig.show()
###############################Cuatro


x0 = np.random.randn(2000)
x1 = np.random.randn(2000) + 1

cuatro = go.Figure()
cuatro.add_trace(go.Histogram(x=x0))
cuatro.add_trace(go.Histogram(x=x1))

# The two histograms are drawn on top of another
cuatro.update_layout(barmode='stack')
#fig.show()

########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}
server = app.server
app.title=tabtitle

########### Set up the layout
app.layout = html.Div(children=[
    html.Div(children = [dcc.Graph(figure=beer_fig)]),
    html.Div(children = [dcc.Graph(figure=histograma)]),
    html.Div(children = [dcc.Graph(figure=fig)]),
     
    html.Div(children = [dcc.Graph(figure=cuatro)]),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl)
    
],
                     )
    
                     

if __name__ == '__main__':
    app.run_server()
