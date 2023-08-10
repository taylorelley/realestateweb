def process_data(json_data):
    processed_data = []
    for item in json_data['listings']:
        processed_data.append({
            'id': item['id'],
            'price': item['price'],
            'location': item['location'],
            'type': item['type'],
            'bedrooms': item['bedrooms'],
            'bathrooms': item['bathrooms'],
            'area': item['area'],
            'land_area': item['land_area'],
        })
    return processed_data
