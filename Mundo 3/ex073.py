times = ("Flamengo","Santos","Palmeiras","Gremio",
             "Atletico Paranaense", "São Paulo","Internacional",
             "Conrithians","Fortaleza","Goias","Bahia","Vasco",
             "Atletico Mineiro","Fluminense","Botafogo","Ceará",
             "Cruzeiro","CSA","Chapecoense","Avaí")
print(f'Lista de times: {times}')
print(f'Os primeiros 5 times são {times[0:5]}')
print(f'Os últimos quatro são {times[-4:]}')
print(f'Times em ordem alfabética {sorted(times)}')
print(f'O Santos está na {times.index("Chapecoense") + 1}ª posiçao.')