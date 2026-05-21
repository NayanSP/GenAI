import json
import pandas as pd

class Few_Shot_Posts:
    def __init__(self, file_path = "LinkedINPostGenerator\\data\\processed_posts.json"):
        self.df = None # dataframe
        self.unique_tags = None
        self.load_posts(file_path)
        
    def load_posts(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            posts = json.load(f)
            df = pd.json_normalize(posts)
            print(df.columns)
            df['Length'] = df['line_count'].apply(self.categorize_length)
            all_tags = df['tags'].apply(lambda x: x).sum()
            print(df.columns)
            print(all_tags)
            self.unique_tags = set(list(all_tags))
            print(self.unique_tags)
            self.df = df
            print(df)
    
    def categorize_length(self, line_count):
        if line_count < 5:
            return "Short"
        elif 5<= line_count <= 10:
            return "Medium"
        else:
            return "Long"
    
    def get_tags(self):
        return self.unique_tags
    
    def get_filtered_posts(self, length, tag):
        df_filtered = self.df[
            (self.df['Length'] == length) &
            (self.df['tags'].apply(lambda tags: tag in tags)) 
        ]

        return df_filtered.to_dict(orient='records')

if __name__ == '__main__':
    fs = Few_Shot_Posts()
    posts = fs.get_filtered_posts('Medium','Job Search')
    print(posts)