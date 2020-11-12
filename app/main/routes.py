import json
from flask import request, jsonify
from app.main import bp
from app.helpers import compare_strings


@bp.route("/compare_texts", methods=["POST"])
def compare_texts():
    texts = json.loads(request.data)
    # should probably add some input validation here (marshmallow?)
    result = compare_strings(texts[0], texts[1])
    return jsonify(result)
