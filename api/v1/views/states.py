#!/usr/bin/python3
"""Create a new view for State objects
"""
from flask import Flask, make_response, abort, jsonify, request
from api.v1.views import app_views
from models import storage
from models.state import State

@app_views.route('/states', methods=['GET', 'POST'])
def get_all_states():
    """Retrieves the list of all State
    """
    n = []
    all_states = storage.all('State')
    for i in all_states.values():
        n.append(i.to_dict())
    return jsonify(n)


@app_views.route('/states/<state_id>', methods=['GET'], strict_slashes=False)
def get_states(state_id):
    """Retrieves a State object
    """
    state_iter = storage.get("State", state_id)
    if state_iter is None:
        abort(404)
    return jsonify(state_iter.to_dict())


@app_views.route('/states/<state_id>', methods=['DELETE'], strict_slashes=False)
def delete_states(state_id):
    """Deletes a State object
    """
    state_iter = storage.get("State", state_id)
    if state_iter is None:
        abort(404)
    storage.delete(state_iter)
    storage.save()
    return make_response(jsonify({}), 200)


@app_views.route('/states', methods=['POST'], strict_slashes=False)
def post_states():
    """Creates a State: POST
    """
    if not request.get_json():
        abort(404, "Not a JSON")

    if 'name' not in request.get_json():
        abort(404, "Missing name")

    datatype = request.get_json()
    temp = State(**dataype)
    temp.save()
    return make_response(jsonify(temp.to_dict()), 201)

@app_views.route('/states/<state_id>', methods=['PUT'], strict_slashes=False)
def put_state(state_id):
    """State object: PUT
    """
    comodin = storage.get("State", state_id)

    if comodin is None:
        abort(404, "Not a JSON")

        if not request.get_json():
            abort(400, description="Not a JSON")

    ignore = ['id', 'created_at', 'updated_at']
    arlequin = request.get_json()

    for key, value in arlequin.items():
        if key not in ignore:
            setattr(state, key, value)
    storage.save()
    return make_response(jsonify(state.to_dict()))
