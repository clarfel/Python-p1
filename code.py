d = {'k1':[{'nest_key':['this is deep',['hello']]}]}
# d['k1'][0]{'nest_key': ['this is deep', ['hello']]} 
# d['k1'][0]['nest_key'][1] ['hello']
print(d['k1'][0]['nest_key'][1][0])