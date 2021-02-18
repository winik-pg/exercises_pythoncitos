import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import pandas as pd

contagios = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_20210217.csv")
decesos = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Defunciones_20210217.csv")
base = pd.read_csv('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/mun_p1_cvegeo.csv', encoding='latin-1', usecols=['Nom_Ent','nom_mun','cve_ent_mun1','cve_ent_mun2'])

#################################
#         CONTAGIOS           EDOS
#################################
#seleccion
onlyc = contagios.iloc[:,3:]
contagios['total'] = onlyc.sum(1)
#create 'total' column
contagios['total']=contagios['total'].astype(int)
#merge base-contagios
cont= pd.merge(base,contagios, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos, sort and show
contaedos = pd.DataFrame(cont.groupby(['Nom_Ent'])['total'].sum()).sort_values('total', ascending=False).head(10)
contaedos.to_csv('0000proceso.csv')
contaedos = pd.read_csv('0000proceso.csv')

#grafica
g10edosc = go.Figure()
g10edosc.add_trace(go.Bar(x=contaedos['Nom_Ent'],y=contaedos['total'],
                          orientation='h',
                #name='Contagios confirmados COVID-19',
                          marker_color='#0776a8',  # cambiar nuemeritos de rgb
                         ))
g10edosc.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='10 entidades con mayor contagios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"))


#################################
#         DECESOS             EDOS
#################################
#create total
onlyd = decesos.iloc[:,3:]
decesos['total'] = onlyd.sum(1)
decesos['total']=decesos['total'].astype(int)
#merge
dec= pd.merge(base,decesos, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos
deceedos = pd.DataFrame(dec.groupby(['Nom_Ent'])['total'].sum()).sort_values('total', ascending=False).head(10)
deceedos.to_csv('0000proceso.csv')
deceedos = pd.read_csv('0000proceso.csv')

#grafica
g10edosd = go.Figure()
g10edosd.add_trace(go.Bar(x=deceedos['Nom_Ent'],y=contaedos['total'],
                #name='Contagios confirmados COVID-19',
                marker_color='#0776a8',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))
g10edosd.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='10 entidades con mayor contagios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"))



####################################
# A P P
####################################
########### Define your variables

mytitle=''
tabtitle='COVID-19 en México'
#githublink='https://github.com/Aeelen/exercises_pythoncitos/'
#sourceurl='https://plotly.com/python/histograms/'

app = dash.Dash()
colors = {
    'background': '#e3e3e3',
    'text': '#b38115',
    'table': 'rgba(227,227,227,0.5)'
    }

server = app.server
app.title=tabtitle

#######################################  BODY  ##################################
app.layout = html.Div(children=[
    
    html.Div(children = [ dcc.Markdown(''' 
    # COVID-19 en México
    ###### Cámara de Diputados, México, 17 de febrero de 2021
    
    ''',)],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'],'width': '100%',
                  }),
# Segunda franja (Lista)
    html.Div( children = [dcc.Graph(figure=g10edosc)],                 
             style = {'margin': '0% 0px 0px 0px', 'width':'100%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),
    html.Div( children = [dcc.Graph(figure=g10edosd)],                  
             style = {'margin': '0% 0px 0px 0px', 'width':'100%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),
    
     html.Br(),
    #html.A('Data Source', href=sourceurl),

],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()
