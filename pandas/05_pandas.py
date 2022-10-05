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

df_produto = spark.table("silver_olist.products").toPandas()
df_order_items = spark.table("silver_olist.order_items").toPandas()

df_order_items.head()

# COMMAND ----------

# FUNCIONA, MAS NÃO É BONITO
df_join_1 = df_order_items.merge(df_produto, how='left', on='idProduct')
df_join_2 = df_join_1.merge(df_sellers, how='left', on='idSeller')

df_result = df_join_2.rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                        "descCity":"descCitySeller",
                                        "descState": "descStateSeller" })

df_result

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                          .merge(df_sellers, how='left', on='idSeller')
                          .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                             "descCity":"descCitySeller",
                                             "descState": "descStateSeller" }))
df_result.head()

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                          .merge(df_sellers, how='left', on='idSeller')
                          .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                             "descCity":"descCitySeller",
                                             "descState": "descStateSeller" }))
df_result.groupby(by=["descCategoryName"])[['idOrder']]
         .count()
         .reset_index()
         .rename(columns={'idOrder': 'qtIdOrder'})

# COMMAND ----------

df_result = (df_order_items.merge(df_produto, how='left', on='idProduct')
                           .merge(df_sellers, how='left', on='idSeller')
                           .rename(columns = {"nrZipPrefix": "nrZipPrefixSeller",
                                              "descCity":"descCitySeller",
                                              "descState": "descStateSeller" }))

df_new = (df_result.groupby(by=["descCategoryName"])[['idOrder', 'idSeller']]  # Agrupa por descCategoryName, fazendo calculo em ['idOrder']
                  .agg( {"idOrder": ['count'],
                         "idSeller": 'nunique'})                               # Realiza a contagem de ['idOrder']
                  .reset_index())                    # Renomeia o idOrder para qtIdOrder
df_new
