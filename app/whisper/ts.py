from faster_whisper import WhisperModel
import argparse

def initialize_model(model_size, device="cuda", compute_type="float16"):
    """
    Initialize the Whisper model with specified parameters.
    
    Parameters:
    - model_size (str): The size of the model to be used.
    - device (str): The device to run the model on, either 'cpu' or 'cuda'.
    - compute_type (str): The compute type, e.g., 'int8', 'int8_float16', 'float16'.
    
    Returns:
    - model (WhisperModel): The initialized Whisper model.
    """
    return WhisperModel(model_size, device=device, compute_type=compute_type)

def transcribe_audio(model, audio_file, beam_size=5):
    """
    Transcribe the given audio file using the specified Whisper model.
    
    Parameters:
    - model (WhisperModel): The Whisper model to use for transcription.
    - audio_file (str): The path to the audio file to be transcribed.
    - beam_size (int): The beam size to use for transcription.
    
    Returns:
    - segments (list): List of transcribed segments.
    - info (dict): Information about the transcription, including detected language and its probability.
    """
    return model.transcribe(audio_file, beam_size=beam_size)

def print_transcription_info(info, segments):
    """
    Print the transcription information and segments.
    
    Parameters:
    - info (dict): Information about the transcription.
    - segments (list): List of transcribed segments.
    """
    print("Detected language '%s' with probability %f" % (info.language, info.language_probability))
    for segment in segments:
        print("[%.2fs -> %.2fs] %s" % (segment.start, segment.end, segment.text))

def main(model_size, audio_file, device, compute_type):
    # Initialize model (default: run on CPU with INT8)
    model = initialize_model(model_size, device, compute_type)
    
    # Optionally, run on GPU with different compute types:
    # model = initialize_model(model_size, device="cuda", compute_type="int8_float16")
    # model = initialize_model(model_size, device="cuda", compute_type="float16")
    
    # Transcribe audio
    segments, info = transcribe_audio(model, audio_file)
    
    # Print transcription info
    print_transcription_info(info, segments)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Transcribe audio using Whisper model.")
    parser.add_argument("--model_size", type=str, help="The size of the Whisper model to use (e.g., 'large-v3').", default='large-v3')
    parser.add_argument("--audio_file", type=str, help="The path to the audio file to be transcribed.")
    parser.add_argument("--device", type=str, help="The device to run the model on, either 'cpu' or 'cuda'.", default='cuda')
    parser.add_argument("--compute_type", type=str, help="The compute type, e.g., 'int8', 'int8_float16', 'float16'.", default='float16') 
    
    args = parser.parse_args() 
    
    main(args.model_size, args.audio_file, args.device, args.compute_type)
    
# model_size = "large-v3"
# audio_file = "app/whisper/Recording.m4a 