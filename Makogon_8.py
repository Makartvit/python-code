import requests


class Candidate:

    def __init__(self, full_name, email, tech_stack, main_skill, main_skill_grade):
        self.full_name = full_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @classmethod
    def generate_candidates(cls, link_to_file):
        candidates_list = []

        response = requests.get(link_to_file)
        if response.status_code == 200:
            text_content = response.text
            lines = text_content.split('\n')
            for line in lines:
                if line:
                    string = line.split(',')
                    candidate_1 = cls(*string)
                    candidates_list.append(candidate_1)

                    print(string)

            return candidates_list

        elif response.status_code == 404:
            print("Not Found.")

    def __str__(self):
        return (f"Full Name: {self.full_name}\nEmail: {self.email}\nTech Stack: {self.tech_stack}\n"
                f"Main Skill: {self.main_skill}\nMain Skill Grade: {self.main_skill_grade}\n")


source = 'https://bitbucket.org/ivnukov/lesson2/raw/4f59074e6fbb552398f87636b5bf089a1618da0a/candidates.csv'
candidates = Candidate.generate_candidates(source)
for candidate in candidates:
    print("Candidate Information:")
    print(candidate)
