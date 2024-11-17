from file_utils import save_list_to_file


my_list = ["Апельсин", "Яблуко", "Банан","Манго","Ананас"]

file_name = "output.txt"

save_list_to_file(my_list, file_name)

print(f"Список успішно збережено у файл {file_name}.")
