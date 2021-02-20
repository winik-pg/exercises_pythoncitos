import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.io as pio
import numpy as np
import pandas as pd
import dash_table


###############################
# DATABASES
############################### Abre archivos

zacatecas = pd.read_csv('https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%202.%20Delitos%20Zacatecas%20(2020)_2.csv', )
covid = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/cdmx_deaths.csv")
bullet = pd.read_csv("https://raw.githubusercontent.com/fdealbam/flying-dog-beers/master/Tabla%20bullets.csv", encoding= "Latin1")

base = pd.read_csv('https://raw.githubusercontent.com/winik-pg/exercises_pythoncitos/master/mun_p1_cvegeo.csv', encoding='latin-1', usecols=['Nom_Ent','nom_mun','cve_ent_mun1','cve_ent_mun2'])
contagios = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Confirmados_20210219.csv")
decesos = pd.read_csv("https://datos.covid-19.conacyt.mx/Downloads/Files/Casos_Diarios_Municipio_Defunciones_20210219.csv")




###############################
# TRATAMIENTO 
###############################   Contagios  por día

endall = len(contagios)

#Select and sum all columns data
contagios1 = contagios.iloc[:,3:endall].sum()

# Make a DataFrame
contagios2 = pd.DataFrame(contagios1)

# index decesos 
contagios2['index'] = contagios2.index 
contagios2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)



############################### Total de contagios 
contagiostotal = contagios2.cases.sum()
###############################


###############################   Contagios por mes  
# by moths 

format = '%d-%m-%Y'
contagios2['days'] = pd.to_datetime(contagios2['days'], format=format)

# Filtering by years and months
cont_feb20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 2)]
cont_mar20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 3)]
cont_abr20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 4)]
cont_may20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 5)]
cont_jun20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 6)]
cont_jul20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 7)]
cont_ago20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 8)]
cont_sep20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 9)]
cont_oct20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 10)]
cont_nov20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 11)]
cont_dic20 = contagios2[(contagios2.days.dt.year == 2020 ) & (contagios2.days.dt.month == 12)]
cont_ene21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 1)]
cont_feb21 = contagios2[(contagios2.days.dt.year == 2021 ) & (contagios2.days.dt.month == 2)]


# Summarize by months 
contagios_feb20 = cont_feb20.cases.sum()
contagios_mar20 = cont_mar20.cases.sum()
contagios_abr20 = cont_abr20.cases.sum()
contagios_may20 = cont_may20.cases.sum()
contagios_jun20 = cont_jun20.cases.sum()
contagios_jul20 = cont_jul20.cases.sum()
contagios_ago20 = cont_ago20.cases.sum()
contagios_sep20 = cont_sep20.cases.sum()
contagios_oct20 = cont_oct20.cases.sum()
contagios_nov20 = cont_nov20.cases.sum()
contagios_dic20 = cont_dic20.cases.sum()
contagios_ene21 = cont_ene21.cases.sum()
contagios_feb21 = cont_feb21.cases.sum()
#means
####### W19.18022021.1
contagios_feb20_prom = round(cont_feb20.cases.mean())
contagios_mar20_prom = round(cont_mar20.cases.mean())
contagios_abr20_prom = round(cont_abr20.cases.mean())
contagios_may20_prom = round(cont_may20.cases.mean())
contagios_jun20_prom = round(cont_jun20.cases.mean())
contagios_jul20_prom = round(cont_jul20.cases.mean())
contagios_ago20_prom = round(cont_ago20.cases.mean())
contagios_sep20_prom = round(cont_sep20.cases.mean())
contagios_oct20_prom = round(cont_oct20.cases.mean())
contagios_nov20_prom = round(cont_nov20.cases.mean())
contagios_dic20_prom = round(cont_dic20.cases.mean())
contagios_ene21_prom = round(cont_ene21.cases.mean())
contagios_feb21_prom = round(cont_feb21.cases.mean())
####### W19.18022021.2

