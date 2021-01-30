import plotly.express as px
import os
import geopandas as gpd
import pandas as pd
import plotly.graph_objects as go
import seaborn as sbn
import dash
import dash_core_components as dcc
import dash_html_components as html
import folium
import dash_table
import dash_bootstrap_components as dbc
from datetime import date

# Abrir BD
os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")
mun = gpd.read_file('00mun.shp') #Para mapas
base = pd.read_csv('Tabla 1. Variación mensual (AÑO ANTERIOR) (mapas).csv')#, encoding= "Utf-8") #Para mapa

cdmx_delit = pd.read_excel('cdmx deaths.xlsx')  #Para gráfica
df2= pd.read_csv("Tabla 2. Delitos Zacatecas (2020)_2.csv")#, encoding= "Latin-1")

#crear tabla David

pv = pd.pivot_table(df2, index=['Municipio'], columns=['Tipo de delito'], values=['ene-20'],aggfunc=sum, fill_value = 0)

g1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Robo')], name = 'ROBO')
gr1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Violencia familiar')], name = 'VIOLENCIA FAMILIAR')
gra1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Lesiones')], name = 'LESIONES')
graf1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Otros delitos del Fuero Común')], name = 'OTROS DELITOS DEL FUERO COMÚN')
grafi1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Daño a la propiedad')], name = 'DAÑO A LA PROPIEDAD')
grafic1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Fraude')], name = 'FRAUDE')
grafica1 = go.Bar(x=pv.index, y=pv[('ene-20', 'Amenazas')], name = 'AMENAZAS')

# Display figure

grafica2 = px.line(cdmx_delit, x = cdmx_delit['nom_mun'], y = cdmx_delit['quincena0'])
grafica2.update_traces(orientation = 'v')
grafica2.update_layout(font_family="Montserrat",title = '<b>Quincena 0</b>',
                       template = 'plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod",)

grafica3 = px.line(cdmx_delit, x = cdmx_delit['nom_mun'], y = cdmx_delit['quincena2'])
grafica3.update_traces(orientation = 'v')
grafica3.update_layout(font_family="Montserrat",
                       title = '<b>Quincena 2</b>',
                       template = 'plotly_dark',
                       title_font_family="Montserrat",
                       title_font_color="goldenrod",)

grafica4 = px.line(cdmx_delit, x = cdmx_delit['nom_mun'], y = cdmx_delit['quincena3'])
grafica4.update_traces(orientation = 'v')
grafica4.update_layout(font_family="Montserrat",title = '<b>Quincena 3</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                      title_font_color="goldenrod",)

grafica5 = px.line(cdmx_delit, x = cdmx_delit['nom_mun'], y = cdmx_delit['quincena4'])
grafica5.update_traces(orientation = 'v')
grafica5.update_layout(font_family="Montserrat",title = '<b>Quincena 4</b>',
                      template='plotly_dark',title_font_family="Montserrat",
                       title_font_color="goldenrod", )
grafica5.update_xaxes(title_font_family="Montserrat")


grafica6 = px.line(cdmx_delit, x = cdmx_delit['nom_mun'], y = cdmx_delit['quincena5']) # , color= "nom_mun")

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


#Grafica8
grafica8 = px.scatter(cdmx_delit, x='Total', y='nom_mun', size='Total', 
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
grafica8.show()



#Grafica 9


eindex = cdmx_delit[['nom_mun','Total' ,'quincena0', 'quincena2',
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

# 1. SHAPE
#conversión dtype
mun['CVEGEO'] = mun['CVEGEO'] .astype(int)  #shape
base['Cve. Municipio'] = base['Cve. Municipio'] .astype(int)      #BD

#merge de archivo shp y base
mun_y_base = pd.merge(mun, base, left_on= "CVEGEO", right_on= 'Cve. Municipio', how='inner' )#, validate='one_to_many')

#Rename
munybase = mun_y_base.rename(columns={"CVE_MUN": "municipio"})

#filtro (para hacer un estado)
#entmap1 = rename[(rename.municipio == '09')] #modificar estado name
#                             # más filtros
#    
munybase.to_csv("Prueba.csv")
data = pd.read_csv("Prueba.csv")

# 2. JSON
import json
os.chdir(r"C:\Users\PRIME\AnacondaProjects\Project_curso\\")

#Abre Json
with open('alcaldias.geojson') as response:
    geojson = json.load(response)

#Muestra atributos de Json
geojson["features"][0]

# Creacion de geodataframe
geo_df = gpd.GeoDataFrame.from_features(geojson["features"])
#merge = geo_df.merge(data, on="municipio").set_index("municipio")
concat = pd.concat([geo_df, data], join="outer")
mapa1 = px.choropleth_mapbox(concat,
                           geojson=geo_df.geometry,
                           locations=concat.index,
                           color="var_febrero",
                           center={"lat": 19.34508941956005, "lon": -99.15325161549731},
                           mapbox_style="open-street-map",
                           zoom=8.5,
                           opacity=0.5,
                           title = '<b>Variaciones Febrero</b>',
                           
                          # font_family="Montserrat",title_font_color="goldenrod",
                 )
mapa1.update_layout(paper_bgcolor='black', #color de fondo
                    plot_bgcolor='black')

mapa2 = px.choropleth_mapbox(concat, geojson=geo_df, locations='municipio', color='var_abril',
                           color_continuous_scale="Viridis",
                           range_color=(0, 12),
                           mapbox_style="carto-positron",
                           zoom=8.5, 
                           center = {"lat": 19.34508941956005, "lon": -99.15325161549731},
                           opacity=0.5,
                           title = '<b>Variaciones Abril</b>',

                          )
mapa2.update_layout(paper_bgcolor='black', #color de fondo
                    plot_bgcolor='black')
#                    title = '<b>Variaciones abril</b>')

#Tabla 1
ptabla = df2.rename(columns={'ene-20': "ene_20", "feb-20": "feb_20",'mar-20': "mar_20",
                                'abr-20': "abr_20",'may-20':"may_20", 'jun-20':"jun_20",
                                'jul-20':"jul_20", 'ago-20': "ago_20",  'sep-20':"sep_20" })

#patabla = paabla.loc[2:, :][paabla["Tipo de delito"]== "Robo"]
patabla = ptabla.iloc[:, 1:12]

tabla1 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla),
                fill_color='lightgrey',
                align='left'),
                #columnwidth = [800,400],
#                align= ['left','left'],

                #font=dict(color='white', size=12),

    cells=dict(values=[  patabla.Municipio, patabla["Tipo de delito"], 
                       patabla.ene_20, patabla.feb_20, patabla.mar_20, patabla.abr_20, 
                       patabla.may_20, patabla.jun_20, patabla.jul_20,patabla.ago_20, 
                       patabla.sep_20, #, patabla.Grado, patabla.Estatus, patabla.hrs_caso
                      ],
               fill_color='white',
               font_size=13,
               height= 30,
                font = dict(color = 'black', size = 10),
               align= ['left','left'],))
])
    
