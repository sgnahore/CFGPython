import requests


def recipe_search(ingredient):
    '''
  
  :param ingredient: The ingredient wanted for the recipe search
  :return: the api search results from the inputted ingredient
  '''
    app_id = '2219b015'  # app id needed to use the API
    app_key = '2872ea2f384c23afe611f6816c90b649'  # app key needed to use the API
    result = requests.get(
        'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(
            ingredient, app_id, app_key))
    data = result.json()
    return data['hits']


def alpha(results):
    '''
  This function takes the results of the recipe search for an ingredient and ouputs them in a alphabetical list
  :param results: the results from the recipe_search function
  :return: the recipes from the results in alphabetical order
  '''
    recipe_names = []  # empty list ready for recipes
    our_recipes = {}  # empty dictionary ready for recipe:url inputs 
    for result in results:
        recipe = result['recipe']
        our_recipes[recipe['label']] = recipe['url']  # creates a nested dictionary with {recipe:url} inputs
        recipe_names.append(recipe['label'])  # creates a list with all the recipe names
    sorted_list = sorted(recipe_names)  # orders the recipe names alphabetically
    for item in sorted_list:  # iterates through the sorted list
        print(item)  # prints the recipe name
        print(our_recipes[item])  # accesses the recipes url from dictionary and prints
    return


def yieldfun(results):
    '''
    This function takes the results of the recipe search for an ingredient and ouputs them in a ascending yield amount
    :param results: the results from the recipe_search function
    :return: the recipes from the results in order of ascending yield amount
    '''
    recipe_names = {}  # empty dictionary ready for  recipe:yield inputs
    our_recipes = {}  # empty dictionary ready for recipe:url inputs
    for result in results:  # iterates through the recipes 
        recipe = result['recipe']
        our_recipes[recipe['label']] = recipe['url']  # adds the recipe:url into the dictionary our_recipes
        recipe_names[recipe['label']] = recipe['yield']  # adds the recipe:yield into the dictionary recipe_names
        sorted_list = {
            k: v
            for k, v in sorted(recipe_names.items(), key=lambda item: item[1])
        }  # sorts the dictionary recipe_names by the keys (the yield)
    for key in sorted_list:  # iterates through the sorted dictionary
        print(key + ' (Yield = ' + str(sorted_list[key]) + ")")  # prints the recipe name and the yield
        print(our_recipes[key])  # prints the url for this recipe 
    return


def calories(results):
    '''
    This function takes the results of the recipe search for an ingredient and outputs them in order of ascending number of calories 
    :param results: the results from the recipe_search function
    :return: the recipes from the results in order of ascending calorie amount
    '''
    recipe_names = {}  # empty dictionary ready for recipe:calories inputs
    our_recipes = {}  # empty dictionary ready for recipe:url inputs
    for result in results:  # iterates through the recipes
        recipe = result['recipe']
        our_recipes[recipe['label']] = recipe['url']  # adds each the recipe:url to the dictionary
        recipe_names[recipe['label']] = recipe['calories']  # adds each recipe:calories to the dictionary
        sorted_list = {
            k: v
            for k, v in sorted(recipe_names.items(), key=lambda item: item[1])
        }  # sorts the dictionary by the keys (the calories)
    for key in sorted_list:  # iterates through the sorted dictionary 
        print(key + ' (Calories = ' + str(sorted_list[key]) + ")")  # prints the recipe name and the calories
        print(our_recipes[key])  # prints the url
    return


def totaltime(results):
    '''
    This function takes the results of the recipe search for an ingredient and outputs them in order of ascending time to make the recipe
    :param results: the results from the recipe_search function
    :return: the recipes from the results in order of ascending time taken 
    '''
    recipe_names = {}  # empty dictionary ready for recipe:time inputs
    our_recipes = {}  # empty dictionary ready for recipe:url inputs
    for result in results:  # iterates through the recipes
        recipe = result['recipe']
        our_recipes[recipe['label']] = recipe['url']# adds each the recipe:url to the dictionary
        recipe_names[recipe['label']] = recipe['totalTime'] # adds each recipe:totaltime to the dictionary
        sorted_list = {
            k: v
            for k, v in sorted(recipe_names.items(), key=lambda item: item[1])
        }# sorts the dictionary by the keys (the total time)
    for key in sorted_list: # iterates through the sorted dictionary 
        print(key + ' (Total time = ' + str(sorted_list[key]) + ")") # prints the recipe name and the total time
        print(our_recipes[key]) # prints the url
    return


def main():
    '''
  This is the main function for the whole recipe search
  It asks for the ingredient and the choice of ordering and then using if statements calls on the functions above to output the recipes in the chosen order
  :return: 
  '''
    ingredient = input('Enter an ingredient: ') #asks for the ingredient input
    results = recipe_search(ingredient) #calls the search function to find the recipes in the api
    sort_by = input("""Please choose how you would like these sorted: 
    1: Alphabetically (A-Z)
    2: Calories
    3: Total time
    4: Yield
Please enter a number 1-4: """) #asks how it would be sorted
    if sort_by == "1":#if they want alphabetical calls the alpha function
        alpha(results)
    elif sort_by == "2":#else if they want calories calls the calories function
        calories(results)
    elif sort_by == "3":#else if they want total time calls the totaltime function
        totaltime(results)
    elif sort_by == "4":#else if they want yield calls the yield function
        yieldfun(results)


main()

