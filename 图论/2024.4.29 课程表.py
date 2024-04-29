class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        prequest = [[] for i in range(numCourses)]
        indegree = [0 for i in range(numCourses)]
        learnLessonList = []
        self.learnLesson = 0
        for i in prerequisites:
            prequest[i[1]].append(i[0])
            indegree[i[0]] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                self.learnLesson += 1
                learnLessonList.append(i)

        def dfs(i):

            while prequest[i]:
                n = prequest[i].pop()
                indegree[n] -= 1
                if indegree[n] == 0:
                    self.learnLesson += 1
                    dfs(n)

        for i in range(numCourses):
            if indegree[i] == 0:
                dfs(i)
        return self.learnLesson == numCourses
