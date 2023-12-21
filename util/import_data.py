import json
from random import choice
import pandas as pd

class jsonParse:
      def __init__(self):
        self.text = [] 
        self.intents = [] 
        self.responses = {} 

      def parse(self, json_path):
            with open(json_path) as data_file:
                  self.data = json.load(data_file)

            for kategori in self.data['intents']:
                for pattern in kategori['patterns']:
                    self.text.append(pattern)
                    self.intents.append(kategori['tag'])
            
                for respon in kategori['responses']:
                  if kategori['tag'] in self.responses.keys():
                        self.responses[kategori['tag']].append(respon)
                  else:
                        self.responses[kategori['tag']] = [respon]

            self.df = pd.DataFrame({'kategori': self.intents,'input_user': self.text})
            
      def get_dataframe(self):
            return self.df

      def get_response(self, kategori):
            return choice(self.responses[kategori])
      