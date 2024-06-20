st = "Yes ! We are learning double  space "

doublespaces = st.find("  ")
print(doublespaces)


# Now, Replace in single space
st = "Yes ! We are learning double   space "

st = st.replace("  ", "")
print(st)