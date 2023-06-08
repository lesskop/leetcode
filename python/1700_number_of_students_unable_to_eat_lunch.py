class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:

        repeat = 0

        while students and sandwiches:

            if repeat > len(students):
                return len(students)

            if students[0] == sandwiches[0]:
                students.pop(0)
                sandwiches.pop(0)
                repeat = 0
            else:
                students.append(students.pop(0))
                repeat += 1

        return 0
