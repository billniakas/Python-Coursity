
# Λεξικο με συχνότητες εμφάνισης φθόγγων
# Πηγή: http://www.foundalis.com/dep/ling/L2_gr.htm

di = {'t':11.35,'e':9.20,'o':10.87,'i':13.62,'a':10.79}

# Ταξινόμηση με βάση τα Κλειδιά
##print(sorted(di))
##print(sorted(di)[::-1])
##print(max(di), min(di))
##for x in sorted(di):
##    print(x, di[x])


# Ταξινόμηση με βάση τις Τιμές
print(sorted(di.values()))
print(sorted(di.values())[::-1])

for x in sorted(di.values()):
    print(x, list(di.keys())[list(di.values()).index(x)])


