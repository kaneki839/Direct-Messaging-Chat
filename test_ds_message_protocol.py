# Jyun Rong Liu
# jyunrl@uci.edu
# 16169703

import ds_protocol
import unittest
import ds_client


class DsProtocolTest(unittest.TestCase):
    def test_dm(self):
        token, send, recv, client = ds_client.only_join('168.235.86.101',
                                                        3021, 'kimikllua',
                                                        '1234')

        send_msg = ds_protocol.direct_msg(token, 'Hello!', 'ohhimark')
        assert ds_client.flush_and_recv(
            send, send_msg, recv
            ) == {"response": {"type": "ok", "message": "Direct message sent"}}

        find_new = ds_protocol.retrieve_new(token)
        assert ds_client.flush_and_recv(
            send, find_new, recv
            ) == {'response': {'type': 'ok', 'messages': []}}
        find_all = ds_protocol.retrieve_all(token)

        assert ds_client.flush_and_recv(
            send, find_all, recv
            ) == {"response": {"type": "ok", "messages": [
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678749599.324168"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678749647.644342"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678749747.715581"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678750050.650922"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678751431.853112"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678751453.0249999"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678751507.013769"
                },
                {
                    "message": "dirmsg",
                    "from": "kimikllua",
                    "timestamp": "1678751617.8256488"
                },
                {
                    "message": "dir",
                    "from": "kimikllua",
                    "timestamp": "1678755857.71297"
                },
                {
                    "message": "dir",
                    "from": "kimikllua",
                    "timestamp": "1678756418.9302359"
                },
                {
                    "message": "diddddd l",
                    "from": "kimikllua",
                    "timestamp": "1678756545.842273"
                },
                {
                    "message": "test",
                    "from": "kimikllua",
                    "timestamp": "1678756640.220017"
                },
                {
                    "message": "hhh",
                    "from": "kimikllua",
                    "timestamp": "1678756707.5308008"
                },
                {
                    "message": "ii",
                    "from": "kimikllua",
                    "timestamp": "1678756805.596375"
                },
                {
                    "message": "3",
                    "from": "kimikllua",
                    "timestamp": "1678756859.3576078"
                },
                {
                    "message": "i",
                    "from": "kimikllua",
                    "timestamp": "1678756948.552879"
                },
                {
                    "message": "6",
                    "from": "kimikllua",
                    "timestamp": "1678757326.663738"
                },
                {
                    "message": "ding",
                    "from": "kimikllua",
                    "timestamp": "1678757759.619424"
                },
                {
                    "message": "ddd",
                    "from": "kimikllua",
                    "timestamp": "1678757797.658989"
                },
                {
                    "message": "ododod",
                    "from": "kimikllua",
                    "timestamp": "1678757839.1769059"
                },
                {
                    "message": "ooo",
                    "from": "kimikllua",
                    "timestamp": "1678758011.1455538"
                },
                {
                    "message": "ooo",
                    "from": "kimikllua",
                    "timestamp": "1678758066.268"
                },
                {
                    "message": "o",
                    "from": "kimikllua",
                    "timestamp": "1678758523.3993092"
                },
                {
                    "message": "test",
                    "from": "kimikllua",
                    "timestamp": "1678758541.301365"
                },
                {
                    "message": "ee",
                    "from": "kimikllua",
                    "timestamp": "1678758570.149465"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774626.682979"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774626.682979"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774695.251812"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774695.251812"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774709.5500119"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774723.804065"
                },
                {
                    "message": "Hello!",
                    "from": "kimikllua",
                    "timestamp": "1678774723.804065"
                },
                {
                    "message": "d",
                    "from": "kimikllua",
                    "timestamp": "1678778049.32672"
                },
                {
                    "message": "eee",
                    "from": "kimikllua",
                    "timestamp": "1678778090.1563241"
                }
                ]
            }
            }
        client.close()


if __name__ == "__main__":
    unittest.main()
