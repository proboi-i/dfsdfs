import re
import json
a = """Air pollution is the introduction of chemicals, particulate matter, or biological materials into the atmosphere, causing harm or discomfort to humans or other living organisms, or damaging ecosystems. Air pollution can cause health problems including, but not limited to, infections, behavioral changes, cancer, organ failure, and premature death. These health effects are not equally distributed across the U.S population; there are demographic disparities by race, ethnicity, socioeconomic status, and education. Air pollution has affected the United States since the beginning of the Industrial Revolution.
According and air is bad According to a 2009 report, around "60 percent of Americans live in areas where air pollution has reached unhealthy levels that can make people sick." Analyzing data from 2016–2018, the American Lung Association found major declines in air quality, including increases in ground-level ozone.In 2016, a study found that levels of nitrogen oxides had plummeted over the previous decade, due to better regulations, economic shifts, and technological innovations. NASA reported a 32% decrease of nitrogen dioxide in New York City and a 42% decrease in Atlanta between the periods of 2005–2007 and 2009–2011."""
a.replace('"','`')

def tokenl(i):
    return re.findall(r"[\w']+", i)

tokens = tokenl(a)
b = {
    "params": [],
    "data": {},
    "enc" : []
}
for i in range(len(tokens)):
    if i not in b["params"]:
        b["data"][tokens[i]] = i
        b["params"].append(tokens[i])
    b["enc"].append(b['data'][tokens[i]])
print(json.dumps(b, indent=4, sort_keys=True))
print(len(b["params"]), " Total parameters")
question = input("Enter text: ")
def encoder(input):
    try:
        if len(input.split()) ==1 :
            return b["data"][input]
        else:
            vals = []
            for i in input.split():
                if i in b["params"]:
                    vals.append(b["data"][i])
                else:
                    pass
            return vals
    except:
        return 1
def decoder(input):
    if len(input) ==1 :
        return b["params"][input]
    else:
        vals = []
        for i in input:
            vals.append(b["params"][i])
        return vals
value = encoder(question)
print(value)
print(decoder(value))
def burp(input):
    if len(input) ==1 :
        return [input]
    else:
        #creating all possible combinations of the input along with permutations
        return [input[i:j] for i in range(len(input)) for j in range(i+1,len(input)+1)]


#creating a list of all possible combinations of the input
combos = list(burp(value))

def capture(input):
    #we are going to take the input of all possible combinations and generate a list of all text possible 
    #from the input
    input = sorted(input,key=len)
    common_values = set()
    for i,value in enumerate(input):
        for j in range(i+1, len(input)):
            common_values.update(set(input[i]).intersection(input[j]))
    common_values = list(common_values)
    return common_values
valuee = capture(combos)
def greedy_nature(input):
    # This function will take input ids and find the longest possible text from the input with ids starting from the first id
    # and ending at the last id
    corpus = b["enc"]
    common_values = set()
    #find all the positions of the ids in the corpus
    for i in input:
        for j in range(len(corpus)):
            if i == corpus[j]:
                common_values.add((i,j))
    common_values = list(common_values)
    #sort the list of tuples by the second element of the 
        
    return common_values
    
grids = greedy_nature(valuee) #([],[]) => format 
def vaslue(input):

    #Now we have the index of the first id and the last id along with the position of the ids in the corpus
    #we are going to find the longest possible text from the corpus
    max = 0
    min =0
    for i in input:
        if i[1] > max:
            max = i[1]
        if i[1] < min:
            min = i[1]
    reval = decoder(b["enc"][max:len(b["enc"])])
    return reval
print(vaslue(grids))

