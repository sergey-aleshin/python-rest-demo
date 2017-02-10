import falcon
import json
from tasks import check_url


def get_req_data(req):
    if req.content_length:
        return json.load(req.stream)

    raise Exception("No data passed")


class Resource:
    def on_post(self, req, resp):

        req_data = None
        try:
            req_data = get_req_data(req)
        except:
            pass

        if req_data is None or req_data.get("url") is None:
            resp.status = falcon.HTTP_400
            return

        check_url.delay(req_data['url'])

        resp.body = json.dumps(req_data) + "\n"


api = falcon.API()
api.add_route('/resource', Resource())