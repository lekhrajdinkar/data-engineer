import shelve

# More like Dictionary
# Shelve key must be only str
# operations are same
# uses pickling behind the scene.
# not that safe to use

#prg-1
with shelve.open('io/shelve') as fund:
    fund['AF'] = "TDF and CIT"
    fund['AFIS'] = "Insurance fund"
    fund['CAD'] = "canadian and European fund"

    print(fund['AF'])
print(fund)

# Prg : Need to closed at the end manually...
fund = shelve.open('io/shelve-2', writeback=True)

# fund['AF'] = "TDF, CIT, CIT-TEMP"
# fund['AFIS'] = "Insurance fund"
# fund['CAD'] = "canadian and European fund"
# fund['AUS'] = ["Australian fund", 'future CGC  business']
print(fund['AF'])
print(fund)
print(fund.get('AFFFF'), '==== get is error safe==== ') # None

fund['AUS'].append('Fund launch in 2024') # UPDATE >> shelve does not get this update by append
# reassigment would work, but not this. writeback=true (py uses memory, hence not good)

for k,v in fund.items():
    print(k, v, fund[k], sep=' -----')

# print in unOrdered way
# for k in fund.keys(): better readability, same
for k in fund:
    print(k, fund[k], sep='::::::')

# print in Ordered way
ordered_key_list = list(fund.keys())
ordered_key_list.sort()
for k in ordered_key_list:
    print(k, fund[k], sep='++++++')

fund.close()