###############################   Contagios por dia  

endall1 = len(decesos)
decesos1 = decesos.iloc[:,3:endall1].sum().T
decesos2 = pd.DataFrame(decesos1)
decesos2['index'] = decesos2.index 
decesos2.rename(columns = {0:'cases', 'index':'days'}, inplace = True)


############################### Total de decesos 
decesos_tot = decesos2.cases.sum()
###############################


format = '%d-%m-%Y'
decesos2['days'] = pd.to_datetime(decesos2['days'], format=format)
decesos2

dec_feb20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 2)]
dec_mar20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 3)]
dec_abr20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 4)]
dec_may20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 5)]
dec_jun20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 6)]
dec_jul20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 7)]
dec_ago20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 8)]
dec_sep20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 9)]
dec_oct20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 10)]
dec_nov20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 11)]
dec_dic20 = decesos2[(decesos2.days.dt.year == 2020 ) & (decesos2.days.dt.month == 12)]
dec_ene21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 1)]
dec_feb21 = decesos2[(decesos2.days.dt.year == 2021 ) & (decesos2.days.dt.month == 2)]
#sum
decesos_feb20 = dec_feb20.cases.sum()
decesos_mar20 = dec_mar20.cases.sum()
decesos_abr20 = dec_abr20.cases.sum()
decesos_may20 = dec_may20.cases.sum()
decesos_jun20 = dec_jun20.cases.sum()
decesos_jul20 = dec_jul20.cases.sum()
decesos_ago20 = dec_ago20.cases.sum()
decesos_sep20 = dec_sep20.cases.sum()
decesos_oct20 = dec_oct20.cases.sum()
decesos_nov20 = dec_nov20.cases.sum()
decesos_dic20 = dec_dic20.cases.sum()
decesos_ene21 = dec_ene21.cases.sum()
decesos_feb21 = dec_feb21.cases.sum()
#means
####### W19.18022021.3
#decesos_feb20_prom = round(dec_feb20.cases.mean()) 
decesos_mar20_prom = round(dec_mar20.cases.mean())
decesos_abr20_prom = round(dec_abr20.cases.mean())
decesos_may20_prom = round(dec_may20.cases.mean())
decesos_jun20_prom = round(dec_jun20.cases.mean())
decesos_jul20_prom = round(dec_jul20.cases.mean())
decesos_ago20_prom = round(dec_ago20.cases.mean())
decesos_sep20_prom = round(dec_sep20.cases.mean())
decesos_oct20_prom = round(dec_oct20.cases.mean())
decesos_nov20_prom = round(dec_nov20.cases.mean())
decesos_dic20_prom = round(dec_dic20.cases.mean())
decesos_ene21_prom = round(dec_ene21.cases.mean())
decesos_feb21_prom = round(dec_feb21.cases.mean())
####### W19.18022021.4

