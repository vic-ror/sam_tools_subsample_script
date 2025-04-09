#Importar módulos
import argparse #Colocar flags em linha de comando
import os #Executar comandos linux dentro do python

#Criando parser para armazenar argmentos
parser = argparse.ArgumentParser()

parser.add_argument("-i", "--input_file", help = "Arquivo de entrada .sam", required = True)
parser.add_argument("-o", "--output_file", help = "Nome arquivo de saída", required = True)
parser.add_argument("-ic", "--input_cov", help = "Cobertura do arquivo de entrada", required = True)
parser.add_argument("-wc", "--wanted_cov", help = "Cobertura desejada", required = True)

#Atribuindo argumentos dentro de objeto
args = parser.parse_args()

#Salvando argumentos em variáveis
arquivo_entrada = args.input_file
arquivo_saida = args.output_file
cov_input = args.input_cov
cov_desejada = args.wanted_cov

#Calculando Razão cobertura desejada/cobertura atual do arquivo
###São escolhidas no arquivo reads aleatórias até que quantidade das reads corresponda a necessária para a corbetura ser igual a desejada
razao = float(cov_desejada)/float(cov_input)

os.system(f"/media/data/anderson/tools/samtools/bin/samtools view -h -s {razao} -o {arquivo_saida} {arquivo_entrada}") #-h matém o header e -s faz o subset

