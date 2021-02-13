import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import pandas as pd


################################### Abre archivos
zacatecas = pd.read_csv('https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%202.%20Delitos%20Zacatecas%20(2020)_2.csv', )
covid = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/cdmx_deaths.csv")
bullet = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%20bullets.csv", encoding= "Latin1")


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


########################################### Grafica 8
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


############################################ Grafica 9
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
    marker_color='#572364',
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





####################### Crear Tabla1
#Tabla de titulos     
    
patabla2 = {'Contagios': [ covid.Total.sum() ],
            'Decesos': [ covid.Total.sum()],
            'Vacunados': [ covid.Total.sum()],             }
patabla3 = pd.DataFrame (patabla2, columns = ['Contagios', 'Decesos', 'Vacunados' ])

tabla2 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla3),
                fill_color='black',
                align=['left', 'left','left']),
                columnwidth = [2,2,2],
#                align= ['left','left'],
                #font=dict(color='black', size=12),

#Cells 
    cells=dict(values=[ patabla3.Contagios, patabla3.Decesos, patabla3.Vacunados
                      ],
               fill_color='black',
               font_size=2,
               height= 10,
    #         font = {'family': 'serif',
    #  'color':  'darkred',
    #  'weight': 'normal',
    #  'size': 16,
    #  },
    #         #font = dict(color = 'white', size = 10),
               #style_column = 30px,
               align= ['left', 'left','left']
             # style="background-color:Red"
              )
              )
               ])

#HEADER
#tabla1.update_traces(header_values=3, selector=dict(type='table'))
tabla2.update_traces(header_fill_color="black", selector=dict(type='table'))
tabla2.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla2.update_traces(header_font_size=13, selector=dict(type='table'))
tabla2.update_traces(header_font_color="gold", selector=dict(type='table'))

#cells
#tabla2.update_traces(columnwidth=3, selector=dict(type='table'))
#tabla2.update_traces(cells_values=[1, patabla["Tipo de delito"], patabla.ene_20.sum()], selector=dict(type='figure'))
#tabla2.update_traces(cells_format=[], selector=dict(type='table'))
tabla2.update_traces(cells_font_size=80, selector=dict(type='table'))
tabla2.update_traces(cells_font_color= "goldenrod", selector=dict(type='table'))
tabla2.update_traces(cells_font_family= 'Montserrat',  selector=dict(type='table'))
tabla2.update_traces(cells_fill_color = "black", selector =dict(type="table"))
tabla2.update_traces(hoverlabel_namelength=20, selector=dict(type='table'))






####################################################################################
########### Define your variables

mytitle='Añadir graficas'
tabtitle='Prueba Dash!'
githublink='https://github.com/fdealbam/flying-dog-beers'
sourceurl='https://plotly.com/python/histograms/'


########### Initiate the app
app = dash.Dash()
colors = {
    'background': '#000000',
    'text': '#FFBF00'
}

server = app.server
app.title=tabtitle

########### Set up the layout
pio.templates.default = "plotly_dark"
app.layout = html.Div(children=[
    
    html.Div(children = [ dcc.Markdown(
        ''' 
    ### *Dashboard mejorado*
    # Incidencia de delitos
    ###### jueves 11 de febrero de 2020
''',
         )],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%',
                  }
             
        ),
     

    
    
   
    
    html.Div( children = [dcc.Graph(id='grafica1',
              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
                       'layout': go.Layout(paper_bgcolor='black',    #color de fondo
                                           plot_bgcolor='black',
                                           title='<b>Mayor incidencia delictiva<b>',
                                           barmode='group',
                                           title_font_color="goldenrod",
                                           title_font_family="Montserrat Black"
                                          )})],
             style = {'margin': '2% 0px 0px 1px', 'width':'100%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),

    
   html.Div(children =[dcc.Graph(figure=grafica2)],
            style={'margin': '3% 0px 0px 1px', 'width':'23%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
  
   html.Div(children = [dcc.Graph(figure=grafica3)],
           style={'margin': '3% 0px 0px 1px', 'width':'23%',
                 'font-family': 'Montserrat',
                 'backgroundColor': colors['background']}),
  
    html.Div(children =[dcc.Graph(figure=grafica4)],
             style={'margin': '3% 0px 0px 1px', 'width':'23%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
  
    html.Div(children = [dcc.Graph(figure=grafica5)],
            style={'margin': '3% 0px 0px 0px', 'width':'23%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
    
    html.Div(children =[dcc.Graph(figure=grafica6)],
             style={'margin': '4% 0px 0px 0px', 'width':'23%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
  

    
    html.Div(children =[dcc.Graph(figure=grafica8)],
            style={'margin': '4% 0px 0px 0px', 'width':'65%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),

#quinta franja
    html.Div(children = [dcc.Graph(figure=grafica9)],
            style={'margin': '5% 0px 0px 0px', 'width':'100%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),
  
  

#############################################################  Tabla 1

    html.Div(children = [dcc.Graph(style={'backgroundColor': colors['background']},
                    figure=tabla2)],
             style={'margin': '1% 0px 0px 0px', 'width':'100%',
                   'font-family': 'Montserrat',
                    #paper_bgcolor='black',
                    #plot_bgcolor='black',
                   'backgroundColor': colors['background']}),

#############################################################      
    
    
    
    
    html.A(" "),
    html.Br(),
    html.A(""),
    html.Br(),
  
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),
    html.I("Con la I se agrega texto!!",
    style={'color': '#C0C0C0','font-family': 'Montserrat',"size" :  "1000"}),
    dcc.Markdown('''
#
#
#### Otra manera de agregar texto
#
Agregar un link: [Markdown](http://commonmark.org/help).

Escritura normal.
 **Negritas** y *Cursiva*,
[links](http://commonmark.org/help),  `cambiar tipo de letra` 

''', style={'color': '#C0C0C0'}),
    #html.Div([html.P('Dash converts Python classes into HTML'),
],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()
