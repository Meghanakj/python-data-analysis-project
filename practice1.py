
print("a")

print(f"value of f is {f}")
class Student:
      def __init__(self,name,department):
            self.name=name
            self.dept=department
      def add_grade(self,grade):
            self.grd.append(grade)
s1=Student("Meghana","ECE")
print(f"{s1.name} and {s1.dept}")
print("Today is my learning day")

l1=[1,2,3]



# import webbrowser
# url = "https://www.linkedin.com/feed/"
# webbrowser.open_new_tab(url)
# webbrowser.open_new(website)
import pandas as pd
import calendar
month=calendar.month(2024,11)
# print(month)
# print("12","10","2024",sep="/")
data={"name":["meghana","Nan","rathna"],
      "age":[112,2,43]
      }
name1={"name":"Meghana","age":23}
# print(f"{sys.getsizeof(name1)}")
name2={"lastname":"KJ"}
# names = name1 | name2
names = {**name1,**name2}
# print(names)
df=pd.DataFrame(data)
# print(df)
# print(df.isnull().sum())
# print(df2)
d_age=df.set_index("age")
# df["name"]=df["name"].fillna("kj")
# print(df)

# print(d_age)

df1=pd.read_csv("updateregion.csv")
# print(df1.tail())
from heapq import nlargest
from collections import Counter
import collections

l=[1,2,3,4]

import heapq
import itertools
l1=[[1,2],[2,3]] #[1,2,3,4
flattened = list(itertools.chain.from_iterable(l1))
l2=[k for i in l1 for k in i ]
# print(flattened)
# print(l2)
l2=[i*3 for i in l] #list compresion
# print(heapq.nlargest(1,l))
# print(heapq.nsmallest(2,l))
# print(l2)
#word count
str1="hello world"

# print(collections.Counter(str1))
from barcode import ISBN13
from barcode.writer import ImageWriter
from PIL import Image
# num = '978116786543'
# saving image as png
# bar_code = ISBN13(num, writer=ImageWriter())
# save image
# bar_code.save('bar_code')
# read the image using pillow
# img = Image.open("bar_code.png")
# img.show()
