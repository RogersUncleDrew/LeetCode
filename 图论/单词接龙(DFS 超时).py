class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1

        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)

        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        endId = wordId[endWord]
        minLength = float("inf")
        visited = [False for i in range(len(wordId))]
        validId = [wordId[i] for i in wordList]
        def dfs(id, length):
            visited[id] = True
            nonlocal minLength
            if id == endId:
                minLength = min(minLength, length)
                return
            for nxtId in edge[id]:
                if not visited[nxtId]:
                    dfs(nxtId, length+(1 if nxtId in validId else 0))
            visited[id] = False
        dfs(wordId[beginWord], 1)
        return minLength
