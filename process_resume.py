import yaml
from datetime import datetime

def load_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def get_skills_with_level(resume, level):
    return [skill['name'] for skill in resume.get('skills', []) if skill.get('level') == level]

def get_institutions_with_future_graduation(resume):
    current_year = datetime.now().year
    return [
        edu['institution'] for edu in resume.get('education', [])
        if edu.get('graduationYear', 0) > current_year
    ]

if __name__ == "__main__":
    resume_data = load_resume('resume.yaml')

    # Пример вывода всех навыков с уровнем владения "medium"
    medium_skills = get_skills_with_level(resume_data, 'medium')
    print("Навыки с уровнем владения medium:", medium_skills)

    # Пример вывода учебных заведений с датой завершения больше текущего года
    future_institutions = get_institutions_with_future_graduation(resume_data)
    print("Учебные заведения с датой завершения больше текущего года:", future_institutions)