############################### contagios totales por estado
####### W19.18022021 
onlyc = contagios.iloc[:,3:]
contagios['total'] = onlyc.sum(1)
#create 'total' column
contagios['total']=contagios['total'].astype(int)
#merge base-contagios
cont= pd.merge(base,contagios, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos, sort and show
contaedos1 = pd.DataFrame(cont.groupby(['Nom_Ent'])['total','poblacion'].sum()).sort_values('total', ascending=False)
contaedos = contaedos1.head(10)
contaedos.to_csv('0000proceso.csv')
contaedo = pd.read_csv('0000proceso.csv')
contaedos = contaedo.sort_values('total', ascending=True)

############################### contagios (tasas) por estado 
####### W19.18022021 
contaedos1['tasa']=((contaedos1.total/contaedos1.poblacion)*10000).round(2)
contaedos2=contaedos1.sort_values('tasa', ascending=True).tail(10)
contaedos2.to_csv('0000proceso.csv')
contaedos2a = pd.read_csv('0000proceso.csv')


############################### decesos totales por estado

onlyd = decesos.iloc[:,3:]
decesos['total'] = onlyd.sum(1)
decesos['total']=decesos['total'].astype(int)
#merge
dec= pd.merge(base,decesos, left_on= ["cve_ent_mun1"], right_on =["cve_ent"], how='inner')
#group by edos
deceedos1 = pd.DataFrame(dec.groupby(['Nom_Ent'])['total','poblacion'].sum()).sort_values('total', ascending=False)
deceedos = deceedos1.head(10)
deceedos.to_csv('0000proceso.csv')
deceedo = pd.read_csv('0000proceso.csv')
deceedos = deceedo.sort_values('total', ascending=True)
####### W19.18022021 

############################### decesos (tasas) por estado
deceedos1['tasa']=((deceedos1.total/deceedos1.poblacion)*10000).round(2)
deceedos2= deceedos1.sort_values('tasa', ascending=True).tail(10)
deceedos2.to_csv('0000proceso.csv')
deceedos2a = pd.read_csv('0000proceso.csv')










###############################
# GRAFICAS
###############################





############################### 1 Contagios Graph 

figaro = go.Figure()
figaro.add_trace(go.Bar(x=contagios2['days'],y=contagios2['cases'],
                #name='Contagios confirmados COVID-19',
                marker_color='firebrick'  # cambiar nuemeritos de rgb
                ))
figaro.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Contagios diarios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
    #width=1200,
    #height=500
    )



############################### 3 Decesos Graph 

figaro2 = go.Figure()
figaro2.add_trace(go.Bar(x=decesos2['days'],y=decesos2['cases'],
                #name='Contagios confirmados COVID-19',
                marker_color='slategray'  # cambiar nuemeritos de rgb
                ))
figaro2.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='',
    xaxis_tickfont_size= 6,
    yaxis=dict(
        title='Decesos diarios',
        titlefont_size=14,
        tickfont_size=12,
        titlefont_family= "Monserrat"),
    autosize=True,
    #width=1200,
    #height=500
    )




############################### 1 Titulo Contagios totales 
    
patabla2 = {'Contagios': [str(f"{contagiostotal:,d}")] }
patabla3 = pd.DataFrame (patabla2)

tabla2 = go.Figure(data=[go.Table(
#Header
    header=dict(values=list(patabla3),
                align= 'left'),

#Cells 
    cells=dict(values=[ patabla3
                      ],
              
               font_size=2,
               height= 80,
               align= 'left',
              ))])

#HEADER
tabla2.update_traces(header_fill_color='rgba(227,227,227,0.5)', selector=dict(type='table'))
tabla2.update_traces(header_font_family= "Montserrat ExtraBold", selector=dict(type='table'))
tabla2.update_traces(header_font_size=14, selector=dict(type='table'))
tabla2.update_traces(header_font_color="black", selector=dict(type='table'))
tabla2.update_traces(header_line_color="#e3e3e3", selector=dict(type='table'))

#cells
tabla2.update_traces(cells_font_size=50, selector=dict(type='table'))
tabla2.update_traces(cells_font_color= "red", selector=dict(type='table'))
tabla2.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla2.update_traces(cells_fill_color = 'rgba(227,227,227,0.5)', selector =dict(type="table"))
tabla2.update_traces(hoverlabel_namelength=80, selector=dict(type='table'))
tabla2.update_traces(cells_line_color= "#e3e3e3", selector=dict(type='table'))

tabla2.update_layout(paper_bgcolor='rgba(227,227,227,0.5)', #color de fondo
                    plot_bgcolor='rgba(227,227,227,0.5)',
                        autosize=True,
                        #width=1200,
                        #height=500
                        )






############################### 2 Titulo Decesos totales


patabla2a = {'Decesos': [str(f"{decesos_tot:,d}") ] }
patabla3a = pd.DataFrame (patabla2a)

