from functools import lru_cache

from .TrueCaser import TrueCaser

__version__ = "0.0.11"


@lru_cache(maxsize=1)
def get_truecaser(tokenizer=None):
    return TrueCaser(tokenizer=tokenizer)


def get_true_case(sentence, out_of_vocabulary_token_option="title", formatted_dict=None, tokenizer=None):
    return get_truecaser(tokenizer=tokenizer).get_true_case(
        sentence,
        out_of_vocabulary_token_option=out_of_vocabulary_token_option,
        formatted_dict=formatted_dict
    )

def get_true_case_array(tokens, out_of_vocabulary_token_option="title", formatted_dict=None, tokenizer=None):
    return get_truecaser(tokenizer=tokenizer).get_true_case_array(
        tokens,
        out_of_vocabulary_token_option=out_of_vocabulary_token_option,
        formatted_dict=formatted_dict
    )