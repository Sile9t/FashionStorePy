

@app.after_request
def save_response(r):
    if flask.request.method == 'POST':
        return r

    if flask.request.endpoint == 'static':
        return r

    history = flask.session.get('history', [])

    if history:
        if (history[-1][0] == flask.request.endpoint and
                history[-1][1] == flask.request.view_args):
            return r

    history.append([
        flask.request.endpoint,
        flask.request.view_args,
        r.status_code
    ])

    flask.session['history'] = history[-5:]
    return r


def url_back(fallback, *args, **kwargs):
    for step in flask.session.get('history', [])[::-1]:
        if (step[0] == flask.request.endpoint and
                step[1] == flask.request.view_args):
            continue

        if 200 <= step[2] < 300:
            return flask.url_for(step[0], **step[1])

    return flask.url_for(fallback, *args, **kwargs)