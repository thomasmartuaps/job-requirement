import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, Response, session, url_for, jsonify, json
)
from werkzeug.security import check_password_hash, generate_password_hash

bp = Blueprint('github', __name__, url_prefix='/github')