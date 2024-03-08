
def validate_ted_or_podcast(ted_or_podcast):
    if not isinstance(ted_or_podcast, str):
        raise TypeError("ted_or_podcast must be of type str")

    if ted_or_podcast not in ('ted', 'podcast'):
        raise ValueError("ted_or_podcast must be either 'ted' or 'podcast'")

def validate_input_transcript(input_transcript):
    if not isinstance(input_transcript, str):
        raise TypeError("user_transcript must be of type str")

    if input_transcript == "":
        raise ValueError("user_transcript must not be empty")