#    font = dict(family="Montserrat",
#        size=18,
#        color="Golden"))


#HEADER
#tabla1.update_traces(header_values=3, selector=dict(type='table'))
tabla1.update_traces(header_fill_color="black", selector=dict(type='table'))
tabla1.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla1.update_traces(header_font_size=13, selector=dict(type='table'))
tabla1.update_traces(header_font_color="goldenrod", selector=dict(type='table'))

#cells
#tabla1.update_traces(columnwidth=3, selector=dict(type='table'))
#tabla1.update_traces(cells_values=[1, patabla["Tipo de delito"], patabla.ene_20.sum()], selector=dict(type='figure'))
#tabla1.update_traces(cells_format=[], selector=dict(type='table'))
tabla1.update_traces(cells_font_size=10, selector=dict(type='table'))
tabla1.update_traces(cells_font_color= "white", selector=dict(type='table'))
tabla1.update_traces(cells_fill_color= "black", selector=dict(type='table'))
tabla1.update_traces(cells_font_family= "Montserrat", selector=dict(type='table'))
tabla1.update_traces(hoverlabel_namelength=50, selector=dict(type='table'))
#tabla1.update_traces(backgroundColor = "black", selector=dict(type='table'))
tabla1.update_xaxes(title_font_family="Montserrat",selector=dict(type='scattermapbox'))
tabla1.update_traces(hoverlabel_bgcolor="black",selector=dict(type='scattermapbox'))


#Tabla 2
patabla2 = {'Rubro':  ['Total', "Promedio", 'Máximo', 'Mínimo'],
        'Enero_20': [ptabla.ene_20.sum(), ptabla.ene_20.mean(), ptabla.ene_20.max(), ptabla.ene_20.min()]         }

patabla3 = pd.DataFrame (patabla2, columns = ['Rubro','Enero_20'])


    
tabla2 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla3),
                fill_color='black',
                align='left'),
                columnwidth = [0.5, 3],
#                align= ['left','left'],
                #font=dict(color='black', size=12),

#Cells 
    
    cells=dict(values=[ patabla3.Rubro, patabla3.Enero_20
                      ],
               fill_color='black',
               font_size=12,
               height= 25,
    #         font = {'family': 'serif',
    #  'color':  'darkred',
    #  'weight': 'normal',
    #  'size': 16,
    #  },
    #         #font = dict(color = 'white', size = 10),
               #style_column = 30px,
               align= ['right','left'],
             # style="background-color:Red"
              )
              )
               ])
