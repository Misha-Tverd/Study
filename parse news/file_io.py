from pathlib import Path
import csv
def path_file(input_file):
    return Path(input_file).read_text(encoding='utf-8').splitlines()

def parse(line):
    parts = [p.strip() for p in line.split('|')]
    if len(parts) != 3:
        return None
    return {'data': parts[0], 'category': parts[1], 'title': parts[2]}

def convert(lines):
    news = []
    for line in lines:
        parset = parse(line)
        if parset:
            news.append(parset)
    return news

def write_csv(output_file, new_list):
    with open(output_file, 'w', newline='', encoding='utf-8') as file:
        write_line = csv.DictWriter(file, fieldnames=['data', 'category', 'title'])
        write_line.writeheader()
        write_line.writerows(new_list)
        
        
def main():
    input_file = 'data/input.txt'
    output_file = 'output/news.csv'
    
    read_file = path_file(input_file)
    new_list = convert(read_file)
    write_csv(output_file, new_list)
    print(f'Конвертація завершена')
    
if __name__ == "__main__":
    main()


