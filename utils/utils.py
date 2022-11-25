import math

def dirviento_viento(d, a):
    for i, viento in enumerate(d['windArrows']):
          #ax[1].scatter(i, velviento_10m[i], marker=fleviento[i], color='g') # para que aparezcan las flechas sobre la curva
        a.scatter(i, d['windgusts_10m'].max() + 0.5, marker=viento, s=150 ,color='r') # para que aparezcan en linea en la parte de arriba de la gráfica
    a.set_ylabel('Dirección del Viento', multialignment='center')
    a.grid(axis='both', color='k', linestyle='--', linewidth=0.3)
    # a.set_ylim(0.5,l)
    # a.set_yticks(range(0, len(model)+1))

    a.plot(d['windgusts_10m'], 'red')
    a.plot(d['windspeed_10m'], 'orange', label='Viento 10m ')
    a.set_xticks(range(0, len(d['hora']), 3))
    a.set_xticklabels(list(d['hora'])[0::3])
    a.set_ylabel('Velocidad del Viento (km/h)', multialignment='center')
    a.grid(axis='both', color='k', linestyle='--', linewidth=0.3)
    a.legend(loc = 'upper right')
    
def temp_simple(d, a):
    ax2 = a.twinx()
    a.plot(d['temperature_2m'], 'r', label='Temperatura ')
    a.plot(d['dewpoint_2m'], 'g', linewidth=0.8, label='Punto de rocío ')
    ax2.plot(d['relativehumidity_2m'], 'b', label='Humedad relativa')
    ax2.legend(loc='upper right')
    a.set_ylabel('Temperatura (ºC)', multialignment='center')
    a.set_ylim(-10, 40)
    a.set_xticks(range(0, len(d['hora']), 3))
    a.set_xticklabels(list(d['hora'])[0::3])
    ax2.set_ylabel('Humedad relativa (%)', multialignment='center')
    ax2.set_ylim(0,100)
    a.grid(axis='both', color='k', linestyle='--', linewidth=0.3)

def hcfm_plot_simple(d, a): #He cambiado el nombre de la función porque le habías dado el mismo que el objeto lista hcfm
    ax3 = a.twinx()
    a.plot(d['hcfm'], 'maroon', label='HCFM ')
    ax3.plot(d['probIg'], 'lawngreen', label='Prob Ig ')
    a.set_ylabel('Humedad Combustible Fino Muerto (%)', multialignment='center')
    a.set_ylim(0, 30)
    ax3.set_ylabel('Probabilidad de ignición (%)', multialignment='center')
    ax3.set_ylim(0,100)
    a.grid(axis='both', color='k', linestyle='--', linewidth=0.3)
    a.legend(loc = 'upper right')

def parse_long( data ):
    deg = int(data[:2])
    dec = ((float(data[2:4]) * 1000 / 6) + float(data[4:6]) * 10 / 6) / 10000
    lon = deg + dec
    if data[-1] == 'W':
        lon = lon * (-1)
    return lon

def get_tr(data):
  if data < 10:
    tr = 't10'
  elif data < 21:
    tr = 't21'
  elif data < 32:
    tr = 't32'
  elif data < 43:
    tr = 't43'
  else:
    tr = 'tmax'
  return tr

def get_dia_noche(hora):
  if hora >= '08:00' and hora < '20:00':
    periodo = 'dia'
  else:
    periodo = 'noche'
  return periodo  

def get_hcfm(hora, temp, hr):
  Tabla_hcfm = {'dia':{'t10':[1,2,2,3,4,5,5,6,7,7,7,8,9,9,10,10,11,12,13,13,13],
              't21':[1,2,2,3,4,5,5,6,6,7,7,8,8,9,9,10,11,12,12,12,13],
              't32':[1,1,2,2,3,4,5,5,6,7,7,8,8,8,9,10,10,11,12,12,13],
              't43':[1,1,2,2,3,4,4,5,6,7,7,8,8,8,9,10,10,11,12,12,13],
              'tmax':[1,1,2,2,3,4,4,5,6,7,7,8,8,8,9,10,10,11,12,12,13]},
              'noche':{'t10':[1,2,3,4,5,6,7,8,9,9,11,11,12,13,14,16,18,21,24,25,25],
              't21':[1,2,3,4,5,6,6,8,8,9,10,11,11,12,14,16,17,20,23,25,25],
              't32':[1,2,3,4,4,5,6,7,8,9,10,10,11,12,13,15,17,20,23,25,25],
              't43':[1,2,3,3,4,5,6,7,8,9,9,10,10,11,13,14,16,19,22,25,25],
              'tmax':[1,2,2,3,4,5,6,6,8,8,9,9,10,11,12,14,16,19,21,24,25]}}


  d_n = get_dia_noche(hora)
  t = get_tr(temp)
  h = math.floor(hr/5)

  return Tabla_hcfm[d_n][t][h]

def get_windarrows(wind):
  E = r'$\leftarrow$'
  S = r'$\uparrow$'
  W = r'$\rightarrow$'
  N = r'$\downarrow$'
  SE = r'$\nwarrow$'
  SW = r'$\nearrow$'
  NW = r'$\searrow$'
  NE = r'$\swarrow$'

  if wind == None:
    viento = None  
  elif wind <= 22.5:
    viento = N
  elif wind <= 67.5:
    viento = NE
  elif wind <= 112.5:
    viento = E
  elif wind <= 157.5:
    viento = SE
  elif wind <= 202.5:
    viento = S
  elif wind <= 247.5:
    viento = SW
  elif wind <= 292.5:
    viento = W
  elif wind <= 337.5:
    viento = NW
  elif wind > 337.5:
    viento = N

  return viento  

def get_probig(temp, hcfm):
  Tabla_ProbIg = [[90,70,60,60,50,40,40,30,30,20,20,20,10,10,10,10],
                [90,70,60,60,50,40,40,30,30,20,20,20,10,10,10,10],
                [90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],
                [90,80,70,60,50,40,40,30,30,20,20,20,10,10,10,10],
                [100,80,70,60,60,50,40,40,30,30,20,20,20,10,10,10],
                [100,90,80,70,60,50,40,40,30,30,20,20,20,20,10,10],
                [100,90,80,70,60,50,50,40,30,30,30,20,20,20,10,10],
                [100,90,80,70,60,60,50,40,40,30,30,20,20,20,10,10],
                [100,100,90,80,70,60,50,40,40,30,30,30,20,20,20,10]]
  temp = max(0, temp)
  hcfm = min(17, hcfm)

  t = math.floor(temp/5)
  h = hcfm -2

  return Tabla_ProbIg[t][h]
