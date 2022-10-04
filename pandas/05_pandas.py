# Databricks notebook source
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# COMMAND ----------

spark_dataframe = spark.table("silver_olist.order_items")
# spark_dataframe.display()

df = spark_dataframe.toPandas()

# COMMAND ----------

type(df)

# COMMAND ----------

df[df['vlPrice'] > 100]

# OUTRA FORMA DE FAZER A MESMA BUSCA
# condicao = df['vlPrice'] > 100
# df[condicao]

# COMMAND ----------

df['log_price'] = np.log(df['vlPrice'])
df['log_freight'] = np.log(df['vlFreight'] + 1)
#METODO 1
# df.rename(columns={"log_price":"vlPriceLog"})
#METODO 2
df.rename(columns={"log_price":"vlPriceLog"}, inplace=True)
df.rename(columns={"log_freight":"vlFreightLog"}, inplace=True)

# COMMAND ----------

plt.hist(df['vlPrice'])
plt.grid(True)
plt.title("Primeira tabelinha")
plt.xlabel("Produto")
plt.ylabel("Frequencia")
plt.show()

# COMMAND ----------

plt.hist(df['vlPriceLog'])
plt.grid(True)
plt.title("Primeira tabelinha")
plt.xlabel("Produto")
plt.ylabel("Frequencia")
plt.legend(["Valores em log"])
plt.show()

# COMMAND ----------

plt.hist(df['vlPriceLog'], density = True, alpha=0.5)
plt.hist(df['vlFreightLog'], density = True, alpha=0.5)
plt.grid(True)
plt.title("Primeira tabelinha")
plt.xlabel("Produto")
plt.ylabel("Frequencia")
plt.legend(["Valores em log", "Frete em log"])
plt.show()

# COMMAND ----------


