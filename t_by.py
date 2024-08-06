from ucimlrepo import fetch_ucirepo 
  
# fetch dataset 
zoo = fetch_ucirepo(id=111) 
  
# data (as pandas dataframes) 
X = zoo.data.features 
y = zoo.data.targets 
  
# metadata 
print(zoo.metadata) 
  
# variable information 
print(zoo.variables) 