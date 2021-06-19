#!/usr/bin/env python
# coding: utf-8

# In[1]:


from mrjob.job import MRJob
class Bacon_count(MRJob):
    def mapper(self, _, line):
        for word in line.split():
            if word.lower() == "bacon":
                yield "bacon", 1

    def reducer(self, key, values):
        yield key, sum(values)
if __name__ == "__main__":
    Bacon_count.run()        
                


# In[ ]:




