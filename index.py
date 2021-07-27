# https://github.com/nats-io/nats.py
# https://github.com/nats-io/stan.py

import asyncio
import json
from nats.aio.client import Client as NATS
from stan.aio.client import Client as STAN
import os

# class NatsConnection():
#     """docstring for SmsNotificationPublisher"""
#     def __init__(self, cluster_id, client_id, url, loop):
#         super(NatsConnection, self).__init__()
#         self.nc = NATS()
#         self.sc = STAN()
#         self.nc.connect(url, io_loop=loop)
#         self.sc.connect(cluster_id, client_id, nats=self.nc)
        
#     async def publish(self, loop):
#         data = {"message": "Remember to use the app today",
#                 "phoneNumbers": ["+256756878460"]}
        
#         # await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'), ack_handler=ack_handler)
#         await self.sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'))
#         await asyncio.sleep(1, loop=loop)

#         await sc.close()
#         await nc.close()



# natscon = NatsConnection(os.getenv('NATS_CLUSTER_ID'), os.getenv('NATS_CLIENT_ID'), os.getenv('NATS_URL'))

# class NatsCon():
#     """docstring for NatsCon"""
#     def __init__(self):
#         pass

#     async def run(self, loop):
#         self.nc = NATS()
#         self.sc = STAN()
#         await self.nc.connect(io_loop=loop)
#         await self.sc.connect(os.getenv('NATS_CLUSTER_ID'), os.getenv('NATS_CLIENT_ID'), nats=self.nc)

#         async def ack_handler(ack):
#             print("Received ack: {}".format(ack.guid))

#         # Publish asynchronously by using an ack_handler which
#         # will be passed the status of the publish.
#         # for i in range(0, 1024):
#         #     await sc.publish("foo", {"message": "Remember to use the app today",
#         #         "phoneNumbers": ["+256756878460"]}, ack_handler=ack_handler)
#         data = {"message": "Remember to use the app today",
#                 "phoneNumbers": ["+256756878460"]}
        
#         # await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'), ack_handler=ack_handler)
#         # await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'))

#         # async def cb(msg):
#         #     print("Received a message on subscription (seq: {}): {}".format(msg.sequence, msg.data))

#         # await sc.subscribe("foo", start_at='first', cb=cb)
#         await asyncio.sleep(1, loop=loop)

#         await self.sc.close()
#         await self.nc.close()

#     def publish(self):
#         data = {"message": "Remember to use the app today",
#                 "phoneNumbers": ["+256756878460"]}
        
#         # await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'), ack_handler=ack_handler)
#         self.sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'))

        
# def start_event():
#     loop = asyncio.get_event_loop()
#     # natscon = NatsConnection(os.getenv('NATS_CLUSTER_ID'), os.getenv('NATS_CLIENT_ID'), os.getenv('NATS_URL'), loop)
#     # loop.run_until_complete(natscon.publish(loop))
#     natscon = NatsCon()
#     loop.run_until_complete(natscon.run(loop))
#     natscon.publish()
#     # loop.run_until_complete(run(loop))
#     loop.close()

async def run(loop):
    nc = NATS()
    sc = STAN()
    await nc.connect(servers=[os.getenv('NATS_URL')],io_loop=loop)
    await sc.connect(os.getenv('NATS_CLUSTER_ID'), os.getenv('NATS_CLIENT_ID'), nats=nc)

    # async def ack_handler(ack):
    #     print("Received ack: {}".format(ack.guid))

    # Publish asynchronously by using an ack_handler which
    # will be passed the status of the publish.
    # for i in range(0, 1024):
    #     await sc.publish("foo", {"message": "Remember to use the app today",
    #         "phoneNumbers": ["+256756878460"]}, ack_handler=ack_handler)
    data = {"message": "Remember to use the app today",
            "phoneNumbers": ["+256756878460"]}
    
    # await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'), ack_handler=ack_handler)
    await sc.publish("smsnotification:created", json.dumps(data).encode('utf-8'))

    # async def cb(msg):
    #     print("Received a message on subscription (seq: {}): {}".format(msg.sequence, msg.data))

    # await sc.subscribe("foo", start_at='first', cb=cb)
    await asyncio.sleep(1, loop=loop)

    await sc.close()
    await nc.close()




if __name__ == '__main__':
    # loop = asyncio.get_event_loop()
    # # natscon = NatsConnection(os.getenv('NATS_CLUSTER_ID'), os.getenv('NATS_CLIENT_ID'), os.getenv('NATS_URL'), loop)
    # # loop.run_until_complete(natscon.publish(loop))
    # natscon = NatsCon()
    # loop.run_until_complete(natscon.run(loop))
    # await natscon.publish()
    # # loop.run_until_complete(run(loop))
    # loop.close()
    # start_event()

    loop = asyncio.get_event_loop()
    loop.run_until_complete(run(loop))
    loop.close()