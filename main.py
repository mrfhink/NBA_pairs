import json
from urllib.request import urlopen

def find_pairs(data_nba: dict, target: int, partial_sum=[], pair=[], result=[]):
    """
    :param result: result list containing first name, last name and heights of pairs found
    :param partial_sum: internal variable that sums a pair of heights to compare with the target
    :param data_nba: dict read from json file containing nba players data
    :param target: number defined by user to find pairs
    :param pair: internal variable that holds first and last names of the pairs
    :return: result
    """
    if sum(partial_sum) == target and len(pair) == 2:
        print("Pair found: %s heights %s add up %s" % (pair, partial_sum, target))
        return [pair[0], pair[1], partial_sum[0], partial_sum[1]] #Getting out of recursivity
    if sum(partial_sum) != target and len(pair) == 2:
        return [] #Getting out of recursivity

    for i in range(len(data_nba)):

        player_height = int(data_nba[i].get("h_in"))
        remaining_data = data_nba[i + 1:]
        player_name = [str(data_nba[i].get("first_name") + " " + data_nba[i].get("last_name"))]

        temp = find_pairs(remaining_data, target, partial_sum + [player_height], pair + [player_name])

        if len(temp) == 4:
            result.append(temp) #Append pairs that added up the input
    return result

if __name__ == "__main__":

    print('Please enter the desired number...')
    target_height_sum = int(input('Number: '))

    # Getting data from url
    url = "https://mach-eight.uc.r.appspot.com/"
    response = urlopen(url)
    data_nba = json.loads(response.read()).get('values')

    result = find_pairs(data_nba, target_height_sum)

    if not result:
        print("Not matches found")
    else:
        print("Matches found: %s" % len(result))
