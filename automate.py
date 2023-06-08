from pathlib import Path

from config import Problem, README_FILE, LANG_TO_EXT, LEETCODE_PROBLEMS_URL


class Solution:
    def __init__(self, p: Problem) -> None:
        self.extension = LANG_TO_EXT.get(p.language)
        self.filename = f"{p.number}_{p.title.lower().replace(' ', '_')}.{self.extension}"
        self.filepath = Path(p.language.lower()) / self.filename

        self.problem_md_link = f"[{p.title}]({LEETCODE_PROBLEMS_URL}/{p.title.lower().replace(' ', '-')}/)"
        self.solution_md_link = f"[{p.language}]({self.filepath})"

        self.md_table_row = f"\n|{p.number}|{self.problem_md_link}|{self.solution_md_link}|{p.difficulty}|"

    def add_new_row_to_readme(self) -> None:
        if not self.filepath.exists():
            with open(README_FILE, 'a') as file:
                file.write(self.md_table_row)

    def create_empty_file(self) -> None:
        try:
            self.filepath.touch(exist_ok=False)
        except FileExistsError:
            print(f'File "{self.filepath}" already exists')


if __name__ == '__main__':
    problem = Problem(
        number=0,
        title='title',
        language='Python',
        # language='SQL',
        difficulty='Easy',
        # difficulty='Medium',
        # difficulty='Hard',
    )

    solution = Solution(problem)

    solution.add_new_row_to_readme()
    solution.create_empty_file()
