from errbot import BotPlugin, webhook


class Alerrtmanagerr(BotPlugin):
    """
    Get alerts from Prometheus Alertmanager via webhooks
    """

    @webhook('/alerrt/<recipient>/<server>/')
    def alerrt(self, data, recipient, server):
        identifier = self.build_identifier(recipient + "@" + server)
        for alert in data['alerts']:
            self.send_card(
                to=identifier,
                summary='Alert of type "{}" {}'.format(
                    data['commonLabels']['alertname'],
                    data['status']
                ),
                title=alert['annotations']['description'],
            )