#HEADER
#tabla1.update_traces(header_values=3, selector=dict(type='table'))
tabla2.update_traces(header_fill_color="black", selector=dict(type='table'))
tabla2.update_traces(header_font_family= "Montserrat ExtraBold", selector=dict(type='table'))
tabla2.update_traces(header_font_size=13, selector=dict(type='table'))
tabla2.update_traces(header_font_color="gold", selector=dict(type='table'))


#cells
#tabla2.update_traces(columnwidth=3, selector=dict(type='table'))
#tabla2.update_traces(cells_values=[1, patabla["Tipo de delito"], patabla.ene_20.sum()], selector=dict(type='figure'))
#tabla2.update_traces(cells_format=[], selector=dict(type='table'))
tabla2.update_traces(cells_font_size=12, selector=dict(type='table'))
tabla2.update_traces(cells_font_color= "lightsalmon", selector=dict(type='table'))
tabla2.update_traces(cells_font_family= 'Montserrat',  selector=dict(type='table'))
tabla2.update_traces(cells_fill_color = "black", selector =dict(type="table"))
tabla2.update_traces(hoverlabel_namelength=50, selector=dict(type='table'))

#Dash
app = dash.Dash()
colors = {
    'background': '#111111',
    'text': '#C0C0C0'
}


# Titulo de la página  ############################################################


app.title = 'Analytics Dashboard'
app.layout = html.Div(children=[
    #style={'backgroundColor':'blue'}),
#app.layout = html.Div(#style={'backgroundColor': colors['background']},
   # 
   #  html.H1(
   #     children='Hello Dash',
   #     style={
   #         'textAlign': 'center',
   #         'color': colors['text']
   #     }
   # ),
    html.Div(children = [ 
    dbc.NavbarSimple(
        children=[
        dbc.NavItem(dbc.NavLink("Web Portal",
                                style={'textAlign': 'center','color': colors['text']},
                                       href="https://plotly.com/python/figure-labels/")),
        ],
        brand="Analytics Dashboard",
        brand_href="https://matplotlib.org/gallery/api/font_family_rc_sgskip.html",
        color="#E3E4E5",
        dark=True,)],
        style={'textAlign': 'center','color': colors['text'],
               'font-family': 'Montserrat', 'font-weight': 'bold','width': '100%',},
        ),
#app.layout = html.Div(children=[
    html.Div(children = [ dcc.Markdown(
        ''' 
    # Segunda GRAN prueba de Dashboard
    ## prueba sobre delitos
    ###### jueves 28 de enero de 2020
''',
       #brand="PRIMEra prueba de Dashboard",
       #brand_href="#",
       #color="#FFE5B4",
       #dark=True,
        )],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%'}
        ),
     
    
#GRAFICAS O MAPAS   #####################################################################
#primera franja
    
    html.Div( children = [dcc.Graph(id='grafica1',
              figure= {'data':[g1,gr1,gra1,graf1,grafi1,grafic1,grafica1],
                       'layout': go.Layout(paper_bgcolor='black', #color de fondo
                                           plot_bgcolor='black',
                                           title='Mayor incidencia delictiva',
                                           barmode='group')})],
             style = {'margin': '1% 0px 0px 0px', 'width':'60%',
                     'font-family': 'Montserrat',#Cambia tipo de letra
                    }), #Fondo de grafico
#segunda franja
    html.Div(children = [dcc.Graph(style={'backgroundColor': colors['background']},
                                   figure=tabla2)],
             style={'margin': '1% 0px 0px 0px', 'width':'35%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),
    
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

#cuarta franja
    html.Div(children = [dcc.Graph(figure=mapa1)],
            style={'margin': '4% 0px 0px 0px', 'width':'35%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),

#    html.Div(children = [dcc.Graph(figure=grafica7)],
#            style={'margin': '2% 0px 0px 0px', 'width':'30%'}),
    html.Div(children =[dcc.Graph(figure=grafica8)],
             style={'margin': '2% 0px 0px 0px', 'width':'60%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']}),

#quinta franja
    html.Div(children = [dcc.Graph(figure=grafica9)],
            style={'margin': '2% 0px 0px 0px', 'width':'100%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),

#sexta franja    
    html.Div(children = [dcc.Graph(figure=mapa2)],
            style={'margin': '2% 0px 0px 0px', 'width':'50%',
                  'font-family': 'Montserrat',
                  'backgroundColor': colors['background']}),

    html.Div(children = [dcc.Graph(figure=tabla1)],
             style={'margin': '2% 0px 0px 0px', 'width':'50%',
                   'font-family': 'Montserrat',
                   'backgroundColor': colors['background']})
#
    
],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )



if __name__ == '__main__':
    app.run_server(debug=True, use_reloader=False)
    app.server.static_folder = 'static'  
