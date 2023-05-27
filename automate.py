from pathlib import Path

from config import Problem, README_FILE, LANG_TO_EXT, LEETCODE_PROBLEMS_URL


def create_empty_file(p: Problem) -> None:
    ext = LANG_TO_EXT.get(p.language)
    file = f"{p.number}_{p.title.lower().replace(' ', '_')}.{ext}"
    path = Path(p.language.lower()) / file

    try:
        path.touch(exist_ok=False)
    except FileExistsError:
        print(f'File "{path}" already exists')


def get_leetcode_problem_link(p: Problem) -> str:
    return f"[{p.title}]({LEETCODE_PROBLEMS_URL}/{p.title.lower().replace(' ', '-')}/)"


def get_solution_link(p: Problem) -> str:
    lang = p.language
    ext = LANG_TO_EXT.get(lang)
    solution_file = f"{p.number}_{p.title.lower().replace(' ', '_')}.{ext}"
    return f"[{lang}]({lang.lower()}/{solution_file})"


def get_table_row_for_solution(p: Problem) -> str:
    return f"\n|{p.number}|{get_leetcode_problem_link(p)}|{get_solution_link(p)}|{p.difficulty}|"


def add_new_row_to_readme(row: str) -> None:
    with open(README_FILE, 'a') as file:
        file.write(row)


if __name__ == '__main__':
    problem = Problem(
        number=577,
        title='Employee Bonus',
        language='SQL',
        difficulty='Easy'
    )

    create_empty_file(problem)
    add_new_row_to_readme(get_table_row_for_solution(problem))
