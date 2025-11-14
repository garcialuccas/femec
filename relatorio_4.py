from math import sqrt, pi
from statistics import stdev, mean

distancias_iniciais = [18.6, 15.1, 17.8]
distancias_finais = [15.7, 12.1, 14.4]

media_distancias_iniciais = mean(distancias_iniciais)
medias_distancias_finais = mean(distancias_finais)

desvio_padrao_inicial = stdev(distancias_iniciais)
desvio_padrao_final = stdev(distancias_finais)

incerteza_estatistica_inicial = desvio_padrao_inicial / sqrt(len(distancias_iniciais))
incerteza_estatistica_final = desvio_padrao_final / sqrt(len(distancias_finais))

incerteza_distancia_inicial = sqrt((incerteza_estatistica_inicial ** 2) + (0.05 ** 2))
incerteza_distancia_final = sqrt((incerteza_estatistica_final ** 2) + (0.05 ** 2))

print(" ===== Tabela 1 =====")
print(f"media inicial: {round(media_distancias_iniciais, 4)}")
print(f"desvio padrao inicial: {round(desvio_padrao_inicial, 4)}")
print(f"incerteza estatistica inicial: {round(incerteza_estatistica_inicial, 4)}")
print(f"incerteza inicial total: {round(incerteza_distancia_inicial, 4)}")
print()
print(f"media final: {round(medias_distancias_finais, 4)}")
print(f"desvio padrao final: {round(desvio_padrao_final, 4)}")
print(f"incerteza estatistica final: {round(incerteza_estatistica_final, 4)}")
print(f"incerteza final total: {round(incerteza_distancia_final, 4)}")
print()

tempos_iniciais = [0.592, 0.795, 0.651]
tempos_finais = [0.775, 0.976, 0.793]
incerteza_instrumental_tempo = 0.001

velocidades_iniciais = []
velocidades_finais = []
incertezas_velocidades_iniciais = []
incertezas_velocidades_finais = []

print("===== Tabela 2 =====")

for linha in range(len(tempos_iniciais)):
    
    delta_t_inicial = tempos_iniciais[linha]
    
    velocidade_inicial = media_distancias_iniciais / delta_t_inicial
    incerteza_velocidade_inicial = sqrt((((1 / delta_t_inicial) ** 2) * ((incerteza_distancia_inicial) ** 2)) + (((media_distancias_iniciais / (delta_t_inicial ** 2)) ** 2) * (incerteza_instrumental_tempo ** 2)))

    velocidades_iniciais.append(velocidade_inicial)
    incertezas_velocidades_iniciais.append(incerteza_velocidade_inicial)
    
    delta_t_final = tempos_finais[linha]
    
    velocidade_final = medias_distancias_finais / delta_t_final
    incerteza_velocidade_final = sqrt((((1 / delta_t_final) ** 2) * ((incerteza_distancia_final) ** 2)) + (((medias_distancias_finais / (delta_t_final ** 2)) ** 2) * (incerteza_instrumental_tempo ** 2)))
    
    velocidades_finais.append(velocidade_final)
    incertezas_velocidades_finais.append(incerteza_velocidade_final)
    
    print(f" === colisao {linha + 1} ===")
    print(f"delta t inicial: {round(delta_t_inicial, 4)}")
    print(f"velocidade inicial: {round(velocidade_inicial, 4)}")
    print(f"incerteza velocidade inicial: {round(incerteza_velocidade_inicial, 4)}")
    print()
    print(f"delta t final: {round(delta_t_final, 4)}")
    print(f"velocidade final: {round(velocidade_final, 4)}")
    print(f"incerteza velocidade final: {round(incerteza_velocidade_final, 4)}")
    print()

print(" ===== Tabela 3 =====")

parafuso_raio = 6 # parametro de impacto
incerteza_parametro_impacto = 0.05 # incerteza da regua
massa_carrinho = 112.72 / 1000 # em quilogramas
incerteza_carrinho = 0.1 / 1000 # em quilogramas

momentos_lineares_iniciais = []
momentos_angulares_iniciais = []
incertezas_momentos_angulares_iniciais = []

momentos_lineares_finais = []
momentos_angulares_finais = []
incertezas_momentos_angulares_finais = []

