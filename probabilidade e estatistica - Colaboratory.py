#Iniciando a utilização da biblioteca pandas
import pandas as pd
import seaborn as sns
orig_url='https://drive.google.com/file/d/1pkOP40FvztNt0pnWgKMG5iTXzRt4TW_N/view?usp=sharing'
import requests
from io import StringIO
file_id = orig_url.split('/')[-2]
dwn_url='https://drive.google.com/uc?export=download&id=' + file_id
url = requests.get(dwn_url).text
csv_raw = StringIO(url)
dfs = pd.read_csv(csv_raw)

# Quantas reclamações foram registradas em 2016, contidas nesta base?
dfs['AnoCalendario'].value_counts().head(1)

# Qual região houve mais reclamação? E qual houve menos?
testeMaior = dfs['Regiao'].value_counts().head(1)
testeMenor = dfs['Regiao'].value_counts().tail(1)
print(testeMaior)
print(testeMenor)

# Qual a quantidade de reclamações realizadas por homens? E por mulheres?
dfs['SexoConsumidor'].value_counts().head(2)

# Em qual região os homens fizeram mais reclamações que as mulheres?
dfs_temp_ = dfs[['Regiao', 'SexoConsumidor']]
dfs_2 = dfs_temp_[dfs['SexoConsumidor']=='M'].value_counts()
dfs_2[1:2]

# Quais assuntos apresentaram mais reclamações em 2016?
dfs[['CodigoAssunto', 'DescricaoAssunto', 'AnoCalendario']].value_counts().head()

# Analisando o nome fantasia, determine qual empresa recebeu mais reclamações em 2016.
dfs[['strNomeFantasia', 'AnoCalendario']].value_counts().head(1)

# Qual empresa possui um maior percentual de resolução de reclamações?
dfs[['Atendida', 'strNomeFantasia']].value_counts().head(1)

# Monte um gráfico mostrando a quantidade de reclamações por região, separando as mesmas por sexo.
dfs_temp = dfs[['Regiao','SexoConsumidor']]
sns.countplot(x='Regiao', hue='SexoConsumidor',data=dfs_temp)

# Elabore um gráfico boxplot mostrando a quantidade de reclamações por região.
sns.boxplot(x=dfs['Regiao'],y=dfs['CEPConsumidor'], data=dfs)