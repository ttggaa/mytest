import random
data = {
    "orderId": None,
    "retailOrderId": str(round(random.random() * 10000000000000)),
    "fromStationCode": "JLL",
    "fromStationName": "吉林",
    "toStationCode": "DHL",
    "toStationName": "敦化",
    "trainDate": "2018-02-12",
    "hasSeat": True,
    "passengers": [
        {
            "passengerId": 1,
            "ticketNo": None,
            "passengerName": "途牛测试单",
            "passengerSex": None,
            "passengerBirthday": None,
            "passportNo": "321181199112253533",
            "passportTypeId": "1",
            "passportTypeName": "身份证",
            "zwCode": "M",
            "zwName": "一等座",
            "cxin": None,
            "price": "86.50",
            "procedureFee": None,
            "reason": "0",
            "provinceCode": None,
            "schoolCode": None,
            "schoolName": None,
            "studentNo": None,
            "schoolSystem": None,
            "enterYear": None,
            "preferenceFromStationName": None,
            "preferenceFromStationCode": None,
            "preferenceToStationName": None,
            "preferenceToStationCode": None,
            "memo": None,
            "childName": None,
            "childBirthday": None,
            "childSex": None,
            "orderNumber": None,
            "piaoType": "1",
            "piaoTypeName": "成人票"
        }
    ],
    "contact": "邢毅勋",
    "phone": "17600105095",
    "userName": None,
    "userPassword": None,
    "insureCode": None,
    "bookType": 0,
    "deadLine": "2018-02-11 23:00:00",
    "reserveCheCi": None,
    "reserveZwCode": None,
    "grabType": "1",
    "grabFrequency": "comon",
    "grabQueue": "prior",
    "grabEntryway": "double",
    "deliveryInfo": None,
    "reservedTrainList": [
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "M",
            "trainDate": "2018-02-12",
            "trainNum": "C1025",
            "rank": 0
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "P",
            "trainDate": "2018-02-12",
            "trainNum": "G8127",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "M",
            "trainDate": "2018-02-12",
            "trainNum": "G8127",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "O",
            "trainDate": "2018-02-12",
            "trainNum": "G8127",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "P",
            "trainDate": "2018-02-12",
            "trainNum": "D7677",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "M",
            "trainDate": "2018-02-12",
            "trainNum": "D7677",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "O",
            "trainDate": "2018-02-12",
            "trainNum": "D7677",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "P",
            "trainDate": "2018-02-12",
            "trainNum": "C1025",
            "rank": 1
        },
        {
            "fromStationCode": "JLL",
            "fromStationName": "吉林",
            "toStationCode": "DHL",
            "toStationName": "敦化",
            "seatType": "O",
            "trainDate": "2018-02-12",
            "trainNum": "C1025",
            "rank": 1
        }
    ],
    "transformFlag": None,
    "departDepartTime": None,
    "destArriveTime": None,
    "isTicketMonitor": 0,
    "paymentAccount": None,
    "promotionInfo": [
        {
            "id": random,
            "code": "4",
            "type": "1",
            "orderId": None,
            "price": 30.00,
            "realPrice": 0.00,
            "num": 1,
            "addTime": None,
            "name": None,
            "rule": None,
            "status": None
        }
    ],
    "cheCi": "C1025",
    "callBackUrl": "http://train.callback.jd.com/tuniu//callback_20009.html",
    "promotionInfo": [{
            "code": str(round(random.random() * 10)),
            "type": "1",
            "price": str(round(random.random() * 100)),
            "realPrice": str(round(random.random() * 100)),
            "num":  round(random.random() * 10)
        }]
}
