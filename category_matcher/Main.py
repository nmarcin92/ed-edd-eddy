from category_matcher.Database import Database


def match_tweets():
    database = Database()
    tweets_ids = database.find_tweets_ids()
    counter = 0
    for t_id in tweets_ids:
        try:
            categories = database.find_categories_for_tweet(t_id)
            leading_category = max(set(categories), key=categories.count)
            database.assign_category(t_id, leading_category)
        except Exception as e:
            #YOLO
            pass
        counter += 1
        if counter % 10000 == 0:
            print str((float(counter) / 2961960.0)) + '%'


if __name__ == "__main__":
    match_tweets()
