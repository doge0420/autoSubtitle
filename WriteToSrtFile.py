from datetime import timedelta
from typing import TextIO

def __format_time_list(timestamps : list):
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

    for timestamp in timestamps:
        temp.append(format_time(timestamp))
        
    return temp

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

    return words, __format_time_list(timestamps)

def count_list(lst : list):
    return sum(map(len, lst))

def create_sub_groups(words : list, timestamps : list):
    final = []
    group_w = []
    group_t = []
    
    for i, word in enumerate(words):
        count = count_list(group_w)
        if count <= 20:
            group_w.append(word)
            group_t.append(timestamps[i])
        else:
            final.append((group_w, [min(group_t), max(group_t)]))
            group_w = []
            group_t = []
            group_w.append(word)
            group_t.append(timestamps[i])

    final.append((group_w, [min(group_t), max(group_t)]))
    
    return final

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
    final = create_sub_groups(words, timestamps)
    writeToSrt(final, file)