for linha in range(len(velocidades_iniciais)):
    
    momento_linear_inicial = massa_carrinho * velocidades_iniciais[linha]
    momento_angular_inicial = parafuso_raio * momento_linear_inicial
    
    incerteza_momento_angular_inicial = sqrt((((parafuso_raio * velocidades_iniciais[linha]) ** 2) * ((incerteza_carrinho) ** 2)) + (((momento_linear_inicial) ** 2) * ((incerteza_parametro_impacto) ** 2)) + (((massa_carrinho * parafuso_raio) ** 2) * ((incertezas_velocidades_iniciais[linha]) ** 2)))
    
    momentos_lineares_iniciais.append(momento_linear_inicial)
    momentos_angulares_iniciais.append(momento_angular_inicial)
    incertezas_momentos_angulares_iniciais.append(incerteza_momento_angular_inicial)
    
    momento_linear_final = massa_carrinho * velocidades_finais[linha]
    momento_angular_final = parafuso_raio * momento_linear_final
    
    incerteza_momento_angular_final = sqrt((((parafuso_raio * velocidades_finais[linha]) ** 2) * ((incerteza_carrinho) ** 2)) + (((momento_linear_final) ** 2) * ((incerteza_parametro_impacto) ** 2)) + (((parafuso_raio * massa_carrinho) ** 2) * ((incertezas_velocidades_finais[linha]) ** 2)))
    
    momentos_lineares_finais.append(momento_linear_final)
    momentos_angulares_finais.append(momento_angular_final)
    incertezas_momentos_angulares_finais.append(incerteza_momento_angular_final)
    
    print(f" === colisao {linha + 1} ===")
    print(f"momento linear inicial: {round(momento_linear_inicial,  4)}")
    print(f"momento angular inicial: {round(momento_angular_inicial, 4)}")
    print(f"incerteza momento angular inicial: {round(incerteza_momento_angular_inicial, 4)}")
    print()
    print(f"momento linear final: {round(momento_linear_final, 4)}")
    print(f"momento angular final: {round(momento_angular_final, 4)}")
    print(f"incerteza momento angular final: {round(incerteza_momento_angular_final, 4)}")
    print()
    
periodos= [2.43 - 1.12, 2.89 - 1.39, 3.87 - 1.84] # tempo em segundos de uma volta do disco, medido a partir do video
incerteza_periodo = 1 / 120 # metade da menor medida do frame rate do video
velocidades_angulares = []
incertezas_velocidades_angulares = []

print(" ===== Tabela 4 =====")

for linha in range(len(periodos)):
    
    velocidade_angular = (2 * pi) / periodos[linha]
    incerteza_velocidade_angular = (2 * pi / (periodos[linha] ** 2)) * incerteza_periodo # derivada da velocidade angular em relacao ao periodo ao quadrado, vezes a incerteza ao quadrado e tudo pela raiz
    
    velocidades_angulares.append(velocidade_angular)
    incertezas_velocidades_angulares.append(incerteza_velocidade_angular)
    
    print(f" === colisao {linha + 1}")
    print(f"periodo: {periodos[linha]}")
    print(f"incerteza periodo: {round(incerteza_periodo, 4)}")
    print(f"velocidade angular: {round(velocidade_angular, 4)}")
    print(f"incerteza velocidade angular: {round(incerteza_velocidade_angular, 4)}")
    print()

massas_disco = []
incertezas_massas_disco = []
diametro_disco = 11
incerteza_diametro = 0.05

print(" ===== Tabela 5 =====")

for linha in range(len(velocidades_angulares)):

    massa_disco = (massa_carrinho * parafuso_raio * (velocidades_iniciais[linha] - velocidades_finais[linha]) * periodos[linha]) / (pi * ((diametro_disco / 2) ** 2))

    incerteza_total_velocidade = sqrt((incertezas_velocidades_iniciais[linha] ** 2) + (incertezas_velocidades_finais[linha] ** 2))

    derivada_velocidade = (massa_carrinho * parafuso_raio * periodos[linha]) / (pi * ((diametro_disco / 2) ** 2))

    derivada_massa_carrinho = (parafuso_raio * (velocidades_iniciais[linha] - velocidades_finais[linha]) * periodos[linha]) / (pi * ((diametro_disco / 2) ** 2))

    derivada_parametro_impacto = (massa_carrinho * (velocidades_iniciais[linha] - velocidades_finais[linha]) * periodos[linha]) / (pi * ((diametro_disco / 2) ** 2))

    derivada_periodo = (massa_carrinho * parafuso_raio * (velocidades_iniciais[linha] - velocidades_finais[linha])) / (pi * ((diametro_disco / 2) ** 2))

    derivada_diametro = (-8 * (massa_carrinho * parafuso_raio * (velocidades_iniciais[linha] - velocidades_finais[linha]) * periodos[linha])) / (pi * (diametro_disco ** 3))

    incerteza_massa_disco = sqrt(((derivada_velocidade ** 2) * (incerteza_total_velocidade ** 2)) + ((derivada_diametro ** 2) * (incerteza_diametro ** 2)) + ((derivada_massa_carrinho ** 2) * (incerteza_carrinho ** 2)) + ((derivada_periodo ** 2) * (incerteza_periodo ** 2)) + ((derivada_periodo ** 2) * (incerteza_parametro_impacto ** 2)))

    massas_disco.append(massa_disco)
    incertezas_massas_disco.append(incerteza_massa_disco)

    print(f" === colisao {linha + 1} ===")
    print(f"massa do disco: {round(massa_disco, 4)}")
    print(f"incerteza massa disco: {round(incerteza_massa_disco, 4)}")
    print()