tabla2a = go.Figure(data=[go.Table(
#Header
    header=dict(values=list(patabla3a),
                align= 'left'),

#Cells 
    cells=dict(values=[ patabla3a
                      ],
              
               font_size=2,
               height= 80,
               align= 'left',
              ))])

#HEADER
tabla2a.update_traces(header_fill_color='rgba(227,227,227,0.5)', selector=dict(type='table'))
tabla2a.update_traces(header_font_family= "Montserrat ExtraBold", selector=dict(type='table'))
tabla2a.update_traces(header_font_size=16, selector=dict(type='table'))
tabla2a.update_traces(header_font_color="black", selector=dict(type='table'))
tabla2a.update_traces(header_line_color="#e3e3e3", selector=dict(type='table'))

#cells
tabla2a.update_traces(cells_font_size=50, selector=dict(type='table'))
tabla2a.update_traces(cells_font_color= "black", selector=dict(type='table'))
tabla2a.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla2a.update_traces(cells_fill_color = 'rgba(227,227,227,0.5)', selector =dict(type="table"))
tabla2a.update_traces(hoverlabel_namelength=80, selector=dict(type='table'))
tabla2a.update_traces(cells_line_color= "#e3e3e3", selector=dict(type='table'))

tabla2a.update_layout(paper_bgcolor='rgba(227,227,227,0.5)', #color de fondo
                    plot_bgcolor='rgba(227,227,227,0.5)',
                    autosize=True,
                    #width=1200,
                    #height=500
                    )

                    




############################### 1 Cintillo CONTAGIOS mensuales

patabla6 = {
            'febrero20'   : [str(f"{contagios_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{contagios_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{contagios_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{contagios_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{contagios_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{contagios_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{contagios_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{contagios_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{contagios_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{contagios_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{contagios_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{contagios_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{contagios_feb21:,d}")],#, decesos_feb21],
                            }


patabla7 = pd.DataFrame (patabla6, columns = [#'blanc',
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])
tabla6 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla6),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[
                       patabla7.febrero20,patabla7.marzo20,patabla7.abril20,patabla7.mayo20,patabla7.junio20,patabla7.julio20,
                       patabla7.agosto20,patabla7.septiembre20,patabla7.octubre20,patabla7.noviembre20,patabla7.diciembre20,
                       patabla7.enero21,patabla7.febrero21],
               font_size=2,
               height= 25,
               align='left'),)])
#HEADER
tabla6.update_traces(header_fill_color='#284740', selector=dict(type='table'))
tabla6.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla6.update_traces(header_font_size=8, selector=dict(type='table'))
tabla6.update_traces(header_font_color="white", selector=dict(type='table'))
tabla6.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))

#cells
tabla6.update_traces(cells_font_size=14, selector=dict(type='table'))
tabla6.update_traces(cells_font_color= "lavenderblush", selector=dict(type='table'))
tabla6.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla6.update_traces(cells_fill_color = '#284740', selector =dict(type="table"))
tabla6.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla6.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla6.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
                    #line_color = 'rgba(255,255,255,0)'
    autosize=True,
    #width=1200,
    #height=500
    )






############################### 2 Cintillo DECESOS mensuales

patabla6a = {
            'febrero20'   : [str(f"{decesos_feb20:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{decesos_mar20:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{decesos_abr20:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{decesos_may20:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{decesos_jun20:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{decesos_jul20:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{decesos_ago20:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{decesos_sep20:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{decesos_oct20:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{decesos_nov20:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{decesos_dic20:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{decesos_ene21:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{decesos_feb21:,d}")],#, decesos_feb21],
                            }

patabla7a = pd.DataFrame (patabla6a, columns = [
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])
tabla6a = go.Figure(data=[go.Table(
    header=dict(values=list(patabla6a),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[#patabla7.blanc,
                       patabla7a.febrero20,patabla7a.marzo20,     patabla7a.abril20,patabla7a.mayo20,patabla7a.junio20,patabla7a.julio20,
                       patabla7a.agosto20, patabla7a.septiembre20,patabla7a.octubre20,patabla7a.noviembre20,patabla7a.diciembre20,
                       patabla7a.enero21,  patabla7a.febrero21],
               font_size=2,
               height= 25,
               align='left'), 
               )])

