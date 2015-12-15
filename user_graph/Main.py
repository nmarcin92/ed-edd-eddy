from user_graph.Database import Database
from user_graph.UserGraphGenerator import UserGraphGenerator

if __name__ == "__main__":
    database = Database()
    user_graph_generator = UserGraphGenerator()
    limit = 10000
    user_graph_generator.generate_csv_file('file/replay_to.csv', database.get_users_in_reply_to_connection(limit))
    user_graph_generator.generate_csv_file('file/retweet.csv', database.get_users_retweet_connection(limit))
    user_graph_generator.generate_csv_file('file/retweet_and_replty_to.csv', database.get_users_retweet_or_reply_to_connection(limit))
    user_graph_generator.generate_csv_file('file/mention.csv', database.get_users_mention_connection(limit))
    user_graph_generator.generate_csv_file2('file/all.csv', database.get_users_mention_connection(limit), database.get_users_retweet_or_reply_to_connection(limit))