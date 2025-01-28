
def criar_sobrescrever_tbl(spark_df, table_name):

    # Salvar o DataFrame no Databricks com overwrite
    spark_df.write \
        .format("delta") \
        .mode("overwrite") \
        .saveAsTable(table_name)


