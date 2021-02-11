import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import numpy as np
import pandas as pd


################################### Abre archivos
zacatecas = pd.read_csv('https://raw.githubusercontent.com/Aeelen-Miranda/flying-dog-beers/master/Tabla%202.%20Delitos%20Zacatecas%20(2020)_2.csv', )
covid = pd.read_csv("https://raw.githubusercontent.com/Aeelen-Miranda/flying-dog-beers/master/cdmx_deaths.csv")

################################### Prepara Grafica 1
pv = pd.pivot_table(zacatecas, index=['Municipio'], columns=['Tipo de delito'], values=['ene-20'],aggfunc=sum, fill_value = 0)

g1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Robo')], name = 'Robo')
gr1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Violencia familiar')], name = 'Violencia familiar')
gra1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Lesiones')], name = 'Lesiones')
graf1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Otros delitos del Fuero Común')], name = 'Otros delitos del Fuero Común')
grafi1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Daño a la propiedad')], name = 'Daño a la propiedad')
grafic1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Fraude')], name = 'Fraude')
grafica1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Amenazas')], name = 'Amenazas')

################################## Grafica 2
grafica2 = px.line(covid, x = covid['nom_mun'], y = covid['quincena0'])
grafica2.update_traces(orientation = 'v')
grafica2.update_layout(font_family="Montserrat",title = '<b>Quincena 0</b>',
                       template = 'plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod",)
#################################### Grafica 3
grafica3 = px.line(covid, x = covid['nom_mun'], y = covid['quincena2'])
grafica3.update_traces(orientation = 'v')
grafica3.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 2</b>',
                       template = 'plotly_dark',
                       title_font_family="Montserrat",
                       title_font_color="goldenrod",)
################################### Grafica 4
grafica4 = px.line(covid, x = covid['nom_mun'], y = covid['quincena3'])
grafica4.update_traces(orientation = 'v')
grafica4.update_layout(font_family="Montserrat",title = '<b>Quincena 3</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                      title_font_color="goldenrod",)
############################################ Grafica 5
grafica5 = px.line(covid, x = covid['nom_mun'], y = covid['quincena4'])
grafica5.update_traces(orientation = 'v')
grafica5.update_layout(font_family="Montserrat",title = '<b>Quincena 4</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod", )
grafica5.update_xaxes(title_font_family="Montserrat")

############################################ Grafica 6
grafica6 = px.line(covid, x = covid['nom_mun'], y = covid['quincena5']) # , color= "nom_mun")

grafica6.update_traces(orientation = 'v', marker=dict(size=12,
                              line=dict(width=2,
                              color='LightGrey')),
                              selector=dict(mode='markers'))
                     
grafica6.update_layout(font_family="Montserrat", #Tipo de letra del contenido de gráfica 
                       title = '<b>Quincena 5</b>',
                       template='plotly_dark',
                      title_font_family="Montserrat", #Tipo de letra del titulo
                      title_font_color="goldenrod",
                      #line_color= "dark"
                      ) #Con esto se cambia color letra
grafica6.update_xaxes(title_font_family="Montserrat") #Tipo de letra de x,y
############################################ Grafica 8
grafica8 = px.scatter(covid, x='Total', y='nom_mun', size='Total', 
                      color='quincena6', title = '<b>Incidencia delictiva en alcaldias</b>',
                     template = "plotly_dark",
                     )
grafica8.update_traces(orientation = 'v')
grafica8.update_layout(
    font_family="Montserrat",
    font_color="lightgray",
    title_font_family="Montserrat",
    font_size=10,
    title_font_color="goldenrod",
    legend_title_font_color="green"
    
)
grafica8.update_xaxes(title_font_family="Montserrat")
#PRIMEr paso

########################################### Grafica 9
eindex = covid[['nom_mun','Total' ,'quincena0', 'quincena2',
       'quincena3', 'quincena4', 'quincena5', 'quincena6']]

# segundo step

eindexx = eindex.groupby(by = 'nom_mun').agg(sum)


# tercer step

egroup_index = eindexx[['Total']].sort_values(by = 'nom_mun')
egroup_index

# creación de la gráfica 


grafica9 = go.Figure()
grafica9.add_trace(go.Bar(
    y=eindexx.quincena0.values,
    x=eindexx.index,
    name='quincena0',
    marker_color='#572364'
))

grafica9.add_trace(go.Bar(
    y=eindexx.quincena2.values,
    x=eindexx.index,
    name='quincena2',
    marker_color='#A18594'
))

grafica9.add_trace(go.Bar(
    y=eindexx.quincena3.values,
    x=eindexx.index,
    name='quincena3',
    marker_color='#6C4675'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena4.values,
    x=eindexx.index,
    name='quincena4',
    marker_color='#AA00FF'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena5.values,
    x=eindexx.index,
    name='quincena5',
    marker_color='#9C2780'
))
grafica9.add_trace(go.Bar(
    y=eindexx.quincena6.values,
    x=eindexx.index,
    name='quincena6',
    marker_color='#CE93D8'
))

grafica9.update_traces(orientation = 'v')
grafica9.update_layout(title = '<b>9. Delitos totales por Alcaldía</b>',
                       title_font_family="Montserrat",title_font_color="goldenrod",
                       
                 template='plotly_dark')
####################################################################################
########### Define your variables
beers=['uno', 'dos', 'tres', 'Cuatro']
ibu_values=[35, 60, 85, 75]
abv_values=[5.4, 7.1, 9.2, 4.3]
color1='darkred'
color2='orange'
mytitle='Añadir graficas'
tabtitle='Prueba Dash!'
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
####################!!!!! Cinco
colors = ['gold', 'mediumturquoise', 'darkorange', 'lightgreen']

pay = go.Figure(data=[go.Pie(labels=['Oxygen','Hydrogen','Carbon_Dioxide','Nitrogen'],
                             values=[4500,2500,1053,500])])
pay.update_traces(hoverinfo='label+percent', textinfo='value', textfont_size=20,
                  marker=dict(colors=colors, line=dict(color='#000000', width=2)))
##################SEIS



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
    html.Div(children = [dcc.Graph(figure=pay)]),
    html.Div( children = [dcc.Graph(id='grafica1',
              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
                       'layout': go.Layout(paper_bgcolor='black', #color de fondo
                                           plot_bgcolor='black',
                                           title='Mayor incidencia delictiva',
                                           barmode='group')})],
             style = {'margin': '1% 0px 0px 0px', 'width':'60%',
                     'font-family': 'Montserrat',#Cambia tipo de letra
                    }),
    html.Div(children =[dcc.Graph(figure=grafica2)],
             style={'margin': '2% 0px 0px 1px', 'width':'22%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    html.Div(children = [dcc.Graph(figure=grafica3)],
            style={'margin': '2% 0px 0px 1px', 'width':'22%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
   html.Div(children =[dcc.Graph(figure=grafica4)],
             style={'margin': '2% 0px 0px 1px', 'width':'22%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    html.Div(children = [dcc.Graph(figure=grafica5)],
            style={'margin': '2% 0px 0px 0px', 'width':'22%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
    
#tercera franja
    html.Div(children =[dcc.Graph(figure=grafica6)],
             style={'margin': '3% 0px 0px 0px', 'width':'100%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    html.Div(children =[dcc.Graph(figure=grafica8)],
             style={'margin': '2% 0px 0px 0px', 'width':'60%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),

#quinta franja
    html.Div(children = [dcc.Graph(figure=grafica9)],
            style={'margin': '2% 0px 0px 0px', 'width':'100%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl)
    
],
                     )
                     

if __name__ == '__main__':
    app.run_server()
