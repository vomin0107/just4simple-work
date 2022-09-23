import pandas as pd


base_url = r'C:\Users\minuk\Documents\All_document\지출결의서/'
df = pd.read_excel(r'C:\Users\minuk\Documents\All_document\연구소자재목록\연구소_자재_목록.xlsx')
target_df = pd.read_excel(base_url + '지출결의서_20210402-3_이상훈(알리구매3).xlsx')

flag = 0
index = 0
for i in range(df.shape[0]):
    if str(df.loc[i][1]) != 'nan':
        # print(str(i), df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5], df.loc[i][6])
        flag += 1
    elif flag > 20:
        index = i
        break
    else:
        flag = 0

date = str(target_df.loc[0][3])
name = str(target_df.loc[1][11])
tax = 0
print(date, name)
for i in range(target_df.shape[0]):
    if str(target_df.loc[i][0]) == '부가세':
        tax = 1
for i in range(7, target_df.shape[0]):
    if str(target_df.loc[i][0]) != 'nan':
        print(index)
        df.loc[index,1] = target_df.loc[i][0]
        print(df.loc[index][1])
        print(target_df.loc[i][0])
        df.loc[index,2] = date
        df.loc[index,3] = name
        df.loc[index,5] = target_df.loc[i][8]
        if tax:
            df.loc[index,4] = str(float(str(target_df.loc[i][12]).replace(',', '')) * 1.1)
            df.loc[index,6] = str(float(str(target_df.loc[i][15]).replace(',', '')) * 1.1)
        else:
            df.loc[index,4] = str(target_df.loc[i][12])
            df.loc[index,6] = str(target_df.loc[i][15])
        print(str(i), target_df.loc[i][0], target_df.loc[i][8], target_df.loc[i][12], target_df.loc[i][15])
        index += 1

for i in range(df.shape[0]):
    if str(df.loc[i][1]) != '0':
        print(str(i), df.loc[i][1], df.loc[i][2], df.loc[i][3], df.loc[i][4], df.loc[i][5], df.loc[i][6])
        flag += 1

df.to_excel('result.xlsx')