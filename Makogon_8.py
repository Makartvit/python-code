class Candidate:

    def __init__(self, first_name, last_name, email, tech_stack, main_skill, main_skill_grade):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.tech_stack = tech_stack
        self.main_skill = main_skill
        self.main_skill_grade = main_skill_grade

    @property
    def first_name_last_name(self):
        return self.first_name + " " + self.last_name

    @classmethod
    def generate_candidates(cls, link_to_file):




