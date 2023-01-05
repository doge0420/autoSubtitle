from utils import writeSrtFile, count_list, format_time_list
import numpy as np

timestamps = [0.39, 0.75, 1.0499999523162842, 1.2299999594688416, 1.2299999594688416, 1.4700000286102295, 1.4700000286102295, 1.4700000286102295, 3.0799999237060547, 3.179999828338623, 3.179999828338623, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.209999829530716, 3.2899999916553497, 3.3599999845027924, 3.3599999845027924, 3.3599999845027924, 3.3599999845027924, 3.3599999845027924, 4.629999995231628, 6.019999980926514, 6.579999923706055, 6.599999904632568, 7.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 8.980000019073486, 9.989999771118164, 9.989999771118164, 10.069999694824219, 10.079999923706055, 10.139999866485596, 10.150000095367432, 10.15999984741211, 10.15999984741211, 10.15999984741211, 10.15999984741211, 10.279999732971191, 10.609999656677246, 10.609999656677246, 10.609999656677246, 10.609999656677246, 10.609999656677246, 10.929999828338623, 11.389999866485596, 11.619999408721924, 11.829999446868896, 11.849999904632568, 12.119999408721924, 12.539999809265137, 12.539999809265137, 13.829999446868896, 13.829999446868896, 13.829999446868896, 14.249999523162842, 14.249999523162842, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 14.299999713897705, 15.299999713897705, 15.719999313354492, 15.979999885559081, 17.199999809265137, 17.199999809265137, 17.199999809265137, 17.299999237060547, 17.299999237060547, 17.299999237060547, 17.299999237060547, 17.299999237060547, 18.549999237060547, 19.0099995803833, 19.559999465942383, 20.84999942779541, 20.84999942779541, 20.84999942779541, 20.84999942779541, 20.84999942779541, 21.75999927520752, 21.77999973297119, 22.499999046325684, 22.519999504089355, 22.59999942779541, 22.619998931884766, 22.619998931884766, 22.739999771118164, 23.739998817443848, 24.07999897003174, 24.1899995803833, 24.3799991607666, 24.519999504089355, 24.56999969482422, 25.02999973297119, 25.809999465942383, 25.809999465942383, 25.809999465942383, 25.809999465942383, 25.859999656677246, 26.25, 26.260000228881836, 26.369998931884766, 26.91999912261963, 29.54999828338623, 30.27999973297119, 30.27999973297119, 30.27999973297119, 30.27999973297119, 30.27999973297119, 30.27999973297119, 30.31999969482422, 30.389999389648438, 30.699999809265137, 30.699999809265137, 30.699999809265137, 31.789999961853027, 31.809998512268066, 31.969998359680176, 31.969998359680176, 32.20999813079834, 32.23999786376953, 32.45999813079834, 32.539998054504395, 32.58999824523926, 32.58999824523926, 32.61999797821045, 32.789998054504395, 32.89999771118164, 33.049997329711914, 33.189998626708984, 33.2599983215332, 33.35999870300293, 33.46999740600586, 33.5099983215332, 33.51999855041504, 33.58999824523926, 33.71999740600586, 33.71999740600586, 38.19999885559082, 38.19999885559082, 38.479997634887695, 38.549997329711914, 38.549997329711914, 38.569997787475586, 38.569997787475586, 38.799997329711914, 39.05999755859375, 39.05999755859375, 39.05999755859375, 39.099998474121094, 39.1299991607666, 39.13999938964844, 39.13999938964844, 39.13999938964844, 39.13999938964844, 39.13999938964844, 39.13999938964844, 39.13999938964844, 39.31999969482422, 39.329999923706055, 39.599998474121094, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.79999923706055, 39.80999946594238, 40.739999771118164, 40.99999809265137, 40.99999809265137, 41.03999900817871, 41.63999938964844, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64, 41.64]

