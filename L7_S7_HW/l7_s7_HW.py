"""
2. Напишите функцию группового переименования файлов. Она должна:
a. принимать параметр желаемое конечное имя файлов. При переименовании в конце имени добавляется порядковый номер.
b. принимать параметр количество цифр в порядковом номере.
c. принимать параметр расширение исходного файла. Переименование должно работать только для этих файлов внутри каталога.
d. принимать параметр расширение конечного файла.
e. принимать диапазон сохраняемого оригинального имени. Например для диапазона [3, 6] берутся буквы с 3 по 6 из исходного имени файла. 
К ним прибавляется желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.
"""
from pathlib import Path

def rename_files( processed_files_path: str='.', 
                  orig_file_name_mask: str='*', 
                  orig_file_ext_mask: str ='*',
                  dest_file_name_prefix:str=None ,
                  digits_quantity_add_in_target_name: int=1, 
                  dest_file_ext: str=None,
                  orig_to_dest_file_name_range: list[int]=[]
                  ) -> int: 
    """
    Выполняет переименование файлов по заданному пути, по заданному шаблону в имена с заданным шаблоном
    Если параметры не заданы, выполняется переименование файлов в текущей директории по маске * 
    в качестве целевого имени выступает некий порядковый номер
    
    :param processed_files_path: путь по которому находятся исходные файлы, если путь не существует, функция вернет 0 обработанных файлов.
    :type processed_files_path: str
    :param orig_file_name_mask: маска имени файлов для исходных файлов не включая расширение
    :type orig_file_name_mask: str
    :param dest_file_name_prefix: префикс для целевых имен
    :type dest_file_name_prefix: str
    :param digits_quantity_add_in_target_name: количество цифр в целевом имени файла при формировании порядкового номера, \
      генерируемый номер будет дополнен нулями до указанного значения
    :type digits_quantity_add_in_target_name: int 
    :param dest_file_ext: расширение для полного имени целевого файла. Если не указано, будет использовано расширение исходного файла
    :type dest_file_ext: float
    :param orig_to_dest_file_name_range: диапазон букв в имени оригинального фйла (включая границы), который будет добавлен между префиксом и номером \
    в имени целевого файла
    :type orig_to_dest_file_name_range: list[int] будут использованы только первые два значения списка. \
        Анализируется имя исходного файла без расширения. Если любое из двух значений выйдет за границы целевого имени, то
          будет использована только та часть имени, которая попадет в заданные границы.\
            Если первое значения не меньше второго, никакая часть исходного имени не будет добавлена в целевое. 
    
    :rtype: int
    :return : количество обработанных файлов
    """
    files_processed_num = 0
    print()
    full_path = Path(processed_files_path).resolve()
    p = Path(full_path).glob('.'.join([orig_file_name_mask, orig_file_ext_mask]))
    files_processed_num = 0
    for file in p:
        if not file.is_file():
            continue
        file_name = f'{files_processed_num:0{digits_quantity_add_in_target_name}}'
        if dest_file_name_prefix:
            file_name = dest_file_name_prefix + file_name
        if len(orig_to_dest_file_name_range) >= 2:
          file_name += Path(file).stem[orig_to_dest_file_name_range[0] - 1:orig_to_dest_file_name_range[1]]
        if dest_file_ext:
            file_name = '.'.join([file_name, dest_file_ext])
        else:
            file_name = ''.join([file_name, Path(file).suffix])
        file_name = Path(file).parent / file_name
        if not Path(file_name).exists():
          file.rename(file_name)
        files_processed_num += 1
    return files_processed_num

#########################################################################################
# files_processing/__init__.py
from l7_s7_files_creator import generate_files_with_specified_extension, generate_files_with_specified_extensions
from l7_s7_t1_HW_module import rename_files

"""
К сожалению на первой строке импорта ловлю ошибку
No module named 'l7_s7_files_creator' при этом сам файл существует. При указании в IDE имя файла подсвечивается, как существующее, но при импорте 
имя модуля не определяется.
Почему - не удалось разобраться ни на семинаре, ни по результатам лекции.
"""

__all__ = ['generate_files_with_specified_extension', 'generate_files_with_specified_extensions', 'rename_files']


##########################################################################################
from files_processing import rename_files

def main():
    rename_files('./L7_S7_HW/files', dest_file_name_prefix='new', orig_to_dest_file_name_range=[2, 3], digits_quantity_add_in_target_name=8)


if __name__ == '__main__':
    main()
