import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_Nobel_laureates'

df = pd.DataFrame(pd.read_html(url)[0])
# print(df)
df_melted=df.melt(id_vars="Year", var_name="Nobel")
df_split=df_melted.assign(value=df_melted.value.str.split(";")).explode('value')
df.to_csv('Laureats.csv', index=False)
print(df_split)










# print(df_split)

# col

# print(df_melted.value.str.split(";",expand=True).head())
# df.to_csv('Laureats.csv', index=False)
# page = requests.get('https://en.wikipedia.org/wiki/List_of_Nobel_laureates')



# # Create a BeautifulSoup object
# soup = BeautifulSoup(page.text, 'html.parser')

# # get the repo list
# table = soup.find('table',{"class":"wikitable"})
# # print(table)

# c0=[]
# c1=[]
# c2=[]
# c3=[]
# c4=[]
# c5=[]

# for row in table.findAll('tr'):
#     cells = row.findAll('td')
#     print(len(cells))
#     # if len(cells)==6:
#     #     c1.append(cells[0].find(text=true))
#     #     c1.append(cells[1].find(text=true))
#     #     c2.append(cells[2].find(text=true))
#     #     c3.append(cells[3].find(text=true))
#     #     c4.append(cells[4].find(text=true))
#     #     c5.append(cells[5].find(text=true))



# rows = table.findAll('tr')
# print(c1)

# header = [th.text.rstrip() for th in rows[0].find_all('th')]
# # print(header)

# df = dict([(x,0) for x in header])
 

# # print(df)
