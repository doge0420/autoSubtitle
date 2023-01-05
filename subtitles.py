import moviepy.editor, torch, whisper, os, sys
from stable_whisper import modify_model
from utils import writeSrtFile

def audioExtract(filename : str) -> str:
    """
    The audioExtract function extracts the audio from a video file and saves it as an mp3.
        The function takes one argument, filename, which is the name of the video file to be converted.
        The function returns a string containing the name of the newly created mp3.
    
    Parameters
    ----------
        filename : str
            Specify the name of the video file that we want to extract audio from
    
    Returns
    -------
    
        The filename of the mp3 file
    """
    video = moviepy.editor.VideoFileClip(filename)
    audio = video.audio
    os.chdir("D:/Video")
    os.chdir("subtemp/")
    audio.write_audiofile(f"{filename}.mp3")
    
    return f"{filename}.mp3"
    
def transcibe(filename : str):
    torch.cuda.empty_cache()
    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(device)
    model = whisper.load_model("small").to(device)
    modify_model(model)
    result = model.transcribe(filename, language="fr", verbose=None)
    print(result["segments"])
    
    return result["segments"], filename
    
def transcribeToSrt(result, filename):
    with open(filename + ".srt", "w", encoding="utf-8") as srt:
        writeSrtFile(result, file=srt)
    

if __name__ =="__main__":
    main_dir = os.getcwd()
    try:
        head_path, tail_path = os.path.split(sys.argv[1])
        os.chdir(f"{head_path}")
        file_name = audioExtract(tail_path)
        result, filename = transcibe(file_name)
        transcribeToSrt(result, filename)
    finally:
        print("Done")
        os.chdir(main_dir)