#HEADER
tabla6a.update_traces(header_fill_color='#284740', selector=dict(type='table'))
tabla6a.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla6a.update_traces(header_font_size=8, selector=dict(type='table'))
tabla6a.update_traces(header_font_color="white", selector=dict(type='table'))
tabla6a.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))

#cells
tabla6a.update_traces(cells_font_size=14, selector=dict(type='table'))
tabla6a.update_traces(cells_font_color= "lavenderblush", selector=dict(type='table'))
tabla6a.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla6a.update_traces(cells_fill_color = '#284740', selector =dict(type="table"))
tabla6a.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla6a.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla6a.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
                    #line_color = 'rgba(255,255,255,0)'
    autosize=True,
    #width=1200,
    #height=500
    )




############################### 3 Cintillo Promedio mensuales de Contagios

patabla8 = {
            'febrero20'   : [str(f"{contagios_feb20_prom:,d}")],#, decesos_feb20],
            'marzo20'     : [str(f"{contagios_mar20_prom:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{contagios_abr20_prom:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{contagios_may20_prom:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{contagios_jun20_prom:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{contagios_jul20_prom:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{contagios_ago20_prom:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{contagios_sep20_prom:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{contagios_oct20_prom:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{contagios_nov20_prom:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{contagios_dic20_prom:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{contagios_ene21_prom:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{contagios_feb21_prom:,d}")],#, decesos_feb21],
                            }

patabla9= pd.DataFrame (patabla8, columns = [#'blanc',
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])
tabla8 = go.Figure(data=[go.Table(
    header=dict(values=list(patabla8),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[
                       patabla9.febrero20,patabla9.marzo20,patabla9.abril20,patabla9.mayo20,patabla9.junio20,patabla9.julio20,
                       patabla9.agosto20,patabla9.septiembre20,patabla9.octubre20,patabla9.noviembre20,patabla9.diciembre20,
                       patabla9.enero21,patabla9.febrero21],
               font_size=2,
               height= 25,
               align='left'),)])
#HEADER
tabla8.update_traces(header_fill_color='#7B878D', selector=dict(type='table'))
tabla8.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla8.update_traces(header_font_size=8, selector=dict(type='table'))
tabla8.update_traces(header_font_color="white", selector=dict(type='table'))
tabla8.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))
#cells
tabla8.update_traces(cells_font_size=14, selector=dict(type='table'))
tabla8.update_traces(cells_font_color= "lavenderblush", selector=dict(type='table'))
tabla8.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla8.update_traces(cells_fill_color = '#7B878D', selector =dict(type="table"))
tabla8.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla8.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla8.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
    autosize=True,
    #width=1200,
    #height=500
    )





############################### 3 Cintillo Promedio mensuales de Decesos

patabla8a = {
            'febrero20'   : ["0"], #, decesos_feb20],
            'marzo20'     : [str(f"{decesos_mar20_prom:,d}")],#, decesos_mar20],
            'abril20'     : [str(f"{decesos_abr20_prom:,d}")],#, decesos_abr20],
            'mayo20'      : [str(f"{decesos_may20_prom:,d}")],#, decesos_may20],
            'junio20'     : [str(f"{decesos_jun20_prom:,d}")],#, decesos_jun20],
            'julio20'     : [str(f"{decesos_jul20_prom:,d}")],#, decesos_jul20],
            'agosto20'    : [str(f"{decesos_ago20_prom:,d}")],#, decesos_ago20],
            'septiembre20': [str(f"{decesos_sep20_prom:,d}")],#, decesos_sep20],
            'octubre20'   : [str(f"{decesos_oct20_prom:,d}")],#, decesos_oct20],
            'noviembre20' : [str(f"{decesos_nov20_prom:,d}")],#, decesos_nov20],
            'diciembre20' : [str(f"{decesos_dic20_prom:,d}")],#, decesos_dic20],
            'enero21'     : [str(f"{decesos_ene21_prom:,d}")],#, decesos_ene21],
            'febrero21'   : [str(f"{decesos_feb21_prom:,d}")],#, decesos_feb21],
                            }

