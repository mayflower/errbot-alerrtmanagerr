import json
from errbot import BotPlugin, webhook


class Alerrtmanagerr(BotPlugin):
    """
    Get alerts from Prometheus Alertmanager via webhooks
    """

    @webhook('/alerrt/<recipient>/<server>/')
    def alerrt(self, incoming_request, recipient, server):
        separator = '-'
        data = incoming_request
        identifier = self.build_identifier(recipient + "@" + server)
        self.send(identifier, separator * 3 + " " + data['commonLabels']['alertname'] + " " + separator * 3)
        self.send(identifier, separator * 20)
        for alert in data['alerts']:
            self.send(identifier, "[Summary]: " + alert['annotations']['summary'] + "\n[Description]: " + alert['annotations']['description'])
        self.send(identifier, separator * 20)
        return None
