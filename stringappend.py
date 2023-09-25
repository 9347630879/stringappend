#operator overloading
roman = "sai"
second = "sundhar"
print(roman + " " + second)

#f'string interpolation
roman = "sai"
second = "sundhar"
fullname = f"{ roman } { second }"
print(fullname)

#string join method

roman = "sai"
second = "sundhar"
lst = (roman,second)
print (" ".join(lst))

#split
DOB = ("06 may 1999")
print(DOB.split(" "))

#split lines
address  ="""


shareen nagar,

kurnool,

andhra pradesh,

"""
print(address.splitlines())

#partition
name = "dhanunjaisaisundhar"
print(name.partition("sai"))

#r-partition

name = "dhanunjaisaisundhar"
print(name.rpartition("sai"))