patabla9a = pd.DataFrame (patabla8a, columns = [
                                              'febrero20','marzo20','abril20','mayo20','junio20','julio20',
                                              'agosto20','septiembre20','octubre20','noviembre20','diciembre20',
                                              'enero21','febrero21'])

tabla8a = go.Figure(data=[go.Table(
    header=dict(values=list(patabla8a),
                align=['left']),
                columnwidth = 2,
    
    cells=dict(values=[#patabla7.blanc,
                       patabla9a.febrero20,patabla9a.marzo20,patabla9a.abril20,patabla9a.mayo20,patabla9a.junio20,patabla9a.julio20,
                       patabla9a.agosto20,patabla9a.septiembre20,patabla9a.octubre20,patabla9a.noviembre20,patabla9a.diciembre20,
                       patabla9a.enero21,patabla9a.febrero21],
               font_size=2,
               height= 25,
               align='left'),)])
#HEADER
tabla8a.update_traces(header_fill_color='#7B878D', selector=dict(type='table'))
tabla8a.update_traces(header_font_family= "Montserrat", selector=dict(type='table'))
tabla8a.update_traces(header_font_size=8, selector=dict(type='table'))
tabla8a.update_traces(header_font_color="white", selector=dict(type='table'))
tabla8a.update_traces(header_line_color='rgba(255,255,255,0)', selector=dict(type='table'))

#cells
tabla8a.update_traces(cells_font_size=14, selector=dict(type='table'))
tabla8a.update_traces(cells_font_color= "lavenderblush", selector=dict(type='table'))
tabla8a.update_traces(cells_font_family= 'Montserrat ExtraBold',  selector=dict(type='table'))
tabla8a.update_traces(cells_fill_color = '#7B878D', selector =dict(type="table"))
tabla8a.update_traces(hoverlabel_namelength=13, selector=dict(type='table'))
tabla8a.update_traces(cells_line_color= "rgba(255,255,255,0)", selector=dict(type='table'))

tabla8a.update_layout(paper_bgcolor='rgba(255,255,255,0)', #color de fondo
                    plot_bgcolor='rgba(255,255,255,0)',
    autosize=True,
    #width=1200,
    #height=500
    )






##############
# SEGUNDA SECCION 

############################### Gráfica CONTAGIOS por estado

g10edosc = go.Figure()
g10edosc.add_trace(go.Bar(x=contaedos['total'],y=contaedos['Nom_Ent'],
                          orientation='h',
                #name='Contagios confirmados COVID-19',
                          marker_color='firebrick',
                         ))
g10edosc.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Más contagios',
    font_color= 'black',
    xaxis_tickfont_size= 9,
    #xaxis_tickfont_color= "goldenrod",
    yaxis=dict(
        #title='',
        titlefont_size=8,
        tickfont_size=10,
        titlefont_family= "Monserrat  ExtraBold",
        ),
     autosize=False,
     width= 250,
     height=500
                     )



############################### Gráfica decesos por estado

g10edosd = go.Figure()
g10edosd.add_trace(go.Bar(x=deceedos['total'],y=contaedos['Nom_Ent'],
                #name='Contagios confirmados COVID-19',
                marker_color='black',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))
g10edosd.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Más decesos',
    font_color= 'black',
    xaxis_tickfont_size= 9,
    yaxis=dict(
        title='',
        titlefont_size=8,
        tickfont_size=10,
        titlefont_family= "Monserrat ExtraBold"),
    autosize=False,
    width= 250,
    height=500
                     )



