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
contagios2 = pd.read_csv("https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/contagios_20210213.csv")


################################### Prepara Grafica 1
pv = pd.pivot_table(zacatecas, index=['Municipio'], columns=['Tipo de delito'], values=['ene-20'],aggfunc=sum, fill_value = 0)

g1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Robo')], name = 'Robo')
gr1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Violencia familiar')], name = 'Violencia familiar')
gra1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Lesiones')], name = 'Lesiones')
graf1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Otros delitos del Fuero Común')], name = 'Otros delitos del Fuero Común')
grafi1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Daño a la propiedad')], name = 'Daño a la propiedad')
grafic1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Fraude')], name = 'Fraude')
grafica1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Amenazas')], name = 'Amenazas')


################################  grafia 1.1 contagios acumulados por día

figaro = go.Figure()
figaro.add_trace(go.Bar(x=contagios2['date'],y=contagios2['confirmados'],
                #name='Contagios confirmados COVID-19',
                marker_color='#0776a8'  # cambiar nuemeritos de rgb
                ))
figaro.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Evolución del COVID-19',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Contagios diarios',
        titlefont_size=14,
        tickfont_size=12,))






################################## Grafica 2
grafica2 = px.line(covid, x = covid['nom_mun'], y = covid['quincena0'])
grafica2.update_traces(orientation = 'v')
grafica2.update_layout(font_family="Montserrat",title = '<b>Quincena 0</b>',
                       template = 'simple_white',title_font_family="Montserrat",
                       title_font_color="goldenrod",
                      paper_bgcolor='rgba(0,0,0,0)',
                      plot_bgcolor='rgba(0,0,0,0)',)


#################################### Grafica 3
grafica3 = px.line(covid, x = covid['nom_mun'], y = covid['quincena2'])
grafica3.update_traces(orientation = 'v')
grafica3.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 2</b>',
                       template = 'simple_white',
                       title_font_family="Montserrat",
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       title_font_color="goldenrod",)


################################### Grafica 4
grafica4 = px.line(covid, x = covid['nom_mun'], y = covid['quincena3'])
grafica4.update_traces(orientation = 'v')
grafica4.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 3</b>',
                       template='simple_white',
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       title_font_family="Montserrat",
                       title_font_color="goldenrod",)


############################################ Grafica 5
grafica5 = px.line(covid, x = covid['nom_mun'], y = covid['quincena4'])
grafica5.update_traces(orientation = 'v')
grafica5.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 4</b>',
                       template='simple_white',
                       paper_bgcolor='rgba(0,0,0,0)', #Hace transparente el borde de la gráfica 
                       title_font_family="Montserrat",
                       plot_bgcolor='rgba(0,0,0,0)',
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
                       template='simple_white',
                       title_font_family="Montserrat", #Tipo de letra del titulo
                       title_font_color="goldenrod",
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                      #line_color= "dark"
                      ) 
grafica6.update_xaxes(title_font_family="Montserrat") #Tipo de letra de x,y


########################################### Grafica 8
grafica8 = px.scatter(covid, x='Total', y='nom_mun', size='Total', 
                      color='quincena6', title = '<b>Incidencia delictiva en alcaldias</b>',
                     template = "simple_white",
                     )

#layout = Layout(
#    paper_bgcolor='rgba(0,0,0,0)',
#    plot_bgcolor='rgba(0,0,0,0)'
#)

