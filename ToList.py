import csv 

def parseCsvToList():
    
    with open('./test3urls.csv') as f:
    #with open('./shorturlpro.csv') as f:    
        reader = csv.reader(f)
        data = list(reader)
    return data
    

def formaterList():
    data = parseCsvToList()
    data.pop(0)
    start_urls=[]
    for element in data:
        start_urls.append(element[0])

    return start_urls

print(formaterList())