############################### Gráfica TASA de contagios por estado

g10edosct = go.Figure()
g10edosct.add_trace(go.Bar(x=contaedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                          orientation='h',
                #name='Contagios confirmados COVID-19',
                          marker_color='palevioletred',
                         ))
g10edosct.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa de contagios',
    font_color= 'black',
    xaxis_tickfont_size= 9,
    #xaxis_tickfont_color= "goldenrod",
     yaxis=dict(
        title='',
        titlefont_size=8,
        tickfont_size=10,
        titlefont_family= "Monserrat ExtraBold"),
    autosize=False,
    width= 250,
    height=500
                     )




############################### Gráfica TASA de decesos por estado
    
g10edosdt = go.Figure()
g10edosdt.add_trace(go.Bar(x=deceedos2a['tasa'],y=contaedos2a['Nom_Ent'],
                #name='Contagios confirmados COVID-19',
                marker_color='slategray',
                orientation='h'          
                # cambiar nuemeritos de rgb
                ))
g10edosdt.update_layout(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
    xaxis_tickangle=-45,
    template = 'simple_white',
    title='Tasa de letalidad',
    font_color= 'black',
    xaxis_tickfont_size= 9,
    yaxis=dict(
        title='',
        titlefont_size=8,
        tickfont_size=10,
        titlefont_family= "Monserrat ExtraBold"),
    autosize=False,
    width= 250,
    height=500
                     )










####################################

# A P P

####################################

########### Define your variables

mytitle=''
tabtitle='COVID-19 en México'
githublink='https://github.com/Aeelen-Miranda/exercises_pythoncitos/blob/master/app.py'
sourceurl='https://plotly.com/python/histograms/'


app = dash.Dash()
colors = {
    'background': '#e3e3e3',
    'text': '#b38115',
    'table': 'rgba(227,227,227,0.5)'
    }

server = app.server
app.title=tabtitle


#################################### TITULOS GENERALES DE APP

