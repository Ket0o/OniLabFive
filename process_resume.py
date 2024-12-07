import yaml

def load_resume(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return yaml.safe_load(file)

def get_skills_with_level(resume, level):
    return [skill['name'] for skill in resume.get('skills', []) if skill.get('level') == level]

def get_current_courses(resume):
    return resume.get('current_courses', [])

if __name__ == "__main__":
    resume_data = load_resume('resume.yaml')

    # Пример вывода всех навыков с уровнем владения "medium"
    medium_skills = get_skills_with_level(resume_data, 'medium')
    print("Навыки с уровнем владения medium:", medium_skills)

    # Пример вывода всех программ на которых я прохожу обучение в данный момент
    current_courses = get_current_courses(resume_data)
    print("Текущие курсы:", current_courses)
