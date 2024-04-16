import faker
import random
from datetime import datetime
import json
import time

fake = faker.Faker()

from confluent_kafka import SerializingProducer


def generate_sales_transactions():
    user = fake.simple_profile()

    return {
        "transactionId": fake.uuid4(),
        "productId": random.choice(["product1", "product2", "product3", "product4", "product5", "product6"]),
        "productName": random.choice(["laptop", "mobile", "tablet", "watch", "headphone", "speaker"]),
        "productCategory": random.choice(["Electroinc", "Fashion", "Grocery", "Home", "Beauty", "Sports"]),
        "productPrice": round(random.uniform(10, 1000), 2),
        "productQuantity": random.randint(1, 10),
        "productBrand": random.choice(["Apple", "Samsung", "OnePlus", "MI", "Sony"]),
        "currency": random.choice(['USD', 'GBP']),
        "customerId": user['username'],
        "transactionDate": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S.%f%z"),
        "paymentMethod": random.choice(["credit_card", "debit_card", "online_transfer"])
    }

def delivery_report(err, msg):
    if err is not None:
        print(f'Message delivery failed {err}')
    else:
        print(f'Message delivered to {msg.topic} [{msg.partition}]')


def main():
    topic = 'financial_transactions'
    producer = SerializingProducer({
        'bootstrap.servers': 'localhost:9092'
    })

    curr_time = datetime.now()

    while (datetime.now()- curr_time).seconds < 120:
        try:
            transaction = generate_sales_transactions()
            transaction['totalAmount'] = transaction['productPrice'] * transaction['productQuantity']
            print(transaction)
            producer.produce(topic, key=transaction['transactionId'], value=json.dumps(transaction), on_delivery=delivery_report)
            producer.poll(0)
            time.sleep(5)
        except BufferError:
            print('Buffer full! waiting...')
            time.sleep(1)
        except Exception as e:
            print(e)


if __name__ == '__main__':
    main()