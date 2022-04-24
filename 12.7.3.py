money = int(input("Введите сумму вклада :"))
per_sent = {"TKB":5.6 , "SKB":5.9 , "VTB":4.28 , "SBER":4.0}
TKB = int((per_sent["TKB"])*(money/100))
SKB = int((per_sent["SKB"])*(money/100))
VTB = int((per_sent["VTB"])*(money/100))
SBER = int((per_sent["SBER"])*(money/100))
deposit = {"TKB":TKB,"SKB":SKB,"VTB":VTB,"SBER":SBER}
print(deposit)
max_val = max(deposit.values())
print("Максимальная сумма, которую вы можете заработать:", max_val)