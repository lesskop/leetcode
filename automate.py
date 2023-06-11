from pathlib import Path

from config import Problem, README_FILE, LANG_TO_EXT, LEETCODE_PROBLEMS_URL


class Solution:
    def __init__(self, p: Problem) -> None:
        self.number = p.number

        self.extension = LANG_TO_EXT.get(p.language)
        self.filename = f"{p.number}_{p.title.lower().replace(' ', '_')}.{self.extension}"
        self.filepath = Path(p.language.lower()) / self.filename

        self.problem_md_link = f"[{p.title}]({LEETCODE_PROBLEMS_URL}/{p.title.lower().replace(' ', '-')}/)"
        self.solution_md_link = f"[{p.language}]({self.filepath})"

        self.md_table_row = f"|{p.number}|{self.problem_md_link}|{self.solution_md_link}|{p.difficulty}|"

    def add_solution_to_readme(self) -> None:
        with open(README_FILE, "r") as f:
            contents = f.readlines()

        contents.insert(self.get_readme_insert_row_index(), self.md_table_row + '\n')

        with open(README_FILE, "w") as f:
            f.writelines(contents)

    def get_readme_insert_row_index(self) -> int:
        with open(README_FILE, "r") as f:
            contents = f.readlines()

        row_start_index = 9
        nums = [int(row.split('|')[1]) for _, row in enumerate(contents[row_start_index:])]

        if self.number > nums[-1]:
            return len(nums) + row_start_index + 1

        for i in range(len(nums) - 1):
            if nums[i] < self.number < nums[i + 1]:
                return i + row_start_index + 1

    def create_empty_file(self) -> None:
        try:
            self.filepath.touch(exist_ok=False)
        except FileExistsError:
            print(f'File "{self.filepath}" already exists')


if __name__ == '__main__':
    problem = Problem(
        number=7878,
        title='7878',
        language='Python',
        # language='SQL',
        difficulty='Easy',
        # difficulty='Medium',
        # difficulty='Hard',
    )

    solution = Solution(problem)

    solution.add_solution_to_readme()
    solution.create_empty_file()
