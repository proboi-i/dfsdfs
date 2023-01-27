import nltk
from nltk.tokenize import word_tokenize

text = """Competences and powers at voivodeship level are shared between the voivode (governor), the sejmik (regional assembly) and the marshal. In most cases these institutions are all based in one city, but in Kuyavian-Pomeranian and Lubusz Voivodeship the voivode's offices are in a different city from those of the executive and the sejmik. Voivodeship capitals are listed in the table below.
The voivode is appointed by the Prime Minister and is the regional representative of the central government. The voivode acts as the head of central government institutions at regional level (such as the police and fire services, passport offices, and various inspectorates), manages central government property in the region, oversees the functioning of local government, coordinates actions in the field of public safety and environment protection, and exercises special powers in emergencies. The voivode's offices collectively are known as the urząd wojewódzki.The sejmik is elected every five years. (The first of the five-year terms began in 2018; previous terms lasted four years.)) Elections for the sejmik fall at the same time as that of local authorities at powiat and gmina level. The sejmik passes by-laws, including the voivodeship's development strategies and budget. It also elects the marszałek and other members of the executive, and holds them to account.
The executive (zarząd województwa), headed by the marszałek drafts the budget and development strategies, implements the resolutions of the sejmik, manages the voivodeship's property, and deals with many aspects of regional policy, including management of European Union funding. The marshal's offices are collectively known as the urząd marszałkowski."""
text.replace('"','`')
tokens = word_tokenize(text)
json = {}
json["params"] = []
json["data"] = {}
for i in range(len(tokens)):
    json["data"][tokens[i]] = i
    json["params"].append(tokens[i])
print(json)
print(len(json["params"]), " Total parameters")

user_input = input("Enter text: ")
def encoder(input):
    if len(input.split()) ==1 :
        return json["data"][input]
    else:
        for i in input.split():
            if i in json["params"]:
                return json["data"][i]
        return "Not found"

print(encoder(user_input))