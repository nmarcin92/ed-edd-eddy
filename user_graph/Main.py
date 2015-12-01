from user_graph.Database import Database
from user_graph.UserGraphGenerator import UserGraphGenerator

if __name__ == "__main__":
    database = Database()
    user_graph_generator = UserGraphGenerator()
    user_graph_generator.generate_csv_file('replay_to.csv', database.get_users_in_reply_to_connection())
    user_graph_generator.generate_csv_file('retweet.csv', database.get_users_retweet_connection())
    user_graph_generator.generate_csv_file('all.csv', database.get_users_retweet_or_reply_to_connection())
