from pathlib import Path
from CommonSpell.encoder import Encoder
from CommonSpell.bo.tokenizer_bo import TibetanTokenizer, TibetanNormalizer
from CommonSpell.aligners.fdmp import FDMPaligner
from CommonSpell.serializers.docx import DocxSerializer
from CommonSpell.weighers.matrix_weigher import TokenMatrixWeigher
from CommonSpell.weighers.token_weigher_count import TokenCountWeigher
from CommonSpell.utils.utils import get_top_weight_index

def add_version(version_text, tokenizer):
    token_string, token_list = tokenizer.tokenize(version_text)
    return token_string, token_list


def get_common_spell_matrix(examplar_text, version_texts):
    aligner = FDMPaligner() 
    tokenizer = TibetanTokenizer(Encoder(), TibetanNormalizer(keep_eol=False))
    token_strings = []
    token_lists = []
    token_string, token_list = add_version(examplar_text, tokenizer)
    token_strings.append(token_string)
    token_lists.append(token_list)
    for version_fn, version_text in version_texts.items():
        token_string, token_list = add_version(version_text, tokenizer)
        token_strings.append(token_string)
        token_lists.append(token_list)

    token_matrix = aligner.get_alignment_matrix(token_strings, token_lists)
    tokenMatrixWeigher = TokenMatrixWeigher()
    weighers = [TokenCountWeigher()]
    for weigher in weighers:
        tokenMatrixWeigher.add_weigher(weigher, weigher_weight=1)
    weighted_matrix = tokenMatrixWeigher.get_weight_matrix(token_matrix)
    return weighted_matrix

def serialize_matrix_plaintext(weighted_token_matrix):
    serialized_matrix = ''
    for tokens_info in weighted_token_matrix:
        top_token_index = get_top_weight_index(tokens_info)
        try:
            voted_token = tokens_info[top_token_index][3]
        except:
            voted_token = ''
        serialized_matrix += voted_token
    return serialized_matrix

def serialize_matrix_docx(weighted_token_matrix, version_texts):
    output_dir = Path('./')
    version_paths = []
    version_to_serialize = {}
    for v_num, (version_fn,_) in enumerate(version_texts.items(),1):
        version_paths.append(Path(version_fn))
    text_id = 'common_spell'
    serializer = DocxSerializer(weighted_token_matrix, output_dir, text_id, version_paths, version_to_serialize)
    serialized_md = serializer.serialize_matrix()
    return serializer.save_serialized_matrix(serialized_md)