app.layout = html.Div(children=[
    
    html.Div(children = [ dcc.Markdown(''' 
    ###### Secretaría de Servicios Parlamentarios, Cámara de Diputados, México, 17 de febrero de 2021
    # COVID-19 en México
    ''',)],style={'font-family': 'Montserrat',# 'sans-serif',
                  'textAlign': 'center','color': colors['text'], 
                  #'height' : '-10px',
                  'margin': '0% 0px -1% 0px',
                  'interwidth' : -1,
                  'width': '100%',
                  }, ), 

    
    

#################################### DISEÑO DE APP

################    
# PRIMERA FRANJA     
################
    
    
# Franja Cifra total contagios
    
    html.Div(children = [dcc.Graph(figure=tabla2)],
             style={'margin': '0% 0px -500px 70px', 'width':'50%',  
                    'font-family': 'Montserrat'}),
                  

# Franja Gráfica contagios
    
    html.Div( children = [dcc.Graph(figure=figaro)],                  
             style = {'margin': '0% 0px 0px 0px', 'width':'100%',
                     'font-family': 'Montserrat', 
                    }),

    

    
    
#corregir
    
# Cintillo 1 Cifras mensuales de contagios
    
    html.Div(children = [dcc.Graph(figure=tabla6)],
             style={
            # para celular
                 #'margin': '-63.6% 0px -50% 55px', 'width':'100%',  
            # para web 
                 'margin': '-17.8% 0px -20% 0px', 'width':'100%',                                                                             
                #
               #  'margin': '-41.8% 0px -50% 55px', 'width':'100%',                                                                             
                    'font-family': 'Montserrat'}),

    
    
# Cintillo 1 titulo (promedio mensuales)
    
    html.Div(children='Promedio de contagios mensuales',
              style={
                  'textAlign': 'left',
                  'font-family': 'Montserrat ExtraBold',
                  "font_size": 16,
                  'color': 'brown',
                  'margin': '-7% 0px 0% 80px', 'width':'100%',}),  

    
# Cintillo 2 Promedio mensuales de contagios
    
    html.Div(children = [dcc.Graph(figure=tabla8)],
             style={
                  'textAlign': 'left',
                  'font-family': 'Montserrat',
                  'color': 'brown',
                  'margin': '-14.2% 0px -10% 0px', 'width':'100%',  
    }),
    
 
    
 
################    
# SEGUNDA FRANJA     
################
   
    
# false  Franja cifra total de decesos
    
    html.Div(children = [dcc.Graph(figure=tabla2a)],
             style={'margin': '-20% 0px 0px 70px', 'width':'50%',  
                    'font-family': 'Montserrat'}),

        
# Franja Gráfica de decesos 
    
    html.Div( children = [dcc.Graph(figure=figaro2)],                  
             style = {'margin': '-50% 0px 0px 0px', 'width':'100%',
                     'font-family': 'Montserrat', 
                    }),


# Cintillo 1 Cifras mensuales de decesos
    
    html.Div(children = [dcc.Graph(figure=tabla6a)],
             style={#
             # para celular
                    #'margin': '-18% 0px 0% 55px', 'width':'100%',
             # para web 
                 'margin': '-20% 0px -20% 0px', 'width':'100%',                                                                             
                    'font-family': 'Montserrat'}),
    
    
# Cintillo 1 titulo (promedio mensuales) Decesos
    
     html.Div('Promedio de decesos mensuales',
              style={
                  'textAlign': 'left',
                  'font-family': 'Montserrat ExtraBold',
                  "font_size": 16,
                  'color': 'brown',
                  'margin': '-7% 0px 0% 80px', 'width':'100%',} ),


# Cintillo 2 Cifras mensuales de decesos

    html.Div(children = [dcc.Graph(figure=tabla8a)],
             style={
                  'textAlign': 'left',
                  'font-family': 'Montserrat',
                  'color': 'brown',
                  'margin': '-15% 0px 0% 0px', 'width':'100%',  
    }),
    
    
    

    

    

    

    
################    
# TERCERA FRANJA
################
   
    
    
# Franja Gráfica de Contagios 10 entidades

    html.Div( children = [dcc.Graph(figure=g10edosc)],                 
             style = {'margin': '-20% 0px 10px 0px', 'width':'24%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),


# Franja Gráfica de TASA Contagios 10 entidades

    html.Div( children = [dcc.Graph(figure=g10edosct)],                 
             style = {'margin': '-20% 0px 10px 0px', 'width':'24%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),
    
    
    
# Franja Gráfica de Decesos 10 entidades
    
    html.Div( children = [dcc.Graph(figure=g10edosd)],                  
             style = {'margin': '-20% 0px 10px 0px', 'width':'24%',
                     'font-family': 'Montserrat', 
                     #'fontColor': 'goldenrod' #Cambia tipo de letra
                    }),

    
# Franja Gráfica de TASA Decesos 10 entidades
    html.Div( children = [dcc.Graph(figure=g10edosdt)],                  
             style = {'margin': '-20% 0px 10px 0px', 'width':'24%',
                     'font-family': 'Montserrat', 
                    }),
    

    
    

    
    

    
    
    
    
    

#############################################################      

  
    #html.A('Code on Github', href=githublink),
    html.Br(),
    #html.A('Data Source', href=sourceurl),

],style={'display': 'flex','flex-direction': 'row','flex-wrap': 'wrap','overflow': 'hidden',
        'font-family': 'Montserrat','backgroundColor': colors['background']}, #Color de fondo dash
                     # dark=True,
                     )
                     

if __name__ == '__main__':
    app.run_server()




#autosize=True,
# Elegir colores CSS
#https://developer.mozilla.org/es/docs/Web/CSS/CSS_Colors/Herramienta_para_seleccionar_color

