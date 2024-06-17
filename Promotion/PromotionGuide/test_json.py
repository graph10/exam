def data(content):
# Инициализация переменных
    name = []
    shops = []
    image = []
    days = []
    type = []

    part1 = "https://skidkaonline"

    # Разбиваем содержимое файла на блоки
    blocks = content.split('] [')
    for block in blocks:
        # Удаляем лишние символы
        block = block.replace('[', '').replace(']', '').replace('{', '').replace('}', '')
        
        # Разбиваем блок на элементы
        elements = block.split(' ')
        
        # Переменные для временного хранения данных
        temp_name = ''
        temp_shops = ''
        temp_image = ''
        temp_days = ''
        temp_type = ''
            
        # Переменная для отслеживания текущего ключа
        current_key = ''
        
        for element in elements:
        # Проверяем, является ли элемент ключом
            if element in ['daystitle', 'imagefull', 'name', 'shops_ids', 'type'] or element in ['daystitle', 'imagefull', 'name', 'shops_Ids', 'type']:
                current_key = element
            else:
                # Добавляем значение к соответствующему ключу
                if current_key == 'daystitle':
                    temp_days += element + ' '
                    # Удаление тегов span
                    temp_days = temp_days.replace('<span>', '').replace('</span>', '')
                elif current_key == 'imagefull':
                    temp_image += element + ' '
                    # Сохраняем только часть строки после src
                    temp_image = temp_image[temp_image.find("src=") + 4:]
                    temp_image = temp_image[:temp_image.find(" ")]
                    parts = temp_image.split('.', 1)
                    if len(parts) > 1:  # Проверяем, есть ли вторая часть после точки
                        temp_image = f"{part1}.{parts[1]}"
                elif current_key == 'name':
                    temp_name += element + ' '
                elif current_key == 'type':
                    temp_type += element + ' '
                elif current_key == 'shops_ids' or current_key == 'shops_Ids':
                    temp_shops += element + ' '

            
        # Добавляем данные в итоговые списки
        days.append(temp_days.strip())
        image.append(temp_image.strip())
        name.append(temp_name.strip())
        shops.append(temp_shops.strip())
        type.append(temp_type.strip())
            
    combined_data = list(zip(days, image, name, shops, type))
    combined_data = list(set(combined_data))
    return combined_data