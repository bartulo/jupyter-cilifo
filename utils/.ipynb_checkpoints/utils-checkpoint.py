import math

def parse_long( data ):
    deg = int(data[:2])
    dec = ((float(data[2:4]) * 1000 / 6) + float(data[4:6]) * 10 / 6) / 10000
    lon = deg + dec
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
