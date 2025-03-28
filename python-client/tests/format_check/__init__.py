from pathlib import Path

from tira.check_format import FormatMsgType

_ERROR = FormatMsgType.ERROR
_OK = FormatMsgType.OK
_WARN = FormatMsgType.WARN

RESOURCES = Path(__file__).parent.parent / "resources"
VALID_RUN_OUTPUT = RESOURCES / "ranking-outputs"
RUN_OUTPUT_WITH_TOO_FEW_QUERIES = RESOURCES / "ranking-output-invalid-too-few-queries"
RUN_OUTPUT_WITH_DUPLICATE_DOCUMENTS = RESOURCES / "ranking-output-invalid-duplicate-documents"
RUN_OUTPUT_WITH_TOO_FEW_COLUMNS = RESOURCES / "ranking-output-invalid-too-few-columns"
EMPTY_OUTPUT = RESOURCES / "input-run-01" / "1"
TEXT_ALIGNMENT_CORPUS_VALID_1 = RESOURCES / "text-alignment" / "1"
TEXT_ALIGNMENT_CORPUS_VALID_2 = RESOURCES / "text-alignment" / "2"
TEXT_ALIGNMENT_CORPUS_INVALID = RESOURCES / "text-alignment" / "invalid"
TEXT_ALIGNMENT_FEATURES_VALID = RESOURCES / "text-alignment" / "features"
TSV_OUTPUT_WITH_VARYING_COLUMNS = RESOURCES / "tsv-varying-columns"
TSV_OUTPUT_VALID = RESOURCES / "tsv-valid"
IR_QUERY_OUTPUT = RESOURCES / "query-processing-outputs" / "query-segmentation"
JSONL_OUTPUT_VALID = RESOURCES / "jsonl-valid"
GEN_IR_SIM_OUTPUT_VALID = RESOURCES / "gen-ir-sim-valid"
JSONL_GZ_OUTPUT_VALID = RESOURCES / "jsonl-valid-gz"
JSONL_OUTPUT_INVALID = RESOURCES / "jsonl-invalid"
STYLE_CHANGE_CORPUS_VALID = RESOURCES / "pan24-style-change-detection"
STYLE_CHANGE_PREDICTIONS_VALID = RESOURCES / "pan24-style-change-detection-prediction"
DOCUMENT_PROCESSING_KEYPHRASES = RESOURCES / "keyphrase-extraction"
DOCUMENT_PROCESSING_OUTPUT = RESOURCES / "document-processing-outputs" / "tiny-example-01"
