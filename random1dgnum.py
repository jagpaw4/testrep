#mean, mode, and median of random single-digit numbers
import random
import statistics as st
n1 = random.randint(1, 10)
n2 = random.randint(1, 10)
n3 = random.randint(1, 10)
n4 = random.randint(1, 10)
n5 = random.randint(1, 10)
n6 = random.randint(1, 10)
set1 = {n1, n2, n3, n4, n5, n6}
print("set created is ", set1)
m1 = st.mean(set1)
m2 = st.mode(set2)
m3 = st.median(set3)
print("The mean, mode, median is", m1, m2, m3, "respectively")
