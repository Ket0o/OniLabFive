import yaml
import json

def load_yaml(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def save_json(data, file_path):
    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    yaml_file = 'resume.yaml'
    json_file = 'resume.json'

    # Загружаем данные из YAML
    resume_data = load_yaml(yaml_file)

    # Сохраняем данные в JSON
    save_json(resume_data, json_file)

    print(f"Конвертация завершена: {yaml_file} -> {json_file}")
