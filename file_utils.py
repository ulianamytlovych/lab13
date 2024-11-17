def save_list_to_file(lst, filename):
    try:
        with open(filename, 'w', encoding='utf-8') as file:
            for item in lst:
                file.write(f"{item}\n")
    except Exception as e:
        print(f"Помилка при збереженні списку у файл: {e}")
