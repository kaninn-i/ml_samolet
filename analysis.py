import pandas

df_1 = pandas.read_csv("cian_parsing_result_sale_1_10_moskva_23_Oct_2024_10_34_07_730447.csv", encoding = "ISO-8859-1", on_bad_lines='skip')
df_2 = pandas.read_csv("cian_flat_sale_1_5_mozhajsk_23_Oct_2024_10_20_04_638946.csv", encoding = "ISO-8859-1", on_bad_lines='skip')
# df_3 = pandas.read_csv("data3.csv")

print('-------------------------------------------')
for i in df_1.columns:
  print(i)
print('-------------------------------------------')
for i in df_2.columns:
  print(i)
  print('-------------------------------------------')