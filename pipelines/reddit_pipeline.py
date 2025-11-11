from utils.constants import CLIENT_ID, SECRET, USER_AGENT, OUTPUT_PATH
from etls.reddit_etl import connect_reddit, extract_posts, transform_data, load_data_to_csv
import pandas as pd


def reddit_pipeline(file_name: str, subreddit: str, time_filter='day', limit=None):
    # Connecting to a Reddit Instance
    instance = connect_reddit(CLIENT_ID, SECRET, USER_AGENT)

    #  Extraction
    posts = extract_posts(instance, subreddit, time_filter, limit)
    post_df = pd.DataFrame(posts)

    # Transformation
    transformed_data = transform_data(post_df)

    # Loading into CSV
    file_path = f'{OUTPUT_PATH}/{file_name}.csv'
    load_data_to_csv(transformed_data, file_path)

    return file_path


