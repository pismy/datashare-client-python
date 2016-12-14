from orange_datashare.abstract_api import AbstractApi


class LightApi(AbstractApi):
    def set_sate(self, user_id, light_udis, on, color=None):
        request = dict(params=dict(on=on), target=dict(byUdi=light_udis))
        if color is not None:
            if isinstance(color, str):
                request["params"]["color"] = dict(hex=color)
            elif isinstance(color, tuple) or isinstance(color, list):
                if len(color) != 3:
                    raise ValueError(
                        'color must either be a a string for hew representation , a 3-tuple int for RGB or a 3-tuple float for HLS')
                if isinstance(color[0], int) and isinstance(color[1], int) and isinstance(color[2], int):
                    request["params"]["color"] = dict(rgb=color)
                else:
                    request["params"]["color"] = dict(hsl=color)
        return self.client._put('/api/v2/users/%s/commands/light/state' % user_id,
                                json=request)
