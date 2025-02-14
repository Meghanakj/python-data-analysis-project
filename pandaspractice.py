
data = {
    'Department': ['Saes', 'IT', 'HR', 'Sales', 'IT', 'HR', 'Sales'],
    'Employee': ['Alice', 'Bob', 'Charlie', 'David', 'Eve', 'Frank', 'Grace'],
    'Salary': [50000, 60000, 45000, 52000, 61000, 47000, 58000],
}
df=pd.DataFrame(data)
# print(df)
df_loc=df.set_index("Salary")
# print(df_loc.loc[50000])
df_average=df.groupby("Department")#["Salary"].mean()
print(df_average)
data1 = {
    'Product': ['Laptop', 'Phone', 'Tablet', 'Monitor', 'Keyboard'],
    'Price': [1200, 700, 300, 250, 100],
    'Stock': [50, 100, 150, 80, 200],
}
df1 = pd.DataFrame(data1)
df_desc=df1.sort_values("Price",ascending=False)
# print(df_desc)
df_index=df_desc.set_index("Product")
# print(df_index)
data2 = [(1, "apple"), (2, "banana"), (3, "cherry"), (1, "apple")]
df_data2 = set(data2)
# print(df_data2)
data_dict=dict(data2)
# print(data_dict)
data3 = {
    'Name': ['John', 'Alice', 'Bob', 'David', None],
    'Age': [25, None, 30, 35, 40],
    'Salary': [50000, 60000, None, 80000, 70000],
}
df3 = pd.DataFrame(data3)
print(df3)
df_avr=df3["Age"].mean()
print(df_avr)
df3["Age"]=df3["Age"].fillna(df_avr)
print(df3)
df_drop=df3.dropna(subset=["Salary"])
print(df_drop)















df = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Alice', 'Charlie', 'Bob'],
    'Age': [25, 30, 25, 35, 30],
    'Score': [85, 90, 85, 95, 90]
})
df_unique = df.drop_duplicates(subset='Name', keep='first')

# print(df_unique)
# df_asc=dfd.sort_values(by=["Age","Score"], ascending=[True,False])
# print(df_asc)
df = pd.DataFrame({
    'ID': [101, 102, 103],
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35]
})
df=df.set_index("ID")
df_102=df.loc[102]
# print(df_102)
l=[1,2,3]
l1=[i*2 for i in l]
# print(l1)
data1= {"name":["meghana","","","Trivikram","Narayana","hari"],
        "Age": [22,46,1,2,3,5]}
data2={"name":["kj","prya","asc","q","a","z"],
        "Age": [1,46,1,2,3,5]}
df_dataframe=pd.DataFrame(data1)
# str=["Helloworld" ,"jkj"]
# print(collections.Counter(str).most_common())
# start1=[i for i in str if i.startswith("H")]
# print(start1)

# # print(df)
# print(df.tail(2))
# print(df.dtypes)
# print(df.isnull().sum())
df = pd.read_csv("updateregion.csv")
# print(df)
df1=df[["CurrentRegion","NewRegion"]]
# print(df1)
df_rename=df.rename(columns={"CurrentRegion": "updatedregion"})
# print(df_rename)
#replace value
df_rename["updatedregion"]=df_rename["updatedregion"].replace("Northwest","North")
# print(df_rename)
df_groupby=df_rename.groupby("NewRegion").size()
# print(df_groupby)
df_sort=df_rename.sort_values("updatedregion",ascending=True).groupby("updatedregion").size()
# print(df_sort)
# df["CurrentRegion"].fillna(0,inplace=True)
# df.dropna(inplace=True)
# print(df)
x = [1, 2, 3, 4]
y = x
y.append(5)
# print(x)
stringdata="Hello this me meghana"
# countm=[i for i in stringdata  if i.startswith("o")]
sounti=Counter(stringdata).get("l")
print(sounti)
iter=[[1,2],[3,4]]
import itertools
iter1=list(itertools.chain.from_iterable(iter))
print(iter1)
liiter1=[j for i in iter for j in i]
print(liiter1)
days=["sunday","monday","tuesday","wednesday","thursday"]
daysq=list(enumerate(days,start=1))
print(daysq)
str1="string"
for i,j in enumerate(str1):
    if j=="r":
        print(f"{i}")
lowd=[i.upper() for i in str1]
print(lowd)