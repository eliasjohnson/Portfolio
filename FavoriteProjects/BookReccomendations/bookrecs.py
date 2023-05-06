'''
I declare that the following source code was written solely by me.
 I understand that copying any source code, in whole or in part, constitutes 
cheating, and that I will receive a zero on this project if I am 
found in violation of this policy.

Project 1: Book Reccommendations
Author: Elias Johnson
Date: September 12, 2021

This program takes two files, ratings.txt and booklist.txt, and returns a
recommendation on what books a reader would like based on your affinity score
with two other readers. 
'''

# read in booklist.txt and make it into a list of tuples outside of function
with open('booklist.txt') as file:
    books = [tuple(line.strip().split(',')) for line in file]


def booklist_dict(the_book_list):
    """Takes the string and returns a dictionary"""
    booklist_dictionary = {}
    for key, value in the_book_list:
        booklist_dictionary[value] = key
    return booklist_dictionary


def ratings_dict():
    """This function will return a dictionary whose key is even lines,
    otherwise the odd lines are the content for the previous even lines"""
    with open('ratings.txt') as file:
        query_dict = {line.strip().lower(): next(file).strip() for line in file}
    final = {}
    for i in query_dict:
        final[i] = [int(x) for x in query_dict[i].split()]
    return final


def dot_prod(x, y):
    """math for calculating the affinity scores"""
    assert len(x) == len(y) #assert makes it so it will only execute if assert evaluates to true.
    return sum(x[i] * y[i] for i in range(len(x)))


def score_finder(the_dict, scores):
    """Returns affinity scores"""
    for name_1 in the_dict:
        friends = []
        for name_2 in the_dict:
            if name_1 != name_2:
                friends.append((name_2, dot_prod(the_dict[name_1], the_dict[name_2])))
        scores[name_1] = friends
    return scores


def friends(name,scores, nfriends = 2):
    """Takes the name of the person requested and returns a string of the top 2 friends"""
    assert affinity_scores
    two_top_friends = []
    new_scores = sorted(scores[name], key = lambda sort: sort[1], reverse = True)
    for the_friends in range(nfriends):
        the_top_friends = new_scores[the_friends]
        two_top_friends.append(the_top_friends)
    return two_top_friends


def recommend(name, scores, book_data, ratings_dict, nfriends = 2):
    """Calculates the recommended books"""
    all_friends = friends(name, scores, nfriends)
    recommended_list = []
    names_values = ratings_dict[name]
    for name, score in all_friends:
        persons_ratings = ratings_dict[name]
        for book in range(len(persons_ratings)):
            if names_values[book] == 0:
                if persons_ratings[book] > 1:
                    book_keys = list(book_data.keys())
                    book_values = list(book_data.values())
                    author_book = (book_values[book], book_keys[book])
                    recommended_list.append(author_book)
    return recommended_list


def compute(the_book_list):
    """Maps ths positions for sorting lastname, firstname, book title"""
    index1 = the_book_list[0].split()
    book_name = the_book_list[0][1]
    return index1[-1], index1[0], book_name


def final_summary(scores, book_data, ratings_dict):
    """Returns the values for all the names in a long string of all the names, friends, affinity scores and book lists"""
    string_of_names = ""
    names = [name for name in ratings_dict]
    sorted_names = sorted(names)
    for output_n in sorted_names:
        string_of_names = string_of_names + report_name(output_n, scores, book_data, ratings_dict)
    return string_of_names


def report_name(output_n, scores, book_data, ratings_dict): 
    """ takes a single name and returns the final_summary of the name """
    report_str = ""
    report_str = report_str + output_n + ": " + str(friends(output_n, scores)) + "\n"
    for the_output in recommend(output_n, scores, book_data, ratings_dict):
        report_str = report_str + "\t" + "   " + str(the_output) + "\n"
    report_str += "\n"

    return report_str


def main():
    """ Displays the results. this is the main function """

    with open('recommendations.txt', 'w') as file_r:
        print(final_summary(scores, book_data, ratings_dict), file=file_r)

    while True: 
        user_input = input(str("\nEnter a readers name: (type 'exit' to end) "))
        if user_input in ratings_dict:
            print (f'Recommendations for {report_name(user_input, scores, book_data, ratings_dict)}')
        elif user_input == "exit": 
            print ("Program ended")
            break 
        else: 
            print(f'No such reader: {user_input}')


scores = {}
book_list_file = books
book_data = booklist_dict(book_list_file)
ratings_dict = ratings_dict()
affinity_scores = score_finder(ratings_dict,scores)
final_summary(scores, book_data, ratings_dict)


if __name__ == '__main__':
    main()