grafica8.update_traces(orientation = 'v')
grafica8.update_layout(
    font_family="Montserrat",
    font_color="black",
    title_font_family="Montserrat",
    font_size=12,
    title_font_color="goldenrod",
    legend_title_font_color="green",
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    
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
grafica9.update_layout(title = '<b>Delitos totales por Alcaldía</b>',
                       title_font_family="Montserrat",
                       title_font_color="goldenrod",
                       paper_bgcolor='rgba(0,0,0,0)',
                       plot_bgcolor='rgba(0,0,0,0)',
                       template='simple_white')





####################### Crear Tabla 1
#Tabla de titulos     
    
patabla2 = {'Contagios': [ covid.Total.sum() ],
            'Decesos': [ covid.quincena6.sum()],
            'Vacunados': [ covid.quincena5.sum()],             }
patabla3 = pd.DataFrame (patabla2, columns = ['Contagios', 'Decesos', 'Vacunados' ])

tabla2 = go.Figure(data=[go.Table(
#Header
    header=dict(values=list(patabla3),
            
                align=['left', 'left','left']),
                columnwidth = [2,2,2],


#Cells 
    cells=dict(values=[ patabla3.Contagios, patabla3.Decesos, patabla3.Vacunados
                      ],
              # fill_color='#e3e3e3',
               font_size=2,
               height= 80,
               align= ['left', 'left','left']))])

#HEADER
#tabla1.update_traces(header_values=3, selector=dict(type='table'))
tabla2.update_traces(header_fill_color='rgba(227,227,227,0.5)', selector=dict(type='table'))
tabla2.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla2.update_traces(header_font_size=12, selector=dict(type='table'))
tabla2.update_traces(header_font_color="black", selector=dict(type='table'))
tabla2.update_traces(header_line_color="#e3e3e3", selector=dict(type='table'))

#cells
#tabla2.update_traces(columnwidth=3, selector=dict(type='table'))
#tabla2.update_traces(cells_values=[1, patabla["Tipo de delito"], patabla.ene_20.sum()], selector=dict(type='figure'))
#tabla2.update_traces(cells_format=[], selector=dict(type='table'))
tabla2.update_traces(cells_font_size=80, selector=dict(type='table'))
tabla2.update_traces(cells_font_color= "goldenrod", selector=dict(type='table'))
tabla2.update_traces(cells_font_family= 'Montserrat',  selector=dict(type='table'))
tabla2.update_traces(cells_fill_color = 'rgba(227,227,227,0.5)', selector =dict(type="table"))
tabla2.update_traces(hoverlabel_namelength=80, selector=dict(type='table'))
tabla2.update_traces(cells_line_color= "#e3e3e3", selector=dict(type='table'))

tabla2.update_layout(paper_bgcolor='rgba(227,227,227,0.5)', #color de fondo
                    plot_bgcolor='rgba(227,227,227,0.5)',
                   #line_color = 'rgba(227,227,227,0.5)',
                    )




####################################################################################
########### Define your variables

mytitle='Añadir graficas'
tabtitle='Prueba Dash!'
githublink='https://github.com/Aeelen/exercises_pythoncitos/'
sourceurl='https://plotly.com/python/histograms/'


########### Initiate the app
app = dash.Dash()
colors = {
    'background': '#e3e3e3',
    'text': '#b38115',
    'table': 'rgba(227,227,227,0.5)'
}

server = app.server
app.title=tabtitle

########### Set up the layout

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
     

############################################################ Resumen    
           # Row 3
                    html.Div(children= 
                        [
                            html.Div(
                                [
                                    html.H1("Resumen", style={"color": '#b38115',
                                                                     'font-family': 'Montserrat',
                                                                     'textAlign': 'left',
                                                              'font_size' : 10,
                                                             'margin': '1% 0px 0px 100px', 'width':'90%',},),
                                    
                                    #html.Br([]),
                                    html.H2(
                                        "\
                                    En esta entidad, los contagios fueron más altos en las siguientes \
                                    cuatro quincenas:  en la quincena 15, en la cual destaca el municipio \
                                    Aguascalientes (1,228) con el mayor número de contagios; seguida por \
                                    la quincena 14, en la cual destaca el municipio Aguascalientes (820); \
                                    asimismo, la quincena 11 con el municipio Aguascalientes (752); finalmente,\
                                    en la quincena 8, en el cual destaca el municipio Aguascalientes (631)",
                                        style={"color": '#FFBF00',
                                              'font-family': 'Montserrat',# 'sans-serif',
                                              'textAlign': 'left',
                                               'font_size' : 80,
                                               'color': colors['text'],
                                               'margin': '1% 390px 10px 100px', 'width':'90%',
                  
                                              },
                                        className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),



############################################################  Grafica contagios
    
    
    html.Div( children = [dcc.Graph(figure=figaro)],                   ####big grap contagios
             style = {'margin': '2% 0px 0px 100px', 'width':'95%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),

        
    
        
    
############################################################   resumen 2

    
 # Segunda franja
    
    html.Div(children = [dcc.Graph(figure=grafica9)],
            style={'margin': '1% 0px 0px 100px', 'width':'40%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']
                                           }),
  

    
    html.Div(children =[dcc.Graph(figure=grafica8)],
            style={'margin': '1% 0px 0px 30px', 'width':'45%',
                  'font-family': 'Montserrat',
                  #'backgroundColor': colors['background']
                  # layout = Layout(
                  # paper_bgcolor='rgba(0,0,0,0)',
                  # plot_bgcolor='rgba(0,0,0,0)'
                  # )
                  }),

    

    
    
############################################################   resumen 3

           # Row 3
                    html.Div(children= 
                        [
                            html.Div(
                                [
                                    html.H1("Resumen", style={"color": '#b38115',
                                                                     'font-family': 'Montserrat',
                                                                     'textAlign': 'left',
                                                              'font_size' : 10,
                                                             'margin': '1% 0px 0px 120px', 'width':'80%',},),
                                    
                                    #html.Br([]),
                                    html.H2(
                                        "\
                                    En esta entidad, los contagios fueron más altos en las siguientes \
                                    cuatro quincenas:  en la quincena 15, en la cual destaca el municipio \
                                    Aguascalientes (1,228) con el mayor número de contagios; seguida por \
                                    la quincena 14, en la cual destaca el municipio Aguascalientes (820); \
                                    asimismo, la quincena 11 con el municipio Aguascalientes (752); finalmente,\
                                    en la quincena 8, en el cual destaca el municipio Aguascalientes (631)" ,
                                        style={"color": '#FFBF00',
                                              'font-family': 'Montserrat',# 'sans-serif',
                                              'textAlign': 'left',
                                               'font_size' : 80,
                                               'color': colors['text'],
                                               'margin': '1% 0px 0px 120px', 'width':'80%',
                  
                                              },
                                        #className="row",
                                    ),
                                ],
                                className="product",
                            )
                        ],
                        className="row",
                    ),

    

   ############################################################    
    
    
    html.Div( children = [dcc.Graph(id='grafica1',
              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
                       'layout': go.Layout(paper_bgcolor='rgba(0,0,0,0)',
                                           plot_bgcolor='rgba(0,0,0,0)',
                                           title='<b>Mayor incidencia delictiva<b>',
                                           barmode='group',
                                           title_font_color="goldenrod",
                                           title_font_family="Montserrat Black",
                                           #paper_bgcolor='rgb(233,233,233)',
                                           
                                          )})],
             style = {'margin': '2% 0px 0px 100px', 'width':'90%',
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

    html.Div(children = [dcc.Graph(figure=tabla2)],
             style={'width':'100%','font-family': 'Montserrat'}),

#############################################################      

  
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A('Data Source', href=sourceurl),

],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()
