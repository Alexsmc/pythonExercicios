times = ('Botafogo', 'Palmeiras', 'Fluminense','Athletico-PR', 'Cruzeiro','Fortaleza','São Paulo','Atlético-MG','Santos','Grêmio','Internacional','Flamengo','Bahia','Vasco','Bragantino','Corinthians','Cuiabá','Goiás','Coritiba', 'América-MG')

print('Os primeiros dolocados são: ', times[0:5])
print('Os ultimos 4 colocados são:', times[16:21])
print(sorted(times))
print('Cruzeiro está na posição: ',times.index('Cruzeiro')+1)