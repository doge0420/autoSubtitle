from datetime import timedelta, datetime
from typing import TextIO


def format_time_list(timestamps):
    """
    The __format_time_list function takes a list of timestamps and formats them into the format required by the srt file.
    The function returns a list of strings that are formatted in this way: HH:MM:SS,mmm
    
    Parameters
    ----------
        timestamps : list
            Pass a list of timestamps to the format_time function
    
    Returns
    -------
    
        A list of formatted timestamps
    """
    temp = []
    def format_time(time : float):
        format_time = timedelta(seconds=time)
        hours, rem = divmod(format_time.seconds, 3600)
        minutes, seconds = divmod(rem, 60)
        microseconds = format_time.microseconds

        return f"{hours:02d}:{minutes:02d}:{seconds:02d},{int(round(microseconds/1000))}"

    if hasattr(timestamps, '__iter__'):
        for timestamp in timestamps:
            temp.append(format_time(timestamp))
            
        return temp
    
    else:
        return format_time(timestamps)
    
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

def create_subtitles(words, timestamps):
    """
    The create_subtitles function takes in a list of words and timestamps, and returns a list of tuples.
    Each tuple contains two lists: the first is the subtitle text, and the second is a list containing 
    the start time (in seconds) and end time (in seconds) for that subtitle.
    
    Parameters
    ----------
        words
            Store the words in the transcript
        timestamps
            Store the start and end times of each word in the subtitle
    
    Returns
    -------
    
        A list of tuples
    """
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

def unpack(result):
    """
    The unpack function takes the result of the whisper Speech to Text API call and returns two lists:
        1. A list of all words transcribed from the audio file
        2. A list of timestamps corresponding to each word in seconds
    
    Parameters
    ----------
        result
            Pass the result of the function to unpack
    
    Returns
    -------
    
        A list of words and a list of timestamps
    """
    words = []
    timestamps = []

    for i in range(len(result)):
        for dicts in result[i]["whole_word_timestamps"]:
            for key, value in dicts.items():
                words.append(value) if key == 'word' else timestamps.append(value)

    return words, timestamps

def count_list(lst : list):
    return sum(map(len, lst))

# def create_sub_groups(words : list, timestamps : list):
#     final = []
#     group_w = []
#     group_t = []
    
#     for i, word in enumerate(words):
#         count = count_list(group_w)
#         if count <= 25:
#             group_w.append(word)
#             group_t.append(timestamps[i])
#         else:
#             final.append((group_w, [min(group_t), max(group_t)]))
#             group_w = []
#             group_t = []
#             group_w.append(word)
#             group_t.append(timestamps[i])

#     final.append((group_w, [min(group_t), max(group_t)]))
    
#     return final    

def writeToSrt(groups : list, srt_file : TextIO):
    """
    The writeToSrt function writes the given groups to a .srt file.
    The groups are written in order, with each group's text and timestamps being separated by newlines.
    Each group is assigned an index number (starting at 1) which is printed before the timestamps and text of that group.
    
    Parameters
    ----------
        groups : list
            Iterate over the groups
        srt_file : TextIO
            Specify the file to write to
    
    Returns
    -------
    
        None
    """
    for i, group in enumerate(groups, start=1):
        text, timestamps = group
        text = ''.join(text)
        print(
            f"{i}\n"
            f"{timestamps[0]} --> {timestamps[1]}\n"
            f"{text}\n",
            flush=True,
            file=srt_file
        )

def writeSrtFile(result, file : TextIO):
    """
    The writeSrtFile function takes in a list of words and timestamps, 
    and writes them to an srt file. The function also takes in a file object, 
    which it uses to write the data to. 
    
    Parameters
    ----------
        result
            Pass the result of the function unpack to writetosrt
        file : TextIO
            Specify the file to write to
    
    Returns
    -------
    
        The final result of the function is a list of tuples, where each tuple contains a list of words and a list of timestamps.
    """
    words, timestamps = unpack(result)
    words, timestamps = clean_word_list(words, timestamps)
    final = create_subtitles(words, timestamps)
    writeToSrt(final, file)