def Weather(records):
    city_data = {}
    results = {}

    for record in records:
        city = record.get('city')

        if city not in city_data:
            city_data[city] = {'temprature_sum':0,'temp_count':0,'humidity_sum':0,'humidity_count':0}

        if 'temperature' in record:
            city_data[city]['temprature_sum']+=record['temperature']
            city_data[city]['temp_count']+=1

        if 'humidity' in record:
            city_data[city]['humidity_sum']+=record['humidity']
            city_data[city]['humidity_count']+=1

    for city,data in city_data.items():
        avg_temp = data['temprature_sum']/data['temp_count'] if data['temp_count']>0 else None
        avg_humidity = data['humidity_sum']/data['humidity_count'] if data['humidity_count']>0 else None

        results[city]={
            'Avg_Temprature':avg_temp,
            'Avg_Humidity':avg_humidity
        }
    return results

def input_records():
    records=[]
    n = int(input('Enter Number of data: '))
    while n!=0:
        data = {
            'city': input('Enter City: '),
            'temperature':input('Enter temperature'),
            'humidity':input('Enter humidity')
        }
        try:
            data['temperature']=int(data['temperature'])
            data['humidity']=int(data['humidity'])
        except:
            print('Invalid record! ')
            return input_records()
        records.append(data)
        n-=1
    return records


records = input_records()
avg = Weather(records)
print(avg)