words = [' Dans', ' cette', ' première', ' vidéo', ' de', ' la', ' série', ' sur', ' E', 'ater', 'T', 'ools,', ' tu', ' vas', ' apprendre', ' à', ' quoi', ' sert', ' la', ' fonction', ' CO', 'UN', 'T', ' et', ' comment', ' l', "'", 'util', 'iser.', ' E', 'ater', 'T', 'ools', ' c', "'", 'est', ' un', ' module', ' nat', 'if', ' à', ' pit', 'on', ' qui', ' a', ' plein', ' de', ' fon', 'ctions', ' qui', ' nous', ' permett', 'ent', ' de', ' créer', ' des', ' id', 'ér', 'ateurs', ' effic', 'aces', ' et', ' rap', 'ides.', ' Donc', ' comme', ' son', ' nom', ' l', "'", 'ind', 'ique,', ' CO', 'UN', 'T', ' CO', 'UN', 'TS', ' et', ' ça', ' jusqu', "'", 'à', ' l', "'", 'inf', 'ini.', ' Cette', ' fonction', ' va', ' ac', 'cep', 'ter', ' deux', ' arguments', ' option', 'nels.', ' Le', ' premier', ' concer', 'ne', ' le', ' nombre', ' de', ' départ,', ' sa', ' valeur', ' par', ' déf', 'aut', ' est', ' 0.', ' Et', ' le', ' deuxième', ' le', ' pas,', ' qui', ' est', ' ét', 'ab', 'li', ' à', ' 1', ' par', ' déf', 'aut.', ' Je', ' veux', ' faire', ' un', ' programme', ' qui', ' compte', ' de', ' 10', ' à', ' 0.', ' Donc', ' je', ' commence', ' le', ' compt', 'eur', ' à', ' 10', ' et', ' je', ' mets', ' le', ' pas', ' à', ' moins', ' 1', ' comme', ' ça', ' on', ' compte', ' à', ' l', "'", 'en', 'vers.', ' Ensuite', ' je', ' fais', ' une', ' bou', 'cle', ' qui', ' va', ' aff', 'icher', ' chaque', ' valeur', ' et', ' je', ' mets', ' un', ' break', ' quand', ' le', ' i', ' atte', 'int', ' 0', ' parce', ' que', ' sinon', ' le', ' code', ' va', ' continuer', ' jusqu', "'", 'à', ' l', "'", 'inf', 'ini.', ' Si', ' tu', ' as', ' trouvé', ' cette', ' vidéo', ' ut', 'ile', ' n', "'", 'hés', 'ite', ' pas', ' à', ' t', "'", 'ab', 'onner', ' pour', ' plus.']

# pour rassembler les mots qui commencent pas par un espace
def clean_word_list(words : list, timestamps : list):
    """
    The clean_word_list function takes a list of words and returns a new list with the 
    words cleaned up. The function removes any leading or trailing whitespace, and combines 
    any words that were separated by whitespace in the original string. For example, if we pass 
    the string &quot;hello   there&quot; to this function it will return [&quot;hello&quot;, &quot;there&quot;].
    
    Parameters
    ----------
        words : list
            Pass a list of words to the function
    
    Returns
    -------
    
        A list of words with the first letter removed
    """
    word_list = []
    timestamp = []
    temp_timestamp = []
    for i, word in enumerate(words):
        if word[0] == " ":
            word_list.append(word)
            timestamp.append(timestamps[i])
            if len(temp_timestamp) > 0:
                timestamp[-1] = temp_timestamp[0]
                temp_timestamp = []
        else:
            word_list[-1] += word
            temp_timestamp.append(timestamps[i])
            
    return word_list, list(timestamp)

# return [wordlist, [start, end]]
# def create_groups(word : list, time : list):
#     final = []
#     temp_word = []
#     temp_time = []
#     delta_list = list(np.diff(time))
#     last_min_time = 0
    
#     for i, word in enumerate(word):
#         if count_list(word) <= 30 and delta_list[i] <= 1:
#             temp_word.append(word)
#             temp_time.append(time[i])
#         else:
#             print(temp_time)
#             final.append((temp_word, [format_time_list(last_min_time), format_time_list(temp_time[-1])]))
#             last_min_time = temp_time[0]
#             temp_word = []
#             temp_time = []
 
#     if len(temp_time) > 0:
        # final.append((temp_word, [format_time_list(last_min_time), format_time_list(temp_time[-1])]))
    
#     return final

def create_subtitles(words, timestamps):
    # Initialize an empty list to store the subtitle groups
    subtitles = []

    # Initialize the start and end times for the current subtitle group
    start_time = end_time = timestamps[0]

    # Initialize an empty string to store the current subtitle group
    current_subtitle = ""

    # Loop through the words and timestamps
    for i in range(len(words)):
        # Append the current word to the current subtitle group
        current_subtitle += words[i]

        # Update the end time to the current timestamp
        end_time = timestamps[i]

        # If the current subtitle group is too long or the time difference between the start and end times is too great,
        # store the current subtitle group in the list of subtitles and reset the current subtitle group and start/end times
        if len(current_subtitle) > 30 or end_time - start_time > 1:
            if start_time == end_time:
                end_time += 0.5
            subtitles.append(([current_subtitle.strip()], [format_time_list(start_time), format_time_list(end_time)]))
            current_subtitle = ""
            start_time = end_time = timestamps[i]

    if start_time == end_time:
        end_time += 0.5
    # Add the final subtitle group to the list of subtitles
    subtitles.append(([current_subtitle.strip()], [format_time_list(start_time), format_time_list(end_time)]))

    return subtitles


word, time = clean_word_list(words, timestamps)
# print(list(map(len, [word, time])))

print(create_subtitles(word, time))