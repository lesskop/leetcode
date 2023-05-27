from typing import Literal
from dataclasses import dataclass

README_FILE = 'README.MD'
LEETCODE_PROBLEMS_URL = 'https://leetcode.com/problems'
LANG_TO_EXT = {'Python': 'py', 'SQL': 'sql', 'JavaScript': 'js', 'TypeScript': 'ts'}


@dataclass(frozen=True)
class Problem:
    number: int
    title: str
    language: Literal['Python', 'SQL', 'JavaScript', 'TypeScript']
    difficulty: Literal['Easy', 'Medium', 'Hard']
