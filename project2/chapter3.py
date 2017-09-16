# sc = ...

filepath = "/Users/steve/ml-100k/u.user"

user_data = sc.textFile(filepath)

# In [3]: user_data.take(3)
# Out[3]: [u'1|24|M|technician|85711', u'2|53|F|other|94043', u'3|23|M|writer|32067']
# userid, age, gender, occupation, zipcode

user_fields = user_data.map(lambda line: line.split("|"))

num_users = user_fields.map(lambda t: t[0]).distinct().count()
# 943 users

num_genders = user_fields.map(lambda t: t[2]).distinct().count()
num_genders_details = user_fields.map(lambda t: (t[2], 1)).reduceByKey(lambda x,y: x+y).collect()

# M:: 670
# F:: 273


num_occupations = user_fields.map(lambda t: t[3]).distinct().count()
# 21

print("MovieLens - 10K descriptive stat result:\nUsers: {}, genders: {}, occupations: {}, ...".format(num_users, num_genders, num_occupations))

ages = user_fields.map(lambda t: int(t[1])).collect()

hist(ages, bins=20, color='lightblue', normed=True)

count_by_occupation = user_fields.map(lambda fields: fields[3]).countByValue()

# doctor: 7
# marketing: 26
# ......

filepath2 = "/Users/steve/ml-100k/u.item"
movie_data = sc.textFile(filepath2)
num_movies = movie_data.count()
# 1682


def convert_year(x):
    try:
        return int(x[-4:])
    except:
        # filling dirty years
        return 1900

movie_fields = movie_data.map(lambda line: line.split("|"))
years = movie_fields.map(lambda fields: fields[2]).map(lambda x: convert_year(x))


years_filtered = years.filter(lambda x: x!= 1900)

movie_ages = years_filtered.map(lambda yr : 2017-yr).countByValue()

values = movie_ages.values()

filepath3 = "/Users/steve/ml-100k/u.data"
rating_data_raw = sc.textFile(filepath3)
num_ratings = rating_data_raw.count()
print("Ratings : {}".format(num_ratings))
# 100K ratings record


rating_data = rating_data_raw.map(lambda line: line.split("\t"))
num_users = rating_data.map(lambda t: t[0]).distinct().count()
ratings = rating_data.map(lambda fields: int(fields[2]))

max_rating = ratings.reduce(lambda x, y: max(x, y))
min_rating = ratings.reduce(lambda x, y: min(x, y))
mean_rating = ratings.reduce(lambda x, y: x + y) / num_ratings
median_rating = np.median(ratings.collect())

ratings_per_users = num_ratings / num_users

split_line = '=' * 82
print(" {}\n\
    ratings: {}\
    rating users; {}\
    max rating: {}\
    min rating: {}\
    mean rating {}\
    median rating {}\
    rating per users : {}\
    \n{}".format(split_line, num_ratings, num_users, max_rating, min_rating, mean_rating, median_rating, ratings_per_users, split_line))

